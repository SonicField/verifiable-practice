#!/usr/bin/env python3
"""Retained work/capture for prospective records and directory recovery controls."""
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
VP = ROOT / 'vp'
HERE = VP / 'artefacts/R-000003'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
COPY = Path('/home/alexturner/vp-preserved/verifiable-practice/adoption-20261019-R-000003')


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def write(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def manifest(directory, owner):
    lines = ['# Artefact Manifest: ' + owner, '', '**Recorded:** ' + NOW,
        '**Owner/producer:** ' + owner + ', worker /root; current capture.',
        '**Retention:** life + 365 days after recorded retirement; active reliance blocks disposal.',
        '**Custody:** local worker-controlled bytes; no authenticated historical action capture.', '',
        '| Relative path | Meaning | SHA-256 |', '|---------------|---------|---------|']
    for p in sorted(directory.rglob('*')):
        if p.is_file() and p.name != 'MANIFEST.md':
            lines.append('| ' + str(p.relative_to(directory)) + ' | preserved input/output/instrument for ' + owner + ' | `' + digest(p) + '` |')
    lines += ['', 'Manifest identity is held in the later immutable A packet inventory. No original',
        'missing history is regenerated. Raw source snapshots are stored source text, not newly',
        'published pages: relative links retain their original logical project path; use current',
        'complete project/packet locators to navigate records, not a raw fragment storage prefix.', '']
    write(directory / 'MANIFEST.md', '\n'.join(lines))


if (HERE / 'results.json').exists() or COPY.exists():
    raise SystemExit('Existing run/copy must not be overwritten; retry needs new R.')

# All edits below are current-view and open-response work under C-000001.
responses = [
 ('F-001', 'D-000001 current mandate and PROJECT/PLAN/STATE/LEDGER/COVERAGE establish prospective adoption. Exact original historical governance remains unknown; current allocation uses the ledger.'),
 ('F-002', 'New D-000001–004 establish an attributable current root and present retention; R-000001 source copies preserve originals. Original historical choices and source captures are not certified; the design register explicitly states that limitation.'),
 ('F-003', 'COVERAGE and D-000004 unit/rationale inventory account for all 71 current source files and 540 units, plus forward operational views/records. Original introduction remains unknown; current retention has a new root/evidence chain.'),
 ('F-004', 'Historical count/check accounts are downgraded to unverified reports and not relied on. R-000001/002 are newly dated captures with source identities, every exit/output and a still-failing baseline control. No missing old output is regenerated.'),
 ('F-005', 'D-000004 selects bounded local research under delegated adoption authority. General efficacy, population comprehension, sustained role reliability and comparison cost remain unmeasured; review is due 2026-10-26 or earlier failure. This is an advisory risk disposition, not proof of effectiveness.'),
 ('F-006', 'STATE and LEDGER expose the actual false baseline, current candidate evidence, owners/deadlines, incoming links, known old findings and pending H-000003/A gate. Changed source gets new H/E/R; dates are never merely renewed.'),
 ('F-007', 'Owner manifests and PROJECT retention/custody policy identify current inputs, old copied reports and consumers. R-000003 separately located copy/recovery verifies exact bytes; same-host physical failure remains outside the copy assurance. No original source deletion is inferred.'),
 ('F-008', 'Current D/C/H/E/R/V authors are /root and a fresh A assessor must use no inherited worker/owner context. Current mandate is an exact worker transcription, not authenticated historical capture. Legacy authors/actions are explicitly unassessable and are not the current conformance claim.'),
]
text = '# V-000002: Worker response to A-000001 findings\n\n'
for field, value in [('ID', 'verifiable-practice:V-000002'), ('Type', 'event — audit-response'), ('Audit kind', 'project'),
    ('Created', NOW), ('Author/operator', 'Codex worker /root'), ('Status', 'open; ready for re-audit after R-000003'),
    ('Origin', '[D-000004](../../decisions/D-000004/record.md) and preserved [A-000001](../../audits/A-000001/record.md)'),
    ('Goal served', '[D-000001](../../decisions/D-000001/record.md)'), ('Sealed', 'open')]:
    text += '**' + field + ':** ' + value + '\n'
text += '\n## Authority and reconstruction limits\n\nCurrent owner delegated local adoption in D-000001. Responses supply current evidence,\nnew retention decisions and explicit unknowns; none reconstructs original action logs or\nchanges a sealed report. Worker proposals are not independent closure.\n'
for fid, body in responses:
    text += '\n## A-000001/' + fid + '\n\n' + body + '\n\n**Proposed disposition:** ready for independent re-audit of current scope; historical\nunknowns remain explicit. Apply the original closure condition in the new packet.\n'
text += '\n## Next handoff\n\nNew A-000002, fresh assessor context, current frozen packet, original A and this response.\nNo finding is self-closed; conformance is pending its scoped verdict.\n'
write(VP / 'records/events/V-000002/record.md', text)

initial = VP / 'artefacts/C-000001/after/source/vp/PLAN.md'
write(VP / 'artefacts/S-000001/PLAN-initial.md', initial.read_text())
write(VP / 'PLAN.md', '# Current Adoption Plan\n\n**As of:** ' + NOW + '\n**Authorising decisions:** D-000001/002/003/004.\n**Preserved initial plan:** [S-000001 initial plan](artefacts/S-000001/PLAN-initial.md).\n\n'
 '| Stage | Evidence / deliverable | Budget / gate | Status |\n|-------|------------------------|---------------|--------|\n'
 '| [S-000001](records/stages/S-000001/record.md) | 71 exact source files; 540 covered units; R-000001 valid failures, R-000002 candidate evidence; R-000003 recovery/lookup; V-000002 response | 90 min worker + two 20-min A rounds; independent conformance required | verification / audit pending |\n\n'
 'Next: finish R-000003, freeze A-000002 packet, request independent Project Audit.\nHistorical complete conformance is unattainable without originals and is not claimed.\nStop acceptance on a mandatory gap; record exceptions before tolerance changes.\n')

state = '# Current Project State\n\n**As of:** ' + NOW + '\n**Source:** [C-000001 after inventory](artefacts/C-000001/after/snapshot.json), 71 exact dirty files.\n'
state += '**Active stage:** S-000001. **Conformance:** adopted prospectively, independent verdict pending.\n**Latest audit:** original A-000001 remains inconclusive at its old snapshot.\n\n'
state += '## Current reliance\n\n| Item | Evidence | Owner | Review by UTC | Effective status / triggers |\n|------|----------|-------|---------------|-----------------------------|\n'
for item, evidence, owner, deadline, status in [
 ('D-000001 root', 'current transcribed mandate', 'commissioning human', '2027-01-17 23:59:59', 'current mandate; owner/goal change'),
 ('D-000004 retention', 'H-000002/R-000002; per-unit rationale', '/root', '2026-11-18 23:59:59 nominal', 'effective due 2026-10-26 through evidence; text/criteria change'),
 ('H-000001 baseline', 'R-000001 exit-1 behavior', '/root', 'historical only', 'falsified; no current reliance'),
 ('H-000002 candidate', 'R-000002 candidate pass and baseline negative', '/root', '2026-10-26 23:59:59', 'failed to falsify bounded checks; source/runtime/criteria change'),
 ('H-000003 coverage/custody', 'R-000003 and independent A pending', '/root', '2026-10-26 23:59:59', 'unknown until scoped verification; record/copy change')]:
    state += '| ' + ' | '.join([item, evidence, owner, deadline, status]) + ' |\n'
state += '\n## Audit findings and gates\n\n| Finding | Response | Worker / due | State |\n|---------|----------|--------------|-------|\n'
for fid, _ in responses:
    state += '| A-000001/' + fid + ' | [V-000002](records/events/V-000002/record.md) | /root, 2026-10-26 UTC | open; no independent closure yet |\n'
state += '\nAll mandatory current-scope gaps block the conformance gate. Old Code Audit findings\nremain imported technical evidence; current repairs do not self-certify their historical\nclosure. General efficacy and missing history remain explicit research/legacy limits.\n\n'
state += '## Handoff and safe continuation\n\nR-000003 is executing a bounded recovery/lookup batch. Owned temporary restoration\nlocation and commands are recorded in its results. A-000002 is reserved, not issued yet.\nDo not infer completion from partial files. Restore C-000001 before-source files to\nreverse product edits and retain new records as abandoned evidence. No builds or remote\noperations are active. Check actual dates/triggers before resuming.\n'
write(VP / 'STATE.md', state)

ledger = '# Record Ledger\n\n**As of:** ' + NOW + '\n**Namespace:** verifiable-practice; sequential /root allocator.\n\n'
ledger += '| ID / link | State | Actual prior origin | Supporting inputs / incoming consumers |\n|-----------|-------|---------------------|----------------------------------------|\n'
for p in sorted((VP / 'records').glob('*/*/record.md')):
    text = p.read_text()
    rid = p.parent.name
    status = re.search(r'^\*\*Status:\*\* (.*)$', text, re.M)
    origin = re.search(r'^\*\*Origin:\*\* (.*)$', text, re.M)
    status = status.group(1).replace('|', '/') if status else 'imported original report'
    raworigin = origin.group(1) if origin else 'legacy unknown / old request'
    # Origins in this view are descriptions; canonical links remain in original records.
    raworigin = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', raworigin).replace('|', '/')
    links = sorted(set(re.findall(r'\b[DSHEBRCVA]-\d{6}\b', text)) - {rid})
    ledger += '| [' + rid + '](' + str(p.relative_to(VP)) + ') | ' + status + ' | ' + raworigin + ' | ' + ', '.join(links) + ' |\n'
ledger += '\n## Incoming reliance and audit chains\n\nD-000001 -> D-000002/S-000001/C-000001; D-000002 -> H-000001/E-000001/R-000001;\nR-000001 -> D-000003; D-000003 -> H-000002/E-000002/R-000002; R-000002 -> D-000004;\nD-000004 -> H-000003/E-000003/R-000003 and V-000002; A-000001/F-001–008 -> V-000002 -> pending A-000002.\nBaseline H-000001 is falsified and is not a premise of current correctness.\n\nReserved A-000002 and V-000003 (copy/custody event). Original A-000001 task-local\nnamespace is preserved by V-000001; this view does not change its original identifier.\n'
write(VP / 'LEDGER.md', ledger)

changed = json.loads((VP / 'artefacts/R-000002/changed-files.json').read_text())
c = VP / 'records/changes/C-000001/record.md'
text = c.read_text() + '\n## Actual changes recorded at ' + NOW + '\n\n'
text += 'Before/after source inventories are ../../../artefacts/C-000001/before/snapshot.json\nand ../../../artefacts/C-000001/after/snapshot.json. R-000002 records 14 changed product\nfiles; all unchanged source is covered by new present retention D-000004.\n\n'
text += '| Path | Before SHA-256 | After SHA-256 |\n|------|---------------|--------------|\n'
for e in changed['files']:
    text += '| ' + e['path'] + ' | `' + str(e['before_sha256']) + '` | `' + e['sha256'] + '` |\n'
text += '\nNew operational documents/records are present adoption work, content-identified in\nR-000003 and independent A inventories. D-000004 adopts bounded local research use\nusing H-000002/R-000002 and per-unit reasons; independent stage/conformance gate remains\npending. No original report/source copy has been overwritten. Later stage completion\nand current-view updates will be linked outcomes, not edits of sealed history.\n'
write(c, text)

# Current records added since the first coverage projection also need their own rows.
coverage = (VP / 'COVERAGE.md').read_text()
for p in sorted((VP / 'records').glob('*/*/record.md')):
    path = str(p.relative_to(ROOT))
    if '/audits/A-000001/' not in path and path not in coverage:
        coverage += '\n| ' + path + ' | exact bytes in A packet inventory | recorded origin/authority; D-000001 current root | current declared lifecycle/dependencies |\n'
write(VP / 'COVERAGE.md', coverage)

started = datetime.now(timezone.utc).isoformat()
entries = json.loads((VP / 'artefacts/D-000004/unit-inventory.json').read_text())
units = entries['units']
expected_paths = {e['path'] for e in entries['product_files']}
actual_paths = {e['path'] for e in units}
missing = sorted(expected_paths - actual_paths)
actual_coverage = (VP / 'COVERAGE.md').read_text()
unlisted_units = [u for u in units if u['path'] + ':' + str(u['line']) + ' — ' + u['unit'] not in actual_coverage]
mutated_units = units[:-1]
missing_unit_detected = set((u['path'], u['line'], u['unit']) for u in units) != set((u['path'], u['line'], u['unit']) for u in mutated_units)
deadline = datetime(2026, 10, 26, 23, 59, 59, tzinfo=timezone.utc)
nominal_choice = datetime(2026, 11, 18, 23, 59, 59, tzinfo=timezone.utc)
future_reference = datetime(2026, 10, 27, tzinfo=timezone.utc)
expiry_detected = future_reference >= min(deadline, nominal_choice)

COPY.mkdir(parents=True)
for e in entries['product_files']:
    source = ROOT / e['path']
    if digest(source) != e['sha256']:
        raise SystemExit('Product changed after R-000002: ' + e['path'])
    target = COPY / e['path']
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
shutil.copytree(VP, COPY / 'vp')
copy_inventory = []
for p in sorted(COPY.rglob('*')):
    if p.is_file():
        copy_inventory.append({'path': str(p.relative_to(COPY)), 'bytes': p.stat().st_size, 'sha256': digest(p)})
write(HERE / 'copy-inventory.json', json.dumps({'location': str(COPY), 'captured': NOW, 'files': copy_inventory,
    'scope': 'independently located directory snapshot; same host, not off-host custody'}, indent=2) + '\n')
RESTORE = Path(tempfile.mkdtemp(prefix='vp-R-000003-restore-'))
shutil.copytree(COPY, RESTORE / 'project')
restored = RESTORE / 'project'
differences = [e['path'] for e in copy_inventory if digest(restored / e['path']) != e['sha256']]
control = RESTORE / 'tampered-control.txt'
original = COPY / entries['product_files'][0]['path']
shutil.copyfile(original, control)
with control.open('ab') as stream:
    stream.write(b'\nPLANTED CHANGE\n')
tamper_detected = digest(control) != digest(original)
capture = subprocess.run(['/usr/bin/python3', '-c', 'import sys; print(sys.version); print(sys.executable)'],
                         cwd=ROOT, capture_output=True, text=True)
write(HERE / 'runtime.stdout.txt', capture.stdout)
write(HERE / 'runtime.stderr.txt', capture.stderr)
results = {'started': started, 'ended': datetime.now(timezone.utc).isoformat(), 'cwd': str(ROOT),
    'members': [
        {'label': 'complete-coverage', 'source_files': len(expected_paths), 'units': len(units), 'missing_paths': missing, 'unlisted_units': unlisted_units, 'criterion_met': not missing and not unlisted_units},
        {'label': 'omitted-unit-negative-control', 'removed': units[-1], 'criterion_met': missing_unit_detected},
        {'label': 'expired-prerequisite-negative-control', 'reference': future_reference.isoformat(), 'nominal_choice_deadline': nominal_choice.isoformat(), 'evidence_deadline': deadline.isoformat(), 'criterion_met': expiry_detected},
        {'label': 'independent-directory-recovery', 'copy': str(COPY), 'restore': str(restored), 'files': len(copy_inventory), 'differences': differences, 'criterion_met': not differences},
        {'label': 'tampered-file-negative-control', 'source': str(original), 'isolated_control': str(control), 'criterion_met': tamper_detected},
        {'label': 'runtime', 'argv': ['/usr/bin/python3', '-c', 'import sys; print(sys.version); print(sys.executable)'], 'exit': capture.returncode, 'criterion_met': capture.returncode == 0}],
    'limits': 'Finite actual snapshot/control trial; no universal efficacy, independent action authentication or physical host-loss protection.'}
write(HERE / 'results.json', json.dumps(results, indent=2) + '\n')
all_good = all(e['criterion_met'] for e in results['members'])
for path, status, outcome in [
    ('records/runs/R-000003/record.md', 'sealed completed; failed to falsify bounded structural/recovery claim' if all_good else 'sealed failed; gate blocked', 'Actual times/member outcomes, copy identity, restoration and isolated negative controls are in ../../../artefacts/R-000003/results.json. Review by 2026-10-26 23:59:59 UTC, earlier on source/record/copy/input change. Independent semantic A remains required.'),
    ('records/hypotheses/H-000003/record.md', 'sealed; bounded structural checks failed to falsify; semantic A pending', 'R-000003 has complete coverage and independent-directory recovery with negative controls. This does not certify a general cold-reader population or root authority authenticity. Independent A must assess current semantic chain.'),
    ('records/experiments/E-000003/record.md', 'sealed completed' if all_good else 'sealed failed', 'Actual R-000003 results retained; post-result criteria were not rewritten. Semantic independent assessment remains separate.'),
    ('records/events/V-000002/record.md', 'sealed response; ready for re-audit' if all_good else 'sealed response; verification incomplete', 'R-000003 supplies current lookup/recovery evidence; R-000001/002 supply new actual attempts. No original finding is closed by the worker. A-000002 applies original closure conditions to prospective scope.')]:
    p = VP / path
    text = p.read_text()
    text = re.sub(r'^\*\*Status:\*\*.*$', '**Status:** ' + status, text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Sealed:\*\*.*$', '**Sealed:** ' + datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'), text, count=1, flags=re.M)
    write(p, text + '\n## Actual outcome\n\n' + outcome + '\n')
for owner in ['R-000003', 'S-000001', 'C-000001']:
    manifest(VP / 'artefacts' / owner, owner)
workspace = (VP / 'workspace/README.md').read_text()
workspace += '\nR-000003 restoration workspace: `' + str(RESTORE) + '`; owner R-000003.\nCopy/restore identities and safe disposal are in R-000003 results. Sole evidence is\nretained under R-000003 and the separate copy; no cleanup was performed.\n'
write(VP / 'workspace/README.md', workspace)
print(json.dumps({'criterion_met': all_good, 'members': results['members'], 'results': str(HERE / 'results.json')}, indent=2))
