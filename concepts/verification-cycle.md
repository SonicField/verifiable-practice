# The Verification Cycle

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
| Test | Criterion defined | Test written and fails |
| Code | Test fails correctly | Test passes, assertions hold |
| Document | Test passes | Learnings recorded |

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
