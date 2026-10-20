import json, subprocess, hashlib, datetime, sys
from pathlib import Path
root=Path("/home/alexturner/verifiable-practice")
out=root/"vp/artefacts/A-000007/assessment"
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(b): return hashlib.sha256(b).hexdigest()
def git(*args): return subprocess.check_output(["/usr/bin/git",*args],cwd=root)
packet=root/"vp/artefacts/A-000007/input"
inv=json.loads((packet/"inventory.json").read_bytes()); prep=json.loads((packet/"preparation.json").read_bytes())
c=inv["git_commit"]
outer={str(x.relative_to(root)): {"bytes":len(x.read_bytes()),"sha256":digest(x.read_bytes())} for x in [root/"vp/records/audits/A-000007/request.md",*(packet/n for n in ["MANIFEST.md","inventory.json","preparation.json"])]}
errors=[]
for k,n in [("request_sha256","vp/records/audits/A-000007/request.md"),("manifest_sha256","vp/artefacts/A-000007/input/MANIFEST.md"),("inventory_sha256","vp/artefacts/A-000007/input/inventory.json")]:
 if prep[k]!=outer[n]["sha256"]:errors.append("outer "+n)
for x in prep["outer_preparation_files"]:
 b=(root/x["path"]).read_bytes()
 if len(b)!=x["bytes"] or digest(b)!=x["sha256"]:errors.append("preparation "+x["path"])
tree=git("rev-parse",c+"^{tree}").decode().strip()
if tree!=inv["git_tree"] or tree!=prep["git_tree"]: errors.append("tree")
entries={}
raw=git("ls-tree","-r","-z",c)
for entry in raw.split(b"\0"):
 if not entry: continue
 meta,path=entry.split(b"\t",1); mode,typ,oid=meta.decode().split()
 entries[path.decode()] = (mode,typ,oid)
indexed={x["path"]:x for x in inv["files"]}
if len(indexed)!=len(inv["files"]):errors.append("duplicate indexed path")
if set(entries)!=set(indexed):errors.append("index path set mismatch")
oids=sorted({x["object"] for x in inv["files"]})
p=subprocess.Popen(["/usr/bin/git","cat-file","--batch"],cwd=root,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
p.stdin.write(("\n".join(oids)+"\n").encode()); p.stdin.close()
blobs={}
for oid in oids:
 head=p.stdout.readline().decode().strip().split(); size=int(head[2]); b=p.stdout.read(size);p.stdout.read(1)
 if head[:2]!=[oid,"blob"]:errors.append("blob header "+oid)
 blobs[oid]=(len(b),digest(b))
if p.wait()!=0: errors.append("cat-file exit")
for path,x in indexed.items():
 if entries.get(path)!=(x["mode"],"blob",x["object"]):errors.append("entry "+path)
 if blobs[x["object"]]!=(x["bytes"],x["sha256"]):errors.append("digest "+path)
 if x["locator"]!=c+":"+path:errors.append("locator "+path)
req=git("show",c+":vp/records/audits/A-000007/request.md")
if digest(req)!=prep["request_sha256"]:errors.append("snapshot request")
bundle=Path(prep["bundle"]); b=bundle.read_bytes()
if (len(b),digest(b))!=(prep["bundle_bytes"],prep["bundle_sha256"]):errors.append("bundle digest")
verify=subprocess.run(["/usr/bin/git","bundle","verify",str(bundle)],cwd=root,capture_output=True)
heads=git("bundle","list-heads",str(bundle)).decode()
if verify.returncode or heads.strip()!=c+" HEAD":errors.append("bundle verify/tip")
result={"started":started,"ended":datetime.datetime.now(datetime.timezone.utc).isoformat(),"phase":sys.argv[1],"fixed_commit":c,"tree":tree,"paths":len(entries),"distinct_blobs":len(blobs),"ls_tree_sha256":digest(raw),"outer":outer,"outer_preparation_checked":len(prep["outer_preparation_files"]),"bundle_bytes":len(b),"bundle_sha256":digest(b),"bundle_verify_exit":verify.returncode,"bundle_verify_stdout":verify.stdout.decode(),"bundle_verify_stderr":verify.stderr.decode(),"bundle_heads":heads,"errors":errors,"instrument_sha256":digest(Path(__file__).read_bytes()),"git_executable_sha256":digest(Path("/usr/bin/git").read_bytes()),"python_executable_sha256":digest(Path(sys.executable).resolve().read_bytes()),"role":"auditor file/blob accounting only; no project execution; bundle verification is not performed restoration"}
(out/(sys.argv[1]+"-identities.json")).write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
