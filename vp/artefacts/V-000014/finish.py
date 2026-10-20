"""Identify the containing receipt and preserve a compact complete Git bundle."""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib
root=Path('/home/alexturner/verifiable-practice');ext=Path('/home/alexturner/vp-preserved/verifiable-practice/PTE-removal-20261020');bundle=ext/'completion.bundle';assert not bundle.exists() and not (ext/'completion.json').exists();commands=[];sha=lambda b:hashlib.sha256(b).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def cmd(label,args,stdin=None):
 start=now();before=sha(Path(args[0]).read_bytes());r=subprocess.run(args,cwd=root,input=stdin,capture_output=True);commands.append({'label':label,'argv':args,'cwd':str(root),'started':start,'ended':now(),'exit':r.returncode,'exe_sha_before':before,'exe_sha_after':sha(Path(args[0]).read_bytes()),'stdout_sha256':sha(r.stdout),'stdout_bytes':len(r.stdout),'stderr':r.stderr.decode()});(ext/'completion-progress.json').write_text(json.dumps(commands,indent=2)+'\n');r.check_returncode();assert before==sha(Path(args[0]).read_bytes());return r.stdout
commit=cmd('receipt-tip',['/usr/bin/git','rev-parse','HEAD']).decode().strip();tree=cmd('receipt-tree',['/usr/bin/git','rev-parse','HEAD^{tree}']).decode().strip();assert not cmd('clean-status',['/usr/bin/git','status','--porcelain'])
listing=cmd('fixed-index',['/usr/bin/git','ls-tree','-r','-z',commit]);entries=[]
for item in listing.split(b'\0'):
 if item:
  meta,path=item.split(b'\t');mode,typ,oid=meta.decode().split();assert typ=='blob';entries.append({'path':path.decode(),'mode':mode,'object':oid})
objects=sorted({e['object'] for e in entries});out=cmd('all-blob-identities',['/usr/bin/git','cat-file','--batch'], ('\n'.join(objects)+'\n').encode());offset=0;ids={}
for oid in objects:
 end=out.index(b'\n',offset);actual,typ,size=out[offset:end].decode().split();size=int(size);assert actual==oid and typ=='blob';data=out[end+1:end+1+size];offset=end+size+2;ids[oid]={'bytes':size,'sha256':sha(data)}
for e in entries:e.update(ids[e['object']]);e['locator']=commit+':'+e['path']
assert len([e for e in entries if not e['path'].startswith('vp/')])==69
(ext/'completion-inventory.json').write_text(json.dumps({'git_commit':commit,'git_tree':tree,'files':entries,'scope':'complete tracked current 69-file product and owned vp record root, including original failed/audit evidence; Git history retains deleted documents'},indent=2)+'\n')
cmd('bundle-create',['/usr/bin/git','bundle','create',str(bundle),'HEAD']);cmd('bundle-verify',['/usr/bin/git','bundle','verify',str(bundle)]);heads=cmd('bundle-tips',['/usr/bin/git','bundle','list-heads',str(bundle)]).decode();assert commit in heads;assert cmd('tip-after',['/usr/bin/git','rev-parse','HEAD']).decode().strip()==commit;assert not cmd('clean-status-after',['/usr/bin/git','status','--porcelain'])
result={'completed':now(),'containing_receipt_commit':commit,'tree':tree,'files':len(entries),'product_files':69,'bundle':str(bundle),'bundle_bytes':bundle.stat().st_size,'bundle_sha256':sha(bundle.read_bytes()),'inventory_sha256':sha((ext/'completion-inventory.json').read_bytes()),'instrument_sha256':sha(Path(__file__).read_bytes()),'commands':commands,'git_clean':True,'limits':'verified self-contained Git bundle and full fixed blob index; no performed checkout restore or off-host protection/authentication claim; no duplicated obsolete source tree'}
(ext/'completion.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# Semantic removal completed custody','','Owner: V14/D25/root D1; producer worker /root. Consumer: owner handoff, later independent review and recovery. Created after containing receipt commit; metadata is outside that commit to avoid claiming its own future identity.','','Containing receipt: `'+commit+'`, tree `'+tree+'`. Complete 69-file maintained product and owned vp history indexed in completion-inventory.json. Local status was clean before and after bundle creation. A7 remains conformant only at its original candidate freeze; the completion bundle adds later authorised receipt projections, not a wider audit verdict.','','Recovery: restore completion.bundle into a separate Git object store and read the fixed commit/path; compare every indexed blob/byte/SHA256. Actual bundle verify and advertised tip checks are captured, not a performed checkout restoration claim. Deleted obsolete documents are available through baseline Git ancestors, not new source archive directories.','','| Path | Bytes | SHA256 | Meaning |','|---|---:|---|---|']
for p in sorted(ext.rglob('*')):
 if p.is_file() and p.name!='MANIFEST.md':lines.append(f'| {p.relative_to(ext)} | {p.stat().st_size} | `{sha(p.read_bytes())}` | Owned audit/custody bundle, index or actual command capture; see designated packet and V14 locators. |')
lines+=['','Retain project life plus 365 days after recorded retirement, no disposal authorised. Current evidence review remains 2026-10-26 23:59:59 UTC or earlier relevant trigger; root review 2027-01-17 UTC. Same-host worker-controlled custody detects byte mismatch and directory loss, not whole-host loss or historical authorship. This manifest is not self-hashed. No remote push occurred.']
(ext/'MANIFEST.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'containing_receipt':commit,'files':len(entries),'bundle_bytes':bundle.stat().st_size,'git_clean':True}))
