# H-000004: Current evidence has identified instruments and discriminating controls

**ID:** verifiable-practice:H-000004
**Type:** hypotheses
**Created:** 2026-10-19 12:24:46 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; completed, bounded claims failed to falsify
**Origin:** [D-000006](../../decisions/D-000006/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 12:27:00 UTC

## Claims fixed before execution

H4a: the exact unchanged 71-file candidate satisfies the same structural/example/frontmatter contracts as E-000002; original baseline still fails the same behaviour checker. Falsifier: candidate error, source mismatch or baseline unexpectedly passes.

H4b: the coverage instrument accepts complete coverage, rejects an actual omitted source-unit row, and rejects a changed file identity. Falsifier: complete rejected, omitted/changed input accepted, or planted input not actually supplied to the same instrument. Each case retains input and actual stdout/stderr/exit.

H4c: an identified separate-directory snapshot restores all required bytes, with a modified isolated copy detected by the same digest comparison. Falsifier: restore mismatch, hidden source consultation for restored bytes, or tampered input accepted.

Shared assumptions: worker-controlled captures are authentic descriptions, not independent authentication; exact executable and relevant installed dependencies are captured immediately before/after every external member and stable throughout batch. Inputs: R-000002 before/after snapshots, D-000004 unit inventory, actual current COVERAGE frozen into R-000004. Owner /root; review by 2026-10-26 23:59:59 UTC, earlier source/runtime/checker/criteria/record/custody change. Separate verdict for each claim. Independent A semantic assessment is still needed; no general efficacy, historical execution proof or host-loss protection.

## Actual outcome

Actual batch start/end 2026-10-19T12:25:44.930331+00:00 / 2026-10-19T12:25:46.991861+00:00. [Retained results](../../../artefacts/R-000004/results.json) identify every member. Candidate structure/behaviour/frontmatter exit 0; baseline-negative exit 1 as expected. Complete coverage exit 0; actual omitted row and changed digest inputs each exit 1 naming the planted unit. Interpreter, standard-library, installed YAML, loaded shared-library and fixed-input identities remain stable before/after. New separate-directory recovery restores 1,238 inventoried files without differences; isolated tampered input detected. H4a/H4b/H4c each failed to falsify within this scope. No older runtime is authenticated. Worker-controlled evidence; general efficacy and physical host-loss recovery remain unverified. Owner /root, review by 2026-10-26 23:59:59 UTC or earlier source/runtime/criteria/custody changes. Independent A pending.
