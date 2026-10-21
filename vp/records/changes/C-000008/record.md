# C-000008: Separate experiment records, provenance and working resources

**ID:** verifiable-practice:C-000008
**Created:** 2026-10-21 17:25:51 UTC
**Author/operator:** working AI/coordinator Codex /root
**Status:** open; pre-action choice and checks
**Level/reason:** C. Changing an operative retention/custody contract can cause
loss of evidence or significant unnecessary preservation work. This is not a
terminology-only D change; A–E consequence thresholds remain unchanged.
**Authority/root:** current human owner's reported VP binary-retention failure
and instruction to correct the distinction, serving the portable traceable-method
goal; original D1 at `9605ad0:vp/records/decisions/D-000001/record.md`.
**Baseline:** b9984e5833258ff138a290680140f0467f0f5758, standard1.1; verified
complete bundle/native proof in its exact completion reference.
**Validity:** C review21October2027 UTC, capped by root17January2027 and earlier
relevant requirements, dependencies, consumers, authority/evidence/custody changes.

## Observation, general problem and applicability

Owner supplied another working AI's reflection: VP conflated preserving build
products with preserving source/dependency/toolchain specifications, commands,
configuration/workloads, raw measurements and analysis needed to reproduce work.
It reported unnecessary binary preservation and emphasised that byte recovery
does not establish experimental reproducibility. This is attributed supplied
testimony; original project/session, failed action logs and cause are unavailable.
It is not an authenticated execution or measured prevalence claim.

Local sources support a general ambiguity: standard1.1 §2 protects all sole
relied-on workspace bytes, §3 treats any digest without custody as non-evidence,
and §9 requires replica of all relied-on revisions/blobs before removal.
Build/run forms and native-format guidance do not distinguish an executable
identity from a retained measurement or specification. Such undifferentiated
rules can apply to any compiled program, interpreter, container or model tool.

## General choice and alternatives before implementation

Standard1.2 will distinguish three roles, independent of extension/format:
(1) durable experiment records: source revisions/patches and relevant dependency/
toolchain specifications, protocol/build/run/configuration/workload inputs,
raw observations/results/failures and analysis with environmental limitations;
(2) provenance identifiers: what actually ran, e.g. executable digest/build ID,
which identifies bytes but neither retrieves them nor obliges their retention;
(3) owned disposable working resources: binaries, caches, temporary containers
and diagnostic builds unless their actual bytes have an explicit evidence or
deliverable retention need. One object can have different roles for different
claims; raw binary measurements remain durable evidence.

Retain a reproduction recipe and distinguish supported reconstruction from
untested/unavailable environment/build reproduction and experimental outcome.
Do not silently require vendoring every tool/dependency or preserving a host.
An unavailable non-reconstructable environment stays an explicit limitation;
a retained executable cannot cure it. Exact-byte replay, delivered release bytes,
forensic evidence or external mandates can require scoped retention with named
reason, owner/consumers, duration and custody. A/B risk alone is not a blanket
binary-capture requirement. Disposable resource cleanup needs owner/consumer
checks, not a preserve-and-restore detour for those resource bytes. Existing
mandatory evidence/authority and audit gates remain; no existing evidence deleted.

Rejected: retaining every runtime machine/binary; deleting all binary-format
data by extension; asserting recipes guarantee reproduction; replacing missing
unique inputs/results with hashes; ignoring specific exact-byte obligations.

## Predeclared falsifiers, plan and gates

Source review fails if an active route still mandates every executable's custody,
permits losing unique measurements/specifications, confuses identity with recovery,
or claims recipes/byte restoration prove experimental reproducibility. Keep all
positive/negative/aborted attempts and no fabricated historical captures.

Check product local Markdown links/anchors/fences, SKILL frontmatter/routing and
coverage hashes; inspect cross-route semantics. Scenarios cover disposable compiled
output, binary-format measurements, raw-log loss, unavailable toolchain, exact-byte
release requirement, temporary diagnostic build, imported unknown-provenance
executable and repository-byte restoration. A separate fresh working reader answers
these cases without the intended verdict/this record; worker evaluates each against
the predeclared outcomes in the canonical scenario table. All eight required outcomes
must hold; no blanket reproducibility/retention inference. This is a bounded
instruction probe, not a real build or universal AI-reliability trial.

Adopt1.2 prospectively for this repository through this owner-authorised C change;
older verdicts remain1.1 and exact scope. Charter's changed-control C stage gate
requires a fresh independent Project Audit A12 before C acceptance. Up to60minutes
worker work, two20-minute independent rounds; report gaps/escalate at budget,
no endless debate. Auditor reads fixed source/records/evidence and only writes
own report/assessment; no experiments, technical repair or acceptance decisions.
Final plain STATE requires a fresh bounded cold reader and containing-commit
history/replica verification before handoff. No project-specific software added.

Current coverage must track the new changed units and accurate current acceptance
boundaries. Its stale A11/F001 aggregate statements will receive a dated sourced
response in this record as part of updating that view; they stay open until a
fresh successor assessment explicitly satisfies A11's observable closure condition.

## Actual results and acceptance

Pre-action rationale committed05688a7 before product mutation. Standard1.2 and21
product files now distinguish the roles across main routing, build/run/manifest/
workspace/project forms, recovery/audit procedures and explanations/scenarios.
No existing evidence or runtime binary was removed or added. Assurance §1.1 is
byte-identical to baselineb9984e5; this changes retention semantics, not thresholds.

Five exact-context patch attempts failed before mutation: first standard patch
included a duplicate/unmatched pruning hunk; two combined form/audit patches
had absent final audit contexts; one route patch assumed a standalone README
sentence; one larger patch included an invalid heading placeholder. All rejected
atomically; corrected focused patches/uniquely checked replacements succeeded.
These are worker edit failures, not project evidence gaps.

Source check01: `/usr/bin/python3 /tmp/vp-c8-check.py`, exit0. Retained source
SHA256a3269e4c9894c3e7c610d522ba7ce86aac3eb85e8251b750ea76a9a83e945e58
at external `review-20261021/completion/sha256/<that-SHA>/check.py` and matching
independent completion-replica address. PyYAML5.4.1; no Python runtime binary
retention inferred. Actual output:69products/21changed,256local destinations/
12fragments valid; frontmatter/routes/fences valid, missing-link/unclosed-fence
negative controls detected; oneSKILL/noPTE/noequal-byteproductcopy; no active
freeze/snapshot/packet terms; assurance table unchanged, version1.2.
`git diff --check` passed. External URL availability/rendering, actual builds/
reconstruction/repetition and broad AI behaviour not tested by this source check.

### Dated response to A11/F001 during C8 coverage maintenance

Original1.1 COVERAGE remains atb9984e5/history. Current aggregate text now names
D27 acceptance at20bb26b,25later C7 paths atc100fbd and A11's exact1.1 scope;
C8 changes are separate pending1.2 units with updated hashes/reason/gate.
Acceptance is no longer labelled pending B and no all69-unchanged-from20bb26b
claim remains. This is a newly attributed current-view correction, not rewriting
sealed A11. Proposed ready for independent review; F001 remains open until A12
checks its observable acceptance/revision consistency condition.

Instruction probe and fresh C-stage audit pending; no acceptance yet.

### Instruction probe01 and source check02, 17:32 UTC

Fresh `/root/c8_evidence_role_probe`, no inherited turns, read only the committed
0fffb29 request and five designated standard/forms. No scenario oracles, C8,
worker chat or private plans were supplied. Actual source/configuration limits
and all eight answers remain in its unique response. Worker evaluation:

| Case/oracle | Actual answer observation | Outcome |
|---|---|---|
| 1 / T35 | Digest-only compiled output is not missing required evidence; recipe not tested reconstruction/repetition | Pass |
| 2 / T36 | Sole binary-format measurements require retained bytes/custody, not hash-only disposal | Pass |
| 3 / T37 | Lost raw log is an explicit gap; executable cannot replace observations; new run newly dated | Pass |
| 4 / T38 | Unreconstructable toolchain stays unavailable; retaining executable does not establish reproduction/obligation | Pass |
| 5 / T39 | Contractual exact shipped bytes require concrete role/period/custody | Pass |
| 6 / T40 | Diagnostic executable may be disposed after authority/use/consumer/required-evidence checks, no executable restore | Pass |
| 7 / T41 | Keep imported identity/raw outputs and unknown provenance; missing executable alone not custody failure | Pass |
| 8 / T42 | Scoped byte recovery alone, no build/environment/repetition/authentication claim | Pass |

All eight predeclared outcomes hold, zero blanket binary-retention/reproduction
inferences. One bounded same-family fresh answer is not an executed benchmark,
full adoption workflow, repeated population trial or universal benefit/adherence
claim. No failed probe/retry. After that input revision, wording “Keep actual binary
bytes only” was clarified to “Require durable retention ... only” to avoid prohibiting
normal temporary working use; roles/outcomes unchanged, but the probe is not claimed
to have read those later bytes. Final candidate gets independent source assessment.

Source check02 re-ran the same identified optional instrument after final wording/
coverage identity adjustment: exit0, same69/21products,256destinations/12fragments,
frontmatter/routes/fences/negative controls/unique-product and unchanged assurance
outcomes. `git diff --check` passed. STATE has not yet received its final handoff
reader; source checks do not substitute for it. Gate A12 pending.
