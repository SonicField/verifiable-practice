# V-000014: Semantic removal checkpoint and Git custody receipt

**ID:** verifiable-practice:V-000014
**Type:** event — version-control checkpoint
**Created:** 2026-10-20 20:48:07 UTC
**Author/operator:** Codex worker /root
**Status:** open; checkpoint allocated before execution
**Origin:** [D-000025](../../decisions/D-000025/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** open

## Known inputs and planned accounting

D25 accepts S3 on R12 content evidence and A7's actual conformant fixed candidate `c17d269bfafcda229ce9fe8734d4709499584fa7` / freeze `2026-10-20T20:41:17.391502+00:00`. A7 bundle is 4208116 bytes, SHA256 `0d9e574409fe3932b2884c44fe1d55c2dcb8d8433f7f0ff926a49a06aea85db2`, at `/home/alexturner/vp-preserved/verifiable-practice/PTE-removal-20261020/A-000007.bundle`. Its full path/blob index covers 23,325 candidate files and 69 product files; the 484-unit product inventory is R12. The first preparation failed and has an attributed reconstruction with unavailable original stderr/timing, rather than invented logs; the second succeeded with actual incremental command captures. A7 owns those outer preparation files and its assessment; its candidate commit excluded its own future outputs as declared.

Before execution, reserve this receipt under D25. Exact staged-root comparison and negative controls precede the local checkpoint. Actual outcome/commit/tree will be appended from captured execution, not assumed. Then seal this receipt and commit it with current views. Containing receipt identity and verified completion bundle/index are produced afterward at the external preservation location, avoiding a self-commit identity claim. A mismatch blocks completed custody reliance and requires a new event/attempt. No source revalidation is invented from file packing. Effective evidence deadline 26 October UTC/earlier trigger; retain life plus 365 days. Same-host byte custody only; no remote publication or disposal.
