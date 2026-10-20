"""Optional frozen-source capture for the owner-selected content assessment."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,shutil,sys
root=Path('/home/alexturner/verifiable-practice');here=root/'vp/artefacts/R-000007';before=root/'vp/artefacts/C-000004/before';started=datetime.now(timezone.utc).isoformat()
if (here/'results.json').exists():raise SystemExit('Refuse overwrite; new R for retry')
commands=[]
def command(name,args):
 start=datetime.now(timezone.utc).isoformat();r=subprocess.run(args,cwd=root,capture_output=True)
 (here/(name+'.stdout.bin')).write_bytes(r.stdout);(here/(name+'.stderr.txt')).write_bytes(r.stderr)
 commands.append({'label':name,'argv':args,'cwd':str(root),'started':start,'ended':datetime.now(timezone.utc).isoformat(),'exit':r.returncode,'stdout':name+'.stdout.bin','stderr':name+'.stderr.txt','executable_sha256':hashlib.sha256(Path('/usr/bin/git').read_bytes()).hexdigest()})
 r.check_returncode();return r.stdout
names=command('product-files',['/usr/bin/git','ls-files','--cached','--others','--exclude-standard','-z']).split(b'\0');head=command('head',['/usr/bin/git','rev-parse','HEAD']).decode().strip();command('status',['/usr/bin/git','status','--short']);entries=[];orientation=[]
for name in sorted(set(n.decode() for n in names if n)):
 if name.startswith(('vp/','.vp/')):continue
 p=root/name;data=p.read_bytes();dest=before/'source'/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
 entries.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 if name.endswith('.md'):
  text=data.decode();lines=text.splitlines();lead='\n'.join(lines[:16]);orientation.append({'path':name,'title':lines[0] if lines else '', 'opening':lead,'headings':[line for line in lines if line.startswith('#')], 'management_mentions':sum(text.lower().count(term) for term in ['quality management','project planning','stage','charter','record','audit'])})
(before/'snapshot.json').write_text(json.dumps({'captured':started,'head':head,'files':entries,'scope':'All current maintained product files; operational vp records separately governed'},indent=2)+'\n')
(here/'orientation-inventory.json').write_text(json.dumps({'scope':'Every public Markdown file opening/headings; supplementary physical orientation evidence, not full semantic verdict','files':orientation},indent=2)+'\n')
(here/'results.json').write_text(json.dumps({'started':started,'ended':datetime.now(timezone.utc).isoformat(),'commands':commands,'files':len(entries),'public_markdown_files':len(orientation),'python_executable':sys.executable,'python_resolved':str(Path(sys.executable).resolve()),'python_sha256':hashlib.sha256(Path(sys.executable).read_bytes()).hexdigest(),'capture_instrument_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'snapshot':'../../C-000004/before/snapshot.json','assessment':'Manual content report follows; inventories/counts are not semantic or reader-comprehension proof'},indent=2)+'\n')
print(json.dumps({'snapshot_files':len(entries),'public_markdown_files':len(orientation),'head':head,'before':str(before)}))
