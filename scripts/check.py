#!/usr/bin/env python3
"""Portable, read-only structural verification. Python standard library only."""
import argparse
import hashlib
import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree(path):
    return {f.relative_to(path).as_posix(): digest(f) for f in path.rglob('*')
            if f.is_file() and '__pycache__' not in f.parts}


def frontmatter(path):
    text = path.read_text(encoding='utf-8')
    parts = text.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError('frontmatter ausente')
    name = re.search(r'^name:\s*([a-z0-9-]+)\s*$', parts[1], re.M)
    description = re.search(r'^description:\s*(.+)', parts[1], re.M)
    if not name or not description:
        raise ValueError('name/description ausente ou inválido')
    if description[1].strip() in ('>', '|', '>-', '|-'):
        if not re.search(r'^\s{2,}\S', parts[1], re.M):
            raise ValueError('description vazia')
    if len(name[1]) > 64 or not parts[2].strip():
        raise ValueError('nome longo ou corpo vazio')
    return name[1]


def validate(root, release=False):
    errors, warnings = [], []
    required = ['README.md', 'AGENTS.md', 'CLAUDE.md', '00. COMECE-AQUI.md',
                'boonos.json', '01. SISTEMA/CATALOGO.json', '01. SISTEMA/PERFIL.yaml',
                '01. SISTEMA/CONTEXTO.md', '01. SISTEMA/ONBOARDING.md',
                '01. SISTEMA/SKILLSET.md', '06. GUIAS/01. INSTALAÇÃO/INSTALAR.md']
    for item in required:
        if not (root/item).is_file():
            errors.append('Arquivo essencial ausente: '+item)
    for base in ['.agents/skills', '.claude/skills']:
        folder = root/base
        if not folder.is_dir():
            errors.append('Pasta de skills ausente: '+base)
            continue
        for item in folder.rglob('*'):
            if item.is_symlink():
                errors.append('Symlink inesperado no pacote de skills: '+str(item.relative_to(root)))
        for child in folder.iterdir():
            if not child.is_dir():
                continue
            try:
                name = frontmatter(child/'SKILL.md')
                if name != child.name:
                    errors.append('name e pasta divergem: '+child.name)
            except (ValueError, OSError, UnicodeError) as exc:
                errors.append(str(child.relative_to(root))+': '+str(exc))
    actual = {p.name for p in (root/'.agents/skills').glob('*/') if p.is_dir()}
    if tree(root/'.agents/skills') != tree(root/'.claude/skills'):
        errors.append('Espelhos de skills divergentes; use scripts/sync_skills.py para diagnóstico.')
    try:
        catalog = json.loads((root/'01. SISTEMA/CATALOGO.json').read_text(encoding='utf-8'))
        entries = catalog['skills']
        names = [e['name'] for e in entries]
        if len(set(names)) != len(names):
            errors.append('Skills duplicadas no catálogo.')
        for entry in entries:
            for key in ['name', 'area', 'label', 'summary', 'inputs', 'output', 'dependencies', 'maturity', 'origin']:
                if key not in entry:
                    errors.append('Campo '+key+' ausente em '+entry.get('name', '?'))
            if entry.get('area') not in ['criativo', 'operacional', 'sistema']:
                errors.append('Área inválida: '+entry.get('name', '?'))
        for missing in set(names)-actual:
            errors.append('Skill base ausente: '+missing)
        for extra in actual-set(names):
            warnings.append('Extensão local válida fora do pacote base: '+extra)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append('Catálogo inválido: '+str(exc))
    for path in root.rglob('*.md'):
        if any(s in path.parts for s in ['.git', '98. PRIVADO', '_PRIVADO', '_privado', '99. ARQUIVO', '01. EVOLUÇÃO', '__pycache__']):
            continue
        content = path.read_text(encoding='utf-8')
        prose = re.sub(r'(?ms)^(```|~~~).*?^\1[^\n]*', '', content)
        for match in re.finditer(r'\[[^\]\n]+\]\((<[^>]+>|[^)\n]+)\)', prose):
            target = match[1].strip().strip('<>')
            if target.startswith('#') or urlsplit(target).scheme:
                continue
            target = unquote(target.split('#', 1)[0])
            if target and not (path.parent/target).exists():
                errors.append('Link local quebrado: '+str(path.relative_to(root))+' → '+target)
    if release:
        try:
            package = json.loads((root/'distribution.json').read_text(encoding='utf-8'))
            for relative, expected in package['files'].items():
                parts = PurePosixPath(relative)
                if parts.is_absolute() or '..' in parts.parts or '\\' in relative:
                    errors.append('Caminho inválido no manifesto: '+relative)
                    continue
                f = root/relative
                if not f.is_file() or f.is_symlink() or digest(f) != expected:
                    errors.append('Arquivo de release ausente/alterado: '+relative)
                elif f.suffix in {'.md', '.json', '.yaml', '.yml', '.py', '.sh'}:
                    text = f.read_text(encoding='utf-8')
                    if re.search(r'(?:/Users/|/home/)[A-Za-z][^\s/]+/', text):
                        errors.append('Path ou dado privado no pacote: '+relative)
                if any(part in {'98. PRIVADO', '_PRIVADO', '_privado', '.git', '.env'} for part in f.relative_to(root).parts):
                    errors.append('Arquivo privado na allowlist: '+relative)
        except (OSError, ValueError, KeyError) as exc:
            errors.append('Manifesto de distribuição inválido: '+str(exc))
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--release', action='store_true')
    args = parser.parse_args()
    errors, warnings = validate(args.root.resolve(), args.release)
    for msg in warnings:
        print('AVISO:', msg)
    for msg in errors:
        print('ERRO:', msg)
    if not errors:
        print('boonOS: estrutura, catálogo, links e espelhos válidos.' + (' Release íntegra.' if args.release else ''))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
