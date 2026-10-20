"""One bounded removal verification batch; old source remains in Git."""
from pathlib import Path
import json,hashlib,subprocess,re
here=Path(__file__).parent;helper=here.parent/'R-000008/capture.py';ns={};exec(helper.read_text().split("if (HERE/'results.json')")[0],ns)
if (here/'results.json').exists():raise SystemExit('Refuse overwrite; new R required')
ns.update({'HERE':here,'started':ns['now'](),'members':[],'py':Path('/usr/bin/python3')});ns['initial']=ns['identity'](ns['py']);ns['initialdeps']=ns['deps']();src=helper.read_text();exec(src[src.index('def run(label'):src.index('head=run(')],ns)
root=ns['ROOT'];vp=ns['VP'];sha=ns['sha'];write=ns['write'];run=ns['run'];identity=ns['identity'];py=ns['py'];before=json.loads((vp/'artefacts/C-000006/before.json').read_text());base=before['head'];baseline=[e for e in before['files'] if not e['path'].startswith('vp/')];names=[e['path'] for e in baseline if (root/e['path']).exists()];entries=[];units=[];changes=[]
for e in baseline:
 name=e['path'];p=root/name
 if not p.exists():changes.append({'path':name,'action':'deleted','before_sha256':e['sha256'],'after_sha256':None,'before_locator':e['locator']});continue
 digest=sha(p);entries.append({'path':name,'bytes':p.stat().st_size,'sha256':digest})
 if digest!=e['sha256']:changes.append({'path':name,'action':'modified','before_sha256':e['sha256'],'after_sha256':digest,'before_locator':e['locator']})
 if name.endswith('.md'):
  active=None;units.append({'path':name,'line':1,'unit':'file/preamble','sha256':digest})
  for i,line in enumerate(p.read_text().splitlines(),1):
   m=re.match(r'^\s*(`{3,}|~{3,})(.*)$',line)
   if m:
    if active is None:active=m.group(1)
    elif m.group(1)[0]==active[0] and len(m.group(1))>=len(active) and not m.group(2).strip():active=None
   elif active is None and re.match(r'^#{1,6}\s',line):units.append({'path':name,'line':i,'unit':re.sub(r'^#+\s*','',line).replace('|','/'),'sha256':digest})
 else:units.append({'path':name,'line':1,'unit':'whole file','sha256':digest})
write(here/'source-inventory.json',{'captured':ns['now'](),'base':base,'files':entries,'removed':[e['path'] for e in changes if e['action']=='deleted'],'changes':changes,'meaning':'exactcurrentproduct; baselineGitlocators+completepatchprovidebeforebytes/noarchives'})
write(here/'unit-inventory.json',{'product_files':entries,'units':units})
write(here/'dependencies-before.json',{'files':ns['initialdeps']});write(here/'runtime.json',{'executable':ns['initial'],'version':ns['sys'].version,'dependencies':'dependencies-before.json','instrument':identity(__file__),'helper':identity(helper)})
inputs=[root/n for n in names];inventory=here/'source-inventory.json'
run('complete-product-patch',['/usr/bin/git','diff','--binary',base,'--',*[e['path'] for e in baseline]],0,[*inputs]);patch=(here/'complete-product-patch.stdout.bin').read_bytes();(vp/'artefacts/C-000006/change.patch').write_bytes(patch)
run('view-patch',['/usr/bin/git','diff','--binary',base,'--','vp/README.md','vp/PROJECT.md','vp/PLAN.md','vp/STATE.md','vp/LEDGER.md','vp/COVERAGE.md'],0,[])
# Single-file defect inputs are verification evidence, not obsolete-document archives.
write(here/'planted-obsolete-guide.md',(root/'docs/document-work.md').read_text()+'\nUse PTE through concepts/pte.md.\n')
write(here/'planted-broken-skill.md',(root/'SKILL.md').read_text()+'\nSee [missing route](docs/nonexistent-clarity-route.md).\n')
for label,argv,expected,extra in [
 ('active-reference-absence',[py,here/'verify.py','absence',root,inventory],0,[]),
 ('obsolete-reference-control',[py,here/'verify.py','absence',root,inventory,'--override-guide',here/'planted-obsolete-guide.md'],1,[here/'planted-obsolete-guide.md']),
 ('all-product-structure',[py,here/'structure.py',root,inventory],0,[]),
 ('broken-route-control',[py,here/'structure.py',root,inventory,'--override-skill',here/'planted-broken-skill.md'],1,[here/'planted-broken-skill.md']),
 ('skill-frontmatter',[py,here/'skill-validator.py',root],0,[]),
 ('deleted-Git-recovery',[py,here/'verify.py','recovery',root,inventory],0,[vp/'artefacts/C-000006/before.json'])]:
 run(label,argv,expected,[argv[1],inventory,*inputs,*extra])
run('current-diff-whitespace',['/usr/bin/git','diff','--check'],0,[*inputs])
stable=all(sha(root/e['path'])==e['sha256'] for e in entries) and ns['deps']()==ns['initialdeps'] and identity(py)==ns['initial'];write(here/'dependencies-after.json',{'files':ns['deps']()})
write(here/'results.json',{'started':ns['started'],'ended':ns['now'](),'members':ns['members'],'files':len(entries),'markdown_files':sum(e['path'].endswith('.md') for e in entries),'units':len(units),'removed':len([e for e in changes if e['action']=='deleted']),'modified':len([e for e in changes if e['action']=='modified']),'source_runtime_stable':stable,'criterion_met':stable and all(m['criterion_met'] for m in ns['members']),'manual_content_evidence':'semantic-analysis.md, separate directsource review, notkeywordproof','limits':'workercontrolledsource-onlychecks, no build/AIpopulation/usefulnesscomparativeclaim; independent stagegatepending'})
print(json.dumps({'files':len(entries),'units':len(units),'changes':changes,'members':[(m['label'],m['criterion_met']) for m in ns['members']],'stable':stable}))
