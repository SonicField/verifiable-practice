# The Verification Cycle

The verification cycle governs implementation steps within [VP's full project quality management lifecycle](../docs/how-vp-works.md). Project authority, stages, records and gates supply its surrounding controls.

Safety comes from verbs, not nouns. Correctness emerges from actions - checking, validating, asserting, testing - not from static structures like type systems or design patterns.

"This value was validated" matters. "This has type ValidatedInput" does not, unless validation actually occurred. The verb happened or it did not. That is provable.

## The Cycle

```
Design → Plan → Deconstruct → [Test → Code → Document] → Next
```

Each phase has entry and exit criteria. Skipping phases is not speed; it is debt with compound interest.

| Phase | Entry | Exit |
|-------|-------|------|
| Design | Problem exists | Success criteria defined |
| Plan | Criteria clear | Testable steps identified |
| Deconstruct | Steps identified | Each step has test criterion |
| Test | Criterion defined | Check can expose the claimed failure; controls and outcomes recorded |
| Code | Authorised change and meaningful check defined | Criteria survive relevant checks; outcomes and limits retained |
| Document | Check outcomes available | Evidence, choices, source coverage and next action recorded |

This cycle applies to an implementation step. The adopted project records the reason and check at its consequence level: A/B need fuller commissioning/execution/acceptance records, C may combine them, D one change/check, E its commit message. Failures and inconclusive checks remain visible. Applicable gates, justified A/B/C dates and all-level change triggers manage integration, handoff and later changes. A useful positive control or deliberately planted defect can establish check sensitivity; a previous natural failure is not the only valid starting point.

## The Decomposition Criterion

If you cannot write a test for a step, either:
- You have not decomposed far enough, or
- You do not yet understand what you are building

"Implement authentication" is not testable. These are:
- Validate password meets complexity rules
- Hash password with salt
- Compare hash against stored hash
- Generate session token on success

Each step independently testable. Each test defines success.

## Assertions, Testing, and Dynamic Analysis

For the full assertion protocol, anti-pattern taxonomy, and language-specific patterns, see `engineering-standards.md`.

## The Practical Question

Before moving to the next step: what did I learn? Write it down. If you cannot articulate what you learned, you were not paying attention.

---

## Optional Onboarding

For an explicit request to learn the whole framework, follow the concept
sequence in [README](../README.md). For a bounded working task, use the
[skill routing](../SKILL.md) and read only relevant references; this section
does not require loading unrelated pillars.
