# C-000003: Version-control enrolment and checkpoint bookkeeping

**ID:** verifiable-practice:C-000003
**Type:** change
**Created:** 2026-10-19 19:19:37 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; committed checkpoint, receipt projection follows
**Origin:** [D-000010](../../decisions/D-000010/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 19:22:46 UTC

Current owner authorises committing all existing framework changes and vp. Baseline is HEAD 38d28d10035462e4c67f4b08d66638d3a4858216 plus dirty files; historical product identities and A-000003 frozen packet remain intact. Scope: new checkpoint records, current-view projections and staging existing bytes. No maintained product content changes in this task. Before mutable views are preserved under artefacts/C-000003/before; initial Git status retained there. H/E/R-000005 checks content-faithful staging. V-000007 will record actual first commit and completion in a follow-up bookkeeping commit. Stop on hash mismatch/commit failure. Staging reversal preserves working files; committed corrections use successor records. No builds/background process. Open until verified checkpoint exists; follow-up projections are outside prior audit input.

## Actual completion at 2026-10-19 19:22:46 UTC

V-000007 records actual local checkpoint e2f63e8cbd5b2c4cd46293a759f1d6c1531f5403, exact tree ce69f829039e7609f1c272250ca422d861acdc8c, full-root R-000006 checks and preserved limitations. Existing framework/evidence bytes are committed; no maintained product content changed in this task. D-000010 authorises a follow-up current-view/receipt commit. First checkpoint contains this then-open record; successor provides sealed completion, without rewriting first-commit history. No new technical or independent audit verdict.
