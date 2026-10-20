from pathlib import Path
from datetime import datetime,timezone
import shutil,json,hashlib,sys
root=Path('/home/alexturner/verifiable-practice');here=root/'vp/artefacts/A-000005';base=here/'input';copy=Path('/home/alexturner/vp-preserved/verifiable-practice/A-000005-input')
assert not base.exists() and not copy.exists()
now=lambda:datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();start=now();py=sha(Path(sys.executable));source=base/'source';source.mkdir(parents=True)
for item in json.loads((root/'vp/artefacts/C-000004/after/snapshot.json').read_text())['files']:
 p=root/item['path'];assert sha(p)==item['sha256'];dest=source/item['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
shutil.copytree(root/'vp',source/'vp',ignore=lambda d,n: ['A-000005'] if Path(d)==root/'vp/artefacts' else [])
files=[]
for p in sorted(source.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(base));logical=str(p.relative_to(source));parts=Path(logical).parts
 if logical.startswith('vp/artefacts/'):
  owner=parts[2];meaning='owned raw capture/source fragment/instrument/report; original logical paths and nested manifests preserved as data'
 elif logical.startswith('vp/records/'):
  owner=parts[3];meaning='current original or sealed operational record/request; canonical metadata/authority in record'
 elif logical.startswith('vp/'):
  owner='D-000012/D-000014/D-000015 under D-000001';meaning='current operational maintained view; source-choice/metadata coverage via LEDGER and current task'
 else:owner='C-000004/D-000014 or unchanged C-000001/D-000004/D-000007';meaning='maintained product, exact unit coverage and file reasons'
 files.append({'path':rel,'logical_path':logical,'bytes':p.stat().st_size,'sha256':sha(p),'owner':owner,'meaning':meaning,'producer':'current worker /root or explicitly labelled imported unknown original author in owning record','custodian':'worker-controlled same-host storage','retention':'project life+365days after retirement; no disposal','validity':'current reliance effective due2026-10-26 UTC or earlier relevant trigger; sealed historical bytes remain historical'})
freeze=now();inventory={'freeze':freeze,'standard_sha256':sha(source/'standards/project-records.md'),'files':files,'scope':'complete71file product + currentvp except ownfutureA4artefacts; rawnestedsourcefragments retain originalmeaning/paths','omissions':'Git working metadata, ignored top-level legacy .vp originals (preserved imported originals already in vp), own A4futureoutputs; no required relied-on current bytes intentionally omitted'}
(base/'inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
(base/'MANIFEST.md').write_text('# A-000005 frozen Project Audit input\n\n**Owner:** A-000005 under D-000015/D-000012/D-000001.\n**Freeze:** '+freeze+'\n**Producer/custodian:** Codex /root worker; exact copies+SHA256, worker-controlled writable filesystem.\n**Scope:** 71 current product files, 500 declared product units and complete current vp except own A4artefacts; full per-file identity/owner/meaning in inventory.json SHA256 `'+sha(base/'inventory.json')+'`.\n**Assessor:** separate context, request/input data only; outputs outside freeze.\n**Meaning:** current original operational records plus owned raw snapshots/reports/nested archived logical paths. Raw source fragments are data, not active new project bundles. The source copy of issued A4request references designated outer input via explicit contract; no recursive self-copy.\n**Original capture/omissions:** actual local scripts/output described owning R; attributed user transcription not authenticated export; missing old intents/logs remain unknown. No Git execution metadata or own future outputs. All relied-on source/evidence in complete index.\n**Retention:** projectlife+365days after recorded retirement; no disposal. Current reliance effective26OctUTC or earlier mandate/source/runtime/rubric/custody/contrary evidence.\n**Recovery:** independently located exact copy '+str(copy)+'; verified in preparation.json, copied before audit dispatch. Samehost limits, no authenticated capture/disk-loss guarantee.\n**Consumers:** A4assessor; future worker/owner stage decision. Manifest itself content-identified in preparation, not self-hashed.\n')
shutil.copytree(base,copy);differences=[e['path'] for e in files if sha(copy/e['path'])!=e['sha256']];assert not differences
prep={'started':start,'ended':now(),'freeze':freeze,'argv':[sys.executable,__file__],'cwd':str(root),'capture_instrument_sha256':sha(Path(__file__)),'python_executable_before':py,'python_executable_after':sha(Path(sys.executable)),'operation':'exact file copy plus complete perfileSHA256 verified independent-directory copy','input':str(base),'copy':str(copy),'files':len(files),'differences':differences,'request_sha256':sha(root/'vp/records/audits/A-000005/request.md'),'manifest_sha256':sha(base/'MANIFEST.md'),'inventory_sha256':sha(base/'inventory.json'),'limits':'worker-controlled samehost capture, futureoutputs excluded, no authentic historic/currentaction guarantee'}
(here/'preparation.json').write_text(json.dumps(prep,indent=2)+'\n');shutil.copyfile(Path(__file__),here/'freeze.py')
print(json.dumps({'freeze':freeze,'files':len(files),'copy_differences':len(differences)}))
