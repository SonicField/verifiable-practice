# C-000003: Version-control enrolment and checkpoint bookkeeping

**ID:** verifiable-practice:C-000003
**Type:** change
**Created:** 2026-10-19 19:19:37 UTC
**Author/operator:** Codex worker /root
**Status:** open
**Origin:** [D-000010](../../decisions/D-000010/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** open

Current owner authorises committing all existing framework changes and vp. Baseline is HEAD 38d28d10035462e4c67f4b08d66638d3a4858216 plus dirty files; historical product identities and A-000003 frozen packet remain intact. Scope: new checkpoint records, current-view projections and staging existing bytes. No maintained product content changes in this task. Before mutable views are preserved under artefacts/C-000003/before; initial Git status retained there. H/E/R-000005 checks content-faithful staging. V-000007 will record actual first commit and completion in a follow-up bookkeeping commit. Stop on hash mismatch/commit failure. Staging reversal preserves working files; committed corrections use successor records. No builds/background process. Open until verified checkpoint exists; follow-up projections are outside prior audit input.
