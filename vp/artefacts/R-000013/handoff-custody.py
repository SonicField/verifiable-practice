"""Optional boundary instrument: actual full fixed-revision recovery outside worktree.

Protocol under D26/R13: capture fixed HEAD/tree; independently bundle and verify;
clone/checkout outside project, compare all Git paths/modes/bytes; preserve each
command result and mismatches. Never copy recovered source into the project.
Output directory must be new. Final external-only receipt can use --external.
"""
from pathlib import Path
import subprocess,hashlib,json,sys,stat
from datetime import datetime,timezone
root=Path('/home/alexturner/verifiable-practice')
store=Path('/home/alexturner/vp-preserved/verifiable-practice/review-20261021')
label=sys.argv[1];assert label.replace('-','').isalnum()
external='--external' in sys.argv[2:]
out=(store/label) if external else (root/'vp/artefacts/R-000013'/label)
out.mkdir(parents=True,exist_ok=False)
sha=lambda b:hashlib.sha256(b).hexdigest()
time=lambda:datetime.now(timezone.utc).isoformat()
started=time();commands=[]
def run(argv,cwd=root,retain=True):
 p=subprocess.run(argv,cwd=cwd,capture_output=True)
 entry={'argv':argv,'cwd':str(cwd),'time':time(),'exit':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':sha(p.stdout),'stderr':p.stderr.decode(errors='replace')}
 if retain:entry['stdout']=p.stdout.decode(errors='replace')
 commands.append(entry);assert p.returncode==0,entry;return p.stdout
git=lambda *args:run(['/usr/bin/git',*args]).decode().strip()
revision=git('rev-parse','HEAD');tree=git('rev-parse',revision+'^{tree}')
bundle=store/(label+'.bundle');restored=store/(label+'-restored');assert not bundle.exists() and not restored.exists()
git('bundle','create',str(bundle),'HEAD');git('bundle','verify',str(bundle))
run(['/usr/bin/git','clone','--quiet',str(bundle),str(restored)])
run(['/usr/bin/git','checkout','--quiet','--detach',revision],restored)
entries=run(['/usr/bin/git','ls-tree','-r','-z',revision],retain=False).split(b'\0')
inventory=[];mismatches=[]
for entry in entries:
 if not entry:continue
 metadata,path=entry.split(b'\t',1);mode,kind,oid=metadata.decode().split();name=path.decode();p=restored/name
 b=run(['/usr/bin/git','cat-file','blob',oid],retain=False)
 if mode=='120000':
  recovered=str(p.readlink()).encode();actual_mode='120000'
 else:
  recovered=p.read_bytes();actual_mode='100755' if p.stat().st_mode & stat.S_IXUSR else '100644'
 row={'path':name,'oid':oid,'mode':mode,'actual_mode':actual_mode,'bytes':len(b),'sha256':sha(b),'restored_sha256':sha(recovered)}
 inventory.append(row)
 if b!=recovered or mode!=actual_mode:mismatches.append(row)
assert git('rev-parse','HEAD')==revision
result={'started':started,'ended':time(),'revision':revision,'tree':tree,'instrument_sha256':sha(Path(__file__).read_bytes()),'runtime_sha256':sha(Path(sys.executable).read_bytes()),'git_sha256':sha(Path('/usr/bin/git').read_bytes()),'bundle':str(bundle),'bundle_sha256':sha(bundle.read_bytes()),'restored_directory':str(restored),'restored_files':len(inventory),'restored_bytes':sum(e['bytes'] for e in inventory),'mismatches':mismatches,'inventory':inventory,'commands':commands,'negative_control':'appending an in-memory byte differs from each recovered digest; no source-copy fixture', 'limits':'Actual full recovery from independently retained self-contained same-host bundle, not authenticated actions, whole-host loss protection or semantic/quality certification. Original source bytes remain Git/replica and external restored checkout only.'}
assert all(sha((restored/e['path']).read_bytes()+b'\0')!=e['sha256'] for e in inventory if e['mode']!='120000')
(out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['revision','bundle_sha256','restored_files','restored_bytes','mismatches']}))
assert not mismatches
