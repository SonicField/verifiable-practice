# Bounded instruction-reading response

## Inputs and limits

Repository: `/home/alexturner/verifiable-practice`.
Immutable input revision: `0fffb29c09b38dd17756de91d6e58fd5da055340`.
All six inputs were read using `git show` at that revision:

- `vp/artefacts/C-000008/instruction-probe/request.md`
- `standards/project-records.md` — version 1.2, 21 October 2026
- `templates/project-records/build.md`
- `templates/project-records/run.md`
- `templates/project-records/manifest.md`
- `templates/project-records/workspace.md`

I am a separately commissioned working instruction reader, not a Project Auditor. My visible context includes the coordinator's bounded assignment, the session's system/developer instructions and environment description, and the six inputs above. I did not read other project files, C8 records, scenario answers, worker conversations or private plans. This is a single bounded response, completed within five minutes; no build, experiment, cleanup, repair, assessment or commit was performed. The only project write is this response.

The session identifies the assistant as Codex based on GPT-6. An exact deployed model identifier, sampling settings and independently verified context-isolation details are not available to me. The provided environment names Bash, the repository working directory, date 2026-10-21 and America/Los_Angeles timezone. Those are supplied configuration descriptions, not independently measured experimental conditions. This response does not claim audit independence or project conformance.

## Cases

### 1. Compiled benchmark, executable digest only

The missing executable bytes do not themselves constitute missing required evidence under the stated conditions. Keep its digest as the identity of what ran, together with the retained source/patches, dependency and toolchain specifications, commands, configuration, workload inputs, raw measurements and analysis. Relevant actual environment details, failures and limitations also belong in the appropriate record. Unique workload inputs must be accessible where needed, not merely named by an unretrievable digest.

The record supports a recorded recipe and examination of the retained observations. It does not support a claim that rebuilding, environment reconstruction or experiment repetition succeeded: those are untested. Dependency availability and custody/replica verification are not supplied by the case and remain unknown. There is no default obligation to recover or retain the executable.

### 2. Sole raw measurements in a binary format

Retain the file as required evidence. Its role as the sole measurements supporting the result controls retention; its binary format does not make it a disposable build product. Preserve accessible bytes, identity, provenance/capture limits, immutable history and a verified independent replica with a documented recovery route. A digest alone cannot replace those measurements. Its current copy may be removed only when required bytes remain recoverable and consumers can resolve them. Disposal of the only retained bytes would require explicitly limiting or withdrawing the unsupported reliance rather than continuing to present the result as supported.

### 3. Lost original raw log, executable retained

Keeping the executable and its digest does not replace the historical observations. Record that the original raw log is lost, identify the affected run and retained evidence, and state which claims can no longer be examined or supported. Trace and contain affected reliance according to the applicable level; the impact is unknown until investigated. The digest identifies executable bytes, not the run's actual output or historical action.

A later rerun would be a separately identified attempt with new evidence. Its output cannot be labelled the original historical capture. Whether independent copies or other sufficient original observations survive is unspecified; do not assume either restoration or total loss beyond the stated log.

### 4. Unreconstructable proprietary environment, old executable retained

Record the recipe, known toolchain/environment identity and limits, available source relationship and the executable identity. State that environment reconstruction is unavailable; do not report a successful rebuild or experimental reproduction. The old executable's availability alone proves neither. Even a later successful execution would need its own inputs, observations and comparison before supporting a repeated-result claim.

The reconstruction gap does not automatically create an obligation to retain the executable bytes. They may remain a working resource, subject to ownership, use and consumer checks. If some concrete replay, evidence, deliverable or external obligation actually requires these bytes, declare that role, owner/consumers, period and custody. No such obligation is established here.

### 5. Contract requires exact shipped executable bytes

These bytes have a specific retained deliverable role. Preserve the exact shipped bytes for the contractual support period, with their immutable identity and accessible retrieval location, release relationship, concrete contract requirement, owner/consumers, period and custody recorded in the existing record/manifest. Required custody includes immutable history and a verified independent replica with a tested recovery route and disclosed failure-domain limits. A checksum or rebuild recipe cannot substitute for the required shipped bytes.

Current copies may move or be pruned only while the required bytes remain preserved and resolvable under those controls. After the contractual period, check remaining evidence roles, consumers and applicable retention policy before changing their disposition; expiry of this one obligation does not establish that all obligations ended. The records and evidence required by the project retention policy still have their own retention terms.

### 6. Finished temporary diagnostic executable

Confirm its owner, completion/use condition, existing cleanup authority, active consumers and absence of a specific byte-retention obligation. Preserve the relevant executable identifier and all required source patches, reproduction specifications and raw comparison evidence in their appropriate durable custody, including the verified replica. Record the resource's role and disposition at the applicable level; an existing entry can suffice.

With those checks satisfied, routine disposal is permitted. It does not require capturing, replicating or restoring the executable first, nor a new manifest or per-file form solely for this temporary resource. The retained comparison supports only its recorded inputs and observations; successful rebuilding or repetition is a separate question.

### 7. Imported executable with unknown source/build provenance

Keep the digest/build identity available, actual command and raw output, relevant known inputs/environment/status and explicit source/build provenance gaps. Retain required raw evidence and records under the custody rules. Describe the build as imported; do not invent source provenance or claim that a build was reproduced. Other run details not supplied in the case remain unknown.

Where the executable has no required retained-byte role, its absence alone is not an evidence-custody failure. Its digest remains a provenance identifier with unavailable-byte limits. Absence of required raw output or other unique evidence would be a different gap. The known output can support a bounded observation, but the digest does not authenticate who ran it, when it ran or the truth of every interpretation.

### 8. Repository bytes restored exactly

This demonstrates byte-exact recovery of the named retained repository source/record scope actually restored and compared, including modes if those were checked. Identify that revision, scope, recovery route, replica and comparison evidence where known; do not infer that unspecified external evidence, other revisions or executable/environment bytes were also restored.

No build reconstruction, environment reconstruction, executable behaviour check or experiment repetition has been demonstrated. Historical action, timing and authority are not authenticated by matching restored bytes. A recoverable-revision claim additionally needs immutable history, a verified independent replica and the documented tested route; exact restoration by itself does not establish every one of those properties. The stated byte recovery therefore leaves experimental reproducibility untested.

## Common qualification

The cases do not specify assurance levels, complete custody facts or all consumers. I have applied the evidence-role rules without inventing those facts or requiring every VP form. Existing level-appropriate records may carry these distinctions. Recorded recipes, tested reconstruction, repeated experimental results and byte recovery must remain separate claims, each bounded by its actual evidence.
