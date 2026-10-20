#!/usr/bin/env python3
"""Optional retained verification instrument; not required VP software."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def visible(text):
    active = None
    out = []
    for line in text.splitlines():
        m = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
        if m:
            marker, suffix = m.groups()
            if active is None:
                active = marker
            elif marker[0] == active[0] and len(marker) >= len(active) and not suffix.strip():
                active = None
            out.append('')
        else:
            out.append(line if active is None else '')
    return '\n'.join(out), active


def structural(base, names, skill_override=None):
    errors = []
    count = 0
    for name in names:
        p = base / name
        if not p.is_file():
            errors.append('missing file: ' + name)
            continue
        if not name.endswith('.md'):
            continue
        text = (Path(skill_override) if name == "SKILL.md" and skill_override else p).read_text()
        body, fence = visible(text)
        if fence:
            errors.append('fence: ' + name)
        if not text.endswith('\n'):
            errors.append('newline: ' + name)
        destinations = re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', body)
        destinations += re.findall(r'^\s*\[[^\]]+\]:\s+(\S+)', body, re.M)
        for dest in destinations:
            dest = dest.strip().split(' "', 1)[0].strip('<>')
            if '<' in dest or '>' in dest:
                continue
            split = urlsplit(dest)
            if split.scheme or dest.startswith('//') or not split.path:
                continue
            count += 1
            if not (p.parent / unquote(split.path)).exists():
                errors.append(name + ' -> ' + dest)
    skill = (Path(skill_override) if skill_override else base / 'SKILL.md').read_text()
    for name in names:
        if name.endswith('.md') and name.startswith(('concepts/', 'playbooks/', 'docs/', 'standards/')):
            if '](' + name + ')' not in skill:
                errors.append('missing skill route: ' + name)
    for op in ('decision', 'stage', 'hypothesis', 'experiment', 'build', 'run', 'change', 'event', 'audit', 'audit-response'):
        text = (base / ('templates/project-records/' + op + '.md')).read_text()
        for field in ('ID', 'Type', 'Created', 'Author/operator', 'Status', 'Origin', 'Goal served', 'Sealed'):
            if '**' + field + ':**' not in text:
                errors.append(op + ': missing ' + field)
    return {'files': len(names), 'local_destinations': count, 'errors': errors,
            'limits': 'File destinations/fences/routes/fields only; no rendering or external URL certification.'}


def block(base, name, function):
    return next(b for b in re.findall(r'```python\n(.*?)\n```', (base / name).read_text(), re.S)
                if 'def ' + function + '(' in b)


def behavior(base):
    issues = []
    observations = []
    source = block(base, 'concepts/engineering-standards.md', 'transfer_funds')
    for optimisation in (0, 1, 2):
        ns = {}
        exec(compile(source, 'retained transfer example', 'exec', optimize=optimisation), ns)
        for label, amount, expected in [('negative', -5, None), ('overdraft', 20, None), ('valid', 3, (7, 3))]:
            sender = type('Account', (), {'balance': 10})()
            receiver = type('Account', (), {'balance': 0})()
            error = None
            try:
                ns['transfer_funds'](sender, receiver, amount)
            except Exception as e:
                error = type(e).__name__
            actual = (sender.balance, receiver.balance)
            good = (error is not None and actual == (10, 0)) if expected is None else (error is None and actual == expected)
            observations.append({'case': label, 'optimisation': optimisation, 'error': error,
                                 'balances': actual, 'criterion_met': good})
            if not good:
                issues.append('transfer/' + str(optimisation) + '/' + label)
    ns = {}
    exec(block(base, 'WHY.md', 'validate_email'), ns)
    cases = {'@.': True, 'user@localhost': False, 'user@[192.168.1.1]': True,
             'user+tag@example.com': True, 'user@example..com': True}
    for value, expected in cases.items():
        actual = ns['validate_email'](value)
        observations.append({'email': value, 'actual': actual, 'expected_function_result': expected})
        if actual != expected:
            issues.append('email execution mismatch: ' + value)
    text = (base / 'WHY.md').read_text()
    if '`"user@[192.168.1.1]"` fails' in text:
        issues.append('email text falsely reports rejection')
    if 'fails on 40%' in text:
        issues.append('unmeasured forty-percent outcome reported')
    for p in (base / 'concepts').glob('*.md'):
        if 'If you cannot clearly recall reading each one, read them now.' in p.read_text():
            issues.append('forced pillar loading: ' + p.name)
    role = (base / 'concepts/zero-code-contract.md').read_text()
    if 'default human-owner arrangement' not in role or 'mandate' not in role:
        issues.append('default human/AI-owner applicability not stated')
    return {'cases': observations, 'issues': issues,
            'limits': 'Bounded executable outcomes and literal contracts, not independent AI behavior or email-standard conformance.'}



parser=argparse.ArgumentParser()
parser.add_argument('base');parser.add_argument('inventory');parser.add_argument('--override-skill')
args=parser.parse_args();names=[e['path'] for e in json.loads(Path(args.inventory).read_text())['files']]
result=structural(Path(args.base),names,args.override_skill);print(json.dumps(result,indent=2));sys.exit(bool(result['errors']))
