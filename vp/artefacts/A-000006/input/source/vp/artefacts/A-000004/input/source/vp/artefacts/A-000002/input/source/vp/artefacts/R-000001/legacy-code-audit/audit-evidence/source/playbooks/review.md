# Reasoning Review

Use this playbook to audit reasoning quality, goal alignment, and falsification discipline for the current project or work session. The output must be concise enough to read in two minutes.

## Inputs

Read:

- the available conversation or task history;
- current project instructions;
- active plans and progress records;
- version-control status and the relevant diff;
- all concept documents in `concepts/` if they are not already fresh in context.

If an `INVESTIGATION-STATUS.md` file exists at the project root, review the investigation with the criteria in [Investigation](investigation.md). Do not substitute a general project review. If a discovery report has just been produced, apply [Discovery Verification](discovery-verification.md) first.

## Review Dimensions

1. **Terminal goal** — Can it be stated in one sentence? Has the work drifted from it?
2. **Instrumental goals** — Do current tasks form a coherent path, or merely follow whatever is nearby?
3. **Human intent** — Does the work serve the outcome the user actually wants?
4. **Rhetoric** — Are authority, aesthetics, convention, or confidence being presented as evidence?
5. **Recorded state** — Are plans, progress, decisions, and commits current enough to recover the work?
6. **Falsifiability** — Do important choices have explicit disconfirming evidence and genuine attempts to find it?
7. **Verification** — Did relevant tests fail before the fix, pass afterward, and exercise the real integration where practical?
8. **Honest reporting** — Are negative and inconclusive outcomes visible, or only successes?

Ask a focused question when missing human context would materially change the conclusion. Do not fill the gap with a plausible assumption.

## Output

```markdown
# VP Review

## Status
[Two to four bullets describing overall health]

## Issues
[Concrete issues, each tied to evidence]

## Open Questions
[Only questions that affect a decision]

## Recommendations
[Strategic and immediate actions, each with an observable success or falsification condition]
```

## Rules

- Distinguish observed facts, interpretations, and unknowns.
- Cite files, commands, or results supporting each material finding.
- Do not confuse passing tests with proof of correctness.
- Do not turn a review request into implementation unless the user also authorises changes.
- If the honest recommendation is to discard work, say so and state the evidence threshold.
