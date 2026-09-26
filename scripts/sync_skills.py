#!/usr/bin/env python3
"""Preview skill mirroring; never remove local files or overwrite a divergent edit."""
import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as temp:
        temp.write(data)
        tmp = Path(temp.name)
    try:
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def synchronize(root, apply=False):
    src, dst = root/'.agents/skills', root/'.claude/skills'
    lockfile = root/'skills-lock.json'
    if lockfile.is_symlink():
        return [], ['Lockfile é symlink; resolver antes de sincronizar.']
    lock = json.loads(lockfile.read_text(encoding='utf-8')) if lockfile.exists() else {'files': {}}
    old = lock.get('files', {})
    changes, conflicts, expected = [], [], {}
    for folder in (src, dst):
        if folder.parent.is_symlink() or folder.is_symlink() or any(p.is_symlink() for p in folder.rglob('*')):
            return [], ['Symlink em skill; resolva explicitamente antes de sincronizar.']
    paths = sorted({p.relative_to(folder).as_posix() for folder in (src, dst)
                    for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts})
    for rel in paths:
        a, b = sha(src/rel), sha(dst/rel)
        expected[rel] = (a, b)
        if a is None:
            conflicts.append('Existe só no espelho; preservar e decidir destino: '+rel)
        elif a != b:
            if b is None or b == old.get(rel):
                changes.append(rel)
            else:
                conflicts.append('Edição no espelho sem baseline correspondente: '+rel)
    if conflicts or not apply:
        return changes, conflicts
    if any((sha(src/rel), sha(dst/rel)) != pair for rel, pair in expected.items()):
        return changes, ['Arquivos mudaram durante a prévia; execute novamente.']
    for rel in changes:
        atomic(dst/rel, (src/rel).read_bytes())
    files = {rel: sha(src/rel) for rel in paths if (src/rel).is_file()}
    atomic(lockfile, (json.dumps({'schema_version': 1, 'purpose': 'mirror-baseline', 'files': files},
                               indent=2, ensure_ascii=False)+'\n').encode())
    return changes, []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--apply', action='store_true')
    group.add_argument('--check', action='store_true')
    args = parser.parse_args()
    changes, conflicts = synchronize(args.root.resolve(), args.apply)
    for item in changes:
        print(('COPIADO: ' if args.apply and not conflicts else 'PREVISTO: ')+item)
    for item in conflicts:
        print('CONFLITO: '+item)
    if not changes and not conflicts:
        print('Espelhos em paridade.')
    return 1 if conflicts or (changes and not args.apply) else 0


if __name__ == '__main__':
    raise SystemExit(main())
