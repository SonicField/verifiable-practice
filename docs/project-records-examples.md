# Worked Record Traces

These are fictional histories, not measurements of parallel_gc, Honest or
this repository. They illustrate the [standard](../standards/project-records.md)
and [templates](../templates/project-records/README.md). Classify consequence
before choosing the form; a complete-looking long table is not the goal.

## 1. Export Contract: B, Serious Data Loss

**Inspiration:** Honest's historical CLI audit reported output failures that
returned success. **Generalisation:** process success should mean the promised
operation completed, including observable output. It does not define every
CLI's success semantics.

Suppose a valuable-data exporter promises that exit0 means all requested bytes
were written. An undetected false success can lose authoritative data and
requires costly recovery, so this example is B. The root owner mandate
permits local repair, preserving the external contract.

| Record | Pre-action and outcome |
|---|---|
| D1 | Root goal, scope, owner/delegation and review date |
| D2 | B classification/reason; failed-sink observation; options/falsifier; source identity; fixed normal-output and forced-failure checks; stop/reversal; authority |
| R1 | Identified baseline tool/source/configuration, unique normal/failed-sink members: normal succeeds; failed sink incorrectly returns0. Original failure/status/output retained |
| R2 | Authorised repair and identified candidate; same checks: normal bytes unchanged, failed sink nonzero/diagnostic. Baseline failure remains distinct. Build identities recorded if an executable is built |
| A1 | Fresh Project Auditor before acceptance: fixed commit/scope/replica; evidence support, identity and traceability; no tests/repairs by assessor |
| D3 | Separate owner/delegated acceptance after R2 and conformant A1; bounded input/failure-path support, finite B review and change triggers |

Hypothesis/protocol sections may be in D2 at B; separate H/E documents are not
required. Any genuinely new material repair choice is dated before execution,
not rewritten into the initial plan after results. A safety-critical deployment
would raise A and require explicit H/E plus independent protocol review.

Coverage links `src/export.c:write_export` to D2/R1/R2/D3 and rootD1. Relevant
build/run evidence identifies actual source, executable, toolchain and inputs;
source/patches, reproduction specifications and raw failures stay recoverable.
The executable digest is an identifier, not a default retention obligation.
Temporary binaries/tools are disposable under §6.1; a recipe, retained binary
or byte recovery does not establish environment reconstruction or experiment
repetition. Unique required inputs and records
are cited by immutable revision/path/hash and verified replica, never copied
source folders. Python may need interpreter/imported-module identities without
a fictitious compile record. Changed contract/tool/workload triggers revalidation;
an old result is not made current by changing its date.

## 2. Telemetry Definition: C, Significant Rework

**Inspiration:** Honest distinguished parser acceptance from an unrecorded
cold-reader claim. **Generalisation:** machine validity cannot establish that
a reader knows units, absence semantics or permitted alternatives.

Suppose a non-safety telemetry interface omits a temperature unit, causing
significant integration rework. Classify C. The owner permits correcting this
contract. One combined C1 record is sufficient for rationale and execution
entries; the charter declares a fresh Project Audit at this interface stage.

| Entry in C1 | Evidence/decision |
|---|---|
| Before work | Root/authority, level/reason, baseline commit/path, ambiguous field, options, scoped parser/reader predictions and falsifiers, fixed questions/inputs/rubric, rollback and declared C gate |
| Parser member | Actual parser/source/configuration; valid control and undeclared-field negative control. Result supports syntax only |
| Reader member1 | Fresh context, document-only prompt; answer “unit unknown” retained as failed comprehension, without hiding it behind parser success |
| Dated repair/protocol amendment | Add authorised unit definition, identify revised input before new trial; original rubric and failed response remain |
| Reader member2 | New context and identified revised document; answer correct for this bounded task; no claim of universal comprehension |
| Candidate parser member | Check candidate schema/examples; baseline syntax evidence is not silently applied to changed inputs |
| Acceptance entry | After conformant gate A1, owner/delegated inline C acceptance, exact scope/limits, C date and relevant text/audience/interface triggers |

Each member has its actual identity/status/raw output. No separate H/E/R/D is
needed merely for these C fields. The selected A report remains distinct and
fresh; another C stage can use its predeclared sampling rule instead. Coverage
maps the definition and checker to C1 and the root. If the reader was secretly
given a manual, preserve that invalid trial and rerun in isolation; do not
relabel the old answer as valid evidence.

## 3. Optional Wording Technique: D

Retire an explanatory wording technique while binding requirements, authority,
acceptance gates and available clarity checks stay unchanged. No consequential
deployed consumer is identified, and source reversal is verified. This is D;
removing an operative requirement or necessary control would raise C or higher.

One C1 change record states level/reason/root mandate, baseline revision,
responsibilities/dependency review and intended check before work. Its outcome
entry gives actual edits, check/result/failures, final revision and verified
rollback locator. No new D/H/E/R/A. Review on relevant meaning, consumer or
custody change; no calendar expiry. The historical retirement planning replay
in this repository tests this minimum form, not general reader efficacy.

## 4. Meaning-Preserving Typo: E

Prepare the commit message before editing: “Level E: spelling correction with
no change of behaviour or meaning; root/task reference; diff review check.”
Keep that message and actual outcome in the final commit. No VP change file,
new hypothesis, audit or expiry date. If the apparent typo changes a normative
value or instruction, reassess its consequence before dependent work.

All forms preserve observation versus interpretation, authority versus test
results, failed attempts and immutable retrieval. They differ in record burden,
independent gates and review policy because consequences differ.
