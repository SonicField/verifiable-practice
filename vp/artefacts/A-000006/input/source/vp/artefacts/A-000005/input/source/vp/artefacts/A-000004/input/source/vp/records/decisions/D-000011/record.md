# D-000011: Include ignored nested evidence explicitly and strengthen coverage verification

**ID:** verifiable-practice:D-000011
**Type:** decision
**Created:** 2026-10-19 19:20:46 UTC
**Author/operator:** Codex worker /root
**Status:** selected; sealed
**Origin:** [D-000010](../D-000010/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 19:20:46 UTC

Observation: initial R-000005 reports matching bytes for 2,222 indexed files, but root .gitignore's .vp/ rule also excludes nested legacy audit evidence inside owned VP source snapshots. General requirement: selection completeness must enumerate the retained bundle independently of repository ignore rules; matching selected bytes cannot establish complete custody. The owner explicitly asked for vp and all new changes.

Select git add -f -- vp to include every owned retained file, preserving existing ignore policy and product bytes. Top-level ignored .vp originals remain separately imported legacy inputs; only owned vp bundle is forced into tracking. Reject dropping nested evidence or changing sealed snapshots. New E/R-000006 independently enumerates every vp regular file, checks all are indexed and byte-identical, with actual omitted-path and changed-blob controls using the same checker. R-000005 remains limited initial comparison, insufficient complete-root evidence; do not overwrite its captured results. Same D-000010 authority and two local commit/checkpoint-receipt scope. C-000003 remains open. Owner /root; review by 2026-10-26 23:59:59 UTC or source/index/filter/custody change. No new technical validity, audit scope or product changes.
