"""Actually restore a fixed baseline from a separately located self-contained Git bundle."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,stat
root=Path('/home/alexturner/verifiable-practice');a=root/'vp/artefacts/R-000013/restore-01';assert not a.exists();a.mkdir();ext=Path('/home/alexturner/vp-preserved/verifiable-practice/review-20261021');ext.mkdir(exist_ok=False);bundle=ext/'baseline.bundle';restore=ext/'restored-baseline';commit='9605ad0dccea157880a05208babfdac5aa5a5fcd';tag='records-archive-2026-10';commands=[];sha=lambda b:hashlib.sha256(b).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def cmd(label,args,cwd=root,stdin=None):
 start=now();before=sha(Path(args[0]).read_bytes());r=subprocess.run(args,cwd=cwd,input=stdin,capture_output=True);out=a/(label+'.stdout.bin');err=a/(label+'.stderr.bin');out.write_bytes(r.stdout);err.write_bytes(r.stderr);commands.append({'label':label,'argv':args,'cwd':str(cwd),'started':start,'ended':now(),'exit':r.returncode,'exe_sha_before':before,'exe_sha_after':sha(Path(args[0]).read_bytes()),'stdout':str(out.relative_to(root)),'stdout_sha256':sha(r.stdout),'stderr':str(err.relative_to(root)),'stderr_sha256':sha(r.stderr)});(a/'commands.json').write_text(json.dumps(commands,indent=2)+'\n');r.check_returncode();assert before==sha(Path(args[0]).read_bytes());return r.stdout
assert cmd('baseline-head',['/usr/bin/git','rev-parse','HEAD']).decode().strip()==commit
cmd('tag',['/usr/bin/git','tag',tag,commit]);cmd('bundle',['/usr/bin/git','bundle','create',str(bundle),tag]);cmd('bundle-verify',['/usr/bin/git','bundle','verify',str(bundle)]);cmd('clone',['/usr/bin/git','clone','--no-checkout',str(bundle),str(restore)]);cmd('checkout',['/usr/bin/git','checkout','--detach',commit],restore)
listing=cmd('baseline-index',['/usr/bin/git','ls-tree','-r','-z',commit]);entries=[]
for item in listing.split(b'\0'):
 if item:
  meta,path=item.split(b'\t',1);mode,typ,oid=meta.decode().split();assert typ=='blob';entries.append({'path':path.decode(),'mode':mode,'object':oid})
assert cmd('restored-index',['/usr/bin/git','ls-tree','-r','-z',commit],restore)==listing
objects=sorted({e['object'] for e in entries});out=cmd('baseline-blobs',['/usr/bin/git','cat-file','--batch'],root,('\n'.join(objects)+'\n').encode());offset=0;ids={}
for oid in objects:
 end=out.index(b'\n',offset);actual,typ,size=out[offset:end].decode().split();size=int(size);assert actual==oid and typ=='blob';data=out[end+1:end+1+size];offset=end+size+2;ids[oid]={'bytes':size,'sha256':sha(data)}
errors=[]
for e in entries:
 e.update(ids[e['object']]);p=restore/e['path'];data=p.read_bytes();e['restored_sha256']=sha(data)
 if e['sha256']!=e['restored_sha256'] or len(data)!=e['bytes']:errors.append(e['path'])
 if bool(p.stat().st_mode&stat.S_IXUSR)!=(e['mode']=='100755'):errors.append(e['path']+':mode')
assert not cmd('restored-status',['/usr/bin/git','status','--porcelain'],restore)
negative=entries[0];assert sha((restore/negative['path']).read_bytes()+b'PLANTED MISMATCH')!=negative['sha256']
result={'started':commands[0]['started'],'ended':now(),'baseline':commit,'tag':tag,'bundle':str(bundle),'bundle_bytes':bundle.stat().st_size,'bundle_sha256':sha(bundle.read_bytes()),'restored_directory':str(restore),'files':entries,'file_count':len(entries),'total_bytes':sum(e['bytes'] for e in entries),'mismatches':errors,'negative_control':'appended in-memory byte change differs from baseline digest','performed_restore':True,'limits':'actual Git checkout from independent-directory bundle; same host, not off-host or authenticated action custody','instrument_sha256':sha(Path(__file__).read_bytes())}
(a/'results.json').write_text(json.dumps(result,indent=2)+'\n');(ext/'baseline-inventory.json').write_text(json.dumps({'baseline':commit,'tag':tag,'files':entries},indent=2)+'\n');(ext/'MANIFEST.md').write_text('# Baseline custody before pruning\n\nOwner D26/R13. Fixed tag '+tag+' / '+commit+'. baseline.bundle SHA256 '+result['bundle_sha256']+'; complete baseline-inventory.json SHA256 '+sha((ext/'baseline-inventory.json').read_bytes())+'. Actual restored checkout compared every '+str(len(entries))+' path, mode and byte; mismatches '+str(len(errors))+'. Raw attempt output remains in R13/restore-01, retained in the later current Git record. Same-host independently located replica, no host-loss/authenticity claim. Retain life plus 365 days; do not prune Git objects or this baseline bundle.\n')
print(json.dumps({'files':len(entries),'bytes':result['total_bytes'],'mismatches':errors,'performed_restore':True,'bundle':str(bundle)}));assert not errors
