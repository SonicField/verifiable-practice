# E-000005: Compare staged Git blobs with current source and evidence

**ID:** verifiable-practice:E-000005
**Type:** experiment
**Created:** 2026-10-19 19:19:37 UTC
**Author/operator:** Codex worker /root
**Status:** sealed; first attempt complete-root selection insufficient
**Origin:** [D-000010](../../decisions/D-000010/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 19:20:46 UTC

Before first checkpoint: stage all current unignored changes using git add -A. R-000005 enumerates git ls-files --stage -z and reads every actual indexed blob with git cat-file --batch; compares SHA-256 to the physical regular file bytes. Include complete vp, supporting binary dependencies and existing framework changes. Read paths/arguments as data; no shell interpolation of filenames. Capture Python/Git executable digests, actual argv, cwd, times, statuses, index object identities and per-file digests. Plant one appended byte in the first retrieved blob and feed it to the identical comparison function; expected exact path is reported differing, without modifying project or index. Missing/altered input or unexpected command status stops acceptance; retain partial outcomes. Retain all status/output/log evidence under R-000005. Bookkeeping completion files are restaged and byte-compared again before receipt commit. No rerun of technical examples, no build, no new efficacy/conformance claim; first and receipt commits are authorised D-000010 outcomes.

R-000005 retained matching selected bytes, but missed ignored nested VP evidence. Successor E-000006 explicitly verifies complete retained-root selection; original protocol/output preserved.
