# Investigation

Use this playbook for a focused question that can be answered by experiment. An investigation produces evidence, not a feature.

## 1. State the Hypothesis

Turn the concern into one specific, testable claim. Confirm with the user:

- the hypothesis;
- the observation that would falsify it;
- the practical decision the result will inform.

Do not experiment until these are clear.

## 2. Isolate the Work

Use a reversible isolation mechanism appropriate to the project, such as an `investigation/<topic>` branch or a temporary worktree. Do not create or switch branches without checking for uncommitted work.

For a project that has adopted [record conformance](../standards/project-records.md),
classify first and use its level-appropriate records/current state through the
[records playbook](project-records.md). Keep the investigation linked to its
commissioning authority; A uses explicit H/E/R, B/C may combine permitted
fields, D its change/check. Do not create a competing root or extra H/E/R
solely for lower-level conformance.

For other VP work, create `INVESTIGATION-STATUS.md`:

```markdown
# Investigation: [Topic]

**Status:** In progress
**Hypothesis:** [One sentence]
**Falsification criterion:** [Observation that contradicts it]
**Decision informed:** [What this result will change]

## Experiment Log

## Verdict
```

## 3. Design Experiments

For each experiment specify:

1. the controlled action;
2. expected result if the hypothesis is falsified;
3. expected result if it survives;
4. conditions that make the result inconclusive;
5. how another person can reproduce it.

Prefer direct, minimal measurements over proxies. Change one variable at a time where possible.

## 4. Execute and Record

Run experiments one at a time. Append the command or procedure, environment, raw observation, and separate interpretation to the status file or adopted level-appropriate entry. Preserve unexpected results; do not normalise them away.

## 5. Reach a Verdict

Use exactly one result:

- **Falsified** — at least one valid observation contradicts the hypothesis.
- **Failed to falsify** — the evidence is consistent with the hypothesis, but does not prove it.
- **Inconclusive** — the experiment cannot distinguish the outcomes.

Record confidence, key evidence, limitations, and implications. Return to the original development context only after protecting any uncommitted work. Preserve the investigation record even when the hypothesis was wrong.
