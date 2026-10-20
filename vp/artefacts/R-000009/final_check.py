"""Predeclared final complete-view batch member, retained separately."""
from pathlib import Path
import json
here=Path(__file__).parent;helper=here.parent/'R-000008/capture.py';ns={};exec(helper.read_text().split("if (HERE/'results.json')")[0],ns)
if (here/'final-results.json').exists():raise SystemExit('Refuse overwrite')
ns.update({'HERE':here,'started':ns['now'](),'members':[],'py':Path('/usr/bin/python3')});ns['initial']=ns['identity'](ns['py']);ns['initialdeps']=ns['deps']();code=helper.read_text();exec(code[code.index('def run(label'):code.index('head=run(')],ns)
vp=ns['VP'];inputs=[p for p in sorted((vp/'records').glob('*/*/*.md')) if p.name in ('record.md','request.md')]
ns['run']('final-complete-view',[ns['py'],here/'check_ledger.py',vp/'LEDGER.md',vp],0,[here/'check_ledger.py',vp/'LEDGER.md',*inputs]);ns['write'](here/'final-results.json',{'started':ns['started'],'ended':ns['now'](),'members':ns['members'],'criterion_met':all(m['criterion_met'] for m in ns['members']),'limits':'final complete metadata/navigation check before terminal status projections; successor A assesses its actual later exactfreeze'})
print('Final complete-view criterion met')
