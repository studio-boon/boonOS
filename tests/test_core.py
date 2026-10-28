import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


sync = module('sync_skills')
pack = module('package')
check = module('check')


class CoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def write(self, relative, value):
        p = self.root/relative
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(value, encoding='utf-8')
        return p

    def test_sync_preserves_independent_mirror_edit(self):
        a = self.write('.agents/skills/pessoal/SKILL.md', 'original')
        changes, conflicts = sync.synchronize(self.root, True)
        self.assertFalse(conflicts)
        a.write_text('source changed')
        b = self.write('.claude/skills/pessoal/SKILL.md', 'user edit')
        changes, conflicts = sync.synchronize(self.root, True)
        self.assertTrue(conflicts)
        self.assertEqual(b.read_text(), 'user edit')

    def test_sync_allows_new_personal_skill_and_updates_unchanged_mirror(self):
        a = self.write('.agents/skills/pessoal/SKILL.md', 'original')
        sync.synchronize(self.root, True)
        a.write_text('new')
        changes, conflicts = sync.synchronize(self.root, False)
        self.assertEqual(changes, ['pessoal/SKILL.md'])
        self.assertEqual((self.root/'.claude/skills/pessoal/SKILL.md').read_text(), 'original')
        sync.synchronize(self.root, True)
        self.assertEqual((self.root/'.claude/skills/pessoal/SKILL.md').read_text(), 'new')

    def test_sync_never_deletes_mirror_only_file(self):
        self.write('.claude/skills/pessoal/SKILL.md', 'keep me')
        _, conflicts = sync.synchronize(self.root, True)
        self.assertTrue(conflicts)
        self.assertTrue((self.root/'.claude/skills/pessoal/SKILL.md').exists())

    def manifest(self):
        file = self.write('README.md', 'template')
        self.write('distribution.json', json.dumps({'schema_version': 1, 'files': {
            'README.md': hashlib.sha256(file.read_bytes()).hexdigest()}}))

    def test_export_excludes_unlisted_private_files(self):
        self.manifest()
        self.write('03. DOCS/98. PRIVADO/client.txt', 'private')
        self.write('01. SISTEMA/extra.md', 'personal context')
        output = self.root/'package.zip'
        pack.export(self.root, output)
        with zipfile.ZipFile(output) as z:
            self.assertEqual(set(z.namelist()), {'boonOS/README.md', 'boonOS/distribution.json'})

    def test_export_refuses_modified_template(self):
        self.manifest()
        self.write('README.md', 'personal facts')
        with self.assertRaises(ValueError):
            pack.export(self.root, self.root/'package.zip')
        self.assertFalse((self.root/'package.zip').exists())

    def test_export_uses_the_exact_bytes_validated(self):
        self.manifest()
        original = Path.read_bytes
        reads = []

        def changing_read(path):
            data = original(path)
            if path == (self.root/'README.md').resolve():
                reads.append(path)
                path.write_text('personal facts', encoding='utf-8')
            return data

        with patch.object(Path, 'read_bytes', changing_read):
            pack.export(self.root, self.root/'package.zip')
        with zipfile.ZipFile(self.root/'package.zip') as z:
            self.assertEqual(z.read('boonOS/README.md'), b'template')
        self.assertEqual(len(reads), 1)

    def test_export_refuses_traversal(self):
        self.write('distribution.json', json.dumps({'schema_version': 1, 'files': {'../outside.md': 'bad'}}))
        with self.assertRaises(ValueError):
            pack.export(self.root, self.root/'package.zip')

    def test_frontmatter_requires_nonempty_description(self):
        file = self.write('SKILL.md', '---\nname: exemplo\ndescription: >\n---\n# Texto\n')
        with self.assertRaises(ValueError):
            check.frontmatter(file)


if __name__ == '__main__':
    unittest.main()
