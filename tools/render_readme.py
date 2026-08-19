#!/usr/bin/env python3
"""README.md renderer for HYPERION-Ω — the primary deliverable."""
from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import contracts as C  # noqa: E402
from render import (  # noqa: E402
    anchor,
    expand_features,
    fallback_hint,
    prompt_file,
    prompt_link,
    spec_link,
    speed_product,
    _wrap,
)


# ==========================================================================
# compact-but-complete inline prompt (the per-part prompt that lives in README)
# ==========================================================================
def render_inline_prompt(p: dict) -> str:
    style = C.LANG_STYLE[p["ext"]]
    L: list[str] = []
    A = L.append
    A(f"You are worker {p['part_id']} of 1000 isolated Claude Opus 5 instances building "
      f"{C.PROJECT_ASCII}.")
    A("You are on your own machine with no shared folder and no way to see the other 999 files.")
    A("First read PREAMBLE-Z and the Ω-CONTRACT in this repository's README and copy the contract")
    A("verbatim into your file header. Then write ONE complete file and nothing else.")
    A("")
    A(f"file        : {p['file']}")
    A(f"module      : {p['module']}")
    A(f"language    : {p['lang']}")
    A(f"capability  : {p['capability']}")
    A(f"determinism : {p['determinism']}")
    A(f"p99 budget  : {p['latency_ns']} ns")
    A(f"lines       : {p['loc_target']} (+/-3%), split by the LINE MAP in PREAMBLE-Z")
    A(f"benchmarks  : {', '.join(p['tier_bench']) or '-'}")
    A("")
    A("MISSION")
    for c in _wrap(p["mission"], 92):
        A("  " + c)
    A("")
    A("IMPLEMENT ALL FOUR — none optional, none stubbed:")
    for i, f in enumerate(p["features"], start=1):
        A(f"  {i}. {f}")
    A("")
    A("PROVIDE: " + ", ".join(p["provides"]))
    A("REQUIRE (each needs a working in-file fallback; never assume it resolves):")
    for c in p["requires"]:
        A(f"  {c}")
        for cc in _wrap("-> if unavailable: " + fallback_hint(c).replace("**", ""), 86):
            A("      " + cc)
    if p.get("late_requires"):
        A("")
        A("SAFETY (fail closed, clause C8): route every external effect through")
        A("cap.t19.gate.action_filter@1 at CALL TIME. If it is absent, REFUSE the effect and emit")
        A("OmegaCode 6001 — never execute an unfiltered action. Test the refusal path.")
    A("")
    A("EXPORT EXACTLY: PART_MANIFEST, register(bus), selftest(), microbench(iters), describe().")
    A(f"TESTS: {style['test']}; >=40 cases + property tests per invariant + a fuzz target.")
    A(f"STYLE: {style['fmt']}; {style['typing']}; deps: {style['deps']}.")
    A("FORBIDDEN: importing any other parts/** file; touching any other path; TODO/FIXME/stubs;")
    A("global mutable state; network in selftest(); deleting tests to hit the line budget.")
    A(f"SELF-CHECK before emitting: contract verbatim? PART_MANIFEST.capability == "
      f"{p['capability']}?")
    A("five symbols present? selftest() passes with an EMPTY bus in degraded mode? every require has")
    A(f"a fallback? microbench asserts p99 <= {p['latency_ns']} ns? determinism class proven?")
    A(f">=40 tests? lines within 3% of {p['loc_target']}? Limitations section honest?")
    A(f"OUTPUT: one fenced code block = the complete contents of {p['file']}. No prose, no ellipses.")
    return "\n".join(L)


# ==========================================================================
def render_part_block(p: dict, loc_rows) -> str:
    L: list[str] = []
    A = L.append
    A(f"<a id=\"{anchor(p)}\"></a>")
    A(f"#### {p['part_id']} · `{p['slug']}` — {p['title']}")
    A("")
    A(f"`{p['file']}` · {p['lang']} · **{p['loc_target']} lines** · publishes "
      f"`{p['capability']}` · determinism `{p['determinism']}` · p99 ≤ {p['latency_ns']} ns · "
      f"[full spec]({spec_link(p)}) · [full prompt]({prompt_file(p)})")
    A("")
    A(f"**Description.** {p['mission']} "
      f"This part belongs to {p['tier']} ({p['tier_title']}), whose accountability is "
      f"{', '.join(p['tier_bench']) or 'infrastructural'}. It is built by a single isolated worker "
      f"and links to the rest of the system only through the Ω-Bus capability "
      f"`{p['capability']}`; it imports no sibling part. Its four mandated mechanisms are:")
    A("")
    for i, line in enumerate(expand_features(p), start=1):
        A(f"{i}. {line}")
    A("")
    if p["requires"]:
        A(f"It requires {len(p['requires'])} capabilities — "
          + ", ".join(f"`{c}`" for c in p["requires"])
          + " — and must ship a working local fallback for each, so that the file remains usable "
            "when the other 999 workers' output is absent.")
    else:
        A("It requires **no** capabilities: it is a bootstrap part, one of the foundations every "
          "other part stands on. It must therefore be completely self-contained.")
    if p.get("late_requires"):
        A("")
        A(f"**Safety obligation (C8, fail-closed).** This part performs or enables external "
          f"effects, so every effect is routed through `{p['late_requires'][0]}` at *call* time — "
          f"not as a static dependency, which would make the graph cyclic. If the gate is absent "
          f"the part must refuse the effect and emit OmegaCode 6001.")
    A("")
    A("<details><summary><b>Prompt for " + p["part_id"] + "</b> (click to expand)</summary>")
    A("")
    A("```text")
    A(render_inline_prompt(p))
    A("```")
    A("")
    A("</details>")
    A("")
    return "\n".join(L)


# ==========================================================================
def render_readme(parts: list[dict], loc_map) -> str:
    L: list[str] = []
    A = L.append
    by_tier: dict[str, list[dict]] = {}
    for p in parts:
        by_tier.setdefault(p["tier"], []).append(p)

    prod = speed_product()

    # ---------------- title ----------------
    A(f"# {C.PROJECT} — a 1000-part general AI designed to beat Claude Opus 5")
    A("")
    A(f"**Project:** {C.PROJECT} (`{C.PROJECT_ASCII}`) &nbsp;·&nbsp; "
      f"**Contract:** Ω-CONTRACT v{C.CONTRACT_VERSION} &nbsp;·&nbsp; "
      f"**Research date:** {C.RESEARCH_DATE}")
    A("")
    A("**1000 parts × ~5000 lines = ~5,000,000 lines**, each part written by one of 1000 "
      "Claude Opus 5 workers **running on separate machines with no shared folder**.")
    A("")
    A("| goal | mechanism |")
    A("|---|---|")
    A("| Beat Opus 5 on every benchmark, under any measurement methodology | "
      "T18 dominance harness: 18 tracked benchmarks with explicit targets (§2), plus a "
      "methodology-sweep that re-runs each benchmark under adversarial harness variants |")
    A(f"| 100× faster than Opus 5 at everything | the 6-law speed decomposition (§3): nominal "
      f"product **×{prod:.1f}**, i.e. **{prod/100:.2f}× headroom** over the 100× requirement, "
      f"because composing speed-ups always erodes |")
    A("| 1000 isolated workers must still produce link-compatible code | the frozen Ω-Contract "
      "(§4): parts never import each other, they publish/acquire **capability URIs** and every "
      "requirement has a mandatory declared fallback |")
    A("")
    A("> [!IMPORTANT]")
    A("> **This README intentionally contains all 1000 part descriptions and all 1000 worker "
      "prompts inline** (§10), as specified. That makes it ~7 MB / ~80,000 lines, which is above "
      "GitHub's markdown rendering limit, so the web view will show it truncated with a *“view "
      "raw”* link. Nothing is missing — it is all there in the raw file. For comfortable browsing "
      "use the equivalent split artefacts:")
    A("> ")
    A("> | you want | go to |")
    A("> |---|---|")
    A("> | a browsable index of all 1000 parts | [`INDEX.md`](INDEX.md) |")
    A("> | the 1000 detailed specifications | [`docs/PART_SPECS_T01..T20.md`](docs) (50 per file) |")
    A("> | the 1000 prompts, grouped by tier | [`docs/PROMPTS_T01..T20.md`](docs) |")
    A("> | one dispatchable prompt per worker | [`prompts/P0001..P1000_*.txt`](prompts) |")
    A("")
    A("### Contents")
    A("")
    A("1. [What we are competing against — measured Opus 5 baseline](#1-what-we-are-competing-"
      "against)")
    A("2. [Benchmark dominance targets](#2-benchmark-dominance-targets)")
    A("3. [The 100× speed law](#3-the-100-speed-law)")
    A("4. [Ω-CONTRACT v1.0.0-frozen — the reason 1000 isolated workers still link](#4-omega-contract)")
    A("5. [PREAMBLE-Z — the shared block every worker receives](#5-preamble-z)")
    A("6. [The 20 tiers](#6-the-20-tiers)")
    A("7. [Per-part line-count map (~5000 lines)](#7-per-part-line-count-map)")
    A("8. [How to dispatch the 1000 workers](#8-how-to-dispatch-the-1000-workers)")
    A("9. [Assembly and verification without a shared filesystem](#9-assembly-and-verification)")
    A("10. [**All 1000 parts — description + prompt**](#10-all-1000-parts)")
    A("11. [Repository layout](#11-repository-layout)")
    A("12. [Honest limitations](#12-honest-limitations)")
    A("")
    A("---")
    A("")

    # ---------------- 1. research ----------------
    A("## 1. What we are competing against")
    A("")
    A(f"Baseline researched on **{C.RESEARCH_DATE}**. Every number below is recorded with its "
      f"source so that a reviewer can re-verify it; numbers we could not source directly are marked "
      f"`est` in §2 and derived from the nearest published data point.")
    A("")
    A("| attribute | value | source |")
    A("|---|---|---|")
    for attr, val, src in C.OPUS5_FACTS:
        A(f"| {attr} | {val} | {src} |")
    A("")
    A("**Why Opus 5 is hard to beat.** It is not a single-axis model: it is simultaneously rank-1 on "
      "agentic coding (SWE-bench Verified, Frontier-Bench), on abstract reasoning (ARC-AGI-3, where "
      "it roughly triples the next-best system), on computer use (OSWorld, Online-Mind2Web) and on "
      "long-horizon economic work (GDPval-AA). A design that wins on one axis by trading away "
      "another does not satisfy the requirement. This is why the architecture below is organised as "
      "20 accountability tiers, each owning named benchmarks, with a dominance harness (T18) that "
      "fails the build if **any** tracked metric regresses.")
    A("")

    # ---------------- 2. benchmarks ----------------
    A("## 2. Benchmark dominance targets")
    A("")
    A(f"{len(C.BENCHMARKS)} tracked benchmarks. `src` = value taken from a published source; "
      "`est` = derived estimate, flagged as such deliberately rather than presented as fact. "
      f"{C.PROJECT} must exceed the Opus 5 column on **every** row, and the T18 harness re-runs each "
      "row under at least three harness variants (different scaffolds, different prompt budgets, "
      "different tie-breaking) so that the win is not an artefact of one methodology.")
    A("")
    A("| benchmark | Opus 5 | unit | HYPERION-Ω target | margin | prov. | note |")
    A("|---|---:|---|---:|---:|---|---|")
    for name, (score, unit, hib, target, prov, note) in C.BENCHMARKS.items():
        margin = target - score
        A(f"| {name} | {score:g} | {unit} | **{target:g}** | +{margin:g} | `{prov}` | {note} |")
    A("")
    A("**Measurement rules (T18).** (a) every benchmark is run 5× with different seeds and the "
      "*worst* run is reported; (b) the harness code is published with the score; (c) any benchmark "
      "where contamination cannot be excluded is additionally reported on a held-out variant "
      "generated after the training cut-off; (d) a win is only claimed when the lower bound of the "
      "95 % interval exceeds the Opus 5 point estimate.")
    A("")

    # ---------------- 3. speed law ----------------
    A("## 3. The 100× speed law")
    A("")
    A("100× is not one trick. It is six independent multiplicative factors, each owned by specific "
      "tiers and each independently measurable — so a shortfall in one is visible and attributable "
      "rather than hidden in an aggregate.")
    A("")
    A(f"**Why the nominal product is ×{prod:.1f} and not ×100.** Targeting exactly 100 would mean "
      f"assuming the six mechanisms compose perfectly, which they never do: speculative acceptance "
      f"drops when sparse routing changes the draft distribution, memoize hit-rate falls as pruning "
      f"makes traffic more unique, and every layer adds scheduler overhead. We therefore budget "
      f"×{prod:.1f} nominal so that a realistic composition efficiency of ~30 % still clears the "
      f"100× requirement. §12 states plainly that this is a budget, not a measurement.")
    A("")
    A("| law | mechanism | factor | how it is obtained |")
    A("|---|---|---:|---|")
    for sid, name, factor, desc in C.SPEED_LAW:
        A(f"| {sid} | {name} | ×{factor:g} | {desc} |")
    A(f"| | **product** | **×{prod:.1f}** | |")
    A("")
    A("Each of the 1000 parts carries a p99 latency budget (listed per part in §10). T09 sums those "
      "budgets along every critical path; if the sum exceeds the end-to-end target, the build fails. "
      "This is what turns \"100× faster\" from a slogan into a checkable constraint distributed over "
      "1000 independently written files.")
    A("")

    # ---------------- 4. contract ----------------
    A("<a id=\"4-omega-contract\"></a>")
    A(f"## 4. Ω-CONTRACT v{C.CONTRACT_VERSION} — the reason 1000 isolated workers still link")
    A("")
    A("**The constraint:** the 1000 Opus 5 workers run on separate PCs and *cannot share folders*. "
      "So no worker can read another worker's file, agree on a helper module, or negotiate an "
      "interface. Conventional decomposition fails here — the moment part 412 imports part 87, the "
      "build is unbuildable.")
    A("")
    A("**The solution:** freeze the interface *before* any code exists, and make it small enough to "
      "fit in every prompt. Every part receives the identical contract text below and copies it "
      "verbatim into its own header. Parts then never import each other; they publish and acquire "
      "**capability URIs** on the Ω-Bus, and every acquisition has a mandatory declared fallback, so "
      "each file is independently loadable, testable and shippable even if the other 999 do not "
      "exist yet.")
    A("")
    A("```text")
    A(C.OMEGA_CONTRACT.strip())
    A("```")
    A("")
    A("**Capability URI grammar.** `cap.<tier>.<domain>.<name>@<major>` — e.g. "
      "`cap.t08.cascade.scheduler@1`. The major version is the only compatibility axis; a part may "
      "only depend on a major it was told about in its prompt. Since the URI is a string agreed in "
      "advance, two workers who never communicate still resolve to the same edge.")
    A("")
    A("**The DAG invariant — why the assembly can never deadlock.** A part may only *statically* "
      "require a capability owned by a strictly lower-numbered part (P0007 may require P0001's "
      "capability; P0001 may not require P0007's). The 1000-part capability graph is therefore a "
      "DAG **by construction**, verified by `tools/validate_assembly.py` (currently: 2001 "
      "capabilities, 6660 edges, **0 cycles**). The lowest-numbered parts have no requirements at "
      "all — they are the foundation. This matters because 1000 isolated workers cannot negotiate "
      "their way out of a circular dependency after the fact.")
    A("")
    A("**Runtime obligations vs. static edges.** One dependency deliberately escapes the DAG: the "
      "safety gate `cap.t19.gate.action_filter@1`. Every effectful part in T12/T13/T15/T20 must "
      "route its side effects through it, but as a **call-time** obligation with **fail-closed** "
      "semantics (no gate ⇒ refuse the effect, OmegaCode 6001), not as a static import edge — which "
      "would introduce a back-edge from those tiers into T19 and make the graph cyclic. Safety is "
      "enforced without sacrificing acyclicity.")
    A("")

    # ---------------- 5. preamble ----------------
    A("## 5. PREAMBLE-Z")
    A("")
    A("Every one of the 1000 prompts is dispatched as **PREAMBLE-Z + the part's own prompt**. "
      "PREAMBLE-Z is identical for all workers; it is what makes the 1000 outputs mutually "
      "compatible. (The files in [`prompts/`](prompts) already have it inlined, so each `.txt` there "
      "is dispatchable as-is.)")
    A("")
    A("```text")
    A(_preamble_z())
    A("```")
    A("")

    # ---------------- 6. tiers ----------------
    A("## 6. The 20 tiers")
    A("")
    A("| tier | title | lang | parts | lines | benchmarks owned | depends on |")
    A("|---|---|---|---:|---:|---|---|")
    for tid, slug, title, lang, ext, mission, bench, deps in C.TIERS:
        A(f"| [{tid}](#{tid.lower()}) | {title} | {lang} | 50 | 250,000 | "
          f"{', '.join(bench) or '—'} | {', '.join(deps) or '—'} |")
    A("| | **total** | | **1000** | **5,000,000** | | |")
    A("")
    A("Tier dependencies are *capability* dependencies, never file dependencies. A tier may be built "
      "before the tier it depends on: the dependent parts simply run in declared-degraded mode until "
      "the provider appears on the bus.")
    A("")
    for tid, slug, title, lang, ext, mission, bench, deps in C.TIERS:
        A(f"<a id=\"{tid.lower()}\"></a>**{tid} — {title}** ({lang}). {mission} "
          f"Accountable for: {', '.join(bench) or 'infrastructure only'}. "
          f"Depends on: {', '.join(deps) or 'nothing'}. "
          f"Specs: [`docs/PART_SPECS_{tid}.md`](docs/PART_SPECS_{tid}.md) · "
          f"Prompts: [`docs/PROMPTS_{tid}.md`](docs/PROMPTS_{tid}.md)")
        A("")

    # ---------------- 7. loc map ----------------
    A("## 7. Per-part line-count map")
    A("")
    A("Every part is ~5000 lines, and the 5000 is *specified*, not hoped for. Each worker receives "
      "this map with its own part's feature names substituted in, which is how 1000 independent "
      "workers produce files of comparable depth. Example instantiation (P0001):")
    A("")
    A("| # | section | lines |")
    A("|---:|---|---:|")
    rows = loc_map(parts[0])
    for i, (name, n, _why) in enumerate(rows, start=1):
        A(f"| {i} | {name} | {n} |")
    A(f"| | **total** | **{sum(r[1] for r in rows)}** |")
    A("")
    A("Roughly 21 % of every file is tests (in-file unit + property + fuzz), 6 % is documentation "
      "and 4 % is the degradation ladder. That ratio is deliberate: an isolated worker cannot be "
      "code-reviewed by its peers, so the file has to review itself.")
    A("")

    # ---------------- 8. dispatch ----------------
    A("## 8. How to dispatch the 1000 workers")
    A("")
    A("```bash")
    A("# each of the 1000 machines runs exactly one of these, in any order, at any time")
    A("claude -p \"$(cat prompts/P0001_abi_types.txt)\"   > out/P0001_abi_types.py")
    A("claude -p \"$(cat prompts/P0002_abi_errors.txt)\"  > out/P0002_abi_errors.py")
    A("# ... 1000 total; no machine needs any file produced by another machine")
    A("```")
    A("")
    A("Properties this gives you:")
    A("")
    A("- **No ordering constraint.** Any part can be built first. A part whose dependencies do not "
      "exist yet still passes its own `selftest()` in degraded mode.")
    A("- **No shared state.** A worker reads only its own prompt. It writes only its own file.")
    A("- **Idempotent re-dispatch.** If a file is rejected, re-run only that one prompt; nothing "
      "else is invalidated, because nothing else depended on its internals.")
    A("- **Parallel to 1000×.** Wall-clock time for the whole build is the time of the slowest "
      "single part.")
    A("")

    # ---------------- 9. assembly ----------------
    A("<a id=\"9-assembly-and-verification\"></a>")
    A("## 9. Assembly and verification")
    A("")
    A("Collection is a one-way gather — each machine uploads its single file; no machine ever needs "
      "to download another's. `tools/validate_assembly.py` then checks, on the gathered tree:")
    A("")
    A("1. **Contract identity** — the contract block in all 1000 headers hashes to one value.")
    A("2. **Manifest agreement** — each file's `PART_MANIFEST` matches "
      "[`manifest/parts.json`](manifest/parts.json) field-for-field.")
    A("3. **Capability closure** — every `requires` URI is provided by exactly one part "
      "([`manifest/capabilities.json`](manifest/capabilities.json)); no duplicates, no orphans.")
    A("4. **Acyclicity** — the capability graph is a DAG; a cycle is a build failure.")
    A("5. **Isolation** — no file imports any `parts/**` module (static scan). This is the check "
      "that enforces the no-shared-folder design.")
    A("6. **Self-test sweep** — all 1000 `selftest()`s pass standalone *and* on the assembled bus.")
    A("7. **Latency roll-up** — the sum of p99 budgets along each critical path meets the §3 target.")
    A("8. **Line budget** — every file within ±3 % of 5000 lines.")
    A("")

    # ---------------- 10. all parts ----------------
    A("## 10. All 1000 parts")
    A("")
    A("For every part: a detailed description (mission, tier accountability, four mandated "
      "mechanisms, required capabilities and their fallbacks, determinism class, latency budget, "
      "line budget) and its **prompt**, inline in a collapsible block. Fuller versions: "
      "[`docs/PART_SPECS_Txx.md`](docs) for specs, [`prompts/*.txt`](prompts) for the "
      "self-contained dispatchable prompts.")
    A("")
    for tid, slug, title, lang, ext, mission, bench, deps in C.TIERS:
        tparts = by_tier[tid]
        A(f"### {tid} — {title}")
        A("")
        A(f"*{mission}* &nbsp;·&nbsp; {lang} &nbsp;·&nbsp; parts "
          f"{tparts[0]['part_id']}–{tparts[-1]['part_id']} &nbsp;·&nbsp; 250,000 lines")
        A("")
        A("| part | title | capability | det. | p99 ns | spec | prompt |")
        A("|---|---|---|---|---:|---|---|")
        for p in tparts:
            A(f"| [{p['part_id']}](#{anchor(p)}) | {p['title']} | `{p['capability']}` | "
              f"{p['determinism']} | {p['latency_ns']} | [spec]({spec_link(p)}) | "
              f"[txt]({prompt_file(p)}) |")
        A("")
        for p in tparts:
            A(render_part_block(p, loc_map(p)))
        A("---")
        A("")

    # ---------------- 11. layout ----------------
    A("## 11. Repository layout")
    A("")
    A("```text")
    A("README.md                     this file: architecture + all 1000 descriptions + prompts")
    A("docs/PART_SPECS_T01..T20.md   1000 detailed part specifications (50 per file)")
    A("docs/PROMPTS_T01..T20.md      1000 worker prompts, grouped by tier")
    A("prompts/P0001..P1000_*.txt    1000 self-contained dispatchable prompts (contract inlined)")
    A("manifest/parts.json           machine-readable record of all 1000 parts")
    A("manifest/capabilities.json    capability -> provider / consumers graph")
    A("tools/contracts.py            frozen constants: contract, benchmarks, speed law, tiers")
    A("tools/catalog/t01..t20.py     the 1000-part catalogue (50 per tier)")
    A("tools/generate.py             regenerates every artefact in this repository")
    A("tools/render*.py              renderers")
    A("tools/validate_assembly.py    post-gather verification of the 1000 files")
    A("parts/<tier_slug>/            where the 1000 gathered worker outputs land")
    A("```")
    A("")
    A("Everything except `parts/` is generated: `python3 tools/generate.py`.")
    A("")

    # ---------------- 12. limitations ----------------
    A("## 12. Honest limitations")
    A("")
    A("This repository is a **complete, executable build plan** — the frozen interface, the 1000 "
      "specifications, the 1000 prompts and the verification harness. It is not a trained model, and "
      "it does not claim the benchmark numbers in §2 have been achieved; those are *targets* that the "
      "T18 harness is designed to adjudicate honestly, including by reporting failure.")
    A("")
    A("Specific caveats, stated plainly:")
    A("")
    A(f"- Rows marked `est` in §2 are derived estimates, not measured values. They are labelled so "
      f"they are never mistaken for published results.")
    A("- The ×%.1f product in §3 is an engineering **budget**, not a measurement. It is assembled "
      "from six mechanisms with individually plausible factors, but multiplicative composition of "
      "speed-ups is optimistic by nature: memory bandwidth, acceptance-rate collapse under "
      "distribution shift, and scheduler overhead all erode it. That is precisely why the budget is "
      "×%.1f rather than ×100 — roughly 3.3× of deliberate headroom. The per-part p99 budgets exist "
      "so the erosion is measured rather than assumed, and it is entirely possible that the realised "
      "figure lands below 100× on some workloads." % (speed_product(), speed_product()))
    A("- \"Beats it on every benchmark under any methodology\" is an unfalsifiable claim in the "
      "general case — a sufficiently adversarial harness can be constructed against any system. What "
      "is actually enforceable, and what §2 enforces, is dominance on the tracked set under "
      "published, re-runnable harnesses with the worst-of-5 rule.")
    A("- ~5,000,000 lines produced by 1000 non-communicating workers will contain semantic "
      "duplication and inconsistent internal taste. The contract guarantees *link* compatibility, "
      "not conceptual elegance.")
    A("- Compute, data and training-time requirements for the T17 tier are out of scope here.")
    A("")
    A(f"---")
    A("")
    A(f"*Generated by `tools/generate.py` · Ω-CONTRACT v{C.CONTRACT_VERSION} · "
      f"baseline researched {C.RESEARCH_DATE}.*")
    return "\n".join(L)


def render_index(parts: list[dict]) -> str:
    """Small, GitHub-renderable index of all 1000 parts."""
    L: list[str] = []
    A = L.append
    by_tier: dict[str, list[dict]] = {}
    for p in parts:
        by_tier.setdefault(p["tier"], []).append(p)
    A(f"# {C.PROJECT} — index of all 1000 parts")
    A("")
    A("A light, always-renderable index. The full architecture, the Opus 5 baseline, the 100× speed "
      "law, the Ω-Contract and the inline prompts live in [`README.md`](README.md).")
    A("")
    A(f"1000 parts · 20 tiers · ~5,000,000 lines · Ω-CONTRACT v{C.CONTRACT_VERSION}")
    A("")
    A("| tier | title | lang | parts | specs | prompts |")
    A("|---|---|---|---|---|---|")
    for tid, slug, title, lang, ext, mission, bench, deps in C.TIERS:
        tp = by_tier[tid]
        A(f"| {tid} | {title} | {lang} | {tp[0]['part_id']}–{tp[-1]['part_id']} | "
          f"[specs](docs/PART_SPECS_{tid}.md) | [prompts](docs/PROMPTS_{tid}.md) |")
    A("")
    for tid, slug, title, lang, ext, mission, bench, deps in C.TIERS:
        A(f"## {tid} — {title}")
        A("")
        A(f"*{mission}*")
        A("")
        A("| part | slug | title | capability | det | p99 ns | spec | prompt |")
        A("|---|---|---|---|---|---:|---|---|")
        for p in by_tier[tid]:
            A(f"| {p['part_id']} | `{p['slug']}` | {p['title']} | `{p['capability']}` | "
              f"{p['determinism']} | {p['latency_ns']} | "
              f"[spec]({spec_link(p)}) | [txt]({prompt_file(p)}) |")
        A("")
    return "\n".join(L)


def _preamble_z() -> str:
    L: list[str] = []
    A = L.append
    A("PREAMBLE-Z  (identical for all 1000 workers; prepend to every part prompt)")
    A("=========================================================================")
    A("")
    A(f"You are one of 1000 Claude Opus 5 instances building {C.PROJECT_ASCII}: a general AI that")
    A("must beat Claude Opus 5 on every benchmark and run 100x faster at everything.")
    A("")
    A("You run on your own machine. There is NO shared folder. You cannot read any file written")
    A("by another worker, you cannot ask anyone a question, and you get exactly one attempt.")
    A("Everything required is in this preamble plus your part prompt.")
    A("")
    A("THE FOUR RULES THAT MAKE 1000 ISOLATED FILES LINK")
    A("  1. Copy the Ω-CONTRACT below verbatim into your file header.")
    A("  2. Never import, read, or guess another parts/** file. Depend only on capability URIs.")
    A("  3. Every capability you require MUST have a working in-file fallback, because the")
    A("     provider may not exist. Record any degradation in describe()['degraded'].")
    A("  4. Export exactly: PART_MANIFEST, register(bus), selftest(), microbench(iters),")
    A("     describe(). The assembler looks for these names and nothing else.")
    A("")
    A("LINE MAP (instantiated with your part's four features; total 5000 lines)")
    A("   1. [ 180] Header + Ω-CONTRACT verbatim + PART_MANIFEST")
    A("   2. [ 320] Public types, schemas, constants owned by this part")
    A("   3. [ 600] Core implementation A  (your feature 1)")
    A("   4. [ 580] Core implementation B  (your feature 2)")
    A("   5. [ 520] Core implementation C  (your feature 3)")
    A("   6. [ 480] Core implementation D  (your feature 4)")
    A("   7. [ 210] Ω-Bus integration: register(), describe(), capability handles")
    A("   8. [ 200] Degradation ladder: a fallback for EVERY required capability")
    A("   9. [ 250] Error paths, budget/deadline handling, partial results")
    A("  10. [ 150] Observability: events, counters, histograms, latency attribution")
    A("  11. [ 170] Determinism harness: split_seed, replay, batch-invariance")
    A("  12. [ 440] In-file test suite: >= 40 unit + boundary + regression cases")
    A("  13. [ 250] Property-based tests for every stated invariant")
    A("  14. [ 170] Adversarial / fuzz tests")
    A("  15. [ 180] Microbenchmark + p99 latency-budget assertion")
    A("  16. [ 300] Documentation: usage, rationale, LIMITATIONS (honest), references")
    A("")
    A("OUTPUT: one fenced code block containing your complete file. No prose. No ellipses.")
    A("")
    A("Ω-CONTRACT v" + C.CONTRACT_VERSION + " (frozen — copy verbatim)")
    A("-" * 73)
    A(C.OMEGA_CONTRACT.strip())
    A("-" * 73)
    return "\n".join(L)
