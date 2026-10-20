# Skill Architecture

Verifiable Practice is a full project quality management system for human–AI collaboration, distributed as a self-contained skill repository. The [method overview](how-vp-works.md) explains governance, planning, quality control/assurance, acceptance and maintenance. This architecture separates discovery, procedures, normative contracts, templates and actual project records so an AI loads the references needed for its role and task.

## Repository Layers

```text
verifiable-practice/
|-- SKILL.md       Skill metadata, shared rules, and routing
|-- concepts/      Stable reasoning principles
|-- playbooks/     Operational procedures for particular tasks
|-- docs/          Explanation for human and AI readers
|-- standards/     Normative contracts for explicitly adopted practices
|-- templates/     Copyable Markdown documents and record fields
|-- vp/            This project's instantiated charter, records and evidence
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

Documentation explains the complete method or a component to human and AI readers. It may overlap in subject with a playbook but should avoid duplicating detailed procedures. Explanations establish the model and trade-offs; playbooks direct the selected task; standards retain adopted requirements.

### Project Records and Evidence

A project's selected record root contains its charter, plan, state, ledger, coverage, typed records and owned raw evidence. The working AI maintains them under owner authority. These files are the actual project history and management state; explanatory guides and template examples cannot substitute for them. Source/decision/evidence identities, failed attempts, validity and custody remain inspectable across sessions. Independent Project Audit assesses a frozen copy through a distinct context.

### Standards and Templates

Standards define testable conformance requirements for explicitly adopted
practices. Templates expose required document fields without adding a software
dependency. Keep normative requirements in the standard, action order in the
playbook, and design rationale in explanatory records. Route all three from
the skill and README.

## Platform Adapters

A host may require installation metadata, permission declarations, command wrappers, or UI configuration. Keep those in a separate adapter layer. An adapter may translate “search the repository” into a host tool, but it must not silently alter the method or expand authority.

Grant the minimum capabilities required for the selected mode. A review should not receive write permission merely because another VP playbook can modify files. A code audit should remain read-only until repair is separately authorised.

For independent record audit, give a fresh assessor context the immutable
request and packet, read access to referenced evidence, and write access only
to its own audit outputs. Keep technical execution and worker-record repair
in a separate working context. Host permissions can enforce this boundary;
directory requests and role instructions still define it when enforcement
is unavailable. Record enforcement/custody limitations explicitly.

## Changing the Skill

When adding or changing material:

1. establish the observed failure or missing capability;
2. place shared rules in `SKILL.md` only when they affect most VP work;
3. place substantial conditional guidance in one focused reference;
4. add a route from `SKILL.md` and a human-facing link from `README.md`;
5. verify relative links, frontmatter, and platform neutrality;
6. test behavioural changes in an isolated scenario when the change affects AI decisions.

Avoid accumulating rules for hypothetical failures. The skill itself should evolve through evidence.
