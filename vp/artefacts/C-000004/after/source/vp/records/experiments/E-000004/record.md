# E-000004: Execute fresh evidence with byte identities and actual coverage defects

**ID:** verifiable-practice:E-000004
**Type:** experiments
**Created:** 2026-10-19 12:24:46 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; completed, bounded claims failed to falsify
**Origin:** [D-000006](../../decisions/D-000006/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 12:27:00 UTC

## Pre-action protocol

Use H-000004. R-000004 copies the unchanged prior checks.py and validator, byte-identifies them and every source/dependency input. Preserve exact complete COVERAGE text; remove one declared row into a separate omitted input, and change one SHA-256 into a separate changed-identity input. The same coverage_check.py parses expected unit labels from the fixed D-000004 inventory and must accept complete input (exit 0), reject omitted input (exit 1, names that unit), and reject wrong digest (exit 1). A planted input must be supplied as the actual command argument, never just compared independently.

Label members: runtime; candidate-structural; candidate-behaviour; baseline-negative (expected 1); frontmatter; coverage-complete; coverage-omitted (expected 1); coverage-wrong-digest (expected 1); independent-directory-recovery; tampered-copy (expected detected). Candidate/source and harness bytes must match retained inventories. Executable symlink and resolved file digest, Python runtime, installed standard-library tree and PyYAML tree inventory, OS/architecture and working paths are captured before/after. External commands must have per-member times/argv/cwd/executable/input identities/stdout/stderr/status. Capture script runs under the same hashed Python; own pre/post image and inputs retained.

No compiled build: interpreted teaching examples and source checks only. Do not execute legacy captures. New preservation copy is a distinct directory, not overwrite; restore into a new workspace. Criterion: every required expected exit/identity/control meets its stated prediction. Stop/inconclusive on unexpected runtime/input identity change, missing output or failed setup; retain even incomplete evidence and allocate a new R for retry. Evidence authenticity remains worker-controlled. No technical correctness/population efficacy or physical host-loss claim. Budget: existing S-000001 worker allowance, audit round 2 after a separate adopting decision. Preserve before/after views; no source changes.

## Actual outcome

Actual batch start/end 2026-10-19T12:25:44.930331+00:00 / 2026-10-19T12:25:46.991861+00:00. [Retained results](../../../artefacts/R-000004/results.json) identify every member. Candidate structure/behaviour/frontmatter exit 0; baseline-negative exit 1 as expected. Complete coverage exit 0; actual omitted row and changed digest inputs each exit 1 naming the planted unit. Interpreter, standard-library, installed YAML, loaded shared-library and fixed-input identities remain stable before/after. New separate-directory recovery restores 1,238 inventoried files without differences; isolated tampered input detected. H4a/H4b/H4c each failed to falsify within this scope. No older runtime is authenticated. Worker-controlled evidence; general efficacy and physical host-loss recovery remain unverified. Owner /root, review by 2026-10-26 23:59:59 UTC or earlier source/runtime/criteria/custody changes. Independent A pending.
