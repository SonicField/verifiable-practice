#!/usr/bin/env python3
"""Coordinator packet capture, preserving input bytes and separate directory custody."""
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
VP = ROOT / 'vp'
HERE = VP / 'artefacts/A-000002'
INPUT = HERE / 'input'
REQUEST = VP / 'records/audits/A-000002/request.md'
BACKUP = Path('/home/alexturner/vp-preserved/verifiable-practice/A-000002-input')


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


if INPUT.exists() or BACKUP.exists():
    raise SystemExit('Refusing to overwrite packet/copy; retry requires another ID.')

# Reconcile mutable indexes once, before freezing them. Never alter sealed operations.
time = now()
lines = ['# Record Ledger', '', '**As of:** ' + time, '**Allocator:** worker /root; verifiable-practice namespace.', '',
    '| ID | Recorded status | Origin (canonical links in original) | Dependencies/consumers |',
    '|----|-----------------|--------------------------------------|------------------------|']
for p in sorted((VP / 'records').glob('*/*/record.md')):
    text = p.read_text(); rid = p.parent.name
    m = re.search(r'^\*\*Status:\*\* (.*)$', text, re.M)
    status = m.group(1) if m else 'legacy original report status'
    m = re.search(r'^\*\*Origin:\*\* (.*)$', text, re.M)
    origin = m.group(1) if m else 'legacy original request/unknown older root'
    origin = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', origin)
    dep = ', '.join(sorted(set(re.findall(r'\b[DSHEBRCVA]-\d{6}\b', text)) - {rid}))
    lines.append('| [' + rid + '](' + str(p.relative_to(VP)) + ') | ' + status.replace('|', '/') + ' | ' + origin.replace('|', '/') + ' | ' + dep + ' |')
lines += ['', '| [A-000002 request](records/audits/A-000002/request.md) | allocated, packet/assessment pending | D-000005 | A-000001 findings / V-000002 / current packet |', '',
    'A-000001 retains its original task-local namespace; V-000001 is its import locator. Current',
    'records use present D-000001 root. Incoming reliance: H-000002/R-000002 -> D-000004;',
    'H-000003/R-000003 -> current retention/audit; A-000001/F-001–008 -> V-000002 -> A-000002.',
    'Historical missing captures do not become current evidence. Never close findings from this ledger alone.', '']
(VP / 'LEDGER.md').write_text('\n'.join(lines))
coverage = (VP / 'COVERAGE.md').read_text()
coverage += '\n## Audit transaction boundary\n\nA-000002 request is a commissioned pending audit under D-000005. Its own future report\nis outside its input snapshot and will be catalogued after it is produced. This avoids\na self-referential verdict. All completed current records/maintained source at freeze\nremain covered; unfinished audit output is not falsely declared completed.\n'
(VP / 'COVERAGE.md').write_text(coverage)
started = now()
INPUT.mkdir(parents=True)
source = INPUT / 'source'
inventory = json.loads((VP / 'artefacts/C-000001/after/snapshot.json').read_text())
for e in inventory['files']:
    p = ROOT / e['path']
    if sha(p) != e['sha256']:
        raise SystemExit('Source changed after candidate checks: ' + e['path'])
    dest = source / e['path']; dest.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p, dest)
for p in sorted(VP.rglob('*')):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    if str(rel).startswith(('vp/artefacts/A-000002/', 'vp/records/audits/A-000002/')):
        continue
    dest = source / rel; dest.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(p, dest)
shutil.copyfile(REQUEST, INPUT / 'request-preparation.md')
captures = []
for label, argv in [('head', ['git', 'rev-parse', 'HEAD']), ('status', ['git', 'status', '--short']),
                    ('runtime', ['/usr/bin/python3', '-c', 'import sys; print(sys.version); print(sys.executable)'])]:
    start = now(); p = subprocess.run(argv, cwd=ROOT, text=True, capture_output=True)
    (INPUT / (label + '.stdout.txt')).write_text(p.stdout); (INPUT / (label + '.stderr.txt')).write_text(p.stderr)
    captures.append({'member': label, 'argv': argv, 'start': start, 'end': now(), 'exit': p.returncode,
                     'stdout': label + '.stdout.txt', 'stderr': label + '.stderr.txt'})
files = []
for p in sorted(INPUT.rglob('*')):
    if p.is_file():
        files.append({'path': str(p.relative_to(INPUT)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
data = {'freeze': now(), 'source_product_files': 71, 'files': files,
        'boundary': 'current product/records plus owned historical raw evidence; excludes this audit future output'}
(INPUT / 'inventory.json').write_text(json.dumps(data, indent=2) + '\n')
text = '# A-000002 Input Packet Manifest\n\n**Freeze:** ' + data['freeze'] + '\n'
text += '**Producer/custodian:** current worker/coordinator /root; authored/copied writable bytes.\n'
text += '**Owner:** A-000002 request under D-000005. **Retention:** project life + 365 days.\n'
text += '**Inventory:** inventory.json; SHA-256 `' + sha(INPUT / 'inventory.json') + '`.\n'
text += '**Current source:** 71 exact files from C-000001 after; operational views/records copied after R-000003.\n'
text += '**Independent directory locator:** `' + str(BACKUP) + '`, per-file verified after copying.\n'
text += '**Limits:** worker-controlled capture, no authenticated original conversation or historical action log; same-host copy, no physical host-loss guarantee.\n\n'
text += 'Every inventoried path has its owner/meaning in the copied record/artefact manifests.\n'
text += 'source/vp/artefacts contains exact stored evidence and raw source snapshots; links inside\nraw historical source are source data at original logical paths, not new current navigation.\n'
text += 'Current record navigation uses the complete packet source root and live request locator.\n'
text += 'A-000001 keeps its original report; V-000002 is the new worker response. Request preparation\ncopy records pre-capture scope. Final issued request is separately frozen alongside the report.\n'
text += 'No inputs are redacted or silently disposed; unknown pre-adoption facts are explicit.\n'
(INPUT / 'MANIFEST.md').write_text(text)
shutil.copytree(INPUT, BACKUP)
checked = [p for p in INPUT.rglob('*') if p.is_file()]
bad = [str(p.relative_to(INPUT)) for p in checked if sha(BACKUP / p.relative_to(INPUT)) != sha(p)]
result = {'started': started, 'ended': now(), 'captures': captures, 'input_files': len(checked),
          'independent_directory': str(BACKUP), 'copy_differences': bad,
          'inventory_sha256': sha(INPUT / 'inventory.json'), 'manifest_sha256': sha(INPUT / 'MANIFEST.md'),
          'capture': 'coordinator-controlled commands and per-file copy checks; not tamper-proof action capture'}
(HERE / 'preparation.json').write_text(json.dumps(result, indent=2) + '\n')
issued = REQUEST.read_text().replace('**Status:** preparation; not issued until packet freeze/inventory below is final.',
    '**Status:** issued; frozen before assessor dispatch.')
issued += '\n## Issued packet identities\n\n**Freeze:** ' + data['freeze'] + '\n**Inventory SHA-256:** `' + result['inventory_sha256'] + '`\n**Manifest SHA-256:** `' + result['manifest_sha256'] + '`\n**Copy verification:** ' + str(len(checked)) + ' input/index files, ' + str(len(bad)) + ' differences.\n**Preparation capture:** ../../../artefacts/A-000002/preparation.json.\n'
REQUEST.write_text(issued)
print(json.dumps({'freeze': data['freeze'], 'files': len(checked), 'copy_differences': bad,
                  'packet': str(INPUT), 'copy': str(BACKUP), 'request_sha256': sha(REQUEST)}, indent=2))
