"""Generate a navigable ledger from varied sealed record grammars; no source edits."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urlsplit
import re,os
root=Path('/home/alexturner/verifiable-practice');vp=root/'vp'
def metadata(t,keys):
 for key in keys:
  m=re.search(r'^\*\*'+re.escape(key)+r':\*\*\s*(.*)$',t,re.M)
  if m:return m.group(1).strip()
 raise ValueError('Missing '+repr(keys))
# Reference expansion already converts paths; do not convert expanded refs twice.
def routes(value,p,t):
 refs={m.group(1).lower():m.group(2) for m in re.finditer(r'^\[([^\]]+)\]:\s+(\S+)',t,re.M)}
 def dest(d):
  s=urlsplit(d)
  return d if s.scheme or d.startswith('//') or not s.path else os.path.relpath((p.parent/s.path).resolve(),vp)+('#'+s.fragment if s.fragment else '')
 value=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:'['+m.group(1)+']('+dest(m.group(2))+')',value)
 value=re.sub(r'\[([^\]]+)\]\[([^\]]+)\]',lambda m:'['+m.group(1)+']('+dest(refs[m.group(2).lower()])+')',value)
 return value.replace('|','&#124;')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
lines=['# Current Record Ledger','','**As of:** '+now,'**Allocator/owner:** working AI /root; root D-000001, latest accepted task D-000022/S-000003 under D-000025.','**Status:** S3 accepted D25; A7 conformant for its fixed candidate; V14 custody handoff; A7/F001 corrected current labels under V15 but advisory not independently closed; old A6 scope historical, A5 withdrawn V10.','**Navigation:** links are rebased from original record locations to this view. Source grammars and historical unknowns remain intact. Created and sealed is original creation metadata where the sealed report records both together; request rows have their own issued timestamps.','','| ID / record | Type | Created UTC | Title | Current state | Canonical origin / goal source |','|---|---|---|---|---|---|']
for p in sorted((vp/'records').glob('*/*/*.md')):
 if p.name!='record.md' and not (p.name=='request.md' and not (p.parent/'record.md').exists()):continue
 t=p.read_text();id=p.parent.name+('/request' if p.name=='request.md' else '')
 typ=metadata(t,['Type','Type / kind','Type / audit kind']) if '**Type' in t else 'audit request'
 created=metadata(t,['Created','Created and sealed'])
 status=metadata(t,['Status'])
 if id=='A-000005/request':status+='; withdrawn before dispatch [V-000010](records/events/V-000010/record.md), no report/verdict'
 try:origin=metadata(t,['Origin','Origin/commission','Commission'])
 except ValueError:origin='Issued audit request; see exact scope and commissioning source in [request]('+str(p.relative_to(vp))+')'
 try:goal=metadata(t,['Goal served'])
 except ValueError:goal='See original immutable request goal/authority; no metadata inferred'
 cells=[f'[{id}]({p.relative_to(vp)})',typ,created,t.splitlines()[0].lstrip('# '),status,routes(origin,p,t)+' / '+routes(goal,p,t)]
 lines.append('| '+' | '.join(c.replace('|','&#124;') for c in cells)+' |')
lines+=['','Original negative verdicts/controls remain sealed. A-000003 historical acceptance does not cover current changed source. A-000004 remains originalfailedfreeze; A6independentlycloseditsnewscope, A5withdrawnnoassessment. S3 accepted D25 after A7 exact-scope conformance; A7/F001 bounded V15 disposition awaits independent closure, original reports not rewritten. Effective current evidence review by26OctUTC and earlier dependencies/authority/custody changes; root17Jan2027. Original A1 missing commissioned root remains stated in its original report; later prospective adoption does not reconstruct it.']
(vp/'LEDGER.md').write_text('\n'.join(lines)+'\n')
print(len(lines)-12)
