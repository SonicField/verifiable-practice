# Project Discovery

Discovery is a collaborative, read-only process for understanding a project whose artefacts, history, goals, or value are unclear. It produces a durable report for recovery; it does not reorganise the project.

## Phase 1: Establish Context

Ask the user what the project was trying to achieve, when the work occurred, where related artefacts may exist, what outcomes matter, and what they remember as false starts. Their memory supplies intent that files cannot establish.

Do not treat memory as proof of technical behaviour. Treat it as primary evidence of purpose and value, then verify technical claims against artefacts where possible.

## Phase 2: Archaeology

For each agreed location:

1. inventory what exists without changing it;
2. identify likely relevance from names, dates, version history, and small metadata reads;
3. present the map and resolve ambiguous scope with the user;
4. read relevant artefacts deeply;
5. record evidence and unresolved questions.

Avoid executing unknown project code during discovery unless the user separately authorises diagnostic execution.

## Phase 3: Triage

Build this table with the user:

```markdown
| Artefact | Location | Intended purpose | Evidence | Verdict | Action |
|----------|----------|------------------|----------|---------|--------|
| ... | ... | ... | ... | Keep / Archive / Evaluate | ... |
```

Distinguish what the artefact claims, what the user remembers, and what current evidence demonstrates.

## Phase 4: Gap Analysis

Compare the preserved outcomes with the terminal goal. Work through a small set of consequential questions one at a time. After each answer, restate the understanding and ask the user to correct it. Preserve confirmed restatements in full; they are recovered knowledge, not conversational debris.

Convert the confirmed gaps into ordered instrumental goals with dependencies and verification criteria.

## Output

Create a discovery report containing:

- date and one-sentence terminal goal;
- searched locations and explicit exclusions;
- artefact inventory and triage;
- valuable outcomes with evidence pointers;
- gaps and ordered instrumental goals;
- full confirmed restatements;
- open questions and uncertainty;
- recommended recovery actions.

The report must stand alone. Recovery must not depend on inaccessible conversation history.
