"""Prepare private analysis/build inputs from a user-supplied GEOE08 image.

Requires Python, Git, and a caller-supplied decomp-toolkit executable.
Does not download any game files or generate distributable game binaries.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import struct
import subprocess
import sys

UPSTREAM = 'https://github.com/ethannicholas/gcn-recomp.git'
COMMIT = '9e93f1bb7cc4a370af53c895e971fdcab55ed3fc'
DOL_SHA1 = '0772a7cabc270b32949f43279a16b0aec81811f9'
MODULES = ['demo', 'game', 'menu'] + [f'pl{i:02x}' for i in range(48)]

def prepare(image, dtk):
    root = Path(__file__).resolve().parents[1]
    for directory in ['game', 'analysis/rel-symbols', 'docs', 'logs', 'upstream']:
        (root / directory).mkdir(parents=True, exist_ok=True)
    destination = root / 'game/disc.nkit.iso'
    if image.resolve() != destination.resolve():
        if destination.exists():
            def sha(p):
                with p.open('rb') as f:
                    return hashlib.file_digest(f, 'sha256').hexdigest()
            if sha(image) != sha(destination):
                raise RuntimeError('A different private game image already exists')
        else:
            shutil.copy2(image, destination)
    upstream = root / 'upstream/gcn-recomp'
    if not upstream.exists():
        subprocess.run(['git', 'clone', UPSTREAM, str(upstream)], check=True)
        subprocess.run(['git', '-C', str(upstream), 'checkout', COMMIT], check=True)
    actual = subprocess.check_output(['git', '-C', str(upstream), 'rev-parse', 'HEAD'], text=True).strip()
    if actual != COMMIT:
        raise RuntimeError(f'Expected upstream {COMMIT}, found {actual}')
    sys.path.insert(0, str(upstream / 'recomp'))
    from dol import DiscImage
    from rel import disc_files, read_disc_file
    disc = DiscImage(str(destination))
    header = disc.read(0, 0x440)
    if header[:6] != b'GEOE08' or header[0x1c:0x20] != bytes.fromhex('c2339f3d'):
        raise RuntimeError('Expected a GameCube GEOE08 image')
    offset = struct.unpack_from('>I', header, 0x420)[0]
    dh = disc.read(offset, 0x100)
    offsets = struct.unpack_from('>18I', dh)
    sizes = struct.unpack_from('>18I', dh, 0x90)
    length = max(o + n for o, n in zip(offsets, sizes) if n)
    dol = disc.read(offset, length)
    if hashlib.sha1(dol).hexdigest() != DOL_SHA1:
        raise RuntimeError('This revision of main.dol is unsupported')
    (root / 'game/main.dol').write_bytes(dol)
    files = disc_files(disc)
    module_dir = root / 'game/files/module'
    module_dir.mkdir(parents=True, exist_ok=True)
    config = ['object: game/main.dol', f'hash: {DOL_SHA1}',
              'symbols: analysis/symbols.txt', 'splits: analysis/splits.txt', 'modules:']
    inventory = []
    for name in MODULES:
        data = read_disc_file(disc, files, f'module/{name}.rel')
        (module_dir / (name + '.rel')).write_bytes(data)
        digest = hashlib.sha1(data).hexdigest()
        config.extend([f'- object: game/files/module/{name}.rel', f'  hash: {digest}',
                       f'  symbols: analysis/rel-symbols/{name}.txt',
                       f'  splits: analysis/rel-symbols/{name}.splits.txt'])
        inventory.append({'name': name, 'sha1': digest, 'bytes': len(data)})
    (root / 'analysis/config.yml').write_text('\n'.join(config) + '\n')
    with (root / 'logs/dtk-analysis.log').open('w') as log:
        subprocess.run([str(dtk.resolve()), 'dol', 'split', 'analysis/config.yml',
                        'analysis/split', '-j', '4'], cwd=root, stdout=log, stderr=log, check=True)
    (root / 'docs/preparation.json').write_text(json.dumps({
        'disc_id': 'GEOE08', 'upstream_commit': actual,
        'main_dol_sha1': DOL_SHA1, 'active_modules': inventory,
        'note': 'Static preparation only; does not establish gameplay compatibility'
    }, indent=2))
    print('Prepared main.dol and 51 active modules')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', type=Path)
    parser.add_argument('--dtk', type=Path, required=True)
    args = parser.parse_args()
    prepare(args.image, args.dtk)
