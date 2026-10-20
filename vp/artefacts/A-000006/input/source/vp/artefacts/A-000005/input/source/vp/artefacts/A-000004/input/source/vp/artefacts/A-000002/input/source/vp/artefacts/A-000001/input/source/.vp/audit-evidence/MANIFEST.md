# Self-audit evidence manifest

Assessment completed: 2026-10-19T11:51:45.690378+00:00.

Producer/custodian: this Codex assessor session. Evidence is writable local capture, not independent historical action capture. Source files were copied without executing project scripts. No independent backup is asserted.

The complete input inventory, hashes, UTC capture time, HEAD and dirty status are in [snapshot.json](snapshot.json). `source/` contains those 70 original files. `results.json` retains each initial command, exit status, stdout and stderr; `final-checks.json` records post-assessment verification and concurrent live changes. `quick_validate.py` is a byte-identical copy of the validator used, retained for reproducibility; it requires PyYAML. Python and OS versions are in `results.json`.

Retain this bundle with its report for as long as the findings or verdict are relied on. No disposal was performed. `.vp/` is ignored by Git; local persistence does not imply commit/clone or independent recovery.

| File | Meaning | SHA-256 |
|------|---------|---------|
| [../audit-report.md](../audit-report.md) | Final standalone report | `4403ca0d5cfa1820d28f8381a54c06596d0d8edd88635880bf7181c50dc2b670` |
| [checks.py](checks.py) | Structural and bounded example checks | `0f737cc431aba7608863d6b6079fdab93c8c10677ad3efa5978579f9dec38bd2` |
| [snapshot.json](snapshot.json) | Complete source identities and capture provenance | `a3f37ccf62bc7173d9955dd6e9ef3f341fee942e57752b9af7f3e027775dde76` |
| [results.json](results.json) | Initial commands and all outcomes | `5f295b0fdd2e6564db14df1122b6b33726a9fa93fbd8288a6260cee55c31b7f1` |
| [final-checks.json](final-checks.json) | Post-assessment checks | `fd3b80749ff42839d6f23bb5dbfac1a657566c92c490bc2fc0ebce2747b30a4c` |
| [quick_validate.py](quick_validate.py) | Copied existing skill validator | `ee6dba90f44d37171c5a6edb8095979c54919ff6822c1a907afca2e78c48738c` |

This manifest does not include its own digest. Source-file identities are individually enumerated in snapshot.json. A matching digest establishes byte consistency, not authorship, accuracy or historical execution.
