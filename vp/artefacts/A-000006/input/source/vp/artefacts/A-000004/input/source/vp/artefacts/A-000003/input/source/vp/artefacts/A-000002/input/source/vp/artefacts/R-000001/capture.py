#!/usr/bin/env python3
"""Capture actual member commands and a byte snapshot without overwriting evidence."""
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
HERE = Path(__file__).resolve().parent
BEFORE = ROOT / 'vp/artefacts/C-000001/before'


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


results = []
def command(label, argv):
    start = now()
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    (HERE / (label + '.stdout.txt')).write_text(p.stdout)
    (HERE / (label + '.stderr.txt')).write_text(p.stderr)
    results.append({'member': label, 'argv': argv, 'cwd': str(ROOT), 'started': start,
                    'ended': now(), 'exit': p.returncode,
                    'stdout': label + '.stdout.txt', 'stderr': label + '.stderr.txt'})
    return p


if BEFORE.exists():
    raise SystemExit('Refusing to overwrite initial snapshot; a retry needs a new record.')
started = now()
names = command('inventory', ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'])
paths = sorted(set(n for n in names.stdout.split('\0') if n and not n.startswith(('vp/', '.vp/'))))
files = []
for name in paths:
    source = ROOT / name
    target = BEFORE / 'source' / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    entry = {'path': name, 'bytes': target.stat().st_size, 'sha256': digest(target)}
    if digest(source) != entry['sha256']:
        raise SystemExit('Concurrent source change: ' + name)
    files.append(entry)
head = command('head', ['git', 'rev-parse', 'HEAD']).stdout.strip()
command('git-status', ['git', 'status', '--short'])
inventory = {'captured': now(), 'head': head, 'physical_root': str(ROOT.resolve()),
             'files': files, 'source': 'current dirty bytes; worker copy, no independent historical capture'}
(BEFORE / 'snapshot.json').write_text(json.dumps(inventory, indent=2) + '\n')
for directory, output in [(ROOT / '.vp', HERE / 'legacy-code-audit'),
                          (ROOT / 'vp/records/audits/A-000001', HERE / 'legacy-project-audit-record')]:
    shutil.copytree(directory, output)
legacy = []
for directory in [HERE / 'legacy-code-audit', HERE / 'legacy-project-audit-record']:
    for p in sorted(directory.rglob('*')):
        if p.is_file():
            legacy.append({'path': str(p.relative_to(HERE)), 'bytes': p.stat().st_size, 'sha256': digest(p)})
(HERE / 'legacy-inventory.json').write_text(json.dumps({'files': legacy, 'capture_time': now()}, indent=2) + '\n')
command('runtime', ['/usr/bin/python3', '-c', 'import sys,yaml; print(sys.version); print(yaml.__version__); print(yaml.__file__)'])
validator = Path('/home/alexturner/.codex/skills/.system/skill-creator/scripts/quick_validate.py')
shutil.copyfile(validator, HERE / 'skill-validator.py')
for kind in ['structural', 'behavior']:
    command(kind, ['/usr/bin/python3', str(HERE / 'checks.py'), kind,
                   str(BEFORE / 'source'), str(BEFORE / 'snapshot.json')])
command('frontmatter', ['/usr/bin/python3', str(HERE / 'skill-validator.py'), str(BEFORE / 'source')])
command('diff-whitespace', ['git', 'diff', '--check'])
(HERE / 'results.json').write_text(json.dumps({'started': started, 'ended': now(), 'members': results,
    'capture': 'worker-controlled subprocess captures; wrapper success is not an aggregate test pass'}, indent=2) + '\n')
print(json.dumps({'files': len(files), 'members': [{'id': r['member'], 'exit': r['exit']} for r in results],
                  'before': str(BEFORE), 'results': str(HERE / 'results.json')}, indent=2))
