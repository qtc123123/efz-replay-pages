import hashlib
import pathlib
import re
import stat
import zipfile

MAX_FILE_BYTES = 64 * 1024 * 1024 + 128 * 1024
MAX_SITE_BYTES = 1_000_000_000


def need(ok, message):
    if not ok:
        raise ValueError(message)


def safe_name(name):
    need(isinstance(name, str) and 0 < len(name) <= 512 and re.fullmatch(r'[A-Za-z0-9_./-]+', name), 'unsafe member name')
    path = pathlib.PurePosixPath(name)
    need(not path.is_absolute() and all(part not in ('', '.', '..') for part in name.split('/')) and str(path) == name, 'noncanonical member name')
    return path


def file_hash(path):
    need(not path.is_symlink() and stat.S_ISREG(path.stat().st_mode), 'regular file required')
    before = path.stat()
    digest = hashlib.sha256()
    size = 0
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            size += len(block)
            need(size <= MAX_SITE_BYTES, 'input capacity')
            digest.update(block)
    after = path.stat()
    need(size == before.st_size and all(getattr(before, key) == getattr(after, key) for key in ('st_dev', 'st_ino', 'st_size', 'st_mtime_ns', 'st_ctime_ns')), 'input changed')
    return digest.hexdigest()


def read_manifest(path, count):
    need(not path.is_symlink() and stat.S_ISREG(path.stat().st_mode) and path.stat().st_size <= 256 * 1024, 'checksum manifest extent/type')
    entries = {}
    for line in path.read_text(encoding='ascii').splitlines(keepends=True):
        match = re.fullmatch(r'([a-f0-9]{64})  ([A-Za-z0-9_./-]+)\n', line)
        need(match is not None, 'checksum manifest line')
        digest, name = match.groups()
        safe_name(name)
        need(name not in entries, 'duplicate checksum path')
        entries[name] = digest
    need(len(entries) == count, 'checksum manifest count')
    parents = {parent.as_posix() for name in entries for parent in safe_name(name).parents if str(parent) != '.'}
    need(not (set(entries) & parents), 'file/directory path conflict')
    return entries


def verify_tree(root, expected):
    need(root.is_dir() and not root.is_symlink(), 'regular output directory required')
    files, directories = set(), set()
    total = 0
    for entry in root.rglob('*'):
        name = entry.relative_to(root).as_posix()
        need(not entry.is_symlink(), 'output symlink refused')
        mode = entry.stat().st_mode
        if stat.S_ISDIR(mode):
            directories.add(name)
        else:
            need(stat.S_ISREG(mode) and entry.stat().st_nlink == 1, 'output link or special file refused')
            need(name in expected, 'extra output file')
            need(file_hash(entry) == expected[name], 'file digest mismatch: ' + name)
            files.add(name)
            total += entry.stat().st_size
    parents = {parent.as_posix() for name in expected for parent in safe_name(name).parents if str(parent) != '.'}
    need(files == set(expected) and directories == parents, 'output allowlist mismatch')
    need(total <= MAX_SITE_BYTES, 'site capacity')
    return total


def extract_checked(archive_path, root, expected):
    need(not archive_path.is_symlink() and stat.S_ISREG(archive_path.stat().st_mode), 'regular ZIP required')
    with zipfile.ZipFile(archive_path) as archive:
        members = archive.infolist()
        names = [member.filename for member in members]
        need(len(names) == len(set(names)) == len(expected) and set(names) == set(expected), 'ZIP member allowlist mismatch')
        for member in members:
            need(member.orig_filename == member.filename, 'ZIP filename alias refused')
            safe_name(member.orig_filename)
            need(not member.is_dir() and stat.S_ISREG(member.external_attr >> 16), 'ZIP link or directory refused')
            need(not (member.flag_bits & 1) and member.compress_type in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED), 'ZIP encoding refused')
            need(0 < member.file_size <= MAX_FILE_BYTES, 'ZIP member extent')
        need(sum(member.file_size for member in members) <= MAX_SITE_BYTES, 'ZIP capacity')
        need(not root.exists() and not root.is_symlink(), 'fresh output required')
        root.mkdir(mode=0o755)
        for member in members:
            target = root.joinpath(*safe_name(member.filename).parts)
            need(not target.exists() and not target.is_symlink(), 'fresh target required')
            target.parent.mkdir(mode=0o755, parents=True, exist_ok=True)
            digest = hashlib.sha256()
            size = 0
            with archive.open(member) as source, target.open('xb') as output:
                for block in iter(lambda: source.read(1024 * 1024), b''):
                    size += len(block)
                    need(size <= member.file_size, 'ZIP body extent')
                    digest.update(block)
                    output.write(block)
            need(size == member.file_size and digest.hexdigest() == expected[member.filename], 'file digest mismatch: ' + member.filename)
            target.chmod(0o644)


def check_transition(base, final, overlay):
    """Every overlay member must be an announced changed or added final file."""
    need(set(base) <= set(final), 'base file deletion refused')
    changed = {name for name, digest in final.items() if base.get(name) != digest}
    need(set(overlay) == changed, 'overlay must equal exact manifest difference')
    need(all(overlay[name] == final[name] for name in overlay), 'overlay final digest mismatch')
    return changed


def apply_overlay(destination, overlay_root, expected):
    """Replace only regular single-link files using already verified overlay bytes."""
    import os
    need(destination.is_dir() and not destination.is_symlink(), 'regular destination required')
    verify_tree(overlay_root, expected)
    for name in expected:
        path = safe_name(name)
        source = overlay_root.joinpath(*path.parts)
        target = destination.joinpath(*path.parts)
        parent = destination
        for component in path.parts[:-1]:
            parent = parent / component
            need(not parent.is_symlink(), 'overlay parent symlink refused')
            if parent.exists():
                need(parent.is_dir(), 'overlay parent directory required')
            else:
                parent.mkdir(mode=0o755)
        need(not target.is_symlink(), 'overlay target symlink refused')
        if target.exists():
            need(stat.S_ISREG(target.stat().st_mode) and target.stat().st_nlink == 1, 'overlay target link or type refused')
        os.replace(source, target)
        target.chmod(0o644)
    for entry in sorted(overlay_root.rglob('*'), key=lambda p: len(p.parts), reverse=True):
        need(entry.is_dir() and not entry.is_symlink(), 'unexpected overlay remainder')
        entry.rmdir()


def main(repository, temporary):
    import json
    base = read_manifest(repository / 'base-site-sha256.txt', 767)
    final = read_manifest(repository / 'site-sha256.txt', 862)
    overlay = read_manifest(repository / 'runtime-overlay-sha256.txt', 112)
    check_transition(base, final, overlay)

    base_path = temporary / 'replay-site.zip'
    base_commitment = read_manifest(repository / 'replay-site.zip.sha256', 1)
    need(base_commitment == {'replay-site.zip': 'd1b20e1df8f011144eeeb80330fe5c1c5ade865fc0c76ff7cee105686e9dda80'}, 'unreviewed base archive commitment')
    need(base_path.stat().st_size == 221228726 and file_hash(base_path) == base_commitment['replay-site.zip'], 'base archive extent/digest')

    overlay_path = repository / 'runtime-overlay.zip'
    overlay_commitment = read_manifest(repository / 'runtime-overlay.zip.sha256', 1)
    need(overlay_commitment == {'runtime-overlay.zip': '66347930e903b9eb44f69f90924f59c69f00823430319d6ea0acd78f21325790'}, 'unreviewed overlay commitment')
    need(overlay_path.stat().st_size == 1381939 and file_hash(overlay_path) == overlay_commitment['runtime-overlay.zip'], 'overlay archive extent/digest')

    destination = temporary / 'replay-pages-site'
    overlay_root = temporary / 'replay-pages-overlay'
    extract_checked(base_path, destination, base)
    base_bytes = verify_tree(destination, base)
    need(base_bytes == 223341184, 'base site extent')
    extract_checked(overlay_path, overlay_root, overlay)
    verify_tree(overlay_root, overlay)
    apply_overlay(destination, overlay_root, overlay)
    final_bytes = verify_tree(destination, final)
    need(final_bytes == 227697550, 'final site extent')
    print(json.dumps({'files': len(final), 'bytes': final_bytes, 'baseArchiveSha256': base_commitment['replay-site.zip'], 'overlaySha256': overlay_commitment['runtime-overlay.zip'], 'overlayFiles': len(overlay), 'exactAllowlist': True, 'allFileHashesVerified': True, 'symlinks': 0}, sort_keys=True))


if __name__ == '__main__':
    import sys
    need(len(sys.argv) == 3, 'repository and fresh temporary root required')
    main(*map(pathlib.Path, sys.argv[1:]))
