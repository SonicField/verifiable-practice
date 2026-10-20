# Project Recovery

Recovery restructures a project after discovery while preserving valuable outcomes. It is the action phase; use a verified discovery report whenever one exists.

## 1. Load the Evidence

Read the discovery report. Confirm with the user whether anything has changed and whether any verdict has been reconsidered. If no report exists, explain the risk and perform discovery first unless the user explicitly chooses a narrower recovery based on current evidence.

## 2. Plan Reversible Steps

For each step record:

| Field | Requirement |
|-------|-------------|
| Action | One precise filesystem or documentation change |
| Reason | Link to the discovery finding it serves |
| Preconditions | What must be true before execution |
| Verification | What will demonstrate success |
| Reversal | How to undo it without data loss |
| Status | Pending, complete, skipped, failed, or rolled back |

Order the steps by dependency. Present the plan before execution. Obtain confirmation before destructive or materially irreversible actions; never infer deletion authority from a general cleanup request.

## 3. Execute Incrementally

For each step:

1. validate preconditions and check for concurrent or uncommitted changes;
2. make the smallest planned change;
3. run the stated verification;
4. record the result and unexpected observations;
5. stop on failure or material divergence and decide whether to revise, skip, or reverse.

Copy or archive before removing originals. Prefer version-controlled, recoverable operations.

## 4. Establish Durable Structure

When adopting formal record conformance, use the
[Project Records Standard](../standards/project-records.md) and
[records playbook](project-records.md). Preserve the legacy path-to-record
mapping and label reconstructed history; new justification does not recover
missing past evidence.

Leave behind:

- a clear README and navigable layout;
- a plan containing terminal and instrumental goals;
- a progress or recovery log;
- falsification criteria for preserved claims;
- version history where appropriate;
- explicit exclusions and unresolved questions.

## 5. Verify Completion

Check that preserved artefacts are intact and usable, links and references resolve, key results can be reproduced, and the resulting project matches the agreed terminal goal. Report skipped checks and failures. Ask the user to validate semantic alignment when only they can judge it.

A clean directory tree is not sufficient evidence of recovery. The valuable outcomes must remain accessible, attributable, and verifiable.
