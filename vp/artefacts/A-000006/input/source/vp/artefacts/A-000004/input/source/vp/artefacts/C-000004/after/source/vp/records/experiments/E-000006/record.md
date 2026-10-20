# E-000006: Verify complete VP custody independently of ignore rules

**ID:** verifiable-practice:E-000006
**Type:** experiment
**Created:** 2026-10-19 19:20:46 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; declared controls passed
**Origin:** [D-000011](../../decisions/D-000011/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 19:21:26 UTC

Use H-000005's byte-preservation claim with explicit strengthened bundle enumeration after R-000005 selection limitation. Enumerate all vp regular files independently of Git ignore rules; compare that required path set against actual git ls-files --stage and compare all actual indexed Git blob bytes to working bytes. Stage owned bundle with git add -f -- vp plus all unignored framework changes. Positive complete paths/bytes expected no differences; remove one actual vp entry in an isolated in-memory index list and run the same coverage function, expected that path missing; append a byte to one actual blob and run the same byte-comparison function, expected that path differing. No working/index mutation by controls. Preserve commands, times, executable hashes, indexed inputs and results. New R-000006 is a fresh attempt, not an overwritten retry. Subsequent metadata-only bookkeeping source checks use the same guard before each authorised commit; their concrete input trees are Git identities, not renewal of technical claims. Stop on mismatch; maintain C-000003 open until actual commit/receipt. No build or project execution. Review by 2026-10-26 23:59:59 UTC or input/filter/runtime/custody change.

## Outcome at 2026-10-19 19:21:26 UTC

R-000006 actual comparison 2026-10-19T19:20:57.601428+00:00 through 2026-10-19T19:20:57.998629+00:00 checked 2537 indexed files and 2466 independently enumerated VP files, with zero byte differences/missing retained paths. Same byte-comparison function rejected planted changed blob; same coverage function detected the removed actual VP path. Full argv/executable/input/blob identities and outputs are in ../../../artefacts/R-000006/checkpoint-comparison/results.json. R-000005 is preserved limited first attempt, not current completeness support. Metadata-only completion/receipt staging requires a fresh source-identity guard before each D-000010-authorised commit; no technical or independent conformance verdict is extended.
