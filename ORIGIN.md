# Extraction Notes

This package was extracted from NBS Framework revision `a1084a3` on 2026-09-24.

The current VP method is a [full project quality management system for human–AI collaboration](docs/how-vp-works.md). The extraction inventory below records its original provenance. Later extensions introduced portable owner, worker and independent auditor responsibilities, controlled project planning and record management. Those current responsibilities are distinct from the source framework's excluded persistent-team implementations.

## Retained Material and Extraction Sources

The original “Why NBS” essay and selected concepts concerning human–AI software reasoning were adapted. The retained generic playbooks derive from the original review, audit, investigation, debugger, discovery, recovery, document-analysis, document-planning and document-description commands. This inventory describes current retained material; earlier inventories remain in Git history.

| Core material | Source material |
|---------------|-----------------|
| `WHY.md` | `docs/framework/Why-NBS.md` |
| `concepts/` | Selected documents directly under the source `concepts/` |
| `playbooks/review.md` | `claude_tools/nbs.md` and `docs/framework/nbs-review.md` |
| `playbooks/code-audit.md` | `claude_tools/nbs-audit.md` and `docs/framework/nbs-audit.md` |
| `playbooks/investigation.md` | `claude_tools/nbs-investigation.md` |
| `playbooks/debugging.md` | `claude_tools/nbs-gdb.md` |
| Discovery and recovery playbooks | Corresponding `claude_tools/nbs-*.md` files |
| Document playbooks | `claude_tools/nbs-doc-*.md` |
| `docs/how-vp-works.md` | `docs/framework/overview.md` and `docs/getting-started/01-what-nbs-is.md` |
| `docs/review-and-audit.md` | `docs/framework/nbs-review.md` and `docs/framework/nbs-audit.md` |
| `docs/discovery-and-recovery.md` | `docs/framework/discovery.md` |
| `docs/investigations.md` | `docs/framework/investigation.md` |
| `docs/document-work.md` | `docs/framework/nbs-doc.md` |
| `docs/testing-ai-behaviour.md` | `docs/tools/testing-strategy.md` and the portable parts of `docs/tools/interactive-testing.md` |
| `docs/skill-architecture.md` | The portable design principles from `docs/framework/skill-system.md` |

## Excluded from the Original Extraction

- `concepts/teams/` and the top-level coordination concept;
- supervisor, worker, gatekeeper, testkeeper, theologian, scribe, medic, librarian, and other team roles;
- chat, bus, polling, sidecar, hub, cursor, restart, and notification machinery;
- Claude Code frontmatter, slash-command installation, and `CLAUDE.md` integration;
- interactive help wrappers, mode-reset commands, and the optional Oracular Speech register;
- terminal-weathering, remote-development, manifest-maintenance, and other project-specific operations.

## Generalisation Choices

The extracted playbooks describe capabilities rather than product tool names. They do not assume slash commands, a particular home-directory layout, conversation APIs, or sub-agent support. Parallel work is optional and bounded. Audit and repair are explicitly separated so that a read-only request does not imply permission to edit code.

The source framework remains unchanged outside this directory. Future generic improvements should be made here first and selectively ported back when they also benefit the team-oriented framework.

## Later Extension: Independent Record Assessment

On 19 October 2026 the user requested a portable auditor/worker split for VP
project records, informed by Medic and Pythia in NBS Framework revision
`1946cfba7770248915608bc5d16bcc5eda2b4415`. The role contract, fresh assessor
context and bounded evidence-based reporting were generalised into the
[record standard](standards/project-records.md) and
[audit playbook](playbooks/record-audit.md). The
[design record](docs/project-records-design.md) preserves sources and choices.

This extends VP's original role boundary without importing team runtime,
chat/bus tools, persistent monitoring, lifecycle management or oracular prose.
Separate sessions and Markdown directory handoff implement the contract.
