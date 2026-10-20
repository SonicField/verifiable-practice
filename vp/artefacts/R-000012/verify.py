"""Bounded active-reference/Git recovery checks; no obsolete source copies."""
from pathlib import Path
import json,sys,re,hashlib,subprocess,argparse
parser=argparse.ArgumentParser();parser.add_argument('kind',choices=['absence','recovery']);parser.add_argument('root');parser.add_argument('inventory');parser.add_argument('--override-guide');args=parser.parse_args();root=Path(args.root);inv=json.loads(Path(args.inventory).read_text());errors=[]
if args.kind=='absence':
 pattern=re.compile(r'\bPTE\b|precise[ -]technical[ -]english|concepts/pte\.md|precise-technical-english\.md|nbs-pte',re.I)
 hits=[]
 for e in inv['files']:
  if not e['path'].endswith('.md'):continue
  p=Path(args.override_guide) if args.override_guide and e['path']=='docs/document-work.md' else root/e['path']
  for i,line in enumerate(p.read_text().splitlines(),1):
   if pattern.search(line):hits.append({'path':e['path'],'line':i,'text':line})
 errors.extend(hits)
 for name in ['concepts/pte.md','playbooks/precise-technical-english.md']:
  if (root/name).exists():errors.append('obsolete maintained file exists: '+name)
 result={'files':len(inv['files']),'hits':hits,'errors':errors,'scope':'all maintained product Markdown only; immutablehistoricalrecords/rawsnapshots/requiredremovalprovenance are not activeinstruction'}
else:
 before=json.loads((root/'vp/artefacts/C-000006/before.json').read_text());observations=[];git=Path('/usr/bin/git')
 for e in before['files']:
  if e['path'] not in ['concepts/pte.md','playbooks/precise-technical-english.md']:continue
  start_sha=hashlib.sha256(git.read_bytes()).hexdigest();argv=[str(git),'show',e['locator']];r=subprocess.run(argv,cwd=root,capture_output=True);end_sha=hashlib.sha256(git.read_bytes()).hexdigest();digest=hashlib.sha256(r.stdout).hexdigest();good=r.returncode==0 and digest==e['sha256'] and len(r.stdout)==e['bytes'] and start_sha==end_sha
  observations.append({'path':e['path'],'locator':e['locator'],'blob':e['git_blob'],'argv':argv,'exit':r.returncode,'executable_sha_before':start_sha,'executable_sha_after':end_sha,'raw_bytes_retained':'existing Gitblob, notduplicatedasarchivefile','bytes':len(r.stdout),'sha256':digest,'expected_sha256':e['sha256'],'stderr':r.stderr.decode(),'criterion_met':good})
  if not good:errors.append(e['path'])
 result={'observations':observations,'errors':errors,'scope':'exact deleted trackedbytes recoverable from fixedGitbaseline; no replicaobsolete source documents created'}
print(json.dumps(result,indent=2));sys.exit(bool(errors))
