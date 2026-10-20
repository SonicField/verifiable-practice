# Verifiable Practice

Verifiable Practice—VP—is a vendor-neutral framework for making AI-assisted software work inspectable, falsifiable, and evidence-led. It treats plausible output as a hypothesis, not a result: clarify the goal, state what would disprove a claim, seek counterexamples, and report the evidence—including failures.

For the motivation and a worked example, read [Why Verifiable Practice](WHY.md).

The repository itself is a reusable AI skill. [SKILL.md](SKILL.md) contains the operating rules and routes an assistant to the relevant concepts and playbooks without loading the entire framework into context.

## Start Here

Read the concepts in this order:

1. [Goals](concepts/goals.md)
2. [Falsifiability](concepts/falsifiability.md)
3. [Rhetoric](concepts/rhetoric.md)
4. [Bullshit Detection](concepts/bullshit-detection.md)
5. [Verification Cycle](concepts/verification-cycle.md)
6. [Zero-Code Contract](concepts/zero-code-contract.md)
7. [Precise Technical English](concepts/pte.md)
8. [Engineering Standards](concepts/engineering-standards.md)

The short form is:

> Establish what matters. Define what would prove you wrong. Try to prove yourself wrong. Build in testable steps. Report what happened, not what sounds reassuring.

## Project Planning and Records

For projects that need an auditable history across sessions, the proposed
[Project Planning and Records Standard](standards/project-records.md) defines
Markdown documents, directory structure and actions for choices, builds,
experiments, changes, expiry and disposal. Its coverage inventory links
maintained code to the evidence and root goal that justify it.

Start with the [guide](docs/project-records.md), then the
[templates](templates/project-records/README.md) and
[execution playbook](playbooks/project-records.md). The
[design register](docs/project-records-design.md) records the observations,
generalisation and alternatives behind each material choice. Conformance is
declared for a scope and snapshot; it is not a claim of software correctness.

An [independent record auditor](docs/independent-record-audit.md) checks a frozen
packet, reports gaps and specifies evidence needed for closure. The working
AI repairs records and produces authorised technical evidence; a fresh
independent re-audit closes findings. The auditor remains outside technical
problem solving. This role split uses Markdown requests, reports and responses.

## Choose the Audit Kind

- **Project Audit:** records, decisions, evidence provenance, validity and
  why code exists. “Independent record audit” is an alias.
- **Code Audit:** implementation correctness and engineering quality.

For an ambiguous request such as “Please audit X”, the AI **must ask which
sort of audit is intended and wait before starting**. It must not guess or
silently perform both. See [Audit Routing](playbooks/audit-routing.md).

## Playbooks

Playbooks turn the concepts into repeatable work:

| Playbook | Use it when |
|----------|-------------|
| [Review](playbooks/review.md) | You need a short check for drift, weak evidence, and hidden assumptions |
| [Code Audit](playbooks/code-audit.md) | You need to audit a codebase and, if authorised, harden it with tests |
| [Investigation](playbooks/investigation.md) | A technical uncertainty needs a controlled experiment |
| [Debugging](playbooks/debugging.md) | A debugger should discriminate between explicit hypotheses |
| [Discovery](playbooks/discovery.md) | A project has scattered artefacts and unclear history |
| [Discovery Verification](playbooks/discovery-verification.md) | A discovery report must survive loss of conversation context |
| [Recovery](playbooks/recovery.md) | Valuable work must be reorganised without losing it |
| [Project Planning and Records](playbooks/project-records.md) | A project needs durable plans, traceable choices and evidence, or revalidation |
| [Project Audit](playbooks/record-audit.md) | A separate assessor reports project-record gaps and independently checks worker responses |
| [Audit Routing](playbooks/audit-routing.md) | An audit kind must be explicit; ambiguous requests require a question and answer |
| [Document Analysis](playbooks/document-analysis.md) | A document's stated purpose may differ from what it actually optimises |
| [Document Planning](playbooks/document-planning.md) | An important document needs a clear outcome and audience before drafting |
| [Document Description](playbooks/document-description.md) | You understand a system but need to explain it clearly |
| [Precise Technical English](playbooks/precise-technical-english.md) | A contract, state machine, or requirement cannot tolerate ambiguity |

## Documentation

The documentation explains the framework for human readers; the playbooks direct an AI performing the work.

| Document | Subject |
|----------|---------|
| [How VP Works](docs/how-vp-works.md) | Failure modes, architecture, verification loop, and limits |
| [Review and Audit](docs/review-and-audit.md) | Project Audit, Code Audit and lighter reasoning review have separate scopes and verdicts |
| [Discovery and Recovery](docs/discovery-and-recovery.md) | The boundary between learning and controlled mutation |
| [Investigations](docs/investigations.md) | Hypotheses, isolation, evidence, and honest verdicts |
| [Document Work](docs/document-work.md) | Analysis, planning, description, and local precision |
| [Testing AI Behaviour](docs/testing-ai-behaviour.md) | Scenario isolation, oracles, adversarial cases, and stochastic results |
| [Skill Architecture](docs/skill-architecture.md) | Progressive disclosure, platform adapters, and maintenance |
| [Project Records](docs/project-records.md) | Planning, decision history, custody and finite validity |
| [Project Records Design](docs/project-records-design.md) | Observations, generalisation, alternatives and falsifiers behind the proposed standard |
| [Worked Record Traces](docs/project-records-examples.md) | Compiled, interpreted and document work using the same record structure |
| [Project Records Scenarios](docs/project-records-scenarios.md) | Adversarial cases, cold-reader trials and process cost evaluation |
| [Independent Record Audit](docs/independent-record-audit.md) | Separate assessor/worker contexts, frozen packets, finding responses and closure |

## Using VP with Any AI Tool

Point an assistant at the repository's root `SKILL.md`, install the repository as a skill directory, or provide `SKILL.md` as project instructions. Ask it to “use VP” for the task. The skill selects the smallest relevant set of supporting documents.

The supporting files are plain Markdown and contain no vendor-specific tool instructions. Map capability names to the host tool rather than editing the method:

| Capability in a playbook | Possible implementation |
|--------------------------|-------------------------|
| Read/search files | Built-in file tools, shell search, or IDE search |
| Ask the user | Normal conversation or a structured question interface |
| Run checks | Shell, CI, test runner, or debugger integration |
| Parallel review | Sub-agents when available; bounded sequential batches otherwise |
| Record evidence | A durable file; conformant project records use Markdown and directory bundles |

A platform adapter may add permissions or command metadata, but the canonical skill and playbooks should remain platform-neutral.

## Scope Boundary

VP includes reasoning, verification, project archaeology, recovery, document
work and independent record assessment with worker remediation. The roles
can use separate sessions and directory handoff. VP does not include
coordination infrastructure for persistent multi-agent teams.

The framework's origin and extraction boundary are recorded in [ORIGIN.md](ORIGIN.md).

## Project Information

- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Changelog](CHANGELOG.md)
- [Citation Metadata](CITATION.cff)
- [MIT Licence](LICENSE)
