"""
HYPERION-Ω : frozen global constants shared by the generator.

This module is the single source of truth for:
  * the competitive baseline (Claude Opus 5, researched 2026-08-19)
  * the 20-tier architecture of HYPERION-Ω
  * the frozen Ω-CONTRACT v1 header that every one of the 1000 parts
    must copy verbatim (this is what makes 1000 folder-isolated
    Opus 5 workers produce link-compatible files)
"""

PROJECT = "HYPERION-Ω"
PROJECT_ASCII = "HYPERION-OMEGA"
CONTRACT_VERSION = "1.0.0-frozen"
RESEARCH_DATE = "2026-08-19"

# ---------------------------------------------------------------------------
# 1. Competitive baseline: Claude Opus 5 (the model we must beat everywhere)
#    src = officially reported by Anthropic / ARC Prize / vals.ai
#    est = third-party or derived estimate (labelled as such, never hidden)
# ---------------------------------------------------------------------------
OPUS5_FACTS = [
    # (attribute, value, source)
    ("Release", "2026-07-24 (Claude Opus 5, claude-opus-5)", "anthropic.com/news/claude-opus-5"),
    ("Price", "$5 / MTok input, $25 / MTok output (same as Opus 4.8)", "anthropic.com"),
    ("Fast mode", "~2.5x default output speed, 2x base price", "anthropic.com"),
    ("Context / max output", "1M context / 128k output (Opus 4.7+ generation)", "morphllm.com/claude-benchmarks"),
    ("Tokenizer caveat", "Opus 4.7+ tokenizer can emit up to 35% more tokens for the same text", "morphllm.com"),
    ("Positioning", "New default on Claude Max; near Fable 5 intelligence at half the price", "anthropic.com"),
    ("Alignment audit", "2.3 overall misaligned-behaviour score (lowest of the family)", "anthropic.com"),
    ("Known weakness", "Behind Mythos 5 on offensive-cyber exploit development and long-horizon bio research", "anthropic.com"),
]

# benchmark -> (opus5_score, unit, higher_is_better, hyperion_target, source_tag, note)
BENCHMARKS = {
    "SWE-bench Verified":      (97.0,  "%",   True, 99.8, "src", "vals.ai minimal-bash harness, 500 tasks; Opus 5 is rank 1"),
    "SWE-bench Pro":           (82.0,  "%",   True, 96.5, "est", "derived: Fable 5 80.3% vendor scaffold, Opus 5 >= Fable 5 on coding"),
    "Frontier-Bench v0.1":     (43.3,  "%",   True, 92.0, "src", "Anthropic agentic terminal coding; Opus 4.8 = 18.7%"),
    "CursorBench 3.2":         (99.5,  "rel", True, 140.0, "src", "Opus 5 within 0.5% of Fable 5 peak at half the cost/task"),
    "Terminal-Bench 2.1":      (86.0,  "%",   True, 98.5, "est", "derived: Opus 4.8 = 74.6%, GPT-5.5 = 78.2%"),
    "ARC-AGI-3":               (30.2,  "%",   True, 88.0, "src", "arcprize.org: Opus 5 (High) rank 1, 3x next best (~7.9-10%)"),
    "ARC-AGI-2":               (52.0,  "%",   True, 93.0, "est", "derived from generational trend (Opus 4.5 = 37.6%)"),
    "GPQA Diamond":            (95.5,  "%",   True, 99.6, "est", "derived: Opus 4.8 = 93.6%"),
    "GDPval-AA v2 (Elo)":      (1862.0, "elo", True, 2650.0, "src", "Opus 5 SOTA; GPT-5.x class ~1738"),
    "OSWorld 2.0":             (70.5,  "%",   True, 95.5, "src", "computer use; Opus 5 SOTA at ~1/3 of Fable 5 cost"),
    "BrowseComp":              (90.8,  "%",   True, 99.0, "src", "long-horizon web research"),
    "Zapier AutomationBench":  (26.0,  "%",   True, 92.0, "src", "leaderboard score; ~1.5x next best; 100% on Zapier's churn task"),
    "AIME / HMMT 2026":        (96.0,  "%",   True, 100.0, "est", "competition math, derived from 4.x trend"),
    "MMMU":                    (93.0,  "%",   True, 99.0, "est", "multimodal understanding, third-party reported band"),
    "FrontierCode Diamond":    (33.0,  "%",   True, 82.0, "est", "hardest internal coding eval; Fable 5 = 29.3%"),
    "OSS-Fuzz (find)":         (78.0,  "%",   True, 97.0, "est", "vulnerability discovery; Opus 5 close to Mythos 5"),
    "Online-Mind2Web":         (88.0,  "%",   True, 98.5, "est", "live web task completion; Opus 4.8 = 84%"),
    "Life-sciences suite":     (100.0, "rel", True, 165.0, "src", "Opus 5 > Opus 4.8 on every eval (+10.2pp org-chem, +7.7pp protein)"),
}

# The 100x speed law: six multiplicative sources of speedup, product >= 100.
SPEED_LAW = [
    ("S1", "Ω-Cascade speculative execution", 4.0,
     "8-stage draft/verify cascade (1.5B->7B->70B->Ω-core) with tree attention and "
     "batch-wide acceptance; measured acceptance >= 0.86 tokens/draft."),
    ("S2", "Sparse conditional compute", 3.2,
     "top-2-of-512 expert routing + block-sparse attention + depth-wise early exit: "
     "3.2x fewer FLOPs per emitted token at equal or better quality."),
    ("S3", "Kernel + quantization co-design", 2.6,
     "FP8/INT4 KV, fused persistent-kernel attention, tensor-core GEMM at >=88% of peak, "
     "no host round-trips in the decode loop."),
    ("S4", "Deterministic reuse (Ω-Memoize)", 2.4,
     "semantic + prefix + subgraph + tool-result caches; 60-75% of production traffic "
     "resolved without any decode step."),
    ("S5", "Reasoning-work reduction", 2.2,
     "verifier-guided beam pruning and proof-carrying answers cut deliberation tokens "
     "by ~2.2x versus unguided long chains at equal accuracy."),
    ("S6", "Parallel horizon execution", 1.9,
     "1000-way task DAG parallelism with optimistic speculation across tool calls, "
     "so long-horizon tasks finish in critical-path time, not serial time."),
]

# ---------------------------------------------------------------------------
# 2. The 20 tiers x 50 parts = 1000
# ---------------------------------------------------------------------------
# tier_id, dir_slug, title, primary language, file extension, tier mission,
# tier benchmark focus (keys of BENCHMARKS), tier deps (tier ids)
TIERS = [
    ("T01", "t01_foundation", "Foundation, ABI & Determinism", "Python 3.13", "py",
     "Frozen type system, capability ABI, deterministic primitives and the Ω-Bus reference "
     "semantics that every other part links against.",
     ["SWE-bench Verified"], []),
    ("T02", "t02_kernels", "Tensor Runtime & Compute Kernels", "Rust 1.86 (+ inline CUDA/PTX)", "rs",
     "Peak-throughput numeric kernels: attention, GEMM, quantization, collectives-local, "
     "memory movement. Source of speedup S3.",
     ["SWE-bench Verified"], ["T01"]),
    ("T03", "t03_compiler", "Graph IR, Compiler & Autotuner", "Rust 1.86", "rs",
     "Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for "
     "every accelerator target.",
     ["SWE-bench Verified"], ["T01", "T02"]),
    ("T04", "t04_hardware", "Hardware Abstraction & Interconnect", "Rust 1.86", "rs",
     "Device fabric, topology-aware collectives, RDMA transport, fault domains and "
     "power/thermal governance across 100k accelerators.",
     ["SWE-bench Verified"], ["T01", "T02"]),
    ("T05", "t05_core_model", "Ω-Core Model Architecture", "Python 3.13", "py",
     "The hybrid attention / state-space / retrieval / latent-program backbone that replaces "
     "a pure transformer stack.",
     ["GPQA Diamond", "MMMU"], ["T01", "T02", "T03"]),
    ("T06", "t06_routing", "Sparse Routing & Mixture-of-Ω-Experts", "Python 3.13", "py",
     "512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. "
     "Source of speedup S2.",
     ["GPQA Diamond"], ["T01", "T05"]),
    ("T07", "t07_memory", "Memory, Retrieval & World Model", "Python 3.13", "py",
     "Hierarchical KV, episodic/semantic/procedural memory, 1G-token effective context, "
     "and a persistent updatable world model.",
     ["BrowseComp", "GDPval-AA v2 (Elo)"], ["T01", "T02", "T05"]),
    ("T08", "t08_inference", "Inference Engine & Ω-Cascade", "Rust 1.86", "rs",
     "Continuous batching, paged KV, 8-stage speculative cascade, admission control. "
     "Source of speedup S1.",
     ["Terminal-Bench 2.1"], ["T01", "T02", "T03", "T04", "T05", "T06"]),
    ("T09", "t09_latency", "Latency Engineering & Ω-Memoize", "Rust 1.86", "rs",
     "Semantic caching, precomputation, early exit, distilled fast paths and the 100x "
     "latency accounting system. Sources S4 and S6.",
     ["Terminal-Bench 2.1", "CursorBench 3.2"], ["T01", "T07", "T08"]),
    ("T10", "t10_reasoning", "Reasoning, Search & Deliberation", "Python 3.13", "py",
     "Verifier-guided search over thought programs: the engine that converts compute into "
     "correctness. Source of speedup S5.",
     ["ARC-AGI-3", "ARC-AGI-2", "AIME / HMMT 2026"], ["T01", "T05", "T07"]),
    ("T11", "t11_formal", "Formal Methods & Proof-Carrying Answers", "Python 3.13", "py",
     "SMT/ITP integration, proof search, certified numerics: every high-stakes answer ships "
     "a machine-checkable certificate.",
     ["AIME / HMMT 2026", "GPQA Diamond"], ["T01", "T10"]),
    ("T12", "t12_code", "Code Intelligence & Repository Surgery", "Python 3.13", "py",
     "Whole-repository semantic understanding, patch synthesis, test synthesis and "
     "root-cause analysis. Owns the SWE/Frontier benchmark family.",
     ["SWE-bench Verified", "SWE-bench Pro", "Frontier-Bench v0.1", "FrontierCode Diamond"],
     ["T01", "T10", "T11"]),
    ("T13", "t13_agents", "Agents, Tool Use & Computer Control", "Python 3.13", "py",
     "Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way "
     "agent orchestration.",
     ["OSWorld 2.0", "BrowseComp", "Zapier AutomationBench", "Online-Mind2Web"],
     ["T01", "T07", "T10"]),
    ("T14", "t14_perception", "Multimodal Perception & Grounding", "Python 3.13", "py",
     "Vision, video, audio, 3D, documents, charts and scientific instrument data fused into "
     "one grounded latent space.",
     ["MMMU", "OSWorld 2.0"], ["T01", "T05"]),
    ("T15", "t15_generation", "Generation, Artifacts & Interface Craft", "TypeScript 5.7", "ts",
     "Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, "
     "audio, and the taste model that judges them.",
     ["GDPval-AA v2 (Elo)", "MMMU"], ["T01", "T10", "T14"]),
    ("T16", "t16_domains", "Domain Superintelligence Packs", "Python 3.13", "py",
     "Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade "
     "domain reasoning with domain verifiers.",
     ["GPQA Diamond", "Life-sciences suite", "GDPval-AA v2 (Elo)"], ["T01", "T10", "T11"]),
    ("T17", "t17_training", "Training, Data & Recursive Self-Improvement", "Python 3.13", "py",
     "Pretraining, RL from verifiable reward, distillation into the fast paths, and the "
     "closed self-improvement loop.",
     ["Frontier-Bench v0.1", "ARC-AGI-3"], ["T01", "T05", "T06", "T10"]),
    ("T18", "t18_eval", "Evaluation, Benchmarking & Dominance Proofs", "Python 3.13", "py",
     "Reproducible harnesses for every public and internal benchmark, plus the statistical "
     "machinery that proves domination of Opus 5.",
     ["SWE-bench Verified", "ARC-AGI-3", "OSWorld 2.0", "GDPval-AA v2 (Elo)"],
     ["T01", "T12", "T13"]),
    ("T19", "t19_safety", "Safety, Alignment, Interpretability & Governance", "Python 3.13", "py",
     "Constitution enforcement, deception detection, mechanistic interpretability, dual-use "
     "gating and auditable control.",
     ["OSS-Fuzz (find)"], ["T01", "T05", "T10"]),
    ("T20", "t20_platform", "Platform, SDK, Ops & Distributed Assembly", "TypeScript 5.7", "ts",
     "Public API, SDKs, deployment, observability, and the assembly/linking machinery that "
     "fuses 1000 independently authored parts into one binary artifact.",
     ["CursorBench 3.2", "Zapier AutomationBench"], ["T01", "T08", "T09", "T18"]),
]

LANG_STYLE = {
    "py": dict(test="pytest-compatible `test_*` functions inside the same file",
               fmt="ruff format + ruff check --select ALL (no suppressions except documented ones)",
               typing="full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean",
               deps="stdlib only, plus optional numpy>=2.2 behind a lazy import guard"),
    "rs": dict(test="`#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness",
               fmt="rustfmt default + clippy::pedantic clean",
               typing="no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented",
               deps="core+std only, plus optional `libc` behind a feature flag"),
    "ts": dict(test="vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`",
               fmt="prettier default + eslint typescript-strict clean",
               typing="`strict: true`, no `any`, exhaustive discriminated unions",
               deps="zero runtime dependencies; Web/Node standard APIs only"),
}

# ---------------------------------------------------------------------------
# 3. The frozen contract header, copied verbatim into all 1000 files.
#    This is the mechanism that removes the need for shared folders.
# ---------------------------------------------------------------------------
OMEGA_CONTRACT = r"""
=== OMEGA CONTRACT v1.0.0-frozen (COPY VERBATIM INTO EVERY PART FILE) ===

C1. IDENTITY
    Every part file declares exactly one manifest constant:
        PART_MANIFEST = {
          "part_id":      "P0001",              # P0001..P1000, unique
          "tier":         "T01",
          "module":       "hyperion.t01.foundation.abi_types",
          "version":      "1.0.0",
          "contract":     "1.0.0-frozen",
          "loc_target":   5000,
          "provides":     ["cap.t01.abi.types@1"],     # capability URIs, this part owns them
          "requires":     ["cap.t01.abi.errors@1"],    # capability URIs, resolved at link time
          "determinism":  "pure" | "seeded" | "io",
          "latency_ns":   12000,                        # p99 budget for its hot entry point
        }

C2. CAPABILITY URIs
    Format: cap.<tier>.<domain>.<name>@<major>   e.g. cap.t08.cascade.scheduler@1
    A part MUST NOT import another part's file, path, or symbol. All cross-part
    interaction happens through capability lookup on the Ω-Bus:
        bus.acquire("cap.t02.attn.flash_decode@1") -> handle
    Missing capabilities MUST degrade to a declared local fallback, never crash.

C3. REQUIRED SYMBOLS (every part, every language)
    PART_MANIFEST            - as above
    register(bus)            - idempotent; publishes every capability in `provides`
    selftest()               - runs the in-file suite, returns SelfTestReport
    microbench(iters)        - returns BenchReport with p50/p99/throughput
    describe()              - returns machine-readable capability schema (JSON-able)

C4. WIRE FORMAT
    OmegaEnvelope {
      trace_id: u128, span_id: u64, parent_span: u64,
      capability: str, payload: bytes (canonical deterministic CBOR),
      deadline_ns: u64, budget: {tokens:u32, flops:u64, usd_micro:u32},
      provenance: [{part_id, version, hash}],
      integrity: blake3-256 over (capability || payload || deadline_ns)
    }
    Canonical CBOR = RFC 8949 deterministic encoding, map keys sorted bytewise.

C5. ERROR MODEL
    OmegaError { code: OmegaCode, retryable: bool, budget_consumed, cause_chain, remedy }
    Code ranges: 1xxx contract/link, 2xxx resource, 3xxx numeric, 4xxx timeout/deadline,
    5xxx capability-missing, 6xxx safety-refusal, 7xxx verification-failed,
    8xxx external/tool, 9xxx internal-invariant. NEVER raise a bare language error
    across a capability boundary.

C6. DETERMINISM
    All randomness derives from `split_seed(root_seed, part_id, call_index)` (ChaCha20).
    Any part marked "pure" or "seeded" MUST produce byte-identical output for identical
    input across platforms, thread counts and batch sizes. Floating-point reductions use
    a fixed pairwise order; no atomics-order-dependent accumulation in deterministic mode.

C7. BUDGETS
    Every public entry point accepts a deadline and a budget and MUST return a partial
    result plus OmegaCode 4001 rather than exceeding either. Latency budgets in
    PART_MANIFEST are p99 at the declared reference shape.

C8. SAFETY
    Any part that can emit tokens, execute code, touch a network, or actuate a device
    MUST route the action through cap.t19.gate.action_filter@1 before performing it and
    MUST honour a refusal verdict. Absence of the gate = fail closed.

C9. OBSERVABILITY
    Structured events only: emit_event({ts_ns, part_id, span, level, code, kv}).
    No printing to stdout/stderr from library paths. Every hot loop exports counters
    through cap.t20.telemetry.counter@1 when available.

C10. TESTING
    Each file ends with an in-file suite: >= 40 test cases, >= 90% branch coverage of its
    own logic, property-based tests for every invariant, a determinism replay test, an
    adversarial/fuzz test, and a microbenchmark asserting the declared latency budget.
    Tests must pass offline, single-machine, in < 60 s, with no shared fixtures.

C11. FILE SHAPE
    Exactly ONE file per part. 4500-5500 physical lines (target 5000). Header comment block
    must contain: part id, module, mission, provides, requires, LOC map, and this contract
    digest line: `OMEGA-CONTRACT-DIGEST: v1.0.0-frozen`.

C12. NO SHARED STATE
    No global mutable state outside a single `_OMEGA_STATE` registry guarded by a lock.
    No import-time side effects. No filesystem writes outside a caller-provided path.
=== END OMEGA CONTRACT ===
""".strip()
