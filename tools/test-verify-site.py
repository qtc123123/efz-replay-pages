import hashlib
import importlib.util
import pathlib
import stat
import tempfile
import unittest
import zipfile
import warnings

spec = importlib.util.spec_from_file_location('verify_site', pathlib.Path(__file__).with_name('verify-site.py'))
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
sha = lambda b: hashlib.sha256(b).hexdigest()

class OverlayTests(unittest.TestCase):
    def test_manifest_transition_only_announces_actual_replacements_and_additions(self):
        self.assertEqual(v.check_transition({'a':'old','b':'same'}, {'a':'new','b':'same','c':'add'}, {'a':'new','c':'add'}), {'a','c'})

    def test_manifest_transition_refuses_deletion_omission_and_unnecessary_overlap(self):
        for base, final, patch in [({'a':'old'}, {}, {}), ({'a':'old'}, {'a':'new'}, {}), ({'a':'old'}, {'a':'old'}, {'a':'old'}), ({'a':'old'}, {'a':'new'}, {'a':'other'})]:
            with self.subTest(base=base, final=final, patch=patch), self.assertRaises(ValueError):
                v.check_transition(base, final, patch)

    def test_apply_replaces_only_verified_files_and_retains_assets(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d)/'site'; patch=pathlib.Path(d)/'overlay'; root.mkdir();patch.mkdir()
            (root/'a').write_bytes(b'old');(root/'asset').write_bytes(b'asset')
            (patch/'a').write_bytes(b'new');(patch/'b').write_bytes(b'add')
            expected={'a':sha(b'new'),'asset':sha(b'asset'),'b':sha(b'add')}
            v.apply_overlay(root,patch,{'a':sha(b'new'),'b':sha(b'add')})
            self.assertEqual(v.verify_tree(root,expected),11)
            self.assertEqual((root/'asset').read_bytes(),b'asset')
            self.assertEqual(list(patch.rglob('*')),[])

    def test_apply_refuses_symlink_parent_or_existing_hardlink(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d)/'site'; patch=pathlib.Path(d)/'overlay'; root.mkdir();patch.mkdir()
            (root/'target').write_bytes(b'old');(root/'a').hardlink_to(root/'target');(patch/'a').write_bytes(b'new')
            with self.assertRaises(ValueError):v.apply_overlay(root,patch,{'a':sha(b'new')})
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d)/'site'; patch=pathlib.Path(d)/'overlay'; root.mkdir();(patch/'dir').mkdir(parents=True)
            (root/'dir').symlink_to(patch/'dir',target_is_directory=True);(patch/'dir'/'a').write_bytes(b'new')
            with self.assertRaises(ValueError):v.apply_overlay(root,patch,{'dir/a':sha(b'new')})

    def test_zip_refuses_nul_truncated_filename_alias(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/'x.zip'
            with zipfile.ZipFile(p,'w') as z:
                info=zipfile.ZipInfo('aX');info.create_system=3;info.external_attr=(stat.S_IFREG|0o644)<<16
                z.writestr(info,b'abc')
            raw=p.read_bytes();self.assertEqual(raw.count(b'aX'),2)
            p.write_bytes(raw.replace(b'aX',b'a\0'))
            with self.assertRaises(ValueError):
                v.extract_checked(p,pathlib.Path(d)/'out',{'a':sha(b'abc')})

    def test_zip_rejects_duplicate_traversal_symlink_and_wrong_hash(self):
        for kind in ['duplicate','traversal','symlink','hash']:
            with self.subTest(kind=kind),tempfile.TemporaryDirectory() as d:
                p=pathlib.Path(d)/'x.zip'
                with zipfile.ZipFile(p,'w') as z:
                    info=zipfile.ZipInfo('../a' if kind=='traversal' else 'a');info.create_system=3;info.external_attr=((stat.S_IFLNK if kind=='symlink' else stat.S_IFREG)|0o644)<<16
                    z.writestr(info,b'abc')
                    if kind=='duplicate':
                        with warnings.catch_warnings():
                            warnings.simplefilter('ignore', UserWarning)
                            z.writestr(info,b'abc')
                with self.assertRaises(ValueError):v.extract_checked(p,pathlib.Path(d)/'out',{'a':sha(b'wrong' if kind=='hash' else b'abc')})

if __name__=='__main__':unittest.main()
