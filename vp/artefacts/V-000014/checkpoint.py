"""Optional local custody accounting, captured outside the staged tree."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess,json,hashlib,sys
root=Path('/home/alexturner/verifiable-practice');vp=root/'vp';external=Path('/home/alexturner/vp-preserved/verifiable-practice/PTE-removal-20261020');phase=sys.argv[1];attempt=external/(phase+'-checkpoint');assert not attempt.exists();attempt.mkdir();commands=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.now(timezone.utc).isoformat()
def command(label,args):
 exe=Path(args[0]);before=sha(exe);start=now();r=subprocess.run(args,cwd=root,capture_output=True);end=now();out=attempt/(label+'.stdout.bin');err=attempt/(label+'.stderr.bin');out.write_bytes(r.stdout);err.write_bytes(r.stderr);commands.append({'label':label,'argv':args,'cwd':str(root),'started':start,'ended':end,'exit':r.returncode,'executable_sha256_before':before,'executable_sha256_after':sha(exe),'stdout':str(out),'stdout_sha256':sha(out),'stderr':str(err),'stderr_sha256':sha(err)});(attempt/'commands.json').write_text(json.dumps(commands,indent=2)+'\n');r.check_returncode();assert before==sha(exe);return r.stdout
assert phase in ('first','receipt')
command('stage-all',['/usr/bin/git','add','-A']);command('stage-owned-vp',['/usr/bin/git','add','-f','--','vp'])
guard=command('complete-root-guard',['/usr/bin/python3',str(vp/'artefacts/R-000011/check_index.py'),str(attempt/'guard')]);assert json.loads(guard)['criterion_met']
command('staged-whitespace',['/usr/bin/git','-c','core.whitespace=-blank-at-eol','diff','--cached','--check'])
message='Accept semantic PTE removal after independent project audit' if phase=='first' else 'Record semantic removal custody and handoff receipt'
command('commit',['/usr/bin/git','commit','-m',message]);commit=command('commit-id',['/usr/bin/git','rev-parse','HEAD']).decode().strip();tree=command('tree-id',['/usr/bin/git','rev-parse','HEAD^{tree}']).decode().strip()
result={'phase':phase,'ended':now(),'commit':commit,'tree':tree,'instrument':str(Path(__file__).resolve()),'instrument_sha256':sha(Path(__file__)),'commands':commands,'guard_summary':json.loads(guard),'guard_results':str(attempt/'guard/results.json'),'guard_results_sha256':sha(attempt/'guard/results.json'),'guard_index_sha256':sha(attempt/'guard/index.stdout.bin'),'limits':'local worker-controlled Git/byte custody; not source semantics, authenticated authorship or host-loss protection'}
(attempt/'receipt.json').write_text(json.dumps(result,indent=2)+'\n')
if phase=='first':
 a=vp/'artefacts/V-000014';a.mkdir(parents=True,exist_ok=True);(a/'first-checkpoint.json').write_text(json.dumps(result,indent=2)+'\n')
 v=vp/'records/events/V-000014/record.md';t=v.read_text().replace('**Status:** open; checkpoint allocated before execution','**Status:** sealed; first checkpoint complete, containing receipt identified externally',1).replace('**Sealed:** open','**Sealed:** '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),1)
 t+=f'''\n## Actual first checkpoint and final receipt plan\n\nFirst completed checkpoint `{commit}`, tree `{tree}`. Actual commands, executable identities/times/outputs and complete staged-root accounting are in artefacts/V-000014/first-checkpoint.json and its exact external raw locators. Guard criterion passed for {result['guard_summary']['files']} staged files, with no differences, missing vp files or untracked files; changed-blob and omitted-vp-entry controls detected their planted defects. Guard raw results SHA256 `{result['guard_results_sha256']}` at `{result['guard_results']}`. Raw guard/index and command outputs remain owned by V14 at the independently located first-checkpoint directory, not disposable /tmp. Source and complete owned vp evidence were committed together.\n\nThis sealed receipt and final current views are the next authorised receipt commit. Its containing commit and completion bundle/index SHA cannot be known before that commit; the required external completion.json/MANIFEST.md under `/home/alexturner/vp-preserved/verifiable-practice/PTE-removal-20261020/` will identify them after execution. Do not rely on completed recovery without verifying that manifest and bundle. Earlier A7 candidate snapshot/verdict stays unchanged; no remote push, disposal, source change or validity renewal. Review by 26 October UTC/earlier trigger; retain life plus 365 days, same-host custody limits.\n'''
 v.write_text(t)
 lines=['# V-000014 owned checkpoint evidence','','Owner: V14 under D25, producer worker /root. Consumer: handoff/recovery and future audit. External raw staged-index/guard/command captures are identified by first-checkpoint.json; retain life plus 365 days, review 26 October UTC or earlier relevant trigger. Same-host worker-controlled bytes, no authenticated action or host-loss claim.','','| Path | Bytes | SHA256 | Meaning |','|---|---:|---|---|']
 for p in sorted(a.iterdir()):
  if p.is_file() and p.name!='MANIFEST.md':lines.append(f'| {p.name} | {p.stat().st_size} | `{sha(p)}` | Optional custody instrument or captured checkpoint outcome; not product experiment. |')
 for p in sorted(attempt.rglob('*')):
  if p.is_file():lines.append(f'| {p} | {p.stat().st_size} | `{sha(p)}` | Owned independently located custody capture. |')
 lines+=['','Manifest identity and sealed V14 receipt are supplied by the containing receipt commit/external completion index; no self-hash or future-outcome claim.']
 (a/'MANIFEST.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({'phase':phase,'commit':commit,'tree':tree,'guard':result['guard_summary']['criterion_met']}))
