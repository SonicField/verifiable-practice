# Extraction Notes

This package was extracted from NBS Framework revision `a1084a3` on 2026-09-24.

## Included

The original “Why NBS” essay and the eight top-level concepts that concern human–AI software reasoning were retained. The generic playbooks were derived from the original review, audit, investigation, debugger, discovery, recovery, document-analysis, document-planning, document-description, and PTE command documents.

| Core material | Source material |
|---------------|-----------------|
| `WHY.md` | `docs/framework/Why-NBS.md` |
| `concepts/` | Directly under the source `concepts/`, except `coordination.md` |
| `playbooks/review.md` | `claude_tools/nbs.md` and `docs/framework/nbs-review.md` |
| `playbooks/code-audit.md` | `claude_tools/nbs-audit.md` and `docs/framework/nbs-audit.md` |
| `playbooks/investigation.md` | `claude_tools/nbs-investigation.md` |
| `playbooks/debugging.md` | `claude_tools/nbs-gdb.md` |
| Discovery and recovery playbooks | Corresponding `claude_tools/nbs-*.md` files |
| Document playbooks | `claude_tools/nbs-doc-*.md` |
| PTE playbook | `claude_tools/nbs-pte.md` |

## Deliberately Excluded

- `concepts/teams/` and the top-level coordination concept;
- supervisor, worker, gatekeeper, testkeeper, theologian, scribe, medic, librarian, and other team roles;
- chat, bus, polling, sidecar, hub, cursor, restart, and notification machinery;
- Claude Code frontmatter, slash-command installation, and `CLAUDE.md` integration;
- interactive help wrappers, mode-reset commands, and the optional Oracular Speech register;
- terminal-weathering, remote-development, manifest-maintenance, and other project-specific operations.

## Generalisation Choices

The extracted playbooks describe capabilities rather than product tool names. They do not assume slash commands, a particular home-directory layout, conversation APIs, or sub-agent support. Parallel work is optional and bounded. Audit and repair are explicitly separated so that a read-only request does not imply permission to edit code.

The source framework remains unchanged outside this directory. Future generic improvements should be made here first and selectively ported back when they also benefit the team-oriented framework.
