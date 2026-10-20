"""Final open-R8 preservation member; refuse overwrites."""
from pathlib import Path
import json,hashlib,shutil,tempfile,sys
ns={};exec((Path(__file__).parent/'capture.py').read_text().split("if (HERE/'results.json')")[0],ns)
now,identity,deps,write=map(ns.get,['now','identity','deps','write']);root,here=ns['ROOT'],ns['HERE']
copy=Path('/home/alexturner/vp-preserved/verifiable-practice/R-000008-candidate-evidence');dest=here/'custody.json'
if copy.exists() or dest.exists():raise SystemExit('Refuse overwrite')
start=now();pre=identity('/usr/bin/python3');dpre=deps();inventory=json.loads((root/'vp/artefacts/C-000004/after/snapshot.json').read_text())
copy.mkdir(parents=True)
for item in inventory['files']:
 p=copy/item['path'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(root/item['path'],p)
shutil.copytree(root/'vp',copy/'vp')
files=[{'path':str(p.relative_to(copy)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(copy.rglob('*')) if p.is_file()]
write(here/'copy-inventory.json',{'captured':now(),'location':str(copy),'files':files})
restored=Path(tempfile.mkdtemp(prefix='vp-R8-restored-'))/'project';shutil.copytree(copy,restored)
def mismatch(base):return [e['path'] for e in files if not (base/e['path']).is_file() or hashlib.sha256((base/e['path']).read_bytes()).hexdigest()!=e['sha256']]
before=mismatch(restored);target=restored/files[0]['path'];original=target.read_bytes();target.write_bytes(original+b'\nPLANTED COPY DEFECT\n');control=mismatch(restored);target.write_bytes(original);after=mismatch(restored)
post=identity('/usr/bin/python3');dpost=deps();good=not before and control==[files[0]['path']] and not after and pre==post and dpre==dpost
write(here/'custody.dependencies-before.json',{'files':dpre});write(here/'custody.dependencies-after.json',{'files':dpost})
write(dest,{'started':start,'ended':now(),'argv':[sys.executable,__file__],'cwd':str(root),'instrument':identity(__file__),'operation':'shutil.copytree + exact same full-inventory SHA256 comparison before/planted/after restoration','copy':str(copy),'restore':str(restored),'inventory':'copy-inventory.json','inventory_identity':identity(here/'copy-inventory.json'),'files':len(files),'differences_before':before,'planted_differences':control,'differences_after':after,'executable_before':pre,'executable_after':post,'dependency_before':'custody.dependencies-before.json','dependency_after':'custody.dependencies-after.json','criterion_met':good,'limits':'same host, independently located pre-result bundle; does not contain future R8 seal/retention/audit or its own later custody output, not authenticated/off-host protection'})
print(json.dumps({'files':len(files),'criterion_met':good,'copy':str(copy)}));sys.exit(not good)
