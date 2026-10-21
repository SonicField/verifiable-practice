"""Bounded Markdown packet assembly; never copies source or expands prior packets."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
root=Path('/home/alexturner/verifiable-practice');a=root/'vp/artefacts/R-000013/packet-shape-01';assert not a.exists();a.mkdir();sha=lambda b:hashlib.sha256(b).hexdigest()
def packet(commit,replica,prior,source=None,earlier_contents=None):
 if source is not None or earlier_contents is not None:raise ValueError('Source copies and earlier packet contents are forbidden')
 assert len(commit)==40
 return f'''# Immutable audit packet index

Revision: `{commit}`.
Scope paths: current product roots (.github, README.md, SKILL.md, WHY.md,
ORIGIN.md, CHANGELOG.md, community/configuration files, concepts, docs,
playbooks, standards, templates); six vp views; current records; unique
current owner evidence and successor manifest locators. Historical source
copies and own future assessor outputs are excluded. Resolve exact paths
with Git at the fixed revision; never expand prior packet contents.
Verified replica: `{replica}`.
Previous report locator only: `{prior}`.
Standard/authority/read boundary: identified at the fixed revision. Missing
bytes are findings, not permission to substitute live files. The independent
assessor writes only its report and ends.
'''
base='9605ad0dccea157880a05208babfdac5aa5a5fcd';ext=Path('/home/alexturner/vp-preserved/verifiable-practice/review-20261021');cycles=[]
# Three assembly cycles with different prior histories; no assessment verdict is claimed.
for label,prior_count,prior in [('cycle1',0,'none; first assessment'),('cycle2',1,base+':vp/records/audits/A-000001/record.md'),('cycle3',7,base+':vp/records/audits/A-000007/record.md')]:
 before={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts};text=packet(base,str(ext/'baseline.bundle'),prior);path=a/(label+'.md');path.write_text(text);after={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts};added=after-before;assert added=={str(path.relative_to(root))};assert len(text.encode())<=2048;cycles.append({'label':label,'prior_audits':prior_count,'packet_bytes':len(text.encode()),'sha256':sha(text.encode()),'added_paths':sorted(added),'scope_expansion':False})
controls=[]
for label,kwargs in [('copied-source',{'source':'in-memory negative payload'}),('earlier-packet',{'earlier_contents':'in-memory negative payload'})]:
 try:packet(base,str(ext/'baseline.bundle'),'none',**kwargs)
 except ValueError as e:controls.append({'label':label,'rejected':True,'reason':str(e)})
 else:raise AssertionError('Negative input accepted')
result={'completed':datetime.now(timezone.utc).isoformat(),'cycles':cycles,'controls':controls,'maximum_packet_bytes':max(c['packet_bytes'] for c in cycles),'constant_shape':True,'tree_growth':'exactly one metadata file per cycle; no source/earlier packet expansion','claim':'packet content is a fixed scope/revision/replica and immediate report pointer; number of older audits is not an assembly input','limits':'three actual assembly cycles, not three performed independent audits; growing Git replica history is deliberately distinct from bounded packet metadata'}
(a/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
