"""Read-only ledger contract checker, separately from generator."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,json,sys
ledger=Path(sys.argv[1]);vp=Path(sys.argv[2]);text=ledger.read_text();errors=[]
rows=[]
for line in text.splitlines():
 if line.startswith('| ['):
  cells=[c.strip() for c in line.strip('|').split('|')]
  if len(cells)!=6:errors.append('column count '+line);continue
  rows.append(cells)
  if not cells[1] or any(s in cells[1].lower() for s in ('not extracted','unavailable','placeholder')):errors.append('unsupported type '+cells[0])
  if not re.search(r'\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}',cells[2]):errors.append('unsupported UTC date '+cells[0])
  if not cells[3] or not cells[4] or not cells[5]:errors.append('empty required metadata '+cells[0])
ids={re.search(r'\[([^\]]+)\]',c[0]).group(1).split('/')[0] for c in rows}
expected={p.parent.name for p in (vp/'records').glob('*/*/record.md')}
expected|={p.parent.name for p in (vp/'records').glob('*/*/request.md') if not (p.parent/'record.md').exists()}
if expected-ids:errors.append('missing IDs '+repr(sorted(expected-ids)))
# Independently read original report source field alternatives for specific regression scope.
for id in ['A-000001','A-000002','A-000003','A-000004']:
 p=vp/'records/audits'/id/'record.md'
 if not p.exists():continue
 original=p.read_text();row=next((r for r in rows if '['+id+']' in r[0]),None)
 typ=re.search(r'^\*\*Type(?: / (?:kind|audit kind))?:\*\*\s*(.*)$',original,re.M)
 date=re.search(r'^\*\*Created(?: and sealed)?:\*\*\s*(.*)$',original,re.M)
 if not row or not typ or not date or row[1]!=typ.group(1).strip() or row[2]!=date.group(1).strip():errors.append('original audit metadata mismatch '+id)
# All local destinations are interpreted from logical vp/LEDGER location even for preserved input copies.
refs={m.group(1).lower():m.group(2) for m in re.finditer(r'^\[([^\]]+)\]:\s+(\S+)',text,re.M)}
for label in re.findall(r'\[[^\]\n]+\]\[([^\]]+)\]',text):
 if label.lower() not in refs:errors.append('undefined reference '+label)
dests=re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',text)+list(refs.values());count=0
for dest in dests:
 s=urlsplit(dest)
 if s.scheme or dest.startswith('//') or not s.path:continue
 count+=1
 if not (vp/unquote(s.path)).exists():errors.append('unresolved '+dest)
print(json.dumps({'ledger':str(ledger),'logical_base':str(vp),'rows':len(rows),'expected_ids':len(expected),'local_destinations':count,'errors':errors,'limits':'Metadata/navigation and selected original audit fields only; no independent conformance verdict'},indent=2))
sys.exit(bool(errors))
