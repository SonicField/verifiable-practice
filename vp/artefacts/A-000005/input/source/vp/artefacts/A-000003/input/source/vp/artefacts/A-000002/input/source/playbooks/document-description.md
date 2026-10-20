# Document Description

Help a user describe a system, codebase, process, or concept they understand but have not yet expressed clearly.

## Process

1. Establish what is being described and inspect it when source material is available.
2. Identify the exact audience and the decision or task the description must enable.
3. Ask for the three facts the audience must understand.
4. Identify common misconceptions and confusing boundaries.
5. Surface inputs, outputs, state changes, dependencies, failure modes, and non-goals as applicable.
6. Test possible analogies. State where each analogy breaks.
7. Propose an outline, then draft only after the user confirms the model.
8. Check the draft against the real system and the stated reader outcome.

## Suggested Structure

```markdown
# [Thing]

## What It Is
## Why It Exists
## How It Works
## Boundaries and Non-Goals
## Failure Modes
## Example
```

Good description is translation, not transcription. Prefer a small accurate model over exhaustive detail. Mark simplifications, and never let an analogy silently become a claim about implementation.
