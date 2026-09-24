# Skill Architecture

Verifiable Practice is distributed as a self-contained skill repository. Its architecture separates selection, operating instructions, and supporting detail so an AI loads only what the current task needs.

## Repository Layers

```text
verifiable-practice/
|-- SKILL.md       Skill metadata, shared rules, and routing
|-- concepts/      Stable reasoning principles
|-- playbooks/     Operational procedures for particular tasks
|-- docs/          Human-facing explanation and maintenance guidance
|-- README.md      Project entry point
`-- ORIGIN.md      Extraction provenance and scope boundary
```

### Skill Entry Point

`SKILL.md` contains a concise description for discovery, rules common to every VP task, and a routing table. It should not absorb the detailed procedures from every playbook. Doing so would consume context before the assistant knows which material is relevant.

### Concepts

Concepts explain why a practice exists and what distinction it preserves. They should remain independent of specific AI products, command syntaxes, repository hosts, or orchestration systems.

### Playbooks

Playbooks tell an assistant how to perform a bounded class of work. They may require capabilities such as reading files, running tests, or asking a question, but should not name a vendor's implementation of those capabilities.

### Documentation

Documentation explains VP to human readers. It may overlap in subject with a playbook but should not duplicate operational instructions. The document explains the method and trade-offs; the playbook directs execution.

## Platform Adapters

A host may require installation metadata, permission declarations, command wrappers, or UI configuration. Keep those in a separate adapter layer. An adapter may translate “search the repository” into a host tool, but it must not silently alter the method or expand authority.

Grant the minimum capabilities required for the selected mode. A review should not receive write permission merely because another VP playbook can modify files. A code audit should remain read-only until repair is separately authorised.

## Changing the Skill

When adding or changing material:

1. establish the observed failure or missing capability;
2. place shared rules in `SKILL.md` only when they affect most VP work;
3. place substantial conditional guidance in one focused reference;
4. add a route from `SKILL.md` and a human-facing link from `README.md`;
5. verify relative links, frontmatter, and platform neutrality;
6. test behavioural changes in an isolated scenario when the change affects AI decisions.

Avoid accumulating rules for hypothetical failures. The skill itself should evolve through evidence.
