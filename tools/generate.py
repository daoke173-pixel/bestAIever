#!/usr/bin/env python3
"""
HYPERION-Ω generator.

Reads tools/contracts.py + tools/catalog/t01..t20.py and emits:

  README.md                     - master index + full spec (the deliverable)
  docs/PART_SPECS_Txx.md        - 20 files, 50 detailed part specs each
  docs/PROMPTS_Txx.md           - 20 files, 50 full worker prompts each
  manifest/parts.json           - machine-readable manifest of all 1000 parts
  manifest/capabilities.json    - capability -> provider/consumer graph
  tools/validate_assembly.py is separate.

Run:  python3 tools/generate.py
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import contracts as C  # noqa: E402
import render as R  # noqa: E402
import render_readme as RR  # noqa: E402


def load_catalog() -> dict[str, list]:
    out: dict[str, list] = {}
    for i in range(1, 21):
        tid = f"T{i:02d}"
        path = ROOT / "tools" / "catalog" / f"t{i:02d}.py"
        spec = importlib.util.spec_from_file_location(f"cat_t{i:02d}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if len(mod.PARTS) != 50:
            raise SystemExit(f"{tid}: expected 50 parts, got {len(mod.PARTS)}")
        out[tid] = mod.PARTS
    return out


# --------------------------------------------------------------------------
# Part record construction
# --------------------------------------------------------------------------
GATE_CAP = "cap.t19.gate.action_filter@1"

# Parts whose effects must pass the safety gate. The gate is NOT a static link-time
# dependency: the Ω-Bus interposes it on every effectful call (contract clause C8).
# Modelling it as a static edge would create a back-edge from T12/T13/T15 into T19 and
# make the graph cyclic, so it is declared as a `late_requires` runtime obligation with
# fail-closed semantics instead. This is an architectural decision, not a workaround:
# a part must refuse the effect if the gate is absent, which is exactly a runtime check.
GATED_TIERS = ("T12", "T13", "T15", "T20")


def _cap_for(tid: str, pslug: str) -> str:
    domain = pslug.split("_")[0][:14]
    return f"cap.{tid.lower()}.{domain}.{pslug}@1"


def build_parts(catalog: dict[str, list]) -> list[dict]:
    # ---- pass 1: assign identities and capability ownership -------------
    skeleton: list[dict] = []
    n = 0
    for tier in C.TIERS:
        tid, slug, title, lang, ext, mission, bench, deps = tier
        for idx, (pslug, ptitle, pmission, pfeatures) in enumerate(catalog[tid], start=1):
            n += 1
            skeleton.append(
                dict(seq=n, part_id=f"P{n:04d}", tier=tier, index_in_tier=idx, slug=pslug,
                     title=ptitle, mission=pmission, features=pfeatures,
                     capability=_cap_for(tid, pslug))
            )
    owner_seq: dict[str, int] = {s["capability"]: s["seq"] for s in skeleton}

    # ---- pass 2: build requires under the DAG invariant -----------------
    # INVARIANT: a part may only statically require a capability owned by a
    # strictly LOWER-numbered part. This makes the 1000-part capability graph a
    # DAG by construction, which is what lets 1000 isolated workers be assembled
    # in any order without a cycle ever appearing at link time.
    parts: list[dict] = []
    base = [
        "cap.t01.abi.abi_types@1",
        "cap.t01.abi.abi_errors@1",
        "cap.t01.omega.omega_bus_core@1",
    ]
    for s in skeleton:
        tid, slug, title, lang, ext, mission, bench, deps = s["tier"]
        seq, idx, pslug, cap = s["seq"], s["index_in_tier"], s["slug"], s["capability"]

        def admit(rcap: str, acc: list[str]) -> None:
            """Add rcap only if it keeps the graph acyclic."""
            if rcap == cap or rcap in acc:
                return
            osq = owner_seq.get(rcap)
            if osq is None or osq >= seq:
                return
            acc.append(rcap)

        requires: list[str] = []
        for b in base:
            admit(b, requires)
        if idx > 1:  # intra-tier spine
            admit(_cap_for(tid, catalog[tid][idx - 2][0]), requires)
        for dep_tid in deps:  # one stable representative per declared tier dep
            admit(_cap_for(dep_tid, catalog[dep_tid][(idx * 7 + 13) % 50][0]), requires)

        # Bootstrap parts (the lowest-numbered ones) legitimately have no
        # dependencies at all - they ARE the foundation everything else stands on.
        late_requires = (
            [GATE_CAP] if tid in GATED_TIERS and pslug != "action_filter_gate" else []
        )

        provides = [cap, f"{cap[:-2]}.describe@1"]
        if tid == "T19" and pslug == "action_filter_gate":
            # canonical, contract-fixed alias so gated workers can name the gate
            # without ever seeing T19's catalogue
            provides.append(GATE_CAP)

        det = "pure"
        if tid in ("T04", "T08", "T09", "T13", "T17", "T20"):
            det = "io"
        elif tid in ("T06", "T10", "T14", "T15", "T18"):
            det = "seeded"

        parts.append(
            dict(
                part_id=s["part_id"],
                seq=seq,
                tier=tid,
                tier_title=title,
                tier_slug=slug,
                tier_mission=mission,
                tier_bench=bench,
                tier_deps=deps,
                index_in_tier=idx,
                slug=pslug,
                title=s["title"],
                mission=s["mission"],
                features=s["features"],
                lang=lang,
                ext=ext,
                module=f"hyperion.{tid.lower()}.{slug.split('_',1)[1]}.{pslug}",
                file=f"parts/{slug}/{s['part_id']}_{pslug}.{ext}",
                capability=cap,
                provides=provides,
                requires=requires,
                late_requires=late_requires,
                determinism=det,
                latency_ns=1000 * ((seq % 47) + 3),  # 3us..49us, deterministic spread
                loc_target=5000,
            )
        )
    if len(parts) != 1000:
        raise SystemExit(f"expected 1000 parts, built {len(parts)}")
    return parts


# --------------------------------------------------------------------------
# LOC budget: every part must be ~5000 lines. We give an explicit map.
# --------------------------------------------------------------------------
def loc_map(p: dict) -> list[tuple[str, int, str]]:
    return [
        ("Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST", 180,
         "Contract digest line, mission, provides/requires, LOC map, revision notes."),
        ("Public types, schemas and constants owned by this part", 320,
         "Every type this part publishes, fully documented, with invariants stated."),
        (f"Core implementation A - {p['features'][0][:64]}", 600,
         "Primary algorithm. No TODOs, no placeholders, no stubbed branches."),
        (f"Core implementation B - {p['features'][1][:64]}", 580,
         "Second required mechanism, fully independent of A's internals."),
        (f"Core implementation C - {p['features'][2][:64]}", 520,
         "Third required mechanism."),
        (f"Core implementation D - {p['features'][3][:64]}", 480,
         "Fourth required mechanism, including its measurement/assertion path."),
        ("Ω-Bus integration: register(), describe(), capability handles", 210,
         "Idempotent registration, schema export, handle lifetime and teardown."),
        ("Degradation ladder: declared fallbacks for every required capability", 200,
         "For each entry in `requires`, a working local fallback + quality annotation."),
        ("Error paths, budget/deadline handling, partial results", 250,
         "Every OmegaCode this part can emit, with remedy text and retryability."),
        ("Observability: events, counters, histograms, latency attribution", 150,
         "Structured events only; no stdout. Counters registered through T20 telemetry."),
        ("Determinism harness: split_seed usage, replay, batch-invariance", 170,
         "Proves the declared determinism class holds."),
        ("In-file test suite: >= 40 cases (unit + boundary + regression)", 440,
         "pytest/cfg(test)/vitest style per language, no shared fixtures, offline."),
        ("Property-based tests for every stated invariant", 250,
         "Generators + shrinkers; each invariant named in a comment."),
        ("Adversarial / fuzz tests", 170,
         "Coverage-guided in-process fuzzing within the 60s budget."),
        ("Microbenchmark + latency-budget assertion", 180,
         f"Asserts p99 <= {p['latency_ns']} ns at the declared reference shape."),
        ("Documentation block: usage, rationale, limitations, references", 300,
         "Honest limitations section is mandatory; no overstated claims."),
    ]


def total_loc(p: dict) -> int:
    return sum(x[1] for x in loc_map(p))


def build_capability_graph(parts: list[dict]) -> dict:
    providers: dict[str, list[str]] = {}
    consumers: dict[str, list[str]] = {}
    for p in parts:
        for c in p["provides"]:
            providers.setdefault(c, []).append(p["part_id"])
        for c in p["requires"]:
            consumers.setdefault(c, []).append(p["part_id"])
    caps = sorted(set(providers) | set(consumers))
    graph = {
        "contract_version": C.CONTRACT_VERSION,
        "capability_count": len(caps),
        "unprovided": sorted(c for c in consumers if c not in providers),
        "duplicate_providers": {c: v for c, v in providers.items() if len(v) > 1},
        "capabilities": {
            c: {
                "providers": sorted(providers.get(c, [])),
                "consumers": sorted(consumers.get(c, [])),
                "fan_in": len(consumers.get(c, [])),
            }
            for c in caps
        },
    }
    return graph


def main() -> None:
    catalog = load_catalog()
    parts = build_parts(catalog)
    loc = total_loc(parts[0])
    print(f"built {len(parts)} parts; LOC/part = {loc}")
    if loc != 5000:
        raise SystemExit(f"line map must sum to 5000, got {loc}")

    for d in ("manifest", "docs", "prompts"):
        (ROOT / d).mkdir(exist_ok=True)

    # ---- manifests ----
    (ROOT / "manifest" / "parts.json").write_text(
        json.dumps(parts, indent=1, ensure_ascii=False), encoding="utf-8"
    )
    graph = build_capability_graph(parts)
    (ROOT / "manifest" / "capabilities.json").write_text(
        json.dumps(graph, indent=1, ensure_ascii=False), encoding="utf-8"
    )
    print(f"wrote manifest/parts.json + manifest/capabilities.json "
          f"({graph['capability_count']} caps, "
          f"{len(graph['unprovided'])} unprovided, "
          f"{len(graph['duplicate_providers'])} dup providers)")

    by_tier: dict[str, list[dict]] = {}
    for p in parts:
        by_tier.setdefault(p["tier"], []).append(p)

    # ---- specs + tier prompt docs ----
    n_specs = n_prompts = 0
    for tier in C.TIERS:
        tid = tier[0]
        tparts = by_tier[tid]
        (ROOT / "docs" / f"PART_SPECS_{tid}.md").write_text(
            R.render_spec_file(tier, tparts, loc_map), encoding="utf-8"
        )
        (ROOT / "docs" / f"PROMPTS_{tid}.md").write_text(
            R.render_prompt_file(tier, tparts, loc_map), encoding="utf-8"
        )
        n_specs += len(tparts)
        n_prompts += len(tparts)
    print(f"wrote docs/PART_SPECS_T01..T20.md ({n_specs} specs)")
    print(f"wrote docs/PROMPTS_T01..T20.md ({n_prompts} prompts)")

    # ---- self-contained dispatchable prompts ----
    for p in parts:
        body = R.render_prompt_body(p, loc_map(p), inline_contract=True)
        (ROOT / "prompts" / f"{p['part_id']}_{p['slug']}.txt").write_text(
            body + "\n", encoding="utf-8"
        )
    print(f"wrote prompts/*.txt ({len(parts)} files)")

    # ---- README (the deliverable) ----
    readme = RR.render_readme(parts, loc_map)
    (ROOT / "README.md").write_text(readme + "\n", encoding="utf-8")
    print(f"wrote README.md ({len(readme):,} chars, "
          f"{readme.count(chr(10)) + 1:,} lines)")

    index = RR.render_index(parts)
    (ROOT / "INDEX.md").write_text(index + "\n", encoding="utf-8")
    print(f"wrote INDEX.md ({len(index):,} chars)")


if __name__ == "__main__":
    main()
