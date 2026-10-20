# R-000006: Full retained-root and staged-byte verification

**ID:** verifiable-practice:R-000006
**Type:** run
**Created:** 2026-10-19 19:20:46 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; complete-root staging and byte comparisons passed
**Origin:** [E-000006](../../experiments/E-000006/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 19:21:26 UTC

Fresh batch after R-000005's complete-root selection limitation. Inputs actual current index, every physical vp file and unignored source; no build. Optional checker retained under artefacts/R-000006, per-file outputs/commands/times/executable hashes retained there. Physical/logical repository path /home/alexturner/verifiable-practice. Run remains open until actual results; failures preserved, future retries get new R. Owner /root; review by 2026-10-26 23:59:59 UTC, earlier source/index/filter/runtime/custody change.

## Outcome at 2026-10-19 19:21:26 UTC

R-000006 actual comparison 2026-10-19T19:20:57.601428+00:00 through 2026-10-19T19:20:57.998629+00:00 checked 2537 indexed files and 2466 independently enumerated VP files, with zero byte differences/missing retained paths. Same byte-comparison function rejected planted changed blob; same coverage function detected the removed actual VP path. Full argv/executable/input/blob identities and outputs are in ../../../artefacts/R-000006/checkpoint-comparison/results.json. R-000005 is preserved limited first attempt, not current completeness support. Metadata-only completion/receipt staging requires a fresh source-identity guard before each D-000010-authorised commit; no technical or independent conformance verdict is extended.
