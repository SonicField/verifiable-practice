#!/usr/bin/env python3
"""Optional staged-evidence byte comparison; no product execution."""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
capture = Path(sys.argv[1]) if len(sys.argv) > 1 else None
if capture and capture.exists():
    raise SystemExit('Existing batch member must not be overwritten')
started = datetime.now(timezone.utc).isoformat()
required_vp = {str(p.relative_to(ROOT)) for p in (ROOT / 'vp').rglob('*') if p.is_file()}
def coverage(paths):
    return sorted(required_vp - set(paths))
def sha(data):
    return hashlib.sha256(data).hexdigest()
def compare(name, blob, expected):
    return [] if sha(blob) == expected else [name]
listing = subprocess.run(['/usr/bin/git', 'ls-files', '--stage', '-z'], cwd=ROOT, capture_output=True)
listing.check_returncode()
files = []
for entry in listing.stdout.split(b'\0'):
    if entry:
        metadata, name = entry.split(b'\t', 1)
        mode, oid, stage = metadata.decode().split()
        if stage != '0' or mode not in ('100644', '100755'):
            raise SystemExit('Unsupported stage/mode for ' + name.decode())
        files.append({'path': name.decode(), 'mode': mode, 'object': oid})
objects = subprocess.run(['/usr/bin/git', 'cat-file', '--batch'], cwd=ROOT,
    input=('\n'.join(item['object'] for item in files)+'\n').encode(), capture_output=True)
objects.check_returncode()
offset = 0
differences = []
negative = None
for item in files:
    end = objects.stdout.index(b'\n', offset)
    oid, typ, size = objects.stdout[offset:end].decode().split()
    if oid != item['object'] or typ != 'blob':
        raise SystemExit('Wrong object response')
    size = int(size); blob = objects.stdout[end+1:end+1+size]; offset=end+size+2
    expected = sha((ROOT / item['path']).read_bytes())
    differences += compare(item['path'], blob, expected)
    item.update({'bytes': size, 'blob_sha256': sha(blob), 'working_sha256': expected})
    if negative is None:
        negative = {'path': item['path'], 'modified_blob_sha256': sha(blob+b'\nPLANTED CHANGE\n'),
                    'detected_paths': compare(item['path'], blob+b'\nPLANTED CHANGE\n', expected)}
untracked = subprocess.run(['/usr/bin/git', 'ls-files', '--others', '--exclude-standard', '-z'],
                           cwd=ROOT, capture_output=True)
untracked.check_returncode()
missing = [name.decode() for name in untracked.stdout.split(b'\0') if name]
tree = subprocess.run(['/usr/bin/git','write-tree'],cwd=ROOT,capture_output=True)
tree.check_returncode()
result = {'started': started, 'ended': datetime.now(timezone.utc).isoformat(),
    'cwd': str(ROOT), 'files': files, 'differences': differences, 'untracked_before_capture': missing,
    'negative_control': negative, 'tree': tree.stdout.decode().strip(),
    'executables': {name: {'path': str(path), 'resolved': str(path.resolve()),
                          'sha256': sha(path.read_bytes())}
                    for name,path in [('python',Path(sys.executable)),('git',Path('/usr/bin/git'))]},
    'commands': [{'argv': ['/usr/bin/git','ls-files','--stage','-z'], 'exit': listing.returncode,
                  'stdout_sha256': sha(listing.stdout), 'stderr': listing.stderr.decode()},
                 {'argv': ['/usr/bin/git','cat-file','--batch'], 'exit': objects.returncode,
                  'stdin': 'ordered object IDs in files', 'stdout_sha256': sha(objects.stdout),
                  'retention': 'blob bytes retained in Git objects; per-blob digest above', 'stderr': objects.stderr.decode()},
                 {'argv': ['/usr/bin/git','ls-files','--others','--exclude-standard','-z'],
                  'exit': untracked.returncode, 'stderr': untracked.stderr.decode()},
                 {'argv': ['/usr/bin/git','write-tree'], 'exit': tree.returncode,'stderr':tree.stderr.decode()}]}
missing_vp = coverage(item['path'] for item in files)
planted = next(item['path'] for item in files if item['path'].startswith('vp/'))
omitted = coverage(item['path'] for item in files if item['path'] != planted)
result['complete_vp_coverage'] = {'required_files': len(required_vp), 'missing': missing_vp, 'omitted_control': {'path': planted, 'detected': omitted}}
good = not differences and not missing and not missing_vp and omitted == [planted] and negative['detected_paths'] == [negative['path']]
result['criterion_met'] = good
if capture:
    capture.mkdir(parents=True)
    (capture/'index.stdout.bin').write_bytes(listing.stdout)
    (capture/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'files':len(files), 'differences':differences,'untracked':missing,
                  'negative_control_detected':bool(negative['detected_paths']),
                  'tree':result['tree'], 'required_vp_files':len(required_vp), 'missing_vp':missing_vp, 'omitted_control_detected':omitted==[planted], 'criterion_met':good}))
if not good:
    raise SystemExit(1)
