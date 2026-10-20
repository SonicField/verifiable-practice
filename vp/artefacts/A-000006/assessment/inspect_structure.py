from pathlib import Path
import re,json,hashlib,datetime
from urllib.parse import urlsplit,unquote
S=Path('/home/alexturner/verifiable-practice/vp/artefacts/A-000006/input/source');O=Path('/home/alexturner/verifiable-practice/vp/artefacts/A-000006/assessment');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inv=json.loads((S.parent/'inventory.json').read_text());products=[r['logical_path'] for r in inv['files'] if not r['logical_path'].startswith('vp/')];errors=[];details={}
def visible(text):
 lines=[];fence=None
 for n,line in enumerate(text.splitlines(),1):
  m=re.match(r'^\s*(`{3,}|~{3,})',line)
  if m:
   if fence is None:fence=m.group(1)[0]
   elif m.group(1)[0]==fence:fence=None
   continue
  if fence is None:lines.append((n,line))
 return lines
units=[]
for path in products:
 p=S/path
 if p.suffix=='.md':
  units.append(f'{path}:1 — file/preamble')
  for n,line in visible(p.read_text()):
   m=re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$',line)
   if m:units.append(f'{path}:{n} — {m.group(2)}')
 else:units.append(f'{path}:1 — whole file')
coverage=(S/'vp/COVERAGE.md').read_text();rows=[]
for line in coverage.splitlines():
 if line.startswith('| ') and re.search(r'`[0-9a-f]{64}`',line):
  cells=[x.strip() for x in line.strip('|').split('|')];unit=cells[0];digest=re.search(r'`([0-9a-f]{64})`',cells[1]).group(1);path=re.match(r'^(.*?):[0-9]+ — ',unit).group(1);rows.append(unit)
  if not (S/path).is_file() or sha(S/path)!=digest:errors.append('coverage digest '+unit)
if set(units)!=set(rows) or len(units)!=len(rows):errors.append({'coverage_unit_difference':{'missing':sorted(set(units)-set(rows)),'extra':sorted(set(rows)-set(units))}})
snap=json.loads((S/'vp/artefacts/C-000004/after/snapshot.json').read_text());before=json.loads((S/'vp/artefacts/C-000004/before/snapshot.json').read_text());changed=[];unchanged=[]
for r in snap['files']:
 if sha(S/r['path'])!=r['sha256'] or sha(S/'vp/artefacts/C-000004/after/source'/r['path'])!=r['sha256']:errors.append('C4after '+r['path'])
 b=next(x for x in before['files'] if x['path']==r['path'])
 if sha(S/'vp/artefacts/C-000004/before/source'/r['path'])!=b['sha256']:errors.append('C4before '+r['path'])
 (changed if b['sha256']!=r['sha256'] else unchanged).append(r['path'])
rationale=(S/'vp/artefacts/D-000004/coverage-rationale.md').read_text();missing_reasons=[p for p in unchanged if p not in rationale]
for p in unchanged:
 if sha(S/'vp/artefacts/C-000001/after/source'/p)!=sha(S/p):errors.append('unchanged C1 identity '+p)
records=sorted((S/'vp/records').glob('*/*/record.md'));requests=sorted((S/'vp/records').glob('*/*/request.md'));operational=[S/'vp'/f for f in ['README.md','PROJECT.md','PLAN.md','STATE.md','LEDGER.md','COVERAGE.md']]+[S/'vp/workspace/README.md']+records+requests
links=[];undefined=[]
for p in [S/f for f in products if f.endswith('.md')]+operational:
 txt='\n'.join(line for _,line in visible(p.read_text()));refs={a.lower():b for a,b in re.findall(r'^\[([^\]]+)\]:\s+(\S+)',txt,re.M)}
 for ref in re.findall(r'\[[^\]\n]+\]\[([^\]]+)\]',txt):
  if ref.lower() not in refs:undefined.append({'source':str(p.relative_to(S)),'reference':ref})
 dests=re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',txt)+list(refs.values())
 for dest in dests:
  dest=dest.strip().strip('<>');split=urlsplit(dest)
  if split.scheme or dest.startswith('//') or not split.path:continue
  target=(p.parent/unquote(split.path)).resolve();ok=target.exists();links.append({'source':str(p.relative_to(S)),'destination':dest,'resolved':str(target),'exists':ok})
ledger=(S/'vp/LEDGER.md').read_text();lrows=[]
for line in ledger.splitlines():
 if line.startswith('| ['):
  cells=[x.strip() for x in line.strip('|').split('|')];lrows.append(cells)
ids={re.search(r'\[([^\]]+)\]',r[0]).group(1).split('/')[0] for r in lrows};expected={p.parent.name for p in records+requests};fields=[];origins={}
for p in records+requests:
 text=p.read_text();fld={m.group(1):m.group(2).strip() for m in re.finditer(r'^\*\*([^*]+):\*\*\s*(.*)$',text,re.M)};fields.append({'path':str(p.relative_to(S)),'fields':fld})
 origin=fld.get('Origin',fld.get('Origin/commission',''));targets=re.findall(r'\[([^\]]+)\]',origin)
 origins[p.parent.name]=[x for x in targets if re.fullmatch(r'[DSECR]-\d{6}',x)]
cycles=[]
def visit(node,path):
 if node in path:cycles.append(path+[node]);return
 for prior in origins.get(node,[]):visit(prior,path+[node])
for node in origins:visit(node,[])
old=S/'vp/artefacts/A-000003/input/source/vp/records';sealed=[]
for p in old.glob('*/*/record.md'):
 if '**Sealed:** open' in p.read_text():continue
 current=S/'vp/records'/p.relative_to(old)
 if current.exists():sealed.append({'id':p.parent.name,'matches':sha(current)==sha(p)})
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'product_files':len(products),'independent_units':len(units),'coverage_rows':len(rows),'markdown_headings':len(units)-len(products),'changed_files':changed,'unchanged_files':unchanged,'missing_unchanged_reasons':missing_reasons,'record_count':len(records),'request_count':len(requests),'ledger_rows':len(lrows),'expected_ids':len(expected),'missing_ledger_ids':sorted(expected-ids),'extra_ledger_ids':sorted(ids-expected),'origin_graph':origins,'origin_cycles':cycles,'current_metadata':fields,'links_checked':len(links),'missing_links':[x for x in links if not x['exists']],'undefined_references':undefined,'preserved_prior_sealed_records':sealed,'errors':errors,'limits':'Full indexed product/current canonical views/records/requests. Explicit Markdown inline and reference-definition local file destinations outside fenced examples only; no heading anchor, external URL, browser rendering, shortcut reference or runtime testing. Origin-field graph is supplemented by manual semantic review for legacy/reference-field forms.'}
(O/'structural-checks.json').write_text(json.dumps(result,indent=2)+'\n');(O/'local-links.json').write_text(json.dumps(links,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['current_metadata','origin_graph','changed_files','unchanged_files','preserved_prior_sealed_records']},indent=2))
