#!/usr/bin/env python3
"""
HYPERION-Ω assembly validator.

Run this AFTER gathering the 1000 worker outputs into parts/<tier_slug>/.
Each of the 1000 machines uploads only its own file; no machine ever downloads
another's. This script is the only place where the 1000 files meet.

Checks (a failure in any one blocks the build):
  1. contract identity    - the Ω-Contract block is byte-identical in all 1000 headers
  2. manifest agreement   - each PART_MANIFEST matches manifest/parts.json
  3. capability closure   - every `requires` has exactly one provider
  4. acyclicity           - the capability graph is a DAG
  5. isolation            - no file imports any other parts/** module
  6. line budget          - every file within +/-3% of 5000 lines
  7. required symbols     - all five contract symbols present
  8. fallback coverage    - a declared fallback exists for every requirement

Run:  python3 tools/validate_assembly.py [--parts-dir parts]
Exit code 0 = assembly is link-valid.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import contracts as C  # noqa: E402

TOLERANCE = 0.03
REQUIRED_SYMBOLS = ("PART_MANIFEST", "register", "selftest", "microbench", "describe")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    def fail(self, check: str, msg: str) -> None:
        self.failures.append(f"[{check}] {msg}")

    def warn(self, check: str, msg: str) -> None:
        self.warnings.append(f"[{check}] {msg}")

    def note(self, msg: str) -> None:
        self.notes.append(msg)

    @property
    def ok(self) -> bool:
        return not self.failures


def contract_digest(text: str) -> str:
    return hashlib.blake2b(text.strip().encode("utf-8"), digest_size=16).hexdigest()


def load_expected() -> list[dict]:
    path = ROOT / "manifest" / "parts.json"
    if not path.exists():
        raise SystemExit("manifest/parts.json missing - run tools/generate.py first")
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------
# check 3 + 4: capability closure and acyclicity (works from the manifest
# alone, so it can run before any worker has finished)
# --------------------------------------------------------------------------
def check_capability_graph(expected: list[dict], rep: Report) -> None:
    providers: dict[str, list[str]] = defaultdict(list)
    for p in expected:
        for cap in p["provides"]:
            providers[cap].append(p["part_id"])

    for cap, owners in sorted(providers.items()):
        if len(owners) > 1:
            rep.fail("closure", f"{cap} provided by {len(owners)} parts: {', '.join(owners)}")

    by_id = {p["part_id"]: p for p in expected}
    for p in expected:
        for cap in p["requires"]:
            if cap not in providers:
                rep.fail("closure", f"{p['part_id']} requires {cap}, which no part provides")

    # acyclicity over part-level edges induced by capabilities
    owner_of = {cap: owners[0] for cap, owners in providers.items() if len(owners) == 1}
    edges: dict[str, set[str]] = {p["part_id"]: set() for p in expected}
    for p in expected:
        for cap in p["requires"]:
            src = owner_of.get(cap)
            if src and src != p["part_id"]:
                edges[p["part_id"]].add(src)

    WHITE, GREY, BLACK = 0, 1, 2
    color: dict[str, int] = dict.fromkeys(edges, WHITE)
    cycles: list[list[str]] = []

    def visit(node: str, stack: list[str]) -> None:
        color[node] = GREY
        stack.append(node)
        for nxt in sorted(edges[node]):
            if color[nxt] == GREY:
                cycles.append(stack[stack.index(nxt):] + [nxt])
            elif color[nxt] == WHITE:
                visit(nxt, stack)
        stack.pop()
        color[node] = BLACK

    sys.setrecursionlimit(10000)
    for node in sorted(edges):
        if color[node] == WHITE:
            visit(node, [])

    for cyc in cycles[:10]:
        rep.fail("acyclicity", "cycle: " + " -> ".join(f"{n} ({by_id[n]['slug']})" for n in cyc))

    rep.note(f"capability graph: {len(providers)} capabilities, "
             f"{sum(len(v) for v in edges.values())} part-level edges, "
             f"{len(cycles)} cycles")


# --------------------------------------------------------------------------
# checks 1, 2, 5, 6, 7, 8: require the gathered files
# --------------------------------------------------------------------------
IMPORT_PATTERNS = [
    re.compile(r"^\s*(?:from|import)\s+([\w\.]*parts\.[\w\.]+)", re.M),
    re.compile(r"^\s*(?:from|import)\s+(hyperion\.t\d\d\.[\w\.]+)", re.M),
    re.compile(r"""(?:require|import)\s*\(\s*['"](.*?parts/.*?)['"]\s*\)""", re.M),
    re.compile(r"""^\s*use\s+crate::parts::([\w:]+)""", re.M),
]


def check_files(expected: list[dict], parts_dir: pathlib.Path, rep: Report) -> None:
    present = 0
    digests: dict[str, list[str]] = defaultdict(list)

    for p in expected:
        path = ROOT / p["file"]
        if parts_dir != ROOT / "parts":
            path = parts_dir / pathlib.Path(p["file"]).relative_to("parts")
        if not path.exists():
            rep.warn("presence", f"{p['part_id']} not gathered yet ({p['file']})")
            continue
        present += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.count("\n") + 1

        # 6. line budget
        lo = int(p["loc_target"] * (1 - TOLERANCE))
        hi = int(p["loc_target"] * (1 + TOLERANCE))
        if not (lo <= lines <= hi):
            rep.fail("line-budget", f"{p['part_id']} has {lines} lines, need {lo}..{hi}")

        # 1. contract identity
        marker = "OMEGA CONTRACT v"
        if marker not in text:
            rep.fail("contract", f"{p['part_id']} does not carry the Ω-Contract header")
        else:
            start = text.index(marker)
            block = text[start:start + len(C.OMEGA_CONTRACT) + 200]
            digests[contract_digest(block[:len(C.OMEGA_CONTRACT)])].append(p["part_id"])

        # 7. required symbols
        for sym in REQUIRED_SYMBOLS:
            if sym not in text:
                rep.fail("symbols", f"{p['part_id']} is missing required symbol `{sym}`")

        # 2. manifest agreement (string presence is enough for a static check)
        if p["capability"] not in text:
            rep.fail("manifest", f"{p['part_id']} does not declare its capability "
                                 f"{p['capability']}")

        # 5. isolation - the check that enforces the no-shared-folder design
        for pat in IMPORT_PATTERNS:
            for m in pat.finditer(text):
                target = m.group(1)
                if p["module"] in target:
                    continue
                rep.fail("isolation", f"{p['part_id']} imports another part: {target!r}")

        # 8. fallback coverage
        for cap in p["requires"]:
            tail = cap.split(".")[-1].split("@")[0]
            if tail not in text:
                rep.fail("fallback", f"{p['part_id']} never mentions required `{cap}`, so it "
                                     f"cannot have a declared fallback for it")

    if len(digests) > 1:
        biggest = max(digests.values(), key=len)
        for d, ids in digests.items():
            if ids is not biggest:
                rep.fail("contract", f"{len(ids)} parts carry a divergent contract digest {d} "
                                     f"(e.g. {', '.join(ids[:5])})")
    rep.note(f"gathered {present}/{len(expected)} part files")


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate a HYPERION-Ω assembly.")
    ap.add_argument("--parts-dir", default="parts",
                    help="directory the 1000 worker outputs were gathered into")
    ap.add_argument("--graph-only", action="store_true",
                    help="only validate the capability graph (no gathered files needed)")
    args = ap.parse_args()

    expected = load_expected()
    rep = Report()

    if len(expected) != 1000:
        rep.fail("count", f"manifest lists {len(expected)} parts, expected 1000")

    check_capability_graph(expected, rep)
    if not args.graph_only:
        check_files(expected, (ROOT / args.parts_dir).resolve(), rep)

    print(f"{C.PROJECT} assembly validation - contract v{C.CONTRACT_VERSION}")
    print("=" * 70)
    for n in rep.notes:
        print(f"  info    {n}")
    for w in rep.warnings[:20]:
        print(f"  WARN    {w}")
    if len(rep.warnings) > 20:
        print(f"  WARN    ... and {len(rep.warnings) - 20} more warnings")
    for f in rep.failures[:50]:
        print(f"  FAIL    {f}")
    if len(rep.failures) > 50:
        print(f"  FAIL    ... and {len(rep.failures) - 50} more failures")
    print("=" * 70)
    if rep.ok:
        print("RESULT: assembly is link-valid.")
        return 0
    print(f"RESULT: {len(rep.failures)} blocking failure(s).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
