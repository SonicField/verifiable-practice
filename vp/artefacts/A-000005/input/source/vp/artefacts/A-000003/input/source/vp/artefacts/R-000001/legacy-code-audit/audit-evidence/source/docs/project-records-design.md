# Design Record: VP Project Planning and Records

**Status:** proposed design, 19 October 2026. These are design records for
this change, not a claim that VP or either inspected project already conforms.

## Goal and Document Plan

Make a future reader able to explain why maintained code exists, what
observations justified it, which choices were available, and when that
justification needs review, using Markdown and preserved directories.

The audience is a project owner, an AI resuming work without its conversation,
and an auditor starting with a code unit. The required outputs are a normative
standard, copyable templates, an operational playbook, independent examples,
and adversarial evaluation scenarios. The standard defines requirements;
templates expose their fields; examples demonstrate traces; scenarios try to
break the method.

The user's initial instruction authorises developing these materials, inspired
by PRINCE2, Capability Maturity Model and aircraft maintenance. Their follow-up
requires generalising each design choice before implementation, recording its
inspiration, and examining Honest as another source. This register makes that
derivation explicit. Early drafting began from parallel GC; these decisions
review and generalise that draft before final integration.

## Inspected Evidence

Inspection was read-only on 19 October 2026. These are document observations,
not reproduced experiments or full audits of those projects. Repository HEADs
at inspection were:

- `parallel_gc`: `91012c763e88b597e2bc58f2bce25c151767a212`;
- `honest`: `664c116c528eb0bc8dd2ac6c8eb11e7746892d20`.

The GC checkout also had untracked builds/results and a submodule with
untracked content. HEAD alone does not describe that entire filesystem.
Honest reported a clean working tree. The excerpts below preserve the
specific observations used in this design even if the source directories
later move. The full documents can be recovered at the stated repository
revision where tracked; directory listings are observations of local state.

| Evidence ID | Source and preserved observation |
|-------------|----------------------------------|
| O-01 | `parallel_gc` root listing: dozens of directories including `build-baseline-ft`, `build-benchmark-restored-gil`, `build-fidelity-ft`, `build-lazy-ft-tsan` and `build-upstream-ft-fresh`; names encode different kinds of information without a shared record identity |
| O-02 | `benchmarks/results/investigations/integration-validation-2026-10-16/build-evidence/README.md`: “The corrected root's source paths are symlink aliases to the original clean worktrees”; “Complete build logs remain under `/tmp/parallel-gc-benchmarks-complete-20261016-ntQPAW`”; four full source identities and executable hashes are recorded elsewhere in the campaign |
| O-03 | `benchmarks/results/investigations/creation-pool-retention-2026-10-16.md`: “the actual retained fraction in old benchmark campaigns cannot be inferred from one test schedule”; “This repair removes those unintended roots; it does not establish historical campaign garbage fractions retrospectively” |
| O-04 | `docs/CLAUDE_INTEGRATION_PLAN.md`: “Imported 42 historical evidence files”; an initial import changed twelve JSON file endings, byte comparison caught it, and original endings were restored; results are ignored by default and selected files explicitly retained |
| O-05 | `README.md`: “Superseded plans, ledgers and earlier documents were removed; they remain in git history”; current performance results are distinguished from earlier results and incomplete hosted validation |
| O-06 | `honest/AGENTS.md`: authority order is specification, checked grammar, conformance tests, guides/examples, historical addendum; “Do not silently choose code over the specification or the specification over code when they disagree” |
| O-07 | `honest/DOCUMENTATION_PLAN.md`: “An independent human or AI cold-reader exercise has not yet been recorded”; automated rewrite work is recorded complete while reader evidence remains outstanding |
| O-08 | `honest/docs/verification-claims.md`: “Automated parsing cannot establish that a declaration communicates well”; claims about isolated-document comprehension need prompts, artefacts, responses and evaluators |
| O-09 | `honest/.vp/audit-report.md`: audited revision `07322a5987242260f72fa953839a4652427b8cc7`; generated build files excluded, specification/Python sampled; baseline `make audit` and clean install failures are retained alongside passing focused checks |
| O-10 | `honest/docs/CONTRACT.md`: `honest-extract` writes at most one document; `DOCUMENTATION_PLAN.md` says multi-block validation belongs in a separate documentation checker, preserving CLI compatibility |
| O-11 | `honest/README.md`: a reader should recover meaning without the producing program, registry or authors; declarations are deliberately repeated, but cannot preserve failed media or make misleading data true |
| O-12 | Existing VP `SKILL.md`, `docs/investigations.md`, `playbooks/investigation.md`, `playbooks/recovery.md`: preserve provenance and negative results, but naming, durable custody, complete code coverage and expiry transitions are unspecified |

## Generalised Design Decisions

Each entry is a material design choice. Its observation is separated from the
general problem; the implementation applies that problem within a stated
scope. None of the observational project outcomes is evidence that the new
standard already improves practice.

### VP-DESIGN-01: An Explicit Conformance Contract

**Inspiration:** O-12 and the user's request for defined actions.
**Generalisation:** advice without mandatory boundaries cannot yield a
repeatable audit verdict. The requirement is an explicit contract for projects
that opt into record conformance, with scope, snapshot, time and legacy gaps.
**Choice:** a normative standard separate from explanatory guidance and
execution instructions. Ordinary VP use does not silently enrol a project.
**Alternative:** make every VP task conform immediately; rejected because it
would misrepresent historical coverage and impose a migration without consent.
**Implementation:** standard §§1, 11–12; routing and templates.
**Falsifier:** two auditors using the same scope cannot distinguish a missing
record from an allowed exclusion. Review after the first adoption audit.

### VP-DESIGN-02: One Record Root and Stable Typed IDs

**Inspiration:** O-01, O-12; O-09 shows a different existing record location.
**Generalisation:** directories named only for topics or dates lose identity
when moved, repeated or superseded. Every operation needs an unambiguous owner
and retrievable record, independently of the source layout or programming language.
**Choice:** a configurable single root, typed IDs, one canonical file per
record, a ledger and separately owned artefacts/workspaces.
**Alternative:** require renaming existing source/build layouts; rejected as
unnecessary disruption. `vp/` is a default, not a reserved universal path.
**Implementation:** §§2–3 and directory templates.
**Falsifier:** an imported record, retry or relocated artefact cannot retain
its identity without project-specific machinery. Test import and move scenarios.

### VP-DESIGN-03: Stages, Baselines and Delegated Authority

**Inspiration:** PRINCE2 as requested; O-07 and O-10 preserve compatibility
and distinguish completed deliverables from remaining evidence.
**Generalisation:** plans drift when actual work, acceptance and authority
are collapsed into a mutable checklist. Bounded stages need deliverables,
gates, tolerances and continuing justification.
**Choice:** root charter, stage records, preserved plan baselines and checkpoint
decisions; existing delegated authority suffices for routine work.
**Alternative:** approval for every tool call; rejected because it does not
express material choice boundaries and obstructs authorised work.
**Implementation:** §§4, 10; project/plan/stage templates.
**Falsifier:** a tolerance breach proceeds without a visible decision, or a
small authorised change requires repeated owner approvals.

### VP-DESIGN-04: Observation, Generalisation and Choice Are Separate

**Inspiration:** the user's follow-up; O-06 and O-10 identify design constraints
that familiar generic features could obscure.
**Generalisation:** a fix derived from one example can become an unjustified
universal rule. A choice must state the observed instance, the broader problem,
its applicability and limits, then why the selected response suits this scope.
**Choice:** require these fields in material decisions; generalisation may
identify a narrow class rather than universal validity.
**Alternative:** mandate reusable mechanisms for every edit; rejected because
a correctly bounded local remedy may serve the goal better.
**Implementation:** §5; decision template; this register.
**Falsifier:** a reviewer cannot tell a local observation from a general
requirement, or a decision generalises beyond the conditions evidenced.

### VP-DESIGN-05: Preserve Contemporary Reasoning

**Inspiration:** O-05; O-09's old audited revision differs from current HEAD.
**Generalisation:** a current summary cannot explain what was knowable when
a choice was made. Commissioning, testing and adoption are different events.
**Choice:** separate commissioning/adoption decisions, pre-action sections,
sealed records, append-only correction/supersession events and current views.
**Alternative:** continually rewrite a single plan or status file; rejected
because later success can erase failed routes and original criteria.
**Implementation:** §§3–6, 9; decision/event templates.
**Falsifier:** a post-result criterion change becomes indistinguishable from
the original protocol, or a correction requires overwriting the original.

### VP-DESIGN-06: Exact Inputs and All Attempts

**Inspiration:** O-02 and O-09.
**Generalisation:** evidence belongs to executed inputs, not nearby source,
an intended environment or a directory label. Retrying creates additional
evidence; it must not erase the first attempt.
**Choice:** distinct build and run records, content identities, predecessor
links, runtime checks, imported/dirty/unknown classifications and labelled batches.
**Alternative:** record only commits and passing outputs; rejected because
interpreted, compiled, manual and path-dependent work all have other inputs.
**Implementation:** §6; build/run/manifest templates.
**Falsifier:** an interpreted Python check, manual review or failed build needs
a fabricated executable, or a changed binary inherits an earlier run identity.

### VP-DESIGN-07: Claims, Instruments and Reader Outcomes

**Inspiration:** O-03, O-07 and O-08.
**Generalisation:** a check may measure the wrong property, and machine
acceptance is not evidence for a human interpretation. Empirical claims need
their own falsifiers and suitable instruments; value choices need owner review.
**Choice:** hypothesis/protocol/run separation, instrument controls, explicit
inconclusive verdicts, manual and reader experiments supported without builds.
**Alternative:** one “tests passed” field; rejected because it cannot show
which claim resisted which test or which outcome was never tested.
**Implementation:** §§5–7; hypothesis/experiment/run templates and examples.
**Falsifier:** parser success is accepted as proof of reader comprehension,
or an invalid measurement is classified as a valid falsification.

### VP-DESIGN-08: Finite Validity and Dependency Impact

**Inspiration:** aircraft reinspection as requested; O-03 and O-09.
**Generalisation:** support is bounded by time, assumptions, scope and inputs;
when any relied-on premise fails, downstream justification needs review.
**Choice:** explicit finite horizons, earlier event triggers, separate
historical verdict/current validity, incoming-link impact tracing, and new
evidence for revalidation. Initial periods are configurable policy proposals.
**Alternative:** fixed universal lifetime or automatic deletion of expired
code; rejected because neither follows from evidence or project goals.
**Implementation:** §7; state/event templates; expiry scenarios.
**Falsifier:** a date can be extended without review, a changed contract keeps
old acceptance automatically, or historical observations are rewritten on expiry.

### VP-DESIGN-09: Complete Coverage at a Snapshot

**Inspiration:** O-06's specification/code relationship; the user's requirement
to begin with a piece of code, not only a remembered investigation.
**Generalisation:** recording changes alone leaves untouched or inherited code
unexplained. Auditability needs the reverse lookup from every maintained unit.
**Choice:** snapshot inventories, stable units and content identity, introducing
and retaining decisions, explicit third-party boundaries and legacy gaps.
**Alternative:** one record per line or reliance on commit messages; rejected
as either excessive or insufficient for mixed and unchanged rationales.
**Implementation:** §8; coverage/change templates.
**Falsifier:** a renamed function, generated configuration, unchanged inherited
unit or contract document cannot be traced without conversation memory.

### VP-DESIGN-10: Custody and Recorded Disposition

**Inspiration:** O-02, O-04 and O-11.
**Generalisation:** a result's locator, meaning and byte identity are separate
from whether its producer still exists. Cleanup must preserve explanation
and disclose loss, including negative evidence.
**Choice:** manifests, durable directory bundles, retention while relied on,
disposition events, independent preserved copies and recovery checks.
**Alternative:** require Git or keep all temporary binaries forever; rejected
because directory-only use and proportionate storage must remain possible.
**Implementation:** §9; manifest/workspace/event templates.
**Falsifier:** moving a result breaks its trace, disposing a binary claims
unchanged reproducibility, or ignored files are assumed to be backed up.

### VP-DESIGN-11: Honest Legacy Adoption

**Inspiration:** O-05 and O-09.
**Generalisation:** recovery cannot create evidence about events no longer
observable. Current retention can be justified without inventing past intent.
**Choice:** read-only inventory, retrospective labels, preserved originals,
new retain/replace decisions and explicit nonconformance until gaps resolve.
**Alternative:** silently relabel old directories with new IDs as “verified”;
rejected because tidiness is not provenance.
**Implementation:** §12; playbook and migration scenarios.
**Falsifier:** an imported binary is assigned the current checkout's identity
without evidence, or a fresh test is reported as recovering a historical run.

### VP-DESIGN-12: Proportional Records without Lost Evidence

**Inspiration:** existing VP's small reversible steps; O-09's bounded audit.
**Generalisation:** ceremony can obscure evidence just as under-recording can
lose it. Granularity should follow material choices and independently
distinguishable inputs/outcomes.
**Choice:** related mechanical edits can share records, labelled batches keep
every member, empty artefact directories are unnecessary, semantic audit
sampling is disclosed while structural scope coverage remains complete.
**Alternative:** sampled coverage or a unique record per assertion; rejected
because either loses the code lookup or overwhelms it.
**Implementation:** §§5–6, 8, 11; compact example and audit template.
**Falsifier:** a mechanical edit needs dozens of duplicative records, or a
batch hides which individual execution failed.

### VP-DESIGN-13: Markdown and Directories as the Portable Interface

**Inspiration:** explicit user constraints and O-11's independent recovery.
**Generalisation:** an auditor must recover records without a proprietary
service or the producer's software. Optional automation must not define meaning.
**Choice:** plain Markdown fields, relative links, native raw files,
ordinary hashing, copyable templates and human-readable checklists.
**Alternative:** encode records in Honest, a database or a custom CLI; rejected
because none is needed to satisfy the requested storage contract.
**Implementation:** all new materials; no required executable component.
**Falsifier:** any mandatory transition or audit requires specialised software
or an external account to understand the retained record bundle.

### VP-DESIGN-14: Evaluate the Standard across Different Work

**Inspiration:** O-07's missing independent reader test and the user's request
to avoid designing around GC.
**Generalisation:** a successful walkthrough from one domain does not show
that a general record method works. It needs independent work types and
adversarial cases with explicit failure observations.
**Choice:** examples for compiled changes and documentation/reader experiments,
scenarios for interpreters, contract disagreement, expiry, invalid instruments,
legacy imports, retries, disposal and small edits.
**Alternative:** claim general validity from a GC migration; rejected because
that would test one specialised workflow and alter another active project.
**Implementation:** examples and behavioural evaluation scenarios.
**Falsifier:** either domain needs mandatory GC-specific fields, or a cold
reader cannot recover rationale despite structurally complete records.

## Review Horizon and Remaining Evidence

These choices are proposed under the user's authority to develop the standard.
They need review by **2026-11-18 23:59:59 UTC**, earlier if an adoption exposes
an unrepresentable workflow, unaffordable record burden, or an audit gap.
This date is a design review deadline, not evidence of empirical validation.

Static link/format checks and worked scenario reviews can reject structural
defects. They cannot establish that independent AI projects comply over time.
Independent cold-reader trials, actual adoption audits and measured record
cost remain necessary evidence. The [evaluation scenarios](project-records-scenarios.md)
specify those trials. The implementation report must distinguish checks
actually run from trials merely specified.

## Implementation Verification: 19 October 2026

The following checks were executed against the proposed implementation:

- A local Markdown check inspected 59 documents: all 149 relative file
  destinations resolved and code fences balanced. It found five broken
  navigation links in the uninstantiated root template on the first run;
  these became explicit destination filenames with a copy-time navigation
  instruction, and the repeated check passed.
- Routing checks found every new standard, template index, playbook and
  explanatory guide in `SKILL.md`.
- All nine operation templates contained the eight common required fields;
  standard and template files had final newlines.
- The existing skill frontmatter validator passed using `/usr/bin/python3`.
  Its first invocation with the shell's `python3` could not run because that
  interpreter lacks PyYAML. No dependency was installed; the system interpreter
  supplied the existing validator's dependency.
- `git diff --check` passed on tracked edits. A terminology search found no
  vendor or GC-specific operating requirements in the standard, templates or
  new execution playbook.

The compiled and document examples were reviewed for chronology and distinct
claim scopes. This caught an illustrative repaired-input run referring to the
baseline's hypothesis/protocol; separate candidate H/E records now preserve
that distinction. This was author review, not an independent trial.

These checks support structural consistency. Markdown rendering, external
source URLs, independent cold-reader exercises, sustained AI compliance,
full adoption audits and process-cost comparisons were not run. Both source
projects were inspected read-only. No conformance claim or migration was made
for them. The proposal remains subject to the review horizon above.

## Extension: Independent Record Audit and Worker Remediation

**Instruction:** the user requires an independent AI to audit records, report
gaps and request regeneration by the working AI, while remaining outside the
project's technical problem-solving role. This extends the original proposal.
The following derivations precede implementation of that extension.

**Source inspection:** read-only, 19 October 2026; `nbs-framework` HEAD
`1946cfba7770248915608bc5d16bcc5eda2b4415`, working tree reported clean.
Sources are design descriptions and a published retrospective; their reported
session outcomes were not independently reproduced in this inspection.

| Evidence ID | Source and preserved observation |
|-------------|----------------------------------|
| O-13 | `claude_tools/nbs-medic.md`: “You do not reason about the project's code, architecture, or design”; distinguishes “Agent claimed it ran tests but didn't” from “The tests are testing the wrong thing”; reports action claims against separately captured session logs |
| O-14 | `claude_tools/nbs-pythia.md`: “Read the decision log. Assess trajectory. Post your checkpoint. Exit”; forbids modifying code, assigning tasks, making team decisions or arguing; each checkpoint is a fresh assessment |
| O-15 | `docs/team/nbs-pythia.md`: a separate instance avoids the coder's context bias; structured decisions reduce persuasion from chat; names hidden assumptions, missing validation and downstream risks without veto |
| O-16 | `blog/The-Medic-Report.md`: reports false positives caused by incomplete log searches and a chained command missed by a search pattern; reports later transparent self-corrections; also reports the team treating Medic's silence as evidence of validity |

### VP-DESIGN-15: Separate Record Auditor and Working AI

**Inspiration:** O-13–15 and the user's explicit role requirement.
**Generalisation:** an observer absorbed into implementation acquires the
worker's immediate goals and can stop evaluating whether records support
claims. The general requirement is separation of assessment from technical
execution, independent of the number of workers or domain.
**Choice:** an auditor in a separate fresh context reads the designated bundle
and writes audit outputs only. It checks provenance, record consistency,
claim/evidence relationships and goal/decision coverage. The worker owns
reconstruction, experiments and code changes; the owner grants authority and
handles unresolved exceptions. The auditor does not design fixes or run the
project to fill gaps. A same-session self-check is labelled preparation.
**Alternative:** inject an auditor prompt into the worker's ongoing context;
rejected because changing the role name does not remove implementation bias.
**Implementation:** standard §11.1; audit playbook and role templates.
**Falsifier:** an auditor reproduces a missing test or patches project code
instead of returning an evidence requirement; independent closure rests on
the worker's own assessment. Review by 2026-11-18, earlier on role drift.

### VP-DESIGN-16: Frozen Inputs and Explicit Evidence Custody

**Inspiration:** O-13's separate action logs, O-15's structured input and
O-16's incomplete searches.
**Generalisation:** assessment must name exactly what was available, what was
searched and who controlled it. A mutable project and an author's narrative
cannot establish an independently captured historical action by themselves.
**Choice:** preserve an identified audit bundle/request, record search
coverage and custody for evidence, keep worker chat outside audit context,
and label missing capture as a limitation. Independent role and independent
capture are separate properties. Hashes do not authenticate authored logs.
**Alternative:** require NBS terminal machinery or call all Markdown logs
trusted; rejected because neither follows from the portable directory contract.
**Implementation:** §11.2; audit request/report templates and packet workflow.
**Falsifier:** missing evidence in a partial search is reported as fabrication,
or an authored result is presented as independently captured merely because
its hash matches. Same review horizon as VP-DESIGN-15.

### VP-DESIGN-17: Findings, Responses and Independent Closure

**Inspiration:** the user's regeneration loop; O-14's bounded observer and
O-16's corrections.
**Generalisation:** a gap report is useful only if its exact evidence
requirement survives handoff and the producer cannot certify its own repair.
Corrections must apply equally to erroneous audit findings and worker records.
**Choice:** local finding IDs under A, objective closure conditions, worker
response events linking preserved replacements/new runs, and a successor A
to close or retain each finding. Regeneration is a new attributed record,
never an invented past action or silent rewrite. Technical questions return
to a commissioned worker investigation, not to the auditor.
**Alternative:** an informal chat request followed by the worker marking it
fixed; rejected because it loses scope, evidence and independent acceptance.
**Implementation:** §11.3; response template, state table and walkthrough.
**Falsifier:** worker acknowledgement closes a finding, regenerated logs
replace missing originals, or a false finding disappears without correction.
Same review horizon as VP-DESIGN-15.

### VP-DESIGN-18: Scheduled, Bounded Audit Rounds and Declared Gates

**Inspiration:** O-14's assess-and-exit lifecycle, O-15's no-veto role and
O-16's misleading silence signal.
**Generalisation:** independent assessment must return a verdict even when
inputs are incomplete, and must not become endless negotiation. Project
authority sets gates; an auditor's silence grants no assurance or new authority.
**Choice:** charter-defined checkpoint triggers and round/time budgets;
explicit reports even with no findings; owner escalation on unresolved budget
exhaustion; predeclared conformance gates, with advisory risks distinguished
from unmet mandatory requirements. Re-audit has a fresh context and cites prior
findings as evidence, not as unquestionable authority.
**Alternative:** continuous debate or silent monitoring as release approval;
rejected because scope drifts and lack of warnings can mean lack of inspection.
**Implementation:** §11.4; project/stage templates and behavioural scenarios.
**Falsifier:** audit scope expands until it becomes product work, silence is
accepted as a pass, or a worker repeatedly regenerates without independent
closure or owner disposition. Same review horizon as VP-DESIGN-15.

### Extension Verification

Static checks on 19 October 2026 passed for 63 Markdown documents and 177
relative file destinations, balanced code fences, independent-audit routing,
common fields in ten operation/response templates, whitespace and skill
frontmatter. A terminology search found no NBS runtime or vendor requirements
in the normative standard, audit playbook or role templates.

Nine additional adversarial cases specify role drift, custody overstatement,
self-certified closure, fabricated regeneration, assessor correction, mutable
packets, false independence, embedded role instructions and exhausted budgets.
These are evaluation specifications, not executed independent AI trials.
Actual role adherence, observer bias, remediation quality and loop cost remain
unverified. No NBS runtime was invoked and no source project was modified.

## Extension: Owner as a Human or AI Role

### VP-DESIGN-19: Ownership Is Defined by Mandate, Not Actor Type

**Instruction:** the user identifies a future AI owner, similar to the NBS
supervisor. This changes the assumed role holder, not the evidence obligations.
**Inspiration:** read-only inspection on 19 October 2026 of
`docs/team/nbs-supervisor.md` and `claude_tools/nbs-supervisor.md` at NBS HEAD
`1946cfba7770248915608bc5d16bcc5eda2b4415`. The supervisor maintains the
terminal goal, delegates work, monitors outcomes and escalates when goal
clarity is lost. That implementation retains human authorisation for session
end; it demonstrates delegated AI supervision, not unrestricted AI authority.
**Generalisation:** responsibility for goals, scope and acceptance can be
assigned to different kinds of actor. Auditability depends on an explicit
mandate and recorded decisions, not on assuming every owner is human.
**Choice:** permit human or AI owners, identify mandate source, decision
limits, duration, escalation, reassignment and withdrawal. The owner records
management choices; the working AI keeps operational VP records; the auditor
is independent of the authors whose records it assesses, including an AI
owner. Delegating tracking does not transfer authority to invent approvals.
**Alternative:** a mandatory human owner or an AI owner with implied unlimited
authority; rejected because neither represents a bounded delegated role.
**Implementation:** standard §4 and §11.1, charter/role templates and guide.
**Falsifier:** changing an actor's label grants authority, a supervisor adopts
its own audit findings as independent, or management approvals lose their
attribution when the worker transcribes them. Review by 2026-11-18, earlier
on ambiguous delegation, owner replacement or an audit independence breach.

**Implementation check:** 63 Markdown documents and 177 relative file
destinations passed link/fence validation; skill frontmatter and tracked diff
whitespace checks passed. T-28 specifies AI-owner replacement and authority
testing; no independent behavioural trial was run for this extension.
