"""Behavioral checks for bounded patches, drift protection and recovery."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "improve.py"
module_spec = importlib.util.spec_from_file_location("boonos_improve", SCRIPT)
improve = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(improve)


class ImprovementTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.ws = improve.Workspace(self.root)
        self.ws.write("feedback.md", b"A briefing missed its audience.\n")
        self.ws.write("checklist.md", b"Confirm objective.\n")

    def tearDown(self):
        self.temp.cleanup()

    def spec(self, **overrides):
        value = {
            "title": "Audience question",
            "evidence": ["feedback.md"],
            "changes": [{"path": "checklist.md", "content": "Confirm objective.\nConfirm audience.\n"}],
            "checks": [{"type": "contains", "path": "checklist.md", "text": "Confirm audience."}],
        }
        value.update(overrides)
        self.ws.write("proposal.json", improve.json_bytes(value))
        return value

    def prepare(self, **overrides):
        self.spec(**overrides)
        return improve.prepare(self.ws, "proposal.json")

    def test_apply_and_rollback_preserve_original_and_record_evidence(self):
        original = self.ws.read("checklist.md")
        record = self.prepare()
        self.assertEqual(self.ws.read("checklist.md"), original)
        applied = improve.apply(self.ws, record["run_id"])
        self.assertIn(b"Confirm audience.", self.ws.read("checklist.md"))
        self.assertEqual(applied["status"], "applied")
        self.assertEqual(applied["functional_evaluation"]["status"], "not_evaluated")
        self.assertEqual(applied["evidence"][0]["sha256"], improve.digest(self.ws.read("feedback.md")))
        result = improve.rollback(self.ws, record["run_id"])
        self.assertEqual(result["status"], "rolled_back")
        self.assertEqual(self.ws.read("checklist.md"), original)

    def test_noop_records_attempt_without_rewriting_target(self):
        current = self.ws.read("checklist.md").decode()
        before = self.ws.path("checklist.md").stat().st_mtime_ns
        record = self.prepare(changes=[{"path": "checklist.md", "content": current}], checks=[{"type": "contains", "path": "checklist.md", "text": "Confirm objective."}])
        self.assertEqual(record["status"], "noop")
        self.assertEqual(improve.apply(self.ws, record["run_id"])["status"], "noop")
        self.assertEqual(self.ws.path("checklist.md").stat().st_mtime_ns, before)

    def test_failed_candidate_does_not_create_history_or_mutate_target(self):
        original = self.ws.read("checklist.md")
        self.spec(checks=[{"type": "contains", "path": "checklist.md", "text": "Unmet requirement"}])
        with self.assertRaises(improve.ImprovementError):
            improve.prepare(self.ws, "proposal.json")
        self.assertEqual(self.ws.read("checklist.md"), original)
        self.assertFalse((self.root / improve.HISTORY).exists())

    def test_apply_drift_refuses_all_files_before_first_write(self):
        self.ws.write("other.md", b"Old other")
        record = self.prepare(changes=[{"path": "checklist.md", "content": "Confirm audience."}, {"path": "other.md", "content": "New other"}], checks=[{"type": "contains", "path": "checklist.md", "text": "Confirm audience."}, {"type": "contains", "path": "other.md", "text": "New other"}])
        self.ws.write("other.md", b"User edit")
        with self.assertRaises(improve.ImprovementError):
            improve.apply(self.ws, record["run_id"])
        self.assertEqual(self.ws.read("checklist.md"), b"Confirm objective.\n")
        self.assertEqual(self.ws.read("other.md"), b"User edit")

    def test_changed_evidence_requires_new_candidate(self):
        record = self.prepare()
        self.ws.write("feedback.md", b"Correction: the audience was already defined.")
        with self.assertRaises(improve.ImprovementError):
            improve.apply(self.ws, record["run_id"])
        self.assertEqual(self.ws.read("checklist.md"), b"Confirm objective.\n")

    def test_rollback_preserves_subsequent_user_edit(self):
        record = self.prepare()
        improve.apply(self.ws, record["run_id"])
        self.ws.write("checklist.md", b"New user decision")
        with self.assertRaises(improve.ImprovementError):
            improve.rollback(self.ws, record["run_id"])
        self.assertEqual(self.ws.read("checklist.md"), b"New user decision")

    def test_new_file_rollback_removes_only_created_file(self):
        record = self.prepare(changes=[{"path": "local/new.md", "content": "New checklist"}], checks=[{"type": "contains", "path": "local/new.md", "text": "checklist"}])
        improve.apply(self.ws, record["run_id"])
        self.ws.write("local/user.md", b"Keep me")
        improve.rollback(self.ws, record["run_id"])
        self.assertFalse((self.root / "local/new.md").exists())
        self.assertEqual(self.ws.read("local/user.md"), b"Keep me")

    def test_write_failure_restores_prior_files_and_records_failure(self):
        self.ws.write("other.md", b"Before other")
        record = self.prepare(changes=[{"path": "checklist.md", "content": "Confirm audience."}, {"path": "other.md", "content": "After other"}], checks=[{"type": "contains", "path": "checklist.md", "text": "Confirm audience."}, {"type": "contains", "path": "other.md", "text": "After other"}])
        write = self.ws.write
        def fail_second(path, data):
            if path == "other.md":
                raise OSError("Simulated unavailable target")
            return write(path, data)
        with patch.object(self.ws, "write", side_effect=fail_second):
            with self.assertRaises(improve.ImprovementError):
                improve.apply(self.ws, record["run_id"])
        self.assertEqual(self.ws.read("checklist.md"), b"Confirm objective.\n")
        self.assertEqual(self.ws.read("other.md"), b"Before other")
        loaded, _, _ = improve.load_record(self.ws, record["run_id"])
        self.assertEqual(loaded["status"], "failed")
        self.assertEqual(loaded["stages"][-1]["status"], "passed")

    def test_snapshot_tamper_refuses_apply(self):
        record = self.prepare()
        self.ws.write(f"{improve.HISTORY}/{record['run_id']}/00.after", b"Tampered")
        with self.assertRaises(improve.ImprovementError):
            improve.apply(self.ws, record["run_id"])
        self.assertEqual(self.ws.read("checklist.md"), b"Confirm objective.\n")

    def test_traversal_absolute_and_reserved_targets_rejected(self):
        for target in ("../escape.md", "/tmp/escape.md", "C:/escape.md", "a/../../escape.md", ".git/config", improve.HISTORY + "/record.json"):
            with self.subTest(target=target):
                self.spec(changes=[{"path": target, "content": "X"}], checks=[{"type": "contains", "path": target, "text": "X"}])
                with self.assertRaises(improve.ImprovementError):
                    improve.prepare(self.ws, "proposal.json")

    def test_symlink_target_and_evidence_are_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / "file.md"
            external.write_text("Outside")
            try:
                (self.root / "linked").symlink_to(outside, target_is_directory=True)
            except OSError as exc:
                self.skipTest("Symlink creation unavailable: " + str(exc))
            for values in ({"evidence": ["linked/file.md"]}, {"changes": [{"path": "linked/file.md", "content": "Changed"}], "checks": [{"type": "contains", "path": "linked/file.md", "text": "Changed"}]}):
                self.spec(**values)
                with self.assertRaises(improve.ImprovementError):
                    improve.prepare(self.ws, "proposal.json")
            self.assertEqual(external.read_text(), "Outside")

    def test_commands_are_never_a_check_type(self):
        self.spec(checks=[{"type": "shell", "path": "checklist.md", "command": "touch INJECTED"}])
        with self.assertRaises(improve.ImprovementError):
            improve.prepare(self.ws, "proposal.json")
        self.assertFalse((self.root / "INJECTED").exists())

    def test_json_and_negative_checks_fail_on_invalid_candidate(self):
        for checks in ([{"type": "json", "path": "checklist.md"}], [{"type": "not_contains", "path": "checklist.md", "text": "audience"}]):
            self.spec(checks=checks)
            with self.assertRaises(improve.ImprovementError):
                improve.prepare(self.ws, "proposal.json")

    def test_lock_prevents_overlapping_run(self):
        with self.ws.locked():
            with self.assertRaises(improve.ImprovementError):
                with self.ws.locked():
                    self.fail("Second execution acquired lock")
        self.assertFalse((self.root / improve.LOCK).exists())

    def test_cli_requires_explicit_apply_and_reports_status(self):
        self.spec()
        command = [sys.executable, str(SCRIPT), "--root", str(self.root)]
        prepared = subprocess.run(command + ["prepare", "--spec", "proposal.json"], capture_output=True, text=True, check=True)
        run_id = json.loads(prepared.stdout)["run_id"]
        denied = subprocess.run(command + ["apply", run_id], capture_output=True, text=True)
        self.assertNotEqual(denied.returncode, 0)
        self.assertEqual(self.ws.read("checklist.md"), b"Confirm objective.\n")
        applied = subprocess.run(command + ["apply", run_id, "--apply"], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(applied.stdout)["status"], "applied")
        status = subprocess.run(command + ["status", run_id], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(status.stdout)["functional_evaluation"], "not_evaluated")


if __name__ == "__main__":
    unittest.main()
