#!/usr/bin/env python3
"""Retained worker transcription/indexing action; records remain plain Markdown."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/alexturner/verifiable-practice')
VP = ROOT / 'vp'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
AFTER = VP / 'artefacts/C-000001/after'
inventory = json.loads((AFTER / 'snapshot.json').read_text())
files = inventory['files']

specific = {
 'SKILL.md': 'Keeps task selection, explicit audit kinds, proportional verification and authority/record routing at the entry point; needed so a future worker knows which contract applies.',
 'README.md': 'Provides the reader entry path, adoption boundary and navigation; preserves usable access to the framework and current conformance state.',
 'WHY.md': 'Explains why adversarial evidence is needed; retains the simple validator as a deliberately inadequate demonstration with current observed outcomes and no claimed failure rate.',
 'ORIGIN.md': 'Preserves attributed extraction lineage and later design-source accounts; retained as historical assertions with unknown original authority/capture, not authenticated evidence.',
 'CHANGELOG.md': 'Keeps a human-readable change summary; operational C/D/R records, rather than this summary, establish actual adoption provenance.',
 'CONTRIBUTING.md': 'Sets contribution/validation boundaries for maintaining a portable instruction framework; requirements are selected policy and do not prove general outcomes.',
 'SECURITY.md': 'Defines reporting and safe-use boundaries; retained as project policy with no claim that deployment security has been established.',
 'CODE_OF_CONDUCT.md': 'States participation expectations and escalation; retained governance policy, not an empirical technical claim.',
 'LICENSE': 'Preserves existing licence text and attribution; no legal sufficiency certification is claimed.',
 'CITATION.cff': 'Preserves citation metadata for research attribution; legal and citation-schema validation remain outside this technical trial.',
 '.gitignore': 'Keeps editor/disposable exclusions explicit; ignored old .vp evidence is separately preserved under owned vp artefacts so it is not mistaken for clone-backed custody.',
 '.gitattributes': 'Preserves repository text-handling policy; exact raw evidence is copied by bytes rather than relying on implicit normalisation.',
 'concepts/goals.md': 'Separates terminal goals from instrumental steps so work can be traced to a purpose and drift identified.',
 'concepts/falsifiability.md': 'Defines claims and disconfirming observations so tests can alter decisions rather than merely demonstrate examples.',
 'concepts/rhetoric.md': 'Exposes persuasion and audience effects when evaluating claims; interpretive guidance remains bounded research policy.',
 'concepts/bullshit-detection.md': 'Keeps observation, assurance and evidence distinguishable; enables questioning unsupported certainty rather than accepting fluent narration.',
 'concepts/verification-cycle.md': 'Organises design/check/change/learning steps; optional onboarding now respects task-specific loading.',
 'concepts/zero-code-contract.md': 'Separates goal/acceptance responsibility from implementation, qualifies default human ownership and routes bounded AI mandates without granting worker self-authority.',
 'concepts/pte.md': 'Provides precise contract wording for independently checkable decisions and failure conditions.',
 'concepts/engineering-standards.md': 'Retains a proposed verification-oriented engineering policy and its examples; caller rejection is now optimisation-safe. Broader engineering claims remain research guidance, not correctness certification.',
 'standards/project-records.md': 'Defines the adopted record contract: identity, temporal choice/evidence chains, expiry, custody, independent assessment and actor-neutral authority; conformance concerns record discipline only.',
 'docs/project-records-design.md': 'Preserves explained inspirations/generalisation/alternatives. Legacy test counts, source excerpts and ordering assertions are explicitly unverified; new current records supply present justification.',
 'docs/project-records-examples.md': 'Teaches code and document traces using labelled fictional histories; candidate syntax and reader evidence are now distinct. These examples are not real executed project records.',
 'docs/project-records-scenarios.md': 'Defines future discriminating behavioural/cost trials; retains unexecuted tests as plans, never as observations. Current audit is one bounded trial only.',
 'playbooks/audit-routing.md': 'Enforces asking and waiting for ambiguous audit requests, separate project/code roles and verdicts; current invocation is explicitly typed project.',
 'playbooks/record-audit.md': 'Directs a separate-context assessor through fixed inputs, findings and independent closure without solving technical work.',
 'playbooks/code-audit.md': 'Scopes engineering findings and separately authorised repairs; its R technical report cannot substitute for an A project verdict.',
 'playbooks/review.md': 'Provides a short reasoning review without claiming independent project conformance or switching into implementation.',
}


def purpose(name):
    if name in specific:
        return specific[name]
    if name.startswith('.github/'):
        return 'Retains contribution/reporting templates as governance input; no hosted workflow or UI behaviour is asserted.'
    if name.startswith('templates/project-records/'):
        role = Path(name).stem
        return 'Retains the ' + role + ' Markdown template to expose required fields and handoff meaning without software; placeholders are instructions for future records, not instantiated history.'
    if name.startswith('playbooks/'):
        return 'Retains the ' + Path(name).stem + ' bounded procedure to make the related reasoning/verification task repeatable, with explicit evidence and authority limits rather than automatic implementation.'
    if name.startswith('docs/'):
        return 'Retains the ' + Path(name).stem + ' explanatory guide for human/future-worker understanding; the routed standard/playbook, rather than illustrative prose, controls execution.'
    return 'Retains existing project support content for the declared framework scope; unknown original introduction is preserved and no external validity is certified.'


rows = []
reasons = ['# Present Retention Reasons: D-000004', '', '**Recorded:** ' + NOW,
 '**Source:** exact R-000002/C-000001 after snapshot; current worker interpretation.',
 '**Legacy:** original introduction/authorship/authority and unretained historical tests remain unknown.', '',
 'These are new retention reasons, not recovered past intent. Content is retained as bounded',
 'research instructions/policy. Current static/example claims use H-000002/R-000002;',
 'broader efficacy, scientific generalisations, legal correctness and AI adherence are unverified.', '']
for entry in files:
    name = entry['path']
    p = AFTER / 'source' / name
    reason = purpose(name)
    reasons += ['## ' + name, '', reason, '',
        '**Alternatives:** discard (loses the stated function), retain unsupported historical assurance',
        '(rejected), or retain current content with bounded evidence and unknown history (selected).',
        '**Review/falsifier:** revise on source/goal/contract change, a failed current trace/check,',
        'or evidence that the stated function conflicts with the adopted scope. Effective review',
        'by 2026-10-26 UTC through verification dependencies. No per-file original authorship is inferred.', '']
    sections = [(1, 'whole file')]
    if name.endswith('.md'):
        headings = [(i, line.strip('# ').replace('|', '/')) for i, line in enumerate(p.read_text().splitlines(), 1)
                    if re.match(r'^#{1,4} ', line)]
        sections = [(1, 'file/preamble')] + headings
    for line, unit in sections:
        rows.append((name, line, unit, entry['sha256']))
reasons += ['## Unit granularity', '',
 'Coverage uses a preamble row plus heading/section rows for Markdown and whole-file rows',
 'for small support/configuration files. A section belongs to the named file function above;',
 'its specific contract/text is preserved at exact bytes, so the reader can inspect what is',
 'retained. D-000003 separately explains the repaired examples/routing/owner distinctions.',
 'This mapping explains current retention without claiming empirical validation of every',
 'sentence. Normative choices and unverified background claims are distinguished above.', '']
(VP / 'artefacts/D-000004/coverage-rationale.md').write_text('\n'.join(reasons))
coverage = ['# Current Maintained Artefact Coverage', '', '**As of:** ' + NOW,
 '**Product snapshot:** [R-000002 after inventory](artefacts/C-000001/after/snapshot.json), 71 files.',
 '**Origin:** [D-000004 present retention](records/decisions/D-000004/record.md).',
 '**Introducing/current retaining change:** C-000001; historical introductions are unknown.',
 '**Current dependency deadline:** 2026-10-26 UTC; earlier relevant source/contract/custody change.',
 '**Semantic limits:** current static/example claims are bounded; general efficacy and historical',
 'authenticity remain unverified. Root/current views are externally content-identified at A freeze,',
 'so COVERAGE does not falsely claim a self-digest. Raw snapshots are owned evidence.', '',
 '| Path / current unit | SHA-256 of exact containing file | Current retaining choice / evidence | Legacy / validity |',
 '|---------------------|----------------------------------|------------------------------------|-------------------|']
for name, line, unit, sha in rows:
    coverage.append('| ' + name + ':' + str(line) + ' — ' + unit + ' | `' + sha + '` | C-000001 / D-000004; H-000002/R-000002 for bounded current checks; file reason in D-000004 rationale | old introduction unknown; research policy / current evidence due 2026-10-26 |')
coverage += ['', '## Forward operational views and records', '',
 '| Unit | Identity locator | Justification / evidence | Validity |',
 '|------|------------------|--------------------------|----------|']
for name in ['README.md', 'PROJECT.md', 'PLAN.md', 'STATE.md', 'LEDGER.md', 'COVERAGE.md', 'workspace/README.md']:
    coverage.append('| vp/' + name + ' | exact bytes in independent A packet inventory | D-000001/D-000002; C-000001; H-000003/R-000003 and independent A | current tracking view, dated; check actual dependencies on resume |')
for p in sorted((VP / 'records').glob('*/*/record.md')):
    if 'audits/A-000001/' in str(p):
        continue
    coverage.append('| ' + str(p.relative_to(ROOT)) + ' | exact bytes in A packet inventory | recorded prior origin, owner/rationale, retained evidence; D-000001 root | declared per record; seal/append-only lifecycle |')
coverage += ['', '## Legacy evidence and exclusions', '',
 'A-000001 and the old Code Audit retain their original identifiers/verdicts. V-000001',
 'and R-000001 import their custody; they are not reconstructed pre-adoption origin nodes.',
 'All artefacts and preserved copies have owning IDs/manifests; treating them as raw inputs',
 'does not exclude current own source from coverage. .git internals, editor files, external',
 'repository code and unproduced binaries are outside the product snapshot, explicitly.',
 'No historical complete conformance or general effectiveness is asserted.', '']
(VP / 'COVERAGE.md').write_text('\n'.join(coverage))
(VP / 'artefacts/D-000004/unit-inventory.json').write_text(json.dumps({'product_files': files,
    'units': [{'path': name, 'line': line, 'unit': unit, 'sha256': sha} for name, line, unit, sha in rows],
    'created': NOW}, indent=2) + '\n')


def finish(path, status, outcome):
    p = VP / path
    text = p.read_text()
    text = re.sub(r'^\*\*Status:\*\*.*$', '**Status:** ' + status, text, count=1, flags=re.M)
    text = re.sub(r'^\*\*Sealed:\*\*.*$', '**Sealed:** ' + NOW, text, count=1, flags=re.M)
    p.write_text(text + '\n## Recorded outcome at ' + NOW + '\n\n' + outcome + '\n')


for rid in ['R-000001', 'R-000002']:
    data = json.loads((VP / 'artefacts' / rid / 'results.json').read_text())
    body = '**Actual start/end:** ' + data['started'] + ' / ' + data['ended'] + '.\n\n'
    body += '| Member | Exit | Retained evidence |\n|--------|------|-------------------|\n'
    for r in data['members']:
        body += '| ' + r['member'] + ' | ' + str(r['exit']) + ' | artefacts/' + rid + '/' + r['stdout'] + '; ' + r['stderr'] + ' |\n'
    body += '\nExact argv/cwd/times are in ../../../artefacts/' + rid + '/results.json. '
    if rid == 'R-000001':
        body += 'Behaviour validly falsified the baseline claim; structural/frontmatter observations are bounded. No after-source inference. Historical missing captures remain unknown.'
    else:
        body += 'Candidate checks failed to falsify H-000002; baseline-negative exit 1 is the required instrument control. Scope excludes general efficacy. Owner /root; accepted bounded outcome review by 2026-10-26 UTC, earlier on checked inputs/criteria/runtime change.'
    finish('records/runs/' + rid + '/record.md', 'sealed completed; baseline falsified' if rid == 'R-000001' else 'sealed completed; candidate failed to falsify bounded claim', body)
finish('records/hypotheses/H-000001/record.md', 'sealed; falsified for starting inputs', 'R-000001 behavior observations falsified the starting consistency claim. Superseded for current reliance by new H-000002; original verdict remains.')
finish('records/hypotheses/H-000002/record.md', 'sealed; failed to falsify for candidate inputs', 'R-000002 tests candidate actual bytes, with retained baseline negative control. No general AI behavior/correctness guarantee. Evidence and this claim are due 2026-10-26 UTC or earlier trigger.')
finish('records/experiments/E-000001/record.md', 'sealed; completed with baseline falsification', 'R-000001 outcomes led to D-000003 targeted repairs, not rewritten criteria. All member outcomes retained.')
finish('records/experiments/E-000002/record.md', 'sealed; completed', 'R-000002 candidate passes and original negative control remains failing; D-000004 selects bounded current retention.')
for did in ['D-000001', 'D-000002', 'D-000003']:
    finish('records/decisions/' + did + '/record.md', 'sealed; selected choice recorded', 'Current mandate/choice acted upon through C-000001 and the linked protocols/runs. This does not seal a completed stage or declare conformance; independent A remains required.')
finish('records/decisions/D-000004/record.md', 'sealed; bounded local research retention', 'Complete product unit/rationale inventory written. R-000002 supports only declared current checks. Stage/conformance gate pending R-000003 and independent A; old history remains unknown.')
finish('records/events/V-000001/record.md', 'sealed; legacy imported with custody limits', 'R-000001 legacy copies/inventory preserve exact old bytes. No originals removed and no historical findings self-closed. A follow-up response and current recovery result are separate records.')

for owner in ['D-000001', 'D-000004', 'R-000001', 'R-000002', 'C-000001']:
    directory = VP / 'artefacts' / owner
    table = ['# Artefact Manifest: ' + owner, '', '**Owner:** records for ' + owner + '; current worker /root.',
             '**Recorded:** ' + NOW, '**Retention:** project life + 365 days after recorded retirement; active consumers prevent disposal.',
             '**Custody:** worker-controlled directory; SHA-256 consistency is not authenticated action history.',
             '**Independent copy:** R-000003 will identify recovery location; pending until its result.', '',
             '| Relative path | Meaning / producer | SHA-256 | Retention |',
             '|---------------|--------------------|---------|-----------|']
    for p in sorted(directory.rglob('*')):
        if p.is_file() and p.name != 'MANIFEST.md':
            rel = str(p.relative_to(directory))
            meaning = 'source/input snapshot' if '/source/' in '/' + rel else ('raw command output/status' if rel.endswith(('.txt', 'results.json')) else 'retained input/check instrument/index/rationale')
            table.append('| ' + rel + ' | ' + meaning + '; owner ' + owner + ' | `' + hashlib.sha256(p.read_bytes()).hexdigest() + '` | retained while relied on; life + 365 days |')
    table += ['', 'This manifest is an index; its own identity is in external frozen packet inventories.',
              'No redaction or disposition has occurred in these copies. The original missing history remains unknown.', '']
    (directory / 'MANIFEST.md').write_text('\n'.join(table))
print(json.dumps({'product_files': len(files), 'section_units': len(rows), 'records_finalised': 11,
                  'outcome_time': NOW, 'pending': 'R-000003, V response, independent A'}, indent=2))
