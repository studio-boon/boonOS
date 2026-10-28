#!/usr/bin/env python3
"""Prepare, apply and roll back small authorized UTF-8 changes; stdlib only.

No commands or scheduler are executed. See APRENDIZADO.md for the spec contract.
"""
from __future__ import annotations

import argparse
import contextlib
import difflib
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import tempfile
from datetime import datetime, timezone
import uuid

HISTORY = "01. SISTEMA/01. EVOLUÇÃO"
LOCK = ".boonos-improve.lock"
MAX_FILE = 2_000_000
MAX_CHANGES = 20


class ImprovementError(Exception):
    pass


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest() if data is not None else None


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


class Workspace:
    def __init__(self, root):
        requested = Path(root).absolute()
        if requested.is_symlink() or getattr(requested, "is_junction", lambda: False)():
            raise ImprovementError("A raiz não pode ser um link/junction.")
        self.root = requested.resolve(strict=True)
        if not self.root.is_dir():
            raise ImprovementError("A raiz deve ser um diretório existente.")

    def path(self, relative, target=False):
        if not isinstance(relative, str) or not relative or "\\" in relative:
            raise ImprovementError("Caminho deve ser relativo, com separadores /.")
        parts = relative.split("/")
        if any(p in ("", ".", "..") or ":" in p for p in parts):
            raise ImprovementError("Caminho vazio, absoluto ou com traversal não permitido.")
        if PurePosixPath(relative).is_absolute() or parts[0] == ".git":
            raise ImprovementError("Caminho fora do escopo permitido.")
        if target and (relative == LOCK or relative == HISTORY or relative.startswith(HISTORY + "/")):
            raise ImprovementError("Uma melhoria não pode editar seu próprio histórico/lock.")
        current = self.root
        for part in parts:
            current = current / part
            if current.is_symlink() or getattr(current, "is_junction", lambda: False)():
                raise ImprovementError("Links/junctions não são permitidos: " + relative)
            if current.exists() and not (current.is_dir() or current.is_file()):
                raise ImprovementError("Arquivo especial não permitido: " + relative)
        try:
            current.resolve().relative_to(self.root)
        except ValueError as exc:
            raise ImprovementError("Caminho escapa da raiz: " + relative) from exc
        return current

    def read(self, relative, missing=False):
        path = self.path(relative)
        if not path.exists() and missing:
            return None
        if not path.is_file():
            raise ImprovementError("Arquivo regular ausente: " + relative)
        if path.stat().st_size > MAX_FILE:
            raise ImprovementError("Arquivo excede limite de 2 MB: " + relative)
        flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
        with os.fdopen(os.open(path, flags), "rb") as handle:
            if not stat.S_ISREG(os.fstat(handle.fileno()).st_mode):
                raise ImprovementError("Arquivo especial não permitido.")
            data = handle.read(MAX_FILE + 1)
        if len(data) > MAX_FILE:
            raise ImprovementError("Arquivo excede limite de 2 MB.")
        return data

    def write(self, relative, data):
        path = self.path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path = self.path(relative)
        previous_mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o600
        fd, tmp = tempfile.mkstemp(prefix=".boonos-", dir=path.parent)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            os.chmod(tmp, previous_mode)
            self.path(relative)
            os.replace(tmp, path)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)

    def remove(self, relative):
        self.path(relative).unlink()

    @contextlib.contextmanager
    def locked(self):
        path = self.path(LOCK)
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError as exc:
            raise ImprovementError("Outra execução possui o lock. Após uma interrupção, confira o processo antes de remover o lock.") from exc
        try:
            with os.fdopen(fd, "w") as handle:
                handle.write(str(os.getpid()))
            yield
        finally:
            path.unlink()


def decode(data, label):
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ImprovementError("UTF-8 obrigatório: " + label) from exc


def parse_json(data, label):
    try:
        return json.loads(decode(data, label))
    except ValueError as exc:
        raise ImprovementError("JSON inválido: " + label) from exc


def validate_checks(ws, checks, known):
    if not isinstance(checks, list) or not checks:
        raise ImprovementError("Declare pelo menos uma checagem de integridade.")
    for check in checks:
        if not isinstance(check, dict) or check.get("type") not in ("contains", "not_contains", "json"):
            raise ImprovementError("Checagem desconhecida; comandos executáveis não são aceitos.")
        ws.path(check.get("path"), target=True)
        if check["path"] not in known:
            raise ImprovementError("Checagens devem se referir aos arquivos alterados.")
        if check["type"] != "json" and (not isinstance(check.get("text"), str) or not check["text"]):
            raise ImprovementError("Checagem textual exige text não vazio.")
    if set(known) != {check["path"] for check in checks}:
        raise ImprovementError("Cada arquivo alterado precisa de uma checagem.")


def evaluate(checks, contents):
    result = []
    for check in checks:
        content = decode(contents[check["path"]], check["path"])
        kind = check["type"]
        if kind == "json":
            try:
                json.loads(content)
                passed = True
            except ValueError:
                passed = False
        else:
            contains = check["text"] in content
            passed = contains if kind == "contains" else not contains
        result.append({"path": check["path"], "type": kind, "status": "passed" if passed else "failed"})
    return result


def save_record(ws, record):
    ws.write(f"{HISTORY}/{record['run_id']}/registro.json", json_bytes(record))


def stage(record, name, status, **details):
    record["stages"].append({"stage": name, "status": status, "at": now(), **details})
    record["updated_at"] = now()


def prepare(ws, spec_path):
    spec = parse_json(ws.read(spec_path), spec_path)
    if not isinstance(spec, dict) or not isinstance(spec.get("title"), str) or not spec["title"].strip():
        raise ImprovementError("Spec exige title não vazio.")
    evidence = spec.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        raise ImprovementError("Declare ao menos um arquivo de evidência.")
    evidence_records = []
    for path in evidence:
        evidence_records.append({"path": path, "sha256": digest(ws.read(path))})
    changes = spec.get("changes")
    if not isinstance(changes, list) or not 1 <= len(changes) <= MAX_CHANGES:
        raise ImprovementError("Declare de 1 a 20 pequenas alterações.")
    before, after, entries = {}, {}, []
    for index, change in enumerate(changes):
        if not isinstance(change, dict) or not isinstance(change.get("content"), str):
            raise ImprovementError("Cada alteração exige path e content UTF-8.")
        path = change.get("path")
        ws.path(path, target=True)
        if path in after:
            raise ImprovementError("Arquivo duplicado no spec: " + path)
        original = ws.read(path, missing=True)
        if original is not None:
            decode(original, path)
        proposed = change["content"].encode("utf-8")
        if len(proposed) > MAX_FILE:
            raise ImprovementError("Alteração excede 2 MB.")
        before[path], after[path] = original, proposed
        entries.append({"path": path, "before_sha256": digest(original), "after_sha256": digest(proposed), "before_file": f"{index:02d}.before" if original is not None else None, "after_file": f"{index:02d}.after"})
    checks = spec.get("checks")
    validate_checks(ws, checks, after)
    results = evaluate(checks, after)
    if any(r["status"] == "failed" for r in results):
        raise ImprovementError("O candidato falhou na integridade declarada; nenhum arquivo foi alterado.")
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "-" + uuid.uuid4().hex[:12]
    record = {"schema_version": 1, "run_id": run_id, "title": spec["title"], "created_at": now(), "status": "noop" if before == after else "prepared", "evidence": evidence_records, "changes": entries, "checks": checks, "stages": [], "functional_evaluation": {"status": "not_evaluated", "note": "Checagens de integridade não comprovam melhora funcional; registrar caso e rubrica separadamente."}}
    stage(record, "evidence", "passed")
    stage(record, "prepare", record["status"])
    stage(record, "integrity", "passed", checks=results)
    base = f"{HISTORY}/{run_id}"
    patches = []
    for entry in entries:
        path = entry["path"]
        if entry["before_file"]:
            ws.write(f"{base}/{entry['before_file']}", before[path])
        ws.write(f"{base}/{entry['after_file']}", after[path])
        patches.extend(difflib.unified_diff(decode(before[path] or b"", path).splitlines(keepends=True), decode(after[path], path).splitlines(keepends=True), fromfile=path + " (antes)", tofile=path + " (candidato)"))
    ws.write(f"{base}/alteracoes.diff", "".join(patches).encode("utf-8"))
    save_record(ws, record)
    return record


def load_record(ws, run_id):
    if not re.fullmatch(r"\d{8}T\d{6}-[0-9a-f]{12}", run_id):
        raise ImprovementError("run_id inválido.")
    record = parse_json(ws.read(f"{HISTORY}/{run_id}/registro.json"), "registro")
    if record.get("run_id") != run_id or record.get("schema_version") != 1:
        raise ImprovementError("Registro incompatível.")
    before, after = {}, {}
    changes = record.get("changes")
    if not isinstance(changes, list) or not 1 <= len(changes) <= MAX_CHANGES:
        raise ImprovementError("Registro sem alterações válidas.")
    for i, entry in enumerate(changes):
        path = entry["path"]
        ws.path(path, target=True)
        if path in after or entry["after_file"] != f"{i:02d}.after" or entry["before_file"] not in (None, f"{i:02d}.before"):
            raise ImprovementError("Registro de arquivos inválido.")
        before[path] = ws.read(f"{HISTORY}/{run_id}/{entry['before_file']}") if entry["before_file"] else None
        after[path] = ws.read(f"{HISTORY}/{run_id}/{entry['after_file']}")
        if digest(before[path]) != entry["before_sha256"] or digest(after[path]) != entry["after_sha256"]:
            raise ImprovementError("Preimagem/candidato alterado; hashes não coincidem.")
    validate_checks(ws, record["checks"], after)
    return record, before, after


def verify_current(ws, expected):
    for path, content in expected.items():
        if digest(ws.read(path, missing=True)) != digest(content):
            raise ImprovementError("Drift detectado; preservar edição posterior: " + path)


def restore(ws, expected, replacement, paths):
    conflicts = []
    for path in reversed(paths):
        try:
            verify_current(ws, {path: expected[path]})
            if replacement[path] is None:
                ws.remove(path)
            else:
                ws.write(path, replacement[path])
        except (OSError, ImprovementError) as exc:
            conflicts.append({"path": path, "error": str(exc)})
    return conflicts


def apply(ws, run_id):
    record, before, after = load_record(ws, run_id)
    if record["status"] == "noop":
        verify_current(ws, before)
        return record
    if record["status"] != "prepared":
        raise ImprovementError("Somente um candidato prepared pode ser aplicado.")
    verify_current(ws, before)
    for item in record["evidence"]:
        if digest(ws.read(item["path"])) != item["sha256"]:
            raise ImprovementError("Evidência mudou desde a preparação: " + item["path"])
    results = evaluate(record["checks"], after)
    if any(r["status"] == "failed" for r in results):
        raise ImprovementError("Candidato falhou na validação antes da escrita.")
    touched = []
    stage(record, "authorization", "explicit_apply")
    try:
        for path, content in after.items():
            if content == before[path]:
                continue
            verify_current(ws, {path: before[path]})
            ws.write(path, content)
            touched.append(path)
        stage(record, "apply", "passed")
        current = {path: ws.read(path) for path in after}
        verify_current(ws, after)
        results = evaluate(record["checks"], current)
        if any(r["status"] == "failed" for r in results):
            raise ImprovementError("Integridade falhou após aplicar.")
        stage(record, "integrity", "passed", checks=results)
        record["status"] = "applied"
        save_record(ws, record)
    except (OSError, ImprovementError) as exc:
        conflicts = restore(ws, after, before, touched)
        record["status"] = "failed"
        stage(record, "apply", "failed", error=str(exc))
        stage(record, "automatic_restore", "partial" if conflicts else "passed", conflicts=conflicts)
        save_record(ws, record)
        raise ImprovementError(f"Aplicação falhou; restauração {'parcial' if conflicts else 'concluída'}; consulte {run_id}: {exc}") from exc
    return record


def rollback(ws, run_id):
    record, before, after = load_record(ws, run_id)
    if record["status"] != "applied":
        raise ImprovementError("Rollback exige estado applied.")
    verify_current(ws, after)
    touched = []
    try:
        for path, content in before.items():
            if content == after[path]:
                continue
            verify_current(ws, {path: after[path]})
            if content is None:
                ws.remove(path)
            else:
                ws.write(path, content)
            touched.append(path)
        verify_current(ws, before)
    except (OSError, ImprovementError) as exc:
        conflicts = restore(ws, before, after, touched)
        stage(record, "rollback", "failed", error=str(exc), recovery_conflicts=conflicts)
        record["status"] = "rollback_failed" if conflicts else "applied"
        save_record(ws, record)
        raise ImprovementError("Rollback falhou; consulte o histórico: " + run_id) from exc
    record["status"] = "rolled_back"
    stage(record, "rollback", "passed")
    save_record(ws, record)
    return record


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace existente; padrão: diretório atual")
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare", help="Preparar candidato com evidência, hashes e diff")
    prep.add_argument("--spec", required=True, help="JSON relativo ao workspace")
    for name in ("apply", "rollback", "status"):
        sub = commands.add_parser(name)
        sub.add_argument("run_id")
        if name != "status":
            sub.add_argument("--apply", action="store_true", help="Executar a alteração já autorizada")
    args = parser.parse_args(argv)
    try:
        ws = Workspace(args.root)
        if args.command in ("apply", "rollback") and not args.apply:
            raise ImprovementError("Revise o candidato e use --apply somente com autorização para esta alteração.")
        if args.command == "status":
            record, _, _ = load_record(ws, args.run_id)
        else:
            with ws.locked():
                if args.command == "prepare":
                    record = prepare(ws, args.spec)
                elif args.command == "apply":
                    record = apply(ws, args.run_id)
                else:
                    record = rollback(ws, args.run_id)
        print(json.dumps({"run_id": record["run_id"], "status": record["status"], "record": f"{HISTORY}/{record['run_id']}/registro.json", "functional_evaluation": record["functional_evaluation"]["status"]}, ensure_ascii=False))
        return 0
    except (ImprovementError, OSError, KeyError, TypeError, ValueError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
