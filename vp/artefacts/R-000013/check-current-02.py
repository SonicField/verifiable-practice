"""Optional structure/custody checks; in-memory negative inputs avoid source copies."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlsplit,unquote
import re,json,hashlib,subprocess,sys
import yaml
root=Path('/home/alexturner/verifiable-practice');a=root/'vp/artefacts/R-000013';attempt=sys.argv[1];dest=a/attempt;assert not dest.exists();dest.mkdir();started=datetime.now(timezone.utc).isoformat();sha=lambda b:hashlib.sha256(b).hexdigest()
baseline='9605ad0dccea157880a05208babfdac5aa5a5fcd';paths=[p.decode() for p in subprocess.check_output(['/usr/bin/git','ls-tree','-r','--name-only','-z',baseline],cwd=root).split(b'\0') if p and not p.startswith(b'vp/')]
def unfenced(text):
 lines=[];fence=None
 for line in text.splitlines():
  m=re.match(r'^\s*(`{3,}|~{3,})',line)
  if m:
   marker=m.group(1)
   if fence is None:fence=marker[0]
   elif marker[0]==fence:fence=None
   lines.append('')
  else:lines.append('' if fence else line)
 return '\n'.join(lines),fence
links=[]
def linkcheck(p,text):
 visible,fence=unfenced(text);errors=[]
 if fence:errors.append(str(p)+':unclosed fence')
 refs={m.group(1).lower():m.group(2).strip('<>') for m in re.finditer(r'^\[([^\]]+)\]:\s*(\S+)',visible,re.M)}
 destinations=[m.group(2).strip('<>') for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',visible)]+list(refs.values())
 for m in re.finditer(r'\[([^\]]+)\]\[([^\]]+)\]',visible):
  if m.group(2).lower() not in refs:errors.append(str(p)+':undefined '+m.group(2))
 for d in destinations:
  u=urlsplit(d)
  if u.scheme or d.startswith('//') or '<' in d or '>' in d:continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  links.append({'source':str(p.relative_to(root)),'destination':d})
  if not target.exists():errors.append(str(p)+':missing '+d)
 return errors
errors=[];inventory=[]
for name in paths:
 p=root/name;data=p.read_bytes();inventory.append({'path':name,'bytes':len(data),'sha256':sha(data)})
 if p.suffix=='.md':errors+=linkcheck(p,data.decode())
# Current views/records/manifests use immutable Git locators for retired files.
for p in sorted((root/'vp').rglob('*.md')):errors+=linkcheck(p,p.read_text())
md=(root/'SKILL.md').read_text();front=re.match(r'^---\n(.*?)\n---\n',md,re.S);assert front;fields=yaml.safe_load(front.group(1));assert fields['name']=='verifiable-practice' and isinstance(fields['description'],str) and fields['description']
negative_link=linkcheck(root/'README.md','[planted](does-not-exist-for-negative-control.md)');assert negative_link
negative_fence=linkcheck(root/'README.md','```python\nunclosed');assert negative_fence
coverage=(root/'vp/COVERAGE.md').read_text()
for e in inventory:
 if e['path'] not in coverage or e['sha256'] not in coverage:errors.append('coverage identity:'+e['path'])
# Scan all actual worktree files, including ignored content; .git is revision storage.
worktree=[p for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts];hashes={}
for p in worktree:hashes.setdefault(sha(p.read_bytes()),[]).append(str(p.relative_to(root)))
product_duplicates={e['path']:hashes[e['sha256']] for e in inventory if len(hashes[e['sha256']])>1};skills=[str(p.relative_to(root)) for p in worktree if p.name=='SKILL.md'];pte=[str(p.relative_to(root)) for p in worktree if p.name=='pte.md'];assert skills==['SKILL.md'] and not pte and not product_duplicates
active_patterns=[]
for name in paths:
 text=(root/name).read_text(errors='replace')
 if re.search(r'\bPTE\b|concepts/pte\.md|precise-technical-english\.md',text):active_patterns.append(name)
# A minimal actual check stored inline in one D replay entry, with no D/H/E/R/A expansion.
replay={'level':'D','records_required':['one change record with inline check'],'independent_audit_required':False,'calendar_expiry_required':False,'binding_controls_unchanged':True,'verified_reversal':'R13 restore-01 complete baseline','limits':'historical planning/check replay; no new retirement, reader efficacy or universal usefulness experiment'}
(dest/'pte-retirement-replay.md').write_text('# D replay: retire an optional wording technique\n\nLevel D: binding requirements/authority/gates remain, substantive clarity checks are retained, no consequential deployed consumer is identified, and baseline source restore is verified. Owner mandate/root locator: D22/D1 at9605ad0. One change record with inline semantic/dependency/active-reference check; no separate D/H/E/R/A and no calendar expiry. Actual current check: no active PTE name/path reference across all '+str(len(paths))+' product files; ordinary-English requirement controls remain in Document Work and standard1.1. Historical R12 semantic responsibility map and before/after bytes resolve at baseline. This is a replay of planning/check requirements, not a newly executed removal or original-timing claim. Outcome: '+('pass' if not active_patterns else 'fail '+str(active_patterns))+'. Rollback uses the actually restored baseline Git paths.\n')
if active_patterns:errors+=['active references:'+str(active_patterns)]
result={'started':started,'ended':datetime.now(timezone.utc).isoformat(),'instrument_sha256':sha(Path(__file__).read_bytes()),'runtime_sha256':sha(Path(sys.executable).read_bytes()),'product_inventory':inventory,'product_files':len(paths),'markdown_files':sum(Path(p).suffix=='.md' for p in paths),'links_checked':len(links),'errors':errors,'SKILL_paths':skills,'pte_paths':pte,'product_duplicate_bytes':product_duplicates,'worktree_files':len(worktree),'worktree_bytes':sum(p.stat().st_size for p in worktree),'negative_link_detected':negative_link,'negative_fence_detected':negative_fence,'D_replay':replay,'limits':'explicit local file/reference/fence/frontmatter and identities; external URL/renderer correctness and broad semantics require separate scope; no source-copy test inputs'}
(dest/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['product_files','links_checked','errors','SKILL_paths','pte_paths','product_duplicate_bytes','worktree_files','worktree_bytes']}));assert not errors
