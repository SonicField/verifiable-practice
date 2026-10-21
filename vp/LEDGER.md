# Current Record Ledger

| Record | State | Origin / purpose |
|---|---|---|
| [D26](records/decisions/D-000026/record.md) | Open B migration decision/plan | Owner feedback; original D25/D1 at baseline |
| [R13](records/runs/R-000013/record.md) | Open labelled evidence batch | D26; actual restore, failures, classification and remaining checks |
| [A8](records/audits/A-000008/record.md) | Sealed nonconformant; F001 open | D26; B gate, A7 advisory closed |
| [V17](records/events/V-000017/record.md) | Response ready for fresh A9 | A8/F001; general minimum-form route correction |
| [V16](records/events/V-000016/record.md) | Sealed adoption summary/retirement | D26; full original history at baseline/replica |

Retired IDs resolve to `9605ad0:vp/records/<type>/<ID>/record.md` (audit request
at request.md). Baseline tag is records-archive-2026-10; successor owner
manifests give original evidence/manifest locators. Original maximum IDs are
D25/S3/H10/E12/R12/C6/V15/A7; never reuse them. D26/R13/V16 are allocated above;
S4 names this stage in D26. D27/A9 are reserved for acceptance/fresh re-audit.

A7/F001 is closed by A8; its old report/response remain baseline history.
A8/F001 is mandatory and open, response V17 awaits A9. Original inconclusive/failed/pass/withdrawn
verdicts remain in V16's sourced historical summary, not silently changed.
