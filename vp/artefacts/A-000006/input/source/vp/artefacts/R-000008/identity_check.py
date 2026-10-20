"""Supplementary opening identity check; not a semantic comprehension test."""
import json,sys
from pathlib import Path
base=Path(sys.argv[1])
names=['README.md','WHY.md','SKILL.md','docs/how-vp-works.md']
observations=[]
for name in names:
    text=(base/name).read_text()
    if name=='SKILL.md' and text.startswith('---'):
        text=text.split('---',2)[2]
    opening='\n'.join(text.splitlines()[:10])
    observations.append({'path':name,'opening':opening,'identity_present':'full project quality management system' in opening})
print(json.dumps({'observations':observations,'limits':'Literal opening identity only; manual requirement matrix supplies semantic assessment'},indent=2))
sys.exit(not all(o['identity_present'] for o in observations))
