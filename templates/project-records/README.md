# Project Record Templates

These documents instantiate the planning, control, traceability and assurance layer of [VP's full project quality management system](../../docs/how-vp-works.md). They record actual project authority, work and evidence; template examples themselves are not operational history.

Use with the [standard](../../standards/project-records.md) and
[playbook](../../playbooks/project-records.md). Copy project-view templates
into the chosen root, normally `vp/`. Copy operation templates to
`records/<type-directory>/<ID>/record.md`. Replace every angle-bracket
placeholder; leave no blank required fields. Use `not applicable — reason`
when a field genuinely does not apply. Placeholders are not valid records.

Classify before acting under standard §1.1. A/B use full forms and independent gates; C may combine reason/results; D uses only change.md’s minimal form; E its prepared final commit message and no VP file. Do not instantiate every template.

Reserve an ID in the ledger when the level requires a record. Fill pre-action sections first.
Append dated amendments to open records; never overwrite pre-action criteria.
Seal terminal outcomes and preserve their original revision. Subsequent corrections
use dated successor entries or commits at C/D; use a separate event when the
applicable A/B or external requirements demand it. Never rewrite sealed fields
as if later evidence had been present originally.
Validity is derived from evidence, A/B/C deadlines, all-level dependencies/triggers and later events;
a completed record alone does not make a claim current.

| File | Destination/purpose |
|------|---------------------|
| [root.md](root.md) | Record root README |
| [project.md](project.md) | PROJECT.md charter and policies |
| [plan.md](plan.md) | PLAN.md current stage sequence |
| [state.md](state.md) | STATE.md current handoff/validity |
| [ledger.md](ledger.md) | LEDGER.md complete record navigation |
| [coverage.md](coverage.md) | COVERAGE.md revision inventory |
| [decision.md](decision.md) | D: decisions |
| [stage.md](stage.md) | S: stages |
| [hypothesis.md](hypothesis.md) | H: hypotheses |
| [experiment.md](experiment.md) | E: protocols |
| [build.md](build.md) | B: build attempts/imports |
| [run.md](run.md) | R: evidence executions |
| [change.md](change.md) | C: changes |
| [event.md](event.md) | V: lifecycle events |
| [audit.md](audit.md) | A: Project Audit reports, kind project |
| [audit-request.md](audit-request.md) | records/audits/<A-ID>/request.md: identified revision/scope, audit reference and independent role |
| [audit-response.md](audit-response.md) | A/B response event; C/D may use a change entry, always pending independent closure |
| [manifest.md](manifest.md) | artefacts/<owner-ID>/MANIFEST.md |
| [workspace.md](workspace.md) | workspace/README.md ownership |

The six project views and records are Markdown; raw files may keep their
native format. A build-free check does not need a fabricated build record.
Material choices need records, not one record per edited line. A labelled
batch must retain each execution's inputs, status and evidence.

Use the [independent audit playbook](../../playbooks/record-audit.md) for the
request/report/response/follow-up cycle. An auditor gets a fresh context and
writes only audit outputs; the working AI repairs records and performs
authorised technical work. Responses never close their own findings.

