#!/usr/bin/env python3
"""Custody checkpoint metadata; optional instrument, not required VP software."""
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
HERE = ROOT / 'vp/artefacts/V-000006'
BUNDLE = Path('/home/alexturner/vp-preserved/verifiable-practice/completed-adoption-20261019')

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2) + '\n' if not isinstance(obj, str) else obj)

if BUNDLE.exists():
    raise SystemExit('Never overwrite a preserved checkpoint; allocate another event.')
started = now()
image = sha(Path(sys.executable))
write(HERE / 'MANIFEST.md', '# V-000006 Custody Instrument\n\n**Owner:** V-000006 under D-000009. **Producer/custodian:** worker /root.\n**Retention:** project life + 365 days after retirement; no scheduled disposal.\n**Consumer:** completed handoff and future recovery/audits.\n\n| Path | Meaning | SHA-256 |\n|------|---------|---------|\n| preserve.py | optional directory copy/checkpoint metadata instrument | `'+sha(HERE / 'preserve.py')+'` |\n\nActual completion metadata is the outer inventory/MANIFEST at `/home/alexturner/vp-preserved/verifiable-practice/completed-adoption-20261019`; it identifies this manifest and all current sealed source bytes. Same-host protection and worker-controlled capture limits apply. No historical action authentication.\n')
source = BUNDLE / 'source'
source.mkdir(parents=True)
product = json.loads((ROOT / 'vp/artefacts/C-000001/after/snapshot.json').read_text())
for entry in product['files']:
    origin = ROOT / entry['path']
    if sha(origin) != entry['sha256']:
        raise SystemExit('Accepted product changed; invalidate before relying: ' + entry['path'])
    dest = source / entry['path']; dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(origin, dest)
shutil.copytree(ROOT / 'vp', source / 'vp')
entries = []
differences = []
for path in sorted(source.rglob('*')):
    if not path.is_file():
        continue
    rel = path.relative_to(source)
    digest = sha(path)
    if digest != sha(ROOT / rel):
        differences.append(str(rel))
    owner = 'V-000006 (completed checkpoint; nested records/manifests define specific ownership)'
    entries.append({'path': 'source/' + str(rel), 'bytes': path.stat().st_size,
                    'sha256': digest, 'owner': owner})
metadata = {'started': started, 'ended': now(), 'producer': '/root worker/coordinator',
    'authority': 'D-000001/D-000009; V-000006', 'files': entries,
    'copy_differences': differences, 'source': str(ROOT), 'bundle': str(BUNDLE),
    'executable': sys.executable, 'resolved_executable': str(Path(sys.executable).resolve()),
    'executable_sha256_before': image, 'executable_sha256_after': sha(Path(sys.executable)),
    'scope': '71 accepted unchanged product files and complete post-audit record root, including sealed A-000003 output and stage-exit projections',
    'limits': 'Same-host independently located directory; no host/disk-loss or independently authenticated action guarantee. A-000003 independently assesses its earlier frozen input, not these subsequent management projections.'}
write(BUNDLE / 'inventory.json', metadata)
write(BUNDLE / 'MANIFEST.md', '# Completed Adoption Checkpoint\n\n**Owner:** V-000006 under D-000009.\n**Producer/custodian:** /root worker/coordinator, optional preserve.py directory-copy/digest capture.\n**Captured:** '+metadata['ended']+'\n**Files:** '+str(len(entries))+'; **copy differences:** '+str(len(differences))+'.\n**Inventory SHA-256:** `'+sha(BUNDLE / 'inventory.json')+'`.\n**Retention:** life + 365 days after recorded retirement; active reliance blocks disposal.\n**Consumers:** current record handoff/retention, future recovery/audits.\n\nsource/ holds the unchanged 71-file accepted product and complete current vp root, including this event/instrument, sealed A-000003 report/assessment and D-000009/S-000001/current-view checkpoint. inventory.json names every source byte and actual producer/input/executable/time/check outcome. All source bytes were compared against original inputs; no redactions or hidden disposal. Own outer metadata is not falsely self-inventoried. Nested manifests preserve specific owner/meaning/retention and historical limits. Restore source/ to a directory and compare its files against this inventory. R-000004 is the actual recorded restoration trial; this metadata records checkpoint copy verification.\n\nA-000003 remains a conformance verdict for its exact earlier prospective freeze. Post-audit projections have delegated authority and byte custody, not additional independent semantic certification. Same-host separate directory protects directory loss/accidental edits only. Capture is worker-controlled; no tamper-proof or historical-authentication claim. Read source/vp/STATE.md and check dates/triggers before fresh reliance; accepted evidence due 2026-10-26 23:59:59 UTC or earlier trigger.\n')
good = not differences and image == sha(Path(sys.executable))
print(json.dumps({'checkpoint': str(BUNDLE), 'files': len(entries),
                  'copy_differences': differences, 'runtime_stable': image == sha(Path(sys.executable)),
                  'complete': good}, indent=2))
if not good:
    raise SystemExit('Incomplete preservation; record custody gap before relying.')
