# Worked Record Traces

These are illustrative histories, not measurements of `parallel_gc`, `honest`
or this repository. IDs and outcomes below are fictional. Tables show the
essential fields and links; they are not complete conformant project bundles.
Use the [templates](../templates/project-records/README.md) for real records.

## 1. Compiled CLI Output Handling

**Inspiration:** Honest's historical CLI audit recorded output failures that
returned success. **Generalisation:** successful process status should mean
the promised operation completed, including observable output. This applies
to writers beyond parsers; it does not define the semantics of every CLI.

Suppose a file-export tool has a documented guarantee that success means all
requested bytes were written. A fictional sequence on 20 October is:

| Record | Time UTC | Contents and links |
|--------|----------|--------------------|
| D-000001 | 09:00 | Root: reliable file exports; owner delegates local fixes; compatibility boundary retained; review 2027-01-18 |
| S-000001 | 09:05 | Output-contract stage; at most one day; deliverable is correct success/failure status; unchanged successful bytes required |
| D-000002 | 09:10 | Commission output investigation; observed successful status on a failed sink; general completion problem; compare final-flush checking, per-write checking, and defer; permit a bounded diagnostic |
| H-000001 | 09:15 | Claim: every reported success wrote and flushed requested bytes; falsifier: forced output failure returns 0; source and output-contract scope; review 2026-11-19, earlier source/toolchain/contract change |
| E-000001 | 09:20 | Fixed protocol: normal output control and deterministic failed sink; nonzero/diagnostic required on failure; unchanged normal bytes; unsupported fault mechanism makes that test inconclusive |
| B-000001 | 09:25 | Clean baseline snapshot, compiler/options/dependencies; full log and binary digest; actual executable recorded |
| R-000001 | 09:30 | Baseline control passes; forced failure returns 0; raw stdout/stderr/status per member retained; valid observation falsifies H |
| D-000003 | 09:35 | Choose final stream-error and flush checks because the contract includes buffered output; record limits of fault injection and alternatives; authorise one coherent change |
| C-000001 | 09:40 | Baseline snapshot and patch plan; affected writer, error path, tests and contract; rollback restores baseline |
| H-000002 | 09:42 | Repaired-input claim: completion status meets the contract; new scope points to C-000001's candidate inputs; same falsifier and finite horizon |
| E-000002 | 09:44 | Candidate protocol for H-000002, preserving E-000001's controls and thresholds; candidate identity fixed before execution |
| B-000002 | 09:50 | New source identity and executable digest; same configuration; not a relabelled baseline build |
| R-000002 | 10:00 | E-000002: normal bytes unchanged, forced failure nonzero with diagnostic; checks fail to falsify H-000002; runtime identities match B-000002 |
| D-000004 | 10:10 | Adopt C using R-000002; retained risk: only specified failure paths tested; review by 2026-11-19, earlier dependency/source/contract change |
| A-000001 | 10:20 | Exact new snapshot inventory and trace inspected; residual risks and audit scope recorded |

Each build/run has retained native evidence under its owning ID with a
Markdown manifest. The contract document and verification test are maintained
units with their own rows; they are part of the justification, not untracked
supporting prose.

### Start from a Piece of Code

The inventory row for `src/export.c:write_export` identifies its exact content,
C-000001, D-000004, H-000002 and R-000002. Following R-000002 reaches E-000002,
B-000002 and the tested inputs. D-000004 reaches the earlier fix choice and
commissioning chain, S-000001 and D-000001. R-000001 explains the failing
baseline and why this check was needed. The rejected options are in D-000003.

If a later contract removes or changes the completion guarantee, create
V-000001, trace both writer and test rows, and commission a new hypothesis and
protocol. Do not renew the old date by editing D-000004. An unchanged
historical binary's result remains historical evidence.

### Interpreted Variant

For a Python exporter, R identifies the interpreter, installed package and
source/harness snapshots. If no package or executable is built, no B is needed;
R explicitly says why. If a wheel or native dependency is built, its B records
the actual inputs. The root/decision/protocol/change/coverage structure stays
the same. “Tests passed at commit X” without interpreter and imported module
identity cannot establish what implementation ran.

## 2. Document Self-Containment and Reader Comprehension

**Inspiration:** Honest separates parser acceptance from unrecorded cold-reader
claims. **Generalisation:** syntactic validity cannot establish that an unknown
reader can recover units, alternatives and intended meaning. This applies to
specifications, operational instructions and durable records.

Suppose a telemetry schema's goal is to remain understandable after its
producer disappears. A fictional project has:

| Record | Contents and links |
|--------|--------------------|
| D-000001 | Root: future readers can interpret telemetry; owner reviews value by 2027-01-18 |
| S-000001 | Documentation stage: complete schema and isolated reader task; machine-validity and comprehension are separate gates |
| D-000002 | Choice: add explicit units and permitted alternatives; local observation is an ambiguous temperature field; general problem is missing interpretive context; compare embedded definitions, external manual, and defer |
| H-000001 | Parser-validity claim; rejects malformed records and accepts complete examples; identities bind schema, examples and parser |
| H-000002 | Reader claim: an unfamiliar reader can identify temperature unit, absence semantics and permitted alternatives from the document alone; any wrong answer or request for unavailable producer information falsifies the tested reader outcome |
| E-000001 | Machine protocol for H-000001; planted undeclared field and valid control; actual parser/source identities required |
| E-000002 | Reader protocol for H-000002; fixed isolated document and questions, excluded surrounding project context, answer rubric and independent evaluator; prompt/model/configuration or human participant conditions recorded |
| R-000001 | Parser execution fails to falsify H-000001 within tested cases; native outputs retained; it says nothing about H-000002 |
| R-000002 | Reader responds “unit unknown”; preserved prompt, document digest, response and rubric assessment; valid falsification of the tested comprehension outcome |
| D-000003 | Reject completeness for adoption, revise embedded field definition; no claim that parser success met the reader gate |
| C-000001 | Before/after document snapshots; define unit in the document; preserve original ambiguity and rollback |
| E-000003 | New fixed reader protocol using revised document; preserve original rubric and identify any change before execution |
| R-000003 | New isolated reader answers correctly; limited sample fails to falsify the revised outcome, not universal human comprehension |
| E-000004 / R-000004 | Revised-document syntax protocol and execution bind machine-validity evidence to the candidate schema/examples; old R-000001 remains baseline evidence |
| D-000004 | Bounded adoption using both syntax and revised reader evidence; short horizon and new-population/contract triggers; explicitly record uncertainty from limited reader trials |

Reader runs have no build and state why. Any parser build has ordinary B
records, and parser results need runtime identities. The schema text,
questions, rubric and output are retained files with manifests; no special
language or schema registry is required by VP.

### Start from a Document or Test

Coverage maps `docs/telemetry.md:temperature definition` to C-000001 and
D-000004. Following evidence recovers the original ambiguity, failed reader
response, revised document, question rubric and limited adoption claim.
Coverage also maps the syntax checker to its own decision and evidence.

If the reader instrument accidentally included a manual defining the unit,
create an invalidation V, mark dependent reader conclusions unknown/invalid,
then rerun isolated trials. The schema's machine-validity evidence may remain
usable if impact review establishes that its independent inputs are unchanged.

## 3. What Generalises and What Stays Local

| Shared record requirement | Compiled example | Document example |
|---------------------------|------------------|------------------|
| Observation before generalisation | Failed sink reports success | Reader cannot identify unit |
| Claim and appropriate falsifier | Exit status and actual bytes | Answer rubric and absent producer context |
| Exact tested identity | Binary, toolchain, source, harness | Document, prompt, questions, participant conditions |
| Negative result retained | Baseline failure | Incorrect reader response |
| Reverse lookup from maintained unit | Writer and regression test | Definition and syntax/reader instruments |
| Triggered review | Changed source/toolchain/contract | Changed text, audience or evaluation context |

The standard carries these relationships. Domain acceptance thresholds,
technical controls and user values belong in the project's own records.
