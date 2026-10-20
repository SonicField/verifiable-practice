# <ID>: <Title>

**ID:** <type-sequence>
**Type:** <type>
**Created:** <YYYY-MM-DD HH:MM:SS UTC>
**Author/operator:** <identity>
**Status:** <open or terminal outcome>
**Origin:** <links to prior commissioning decision/stage/change>
**Goal served:** <root decision link and outcome>
**Sealed:** <UTC timestamp when terminal; open until then>

## Inputs before Invocation

**Classification:** <fresh/incremental/imported; reused inputs>
**Predecessor build:** <B link or why none>
**Source:** <exact snapshots for every repo/submodule; clean status or retained
base+patch+untracked/generated inputs; no guessed identity>
**Dependencies:** <versions, content identities, native modules and configuration>
**Toolchain/environment:** <compiler/version, OS/architecture, relevant variables>
**Working/physical paths:** <logical and resolved paths; owned workspace>
**Procedure:** <configure/compile/train/link commands, flags, options>
**Profile/training inputs:** <identities and seeds or not applicable>

## Actual Outcome

**Start/end:** <UTC times per phase>
**Phase exit statuses:** <configure/compile/train/link; failed/aborted retained>
**Logs/warnings/errors:** <manifest and paths>
**Outputs:** <paths, SHA-256 or equivalent content digests>
**Runtime verification:** <feature/mode/configuration observations>
**Limitations/unknowns:** <imported provenance gaps; partial outputs>
**Next action:** <run, retry as new B, investigate or abandon>

