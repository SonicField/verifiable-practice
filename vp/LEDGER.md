# Current Record Ledger

| Record | State | Origin / purpose |
|---|---|---|
| [D26](records/decisions/D-000026/record.md) | Accepted via D27; final seal pending | Owner feedback; original D25/D1 at baseline |
| [R13](records/runs/R-000013/record.md) | Open labelled evidence batch | D26; actual restore, failures, classification and remaining checks |
| [A8](records/audits/A-000008/record.md) | Original nonconformant; F001 closed by A10 | D26; B gate, A7 advisory closed |
| [A9](records/audits/A-000009/record.md) | Original nonconformant; F001 closed by A10 | D26; V17 closure failed |
| [A10](records/audits/A-000010/record.md) | Conformant at20bb26b, prior gaps closed | D26/V18; fixed scope only |
| [D27](records/decisions/D-000027/record.md) | Separate accepted B transition; handoff open | D26/R13/A10, existing owner delegation |
| [V18](records/events/V-000018/record.md) | Sealed response; A10 independently closes findings | A9/F001; correct search claim/general downstream prescriptions |
| [V17](records/events/V-000017/record.md) | Sealed first response; A9 closure failed | A8/F001; general minimum-form route correction |
| [V16](records/events/V-000016/record.md) | Sealed adoption summary/retirement | D26; full original history at baseline/replica |

Retired IDs resolve to `9605ad0:vp/records/<type>/<ID>/record.md` (audit request
at request.md). Baseline tag is records-archive-2026-10; successor owner
manifests give original evidence/manifest locators. Original maximum IDs are
D25/S3/H10/E12/R12/C6/V15/A7; never reuse them. D26/R13/V16 are allocated above;
S4 names this stage in D26. D27/A10 are now allocated; next unused D28/V19/R14/A11.

A7/F001 is closed by A8; its old report/response remain baseline history.
A8/F001 and residual A9/F001 are independently closed by A10. Original inconclusive/failed/pass/withdrawn
verdicts remain in V16's sourced historical summary, not silently changed.
