# Owner-supplied review

Source: /home/alexturner/.codex/attachments/dd82533c-5352-4fe6-adb1-1c5598c7e99e/pasted-text-1.txt; SHA256 7a4fbfd060a6b873165e04c0e2b0bd6533e2de16b2dd8c137ee769efe4f977dc; captured 2026-10-21 12:36:42 UTC. The active owner goal instructs action on all three concerns. The pasted review is evidence/proposals, not proof of external certification claims.

None selected 

Skip to content
Using Meta Mail with screen readers

Conversations
 
Program Policies
Powered by Google
Last account activity: 39 minutes ago
Details
# Verifiable Practice review and proposed changes

Repository reviewed at commit `9605ad0` (SonicField/verifiable-practice), 21 October 2026.

## Initial impressions

### What works

The method documents read well. WHY.md, the working rules and the completion standard in SKILL.md are the strongest part. An assistant can act on them after one reading, and the email validation example makes the falsification point without fuss.

Underneath, VP is a way of working with a collaborator who is capable, forgets everything between sessions, and is indifferent to truth unless something makes truth matter. Conventional project methods assume a worker who remembers and who can be held to account later. VP assumes neither, and its best ideas follow from that.

- **Falsifiers before reliance.** A claim needs a stated refuting observation before anything is built on it, and negative results are reported as prominently as positive ones.
- **Authority kept separate from evidence.** A passing experiment grants no permission, and inspection does not authorise repair.
- **An auditor with a fresh context.** The assessor cannot repair what it finds, and only a fresh assessment closes a finding. With AI, independence is cheap, because it only requires a session that has not seen the work.
- **Traceability to the root goal.** Every maintained artefact leads back through change, decision and evidence to the authorised purpose, with failed attempts left visible.
- **Justification expires.** Review horizons and triggers force revalidation when a model, runtime or premise changes.
- **Missing history stays missing.** The adoption mandate asked how the worker would cope where the required information was totally missing. It never invented the past. The phrase "original historical intent unknown" appears 226 times, and legacy claims are kept apart from current reliance.

### What the self-application revealed

- **Audit packets nest recursively.** Each audit froze the whole repository, including earlier audits' frozen packets. Packet sizes grew to 166, 589, 1,262, 2,874, 5,799 and then 11,616 files. A clone checks out 23,353 files and roughly 450MB to carry 69 product files. Git hides much of this, with 588 distinct blobs in a 6MB pack. The worker switched to Git bundles for A7, but the sealed copies remain.
- **Stale copies pollute the tree.** The retired `concepts/pte.md` still exists 207 times in the working tree. There are 216 copies of SKILL.md, 215 of them obsolete. Any agent that searches the repository for guidance will find stale versions far more often than the live one.
- **The paperwork outweighs the product.** The records run to about 54,000 words, against about 35,000 for the method. Retiring PTE, two files totalling 8KB, produced thirteen records and an audit report of around 2,000 words. SKILL.md asks for proportion, yet the repository applies the heaviest form to itself.
- **Legibility has decayed where it matters most.** STATE.md and PROJECT.md, the views a returning reader opens first, contain run-together text such as "D12owner-selectedcontentassessment/repair →R7baseline" and "Allfailures/rawbytesremain". A7 passed them as conformant.
- **The audit measures consistency rather than usefulness.** A7 verified that 801 links resolve, that every origin chain reaches D1 and that the hashes agree. Nothing tests whether a cold reader can follow the record.
- **The hashes prove less than they appear to.** A process the worker controls computes them on the same host. They show that nothing changed after capture, not who did what or when. The records state this candidly.
- **Short validity windows create churn.** Most current justification lapses on 26 October, so a documents project with no running code has a weekly revalidation cycle built in.

### Why AI work freezes and copies

This is a general pattern in AI designed systems, not peculiar to VP. Several mechanisms seem to compound.

- An agent lives in snapshots. With no continuity between sessions, it represents history as frozen states rather than as a relationship between versions. A copy is self-evidently present, whereas a commit reference requires trusting a later reader's tooling.
- Copying is never punished, while deletion often is. Duplication never looks like a mistake when it happens, and its cost lands later on someone else.
- Identity gets confused with availability. Content addressing in Git is the strongest identity guarantee available. The worker's real worry was whether the bytes would remain reachable, and it answered that by copying, where a replica answers it properly.
- No snapshot boundary was defined. "Freeze everything the assessor might need" naturally includes earlier frozen packets, which produces the doubling.

VP contributed to this itself. The method requires only Markdown and directories, and the charter repeatedly says Git is optional for other projects. That leaves the standard with no notion of history except copying, so the worker was arguably following the design.

### The open question

All of VP's current evidence comes from applying it to itself, which tests record discipline rather than outcomes. Whether VP produces better results on a real deliverable than a lighter regime would remains unknown, as the README concedes.

---

## Issue 1. Scale assurance to the consequence of failure

### Problem

SKILL.md says rigour should be proportionate and that small changes need no ceremonial paperwork, but the method gives no rule for how much record a change earns. An agent therefore defaults to maximum ceremony, because maximum ceremony can never be faulted. The PTE retirement is the evidence. A low-consequence documentation change received the full treatment.

### Proposed fix

Adopt the structure of DO-178C Design Assurance Levels. In avionics, the severity of a failure fixes both how many objectives apply and how many need independent verification.

| DAL | Failure effect | Objectives | With independence |
|---|---|---|---|
| A | Catastrophic | 71 | 30 |
| B | Hazardous | 69 | 18 |
| C | Major | 62 | 5 |
| D | Minor | 26 | 2 |
| E | No safety effect | 0 | 0 |

Source [DO-178C](https://en.wikipedia.org/wiki/DO-178C).

A VP version might read as follows. The consequence categories are a starting proposal for the owner to settle.

| VP level | Consequence if the change is wrong | Required records | Independent audit |
|---|---|---|---|
| A | Harm to people, regulatory breach, or irreversible loss | Decision with falsifier, hypothesis and protocol before execution, run evidence, owner acceptance | Fresh auditor reviews the protocol before execution and the result before acceptance |
| B | Serious loss or costly recovery | Decision with falsifier, run evidence, owner acceptance | Fresh auditor before acceptance |
| C | Significant rework or a user-visible defect | Decision with falsifier and run evidence | Sampled, or at stage gates |
| D | Minor and easily reversed | Change record giving the reason and the check performed | None |
| E | No effect on behaviour or meaning (typos, formatting) | Commit message | None |

Further points.

- The level is assigned before work starts, and the assignment is itself recorded. If the owner and worker disagree, the higher level applies.
- Validity horizons scale with the level. Levels D and E need no expiry date beyond their change triggers.
- Most edits to VP's own documents would fall at D or C.
- FDA Computer Software Assurance, finalised in September 2025, supports the same principle for regulated industry. Features are classed by process risk, and documentation need only show fitness for intended use. Citing it will help VP's case with regulated readers. See [Hogan Lovells summary](https://www.hlc.com/en/publications/fda-finalizes-computer-software-assurance-guidance-for-production-and-quality-system-software).

### Falsifiers and acceptance

- Replay the PTE retirement under the scale. It should classify at D and produce no more than a change record and a check. If the scale yields the same ceremony as before, it has failed.
- Give two fresh assessors the same ten historical changes to classify independently. Substantial disagreement would show the level definitions are too vague to use.

---

## Issue 2. Make revision control the mandatory custody mechanism

### Problem

VP requires only Markdown and directories. With no notion of history except copying, audit packets froze the whole repository, including earlier packets, and grew by doubling. Copies preserve bytes while misleading every later search.

### Proposed fix

- Replace the "Markdown and directories, no specialised software" requirement with a statement of the properties custody needs. These are content-addressed identity, immutable history and at least one independent replica. Git provides all three, and a project using anything else must show equivalence.
- Evidence is cited by commit and path, or by blob hash. It is never copied into the working tree.
- An audit packet consists of a commit ID, the list of paths in scope and the location of a verified replica or bundle. It contains no copied source.
- Earlier packets are referenced by hash and never included, and the standard should prohibit recursive freezing explicitly.
- Raw evidence that does not belong in version control, such as large binaries or external logs, is stored once and referenced by hash.
- Removing material from the working tree is permitted when its content remains in history and in the replica. The disposal is recorded by the commit that performs it.

### Falsifiers and acceptance

- The size of an audit packet must not depend on how many audits came before it.
- After several audit cycles, the working tree file count should grow no faster than the product and its records.
- A hash scan of the working tree should find no duplicate of any product file, apart from deliberate exceptions that are documented.

---

## Issue 3. Prune this repository's records

Depends on Issue 2 being accepted, so that the pruning follows the new custody rule.

### Problem

The working tree holds 23,353 files and about 450MB for a method of 69 files. It contains 207 copies of a retired document and 215 obsolete copies of SKILL.md. The current views are hard to read, and the records outweigh the method.

### Proposed fix

1. Tag the current commit (for example `records-archive-2026-10`) and verify a bundle on an independent replica, preferably off-host.
2. Remove the nested packet sources under `vp/artefacts/` with `git rm`. Keep the manifests, rewritten to cite commit and hash in place of copied paths.
3. Replace the adoption experiment's detailed records with a single short summary record. It should state what the experiment did and found, and that the full records are preserved at the tag.
4. Rewrite STATE.md, PROJECT.md and PLAN.md in short, plain prose. Each should state the current stage, open findings and next action. Stage narratives belong in Git history, not in PROJECT.md.
5. Reclassify open validity windows under the Issue 1 levels, removing the weekly churn on documentation.

### Falsifiers and acceptance

- Searching the working tree for SKILL.md returns exactly one file, and searching for pte.md returns none.
- The working tree file count is close to the product files plus the records, with no nested copies.
- Every byte removed can be recovered from the tag and the replica, and this is checked by an actual restore rather than by inspecting hashes.
- A fresh session given only STATE.md can state the current stage, the open findings and the next action correctly, as checked against the records. Failure on this test means the rewrite has not achieved its purpose.
vp-review.md
Displaying vp-review.md.