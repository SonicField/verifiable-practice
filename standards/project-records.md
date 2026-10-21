# VP Project Planning and Records Standard

**Version:** 1.1, 21 October 2026.

This is the normative contract for an explicitly adopted VP project. “Must”
is required, “should” permits a recorded reason for another approach, and
“may” is optional. These meanings do not depend on capitalisation.

VP connects maintained work to its authorised goal through choices and
checkable evidence. Assurance depends on the consequence of being wrong.
Declaring project conformance does not give every change the same burden.

Documentation is Markdown in directories. Custody must provide
content-addressed identity, immutable revision history and at least one
verified independent replica. Git and a separate repository or self-contained
bundle provide an ordinary implementation. An alternative must demonstrate
these properties and actual restoration; hashes and folder copies alone
are insufficient. No database, service or VP-specific software is required.

**Project Audit** (`project`) assesses records and their support. **Code Audit**
(`code`) assesses engineering quality. For “Please audit X” or another
ambiguous request, ask the kind and wait. Never infer a default or silently
perform both. Use [Audit Routing](../playbooks/audit-routing.md).

## 1. Scope and Limits

Conformance names a project, standard version, exact revision, scope and
assessment time. It covers the requirements applicable to each declared
assurance level, including recorded exclusions and mandatory external gates.
It does not certify correctness, safety, regulatory compliance or efficiency.

Declare when adoption begins. Earlier work remains legacy until supported;
a new test cannot establish an unrecorded past action. Preserve failed,
rejected, aborted and inconclusive evidence. A digest identifies bytes, not
who performed an action or whether the claim is true.

### 1.1 Consequence Determines Assurance

Classify before work starts. Assess the credible effect in the intended use,
including affected people, money, data, authority and dependent work. File
size, number of edits, an AI author and project adoption do not determine
severity. Verified reversal reduces recovery cost; “it is in Git” alone does
not demonstrate that recovery works.

| Level | Consequence if wrong | Minimum record and check | Required independence |
|---|---|---|---|
| A | Harm to people, regulatory breach, or irreversible loss | Authorised decision; explicit scoped hypothesis and protocol before execution; every relevant build/run and failure; owner acceptance | Fresh independent review of protocol before execution and results before acceptance |
| B | Serious loss or costly recovery | Pre-action decision with intended outcome/falsifier; identified run evidence and failures; separate owner/delegated acceptance | Fresh Project Auditor before acceptance |
| C | Significant rework or a user-visible defect beyond minor inconvenience | One decision/change record with pre-action rationale/falsifier and identified results; related build/run notes may be inline | Project-declared sampling or named stage gates; not an audit for every edit |
| D | Minor consequence, limited scope and easily reversed | One change record: level/reason/root mandate before work; actual check/outcome and revision afterward | None unless an external requirement applies |
| E | No effect on behaviour or meaning, including a proven typo/format correction | Commit message: level/reason, root/task reference, and check or reason no check applies | None unless an external requirement applies |

These are minimum sufficient forms, not targets to exceed. D must not acquire
separate D/H/E/R/A records solely because the project declares conformance.
E must not acquire a change record solely for VP. A reader's ability to find
the reason and check matters more than the number of files.

Record the classification and consequential assumptions before implementation:
in the A/B decision, C/D record, or E's prepared commit message. Keep that E
message in the final revision. Preparation timing is an attributed record,
not an independently authenticated log. If evidence shows a higher consequence,
stop dependent work, raise the level and meet its gates before proceeding.

Use the higher level when owner and worker disagree, or a credible consequence
cannot yet be excluded. Resolve uncertainty through explicit scope/evidence;
do not silently choose the lowest level. Split unrelated changes when they
have different consequences; do not use a high-level project to inflate a
minor edit or bundle a hazardous change into a low-level task.

Use the following C/D boundary in documentation and tooling projects. A C
change alters an operative requirement, external interface, delegated authority,
acceptance gate, or a control whose failure creates significant recovery work.
A D change adjusts explanatory guidance or removes an optional process technique
when binding requirements, authority, gates and available checks stay unchanged,
there is no identified consequential deployed consumer, and source reversal is
verified. This includes retiring an unused prescribed wording style while
retaining its substantive clarity checks. A missing necessary control or an
identified binding dependency raises the level; uncertainty about such a
current dependency must be resolved before applying D.

Assess the direct credible failure in the declared scope. Do not promote every
sentence to C/A on the speculative argument that a future reader might build
an unspecified defective system from it. Classification of that future system
belongs to its own use/exposure assessment. Conversely, calling an operative
contract “documentation” cannot lower its level. Reversal of text does not undo
known downstream loss; name those consumers and consequences explicitly.

The charter must name C sampling rules or stage gates before work. A default
is a fresh Project Audit at each stage that changes an authority, interface
or acceptance contract, plus a declared sample of other C changes. Record
selection, coverage and limits; missing selected checks block that gate.
Domain regulation, contractual controls and owner-required gates override
this table upward. VP levels are not aviation Design Assurance Levels or a
claim of compliance with DO-178C or FDA guidance.

## 2. Project Directory Contract

Choose one record root, normally `vp/`, linked from README and project
instructions. Source keeps its ordinary layout. Keep current evidence once:

```text
project/
|-- README.md
|-- <current source and ordinary project files>
`-- vp/
    |-- README.md
    |-- PROJECT.md
    |-- PLAN.md
    |-- STATE.md
    |-- LEDGER.md
    |-- COVERAGE.md
    |-- records/<type>/<ID>/record.md
    |-- records/audits/<A-ID>/{request.md,record.md}
    |-- artefacts/<owner-ID>/MANIFEST.md
    |-- artefacts/<owner-ID>/<unique current raw evidence>
    `-- workspace/README.md
```

| Current view | Purpose |
|---|---|
| README | Entry points, standard, record vocabulary and how to read an immutable trace |
| PROJECT | Goal, owner/mandate, scope, consequence rules, gates, custody and validity policy |
| PLAN | Current stages, deliverables, checks, budgets, stop conditions and next decision |
| STATE | Current stage, all open findings/gates, work in progress and next action |
| LEDGER | Current record IDs/states/origins and immutable locators for retired records |
| COVERAGE | Maintained units, introducing/retaining records, evidence, level and validity |

Use short plain prose in current views. Stage narratives and earlier views
belong in revision history, not repeated in the charter. A cold reader given
only STATE must be able to state the current stage, open findings and next
action; a promised link count is not evidence of that understanding.

Before replacing a view, preserve its revision in history and the replica.
Retired records may be replaced in the working tree by a concise summary and
immutable locators. Do not copy a retired record or product source into an
archive directory. Type directories may remain absent until needed.

Each ID owns one record directory; tightly related fields may share a record
according to §1.1. Disposable workspaces must have owners and no sole relied-on
bytes. Restored source/checkouts belong outside the project search tree.

## 3. Identity and Record Fields

Use namespace-qualified monotonically allocated IDs; never reuse withdrawn
or retired numbers. The ledger may resolve retired IDs by revision/path
rather than keep their files live. Simultaneous writers reserve distinct IDs.

A–D records identify author/operator, creation time in UTC, level and reason,
authority/root, baseline inputs, intended outcome/check, actual results,
failures/limits, next action and terminal timestamp. Apply only the detail
needed for their consequence; use an explicit reason for an inapplicable
field. E uses the commit-message form in §1.1.

Link immutable inputs as `repository + commit + path`, or blob hash with a
retrieval locator. A mutable branch or a digest without accessible custody
is not evidence. Include dirty/generated/external inputs when relied on.
Commit metadata is attribution, not authenticated action timing.

Open records may append dated amendments. Never rewrite a sealed original
as if it had contained later evidence. Corrections use successor entries or
commits. A current locator manifest may replace a historical one under §9,
but must identify itself as a successor and resolve the original exact bytes.

## 4. Planning and Authority

Owner is a role, human or AI. Identify its originating mandate, scope,
reserved/delegated decisions, duration or review, escalation, withdrawal and
handoff. Naming an actor “owner” does not enlarge its authority. The owner
controls goal, scope and acceptance; the worker maintains routine records.
An AI owner should delegate implementation. Transcribed authority retains
source, attribution and missing-original limits.

Goals and values need authority and continuing-value review. Technical
hypotheses need falsifiable evidence. A passing test grants no permission;
an inspection request does not authorise repair.

Plan bounded stages with baseline, deliverables, consequence levels,
acceptance/harm criteria, applicable independent gates, budgets/tolerances,
stop/reversal rules and owner. Preserve the plan revision. At exit record
actual outcomes and an authorised acceptance/revision/stop; C/D may do this
inline. A/B require separate acceptance after evidence. Exceeded tolerances
or changed goals require an exception before dependent work proceeds.
Existing delegation remains usable; VP does not require repeated permission.

## 5. Choices and Relied-On Ideas

Before a material choice, record the source observation, general problem,
applicability, goal relationship, alternatives, reason, authority and scoped
falsifier. Do not infer universal usefulness from one project. D may combine
this with its change record; E's reason is its commit message.

State a refuting observation before relying on an important empirical claim.
A uses explicit H/E records; B/C may put hypothesis/protocol sections in the
decision and link results. A D check does not need a separate hypothesis file.
Distinguish observed result, interpretation, assumption and unknown.

A failed-to-falsify result is not proof. Test verdict and present validity
are different. Prospective choices must remain distinct from later results;
A/B acceptance is a new record, and C/D append outcomes without replacing
pre-action reasoning. Origin chains reach the authorised root without cycles.

## 6. Experiments, Builds and Runs

Fix relevant inputs, procedure, controls, thresholds, sample/analysis method,
stop rules and inconclusive conditions before evidence execution. Changes
after observing results are new labelled protocols/attempts. Exploratory work
is labelled exploratory, not claimed to satisfy invented prior criteria.

Identify actual source, executable/tool, dependencies, configuration, data,
working directory, command, time/status, runtime mode and outputs to the
detail required to distinguish the claim from a setup error. A/B use build/run
records; C may retain inline labelled execution entries; D records its actual
check in the change record. No compile record applies to a manual document
check. Do not hash every unrelated installed tool for a prose correction.

Record every relevant failure, retry, abort and skipped check. A bounded batch
may group uniquely labelled members with individual inputs/status/output.
A retry is a new attempt, never an overwritten result. Preserve seed/order,
warmup, allocation and interference when they affect the claim. Imported
binaries have known digest and explicit unknown provenance, not a fictitious
reproduced build. Actual clean/dirty/generated inputs distinguish source.

Keep unique raw evidence in revision control, or once in a declared external
content-addressed store when size/sensitivity requires it. The independent
replica is for recovery, not another browsable source archive in the project.
Authored summaries link original evidence and exclusions. Do not report
regenerated logs as historical captures.

## 7. Validity and Reverification

Every relied-on item has an owner, tested scope and relevant change triggers.
A/B/C also have a finite UTC review date justified by exposure, consequence,
change rate and evidence strength. D/E have trigger-only review: no calendar
expiry is required. This is an explicit exception to blanket date policies.

| Level | Starting maximum, subject to a justified project policy | Earlier triggers |
|---|---|---|
| A | 90 days | Relevant inputs, safety/authority/rule change, contrary evidence or custody loss |
| B | 180 days | Relevant inputs, cost/recovery assumptions, authority or custody change |
| C | 365 days | Meaning, interface, dependency, acceptance or evidence change |
| D/E | No calendar deadline | Relevant meaning/input/authority change or discovered defect |

These are conservative policy starting points, not measured universal
lifetimes. Fast-changing performance or provisional claims may need much
shorter windows even within a level. An external mandate may impose stricter
reviews. Stable documentation must not inherit a weekly runtime deadline
from unrelated past experiments.

Effective reliance cannot exceed relevant dependencies. A D wording change
cannot extend an A/B claim underneath it. Historical verdicts stay attached
to their exact inputs and time; expired evidence is not made fresh by writing
another date. Reclassification records why earlier defaults no longer apply,
and distinguishes current policy from new empirical evidence.

At resume, stage entry, integration and handoff check actual triggers/dates.
On contradiction, expiry or lost custody, trace incoming dependencies, mark
unknown impact, contain affected reliance, and commission evidence at the
applicable level. A/B use an event; C/D may record it in their change entry.
Owner-reviewed goals are not falsified by a technical test. Reassignment
cannot erase gaps, change authority or renew evidence.

## 8. Coverage and Traceability

Account for all maintained in-scope units at an accepted revision, including
configurations, tests and documents. Whole-file rows suffice when the reason
covers the whole file; use sections/symbols for genuinely mixed decisions.
Do not create a row for every heading without a different rationale.

Each row identifies revision/path or content hash, introducing/retaining
record (or E commit), root, relevant check/evidence, level, validity and gaps.
Resolve historical units through immutable revision history, never a copied
source tree. Reference external/vendored bytes by immutable version/hash and
boundary rationale; do not claim their internal history was reconstructed.

A reader must be able to follow a maintained unit through its choice/check
to the authorised root, including earlier rejected approaches where relevant.
C/D inline evidence and E commit reasons are valid endpoints. No extra D/H/E/R
chain is required solely to make a simple edit resemble an A-level project.

## 9. Custody, Retention and Pruning

Custody must provide content-addressed identity, immutable history and an
independent verified replica with a documented restoration route. Replicate
all relied-on revisions/blobs/external evidence before removing current
files. A separate directory/repository or bundle may address working-tree
loss; state that a same-host copy cannot survive whole-host loss. Use an
off-host or separate failure-domain replica when that loss is a credible
consequence or another requirement demands it. Never claim Git creates a
replica merely because a repository exists.

Keep live product/evidence once. **Do not copy product source, old records or
audit inputs into the worktree. Do not assemble history by recursively copying repository directories.**
An audit reference must not contain an earlier audit reference; cite its immutable locator only.
Native evidence stores may contain deliberate equal bytes for legitimate
input/output reasons; enumerate exceptions and ownership. Guidance/code
copies are not such an exception. External large evidence is stored once
per declared content-addressed store and replicated for recovery.

A current manifest lists owner/meaning, unique evidence paths/hashes or
historical commit/path/blob locators, producer/capture limits, consumer,
retention and recovery replica. A record without raw evidence needs no empty
manifest. Old manifests survive in history; replacement manifests explicitly
name their successor role and the exact original revision/path.

Removing current files is permitted once history and replica preserve all
required bytes and consumers can resolve them. Record removal/reason/authority
in its commit and the level-appropriate record. No separate V is required
for routine D cleanup. Retired records may become a short summary with exact
history locators; this is not permission to erase history or invent it.

Retain history, rationale and positive/negative evidence for project life plus
the declared post-retirement period. A restore must actually recover selected
or complete bytes according to consequence and scope, not merely inspect
hashes. Pruning claimed to preserve every removed byte requires a complete
restore/byte comparison. Evidence loss remains visible and downgrades claims.
Secrets may be redacted with explicit limitations and protected custody.

### 9.1 Recoverable Revisions

A **recoverable revision** identifies retained project bytes through an
immutable revision ID, revision history, a verified independent replica and
a documented, tested recovery route. Name the repository, revision, relevant
paths or external content IDs, replica locator, recovery evidence and limits.
Recovery evidence identifies the revision and scope actually restored; do not
claim that a selected restore tested every other retained byte.

| Property | What establishes it | What it does not establish |
|---|---|---|
| Label | Optional tag or descriptive name | Immutable identity: a tag can be moved |
| Content identity | Immutable revision ID and path, or content hash with retrieval locator | Availability, authority or occurrence of an action |
| Custody | Immutable history and verified independent replica | Whole-host protection unless the replica has the relevant failure independence |
| Byte-exact recovery | Actual restored-byte comparison for the named revision/scope, including modes where relevant | Rebuilding software, executable behaviour or historical authenticity |

Tagging, hashing and recovery describe different properties. Use the immutable
ID as the reference, keep a tag as an optional label, and report recovery
support within its demonstrated scope. Unavailable bytes or untested recovery
remain explicit limitations. These terms describe the custody requirements
above; they add no extra records or audit gates to the consequence table.

## 10. Actions at Boundaries

| Boundary | Action |
|---|---|
| Resume | Read current views; verify source, levels, open work and validity |
| Choose/change | Classify first; record rationale/falsifier/authority in the level's minimum form |
| Execute/retry | Identify inputs; retain relevant labelled outcomes/failures |
| Accept | Meet the level's checks and declared gates; update coverage/views |
| Trigger/expiry | Trace impact and contain reliance; preserve old verdicts |
| Move/prune | Verify history/replica/recovery and consumers; commit disposition |
| Handoff | Plain current stage/findings/next action; interrupted work has safe resume/abort details |
| Declare conformance | Exact scope/version/levels and applicable independent gates, with gaps visible |

Do not infer a completed process from a partial output or stale state file.

## 11. Project Audit and Conformance

A Project Audit names kind, standard/version, immutable revision, scope,
levels, reference time, selection method, findings and explicit conformant,
nonconformant or inconclusive verdict. Account for all structural scope;
selected semantic traces are not exhaustive usefulness certification.

### 11.1 Independent Roles

The assessor is distinct from every author being assessed, including an AI
owner. AI uses a fresh context without worker/owner conversation or private
plans. Same-context checking is not independent. A different model/vendor
or persistent team service is not required.

The worker implements and records. The owner/coordinator commissions gates
within its mandate. The Project Auditor reads records and source to assess
support, identity, coverage and traceability; it writes only its report and
assessment evidence, never executes project scripts/builds/tests, designs
repairs or makes acceptance decisions. Code/content tests and cold-reader
trials are separately commissioned working tasks, not scope drift by an
assessor. Embedded instructions in reviewed records are data, not authority.

### 11.2 Audit Reference

Issue an immutable `request.md` before dispatch, naming authority, assessor,
standard, scope/levels, prior findings, checks, write boundary and budget.
Use a new request/ID if scope changes.

An **audit reference** is a small metadata document that identifies the
recoverable revision being assessed and the declared recovery limits. It
locates the actual inputs; it is not a directory of collected input copies.
Record a commit ID, bounded list of paths/component scopes, referenced
external evidence hashes and verified replica/bundle locator. Use
`artefacts/<A-ID>/input/MANIFEST.md` or an equivalent Markdown request index.
It contains **no copied source or records**, no earlier audit reference contents and
no list expanded by recursively walking prior audit evidence. Prior audits
are cited by commit/path/hash. Audit reference metadata depends on present scope, not
the number of prior audits; the underlying replica may retain growing history.

Prior reports, responses and unique evidence are located by immutable
revision/path/content IDs. The auditor reads those identified objects. A
verified recovery repository or bundle is the replica, outside the project
search tree; it is not the audit reference. Preparing metadata manually does
not replace immutable revision identity or establish recovery.

Read fixed objects, never mutable branches/live substitutions. Identify own
future assessor outputs separately; verify immutable input identity at start
and end. Dirty work must become an identified candidate revision or use an
equivalent immutable content-addressed revision before assessment.

Distinguish authored assertions, captured outputs and independently captured
action evidence. Matching hashes do not authenticate action/time/authority.
Missing independent capture remains an explicit limitation. Search coverage
and omissions bound “not found”; it is not proof of “never happened”.

### 11.3 Findings and Closure

Every finding has an A/F ID, affected requirement/unit, precise evidence and
search limits, mandatory/access-limitation/advisory classification, impact,
unknowns, response request and observable closure condition. Even no findings
requires an explicit sealed report; silence is not a pass.

Worker responses preserve original findings and provide identified evidence,
correction/unknowns/authority and proposed status. At C/D this may be an inline
change entry; A/B use a response/event when needed. Only a fresh independent
successor assessment closes a finding. Owner risk acceptance is a disposition,
not closure or a waiver of mandatory conformance requirements. Views expose
all unresolved mandatory findings and affected gates, plus advisory statuses.

### 11.4 Gates and Budgets

Apply §1.1: A has protocol and result gates, B acceptance, C declared sample/
stage gates, D/E no automatic audit. Project conformance requires an independent
assessment of its adopted control system and level assignments; this does
not require an audit for every subsequent D/E change. A changed declared
scope/level gate needs a new appropriately scoped assessment.

Charters name assignment, cadence/trigger, round/time budget, response owner
and escalation. Re-audit relevant invalidation at the applicable level. Each
invocation reads, reports and ends; it cannot enter endless repair debate.
Budget exhaustion exposes gaps and routes an owner decision, never lowers
the declared gate. The auditor grants no product/publication authority.

## 12. Adoption and Migration

Discover actual sources/results/history first; identify unknowns. Preserve
original revisions, then explicitly adopt the version, consequence rules,
custody/replica, current views and gates. Reclassify inherited policies with
sources/reasons, not retroactive passes or date-only renewal. Test actual
recovery before pruning; keep immutable locators and a short summary of
legacy results/gaps. Other projects do not inherit this repository's layout,
levels or software merely because they supplied inspiration.

## 13. Design Sources

PRINCE2 supplies controlled stages/value/exception ideas; Capability Maturity
Model supplies repeatability and improvement; light-aircraft maintenance
supplies identity/history/reverification. The 21 October review adds the
consequence-based assurance structure associated with DO-178C and risk-based
software assurance associated with FDA guidance. These are inspirations,
not certification or transferred aviation objective counts. See
[design rationale](../docs/project-records-design.md),
[execution playbook](../playbooks/project-records.md) and
[templates](../templates/project-records/README.md).
