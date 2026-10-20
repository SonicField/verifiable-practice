#!/usr/bin/env python3
"""Read-only VP self-audit checks; capture writes only into this evidence directory."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_and_untracked():
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT, capture_output=True, check=True,
    )
    return sorted(set(p for p in result.stdout.decode().split("\0") if p))


def capture():
    manifest_path = HERE / "snapshot.json"
    if manifest_path.exists():
        raise SystemExit("Snapshot already exists; refusing to overwrite it")
    names = tracked_and_untracked()
    files = []
    for name in names:
        original = ROOT / name
        target = HERE / "source" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
        files.append({"path": name, "bytes": target.stat().st_size,
                      "sha256": digest(target)})
        if digest(original) != digest(target):
            raise SystemExit(f"Concurrent input change: {name}")
    def git(*args):
        return subprocess.run(["git", *args], cwd=ROOT, text=True,
                              capture_output=True, check=True).stdout.strip()
    manifest = {"captured_utc": datetime.now(timezone.utc).isoformat(),
                "repository": str(ROOT), "head": git("rev-parse", "HEAD"),
                "status": git("status", "--short"), "files": files,
                "capture": "Auditor copy of Git-enumerated current files; not independent action capture"}
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"files": len(files), "head": manifest["head"],
                      "captured_utc": manifest["captured_utc"]}))


def verify(live=False):
    manifest = json.loads((HERE / "snapshot.json").read_text())
    base = ROOT if live else HERE / "source"
    failures = [entry["path"] for entry in manifest["files"]
                if not (base / entry["path"]).is_file()
                or digest(base / entry["path"]) != entry["sha256"]]
    if live:
        failures += ["ADDED: " + name for name in
                     sorted(set(tracked_and_untracked()) -
                            {entry["path"] for entry in manifest["files"]})]
    print(json.dumps({"check": "input identities", "live": live,
                      "files": len(manifest["files"]), "differences": failures}))
    return bool(failures)


def outside_fences(content):
    active = None
    visible = []
    for line in content.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, suffix = match.groups()
            if active is None:
                active = marker
            elif marker[0] == active[0] and len(marker) >= len(active) and not suffix.strip():
                active = None
            visible.append("")
        else:
            visible.append(line if active is None else "")
    return "\n".join(visible), active


def structural(base):
    names = [entry["path"] for entry in json.loads((HERE / "snapshot.json").read_text())["files"]]
    markdown = [name for name in names if name.endswith(".md")]
    broken, fences, newlines = [], [], []
    relative_count, external_count, placeholder_count = 0, 0, 0
    for name in markdown:
        content = (base / name).read_text()
        visible, active = outside_fences(content)
        if active:
            fences.append(name)
        if not content.endswith("\n"):
            newlines.append(name)
        destinations = re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", visible)
        destinations += re.findall(r"^\s*\[[^\]]+\]:\s+(\S+)", visible, re.M)
        for destination in destinations:
            destination = destination.strip().split(' "', 1)[0]
            if destination.startswith("<") and destination.endswith(">"):
                destination = destination[1:-1]
            if "<" in destination or ">" in destination:
                placeholder_count += 1
                continue
            split = urlsplit(destination)
            if split.scheme or destination.startswith("//"):
                external_count += 1
                continue
            if not split.path:
                continue
            relative_count += 1
            if not ((base / name).parent / unquote(split.path)).exists():
                broken.append({"file": name, "destination": destination})
    skill = (base / "SKILL.md").read_text()
    routed = [name for name in names if name.startswith(("concepts/", "playbooks/", "docs/", "standards/"))
              and name.endswith(".md")] + ["templates/project-records/README.md"]
    missing_routes = [name for name in routed if f"]({name})" not in skill]
    common = ["ID", "Type", "Created", "Author/operator", "Status", "Origin", "Goal served", "Sealed"]
    operations = ["decision", "stage", "hypothesis", "experiment", "build", "run", "change", "event", "audit", "audit-response"]
    missing_fields = {name: [field for field in common if f"**{field}:**" not in
                      (base / f"templates/project-records/{name}.md").read_text()] for name in operations}
    missing_fields = {name: fields for name, fields in missing_fields.items() if fields}
    result = {"check": "structural", "markdown_files": len(markdown),
              "relative_file_links": relative_count, "external_links_not_fetched": external_count,
              "placeholder_destinations_skipped": placeholder_count,
              "broken_file_links": broken, "unbalanced_fences": fences,
              "missing_final_newlines": newlines, "missing_skill_routes": missing_routes,
              "operation_templates": len(operations), "missing_common_fields": missing_fields,
              "limits": "No Markdown rendering, heading-anchor validation, placeholder instantiation or AI execution"}
    print(json.dumps(result, indent=2))
    return bool(broken or fences or newlines or missing_routes or missing_fields)


def python_block(base, file, function):
    content = (base / file).read_text()
    return next(block for block in re.findall(r"```python\n(.*?)\n```", content, re.S)
                if f"def {function}(" in block)


def transfer(base):
    source = python_block(base, "concepts/engineering-standards.md", "transfer_funds")
    observations = []
    failures = 0
    for optimisation in (0, 1, 2):
        namespace = {}
        exec(compile(source, "VP transfer example", "exec", optimize=optimisation), namespace)
        for label, amount in (("negative", -5), ("overdraft", 20)):
            sender = type("Account", (), {"balance": 10})()
            receiver = type("Account", (), {"balance": 0})()
            error = None
            try:
                namespace["transfer_funds"](sender, receiver, amount)
            except Exception as exception:
                error = type(exception).__name__
            preserved = (sender.balance, receiver.balance) == (10, 0)
            safe = error is not None and preserved
            failures += not safe
            observations.append({"optimisation": optimisation, "case": label,
                                 "error": error, "balances": [sender.balance, receiver.balance],
                                 "rejects_before_mutation": safe})
    print(json.dumps({"check": "transfer", "cases": observations, "unsafe_cases": failures}, indent=2))
    return bool(failures)


def email(base):
    namespace = {}
    exec(python_block(base, "WHY.md", "validate_email"), namespace)
    case = "user@[192.168.1.1]"
    actual = namespace["validate_email"](case)
    text = (base / "WHY.md").read_text()
    mismatch = f'`"{case}"` fails' in text and actual is not False
    print(json.dumps({"check": "email", "input": case, "actual": actual,
                      "document_claims_rejection": f'`"{case}"` fails' in text,
                      "contradiction": mismatch}))
    return mismatch


parser = argparse.ArgumentParser()
parser.add_argument("check", choices=["capture", "verify", "structural", "transfer", "email"])
parser.add_argument("--live", action="store_true", help="Read live source instead of the preserved snapshot")
args = parser.parse_args()
base = ROOT if args.live else HERE / "source"
if args.check == "capture":
    capture()
    result = 0
elif args.check == "verify":
    result = verify(args.live)
else:
    result = {"structural": structural, "transfer": transfer, "email": email}[args.check](base)
sys.exit(int(bool(result)))
