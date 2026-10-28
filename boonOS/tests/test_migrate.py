"""Migration preserves personal content and refuses ambiguous/destructive paths."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unicodedata
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1]/"scripts/migrate.py"
spec = importlib.util.spec_from_file_location("boonos_migrate", SCRIPT)
migrate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migrate)

OLD = b"---\nname: sample\ndescription: Older stock skill\n---\nOld workflow\n"
NEW = b"---\nname: sample\ndescription: Updated stock skill\n---\nNew workflow\n"
LOCAL = b"---\nname: sample\ndescription: Personal workflow\n---\nKeep my changes\n"


class MigrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=str(Path(tempfile.gettempdir()).resolve()))
        self.base = Path(self.tmp.name)
        self.source = self.base/"old"
        self.template = self.base/"release"
        self.dest = self.base/"new"
        self.source.mkdir()
        self.template.mkdir()
        self.write(self.template, "README.md", b"Current release\n")
        self.write(self.template, "01. SISTEMA/CONTEXTO.md", b"# New context\n")
        self.write(self.template, "01. SISTEMA/PERFIL.yaml", b"new_field: unset\n")
        self.write(self.template, "01. SISTEMA/CATALOGO.json", b'{"skills": ["sample"]}\n')
        self.write(self.template, ".gitignore", b".env\n")
        for prefix in migrate.SKILL_ROOTS:
            self.write(self.template, prefix+"/sample/SKILL.md", NEW)
        import hashlib
        baseline = {"schema_version": 1, "versions": {"main": {"sample": {"SKILL.md": hashlib.sha256(OLD).hexdigest()}}, "beta20": {}}}
        self.write(self.template, "scripts/migration-baselines.json", json.dumps(baseline).encode())
        self.seal()

    def tearDown(self):
        self.tmp.cleanup()

    @staticmethod
    def write(root, relative, data):
        path = root/relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def seal(self):
        files = {p.relative_to(self.template).as_posix(): migrate.sha(p) for p in self.template.rglob("*") if p.is_file() and p.name != "distribution.json"}
        self.write(self.template, "distribution.json", json.dumps({"schema_version": 1, "version": "2.1-test", "files": files}).encode())

    def plan(self, **kwargs):
        return migrate.make_plan(self.source, self.dest, self.template, **kwargs)

    def test_preview_is_read_only_and_apply_preserves_personal_data(self):
        personal = {"_00. TRABALHO/brief.md": b"Personal brief", "_01. SISTEMA/PERFIL.yaml": b"owner: personal\n", "_01. SISTEMA/CONTEXTO.md": b"My context\n", "_01. SISTEMA/ONBOARDING.md": b"Paused", "_01. SISTEMA/SKILLSET.md": b"My favorites", "_01. SISTEMA/DECISOES.md": b"My decisions", "_02. MEMORIA/note.md": b"Keep this", "_03. DOCS/source.txt": b"Source", "_99. OLD/history.md": b"History", "CLAUDE.md": b"Old root truth\n"}
        for rel, data in personal.items(): self.write(self.source, rel, data)
        old = migrate.inventory(self.source)[0]
        release = migrate.inventory(self.template)[0]
        plan = self.plan()
        self.assertFalse(self.dest.exists())
        self.assertEqual(migrate.inventory(self.source)[0], old)
        receipt = migrate.perform(plan)
        self.assertEqual((self.dest/"01. SISTEMA/PERFIL.yaml").read_bytes(), b"owner: personal\n")
        self.assertEqual((self.dest/"00. TRABALHO/brief.md").read_bytes(), b"Personal brief")
        self.assertEqual((self.dest/"99. ARQUIVO/history.md").read_bytes(), b"History")
        self.assertEqual((self.dest/migrate.LEGACY/"CLAUDE.md").read_bytes(), personal["CLAUDE.md"])
        context = (self.dest/"01. SISTEMA/CONTEXTO.md").read_bytes()
        self.assertTrue(context.startswith(b"My context\n"))
        self.assertIn(b"LEGADO/CLAUDE.md", context)
        self.assertEqual(migrate.inventory(self.source)[0], old)
        self.assertEqual(migrate.inventory(self.template)[0], release)
        self.assertEqual(receipt["validation"]["source_unchanged"], "passed")

    def test_beta_paths_private_files_and_exclusions(self):
        for rel, data in {"00. TRABALHO/job.md": b"Job", "04. GESTAO/finance.md": b"Budget", "03. DOCS/_PRIVADO/local.txt": b"Private local data", "99. OLD/old.txt": b"Past", "scratch.txt": b"Unclassified", ".env": b"DO_NOT_COPY=secret", "nested/.env.local": b"SECRET", ".git/config": b"Git", "node_modules/package/data": b"Cache", ".gitignore": b"!**/98. PRIVADO/\n"}.items(): self.write(self.source, rel, data)
        receipt = migrate.perform(self.plan())
        self.assertEqual((self.dest/"03. DOCS/98. PRIVADO/local.txt").read_bytes(), b"Private local data")
        self.assertEqual((self.dest/"04. GESTÃO/finance.md").read_bytes(), b"Budget")
        self.assertEqual((self.dest/migrate.LEGACY/"scratch.txt").read_bytes(), b"Unclassified")
        self.assertFalse(any(p.name.startswith(".env") for p in self.dest.rglob("*")))
        excluded = {r["path"] for r in receipt["excluded"]}
        self.assertIn(".env", excluded)
        self.assertIn(".git/", excluded)
        self.assertNotIn("DO_NOT_COPY", json.dumps(receipt))
        ignore = (self.dest/".gitignore").read_text()
        self.assertGreater(ignore.rfind("**/98. PRIVADO/"), ignore.find("!**/98. PRIVADO/"))

    def test_known_stock_skill_uses_new_release(self):
        for prefix in migrate.SKILL_ROOTS: self.write(self.source, prefix+"/sample/SKILL.md", OLD)
        receipt = migrate.perform(self.plan())
        for prefix in migrate.SKILL_ROOTS:
            self.assertEqual((self.dest/prefix/"sample/SKILL.md").read_bytes(), NEW)
        self.assertEqual(receipt["skills"][0]["action"], "use_new_release")

    @unittest.skipUnless(shutil.which("git"), "Git needed to verify actual ignore behavior")
    def test_rooted_gitignore_still_protects_files_after_root_rename(self):
        self.write(self.source, ".gitignore", b"/_03. DOCS/contract-private.md\n/_0?. DOCS/notes/*.md\n!/_03. DOCS/notes/share.md\n")
        for name in ("contract-private.md", "notes/share.md", "public.txt"):
            self.write(self.source, "_03. DOCS/" + name, b"Personal content")
        def git(root, *args):
            return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
        self.assertEqual(git(self.source, "init", "--quiet").returncode, 0)
        self.assertEqual(git(self.source, "check-ignore", "-q", "_03. DOCS/contract-private.md").returncode, 0)
        before = migrate.inventory(self.source)[0]
        receipt = migrate.perform(self.plan())
        self.assertEqual(git(self.dest, "init", "--quiet").returncode, 0)
        for relative in ("03. DOCS/contract-private.md", "03. DOCS/notes/share.md"):
            self.assertEqual(git(self.dest, "check-ignore", "-q", relative).returncode, 0, relative)
        self.assertEqual(git(self.dest, "check-ignore", "-q", "03. DOCS/public.txt").returncode, 1)
        self.assertEqual(migrate.inventory(self.source)[0], before)
        self.assertIn("/03. DOCS/contract-private.md", receipt["remapped_ignore_rules"])

    def test_modified_skill_conflict_and_explicit_local_override(self):
        for prefix in migrate.SKILL_ROOTS: self.write(self.source, prefix+"/sample/SKILL.md", LOCAL)
        plan = self.plan()
        self.assertTrue(plan["conflicts"])
        with self.assertRaises(migrate.MigrationError): migrate.perform(plan)
        self.assertFalse(self.dest.exists())
        receipt = migrate.perform(self.plan(prefer_local=True))
        for prefix in migrate.SKILL_ROOTS:
            self.assertEqual((self.dest/prefix/"sample/SKILL.md").read_bytes(), LOCAL)
        lock = json.loads((self.dest/"skills-lock.json").read_text())
        self.assertEqual(lock["files"]["sample/SKILL.md"], migrate.sha(self.dest/".agents/skills/sample/SKILL.md"))
        self.assertEqual(receipt["skills"][0]["action"], "preserve_local_override")

    def test_personal_extension_in_one_mirror_is_preserved_in_both(self):
        self.write(self.source, ".agents/skills/personal/SKILL.md", b"Personal extension")
        migrate.perform(self.plan())
        for prefix in migrate.SKILL_ROOTS:
            self.assertEqual((self.dest/prefix/"personal/SKILL.md").read_bytes(), b"Personal extension")

    def test_divergent_source_mirrors_never_choose_a_winner(self):
        self.write(self.source, ".agents/skills/sample/SKILL.md", LOCAL)
        self.write(self.source, ".claude/skills/sample/SKILL.md", OLD)
        with self.assertRaises(migrate.MigrationError): self.plan(prefer_local=True)
        self.assertFalse(self.dest.exists())

    def test_personal_mapping_collision_aborts(self):
        self.write(self.source, "_00. TRABALHO/job.md", b"A")
        self.write(self.source, "00. TRABALHO/job.md", b"B")
        plan = self.plan()
        self.assertTrue(plan["conflicts"])
        with self.assertRaises(migrate.MigrationError): migrate.perform(plan)
        self.assertFalse(self.dest.exists())

    def test_portable_case_collision_aborts_instead_of_overwriting(self):
        self.write(self.source, "_00. TRABALHO/Job.md", b"A")
        self.write(self.source, "00. TRABALHO/job.md", b"B")
        plan = self.plan()
        self.assertTrue(plan["conflicts"])
        self.assertFalse(self.dest.exists())

    def test_generated_manifest_case_and_unicode_collision_aborts(self):
        relative = unicodedata.normalize("NFD", migrate.MANIFEST).replace("MANIFESTO.json", "manifesto.json")
        original = b'{"personal": "preserve this existing manifest"}\n'
        self.write(self.source, relative, original)
        plan = self.plan()
        self.assertTrue(plan["conflicts"])
        with self.assertRaises(migrate.MigrationError):
            migrate.perform(plan)
        self.assertFalse(self.dest.exists())
        self.assertEqual((self.source/relative).read_bytes(), original)

    def test_staging_copy_failure_leaves_source_and_destination_untouched(self):
        self.write(self.source, "_00. TRABALHO/job.md", b"Keep")
        before = migrate.inventory(self.source)[0]
        plan = self.plan()
        original_copy = migrate.shutil.copyfile
        count = 0
        def fail_during_copy(src, dst):
            nonlocal count
            count += 1
            if count == 3:
                raise OSError("Simulated full disk")
            return original_copy(src, dst)
        with patch.object(migrate.shutil, "copyfile", side_effect=fail_during_copy):
            with self.assertRaises(OSError):
                migrate.perform(plan)
        self.assertEqual(migrate.inventory(self.source)[0], before)
        self.assertFalse(self.dest.exists())
        self.assertFalse(list(self.base.glob(".boonos-migracao-*")))

    def test_worktree_git_pointer_is_excluded(self):
        self.write(self.source, ".git", b"gitdir: /unrelated/worktree/metadata")
        plan = self.plan()
        self.assertIn(".git", [item["path"] for item in plan["excluded"]])
        self.assertFalse(any(item["source"] == ".git" for item in plan["copies"]))
        migrate.perform(plan)
        self.assertFalse((self.dest/migrate.LEGACY/".git").exists())

    def test_old_catalog_is_archived_and_release_catalog_remains_current(self):
        self.write(self.source, "_01. SISTEMA/CATALOGO.json", b'{"personal":"old schema"}')
        migrate.perform(self.plan())
        self.assertEqual((self.dest/"01. SISTEMA/CATALOGO.json").read_bytes(), (self.template/"01. SISTEMA/CATALOGO.json").read_bytes())
        self.assertEqual((self.dest/migrate.LEGACY/"_01. SISTEMA/CATALOGO.json").read_bytes(), b'{"personal":"old schema"}')

    def test_rerun_and_existing_empty_directory_are_refused(self):
        migrate.perform(self.plan())
        with self.assertRaises(migrate.MigrationError): self.plan()
        empty = self.base/"empty"
        empty.mkdir()
        with self.assertRaises(migrate.MigrationError): migrate.make_plan(self.source, empty, self.template)

    def test_source_drift_prevents_promotion(self):
        self.write(self.source, "_00. TRABALHO/job.md", b"Before")
        plan = self.plan()
        self.write(self.source, "_00. TRABALHO/job.md", b"New user edit")
        with self.assertRaises(migrate.MigrationError): migrate.perform(plan)
        self.assertFalse(self.dest.exists())
        self.assertEqual((self.source/"_00. TRABALHO/job.md").read_bytes(), b"New user edit")

    def test_release_hash_failure_leaves_destination_absent(self):
        self.write(self.template, "README.md", b"Unsealed edit")
        with self.assertRaises(migrate.MigrationError): self.plan()
        self.assertFalse(self.dest.exists())

    def test_symlink_source_file_root_and_destination_parent_are_rejected(self):
        outside = self.base/"outside"
        outside.mkdir()
        (outside/"keep.txt").write_text("Outside")
        try:
            (self.source/"link").symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            self.skipTest(str(exc))
        with self.assertRaises(migrate.MigrationError): self.plan()
        (self.source/"link").unlink()
        alias = self.base/"alias"
        alias.symlink_to(self.source, target_is_directory=True)
        with self.assertRaises(migrate.MigrationError): migrate.make_plan(alias, self.dest, self.template)
        parent = self.base/"parent-link"
        parent.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(migrate.MigrationError): migrate.make_plan(self.source, parent/"new", self.template)
        self.assertEqual((outside/"keep.txt").read_text(), "Outside")

    def test_overlap_and_manifest_traversal_are_rejected(self):
        for destination in (self.source/"new", self.template/"new"):
            with self.assertRaises(migrate.MigrationError): migrate.make_plan(self.source, destination, self.template)
        manifest = json.loads((self.template/"distribution.json").read_text())
        manifest["files"]["../escape"] = "0"*64
        self.write(self.template, "distribution.json", json.dumps(manifest).encode())
        with self.assertRaises(migrate.MigrationError): self.plan()


if __name__ == "__main__":
    unittest.main()
