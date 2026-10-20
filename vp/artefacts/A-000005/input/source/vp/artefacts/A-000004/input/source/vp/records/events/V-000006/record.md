# V-000006: Preserve completed audit outputs and stage handoff

**ID:** verifiable-practice:V-000006
**Type:** event
**Created:** 2026-10-19 12:35:26 UTC
**Author/operator:** Codex delegated worker/coordinator /root
**Status:** selected; sealed
**Origin:** [D-000009](../../decisions/D-000009/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 12:35:26 UTC

**Kind:** custody/checkpoint. D-000009 accepts A-000003 exact freeze; this event declares preservation of the completed report, independent assessment and authorised completion projections. All original A input/assessment snapshots retain their own manifests and dates. No prior verdict changes.

Preserved destination: `/home/alexturner/vp-preserved/verifiable-practice/completed-adoption-20261019`. Bundle source/ contains the current product and entire current vp/ root. Outer inventory.json and MANIFEST.md, produced after copying, are the completion metadata: per-file exact hashes/count, producer/capture times/executable identity, comparison outcome, scope and retention. Do not rely on the copy until those metadata files record zero differences. They are outside their own source snapshot, avoiding self-hash claims; the event's sealed bytes are included in source. Copy instrument/capture is worker-controlled, not independently authenticated action performance. A-000003's pre-existing independent input verification supports its own earlier snapshot only.

Owner/producer/custodian /root; authority D-000001/D-000009; consumers current retention D-000007/009 and future audits/recovery. Retain bundle/records/raw failures/inputs for project life + 365 days after retirement; no scheduled disposal. Same-host separate directory protection only; no disk/host-loss claim. R-000004 recovery remains the actual restoration trial, and this later bundle supplies complete sealed outputs/current handoff. A failed copy blocks reliance and needs a new event; original bytes remain local. Current views are post-audit authorised projections, not an extension of A-000003 semantic assessment. Review due 2026-10-26 23:59:59 UTC or earlier custody/source/mandate changes.
