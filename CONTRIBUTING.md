# Contributing to Verifiable Practice

VP is a research project for making AI-assisted software work inspectable, falsifiable, and evidence-led. Contributions are welcome when they make the framework clearer, more useful, or easier to test.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Before Opening an Issue

Search existing issues and read the relevant concept, playbook, or guide. For a problem report, include:

- what you were trying to achieve;
- the VP material and revision you used;
- the AI host or execution environment when relevant;
- what happened and what you expected;
- the smallest reproducible example;
- evidence such as prompts, outputs, or files, with secrets removed.

Do not publish sensitive security reports as ordinary issues. Follow [SECURITY.md](SECURITY.md).

## Proposing a Change

Describe:

1. the observed problem or missing capability;
2. evidence that the problem occurs;
3. the proposed change;
4. what observable result would show that the change did not help;
5. whether the change belongs in the shared skill, a concept, a playbook, a standard, a template, human-facing documentation, or a platform adapter.

Discuss broad changes in an issue before investing in a large pull request.

## Pull Requests

- Keep changes focused and explain the goal they serve.
- Preserve platform neutrality in `SKILL.md`, `concepts/`, `playbooks/`, and `docs/`.
- Put host-specific metadata or commands in a clearly isolated adapter.
- Update `SKILL.md` routing and `README.md` navigation when content files change.
- Use British English and preserve the existing direct style.
- Add or update behavioural scenarios when a change affects AI decisions.
- Report failed and skipped validation, not only successful checks.
- Update `CHANGELOG.md` under “Unreleased” for user-visible changes.
- For standards, preserve each material choice's observation, generalised
  requirement, applicability, alternatives and falsifier in a design record.
  Test across different work types; do not infer general validity from one project.

## Validation

Before submitting:

1. Validate `SKILL.md` frontmatter with an appropriate skill validator.
2. Check that every relative Markdown link resolves.
3. Check Markdown code fences and formatting.
4. Search canonical material for accidental vendor-specific terminology.
5. Confirm that `SKILL.md` routes to every concept, playbook, and explanatory document.
6. Review the diff for duplicated guidance and unjustified absolute rules.

## Licence

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
