# Project Records: Design Rationale

This is current rationale for standard 1.1. Original detailed design choices,
source observations from parallel_gc and NBS, and their historical limits
remain at `records-archive-2026-10` / `9605ad0:docs/project-records-design.md`.
The repository’s D26/R13 operational records preserve the owner review,
generalisation, alternatives and pre-action checks as self-application evidence.
They are not required inputs or record files for other projects.

## Enduring Responsibilities

PRINCE2 inspired bounded stages, continuing value and exception decisions;
Capability Maturity Model ideas inspired repeatability/improvement; aircraft
maintenance inspired identity, history and review triggers. NBS Medic/Pythia
inspired the distinct assessor who reports gaps without joining implementation.
These are design inspirations, not claimed certification or required runtimes.

Authority stays separate from empirical evidence. A root mandate constrains
owner/worker decisions; fresh tests cannot manufacture permission or history.
Failed attempts remain recoverable. A human or AI owner must have a bounded
mandate; the worker keeps routine records, and the auditor remains distinct
from every author it assesses. Ambiguous audit requests ask the kind first.

## 1. Scale by Failure Consequence

**Observation:** self-adoption applied many records and a full audit to an
8KB retirement. Saying “be proportional” did not tell a worker what to omit.
**General problem:** an unlimited objective list rewards ceremony because
there is no stopping rule based on consequence.
**Choice:** explicit A–E minimum forms, pre-action classification, operational
C/D boundary, higher level on disagreement, and only declared independent gates.
D uses one change/check; E its commit message. A/B keep strong independent
controls; C uses stated samples/stages. D/E use event review, not weekly expiry.
**Alternatives rejected:** the same record set for everything; no records at
all; severity inferred from filename/line count; consequence reduction by
unproved assumptions or a project's low-risk label.
**Falsifiers:** The wording-technique retirement replay still requires multiple records/an audit,
or independent classification fails its predeclared agreement threshold.
Actual participant results, including the failed first trial, belong in R13.
Small sample agreement does not establish reliable classification everywhere.

The owner's review proposes a DO-178C-inspired structure and cites
[DO-178C](https://en.wikipedia.org/wiki/DO-178C) and a
[summary of FDA Computer Software Assurance guidance](https://www.hlc.com/en/publications/fda-finalizes-computer-software-assurance-guidance-for-production-and-quality-system-software).
These supplied references motivate a risk-based analogy. External retrieval
was unavailable in this environment; VP does not assert the cited numerical
objective counts, finalisation date or regulatory compliance. Consult the
[current FDA source](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/computer-software-assurance-production-and-quality-system-software)
when applying domain regulation; that domain's actual requirements prevail.

## 2. Identity, Availability and Restoration

**Observation:** copied audit input directories nested earlier copies and stale
instructions outnumbered current ones. A Git bundle reduced storage but did
not remove searchable obsolete copies.
**General problem:** identity was confused with availability, and input
selection had no stopping rule. A copy looked safer while its cost landed later.
**Choice:** require immutable content-addressed revision history and a verified
independent replica; reference historical bytes, never copy source or earlier
audit references into today's worktree. Large external evidence is stored once per
content-addressed store and replicated. Audit reference metadata depends on present
scope, not the number of past audits. Current locator manifests resolve the
original exact manifests instead of repeating every old source inventory.
**Alternatives rejected:** directory copies without revision history;
hashes without retrievable bytes; assuming Git supplies a replica; recursive
scope expansion; silent loss disguised as cleanup.
**Falsifiers:** later audit references contain earlier audit reference/source contents,
working-tree growth follows audit reference history, product hashes have undocumented
duplicates, or a promised recovery is never actually performed.

## 3. Keep Current Views Useful

**Observation:** detailed records outweighed the method; first-read views had
compressed words and previous-stage narratives. Consistency audits passed
without a cold-reader outcome.
**General problem:** record completeness is not usable continuity. A future
worker needs current state and a route to history, not all history in view.
**Choice:** preserve baseline tag/verified restore, then prune current copies
and detailed adoption records. Keep one summary, exact historical locators and
short plain current views. Reclassify review policy without renewing old tests.
**Alternatives rejected:** archival document directories; rewriting originals
as new captures; retaining weekly expiry on stable prose; a link-count proxy
for understanding.
**Falsifiers:** multiple live skill instructions or a retired technique document remain in the worktree,
removed bytes cannot be restored, or a fresh reader given only STATE misstates
stage/open findings/next action. R13 captures actual evidence and limits;
independent Project Audit checks that evidence without performing repairs.

## 4. Name Preservation Properties Directly

**Observation:** container language in the re-audit route still suggested
collecting old reports, despite the explicit reference-only custody contract.
The owner requested terminology that describes tags, hashes and recovery.
**General problem:** a preservation metaphor obscures which properties are
actually established, and encourages manual copies as a substitute.
**Choice:** call the retained identified state a **recoverable revision**,
with immutable identity/history, verified replica and scoped recovery evidence.
Call the small metadata locator an **audit reference**. State **byte-exact
recovery** only for the tested revision/paths, separate from build reproduction
or executable behaviour. These names apply to code, documents and native data.
**Alternatives rejected:** tagged alone (labels can move); hashed alone
(missing bytes are still missing); binary recoverable (can imply execution or
a reproducible build); directory collections (reintroduce duplicate history).
**Falsifiers:** a route instructs copying inputs; a moved tag changes an
identified audit input; unavailable hashed bytes are called recoverable; a
source restore is represented as a successful build. The repository C7
records the current choice/check; other projects do not need that record.
Existing consequence forms and independent gates remain the contract.

## Remaining Research Question

These changes test record usability, bounded repeatability and recovery in
this repository. They do not show VP produces better real deliverables than
a lighter regime. That comparison needs a scoped task, outcome/cost measures,
baseline and independent evidence before a benefit claim is retained.
