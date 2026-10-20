#!/usr/bin/env python3
"""Optional retained coverage instrument. Its inputs and outputs are evidence."""
import hashlib
import json
import sys
from pathlib import Path

inventory_path, coverage_path, source_path = map(Path, sys.argv[1:])
inventory = json.loads(inventory_path.read_text())
rows = {}
for line in coverage_path.read_text().splitlines():
    if line.startswith('| '):
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if len(cells) >= 2:
            rows.setdefault(cells[0], []).append(cells[1].strip('`'))
missing, wrong, duplicates, source_errors = [], [], [], []
for unit in inventory['units']:
    label = f"{unit['path']}:{unit['line']} — {unit['unit']}"
    if label not in rows:
        missing.append(label)
    elif rows[label] != [unit['sha256']]:
        (duplicates if len(rows[label]) != 1 else wrong).append(label)
for item in inventory['product_files']:
    path = source_path / item['path']
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        source_errors.append(item['path'])
result = {'inventory': str(inventory_path), 'coverage_input': str(coverage_path),
          'source': str(source_path), 'expected_units': len(inventory['units']),
          'missing': missing, 'wrong_digests': wrong, 'duplicates': duplicates,
          'source_errors': source_errors}
print(json.dumps(result, indent=2))
sys.exit(bool(missing or wrong or duplicates or source_errors))
