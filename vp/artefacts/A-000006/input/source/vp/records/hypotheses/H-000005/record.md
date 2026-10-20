# H-000005: Version control preserves the selected evidence bytes

**ID:** verifiable-practice:H-000005
**Type:** hypothesis
**Created:** 2026-10-19 19:19:37 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; failed to falsify for R-000006 identified index
**Origin:** [D-000010](../../decisions/D-000010/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 19:21:26 UTC

Claim: every staged regular file equals its current working bytes; all unignored new source/records are selected, including retained raw binaries/manifests. Falsifier: missing path or differing blob SHA-256. Inputs: actual index/working files after git add -A; record exact indexed blob IDs, counts and digests at execution. Positive complete comparison; negative control supplies one actually mutated in-memory blob to the same comparison function and must report that path differing. No build; ordinary Git source/custody verification. Scope excludes ignored .vp legacy originals already preserved under vp. Owner /root; review by 2026-10-26 23:59:59 UTC or index/source/filter/custody change. No action authentication or product correctness claim.

## Outcome at 2026-10-19 19:21:26 UTC

R-000006 actual comparison 2026-10-19T19:20:57.601428+00:00 through 2026-10-19T19:20:57.998629+00:00 checked 2537 indexed files and 2466 independently enumerated VP files, with zero byte differences/missing retained paths. Same byte-comparison function rejected planted changed blob; same coverage function detected the removed actual VP path. Full argv/executable/input/blob identities and outputs are in ../../../artefacts/R-000006/checkpoint-comparison/results.json. R-000005 is preserved limited first attempt, not current completeness support. Metadata-only completion/receipt staging requires a fresh source-identity guard before each D-000010-authorised commit; no technical or independent conformance verdict is extended.
