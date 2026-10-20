# V-000003: Preserve an independent directory copy and its recovery limits

**ID:** verifiable-practice:V-000003
**Type:** event — custody/preservation
**Created:** 2026-10-19 12:15:39 UTC
**Author/operator:** Codex working AI /root
**Status:** recorded; sealed
**Origin:** [D-000004](../../decisions/D-000004/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 12:15:39 UTC

R-000003 copied the actual stage input tree to
/home/alexturner/vp-preserved/verifiable-practice/adoption-20261019-R-000003,
restored from that directory and verified 562 enumerated files with zero
differences. Its copy-inventory.json, results.json and manifest record exact
bytes, times, owned temporary restoration and negative controls. This is an
independently located directory on the same host; hardware/off-host durability
and independently authenticated historical actions are not established.

That recovery snapshot predates R-000003's sealed result and subsequent
handoff views. Preserve those new bytes as a separate A-000002 packet copy
at its capture checkpoint; do not overwrite the tested old snapshot.
The new packet manifest/capture results identify the final copy and all
current input bytes. No old reports/files have been deleted or relabelled.
Consumers are current D-000004 retention, H-000003 and independent A requests.
Retention is project life + 365 days after recorded retirement; disposal
requires consumer review and a new event. Current source is unchanged from
R-000002. Later closure never changes the old audit verdict.
