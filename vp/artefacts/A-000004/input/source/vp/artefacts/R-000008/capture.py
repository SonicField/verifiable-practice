"""One frozen candidate batch; optional evidence tooling, never required VP software."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,sys,sysconfig,shutil,subprocess,re,yaml
ROOT=Path('/home/alexturner/verifiable-practice');VP=ROOT/'vp';HERE=VP/'artefacts/R-000008';AFTER=VP/'artefacts/C-000004/after';BEFORE=VP/'artefacts/C-000004/before'
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(v if isinstance(v,str) else json.dumps(v,indent=2)+'\n')
def identity(p):
 p=Path(p);return {'path':str(p),'resolved':str(p.resolve()),'bytes':p.stat().st_size,'sha256':sha(p)}
def deps():
 entries=[]
 for owner,base in [('stdlib',Path(sysconfig.get_path('stdlib'))),('installed-yaml',Path(yaml.__file__).parent)]:
  for directory,dirs,names in os.walk(base):
   dirs[:]=[d for d in dirs if d not in ('site-packages','dist-packages','__pycache__','.git')]
   for name in sorted(names):
    p=Path(directory)/name
    if p.is_file() and (name.endswith(('.py','.so')) or '.so.' in name):entries.append({'owner':owner,**identity(p)})
 for line in Path('/proc/self/maps').read_text().splitlines():
  name=line.split()[-1]
  if name.startswith('/') and '.so' in name and Path(name).is_file() and not any(e['path']==name for e in entries):entries.append({'owner':'loaded-shared-library',**identity(name)})
 return sorted(entries,key=lambda e:(e['owner'],e['path']))
if (HERE/'results.json').exists() or AFTER.exists():raise SystemExit('Refuse overwrite; new R required')
started=now();members=[];py=Path('/usr/bin/python3');initial=identity(py);initialdeps=deps()
write(HERE/'dependencies-before.json',{'captured':now(),'files':initialdeps})
write(HERE/'runtime.json',{'captured':now(),'executable':initial,'version':sys.version,'yaml':yaml.__version__,'cwd':str(ROOT),'instrument':identity(__file__),'environment':{k:os.environ.get(k) for k in ('PYTHONPATH','LANG','LC_ALL','TZ')}})
def run(label,argv,expected,inputs):
 pre=identity(argv[0]);dpre=deps();ipre=[identity(p) for p in inputs];start=now()
 result=subprocess.run(list(map(str,argv)),cwd=ROOT,capture_output=True)
 end=now();write(HERE/(label+'.stdout.bin'),result.stdout.decode());write(HERE/(label+'.stderr.txt'),result.stderr.decode())
 post=identity(argv[0]);dpost=deps();ipost=[identity(p) for p in inputs]
 good=result.returncode==expected and pre==post and ipre==ipost and dpre==dpost==initialdeps and identity(py)==initial
 write(HERE/(label+'.dependencies-before.json'),{'files':dpre});write(HERE/(label+'.dependencies-after.json'),{'files':dpost})
 members.append({'label':label,'argv':list(map(str,argv)),'cwd':str(ROOT),'started':start,'ended':end,'exit':result.returncode,'expected_exit':expected,'executable_before':pre,'executable_after':post,'inputs_before':ipre,'inputs_after':ipost,'dependencies_before':label+'.dependencies-before.json','dependencies_after':label+'.dependencies-after.json','stdout':label+'.stdout.bin','stderr':label+'.stderr.txt','criterion_met':good})
 write(HERE/'progress.json',{'started':started,'members':members})
 if not good:raise RuntimeError('Required member failed: '+label)
 return result.stdout
head=run('head',['/usr/bin/git','rev-parse','HEAD'],0,[]).decode().strip()
run('status',['/usr/bin/git','status','--short'],0,[])
names=[e['path'] for e in json.loads((BEFORE/'snapshot.json').read_text())['files']]
entries=[];units=[];changes=[];orientation=[];blocks=[]
for name in names:
 p=ROOT/name;dest=AFTER/'source'/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest);digest=sha(p)
 entries.append({'path':name,'bytes':p.stat().st_size,'sha256':digest})
 old=sha(BEFORE/'source'/name)
 if old!=digest:changes.append({'path':name,'before_sha256':old,'after_sha256':digest})
 if name.endswith('.md'):
  text=p.read_text();lines=text.splitlines();active=None;headings=[]
  for i,line in enumerate(lines,1):
   m=re.match(r'^\s*(`{3,}|~{3,})(.*)$',line)
   if m:
    if active is None:active=m.group(1)
    elif m.group(1)[0]==active[0] and len(m.group(1))>=len(active) and not m.group(2).strip():active=None
   elif active is None and re.match(r'^#{1,6}\s',line):headings.append((i,re.sub(r'^#+\s*','',line).replace('|','/')))
  units.append({'path':name,'line':1,'unit':'file/preamble','sha256':digest})
  units.extend({'path':name,'line':i,'unit':h,'sha256':digest} for i,h in headings)
  orientation.append({'path':name,'opening':'\n'.join(lines[:16]),'headings':headings})
  for lang in ('python','c','cpp','bash','sh','javascript'):
   before=re.findall(r'```'+lang+r'\n(.*?)\n```',(BEFORE/'source'/name).read_text(),re.S);after=re.findall(r'```'+lang+r'\n(.*?)\n```',text,re.S)
   if before or after:blocks.append({'path':name,'language':lang,'blocks':len(after),'identical':before==after})
 else:units.append({'path':name,'line':1,'unit':'whole file','sha256':digest})
# Current record-view destinations for product navigation only. Raw fragments are owned evidence,
# not complete new adoption bundles; full independent packet supplies all dependencies later.
for p in VP.glob('*.md'):
 dest=AFTER/'source/vp'/p.name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
shutil.copytree(VP/'records',AFTER/'source/vp/records')
write(AFTER/'snapshot.json',{'captured':now(),'head':head,'files':entries,'scope':'71 maintained product files; additional copied vp views/records are navigation targets, raw source fragments retain original logical paths'})
write(HERE/'unit-inventory.json',{'captured':now(),'product_files':entries,'units':units})
write(HERE/'changed-paths.json',{'files':changes});write(HERE/'code-blocks.json',{'blocks':blocks,'criterion_met':all(b['identical'] for b in blocks),'limits':'Executable-language fenced examples; text and Mermaid diagrams intentionally updated'})
write(HERE/'orientation-inventory.json',{'files':orientation,'limits':'All public openings/headings; supplementary to manual semantic assessment'})
coverage='# Current Maintained Artefact Coverage\n\n**As of:** '+now()+'\n**Snapshot:** [C-000004 after](artefacts/C-000004/after/snapshot.json).\n**Authority:** D-000012/D-000013 under D-000001; pending completed R-000008 and retaining decision, no independent candidate verdict yet.\n**Validity:** current candidate checks provisional; retained background choices remain due 2026-10-26 UTC, earlier relevant dependency/authority/custody change.\n\n| Path / current unit | SHA-256 of exact containing file | Current retaining choice / evidence | Legacy / validity |\n|---|---|---|---|\n'
changed={e['path'] for e in changes}
for u in units:
 why='C-000004 / D-000013 selected communication rationale / H-000007 E-000008 R-000008 pending; requirement-to-source matrix and changed-file reasons' if u['path'] in changed else 'C-000001 / D-000004 file rationale / D-000007 retention; unchanged bytes; bounded example/structural rerun H-000007 E-000008 R-000008 pending'
 coverage+=f"| {u['path']}:{u['line']} — {u['unit']} | `{u['sha256']}` | {why} | original introduction unknown for unchanged legacy; current evidence/choices capped by 2026-10-26 UTC |\n"
coverage+='\n## Operational records and owned evidence\n\nAll current vp views/records are operational maintained units identified individually by the complete independent audit input inventory, with owner, meaning and producer metadata. No self-digest is asserted for this mutable view. Each record carries canonical origin, root and status; LEDGER indexes metadata. The D-000012/D-000013/C-000004/S-000002 chain governs new operational views and documentation evidence; earlier records retain their original mandates and scope. Artefact owner manifests bind every regular file; original nested source fragments/packets are owned historical data at original logical paths, not new record bundles. Full input inventory verifies exact bytes before/after assessment. Sealed historical evidence remains immutable. A-000003 is historical; candidate gate pending.\n'
write(VP/'COVERAGE.md',coverage);write(HERE/'coverage-complete.md',coverage)
unit=units[-1];label=f"{unit['path']}:{unit['line']} — {unit['unit']}";row=next(l for l in coverage.splitlines(keepends=True) if l.startswith('| '+label+' |'))
write(HERE/'coverage-omitted.md',coverage.replace(row,'',1));write(HERE/'coverage-wrong-digest.md',coverage.replace(row,row.replace(unit['sha256'],'0'*64),1))
control=HERE/'removed-identity-source'
for name in ['README.md','WHY.md','SKILL.md','docs/how-vp-works.md']:
 dest=control/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(AFTER/'source'/name,dest)
p=control/'README.md';p.write_text(p.read_text().replace('full project quality management system','project method',1))
source_inputs=[AFTER/'source'/n for n in names]
run('candidate-structural',[py,HERE/'checks.py','structural',AFTER/'source',AFTER/'snapshot.json'],0,[HERE/'checks.py',AFTER/'snapshot.json',*source_inputs])
run('candidate-behaviour',[py,HERE/'checks.py','behavior',AFTER/'source',AFTER/'snapshot.json'],0,[HERE/'checks.py',*source_inputs])
run('frontmatter',[py,HERE/'skill-validator.py',AFTER/'source'],0,[HERE/'skill-validator.py',AFTER/'source/SKILL.md'])
for label,base,expected in [('identity-candidate',AFTER/'source',0),('identity-baseline-negative',BEFORE/'source',1),('identity-removed-negative',control,1)]:
 run(label,[py,HERE/'identity_check.py',base],expected,[HERE/'identity_check.py',*[base/n for n in ['README.md','WHY.md','SKILL.md','docs/how-vp-works.md']]])
for label,filename,expected in [('coverage-complete','coverage-complete.md',0),('coverage-omitted','coverage-omitted.md',1),('coverage-wrong-digest','coverage-wrong-digest.md',1)]:
 run(label,[py,HERE/'coverage_check.py',HERE/'unit-inventory.json',HERE/filename,AFTER/'source'],expected,[HERE/'coverage_check.py',HERE/'unit-inventory.json',HERE/filename,*source_inputs])
run('diff-whitespace',['/usr/bin/git','diff','--check'],0,[ROOT/n for n in names])
write(HERE/'dependencies-after.json',{'captured':now(),'files':deps()})
stable=identity(py)==initial and deps()==initialdeps and all(sha(ROOT/e['path'])==e['sha256'] for e in entries)
write(HERE/'results.json',{'started':started,'ended':now(),'members':members,'files':len(entries),'markdown':len(orientation),'units':len(units),'changed_files':len(changes),'source_runtime_stable':stable,'code_blocks_identical':all(b['identical'] for b in blocks),'mechanical_criteria_met':stable and all(m['criterion_met'] for m in members) and all(b['identical'] for b in blocks),'manual_content_assessment':'semantic-matrix.md, separately authored after actual current text review','limits':'No population comprehension, general efficacy, independent product correctness, external authenticity or off-host durability claim'})
print(json.dumps({'files':len(entries),'units':len(units),'changed':len(changes),'stable':stable,'members':[(m['label'],m['criterion_met']) for m in members]}))
