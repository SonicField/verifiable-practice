from pathlib import Path
import json,hashlib,datetime,sys
root=Path('/home/alexturner/verifiable-practice'); inp=root/'vp/artefacts/A-000006/input'; other=Path('/home/alexturner/vp-preserved/verifiable-practice/A-000006-input'); out=root/'vp/artefacts/A-000006/assessment'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inv=json.loads((inp/'inventory.json').read_text()); prep=json.loads((root/'vp/artefacts/A-000006/preparation.json').read_text()); expected={'MANIFEST.md','inventory.json'}|{r['path'] for r in inv['files']}; failures=[]
for base in (inp,other):
 actual={str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()}
 if actual!=expected: failures.append({'base':str(base),'missing':sorted(expected-actual),'extra':sorted(actual-expected)})
 for r in inv['files']:
  p=base/r['path']
  if not p.is_file() or p.stat().st_size!=r['bytes'] or sha(p)!=r['sha256']:failures.append({'base':str(base),'path':r['path'],'issue':'byte/digest mismatch'})
 for p,key in [('MANIFEST.md','manifest_sha256'),('inventory.json','inventory_sha256')]:
  if sha(base/p)!=prep[key]:failures.append({'base':str(base),'path':p,'issue':'preparation mismatch'})
fixed=[root/'vp/records/audits/A-000006/request.md',inp/'MANIFEST.md',inp/'inventory.json',root/'vp/artefacts/A-000006/preparation.json']
identities={str(p):sha(p) for p in fixed}
for p in [fixed[0],inp/'source/vp/records/audits/A-000006/request.md',other/'source/vp/records/audits/A-000006/request.md']:
 if sha(p)!=prep['request_sha256']:failures.append({'path':str(p),'issue':'request mismatch'})
if (out/'pre-verification.json').exists():
 before=json.loads((out/'pre-verification.json').read_text())
 if before['identities']!=identities:failures.append('fixed identities changed from initial verification')
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inventory_entries':len(inv['files']),'input_file_count_each':len(expected),'inventory_unique':len({r['path'] for r in inv['files']})==len(inv['files']),'checked_both_locations':True,'failures':failures,'identities':identities,'limits':'Read-only full file, byte-size, SHA-256 and exact path accounting. Same-host worker-controlled copies; no historical action authentication or technical execution.'}
(out/sys.argv[1]).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
