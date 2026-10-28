#!/usr/bin/env python3
"""Gera ou confere README e licença da vitrine a partir da cópia do pacote."""
import argparse
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / 'boonOS'
LINK = re.compile(r'\]\((<[^>]+>|[^)]+)\)')
HTML_ASSET = re.compile(r'((?:src|srcset)=")(\.github/assets/[^\"]+)(")')


def public_text(source):
    """Preserva o conteúdo; ajusta links locais para a pasta do pacote."""
    def link(match):
        raw = match.group(1)
        angled = raw.startswith('<') and raw.endswith('>')
        value = raw[1:-1] if angled else raw
        if value.startswith(('#', '/')) or urlsplit(value).scheme:
            return match.group(0)
        adjusted = 'boonOS/' + value
        return '](' + ('<' + adjusted + '>' if angled else adjusted) + ')'
    text = LINK.sub(link, source)
    return HTML_ASSET.sub(lambda m: m.group(1) + 'boonOS/' + m.group(2) + m.group(3), text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verifica sem alterar arquivos.')
    args = parser.parse_args()
    errors = []
    for name in ('README.md', 'LICENSE.md'):
        expected = public_text((PACKAGE / name).read_text(encoding='utf-8'))
        destination = ROOT / name
        if args.check:
            if not destination.is_file() or destination.read_text(encoding='utf-8') != expected:
                errors.append(name)
        else:
            destination.write_text(expected, encoding='utf-8')
    if errors:
        parser.exit(1, 'Vitrine fora de sincronia: ' + ', '.join(errors) + '. Rode python3 .github/sync_vitrine.py.\n')
    print('README e licença da vitrine coerentes com o pacote.')


if __name__ == '__main__':
    main()
