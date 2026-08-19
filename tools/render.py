#!/usr/bin/env python3
"""
HYPERION-Ω renderers.

Pure functions: (part records + contracts) -> markdown / text.
No I/O here except what generate.py performs.
"""
from __future__ import annotations

import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import contracts as C  # noqa: E402

GATE_CAP = "cap.t19.gate.action_filter@1"


# ==========================================================================
# small helpers
# ==========================================================================
def anchor(p: dict) -> str:
    """GitHub-style anchor for a part heading."""
    return f"{p['part_id'].lower()}-{p['slug'].replace('_', '-')}"


def spec_link(p: dict) -> str:
    return f"docs/PART_SPECS_{p['tier']}.md#{anchor(p)}"


def prompt_link(p: dict) -> str:
    return f"docs/PROMPTS_{p['tier']}.md#prompt-{anchor(p)}"


def prompt_file(p: dict) -> str:
    return f"prompts/{p['part_id']}_{p['slug']}.txt"


def speed_product() -> float:
    v = 1.0
    for _sid, _name, factor, _desc in C.SPEED_LAW:
        v *= factor
    return v


# --------------------------------------------------------------------------
# Deterministic prose expansion for the four mandate features.
# --------------------------------------------------------------------------
_REQ_TMPL = [
    ("Implement **{f}** as a first-class, fully realised mechanism. No stub, no "
     "`NotImplementedError`, no configuration flag whose default disables it. Its state must be "
     "reportable through `describe()` and it must be exercised by at least eight in-file tests, "
     "including one that fails loudly if the mechanism is silently bypassed."),
    ("Implement **{f}**, and make it correct under concurrency: at least 64 in-flight "
     "`OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be "
     "held across an `await` / `.await` / `yield` boundary, and the part must expose a "
     "contention counter so T09 can attribute latency to it."),
    ("Implement **{f}** with an explicit *a-priori* cost model. Before doing the work the part must "
     "be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort "
     "with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's "
     "`budget` or `deadline_ns`."),
    ("Implement **{f}** together with its verification path, so that anything this mechanism "
     "produces can be independently re-checked *inside this same file* without contacting any other "
     "part. The checker must be cheap enough to run on every call in debug mode and must be wired "
     "into `selftest()`."),
]

_BENCH_TMPL = [
    "Its contribution is measured against **{b}** — a regression on that benchmark is an automatic "
    "rejection of this part.",
    "Correctness here is what makes the tier's **{b}** target reachable; the part therefore ships a "
    "microbenchmark that stands in for that benchmark's inner loop.",
    "This mechanism sits on the critical path of **{b}**, so its p99 latency assertion is part of "
    "the acceptance criteria, not an optional extra.",
]


def expand_features(p: dict) -> list[str]:
    out = []
    base = int(p["part_id"][1:])
    for i, feat in enumerate(p["features"]):
        tmpl = _REQ_TMPL[(base + i) % len(_REQ_TMPL)]
        line = tmpl.format(f=feat)
        if p["tier_bench"]:
            b = p["tier_bench"][(base + i) % len(p["tier_bench"])]
            line += " " + _BENCH_TMPL[(base + i) % len(_BENCH_TMPL)].format(b=b)
        out.append(line)
    return out


_DET_TEXT = {
    "pure": ("`pure` — byte-identical output for byte-identical input, on every machine, forever. "
             "No clock, no RNG, no environment reads, no hash-order iteration, no floating-point "
             "reduction whose order depends on thread count."),
    "seeded": ("`seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. "
               "Given the same seed triple the output is byte-identical. The part must never touch a "
               "global RNG."),
    "io": ("`io` — the part may touch time, devices, sockets or subprocesses, but every such touch "
           "goes through an injected effect handle so that `selftest()` runs fully offline against a "
           "deterministic fake, and a replay log can reproduce any production trace."),
}


def fallback_hint(cap: str) -> str:
    """Deterministic, contract-legal description of the mandatory local fallback."""
    tail = cap.split(".")[-1].split("@")[0]
    if "abi_types" in cap:
        return ("re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set "
                "`degraded['abi']='local-mirror'`")
    if "abi_errors" in cap:
        return ("raise the local `_OmegaErrorShim` carrying the same numeric code, and set "
                "`degraded['errors']='shim'`")
    if "omega_bus_core" in cap:
        return ("run against the in-file `_LoopbackBus` (direct call, no queue) and set "
                "`degraded['bus']='loopback'`")
    if "action_filter" in cap:
        return ("**fail closed** — refuse the effect, emit OmegaCode 6001, and never execute an "
                "unfiltered external action")
    return (f"use the in-file conservative substitute for `{tail}` (documented, slower, lower quality) "
            f"and set `degraded['{tail}']='local'`")


# ==========================================================================
# PART SPEC rendering  (docs/PART_SPECS_Txx.md)
# ==========================================================================
def render_part_spec(p: dict, loc_rows: list[tuple[str, int, str]]) -> str:
    L: list[str] = []
    A = L.append
    A(f"### {p['part_id']} · `{p['slug']}` — {p['title']}")
    A("")
    A("| field | value |")
    A("|---|---|")
    A(f"| part id | `{p['part_id']}` ({p['index_in_tier']}/50 of {p['tier']}) |")
    A(f"| tier | `{p['tier']}` — {p['tier_title']} |")
    A(f"| language | {p['lang']} |")
    A(f"| file to produce | `{p['file']}` |")
    A(f"| module path | `{p['module']}` |")
    A(f"| capability published | `{p['capability']}` |")
    A(f"| determinism class | `{p['determinism']}` |")
    A(f"| p99 latency budget | {p['latency_ns']} ns ({p['latency_ns']/1000:.0f} µs) |")
    A(f"| line budget | {p['loc_target']} lines (map below, ±3 %) |")
    A(f"| benchmarks owned by tier | {', '.join(p['tier_bench']) or '—'} |")
    A(f"| worker prompt | [`{prompt_file(p)}`]({prompt_file(p)}) · [inline]({prompt_link(p)}) |")
    A("")
    A(f"**Mission.** {p['mission']}")
    A("")
    A(f"**Tier context.** {p['tier_mission']}")
    A("")
    A("**Mandate — all four items are required; none is optional.**")
    A("")
    for i, line in enumerate(expand_features(p), start=1):
        A(f"{i}. {line}")
    A("")
    A("**Published capabilities.**")
    A("")
    for c in p["provides"]:
        A(f"- `{c}`")
    A("")
    A("**Required capabilities and their mandatory declared fallbacks.** "
      "Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement "
      "resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → "
      "record the degradation in `describe()['degraded']`.")
    A("")
    A("| required capability | if unavailable, this part must |")
    A("|---|---|")
    for c in p["requires"]:
        A(f"| `{c}` | {fallback_hint(c)} |")
    A("")
    if p.get("late_requires"):
        A("**Runtime safety obligation (contract clause C8).** This part performs or enables "
          "external effects, so every effect must pass the safety gate "
          f"`{GATE_CAP}`. This is deliberately **not** a static link-time dependency — modelling it "
          "as one would make the capability graph cyclic. It is resolved at call time, and it is "
          "**fail-closed**: if the gate is not present on the bus, the part must refuse the effect "
          "and emit OmegaCode 6001. Executing an unfiltered external action is the single most "
          "serious defect a part can contain.")
        A("")
    A(f"**Determinism.** {_DET_TEXT[p['determinism']]}")
    A("")
    A("**Line-count map — this is the acceptance shape of the file.**")
    A("")
    A("| # | section | lines | requirement |")
    A("|---:|---|---:|---|")
    for i, (name, n, why) in enumerate(loc_rows, start=1):
        A(f"| {i} | {name} | {n} | {why} |")
    A(f"| | **total** | **{sum(r[1] for r in loc_rows)}** | |")
    A("")
    A("**Acceptance criteria — a reviewer rejects the file if any one fails.**")
    A("")
    A(f"- [ ] File is exactly one file at `{p['file']}`, self-contained, no imports of any other "
      f"`parts/**` module.")
    A(f"- [ ] `PART_MANIFEST` is present and its `capability` field is exactly "
      f"`{p['capability']}`.")
    A("- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the "
      "contract signatures.")
    A("- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a "
      "temp dir, in under 60 s.")
    A(f"- [ ] `microbench()` asserts p99 ≤ {p['latency_ns']} ns at the declared reference shape.")
    A(f"- [ ] Declared determinism class `{p['determinism']}` is proven by the in-file determinism "
      f"harness.")
    A("- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets "
      "`selftest()` pass in degraded mode.")
    A("- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz "
      "target.")
    A("- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.")
    A(f"- [ ] Total lines within ±3 % of {p['loc_target']}.")
    A("")
    A("**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a "
      "debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / "
      "FIXME / `pass  # later`; suppressing type or lint errors without a written justification.")
    A("")
    A("---")
    A("")
    return "\n".join(L)


def render_spec_file(tier: tuple, parts: list[dict], loc_map) -> str:
    tid, slug, title, lang, ext, mission, bench, deps = tier
    L: list[str] = []
    A = L.append
    A(f"# {C.PROJECT} — Part specifications · {tid} · {title}")
    A("")
    A(f"> Contract: **Ω-CONTRACT v{C.CONTRACT_VERSION}** · 50 parts · "
      f"{len(parts) * 5000:,} lines of code · language: {lang}")
    A("")
    A(f"**Tier mission.** {mission}")
    A("")
    A(f"**Benchmarks this tier is accountable for.** {', '.join(bench) or '—'}")
    A("")
    A(f"**Tier dependencies.** {', '.join(deps) if deps else 'none (this tier is the root)'}")
    A("")
    A("Each part below is built by exactly one isolated Opus 5 worker that sees only: this "
      "specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's "
      "files. Link-compatibility comes from the contract, not from coordination.")
    A("")
    A("| part | slug | title | capability |")
    A("|---|---|---|---|")
    for p in parts:
        A(f"| [{p['part_id']}](#{anchor(p)}) | `{p['slug']}` | {p['title']} | "
          f"`{p['capability']}` |")
    A("")
    A("---")
    A("")
    for p in parts:
        A(render_part_spec(p, loc_map(p)))
    return "\n".join(L)


# ==========================================================================
# PROMPT rendering
# ==========================================================================
def render_prompt_body(p: dict, loc_rows: list[tuple[str, int, str]],
                       inline_contract: bool) -> str:
    style = C.LANG_STYLE[p["ext"]]
    L: list[str] = []
    A = L.append
    A("=" * 78)
    A(f"HYPERION-Ω  ·  WORKER {p['part_id']}  ·  ONE FILE  ·  ~{p['loc_target']} LINES")
    A("=" * 78)
    A("")
    A("ROLE")
    A("----")
    A(f"You are worker {p['part_id']} of 1000 independent Claude Opus 5 instances building "
      f"{C.PROJECT_ASCII}, a general AI that must beat Claude Opus 5 on every benchmark and run 100x")
    A("faster. You are running on your own machine. You have NO access to the other 999 workers,")
    A("NO shared folder, NO ability to ask questions. Everything you need is in this prompt.")
    A("Produce your file in one pass. Do not ask for clarification. Do not stop early.")
    A("")
    if inline_contract:
        A("Ω-CONTRACT (FROZEN — COPY VERBATIM INTO YOUR FILE HEADER)")
        A("-" * 78)
        A(C.OMEGA_CONTRACT.strip())
        A("-" * 78)
    else:
        A("Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.")
    A("")
    A("YOUR PART")
    A("---------")
    A(f"part_id      : {p['part_id']}  ({p['index_in_tier']}/50 of tier {p['tier']})")
    A(f"tier         : {p['tier']} — {p['tier_title']}")
    A(f"title        : {p['title']}")
    A(f"file         : {p['file']}          <-- create exactly this path, nothing else")
    A(f"module       : {p['module']}")
    A(f"language     : {p['lang']}")
    A(f"capability   : {p['capability']}")
    A(f"determinism  : {p['determinism']}")
    A(f"p99 budget   : {p['latency_ns']} ns")
    A(f"line budget  : {p['loc_target']} (+/- 3%)")
    A(f"tier benches : {', '.join(p['tier_bench']) or '-'}")
    A("")
    A("MISSION")
    A("-------")
    for chunk in _wrap(p["mission"], 76):
        A(chunk)
    A("")
    A("Tier context:")
    for chunk in _wrap(p["tier_mission"], 76):
        A("  " + chunk)
    A("")
    A("MANDATE — implement all four. None is optional. None may be stubbed.")
    A("-------------------------------------------------------------------")
    for i, feat in enumerate(p["features"], start=1):
        A(f"  {i}. {feat}")
    A("")
    A("Expanded obligations:")
    for i, line in enumerate(expand_features(p), start=1):
        plain = line.replace("**", "")
        for j, chunk in enumerate(_wrap(plain, 72)):
            A(("  %d. " % i if j == 0 else "     ") + chunk)
    A("")
    A("REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)")
    A("--------------------------------------------------------------------------")
    A("  PART_MANIFEST      : a frozen mapping with keys")
    A("                       part_id, capability, provides, requires, determinism,")
    A("                       latency_ns, loc, contract_version, schema_hash")
    A("  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a")
    A("                       teardown handle; MUST NOT fail if `requires` are missing")
    A("  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in")
    A("                       degraded mode when the bus is empty")
    A("  microbench(iters)  : -> dict with p50/p99/throughput; asserts")
    A(f"                       p99 <= {p['latency_ns']} ns at the reference shape")
    A("  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}")
    A("")
    A("PROVIDES")
    A("--------")
    for c in p["provides"]:
        A(f"  {c}")
    A("")
    A("REQUIRES — and the fallback you MUST write for each one")
    A("------------------------------------------------------")
    A("You may NEVER assume a requirement resolves: the other 999 workers are on other")
    A("machines and their files may not exist when yours is loaded. For each line below,")
    A("write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].")
    for c in p["requires"]:
        A("")
        A(f"  {c}")
        for chunk in _wrap("if unavailable: " + fallback_hint(c).replace("**", ""), 70):
            A("      " + chunk)
    if p.get("late_requires"):
        A("")
        A("RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED")
        A("-----------------------------------------------------------")
        A(f"  Your part performs or enables external effects. Every effect MUST be routed")
        A(f"  through {GATE_CAP} at CALL TIME (not link time).")
        A("  If that capability is absent from the bus you MUST refuse the effect and emit")
        A("  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.")
        A("  Write at least three tests proving the refusal path, including one that asserts")
        A("  no side effect occurred when the gate was missing.")
    A("")
    A("DETERMINISM")
    A("-----------")
    for chunk in _wrap(_DET_TEXT[p["determinism"]].replace("`", "").replace("**", ""), 74):
        A("  " + chunk)
    A("")
    A("LINE MAP — write your file in exactly these sections, in this order.")
    A("-------------------------------------------------------------------")
    for i, (name, n, why) in enumerate(loc_rows, start=1):
        A(f"  {i:2d}. [{n:4d} lines] {name}")
        for chunk in _wrap(why, 66):
            A("                     " + chunk)
    A(f"      TOTAL: {sum(r[1] for r in loc_rows)} lines")
    A("")
    A(f"LANGUAGE RULES ({p['lang']})")
    A("-" * 78)
    A(f"  tests   : {style['test']}")
    A(f"  format  : {style['fmt']}")
    A(f"  typing  : {style['typing']}")
    A(f"  deps    : {style['deps']}")
    A("")
    A("HARD PROHIBITIONS")
    A("-----------------")
    A("  * Do NOT import, reference, read or guess the contents of any other parts/** file.")
    A("  * Do NOT create, rename or delete any file other than your own.")
    A("  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.")
    A("  * No global mutable state; no module-level side effects; no printing outside a")
    A("    debug guard; no network in selftest(); no wall-clock/RNG outside your class.")
    A("  * Do not shorten the file by deleting tests. The line map is the contract.")
    A("")
    A("SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)")
    A("-------------------------------------------------------------------")
    A("  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt")
    A(f"     exactly (capability == {p['capability']})?")
    A("  2. Do all five required symbols exist with the exact signatures?")
    A("  3. With an EMPTY bus, does selftest() still return True in degraded mode?")
    A("  4. Is every `requires` entry paired with a real, working fallback?")
    A(f"  5. Does microbench() actually assert p99 <= {p['latency_ns']} ns?")
    A(f"  6. Is the declared determinism class `{p['determinism']}` provably held?")
    A("  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?")
    A(f"  8. Is the total line count within 3% of {p['loc_target']}?")
    A("  9. Is the Limitations section honest and specific (no marketing claims)?")
    A(" 10. Would this file compile/run on a clean machine with only the declared deps?")
    A("")
    A("OUTPUT FORMAT")
    A("-------------")
    A(f"  Emit ONE fenced code block containing the complete contents of `{p['file']}`.")
    A("  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.")
    A("")
    A("BEGIN NOW.")
    A("=" * 78)
    return "\n".join(L)


def _wrap(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines or [""]


def render_prompt_file(tier: tuple, parts: list[dict], loc_map) -> str:
    tid, slug, title, lang, ext, mission, bench, deps = tier
    L: list[str] = []
    A = L.append
    A(f"# {C.PROJECT} — Worker prompts · {tid} · {title}")
    A("")
    A(f"> 50 prompts · one per part · language {lang} · Ω-CONTRACT v{C.CONTRACT_VERSION}")
    A("")
    A("Each prompt is self-contained *except* for the contract, which is **BLOCK A** below. "
      "Prepend BLOCK A verbatim when dispatching a prompt, or use the fully inlined "
      "single-file version in [`prompts/`](../prompts) — those `.txt` files already contain it.")
    A("")
    A("## BLOCK A — Ω-CONTRACT v" + C.CONTRACT_VERSION + " (verbatim, frozen)")
    A("")
    A("````text")
    A(C.OMEGA_CONTRACT.strip())
    A("````")
    A("")
    A("---")
    A("")
    for p in parts:
        A(f"## PROMPT {anchor(p)}")
        A("")
        A(f"**{p['part_id']} · `{p['slug']}` — {p['title']}** · "
          f"[spec](PART_SPECS_{tid}.md#{anchor(p)}) · "
          f"[self-contained txt](../{prompt_file(p)})")
        A("")
        A("````text")
        A(render_prompt_body(p, loc_map(p), inline_contract=False))
        A("````")
        A("")
    return "\n".join(L)
