#!/usr/bin/env python3
"""Preview or copy a legacy boonOS into a NEW directory using this release."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
import unicodedata

TEMPLATE = Path(__file__).resolve().parent.parent
ARCHIVE = "99. ARQUIVO/01. MIGRAÇÃO"
LEGACY = ARCHIVE + "/LEGADO"
MANIFEST = ARCHIVE + "/MANIFESTO.json"
ROOTS = {
    "00. TRABALHO": "00. TRABALHO", "01. SISTEMA": "01. SISTEMA",
    "02. MEMORIA": "02. MEMORIA", "03. DOCS": "03. DOCS",
    "04. GESTÃO": "04. GESTÃO", "04. GESTAO": "04. GESTÃO",
    "99. OLD": "99. ARQUIVO", "99. ARQUIVO": "99. ARQUIVO",
}
SKILL_ROOTS = (".agents/skills", ".claude/skills")
EXCLUDE_DIRS = {".git", "__pycache__", "node_modules", ".venv", "venv", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
EXCLUDE_FILES = {".git", ".DS_Store", ".boonos-improve.lock"}
PRIVATE = {"_PRIVADO", "_privado"}
IGNORE = "\n# Migração: proteção por nome, inclusive caminhos históricos.\n**/98. PRIVADO/\n**/_PRIVADO/\n**/_privado/\n**/PRIVADO.md\n.env\n.env.*\n**/.env\n**/.env.*\n01. SISTEMA/01. EVOLUÇÃO/\n99. ARQUIVO/01. MIGRAÇÃO/\n"


class MigrationError(Exception):
    pass


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def overlap(a, b):
    return a == b or a in b.parents or b in a.parents


def no_links(path):
    for item in [path, *path.parents]:
        if item.is_symlink() or getattr(item, "is_junction", lambda: False)():
            raise MigrationError("Link/junction não permitido: " + str(item))


def root_path(value, exists=True):
    path = Path(value).absolute()
    no_links(path)
    if exists and not path.is_dir():
        raise MigrationError("Diretório de origem/release ausente: " + str(path))
    return path.resolve()


def relative_path(root, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise MigrationError("Caminho relativo inválido no manifesto.")
    parts = relative.split("/")
    if any(p in ("", ".", "..") or ":" in p for p in parts):
        raise MigrationError("Traversal/caminho absoluto não permitido: " + relative)
    path = root.joinpath(*parts)
    no_links(path)
    if root != path and root not in path.resolve().parents:
        raise MigrationError("Caminho escapa da raiz: " + relative)
    return path


def sha(path):
    no_links(path)
    if not path.is_file() or not stat.S_ISREG(path.stat().st_mode):
        raise MigrationError("Arquivo regular esperado: " + str(path))
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def excluded_name(name, directory=False):
    environment = name == ".env" or name.startswith(".env.")
    return (name in EXCLUDE_DIRS or environment) if directory else name in EXCLUDE_FILES or environment or name.endswith((".pyc", ".pyo"))


def inventory(root):
    files, excluded = {}, []
    for folder, dirs, names in os.walk(root, followlinks=False):
        base = Path(folder)
        for name in list(dirs):
            path = base / name
            rel = path.relative_to(root).as_posix()
            if excluded_name(name, True):
                dirs.remove(name)
                excluded.append({"path": rel + "/", "reason": "git_or_cache"})
            else:
                no_links(path)
        for name in names:
            path = base / name
            rel = path.relative_to(root).as_posix()
            if excluded_name(name):
                excluded.append({"path": rel, "reason": "environment_or_cache"})
                continue
            no_links(path)
            files[rel] = sha(path)
    return files, excluded


def read_json(path):
    no_links(path)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise MigrationError("JSON inválido: " + str(path)) from exc


def package(template):
    manifest = read_json(template / "distribution.json")
    if manifest.get("schema_version") != 1 or not isinstance(manifest.get("version"), str) or not isinstance(manifest.get("files"), dict) or not manifest["files"]:
        raise MigrationError("distribution.json exige schema_version 1, version e files.")
    for rel, expected in manifest["files"].items():
        path = relative_path(template, rel)
        if any(p in EXCLUDE_DIRS or p in PRIVATE or p == "98. PRIVADO" or p.startswith(".env") for p in Path(rel).parts):
            raise MigrationError("Arquivo privado/cache não pode integrar a release: " + rel)
        if not re.fullmatch(r"[0-9a-f]{64}", expected or "") or sha(path) != expected:
            raise MigrationError("Release alterada/ausente: " + rel)
    return manifest


def skills_from(files):
    per_mirror = []
    for prefix in SKILL_ROOTS:
        found = {}
        for rel, digest in files.items():
            if rel.startswith(prefix + "/"):
                remainder = rel[len(prefix) + 1:]
                if "/" not in remainder:
                    raise MigrationError("Arquivo solto na raiz de skills: " + rel)
                name, within = remainder.split("/", 1)
                if not re.fullmatch(r"[a-z0-9-]+", name):
                    raise MigrationError("Nome de skill inválido: " + name)
                found.setdefault(name, {})[within] = digest
        per_mirror.append(found)
    names = set(per_mirror[0]) | set(per_mirror[1])
    result = {}
    for name in names:
        a, b = per_mirror[0].get(name), per_mirror[1].get(name)
        if a is not None and b is not None and a != b:
            raise MigrationError("Espelhos de origem divergem: " + name + ". Resolva explicitamente antes de migrar.")
        result[name] = {"files": a if a is not None else b, "prefix": SKILL_ROOTS[0] if a is not None else SKILL_ROOTS[1]}
    return result


def mapped_root(name):
    normalized = unicodedata.normalize("NFC", name)
    if normalized.startswith("_"):
        normalized = normalized[1:]
    if normalized in ROOTS:
        return ROOTS[normalized]
    short = {"00": "00. TRABALHO", "01": "01. SISTEMA", "02": "02. MEMORIA", "03": "03. DOCS", "04": "04. GESTÃO", "99": "99. ARQUIVO"}
    return short.get(normalized) if name.startswith("_") else None


def mapping(relative):
    parts = relative.split("/")
    target = mapped_root(parts[0])
    if target and len(parts) > 1:
        rest = ["98. PRIVADO" if p in PRIVATE else p for p in parts[1:]]
        if target == "01. SISTEMA" and rest[0] == "CATALOGO.json":
            return LEGACY + "/" + relative, "archive_previous_catalog"
        return "/".join([target, *rest]), "preserve_personal"
    return LEGACY + "/" + "/".join("98. PRIVADO" if p in PRIVATE else p for p in parts), "archive_unclassified"


def remapped_exclusions(data, source_files):
    """Keep positive root rules effective after renaming; never relocate negations."""
    renamed = {}
    for relative in source_files:
        name = relative.split("/", 1)[0]
        target = mapped_root(name)
        if target and target != name:
            renamed[name] = target
    if not renamed:
        return []
    try:
        lines = data.decode("utf-8-sig").splitlines()
    except UnicodeError as exc:
        raise MigrationError(".gitignore precisa ser UTF-8 para preservar exclusões após renomear pastas.") from exc
    rules = set()
    for line in lines:
        if not line or line.startswith(("#", "!")):
            continue
        head, separator, tail = line.lstrip("/").partition("/")
        if not separator:
            head = head.rstrip(" ")
        # Git permits escaped spaces. Expanding an escaped glob conservatively
        # can ignore more, never remove an exclusion inherited from the source.
        head = re.sub(r"\\(.)", r"\1", head)
        for original, target in renamed.items():
            if fnmatch.fnmatchcase(unicodedata.normalize("NFC", original), unicodedata.normalize("NFC", head)):
                rules.add("/" + target + (separator + tail if separator else ""))
    return sorted(rules)


def make_plan(source, destination, template=TEMPLATE, prefer_local=False):
    source, template = root_path(source), root_path(template)
    destination = root_path(destination, exists=False)
    if destination.exists():
        raise MigrationError("Destino já existe; escolha um diretório novo.")
    if not destination.parent.is_dir():
        raise MigrationError("A pasta pai do destino precisa existir.")
    if overlap(source, destination) or overlap(template, destination) or overlap(source, template):
        raise MigrationError("Origem, destino e release não podem se sobrepor.")
    release = package(template)
    source_files, excluded = inventory(source)
    baselines_file = template / "scripts/migration-baselines.json"
    baselines = read_json(baselines_file)
    if baselines.get("schema_version") != 1 or not isinstance(baselines.get("versions"), dict):
        raise MigrationError("Baseline de skills inválida.")
    baseline_hash = sha(baselines_file)
    legacy_skills = skills_from(source_files)
    current_skills = skills_from(release["files"])
    copies = {rel: {"from": "release", "source": rel, "target": rel, "sha256": value, "action": "release"} for rel, value in release["files"].items()}
    copies["distribution.json"] = {"from": "release", "source": "distribution.json", "target": "distribution.json", "sha256": sha(template/"distribution.json"), "action": "release_manifest"}
    conflicts, skill_decisions, preserved = [], [], {}
    release_names = {unicodedata.normalize("NFC", rel).casefold(): rel for rel in copies}
    for name, skill in sorted(legacy_skills.items()):
        matches = [version for version, items in baselines["versions"].items() if items.get(name) == skill["files"]]
        current = current_skills.get(name)
        stock = bool(matches) or (current is not None and current["files"] == skill["files"])
        if current is not None and stock:
            skill_decisions.append({"name": name, "action": "use_new_release", "matched_baselines": matches})
            continue
        if current is not None and not prefer_local:
            conflicts.append("Skill personalizada conflita com a release: " + name + "; revise ou use --prefer-local-skills conscientemente.")
            continue
        action = "preserve_local_override" if current is not None else "preserve_extension"
        skill_decisions.append({"name": name, "action": action})
        for prefix in SKILL_ROOTS:
            for rel in list(copies):
                if rel.startswith(prefix + "/" + name + "/"):
                    del copies[rel]
            for within, digest in skill["files"].items():
                target = f"{prefix}/{name}/{within}"
                copies[target] = {"from": "source", "source": f"{skill['prefix']}/{name}/{within}", "target": target, "sha256": digest, "action": action}
    for rel, digest in sorted(source_files.items()):
        if any(rel.startswith(prefix + "/") for prefix in SKILL_ROOTS) or rel == ".gitignore":
            continue
        target, action = mapping(rel)
        portable = unicodedata.normalize("NFC", target).casefold()
        target = release_names.get(portable, target)
        if portable == unicodedata.normalize("NFC", MANIFEST).casefold() or portable in preserved:
            conflicts.append("Colisão de arquivos pessoais em " + target + ": " + rel)
            continue
        preserved[portable] = rel
        copies[target] = {"from": "source", "source": rel, "target": target, "sha256": digest, "action": action}
    # Confirm no planned file is an ancestor of another planned file.
    all_targets = set(copies)
    for rel in all_targets:
        parts = rel.split("/")
        if any("/".join(parts[:i]) in all_targets for i in range(1, len(parts))):
            conflicts.append("Colisão entre arquivo e diretório: " + rel)
        relative_path(destination, rel)
    notices = ["Perfil YAML e contexto pessoal são preservados sem inferir novas respostas. Retome o onboarding para revisar campos novos.", "A origem intacta é a cópia de recuperação; esta operação não comprova backup externo ou sincronização."]
    source_ignore = (source/".gitignore").read_bytes() if ".gitignore" in source_files else b""
    ignore_rules = remapped_exclusions(source_ignore, source_files)
    if ignore_rules:
        notices.append("Exclusões Git de raízes renomeadas foram acrescentadas sem remapear negações; podem proteger arquivos extras. Revise as regras antes de versionar conteúdo pessoal.")
    if "CLAUDE.md" in source_files:
        notices.append("CLAUDE.md antigo arquivado byte a byte; revisar conteúdo antes de promover decisões para o contexto novo.")
    return {"schema_version": 1, "created_at": timestamp(), "version": release["version"], "source": str(source), "destination": str(destination), "template": str(template), "prefer_local_skills": prefer_local, "conflicts": conflicts, "excluded": excluded, "skills": skill_decisions, "notices": notices, "remapped_ignore_rules": ignore_rules, "copies": sorted(copies.values(), key=lambda x: x["target"]), "source_inventory": source_files, "release_inventory": release["files"], "baseline_sha256": baseline_hash}


def perform(plan):
    if plan["conflicts"]:
        raise MigrationError("Prévia tem conflitos; nenhum destino criado.")
    source = root_path(plan["source"])
    template = root_path(plan["template"])
    destination = root_path(plan["destination"], exists=False)
    if destination.exists():
        raise MigrationError("Destino já existe; operação recusada.")
    if inventory(source)[0] != plan["source_inventory"] or sha(template/"scripts/migration-baselines.json") != plan["baseline_sha256"]:
        raise MigrationError("Origem/baseline mudou; refaça a prévia.")
    staging = Path(tempfile.mkdtemp(prefix=".boonos-migracao-", dir=destination.parent))
    reservation = None
    try:
        mappings = []
        for entry in plan["copies"]:
            base = source if entry["from"] == "source" else template
            src = relative_path(base, entry["source"])
            if sha(src) != entry["sha256"]:
                raise MigrationError("Arquivo mudou durante a migração: " + entry["source"])
            dst = relative_path(staging, entry["target"])
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
            os.chmod(dst, stat.S_IMODE(src.stat().st_mode))
            if sha(dst) != entry["sha256"]:
                raise MigrationError("Cópia não confere: " + entry["target"])
            mappings.append(dict(entry))
        # Merge ignores, with private protection last so legacy negations cannot undo it.
        ignore_path = staging/".gitignore"
        release_ignore = ignore_path.read_bytes() if ignore_path.exists() else b""
        source_ignore = (source/".gitignore").read_bytes() if ".gitignore" in plan["source_inventory"] else b""
        remapped = "\n# Exclusões preservadas nos destinos renomeados; revisar antes de versionar.\n" + "\n".join(plan["remapped_ignore_rules"]) + "\n"
        ignore_path.write_bytes(release_ignore + b"\n# Regras preservadas da origem\n" + source_ignore + remapped.encode() + IGNORE.encode())
        generated = [{"path": ".gitignore", "action": "merge_ignore_protection", "source_sha256": plan["source_inventory"].get(".gitignore"), "sha256": sha(ignore_path)}]
        if "CLAUDE.md" in plan["source_inventory"]:
            context = staging/"01. SISTEMA/CONTEXTO.md"
            original = context.read_bytes() if context.exists() else b"# Contexto\n"
            context.parent.mkdir(parents=True, exist_ok=True)
            notice = "\n\n## Contexto anterior para revisão\n\nO CLAUDE.md da instalação anterior foi preservado em [contexto legado](<../99. ARQUIVO/01. MIGRAÇÃO/LEGADO/CLAUDE.md>). Seu conteúdo não foi promovido automaticamente para decisões atuais. Revise-o ao retomar o onboarding.\n"
            context.write_bytes(original + notice.encode())
            generated.append({"path": "01. SISTEMA/CONTEXTO.md", "action": "append_legacy_pointer", "before_sha256": hashlib.sha256(original).hexdigest(), "sha256": sha(context)})
        # Rebuild mirror baseline from the final files without importing or executing source code.
        left, _ = inventory(staging/".agents/skills")
        right, _ = inventory(staging/".claude/skills")
        if left != right:
            raise MigrationError("Espelhos no destino divergiram; migração interrompida.")
        lock = {"schema_version": 1, "purpose": "mirror-baseline", "files": left}
        (staging/"skills-lock.json").write_text(json.dumps(lock, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        generated.append({"path": "skills-lock.json", "action": "rebuild_mirror_baseline", "sha256": sha(staging/"skills-lock.json")})
        if inventory(source)[0] != plan["source_inventory"]:
            raise MigrationError("Origem mudou durante a cópia; destino não promovido.")
        if package(template)["files"] != plan["release_inventory"]:
            raise MigrationError("Release mudou durante a cópia.")
        receipt = {key: plan[key] for key in ("schema_version", "created_at", "version", "source", "destination", "prefer_local_skills", "excluded", "skills", "notices", "remapped_ignore_rules")}
        for entry in mappings:
            entry["destination_sha256"] = sha(relative_path(staging, entry["target"]))
        receipt.update({"status": "copied", "mappings": mappings, "generated": generated, "completed_at": timestamp(), "validation": {"copy_hashes": "passed", "mirror_parity": "passed", "source_unchanged": "passed", "runtime_or_external_effect": "not_tested"}})
        record = relative_path(staging, MANIFEST)
        record.parent.mkdir(parents=True, exist_ok=True)
        record.write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        # Reserve the final name atomically: a preexisting directory is never overwritten.
        destination.mkdir()
        reservation = destination.stat()
        no_links(destination)
        if list(destination.iterdir()) or destination.stat().st_ino != reservation.st_ino:
            raise MigrationError("Destino foi alterado durante a promoção.")
        if os.name == "nt":
            # Windows rename refuses an existing target. Remove only our empty reservation.
            destination.rmdir()
            reservation = None
        os.rename(staging, destination)
        reservation = None
        return receipt
    finally:
        if staging.exists():
            shutil.rmtree(staging)
        if reservation is not None and destination.exists():
            if not destination.is_symlink() and destination.stat().st_ino == reservation.st_ino and not list(destination.iterdir()):
                destination.rmdir()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Instalação antiga; permanece intacta")
    parser.add_argument("destination", help="Diretório novo, fora da origem e da release")
    parser.add_argument("--apply", action="store_true", help="Criar a nova instalação após revisar a prévia")
    parser.add_argument("--prefer-local-skills", action="store_true", help="Preservar conscientemente skills locais que conflitam com as novas")
    args = parser.parse_args(argv)
    try:
        plan = make_plan(args.source, args.destination, prefer_local=args.prefer_local_skills)
        summary = {"status": "conflicts" if plan["conflicts"] else "preview", "version": plan["version"], "source": plan["source"], "destination": plan["destination"], "files_planned": len(plan["copies"]), "conflicts": plan["conflicts"], "skills": plan["skills"], "excluded": plan["excluded"], "notices": plan["notices"], "remapped_ignore_rules": plan["remapped_ignore_rules"], "mappings": [{"from": e["from"], "source": e["source"], "target": e["target"], "action": e["action"]} for e in plan["copies"] if e["from"] == "source"]}
        if args.apply and not plan["conflicts"]:
            perform(plan)
            summary["status"] = "copied"
            summary["manifest"] = str(Path(plan["destination"])/MANIFEST)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 1 if plan["conflicts"] else 0
    except (MigrationError, OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
