#!/usr/bin/env python3
"""Export only the unchanged release allowlist; never export user context by glob."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import tempfile
import zipfile


def approved_files(root):
    root = root.resolve()
    manifest = json.loads((root/'distribution.json').read_text(encoding='utf-8'))
    if manifest.get('schema_version') != 1 or not isinstance(manifest.get('files'), dict):
        raise ValueError('Manifesto inválido.')
    result = []
    for rel, expected in manifest['files'].items():
        parts = PurePosixPath(rel)
        if parts.is_absolute() or '..' in parts.parts or '\\' in rel or not parts.parts:
            raise ValueError('Caminho inválido no manifesto: '+rel)
        if any(part in {'.git', '.env', '98. PRIVADO', '_PRIVADO', '_privado'} for part in parts.parts):
            raise ValueError('Conteúdo privado no manifesto: '+rel)
        path = root/rel
        if any(root.joinpath(*parts.parts[:i]).is_symlink() for i in range(1, len(parts.parts)+1)):
            raise ValueError('Symlink no pacote: '+rel)
        if not path.is_file():
            raise ValueError('Release alterada: '+rel+'. Exporte a partir de um clone limpo.')
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError('Release alterada: '+rel+'. Exporte a partir de um clone limpo.')
        result.append((rel, data))
    return manifest, result


def export(root, output):
    if output.exists() or output.is_symlink():
        raise ValueError('A saída já existe; escolha outro arquivo.')
    manifest, files = approved_files(root)
    with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.zip', delete=False) as temp:
        staged = Path(temp.name)
    try:
        with zipfile.ZipFile(staged, 'w', zipfile.ZIP_DEFLATED) as archive:
            for rel, data in sorted(files):
                info = zipfile.ZipInfo('boonOS-2.1/'+rel, (2026, 9, 25, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
            info = zipfile.ZipInfo('boonOS-2.1/distribution.json', (2026, 9, 25, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, json.dumps(manifest, indent=2, ensure_ascii=False)+'\n')
        # Exclusive create avoids overwriting a file created during export.
        with output.open('xb') as final:
            final.write(staged.read_bytes())
    finally:
        staged.unlink(missing_ok=True)
    return len(files)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    try:
        count = export(args.root.resolve(), args.output.absolute())
        print(f'Pacote criado: {args.output} ({count} arquivos + manifesto).')
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc)+'\n')


if __name__ == '__main__':
    main()
