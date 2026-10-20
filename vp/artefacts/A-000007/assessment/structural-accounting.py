import subprocess,json,re,hashlib,posixpath,datetime
from pathlib import Path
root=Path("/home/alexturner/verifiable-practice");out=root/"vp/artefacts/A-000007/assessment"
inv=json.loads((root/"vp/artefacts/A-000007/input/inventory.json").read_bytes());c=inv["git_commit"];idx={x["path"]:x for x in inv["files"]};cache={}
def read(p):
 if p not in cache: cache[p]=subprocess.check_output(["git","show",c+":"+p],cwd=root)
 return cache[p]
def j(p):return json.loads(read(p))
def h(b):return hashlib.sha256(b).hexdigest()
def visible(text):
 active=None;lines=[]
 for l in text.splitlines():
  m=re.match(r"^\s*(`{3,}|~{3,})(.*)$",l)
  if m:
   marker,suffix=m.groups()
   if active is None:active=marker
   elif marker[0]==active[0] and len(marker)>=len(active) and not suffix.strip():active=None
   lines.append("")
  else:lines.append(l if active is None else "")
 return "\n".join(lines),active
errors=[];warnings=[]
s=j("vp/artefacts/R-000012/source-inventory.json");u=j("vp/artefacts/R-000012/unit-inventory.json");before=j("vp/artefacts/C-000006/before.json")
product={x["path"] for x in s["files"]};actual={p for p in idx if not p.startswith("vp/")}
if product!=actual:errors.append("product path set")
for x in s["files"]:
 if (x["bytes"],x["sha256"])!=(idx[x["path"]]["bytes"],idx[x["path"]]["sha256"]):errors.append("product identity "+x["path"])
units=[]
for p in sorted(product):
 b=read(p);text=b.decode();digest=h(b)
 units.append((p,1,"file/preamble" if p.endswith(".md") else "whole file",digest))
 if p.endswith(".md"):
  body,fence=visible(text)
  if fence:errors.append("fence "+p)
  for n,l in enumerate(body.splitlines(),1):
   if re.match(r"^#{1,6}\s",l):units.append((p,n,re.sub(r"^#+\s*","",l).replace("|","/"),digest))
recorded=[(x["path"],x["line"],x["unit"],x["sha256"]) for x in u["units"]]
if set(units)!=set(recorded) or len(units)!=len(recorded):errors.append("unit identities")
cov=read("vp/COVERAGE.md").decode();rows=[]
for l in cov.splitlines():
 m=re.match(r"\| (.*?):(\d+) — (.*?) \| `([0-9a-f]{64})` \| (.*?) \| (.*?) \|",l)
 if m:
  p,n,name,digest,choice,valid=m.groups();rows.append((p,int(n),name,digest))
  if "rootD1" not in choice or "26Oct" not in valid:errors.append("coverage trace/validity "+p)
if set(rows)!=set(units) or len(rows)!=len(units):errors.append("coverage rows")
for x in before["files"]:
 b=subprocess.check_output(["git","show",x["locator"]],cwd=root)
 oid=subprocess.check_output(["git","rev-parse",x["locator"]],cwd=root).decode().strip()
 if (len(b),h(b),oid)!=(x["bytes"],x["sha256"],x["git_blob"]):errors.append("baseline "+x["path"])
patch=subprocess.check_output(["git","diff","--binary",s["base"],c,"--",*[x["path"] for x in before["files"] if not x["path"].startswith("vp/")]],cwd=root)
if patch!=read("vp/artefacts/C-000006/change.patch"):errors.append("complete patch")
canonical=sorted(p for p in idx if re.match(r"vp/records/[^/]+/[^/]+/(record|request)\.md$",p));views=["vp/"+x+".md" for x in ["README","PROJECT","PLAN","STATE","LEDGER","COVERAGE"]]+["vp/workspace/README.md"]
links=[];missing=[];field_gaps=[];origins={};ledger=read("vp/LEDGER.md").decode()
for p in canonical:
 text=read(p).decode();rid=p.split("/")[3]
 if rid not in ledger:errors.append("ledger absent "+rid)
 for field in ["ID","Type","Created","Author/operator","Status","Origin","Goal served","Sealed"]:
  if not re.search(r"\*\*[^*]*"+re.escape(field),text,re.I):field_gaps.append((p,field))
 origin=re.search(r"^\*\*Origin:\*\*(.*)$",text,re.M)
 if origin:origins[p]=re.findall(r"\b[DSEHRBVC]-\d{6}\b",origin.group(1))
for p in sorted(product)+views+canonical:
 text,unused=visible(read(p).decode());definitions=dict(re.findall(r"^\s*\[([^]\n]+)\]:\s+(\S+)",text,re.M))
 destinations=re.findall(r"!?\[[^]\n]*\]\(([^)\n]+)\)",text)+list(definitions.values())
 for label in re.findall(r"\[[^]\n]+\]\[([^]\n]+)\]",text):
  if label not in definitions:warnings.append("undefined reference "+p+":"+label)
 for d in destinations:
  d=d.strip().split(' "',1)[0].strip("<>");path=d.split("#",1)[0]
  if not path or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",path) or path.startswith("//") or any(t in path for t in ["<",">"]):continue
  target=posixpath.normpath(posixpath.join(posixpath.dirname(p),path));links.append((p,d,target))
  if target not in idx and not any(x.startswith(target.rstrip("/")+"/") for x in idx):
   if target.startswith("vp/artefacts/A-000007/input/") and (root/target).is_file():continue
   missing.append((p,d,target))
manifest_rows=0;manifest_mismatches=[];manifests=[p for p in idx if re.match(r"vp/artefacts/[^/]+/MANIFEST.md$",p)]
for p in manifests:
 for l in read(p).decode().splitlines():
  m=re.match(r"\| ([^|]+?) \| (\d+) \| `([0-9a-f]{64})` \|",l)
  if not m:continue
  name,n,digest=m.groups();target=posixpath.normpath(posixpath.join(posixpath.dirname(p),name.strip().strip("`")));manifest_rows+=1
  if target not in idx or (idx[target]["bytes"],idx[target]["sha256"])!=(int(n),digest):manifest_mismatches.append((p,name,target))
members=[];res=j("vp/artefacts/R-000012/results.json");deps=j("vp/artefacts/R-000012/dependencies-before.json")
for m in res["members"]:
 observations={"label":m["label"],"started":m["started"],"ended":m["ended"],"exit":m["exit"],"expected_exit":m["expected_exit"],"input_count":len(m["inputs_before"]),"inputs_equal":m["inputs_before"]==m["inputs_after"],"executables_equal":m["executable_before"]==m["executable_after"],"dependencies_equal":j("vp/artefacts/R-000012/"+m["dependencies_before"])==j("vp/artefacts/R-000012/"+m["dependencies_after"]),"stdout_sha256":h(read("vp/artefacts/R-000012/"+m["stdout"])),"stderr_bytes":len(read("vp/artefacts/R-000012/"+m["stderr"]))}
 for x in m["inputs_before"]:
  path=x["path"].removeprefix(str(root)+"/")
  if path in idx and (idx[path]["bytes"],idx[path]["sha256"])!=(x["bytes"],x["sha256"]):errors.append("R12 input identity "+m["label"]+":"+path)
 if not all(observations[k] for k in ["inputs_equal","executables_equal","dependencies_equal"]) or m["exit"]!=m["expected_exit"]:errors.append("member "+m["label"])
 members.append(observations)
base_records=subprocess.check_output(["git","ls-tree","-r","--name-only",s["base"],"vp/records"],cwd=root).decode().splitlines();changed_history=[]
for p in base_records:
 if p.endswith("/record.md") or p.endswith("/request.md"):
  if p in idx:
   old=subprocess.check_output(["git","rev-parse",s["base"]+":"+p],cwd=root).decode().strip()
   if old!=idx[p]["object"]:changed_history.append(p)
result={"time":datetime.datetime.now(datetime.timezone.utc).isoformat(),"fixed_commit":c,"product_files":len(product),"unit_count":len(units),"coverage_rows":len(rows),"baseline_files_checked":len(before["files"]),"patch_sha256":h(patch),"canonical_records_requests":len(canonical),"canonical_allocated_ids":len({p.split("/")[3] for p in canonical}),"common_field_search_gaps":field_gaps,"origins":origins,"local_destinations":len(links),"missing_local_destinations":missing,"direct_owner_manifests":len(manifests),"manifest_digest_rows":manifest_rows,"manifest_mismatches":manifest_mismatches,"dependency_rows_per_member":len(deps["files"]),"members":members,"existing_baseline_records_changed":changed_history,"errors":errors,"warnings":warnings,"limits":"Independent file/link/digest accounting; did not execute project instruments. Inline and reference-definition file destinations only; no shortcut/autolinks, rendered anchors, external URLs or authentication. Origin list requires manual causal interpretation, excludes root/goal/support cycles from origin claims."}
(out/"structural-evidence.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if k not in ["origins","members"]},indent=2))
