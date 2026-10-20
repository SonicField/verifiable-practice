# Record Ledger

**As of:** 2026-10-19T12:17:06.303564+00:00
**Allocator:** worker /root; verifiable-practice namespace.

| ID | Recorded status | Origin (canonical links in original) | Dependencies/consumers |
|----|-----------------|--------------------------------------|------------------------|
| [A-000001](records/audits/A-000001/record.md) | sealed; verdict `inconclusive`; all eight findings open.   | immutable request and preserved [user commissioning excerpt][authority]; no project commissioning D supplied.   |  |
| [C-000001](records/changes/C-000001/record.md) | sealed; candidate retained for bounded research, independent stage gate pending | D-000002 | D-000001, D-000002, D-000004, D-000005, E-000001, H-000001, H-000002, R-000001, R-000002, R-000003 |
| [D-000001](records/decisions/D-000001/record.md) | sealed; selected choice recorded | Current owner mandate; this is the new root, not a reconstructed old root. | A-000001, C-000001, D-000002, S-000001 |
| [D-000002](records/decisions/D-000002/record.md) | sealed; selected choice recorded | D-000001 | A-000001, C-000001, D-000001, S-000001 |
| [D-000003](records/decisions/D-000003/record.md) | sealed; selected choice recorded | D-000002 | C-000001, D-000001, D-000002, E-000002, H-000002, R-000001 |
| [D-000004](records/decisions/D-000004/record.md) | sealed; bounded local research retention | D-000003 | A-000001, C-000001, D-000001, D-000003, H-000002, H-000003, R-000002, R-000003 |
| [D-000005](records/decisions/D-000005/record.md) | selected; sealed | D-000004 | A-000001, A-000002, D-000001, D-000004, R-000001, R-000002, R-000003, S-000001, V-000002 |
| [V-000001](records/events/V-000001/record.md) | sealed; legacy imported with custody limits | D-000001 | A-000001, D-000001, D-000004, R-000001, R-000003 |
| [V-000002](records/events/V-000002/record.md) | sealed response; ready for re-audit | D-000004 and preserved A-000001 | A-000001, A-000002, D-000001, D-000004, H-000003, R-000001, R-000003 |
| [V-000003](records/events/V-000003/record.md) | recorded; sealed | D-000004 | A-000002, D-000001, D-000004, H-000003, R-000002, R-000003 |
| [E-000001](records/experiments/E-000001/record.md) | sealed; completed with baseline falsification | D-000002 | A-000001, D-000001, D-000002, D-000003, H-000001, R-000001 |
| [E-000002](records/experiments/E-000002/record.md) | sealed; completed | D-000003 | D-000001, D-000003, D-000004, H-000002, R-000001, R-000002 |
| [E-000003](records/experiments/E-000003/record.md) | sealed completed | D-000004 | D-000001, D-000004, R-000002, R-000003 |
| [H-000001](records/hypotheses/H-000001/record.md) | sealed; falsified for starting inputs | D-000002 | D-000001, D-000002, E-000001, H-000002, R-000001 |
| [H-000002](records/hypotheses/H-000002/record.md) | sealed; failed to falsify for candidate inputs | D-000003 | D-000001, D-000003, E-000002, R-000002 |
| [H-000003](records/hypotheses/H-000003/record.md) | sealed; bounded structural checks failed to falsify; semantic A pending | D-000004 | D-000001, D-000004, E-000003, R-000002, R-000003 |
| [R-000001](records/runs/R-000001/record.md) | sealed completed; baseline falsified | E-000001 | D-000001, E-000001, H-000001 |
| [R-000002](records/runs/R-000002/record.md) | sealed completed; candidate failed to falsify bounded claim | E-000002 | C-000001, D-000001, E-000002, H-000002, R-000001 |
| [R-000003](records/runs/R-000003/record.md) | sealed completed; failed to falsify bounded structural/recovery claim | E-000003 | D-000001, E-000003, H-000003, R-000002 |
| [S-000001](records/stages/S-000001/record.md) | open | D-000002 | A-000001, C-000001, D-000001, D-000002, E-000001, H-000001, R-000001 |

| [A-000002 request](records/audits/A-000002/request.md) | allocated, packet/assessment pending | D-000005 | A-000001 findings / V-000002 / current packet |

A-000001 retains its original task-local namespace; V-000001 is its import locator. Current
records use present D-000001 root. Incoming reliance: H-000002/R-000002 -> D-000004;
H-000003/R-000003 -> current retention/audit; A-000001/F-001–008 -> V-000002 -> A-000002.
Historical missing captures do not become current evidence. Never close findings from this ledger alone.
