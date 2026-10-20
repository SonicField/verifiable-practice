"""Final full-index gate then authorised local commit; receipt produced after commit."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,sys
root=Path('/home/alexturner/verifiable-practice');here=root/'vp/artefacts/V-000011';assert not (here/'first-commit.json').exists()
now=lambda:datetime.now(timezone.utc).isoformat()
def image(p):p=Path(p);return {'path':str(p),'resolved':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
members=[]
def run(label,argv):
 before=image(argv[0]);start=now();r=subprocess.run(argv,cwd=root,capture_output=True);after=image(argv[0]);members.append({'label':label,'argv':argv,'cwd':str(root),'started':start,'ended':now(),'exit':r.returncode,'executable_before':before,'executable_after':after,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()});assert before==after;r.check_returncode();return r.stdout.decode().strip()
# No project/input file mutation between final guard and commit.
run('final-full-index',['/usr/bin/python3',str(root/'vp/artefacts/R-000011/check_index.py')]);run('commit',['/usr/bin/git','commit','--quiet','-m','Clarify VP as a full project quality management system'])
head=run('committed-head',['/usr/bin/git','rev-parse','HEAD']);tree=run('committed-tree',['/usr/bin/git','rev-parse','HEAD^{tree}'])
(here/'first-commit.json').write_text(json.dumps({'captured':now(),'members':members,'head':head,'tree':tree,'instrument':image(__file__),'limits':'post-commit receipt not included in this firstcommit; next receiptcommit under ownerpolicy; source/evidence initialfinalgate distinct from futureoutputs'},indent=2)+'\n')
(here/'final-full-index.stdout.txt').write_text(members[0]['stdout']);print(json.dumps({'head':head,'tree':tree,'final_guard':members[0]['stdout']}))
