# Project Planning, Records and Custody

VP keeps a reason and a check attached to maintained work, so a later reader
can reach the authorised goal without the original conversation. The
[standard](../standards/project-records.md) defines the contract; the
[playbook](../playbooks/project-records.md) gives its action order.

## Assurance Follows Consequence

A typo and a safety controller should not generate the same records.
Classify before work: A covers harm/regulatory breach/irreversible loss,
B serious loss or costly recovery, C significant rework or more than minor
user defect, D minor/easily reversed change, E no behaviour/meaning effect.
Use the higher credible level on disagreement or uncertainty.

A/B have independent gates and owner acceptance. C uses a declared sample
or stage gate. D needs one change record with its reason and actual check;
E needs its commit message. A project that adopts VP does not automatically
require A/B paperwork on every edit. See standard §1.1 for the operative
contract versus explanatory-guidance boundary and required forms.

An optional wording technique can be retired at D when binding requirements,
authority, gates and available checks remain intact, no consequential deployed
consumer is identified, and reversal is verified. Removing a necessary control
or altering an operative contract raises the consequence. Document count does
not decide the level.

## History Is a Relationship Between Revisions

Current source is kept once. Earlier code, documents, failed attempts, records
and original manifests are cited by repository/commit/path or retrievable blob
hash. Revision control must provide content identity and immutable history;
a verified independent replica provides recovery. Git is one ordinary
implementation, not a VP-specific service. Alternatives must demonstrate
those properties. Same-host replicas cannot protect against whole-host loss.

A **recoverable revision** identifies retained bytes by immutable revision ID,
history, verified replica and a tested recovery route. Recovery evidence names
the revision and scope actually restored. A tag is an optional label; a hash
identifies content; neither alone establishes recovery. **Byte-exact recovery**
describes restored bytes, not rebuilding or executing software.

An **audit reference** is small metadata locating that revision, bounded scope,
replica and recovery evidence/limits. Source and earlier reports are read by
immutable locators, never collected into a new input directory. Reference
size follows present scope, not audit count. Native large evidence is kept once in a declared
store, cited by hash and replicated for recovery.

Pruning the worktree is allowed after actual restore/byte verification. A short
summary can replace detailed history in today's records, with exact immutable
locators and current successor manifests. Original sealed bytes and unknowns
remain historical; a tidy summary does not recover missing events.

## Traceability Without Repetition

COVERAGE links a meaningful file/region to its introducing or retaining record,
check, root, assurance level and validity. Whole-file rationale is sufficient
where it explains the file; a row for every heading is not inherently better.
A D record's inline check or E commit reason is a valid trace endpoint.

The owner controls goal/scope/authority and acceptance. The worker maintains
records and performs authorised technical work. A separate Project Auditor
checks support and reports gaps; it never repairs or runs technical tests.
Only fresh independent follow-up closes an audit finding. Code Audit remains
a distinct commission; ambiguous audit requests must ask the kind and wait.

## Review Changes, Not the Calendar Alone

A/B/C have justified finite review dates plus relevant triggers. D/E use
change-trigger review without default expiry. A simple text edit cannot extend
an underlying safety claim, and an unrelated old benchmark must not expire
stable documentation every week. Reclassification changes policy, not the
observed result of an old test. General VP cost/benefit and sustained AI
adherence still require real deliverable studies; self-application does not
establish them.

Current PROJECT, PLAN and STATE are short management views. A reader given
only STATE should identify stage, open findings and next action. Actual cold
reading and actual restoration are stronger evidence for that use than link
counts and matching hashes alone. [Examples](project-records-examples.md) and
[scenarios](project-records-scenarios.md) show the limits and failure cases.
