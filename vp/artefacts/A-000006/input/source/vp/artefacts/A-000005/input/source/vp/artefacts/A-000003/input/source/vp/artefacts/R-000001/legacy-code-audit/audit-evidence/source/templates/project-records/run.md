# <ID>: <Title>

**ID:** <type-sequence>
**Type:** <type>
**Created:** <YYYY-MM-DD HH:MM:SS UTC>
**Author/operator:** <identity>
**Status:** <open or terminal outcome>
**Origin:** <links to prior commissioning decision/stage/change>
**Goal served:** <root decision link and outcome>
**Sealed:** <UTC timestamp when terminal; open until then>

## Inputs before Execution

**Protocol/hypothesis:** <E/H links>
**Build/executable:** <B links and digest checked at execution; no build with reason
for manual/source-only checks>
**Other inputs:** <exact checked source, harness, dependencies, datasets,
reader artefacts, model/configuration where relevant>
**Procedure and directory:** <commands or manual steps; logical/physical paths>
**Environment/runtime mode:** <actual features; host/OS; resource allocation>
**Sampling:** <count, seed/order/warm-up/interference; batch member labels>

## Outcome

**Start/end:** <UTC times>
**Execution status:** <completed/failed/aborted; exit code or manual completion>
**Member outcomes:** <each labelled batch member's inputs/status/raw output>
**Raw evidence:** <manifest and file links>
**Observations:** <measurements and errors without interpretation>
**Analysis:** <calculation, every input run/member and exclusions>
**Verdict:** <falsified/failed to falsify/inconclusive; infrastructure failures
or invalid measurements distinguished>
**Interpretation/unknowns:** <bounded implications and missing coverage>
**Accepted outcome owner/review by/triggers:** <finite deadline and dependencies
if relied on; otherwise explicitly not accepted for reliance>
**Next action:** <D to accept/reject/investigate; retries get new IDs>

