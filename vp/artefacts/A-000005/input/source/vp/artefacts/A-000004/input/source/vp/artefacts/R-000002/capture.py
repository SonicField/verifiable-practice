#!/usr/bin/env python3
"""Retained candidate verification batch; never overwrites an earlier attempt."""
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
HERE = Path(__file__).resolve().parent
AFTER = ROOT / 'vp/artefacts/C-000001/after'
BEFORE = ROOT / 'vp/artefacts/C-000001/before'


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


results = []
def command(label, argv):
    start = now()
    p = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True)
    (HERE / (label + '.stdout.txt')).write_text(p.stdout)
    (HERE / (label + '.stderr.txt')).write_text(p.stderr)
    results.append({'member': label, 'argv': argv, 'cwd': str(ROOT), 'started': start,
                    'ended': now(), 'exit': p.returncode,
                    'stdout': label + '.stdout.txt', 'stderr': label + '.stderr.txt'})
    return p


if AFTER.exists():
    raise SystemExit('Candidate snapshot exists; retry requires new record/snapshot.')
started = now()
p = command('inventory', ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'])
names = sorted(set(n for n in p.stdout.split('\0') if n and not n.startswith(('vp/', '.vp/'))))
files = []
for name in names:
    original = ROOT / name
    copy = AFTER / 'source' / name
    copy.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(original, copy)
    if digest(original) != digest(copy):
        raise SystemExit('Concurrent change: ' + name)
    files.append({'path': name, 'bytes': copy.stat().st_size, 'sha256': digest(copy)})
# Preserve targets of the product's operational-root links in this source bundle.
for p in (ROOT / 'vp').glob('*.md'):
    dest = AFTER / 'source/vp' / p.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(p, dest)
shutil.copytree(ROOT / 'vp/records', AFTER / 'source/vp/records')
head = command('head', ['git', 'rev-parse', 'HEAD']).stdout.strip()
command('git-status', ['git', 'status', '--short'])
(AFTER / 'snapshot.json').write_text(json.dumps({'captured': now(), 'head': head, 'files': files,
    'source': 'dirty exact candidate bytes; worker capture'}, indent=2) + '\n')
for name in ['checks.py', 'skill-validator.py']:
    shutil.copyfile(ROOT / 'vp/artefacts/R-000001' / name, HERE / name)
command('runtime', ['/usr/bin/python3', '-c', 'import sys,yaml; print(sys.version); print(yaml.__version__); print(yaml.__file__)'])
for kind in ['structural', 'behavior']:
    command(kind, ['/usr/bin/python3', str(HERE / 'checks.py'), kind,
                   str(AFTER / 'source'), str(AFTER / 'snapshot.json')])
command('baseline-negative', ['/usr/bin/python3', str(HERE / 'checks.py'), 'behavior',
                             str(BEFORE / 'source'), str(BEFORE / 'snapshot.json')])
command('frontmatter', ['/usr/bin/python3', str(HERE / 'skill-validator.py'), str(AFTER / 'source')])
command('diff-whitespace', ['git', 'diff', '--check'])
command('diff', ['git', 'diff', '--', 'README.md', 'SKILL.md', 'WHY.md', 'concepts', 'CHANGELOG.md'])
old = {f['path']: f for f in json.loads((BEFORE / 'snapshot.json').read_text())['files']}
changed = [dict(f, before_sha256=old.get(f['path'], {}).get('sha256')) for f in files
           if f['sha256'] != old.get(f['path'], {}).get('sha256')]
(HERE / 'changed-files.json').write_text(json.dumps({'files': changed}, indent=2) + '\n')
(HERE / 'results.json').write_text(json.dumps({'started': started, 'ended': now(), 'members': results,
    'expected_negative_member': 'baseline-negative exit 1', 'capture': 'worker controlled'}, indent=2) + '\n')
print(json.dumps({'files': len(files), 'changed_files': len(changed),
    'members': [{'id': r['member'], 'exit': r['exit']} for r in results]}, indent=2))
