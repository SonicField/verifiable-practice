#!/usr/bin/env python3
"""Capture a new immutable audit packet without editing issued requests."""
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
VP = ROOT / 'vp'
HERE = VP / 'artefacts/A-000003'
INPUT = HERE / 'input'
BACKUP = Path('/home/alexturner/vp-preserved/verifiable-practice/A-000003-input')
REQUEST = VP / 'records/audits/A-000003/request.md'

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + '\n' if not isinstance(obj, str) else obj)

if INPUT.exists() or BACKUP.exists():
    raise SystemExit('Refuse overwrite; a successor needs another A.')
started = now()
INPUT.mkdir(parents=True)
source = INPUT / 'source'
product = json.loads((VP / 'artefacts/C-000001/after/snapshot.json').read_text())
for entry in product['files']:
    origin = ROOT / entry['path']
    if sha(origin) != entry['sha256']:
        raise SystemExit('Product changed: ' + str(origin))
    dest = source / entry['path']; dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(origin, dest)
for origin in sorted(VP.rglob('*')):
    if not origin.is_file() or origin.is_relative_to(HERE):
        continue
    dest = source / origin.relative_to(ROOT)
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(origin, dest)
shutil.copyfile(HERE / 'prepare_packet.py', INPUT / 'preparation-instrument.py')
write(INPUT / 'capture-runtime.json', {'captured': now(), 'operator': '/root worker/coordinator',
    'executable': sys.executable, 'resolved': str(Path(sys.executable).resolve()),
    'executable_sha256': sha(Path(sys.executable)), 'version': sys.version,
    'request_sha256': sha(REQUEST), 'cwd': str(ROOT),
    'capture': 'worker-controlled copy/digest operations, not authenticated action logging'})
freeze = now()
entries = []
for path in sorted(INPUT.rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(INPUT)
    parts = rel.parts
    owner, meaning = 'A-000003', 'packet preparation input / capture metadata'
    if parts[:3] == ('source', 'vp', 'artefacts') and len(parts) >= 4:
        owner, meaning = parts[3], 'exact owned raw evidence; original nested manifest defines role/retention'
    elif parts[:3] == ('source', 'vp', 'records') and len(parts) >= 5:
        owner, meaning = parts[4], 'exact record or immutable audit request/report'
    elif parts[:2] == ('source', 'vp'):
        owner, meaning = 'D-000007 / D-000008', 'current governance/coverage/handoff view at freeze'
    elif parts[0] == 'source':
        owner, meaning = 'C-000001 / D-000007', 'unchanged maintained product, present retention with legacy unknowns'
    entries.append({'path': str(rel), 'bytes': path.stat().st_size, 'sha256': sha(path),
                    'owner': owner, 'meaning': meaning})
write(INPUT / 'inventory.json', {'freeze': freeze, 'source_product_files': 71,
    'files': entries, 'excluded': 'A-000003 future report/assessment and own preparation outside input; no product exclusion'})
manifest = f'''# A-000003 Input Manifest

**Freeze:** {freeze}
**Owner:** A-000003 under D-000008. **Producer/custodian:** worker/coordinator /root.
**Request SHA-256:** `{sha(REQUEST)}`; issued request copied unchanged into source/vp/records/audits/A-000003/request.md.
**Inventory SHA-256:** `{sha(INPUT / 'inventory.json')}`.
**Product:** 71 unchanged files; 540 units, current retention D-000007, evidence R-000004.
**Preserved copy:** `{BACKUP}`, every input/index byte compared after copy.
**Retention:** project life + 365 days after retirement; no scheduled disposal; owner consumer review and new event before removal.

inventory.json maps every path to byte identity, owner and meaning; nested manifests retain original evidence roles. Current requests all resolve at source/vp paths. Exact raw historical packets, source fragments and installed dependency bytes remain evidence data with original logical locators, not new published pages. All six current views and completed records/reports are included; only this audit's future outputs and its own external preparation metadata are outside input. Preparation metadata is explicitly designated additional fixed input in the issued request. No redactions or silent disposal; missing history is unknown.

Worker controls writable captures. Hashes establish consistency, not action authenticity or historical mandate/author verification. Fresh auditor independently assesses records, not technical correctness. Same-host separate-directory preservation supports directory loss/accidental-edit recovery only; no physical host-loss guarantee. R-000004 recovery copy predates its final results; this packet preserves those completed results/current records. The assessor verifies input/request/preparation before and after and reports limitations.
'''
write(INPUT / 'MANIFEST.md', manifest)
shutil.copytree(INPUT, BACKUP)
all_files = [p for p in INPUT.rglob('*') if p.is_file()]
differences = [str(p.relative_to(INPUT)) for p in all_files if sha(p) != sha(BACKUP / p.relative_to(INPUT))]
preparation = {'started': started, 'freeze': freeze, 'ended': now(), 'files': len(all_files),
    'copy': str(BACKUP), 'copy_differences': differences, 'request_sha256': sha(REQUEST),
    'inventory_sha256': sha(INPUT / 'inventory.json'), 'manifest_sha256': sha(INPUT / 'MANIFEST.md'),
    'capture': 'worker-controlled copy/digest operations; immutable by workflow, not tamper-proof'}
write(HERE / 'preparation.json', preparation)
write(HERE / 'MANIFEST.md', '# A-000003 Preparation Evidence\n\n**Owner:** A-000003 / D-000008. **Producer/custodian:** worker /root.\n**Retention:** life + 365 days after retirement, active reliance blocks disposal.\n**Meaning:** prepare_packet.py is copy instrument; preparation.json records actual copy/count/identities. Input and future independent assessment have nested own manifests.\n\n| Path | SHA-256 |\n|------|---------|\n| prepare_packet.py | `'+sha(HERE / 'prepare_packet.py')+'` |\n| preparation.json | `'+sha(HERE / 'preparation.json')+'` |\n\nSeparate copy/input manifest above owns exact bundle. No authenticated capture or physical host-loss claim.\n')
print(json.dumps(preparation, indent=2))
if differences:
    raise SystemExit('Copy failed identity verification')
