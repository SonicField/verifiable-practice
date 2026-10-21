# Code Audit

Audit a codebase against the [engineering standards](../concepts/engineering-standards.md), produce a prioritised report, and—only when authorised—repair violations with adversarial tests.

Auditing and fixing are separate decisions. A request to inspect code authorises a report, not source changes.

**Audit kind:** `code`. Use this only after an explicit kind has been selected
through [Audit Routing](audit-routing.md). For an ambiguous “Please audit X”,
ask the intended kind and wait before inspecting. Project-record conformance
uses [Project Audit](record-audit.md) with a separate assessor contract.

## Phase 1: Scope

1. Identify languages, source roots, test commands, generated code, vendored code, and build artefacts.
2. Exclude trivial re-export files unless they contain behaviour.
3. Record the exact file set and exclusions in the report.
4. For a large codebase, propose a bounded first batch or ask the user to approve the cost before broad parallel analysis.

## Phase 2: Audit

Read the engineering standards and any project-specific standards. Apply their compatible union; report conflicts instead of silently choosing one.

For every finding, record:

1. file and line;
2. violated invariant or standard;
3. severity;
4. observed or plausible failure mode;
5. specific repair;
6. a test that would fail without the repair.

Use these severities:

| Severity | Meaning |
|----------|---------|
| BUG | Current behaviour can be wrong, corrupting, or unreachable |
| SECURITY | A weakness affects trust boundaries, sensitive data, or failure visibility |
| HARDENING | A missing guard or invariant makes future faults harder to detect |

Focus on missing preconditions, postconditions, and invariants; silent error swallowing; assertions without useful diagnostics; unsupported promises; unreachable guards; and missing dynamic analysis where the language requires it. Do not inflate counts with style preferences.

Independent files may be reviewed concurrently when the host supports bounded parallel work. Parallelism is an optimisation, not part of the method. Never launch unbounded work, and never let concurrent reviewers edit the same files.

## Phase 3: Consolidate

Write a durable code-audit report, by default `.vp/code-audit-report.md`, containing:

- audit kind `code` and applied engineering standards;
- scope and exclusions;
- counts by severity and category;
- findings ordered by severity;
- files ranked by material risk, not raw count;
- unsupported or unfalsifiable claims;
- uncertainty and likely false positives;
- the exact verification command for each proposed repair.

Present this report before changing code.

In a project conforming to the record standard, preserve the report as
technical evidence with its owning level-appropriate entry and a manifest
when raw evidence requires one (A/B run records, C inline run, D change/check), in the chosen
record root. It is not an A project-conformance report. Existing historical
`audit-report.md` files remain preserved; identify their kind in the catalogue
rather than renaming or rewriting their evidence.

## Phase 4: Repair, If Authorised

For each repair:

1. Write a test that exposes the defect or missing guarantee.
2. Run it and confirm the expected pre-fix failure. If the test already passes, reassess the finding.
3. Make the smallest repair that satisfies the stated invariant.
4. Run the focused test and relevant static or dynamic analysis.
5. Run the full applicable suite after all focused checks pass.
6. Record commands, exit status, failures, skipped checks, and environmental limitations.

Adversarial cases should include applicable empty values, boundaries, malformed input, type confusion, resource limits, concurrency, and reordering. Do not add an assertion merely to satisfy a checklist: every assertion must express a real contract and have a meaningful failure message.

## Completion Criteria

The audit is complete when the reviewed scope and exclusions are explicit, every finding is evidence-backed and reproducible, and uncertainty is reported. A repair is complete only when its test was shown to detect the original gap, the focused verification passes, and broader regression checks have run or are explicitly documented as unavailable.
