# A-000007 preparation attempt 01 — failed

**Recorded:** 2026-10-20T20:41:12.928275+00:00
**Owner / authority:** Worker /root, D-000024; audit-input custody preparation, not a project experiment or product verification run.
**Status:** failed; reconstruction from tool response, not a recovered execution log.

The original preparation script selected candidate `c17d269bfafcda229ce9fe8734d4709499584fa7` and called `/usr/bin/git bundle create /home/alexturner/vp-preserved/verifiable-practice/PTE-removal-20261020/A-000007.bundle c17d269bfafcda229ce9fe8734d4709499584fa7`. The tool response reported `subprocess.CalledProcessError`, exit 128. The script accumulated subprocess metadata in memory and raised before writing it; original stderr, per-command digests and exact execution timestamps were consequently not preserved. No substitute output is presented as historical evidence.

Read-only inspection after the failure found the designated input and preservation directories empty: no completed bundle, index, manifest or frozen packet existed, and no assessor had been dispatched. The issued request and candidate commit were unchanged. Original instrument bytes are retained here, SHA256 `778cbe20210a5d9766d544d675b2eab5774798996a47a39eac21feb27884c0e7`.

## Generalisation and next attempt, specified before execution

Git bundles need an advertised reference for a recoverable tip. Packing a raw commit expression does not by itself supply that reference. Use `HEAD` only after verifying that it equals the fixed candidate; verify the bundle tip and candidate again afterward. Candidate identity, rather than the mutable name, defines the audit source. Preserve failure metadata incrementally in the next attempt. The new attempt fills the previously empty designated packet, includes this failure disclosure in outer preparation, and does not replace any sealed request or previously completed capture. This is a preparation correction within D24, not a new source choice or a claim about PTE.

Retention: life of project plus 365 days after retirement; no disposal authorised. Same-host, worker-controlled custody and attributed failure transcript; no independently authenticated execution claim. Consumer: A7 assessor and later stage gate.
