# <ID>: <Title>

**ID:** <type-sequence>
**Type:** <type>
**Assurance:** <A/B separate build record; C may use inline identified build notes; D/E do not instantiate this for prose checks>
**Created:** <YYYY-MM-DD HH:MM:SS UTC>
**Author/operator:** <identity>
**Status:** <open or terminal outcome>
**Origin:** <links to prior commissioning decision/stage/change>
**Goal served:** <root decision link and outcome>
**Sealed:** <UTC timestamp when terminal; open until then>

## Inputs before Invocation

**Classification:** <fresh/incremental/imported; reused inputs>
**Predecessor build:** <B link or why none>
**Source:** <exact revisions for every repo/submodule; clean status or retained
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
**Output identities:** <paths and relevant executable SHA-256/build IDs; identifiers
do not require retaining those binaries>
**Reproduction record:** <source/patches, dependency/toolchain specifications,
commands/configuration and unique required inputs; environment/build reconstruction
tested, untested or unavailable, with evidence and limits>
**Working resources/disposition:** <temporary binaries/caches/containers, owner and
use/disposal condition; no binary capture or recovery required by default>
**Required retained output bytes:** <only where a specific evidence/deliverable/
external obligation applies: reason, consumers, period and custody; otherwise none>
**Runtime verification:** <feature/mode/configuration observations>
**Limitations/unknowns:** <imported provenance gaps; partial outputs>
**Next action:** <run, retry as new B, investigate or abandon>

