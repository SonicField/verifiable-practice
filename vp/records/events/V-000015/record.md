# V-000015: Correct current navigation labels following A7 advisory

**ID:** verifiable-practice:V-000015
**Type:** audit-response — advisory disposition
**Created:** 2026-10-20 20:48:32 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; current-view correction and bounded disposition, ready for future independent assessment
**Origin:** [D-000025](../../decisions/D-000025/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-20 20:48:32 UTC

[A-000007/F-001](../../audits/A-000007/record.md) is an open advisory, not a mandatory gap. The frozen README calls A3/D9 an accepted current baseline; the frozen ledger calls D12/S2 the current content task. Sources are `c17d269bfafcda229ce9fe8734d4709499584fa7:vp/README.md`, SHA256 `0900463bb82fc204e477d67f3b97bdd77baa4ca05d612677a8d346f09ace4887`, and `c17d269bfafcda229ce9fe8734d4709499584fa7:vp/LEDGER.md`, SHA256 `5cd45ec107c272652a86fd253b46506465704f1f921f658a8c6b1e0b940775fd`. Original candidate bytes and sealed report stay unchanged in Git.

General problem: a record index can have valid links while its navigation text misidentifies the current task. Under D25's bounded disposition and existing current-view maintenance authority, replace the current labels with S3/D22/D25 and A7's exact-snapshot verdict, explicitly label A3/D9 historical, and preserve original history through Git. This is later authorised bookkeeping outside A7's frozen scope, not a source change or an enlarged verdict. Record the response as ready for future independent assessment, never as worker-closed. Review by 2026-10-26 23:59:59 UTC/earlier stage, label, packet, authority or custody change. No reader-efficacy or historic-authenticity claim; retain project life plus 365 days. V14 completed Git index will identify the later view bytes. No technical experiment is required to correct these sourced labels.

## Actual correction

README now names S3/D25 and A7 as the latest accepted stage and labels A3/A6 historical; ledger allocator/status/footer now name D22/S3/D25 and the advisory disposition. STATE/PLAN/PROJECT/COVERAGE carry the same current gate and finding distinction. No sealed audit input/report was changed; advisory independent closure remains pending. Current view bytes are identified by V14’s later completed Git index, not a self-digest.
