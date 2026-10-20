#!/usr/bin/env python3
"""One new evidence batch; refuse overwrite. Not required VP software."""
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import sysconfig
import tempfile
from datetime import datetime, timezone
from pathlib import Path
import yaml

ROOT = Path('/home/alexturner/verifiable-practice')
VP = ROOT / 'vp'
HERE = VP / 'artefacts/R-000004'
PYTHON = Path('/usr/bin/python3')
COPY = Path('/home/alexturner/vp-preserved/verifiable-practice/R-000004-recovery-input')

def now():
    return datetime.now(timezone.utc).isoformat()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n' if not isinstance(value, str) else value)

def identify(path):
    path = Path(path)
    return {'path': str(path), 'resolved': str(path.resolve()),
            'symlink': os.readlink(path) if path.is_symlink() else None,
            'bytes': path.stat().st_size, 'sha256': sha(path)}

def dependency_inventory():
    roots = [('python-standard-library', Path(sysconfig.get_path('stdlib'))),
             ('installed-PyYAML', Path(yaml.__file__).parent)]
    entries = []
    for owner, base in roots:
        for directory, dirs, names in os.walk(base):
            dirs[:] = [d for d in dirs if d not in ('site-packages', 'dist-packages', '__pycache__', '.git')]
            for name in sorted(names):
                path = Path(directory) / name
                if path.is_file() and (name.endswith(('.py', '.so')) or '.so.' in name):
                    entries.append({'owner': owner, **identify(path)})
    for line in Path('/proc/self/maps').read_text().splitlines():
        name = line.split()[-1]
        if name.startswith('/') and '.so' in name and Path(name).is_file():
            entry = {'owner': 'loaded-shared-library', **identify(name)}
            if entry not in entries:
                entries.append(entry)
    return sorted(entries, key=lambda e: (e['owner'], e['path']))

if (HERE / 'results.json').exists() or COPY.exists():
    raise SystemExit('Refuse overwrite; a retry requires a new R.')
start = now()
members = []
initial_image = identify(PYTHON)
write(HERE / 'interpreter-at-start.json', {'captured': start, 'executable': initial_image,
      'sys_executable': sys.executable, 'version': sys.version, 'platform': platform.platform(),
      'machine': platform.machine(), 'yaml_version': yaml.__version__,
      'cwd': str(ROOT), 'physical_cwd': str(ROOT.resolve()),
      'relevant_environment': {k: os.environ.get(k) for k in
          ('PYTHONPATH', 'PYTHONHASHSEED', 'LC_ALL', 'LANG', 'TZ')}})
initial_deps = dependency_inventory()
write(HERE / 'dependencies-before.json', {'captured': now(), 'files': initial_deps})
# Preserve installed YAML and the actual interpreter image, not just version labels.
shutil.copyfile(PYTHON.resolve(), HERE / 'python-executable.bin')
shutil.copytree(Path(yaml.__file__).parent, HERE / 'installed-yaml',
                ignore=shutil.ignore_patterns('__pycache__'))
shutil.copyfile(VP / 'artefacts/R-000002/checks.py', HERE / 'checks.py')
shutil.copyfile(VP / 'artefacts/R-000002/skill-validator.py', HERE / 'skill-validator.py')
shutil.copyfile(VP / 'artefacts/D-000004/unit-inventory.json', HERE / 'unit-inventory.json')
shutil.copyfile(VP / 'COVERAGE.md', HERE / 'coverage-complete.md')
units = json.loads((HERE / 'unit-inventory.json').read_text())
complete = (HERE / 'coverage-complete.md').read_text()
unit = units['units'][-1]
label = f"{unit['path']}:{unit['line']} — {unit['unit']}"
row = next(line for line in complete.splitlines(keepends=True) if line.startswith('| ' + label + ' |'))
write(HERE / 'coverage-omitted.md', complete.replace(row, '', 1))
write(HERE / 'coverage-wrong-digest.md', complete.replace(row, row.replace(unit['sha256'], '0'*64), 1))
write(HERE / 'planted-inputs.json', {'removed_unit': unit, 'original_row': row,
      'complete': identify(HERE / 'coverage-complete.md'),
      'omitted': identify(HERE / 'coverage-omitted.md'),
      'wrong_digest': identify(HERE / 'coverage-wrong-digest.md')})

fixed_inputs = [HERE / 'capture.py', HERE / 'coverage_check.py', HERE / 'checks.py',
                HERE / 'skill-validator.py', HERE / 'unit-inventory.json',
                HERE / 'coverage-complete.md', HERE / 'coverage-omitted.md', HERE / 'coverage-wrong-digest.md',
                VP / 'artefacts/C-000001/before/snapshot.json', VP / 'artefacts/C-000001/after/snapshot.json']
source_identities = []
for which in ('before', 'after'):
    snapshot = VP / 'artefacts/C-000001' / which
    for item in json.loads((snapshot / 'snapshot.json').read_text())['files']:
        path = snapshot / 'source' / item['path']
        if sha(path) != item['sha256']:
            raise SystemExit('Source identity differs: ' + str(path))
        source_identities.append({'snapshot': which, **identify(path)})
for item in units['product_files']:
    if sha(ROOT / item['path']) != item['sha256']:
        raise SystemExit('Live product changed: ' + item['path'])
write(HERE / 'source-identities.json', {'captured': now(), 'files': source_identities})
write(HERE / 'instrument-inputs-before.json', {'captured': now(), 'files': [identify(p) for p in fixed_inputs]})

def run(label, arguments, expected, inputs):
    pre = identify(PYTHON)
    dependencies_pre = dependency_inventory()
    write(HERE / (label + '.dependencies-before.json'), {'captured': now(), 'files': dependencies_pre})
    input_pre = [identify(p) for p in inputs]
    started = now()
    result = subprocess.run([str(PYTHON), *map(str, arguments)], cwd=ROOT,
                            capture_output=True, text=True)
    ended = now()
    write(HERE / (label + '.stdout.txt'), result.stdout)
    write(HERE / (label + '.stderr.txt'), result.stderr)
    post = identify(PYTHON)
    dependencies_post = dependency_inventory()
    write(HERE / (label + '.dependencies-after.json'), {'captured': now(), 'files': dependencies_post})
    input_post = [identify(p) for p in inputs]
    good = (result.returncode == expected and pre == post == initial_image and
            input_pre == input_post and dependencies_pre == dependencies_post == initial_deps)
    members.append({'label': label, 'argv': [str(PYTHON), *map(str, arguments)],
        'cwd': str(ROOT), 'started': started, 'ended': ended, 'exit': result.returncode,
        'expected_exit': expected, 'executable_before': pre, 'executable_after': post,
        'dependency_before': label + '.dependencies-before.json',
        'dependency_after': label + '.dependencies-after.json', 'inputs_before': input_pre,
        'inputs_after': input_post, 'stdout': label + '.stdout.txt',
        'stderr': label + '.stderr.txt', 'criterion_met': good})
    write(HERE / 'progress.json', {'started': start, 'captured': now(), 'members': members})
    if not good:
        raise RuntimeError('Required member failed: ' + label)

after = VP / 'artefacts/C-000001/after'
before = VP / 'artefacts/C-000001/before'
run('runtime', ['-c', 'import sys,yaml; print(sys.version); print(sys.executable); print(yaml.__version__); print(yaml.__file__)'], 0, [])
for label_name, mode, base, expected in [('candidate-structural','structural',after,0),
        ('candidate-behaviour','behavior',after,0), ('baseline-negative','behavior',before,1)]:
    run(label_name, [HERE / 'checks.py', mode, base / 'source', base / 'snapshot.json'],
        expected, [HERE / 'checks.py', base / 'snapshot.json'])
run('frontmatter', [HERE / 'skill-validator.py', after / 'source'], 0,
    [HERE / 'skill-validator.py', after / 'source/SKILL.md'])
for label_name, coverage, expected in [('coverage-complete','coverage-complete.md',0),
        ('coverage-omitted','coverage-omitted.md',1), ('coverage-wrong-digest','coverage-wrong-digest.md',1)]:
    run(label_name, [HERE / 'coverage_check.py', HERE / 'unit-inventory.json', HERE / coverage, ROOT],
        expected, [HERE / 'coverage_check.py', HERE / 'unit-inventory.json', HERE / coverage])

# This preserved copy is a pre-result batch input. Final results are retained later
# in the next audit packet; never claim that this copy contains its own future output.
recovery_started = now()
recovery_image_before = identify(PYTHON)
COPY.mkdir(parents=True)
for item in units['product_files']:
    target = COPY / item['path']; target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / item['path'], target)
shutil.copytree(VP, COPY / 'vp')
copy_entries = [{'path': str(p.relative_to(COPY)), 'bytes': p.stat().st_size, 'sha256': sha(p)}
                for p in sorted(COPY.rglob('*')) if p.is_file()]
write(HERE / 'copy-inventory.json', {'captured': now(), 'location': str(COPY), 'files': copy_entries})
restore_root = Path(tempfile.mkdtemp(prefix='vp-R-000004-restore-'))
shutil.copytree(COPY, restore_root / 'project')
restored = restore_root / 'project'
differences = [e['path'] for e in copy_entries if sha(restored / e['path']) != e['sha256']]
tampered = restore_root / 'tampered-control.txt'
shutil.copyfile(COPY / copy_entries[0]['path'], tampered)
with tampered.open('ab') as stream:
    stream.write(b'\nPLANTED R4 CHANGE\n')
tamper_difference = sha(tampered) != copy_entries[0]['sha256']
members.append({'label': 'independent-directory-recovery', 'started': now(), 'ended': now(),
    'copy': str(COPY), 'restore': str(restored), 'files': len(copy_entries), 'differences': differences,
    'operation': 'shutil.copytree then SHA-256 comparison against fixed copy inventory',
    'executable_before': recovery_image_before, 'executable_after': identify(PYTHON),
    'criterion_met': not differences and recovery_image_before == identify(PYTHON) == initial_image})
members[-1]['started'] = recovery_started
members.append({'label': 'tampered-copy', 'input': identify(tampered),
    'expected_digest': copy_entries[0]['sha256'], 'operation': 'same SHA-256 comparison',
    'executable': identify(PYTHON), 'criterion_met': tamper_difference})
final_deps = dependency_inventory()
write(HERE / 'dependencies-after.json', {'captured': now(), 'files': final_deps})
final_inputs = [identify(p) for p in fixed_inputs]
write(HERE / 'instrument-inputs-after.json', {'captured': now(), 'files': final_inputs})
unchanged = (initial_deps == final_deps and identify(PYTHON) == initial_image and
             final_inputs == json.loads((HERE / 'instrument-inputs-before.json').read_text())['files'] and
             all(sha(e['path']) == e['sha256'] for e in source_identities))
members.append({'label': 'batch-identities-stable', 'criterion_met': unchanged})
write(HERE / 'results.json', {'started': start, 'ended': now(), 'members': members,
    'criterion_met': all(m['criterion_met'] for m in members),
    'claims': {'H4a': 'failed to falsify', 'H4b': 'failed to falsify', 'H4c': 'failed to falsify'},
    'limits': 'New current evidence only. Worker-controlled captures; no proof of older runtime, general efficacy or physical host-loss durability.'})
print(json.dumps({'criterion_met': all(m['criterion_met'] for m in members),
                  'members': [(m['label'], m['criterion_met']) for m in members],
                  'files_restored': len(copy_entries), 'restore': str(restored)}, indent=2))
