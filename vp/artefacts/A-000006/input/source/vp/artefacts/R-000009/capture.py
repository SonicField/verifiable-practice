"""New one-attempt ledger batch. Reuse retained identity capture helpers only."""
from pathlib import Path
import json,shutil
here=Path(__file__).parent;ns={};helper=here.parent/'R-000008/capture.py';exec(helper.read_text().split("if (HERE/'results.json')")[0],ns)
if (here/'results.json').exists():raise SystemExit('New R required; refuse overwrite')
ns['HERE']=here;ns['started']=ns['now']();ns['members']=[];ns['py']=Path('/usr/bin/python3');ns['initial']=ns['identity'](ns['py']);ns['initialdeps']=ns['deps']()
# The exact helper function's global environment is this same dictionary.
code=helper.read_text();a=code.index('def run(label');b=code.index("head=run(");exec(code[a:b],ns)
run=ns['run'];vp=ns['VP'];py=ns['py'];write=ns['write'];identity=ns['identity'];inputs=[p for p in sorted((vp/'records').glob('*/*/*.md')) if p.name in ('record.md','request.md')]
write(here/'dependencies-before.json',{'files':ns['initialdeps']});write(here/'helpers-identity.json',{'capture_helpers':identity(helper),'instrument':identity(__file__)})
run('generate-ledger',[py,here/'generate_ledger.py'],0,[here/'generate_ledger.py',*inputs])
ledger=vp/'LEDGER.md';shutil.copyfile(ledger,here/'candidate-ledger.md');text=ledger.read_text();rows=[l for l in text.splitlines() if l.startswith('| [')];row=rows[0];cells=row.split('|');cells[2]=' placeholder ';changed='|'.join(cells);write(here/'missing-type-ledger.md',text.replace(row,changed,1));write(here/'control-inputs.json',{'original_row':row,'changed_row':changed,'baseline':'C-000005/before/views/LEDGER.md','limits':'actual Type cell replaced; same checker as complete/baseline'})
for label,p,expected in [('candidate',here/'candidate-ledger.md',0),('deficient-predecessor',vp/'artefacts/C-000005/before/views/LEDGER.md',1),('missing-type',here/'missing-type-ledger.md',1)]:
 run(label,[py,here/'check_ledger.py',p,vp],expected,[here/'check_ledger.py',p,*inputs])
write(here/'dependencies-after.json',{'files':ns['deps']()});write(here/'results.json',{'started':ns['started'],'ended':ns['now'](),'members':ns['members'],'criterion_met':all(m['criterion_met'] for m in ns['members']),'candidate_identity':identity(here/'candidate-ledger.md'),'claim':'H-000008 bounded ledger contract failed to falsify; mandatoryfinding closure pending independent A5','limits':'worker-controlled source-only metadata/navigation evidence; no authenticated history, full product efficacy or self-awarded conformance'})
print(json.dumps({'members':[(m['label'],m['criterion_met']) for m in ns['members']],'ledger':identity(ledger)}))
