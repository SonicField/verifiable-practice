"""Remove only history whose complete baseline restoration has succeeded."""
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,hashlib,shutil
root=Path('/home/alexturner/verifiable-practice');vp=root/'vp';a=vp/'artefacts/R-000013';restore=json.loads((a/'restore-01/results.json').read_text());legacy=json.loads((a/'ignored-legacy-inventory.json').read_text());assert restore['performed_restore'] and not restore['mismatches'] and not legacy['missing_baseline_bytes'];base=restore['baseline'];now=datetime.now(timezone.utc).isoformat();manifest=[];removed=[]
for e in restore['files']:
 p=e['path'];parts=Path(p).parts
 if p.startswith('vp/artefacts/') and len(parts)==4 and parts[-1]=='MANIFEST.md':manifest.append(e)
 if p.startswith('vp/artefacts/') or p.startswith('vp/records/'):removed.append(p)
# New transition records/evidence were not in the baseline, and are not targeted.
assert not any(p.startswith('vp/artefacts/R-000013/') or p.startswith('vp/artefacts/D-000026/') for p in removed)
r=subprocess.run(['/usr/bin/git','rm','-r','--ignore-unmatch','--']+removed,cwd=root,capture_output=True);(a/'prune.stdout.bin').write_bytes(r.stdout);(a/'prune.stderr.bin').write_bytes(r.stderr);r.check_returncode()
for e in manifest:
 p=root/e['path'];p.parent.mkdir(parents=True,exist_ok=True);owner=p.parent.name
 p.write_text(f'''# {owner}: current locator for historical evidence

This is a successor custody index under D26, not the original sealed manifest.
Original: `{base}:{e['path']}`, blob `{e['object']}`, SHA256 `{e['sha256']}`.
The owner's historical evidence resolves under `{base}:vp/artefacts/{owner}/`.
Its original manifest supplies per-file meaning, producer, consumers and limits.

All baseline bytes were actually restored from `records-archive-2026-10` in
`/home/alexturner/vp-preserved/verifiable-practice/review-20261021/baseline.bundle`
and compared, with zero mismatches (R13 restore-01). Current source copies
are removed; historical positives, failures, requests and unknowns remain in
that revision and replica. This index does not certify historical actions.
Retention: project life plus 365 days; no history/replica disposal authorised.
''')
# The ignored original is already preserved byte-for-byte under explicit baseline locators.
for e in legacy['files']:
 p=root/e['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==e['sha256'];p.unlink()
for p in sorted((root/'.vp').rglob('*'),key=lambda p:len(p.parts),reverse=True):
 if p.is_dir():p.rmdir()
(root/'.vp').rmdir()
result={'occurred':now,'baseline':base,'restored_files':restore['file_count'],'removed_tracked_paths':removed,'current_successor_manifest_paths':[e['path'] for e in manifest],'removed_ignored_paths':[e['path'] for e in legacy['files']],'git_rm_exit':r.returncode,'authority':'D26 and current owner feedback Issue3','recovery':'baseline tag and actual independently located restored bundle; every ignored byte mapped to restored baseline','limits':'working-tree retirement only, original Git history and old external preservation directories unchanged'}
(a/'pruning.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'removed_baseline_paths':len(removed),'successor_manifests':len(manifest),'removed_ignored':len(legacy['files'])}))
