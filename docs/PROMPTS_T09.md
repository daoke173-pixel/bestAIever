# HYPERION-Ω — Worker prompts · T09 · Latency Engineering & Ω-Memoize

> 50 prompts · one per part · language Rust 1.86 · Ω-CONTRACT v1.0.0-frozen

Each prompt is self-contained *except* for the contract, which is **BLOCK A** below. Prepend BLOCK A verbatim when dispatching a prompt, or use the fully inlined single-file version in [`prompts/`](../prompts) — those `.txt` files already contain it.

## BLOCK A — Ω-CONTRACT v1.0.0-frozen (verbatim, frozen)

````text
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
````

---

## PROMPT p0401-latency-accounting

**P0401 · `latency_accounting` — End-to-End Latency Accounting Framework** · [spec](PART_SPECS_T09.md#p0401-latency-accounting) · [self-contained txt](../prompts/P0401_latency_accounting.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0401  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0401 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0401  (1/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : End-to-End Latency Accounting Framework
file         : parts/t09_latency/P0401_latency_accounting.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.latency_accounting
language     : Rust 1.86
capability   : cap.t09.latency.latency_accounting@1
determinism  : io
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The measurement system that makes the 100x claim auditable.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. phase decomposition with nanosecond attribution and no double counting
  2. critical-path extraction from the span tree
  3. per-part latency attribution across all 1000 parts
  4. accounting-completeness verification (sum equals wall clock)

Expanded obligations:
  1. Implement phase decomposition with nanosecond attribution and no double
     counting, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement critical-path extraction from the span tree with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement per-part latency attribution across all 1000 parts together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement accounting-completeness verification (sum equals wall clock)
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.latency.latency_accounting@1
  cap.t09.latency.latency_accounting.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.string.string_interning@1
      if unavailable: use the in-file conservative substitute for
      `string_interning` (documented, slower, lower quality) and set
      `degraded['string_interning']='local'`

  cap.t07.freshness.freshness_manager@1
      if unavailable: use the in-file conservative substitute for
      `freshness_manager` (documented, slower, lower quality) and set
      `degraded['freshness_manager']='local'`

  cap.t08.stop.stop_conditions@1
      if unavailable: use the in-file conservative substitute for
      `stop_conditions` (documented, slower, lower quality) and set
      `degraded['stop_conditions']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - phase decomposition with nanosecond attribution and no double co
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - critical-path extraction from the span tree
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-part latency attribution across all 1000 parts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accounting-completeness verification (sum equals wall clock)
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 28000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.latency.latency_accounting@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 28000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0401_latency_accounting.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0402-speed-law-model

**P0402 · `speed_law_model` — The 100x Speed Law Model** · [spec](PART_SPECS_T09.md#p0402-speed-law-model) · [self-contained txt](../prompts/P0402_speed_law_model.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0402  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0402 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0402  (2/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : The 100x Speed Law Model
file         : parts/t09_latency/P0402_speed_law_model.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.speed_law_model
language     : Rust 1.86
capability   : cap.t09.speed.speed_law_model@1
determinism  : io
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Formalises S1..S6 multiplicativity and proves the product exceeds 100.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. formal model of each speedup source with measured inputs
  2. interaction/overlap correction so factors are not double counted
  3. confidence intervals and sensitivity analysis
  4. auditable derivation report with reproducible measurements

Expanded obligations:
  1. Implement formal model of each speedup source with measured inputs with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement interaction/overlap correction so factors are not double
     counted together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's CursorBench 3.2
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement confidence intervals and sensitivity analysis as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement auditable derivation report with reproducible measurements,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     CursorBench 3.2 — a regression on that benchmark is an automatic
     rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.speed.speed_law_model@1
  cap.t09.speed.speed_law_model.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.latency.latency_accounting@1
      if unavailable: use the in-file conservative substitute for
      `latency_accounting` (documented, slower, lower quality) and set
      `degraded['latency_accounting']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t07.attention.attention_sink@1
      if unavailable: use the in-file conservative substitute for
      `attention_sink` (documented, slower, lower quality) and set
      `degraded['attention_sink']='local'`

  cap.t08.adapter.adapter_serving@1
      if unavailable: use the in-file conservative substitute for
      `adapter_serving` (documented, slower, lower quality) and set
      `degraded['adapter_serving']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - formal model of each speedup source with measured inputs
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - interaction/overlap correction so factors are not double counted
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - confidence intervals and sensitivity analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - auditable derivation report with reproducible measurements
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 29000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.speed.speed_law_model@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 29000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0402_speed_law_model.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0403-memoize-core

**P0403 · `memoize_core` — Ω-Memoize Core Engine** · [spec](PART_SPECS_T09.md#p0403-memoize-core) · [self-contained txt](../prompts/P0403_memoize_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0403  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0403 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0403  (3/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Ω-Memoize Core Engine
file         : parts/t09_latency/P0403_memoize_core.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.memoize_core
language     : Rust 1.86
capability   : cap.t09.memoize.memoize_core@1
determinism  : io
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The unified reuse layer: 60-75% of traffic answered without decoding (S4).

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-level cache hierarchy (exact, prefix, semantic, subgraph, tool)
  2. unified lookup with cost-ordered probing
  3. correctness conditions per level with enforcement
  4. measured overall reuse rate on production-shaped traffic

Expanded obligations:
  1. Implement multi-level cache hierarchy (exact, prefix, semantic,
     subgraph, tool) together with its verification path, so that anything
     this mechanism produces can be independently re-checked *inside this
     same file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's CursorBench 3.2
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  2. Implement unified lookup with cost-ordered probing as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement correctness conditions per level with enforcement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured overall reuse rate on production-shaped traffic with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.memoize.memoize_core@1
  cap.t09.memoize.memoize_core.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.speed.speed_law_model@1
      if unavailable: use the in-file conservative substitute for
      `speed_law_model` (documented, slower, lower quality) and set
      `degraded['speed_law_model']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t07.persistence.persistence_layer@1
      if unavailable: use the in-file conservative substitute for
      `persistence_layer` (documented, slower, lower quality) and set
      `degraded['persistence_layer']='local'`

  cap.t08.engine.engine_telemetry@1
      if unavailable: use the in-file conservative substitute for
      `engine_telemetry` (documented, slower, lower quality) and set
      `degraded['engine_telemetry']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - multi-level cache hierarchy (exact, prefix, semantic, subgraph, 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - unified lookup with cost-ordered probing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - correctness conditions per level with enforcement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured overall reuse rate on production-shaped traffic
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 30000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.memoize.memoize_core@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 30000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0403_memoize_core.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0404-exact-cache

**P0404 · `exact_cache` — Exact-Match Response Cache** · [spec](PART_SPECS_T09.md#p0404-exact-cache) · [self-contained txt](../prompts/P0404_exact_cache.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0404  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0404 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0404  (4/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Exact-Match Response Cache
file         : parts/t09_latency/P0404_exact_cache.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.exact_cache
language     : Rust 1.86
capability   : cap.t09.exact.exact_cache@1
determinism  : io
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Byte-identical requests answered in microseconds.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. canonical request normalisation and hashing
  2. scope/permission-aware key composition
  3. invalidation on model, knowledge and policy changes
  4. hit-rate and latency measurement

Expanded obligations:
  1. Implement canonical request normalisation and hashing as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement scope/permission-aware key composition, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement invalidation on model, knowledge and policy changes with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement hit-rate and latency measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.exact.exact_cache@1
  cap.t09.exact.exact_cache.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.memoize.memoize_core@1
      if unavailable: use the in-file conservative substitute for
      `memoize_core` (documented, slower, lower quality) and set
      `degraded['memoize_core']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t07.index.index_build_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `index_build_pipeline` (documented, slower, lower quality) and set
      `degraded['index_build_pipeline']='local'`

  cap.t08.api.api_gateway_runtime@1
      if unavailable: use the in-file conservative substitute for
      `api_gateway_runtime` (documented, slower, lower quality) and set
      `degraded['api_gateway_runtime']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - canonical request normalisation and hashing
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - scope/permission-aware key composition
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - invalidation on model, knowledge and policy changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - hit-rate and latency measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 31000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.exact.exact_cache@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 31000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0404_exact_cache.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0405-similarity-cache

**P0405 · `similarity_cache` — Approximate Semantic Cache with Safety Gates** · [spec](PART_SPECS_T09.md#p0405-similarity-cache) · [self-contained txt](../prompts/P0405_similarity_cache.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0405  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0405 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0405  (5/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Approximate Semantic Cache with Safety Gates
file         : parts/t09_latency/P0405_similarity_cache.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.similarity_cache
language     : Rust 1.86
capability   : cap.t09.similarity.similarity_cache@1
determinism  : io
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Reuse by meaning, with hard guards against wrong reuse.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. calibrated similarity thresholds per query class
  2. context-sensitivity detection preventing unsafe reuse
  3. shadow verification sampling to measure false-hit rate
  4. quality audit with a target false-hit rate under 0.1%

Expanded obligations:
  1. Implement calibrated similarity thresholds per query class, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement context-sensitivity detection preventing unsafe reuse with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement shadow verification sampling to measure false-hit rate
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement quality audit with a target false-hit rate under 0.1% as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.similarity.similarity_cache@1
  cap.t09.similarity.similarity_cache.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.exact.exact_cache@1
      if unavailable: use the in-file conservative substitute for
      `exact_cache` (documented, slower, lower quality) and set
      `degraded['exact_cache']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t07.cost.cost_aware_retrieval@1
      if unavailable: use the in-file conservative substitute for
      `cost_aware_retrieval` (documented, slower, lower quality) and set
      `degraded['cost_aware_retrieval']='local'`

  cap.t08.cost.cost_accounting_runtime@1
      if unavailable: use the in-file conservative substitute for
      `cost_accounting_runtime` (documented, slower, lower quality) and set
      `degraded['cost_accounting_runtime']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - calibrated similarity thresholds per query class
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - context-sensitivity detection preventing unsafe reuse
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - shadow verification sampling to measure false-hit rate
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - quality audit with a target false-hit rate under 0.1%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 32000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.similarity.similarity_cache@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 32000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0405_similarity_cache.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0406-template-cache

**P0406 · `template_cache` — Structural Template Cache** · [spec](PART_SPECS_T09.md#p0406-template-cache) · [self-contained txt](../prompts/P0406_template_cache.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0406  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0406 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0406  (6/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Structural Template Cache
file         : parts/t09_latency/P0406_template_cache.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.template_cache
language     : Rust 1.86
capability   : cap.t09.template.template_cache@1
determinism  : io
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Recognises repeated task shapes and reuses their solution skeletons.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. task-shape abstraction and template extraction
  2. slot-filling with verification of the filled result
  3. template library growth and pruning policy
  4. measured cost reduction on repetitive workloads

Expanded obligations:
  1. Implement task-shape abstraction and template extraction with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement slot-filling with verification of the filled result together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement template library growth and pruning policy as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Terminal-Bench
     2.1 — a regression on that benchmark is an automatic rejection of this
     part.
  4. Implement measured cost reduction on repetitive workloads, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.template.template_cache@1
  cap.t09.template.template_cache.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.similarity.similarity_cache@1
      if unavailable: use the in-file conservative substitute for
      `similarity_cache` (documented, slower, lower quality) and set
      `degraded['similarity_cache']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t07.context.context_window_manager@1
      if unavailable: use the in-file conservative substitute for
      `context_window_manager` (documented, slower, lower quality) and set
      `degraded['context_window_manager']='local'`

  cap.t08.cascade.cascade_stage1_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage1_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage1_draft']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - task-shape abstraction and template extraction
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - slot-filling with verification of the filled result
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - template library growth and pruning policy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured cost reduction on repetitive workloads
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 33000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.template.template_cache@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 33000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0406_template_cache.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0407-computation-reuse

**P0407 · `computation_reuse` — Cross-Request Computation Reuse** · [spec](PART_SPECS_T09.md#p0407-computation-reuse) · [self-contained txt](../prompts/P0407_computation_reuse.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0407  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0407 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0407  (7/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Cross-Request Computation Reuse
file         : parts/t09_latency/P0407_computation_reuse.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.computation_reuse
language     : Rust 1.86
capability   : cap.t09.computation.computation_reuse@1
determinism  : io
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Shares expensive intermediate work between concurrent requests.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. identical-subcomputation detection across in-flight requests
  2. single-flight coalescing with result fan-out
  3. isolation verification preventing cross-tenant leakage
  4. measured duplicate-work elimination rate

Expanded obligations:
  1. Implement identical-subcomputation detection across in-flight requests
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement single-flight coalescing with result fan-out as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Terminal-Bench
     2.1 — a regression on that benchmark is an automatic rejection of this
     part.
  3. Implement isolation verification preventing cross-tenant leakage, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     CursorBench 3.2 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured duplicate-work elimination rate with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.computation.computation_reuse@1
  cap.t09.computation.computation_reuse.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.template.template_cache@1
      if unavailable: use the in-file conservative substitute for
      `template_cache` (documented, slower, lower quality) and set
      `degraded['template_cache']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t07.vector.vector_index@1
      if unavailable: use the in-file conservative substitute for
      `vector_index` (documented, slower, lower quality) and set
      `degraded['vector_index']='local'`

  cap.t08.cascade.cascade_rollback@1
      if unavailable: use the in-file conservative substitute for
      `cascade_rollback` (documented, slower, lower quality) and set
      `degraded['cascade_rollback']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - identical-subcomputation detection across in-flight requests
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - single-flight coalescing with result fan-out
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - isolation verification preventing cross-tenant leakage
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured duplicate-work elimination rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 34000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.computation.computation_reuse@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 34000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0407_computation_reuse.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0408-early-exit-runtime

**P0408 · `early_exit_runtime` — Early-Exit Runtime Controller** · [spec](PART_SPECS_T09.md#p0408-early-exit-runtime) · [self-contained txt](../prompts/P0408_early_exit_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0408  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0408 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0408  (8/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Early-Exit Runtime Controller
file         : parts/t09_latency/P0408_early_exit_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.early_exit_runtime
language     : Rust 1.86
capability   : cap.t09.early.early_exit_runtime@1
determinism  : io
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Stops thinking the moment the answer is certain (S5 contributor).

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. confidence-threshold policy per task class with calibration
  2. verifier-gated exit preventing premature confident errors
  3. compute-saving measurement at matched accuracy
  4. worst-case-quality guardrails

Expanded obligations:
  1. Implement confidence-threshold policy per task class with calibration as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement verifier-gated exit preventing premature confident errors, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     CursorBench 3.2 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement compute-saving measurement at matched accuracy with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement worst-case-quality guardrails together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Its contribution is measured against
     CursorBench 3.2 — a regression on that benchmark is an automatic
     rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.early.early_exit_runtime@1
  cap.t09.early.early_exit_runtime.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.computation.computation_reuse@1
      if unavailable: use the in-file conservative substitute for
      `computation_reuse` (documented, slower, lower quality) and set
      `degraded['computation_reuse']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t07.citation.citation_grounding@1
      if unavailable: use the in-file conservative substitute for
      `citation_grounding` (documented, slower, lower quality) and set
      `degraded['citation_grounding']='local'`

  cap.t08.logit.logit_processor@1
      if unavailable: use the in-file conservative substitute for
      `logit_processor` (documented, slower, lower quality) and set
      `degraded['logit_processor']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - confidence-threshold policy per task class with calibration
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - verifier-gated exit preventing premature confident errors
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - compute-saving measurement at matched accuracy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - worst-case-quality guardrails
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 35000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.early.early_exit_runtime@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 35000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0408_early_exit_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0409-distill-fast-paths

**P0409 · `distill_fast_paths` — Distilled Fast Path Registry** · [spec](PART_SPECS_T09.md#p0409-distill-fast-paths) · [self-contained txt](../prompts/P0409_distill_fast_paths.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0409  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0409 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0409  (9/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Distilled Fast Path Registry
file         : parts/t09_latency/P0409_distill_fast_paths.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.distill_fast_paths
language     : Rust 1.86
capability   : cap.t09.distill.distill_fast_paths@1
determinism  : io
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Small models handle the easy majority; the core handles the rest.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fast-path model registry with per-task competence maps
  2. routing thresholds calibrated to maintain quality parity
  3. continuous distillation from core traffic
  4. measured fraction of traffic served by fast paths

Expanded obligations:
  1. Implement fast-path model registry with per-task competence maps, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     CursorBench 3.2 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement routing thresholds calibrated to maintain quality parity with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement continuous distillation from core traffic together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured fraction of traffic served by fast paths as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.distill.distill_fast_paths@1
  cap.t09.distill.distill_fast_paths.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.early.early_exit_runtime@1
      if unavailable: use the in-file conservative substitute for
      `early_exit_runtime` (documented, slower, lower quality) and set
      `degraded['early_exit_runtime']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t07.memory.memory_compression_learned@1
      if unavailable: use the in-file conservative substitute for
      `memory_compression_learned` (documented, slower, lower quality) and
      set `degraded['memory_compression_learned']='local'`

  cap.t08.multi.multi_model_serving@1
      if unavailable: use the in-file conservative substitute for
      `multi_model_serving` (documented, slower, lower quality) and set
      `degraded['multi_model_serving']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - fast-path model registry with per-task competence maps
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - routing thresholds calibrated to maintain quality parity
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - continuous distillation from core traffic
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured fraction of traffic served by fast paths
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 36000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.distill.distill_fast_paths@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 36000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0409_distill_fast_paths.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0410-precompute-engine

**P0410 · `precompute_engine` — Offline Precomputation Engine** · [spec](PART_SPECS_T09.md#p0410-precompute-engine) · [self-contained txt](../prompts/P0410_precompute_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0410  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0410 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0410  (10/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Offline Precomputation Engine
file         : parts/t09_latency/P0410_precompute_engine.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.precompute_engine
language     : Rust 1.86
capability   : cap.t09.precompute.precompute_engine@1
determinism  : io
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Does tomorrow's work tonight, cheaply.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. forecast-driven precomputation of likely requests and embeddings
  2. cost-arbitrage scheduling into cheap capacity windows
  3. staleness management and invalidation
  4. measured online-latency reduction versus precompute cost

Expanded obligations:
  1. Implement forecast-driven precomputation of likely requests and
     embeddings with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement cost-arbitrage scheduling into cheap capacity windows together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement staleness management and invalidation as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured online-latency reduction versus precompute cost, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.precompute.precompute_engine@1
  cap.t09.precompute.precompute_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.distill.distill_fast_paths@1
      if unavailable: use the in-file conservative substitute for
      `distill_fast_paths` (documented, slower, lower quality) and set
      `degraded['distill_fast_paths']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t07.memory.memory_gc@1
      if unavailable: use the in-file conservative substitute for
      `memory_gc` (documented, slower, lower quality) and set
      `degraded['memory_gc']='local'`

  cap.t08.output.output_verification_loop@1
      if unavailable: use the in-file conservative substitute for
      `output_verification_loop` (documented, slower, lower quality) and set
      `degraded['output_verification_loop']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - forecast-driven precomputation of likely requests and embeddings
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost-arbitrage scheduling into cheap capacity windows
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - staleness management and invalidation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured online-latency reduction versus precompute cost
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 37000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.precompute.precompute_engine@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 37000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0410_precompute_engine.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0411-prefetch-predictor

**P0411 · `prefetch_predictor` — Next-Action Prediction & Prefetch** · [spec](PART_SPECS_T09.md#p0411-prefetch-predictor) · [self-contained txt](../prompts/P0411_prefetch_predictor.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0411  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0411 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0411  (11/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Next-Action Prediction & Prefetch
file         : parts/t09_latency/P0411_prefetch_predictor.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.prefetch_predictor
language     : Rust 1.86
capability   : cap.t09.prefetch.prefetch_predictor@1
determinism  : io
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Predicts the user's or agent's next need and prepares it (S6).

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. sequence models over session and workflow traces
  2. prefetch budget control with wasted-work accounting
  3. accuracy measurement per prediction horizon
  4. measured p50/p99 improvement attributable to prefetch

Expanded obligations:
  1. Implement sequence models over session and workflow traces together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement prefetch budget control with wasted-work accounting as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement accuracy measurement per prediction horizon, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured p50/p99 improvement attributable to prefetch with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.prefetch.prefetch_predictor@1
  cap.t09.prefetch.prefetch_predictor.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.precompute.precompute_engine@1
      if unavailable: use the in-file conservative substitute for
      `precompute_engine` (documented, slower, lower quality) and set
      `degraded['precompute_engine']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t07.memory.memory_audit@1
      if unavailable: use the in-file conservative substitute for
      `memory_audit` (documented, slower, lower quality) and set
      `degraded['memory_audit']='local'`

  cap.t08.engine.engine_fault_tolerance@1
      if unavailable: use the in-file conservative substitute for
      `engine_fault_tolerance` (documented, slower, lower quality) and set
      `degraded['engine_fault_tolerance']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - sequence models over session and workflow traces
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - prefetch budget control with wasted-work accounting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accuracy measurement per prediction horizon
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured p50/p99 improvement attributable to prefetch
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 38000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.prefetch.prefetch_predictor@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 38000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0411_prefetch_predictor.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0412-parallel-horizon

**P0412 · `parallel_horizon` — Parallel Horizon Execution Engine** · [spec](PART_SPECS_T09.md#p0412-parallel-horizon) · [self-contained txt](../prompts/P0412_parallel_horizon.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0412  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0412 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0412  (12/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Parallel Horizon Execution Engine
file         : parts/t09_latency/P0412_parallel_horizon.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.parallel_horizon
language     : Rust 1.86
capability   : cap.t09.parallel.parallel_horizon@1
determinism  : io
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Turns serial long-horizon work into critical-path-time work (S6 core).

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. speculative parallel execution of independent DAG branches
  2. optimistic execution with dependency-violation rollback
  3. 1000-way concurrency management with resource caps
  4. measured wall-clock reduction on long-horizon tasks

Expanded obligations:
  1. Implement speculative parallel execution of independent DAG branches as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement optimistic execution with dependency-violation rollback, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement 1000-way concurrency management with resource caps with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured wall-clock reduction on long-horizon tasks together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.parallel.parallel_horizon@1
  cap.t09.parallel.parallel_horizon.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.prefetch.prefetch_predictor@1
      if unavailable: use the in-file conservative substitute for
      `prefetch_predictor` (documented, slower, lower quality) and set
      `degraded['prefetch_predictor']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t07.streaming.streaming_ingest@1
      if unavailable: use the in-file conservative substitute for
      `streaming_ingest` (documented, slower, lower quality) and set
      `degraded['streaming_ingest']='local'`

  cap.t08.engine.engine_security@1
      if unavailable: use the in-file conservative substitute for
      `engine_security` (documented, slower, lower quality) and set
      `degraded['engine_security']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - speculative parallel execution of independent DAG branches
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - optimistic execution with dependency-violation rollback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - 1000-way concurrency management with resource caps
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured wall-clock reduction on long-horizon tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 39000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.parallel.parallel_horizon@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 39000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0412_parallel_horizon.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0413-dag-critical-path

**P0413 · `dag_critical_path` — Critical Path Optimiser** · [spec](PART_SPECS_T09.md#p0413-dag-critical-path) · [self-contained txt](../prompts/P0413_dag_critical_path.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0413  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0413 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0413  (13/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Critical Path Optimiser
file         : parts/t09_latency/P0413_dag_critical_path.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.dag_critical_path
language     : Rust 1.86
capability   : cap.t09.dag.dag_critical_path@1
determinism  : io
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Finds and shortens the one path that determines total time.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. critical-path computation with measured node costs
  2. targeted optimisation recommendation per path node
  3. what-if analysis for proposed changes
  4. measured makespan reduction after optimisation

Expanded obligations:
  1. Implement critical-path computation with measured node costs, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement targeted optimisation recommendation per path node with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement what-if analysis for proposed changes together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured makespan reduction after optimisation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.dag.dag_critical_path@1
  cap.t09.dag.dag_critical_path.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.parallel.parallel_horizon@1
      if unavailable: use the in-file conservative substitute for
      `parallel_horizon` (documented, slower, lower quality) and set
      `degraded['parallel_horizon']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t07.kv.kv_compression_runtime@1
      if unavailable: use the in-file conservative substitute for
      `kv_compression_runtime` (documented, slower, lower quality) and set
      `degraded['kv_compression_runtime']='local'`

  cap.t08.admission.admission_control@1
      if unavailable: use the in-file conservative substitute for
      `admission_control` (documented, slower, lower quality) and set
      `degraded['admission_control']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - critical-path computation with measured node costs
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - targeted optimisation recommendation per path node
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - what-if analysis for proposed changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured makespan reduction after optimisation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 40000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.dag.dag_critical_path@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 40000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0413_dag_critical_path.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0414-async-pipeline

**P0414 · `async_pipeline` — Asynchronous Pipeline Orchestrator** · [spec](PART_SPECS_T09.md#p0414-async-pipeline) · [self-contained txt](../prompts/P0414_async_pipeline.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0414  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0414 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0414  (14/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Asynchronous Pipeline Orchestrator
file         : parts/t09_latency/P0414_async_pipeline.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.async_pipeline
language     : Rust 1.86
capability   : cap.t09.async.async_pipeline@1
determinism  : io
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Everything that can overlap, does.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dependency-driven async execution with structured concurrency
  2. overlap-efficiency measurement (achieved versus ideal)
  3. deadlock freedom and cancellation correctness
  4. pipeline-depth tuning under memory limits

Expanded obligations:
  1. Implement dependency-driven async execution with structured concurrency
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement overlap-efficiency measurement (achieved versus ideal)
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement deadlock freedom and cancellation correctness as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement pipeline-depth tuning under memory limits, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.async.async_pipeline@1
  cap.t09.async.async_pipeline.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.dag.dag_critical_path@1
      if unavailable: use the in-file conservative substitute for
      `dag_critical_path` (documented, slower, lower quality) and set
      `degraded['dag_critical_path']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t07.forgetting.forgetting_policy@1
      if unavailable: use the in-file conservative substitute for
      `forgetting_policy` (documented, slower, lower quality) and set
      `degraded['forgetting_policy']='local'`

  cap.t08.cascade.cascade_batching@1
      if unavailable: use the in-file conservative substitute for
      `cascade_batching` (documented, slower, lower quality) and set
      `degraded['cascade_batching']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - dependency-driven async execution with structured concurrency
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - overlap-efficiency measurement (achieved versus ideal)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deadlock freedom and cancellation correctness
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - pipeline-depth tuning under memory limits
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 41000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.async.async_pipeline@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 41000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0414_async_pipeline.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0415-tail-latency

**P0415 · `tail_latency` — Tail Latency Engineering** · [spec](PART_SPECS_T09.md#p0415-tail-latency) · [self-contained txt](../prompts/P0415_tail_latency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0415  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0415 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0415  (15/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Tail Latency Engineering
file         : parts/t09_latency/P0415_tail_latency.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.tail_latency
language     : Rust 1.86
capability   : cap.t09.tail.tail_latency@1
determinism  : io
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
p99.9 matters more than p50 for agents making 1000 calls.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hedged requests with cancellation and cost caps
  2. tail-cause attribution (GC, cache miss, straggler, throttle)
  3. per-cause mitigation with measured effect
  4. p99.9 target enforcement in the benchmark gate

Expanded obligations:
  1. Implement hedged requests with cancellation and cost caps together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement tail-cause attribution (GC, cache miss, straggler, throttle)
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement per-cause mitigation with measured effect, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement p99.9 target enforcement in the benchmark gate with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.tail.tail_latency@1
  cap.t09.tail.tail_latency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.async.async_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `async_pipeline` (documented, slower, lower quality) and set
      `degraded['async_pipeline']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t07.reranker.reranker_model@1
      if unavailable: use the in-file conservative substitute for
      `reranker_model` (documented, slower, lower quality) and set
      `degraded['reranker_model']='local'`

  cap.t08.constrained.constrained_decoding@1
      if unavailable: use the in-file conservative substitute for
      `constrained_decoding` (documented, slower, lower quality) and set
      `degraded['constrained_decoding']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - hedged requests with cancellation and cost caps
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tail-cause attribution (GC, cache miss, straggler, throttle)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-cause mitigation with measured effect
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - p99.9 target enforcement in the benchmark gate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 42000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.tail.tail_latency@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 42000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0415_tail_latency.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0416-jitter-control

**P0416 · `jitter_control` — Latency Jitter & Predictability Control** · [spec](PART_SPECS_T09.md#p0416-jitter-control) · [self-contained txt](../prompts/P0416_jitter_control.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0416  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0416 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0416  (16/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Latency Jitter & Predictability Control
file         : parts/t09_latency/P0416_jitter_control.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.jitter_control
language     : Rust 1.86
capability   : cap.t09.jitter.jitter_control@1
determinism  : io
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Consistent latency is a feature; variance is a bug.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. variance-source identification and elimination
  2. pacing and admission smoothing
  3. jitter measurement with distribution shape analysis
  4. predictability score reported per endpoint

Expanded obligations:
  1. Implement variance-source identification and elimination as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement pacing and admission smoothing, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against CursorBench 3.2 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement jitter measurement with distribution shape analysis with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement predictability score reported per endpoint together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.jitter.jitter_control@1
  cap.t09.jitter.jitter_control.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.tail.tail_latency@1
      if unavailable: use the in-file conservative substitute for
      `tail_latency` (documented, slower, lower quality) and set
      `degraded['tail_latency']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t07.belief.belief_revision@1
      if unavailable: use the in-file conservative substitute for
      `belief_revision` (documented, slower, lower quality) and set
      `degraded['belief_revision']='local'`

  cap.t08.weight.weight_hotswap@1
      if unavailable: use the in-file conservative substitute for
      `weight_hotswap` (documented, slower, lower quality) and set
      `degraded['weight_hotswap']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - variance-source identification and elimination
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - pacing and admission smoothing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - jitter measurement with distribution shape analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - predictability score reported per endpoint
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 43000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.jitter.jitter_control@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 43000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0416_jitter_control.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0417-warmup-manager

**P0417 · `warmup_manager` — Warmup & Cold Start Elimination** · [spec](PART_SPECS_T09.md#p0417-warmup-manager) · [self-contained txt](../prompts/P0417_warmup_manager.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0417  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0417 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0417  (17/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Warmup & Cold Start Elimination
file         : parts/t09_latency/P0417_warmup_manager.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.warmup_manager
language     : Rust 1.86
capability   : cap.t09.warmup.warmup_manager@1
determinism  : io
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The first request is as fast as the thousandth.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. staged warmup: weights, kernels, caches, JIT, indexes
  2. predictive warmup from deployment and traffic signals
  3. cold-start latency measurement per stage
  4. target: cold start within 1.2x of warm latency

Expanded obligations:
  1. Implement staged warmup: weights, kernels, caches, JIT, indexes, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     CursorBench 3.2 — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement predictive warmup from deployment and traffic signals with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement cold-start latency measurement per stage together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement target: cold start within 1.2x of warm latency as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.warmup.warmup_manager@1
  cap.t09.warmup.warmup_manager.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.jitter.jitter_control@1
      if unavailable: use the in-file conservative substitute for
      `jitter_control` (documented, slower, lower quality) and set
      `degraded['jitter_control']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t07.retrieval.retrieval_cache@1
      if unavailable: use the in-file conservative substitute for
      `retrieval_cache` (documented, slower, lower quality) and set
      `degraded['retrieval_cache']='local'`

  cap.t08.parallel.parallel_generation@1
      if unavailable: use the in-file conservative substitute for
      `parallel_generation` (documented, slower, lower quality) and set
      `degraded['parallel_generation']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - staged warmup: weights, kernels, caches, JIT, indexes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - predictive warmup from deployment and traffic signals
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cold-start latency measurement per stage
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: cold start within 1.2x of warm latency
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 44000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.warmup.warmup_manager@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 44000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0417_warmup_manager.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0418-gc-pause-control

**P0418 · `gc_pause_control` — Pause-Free Operation Engineering** · [spec](PART_SPECS_T09.md#p0418-gc-pause-control) · [self-contained txt](../prompts/P0418_gc_pause_control.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0418  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0418 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0418  (18/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Pause-Free Operation Engineering
file         : parts/t09_latency/P0418_gc_pause_control.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.gc_pause_control
language     : Rust 1.86
capability   : cap.t09.gc.gc_pause_control@1
determinism  : io
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
No stop-the-world event ever touches a request.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. allocation-free hot paths with preallocated pools
  2. incremental background reclamation with bounded steps
  3. pause-time distribution measurement
  4. verification that no pause exceeds the jitter budget

Expanded obligations:
  1. Implement allocation-free hot paths with preallocated pools with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement incremental background reclamation with bounded steps together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement pause-time distribution measurement as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement verification that no pause exceeds the jitter budget, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.gc.gc_pause_control@1
  cap.t09.gc.gc_pause_control.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.warmup.warmup_manager@1
      if unavailable: use the in-file conservative substitute for
      `warmup_manager` (documented, slower, lower quality) and set
      `degraded['warmup_manager']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t07.user.user_model@1
      if unavailable: use the in-file conservative substitute for
      `user_model` (documented, slower, lower quality) and set
      `degraded['user_model']='local'`

  cap.t08.quantised.quantised_serving@1
      if unavailable: use the in-file conservative substitute for
      `quantised_serving` (documented, slower, lower quality) and set
      `degraded['quantised_serving']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - allocation-free hot paths with preallocated pools
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - incremental background reclamation with bounded steps
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - pause-time distribution measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification that no pause exceeds the jitter budget
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 45000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.gc.gc_pause_control@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 45000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0418_gc_pause_control.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0419-syscall-reduction

**P0419 · `syscall_reduction` — Syscall & Context-Switch Minimisation** · [spec](PART_SPECS_T09.md#p0419-syscall-reduction) · [self-contained txt](../prompts/P0419_syscall_reduction.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0419  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0419 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0419  (19/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Syscall & Context-Switch Minimisation
file         : parts/t09_latency/P0419_syscall_reduction.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.syscall_reduction
language     : Rust 1.86
capability   : cap.t09.syscall.syscall_reduction@1
determinism  : io
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Removes operating-system overhead from the hot path.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. batched IO, io_uring-style submission and busy-poll modes
  2. thread-affinity and preemption avoidance
  3. syscall-count measurement per request
  4. measured latency improvement from each reduction

Expanded obligations:
  1. Implement batched IO, io_uring-style submission and busy-poll modes
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement thread-affinity and preemption avoidance as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Terminal-Bench
     2.1 — a regression on that benchmark is an automatic rejection of this
     part.
  3. Implement syscall-count measurement per request, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured latency improvement from each reduction with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.syscall.syscall_reduction@1
  cap.t09.syscall.syscall_reduction.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.gc.gc_pause_control@1
      if unavailable: use the in-file conservative substitute for
      `gc_pause_control` (documented, slower, lower quality) and set
      `degraded['gc_pause_control']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t07.memory.memory_sharding@1
      if unavailable: use the in-file conservative substitute for
      `memory_sharding` (documented, slower, lower quality) and set
      `degraded['memory_sharding']='local'`

  cap.t08.prompt.prompt_compilation@1
      if unavailable: use the in-file conservative substitute for
      `prompt_compilation` (documented, slower, lower quality) and set
      `degraded['prompt_compilation']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - batched IO, io_uring-style submission and busy-poll modes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - thread-affinity and preemption avoidance
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - syscall-count measurement per request
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured latency improvement from each reduction
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 46000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.syscall.syscall_reduction@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 46000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0419_syscall_reduction.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0420-network-latency

**P0420 · `network_latency` — Network Path Latency Optimisation** · [spec](PART_SPECS_T09.md#p0420-network-latency) · [self-contained txt](../prompts/P0420_network_latency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0420  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0420 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0420  (20/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Network Path Latency Optimisation
file         : parts/t09_latency/P0420_network_latency.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.network_latency
language     : Rust 1.86
capability   : cap.t09.network.network_latency@1
determinism  : io
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The wire should add microseconds, not milliseconds.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. connection reuse, 0-RTT resumption and header compression
  2. geographic routing and edge termination policy
  3. protocol-overhead measurement and reduction
  4. measured RTT contribution to end-to-end latency

Expanded obligations:
  1. Implement connection reuse, 0-RTT resumption and header compression as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement geographic routing and edge termination policy, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement protocol-overhead measurement and reduction with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured RTT contribution to end-to-end latency together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.network.network_latency@1
  cap.t09.network.network_latency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.syscall.syscall_reduction@1
      if unavailable: use the in-file conservative substitute for
      `syscall_reduction` (documented, slower, lower quality) and set
      `degraded['syscall_reduction']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t07.kv.kv_dedup@1
      if unavailable: use the in-file conservative substitute for `kv_dedup`
      (documented, slower, lower quality) and set
      `degraded['kv_dedup']='local'`

  cap.t08.prefill.prefill_decode_split@1
      if unavailable: use the in-file conservative substitute for
      `prefill_decode_split` (documented, slower, lower quality) and set
      `degraded['prefill_decode_split']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - connection reuse, 0-RTT resumption and header compression
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - geographic routing and edge termination policy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - protocol-overhead measurement and reduction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured RTT contribution to end-to-end latency
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 47000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.network.network_latency@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 47000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0420_network_latency.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0421-edge-inference

**P0421 · `edge_inference` — Edge & Local-First Execution** · [spec](PART_SPECS_T09.md#p0421-edge-inference) · [self-contained txt](../prompts/P0421_edge_inference.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0421  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0421 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0421  (21/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Edge & Local-First Execution
file         : parts/t09_latency/P0421_edge_inference.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.edge_inference
language     : Rust 1.86
capability   : cap.t09.edge.edge_inference@1
determinism  : io
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The lowest-latency path is the one that never leaves the device.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. local model tier with capability-based cloud escalation
  2. hybrid local/cloud execution splitting a single request
  3. privacy benefits and quality tradeoffs measured
  4. latency comparison versus cloud-only serving

Expanded obligations:
  1. Implement local model tier with capability-based cloud escalation, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     CursorBench 3.2 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement hybrid local/cloud execution splitting a single request with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement privacy benefits and quality tradeoffs measured together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement latency comparison versus cloud-only serving as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.edge.edge_inference@1
  cap.t09.edge.edge_inference.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.network.network_latency@1
      if unavailable: use the in-file conservative substitute for
      `network_latency` (documented, slower, lower quality) and set
      `degraded['network_latency']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t07.memory.memory_consolidation@1
      if unavailable: use the in-file conservative substitute for
      `memory_consolidation` (documented, slower, lower quality) and set
      `degraded['memory_consolidation']='local'`

  cap.t08.cascade.cascade_scheduler@1
      if unavailable: use the in-file conservative substitute for
      `cascade_scheduler` (documented, slower, lower quality) and set
      `degraded['cascade_scheduler']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - local model tier with capability-based cloud escalation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hybrid local/cloud execution splitting a single request
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - privacy benefits and quality tradeoffs measured
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency comparison versus cloud-only serving
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 48000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.edge.edge_inference@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 48000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0421_edge_inference.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0422-compression-latency

**P0422 · `compression_latency` — Payload Compression Latency Tradeoffs** · [spec](PART_SPECS_T09.md#p0422-compression-latency) · [self-contained txt](../prompts/P0422_compression_latency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0422  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0422 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0422  (22/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Payload Compression Latency Tradeoffs
file         : parts/t09_latency/P0422_compression_latency.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.compression_latency
language     : Rust 1.86
capability   : cap.t09.compression.compression_latency@1
determinism  : io
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Compresses only when it actually makes things faster.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. adaptive compression decisions from payload size and link speed
  2. streaming compression avoiding buffering delay
  3. CPU-cost versus transfer-saving model
  4. measured net latency effect per decision

Expanded obligations:
  1. Implement adaptive compression decisions from payload size and link
     speed with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement streaming compression avoiding buffering delay together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement CPU-cost versus transfer-saving model as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured net latency effect per decision, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.compression.compression_latency@1
  cap.t09.compression.compression_latency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.edge.edge_inference@1
      if unavailable: use the in-file conservative substitute for
      `edge_inference` (documented, slower, lower quality) and set
      `degraded['edge_inference']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t07.embedding.embedding_model@1
      if unavailable: use the in-file conservative substitute for
      `embedding_model` (documented, slower, lower quality) and set
      `degraded['embedding_model']='local'`

  cap.t08.sampler.sampler_engine@1
      if unavailable: use the in-file conservative substitute for
      `sampler_engine` (documented, slower, lower quality) and set
      `degraded['sampler_engine']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - adaptive compression decisions from payload size and link speed
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - streaming compression avoiding buffering delay
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - CPU-cost versus transfer-saving model
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured net latency effect per decision
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 49000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.compression.compression_latency@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 49000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0422_compression_latency.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0423-batch-latency-tradeoff

**P0423 · `batch_latency_tradeoff` — Batching Latency/Throughput Optimiser** · [spec](PART_SPECS_T09.md#p0423-batch-latency-tradeoff) · [self-contained txt](../prompts/P0423_batch_latency_tradeoff.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0423  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0423 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0423  (23/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Batching Latency/Throughput Optimiser
file         : parts/t09_latency/P0423_batch_latency_tradeoff.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.batch_latency_tradeoff
language     : Rust 1.86
capability   : cap.t09.batch.batch_latency_tradeoff@1
determinism  : io
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Finds the exact batching point that meets SLOs at minimum cost.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. queueing-theory model calibrated with measurements
  2. per-SLO-class batching parameter selection
  3. dynamic adjustment under changing load
  4. cost-at-SLO measurement versus fixed configurations

Expanded obligations:
  1. Implement queueing-theory model calibrated with measurements together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement per-SLO-class batching parameter selection as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement dynamic adjustment under changing load, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement cost-at-SLO measurement versus fixed configurations with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.batch.batch_latency_tradeoff@1
  cap.t09.batch.batch_latency_tradeoff.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.compression.compression_latency@1
      if unavailable: use the in-file conservative substitute for
      `compression_latency` (documented, slower, lower quality) and set
      `degraded['compression_latency']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t07.world.world_state_store@1
      if unavailable: use the in-file conservative substitute for
      `world_state_store` (documented, slower, lower quality) and set
      `degraded['world_state_store']='local'`

  cap.t08.model.model_loading@1
      if unavailable: use the in-file conservative substitute for
      `model_loading` (documented, slower, lower quality) and set
      `degraded['model_loading']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - queueing-theory model calibrated with measurements
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-SLO-class batching parameter selection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - dynamic adjustment under changing load
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost-at-SLO measurement versus fixed configurations
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 3000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.batch.batch_latency_tradeoff@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 3000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0423_batch_latency_tradeoff.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0424-priority-lanes

**P0424 · `priority_lanes` — Priority Lanes & Interactive Fast Path** · [spec](PART_SPECS_T09.md#p0424-priority-lanes) · [self-contained txt](../prompts/P0424_priority_lanes.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0424  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0424 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0424  (24/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Priority Lanes & Interactive Fast Path
file         : parts/t09_latency/P0424_priority_lanes.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.priority_lanes
language     : Rust 1.86
capability   : cap.t09.priority.priority_lanes@1
determinism  : io
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Interactive requests never queue behind batch work.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. strict-priority lanes with reserved capacity
  2. batch-work preemption with safe checkpointing
  3. interactive p99 protection measurement under batch load
  4. fairness accounting across lanes

Expanded obligations:
  1. Implement strict-priority lanes with reserved capacity as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement batch-work preemption with safe checkpointing, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement interactive p99 protection measurement under batch load with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement fairness accounting across lanes together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.priority.priority_lanes@1
  cap.t09.priority.priority_lanes.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.batch.batch_latency_tradeoff@1
      if unavailable: use the in-file conservative substitute for
      `batch_latency_tradeoff` (documented, slower, lower quality) and set
      `degraded['batch_latency_tradeoff']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t07.subgraph.subgraph_memoize@1
      if unavailable: use the in-file conservative substitute for
      `subgraph_memoize` (documented, slower, lower quality) and set
      `degraded['subgraph_memoize']='local'`

  cap.t08.speculative.speculative_tools@1
      if unavailable: use the in-file conservative substitute for
      `speculative_tools` (documented, slower, lower quality) and set
      `degraded['speculative_tools']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - strict-priority lanes with reserved capacity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - batch-work preemption with safe checkpointing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - interactive p99 protection measurement under batch load
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fairness accounting across lanes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 4000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.priority.priority_lanes@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 4000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0424_priority_lanes.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0425-speculative-ui

**P0425 · `speculative_ui` — Perceived Latency Engineering** · [spec](PART_SPECS_T09.md#p0425-speculative-ui) · [self-contained txt](../prompts/P0425_speculative_ui.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0425  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0425 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0425  (25/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Perceived Latency Engineering
file         : parts/t09_latency/P0425_speculative_ui.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.speculative_ui
language     : Rust 1.86
capability   : cap.t09.speculative.speculative_ui@1
determinism  : io
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Feels instant even when it is not.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. progressive disclosure and streaming-order optimisation
  2. optimistic partial results with correction protocol
  3. perceived-latency measurement methodology
  4. user-facing latency budget definitions

Expanded obligations:
  1. Implement progressive disclosure and streaming-order optimisation, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement optimistic partial results with correction protocol with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement perceived-latency measurement methodology together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement user-facing latency budget definitions as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.speculative.speculative_ui@1
  cap.t09.speculative.speculative_ui.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.priority.priority_lanes@1
      if unavailable: use the in-file conservative substitute for
      `priority_lanes` (documented, slower, lower quality) and set
      `degraded['priority_lanes']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t07.multimodal.multimodal_memory@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_memory` (documented, slower, lower quality) and set
      `degraded['multimodal_memory']='local'`

  cap.t08.kv.kv_offload_runtime@1
      if unavailable: use the in-file conservative substitute for
      `kv_offload_runtime` (documented, slower, lower quality) and set
      `degraded['kv_offload_runtime']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - progressive disclosure and streaming-order optimisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - optimistic partial results with correction protocol
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - perceived-latency measurement methodology
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - user-facing latency budget definitions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 5000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.speculative.speculative_ui@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 5000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0425_speculative_ui.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0426-cache-coherence

**P0426 · `cache_coherence` — Cross-Layer Cache Coherence & Invalidation** · [spec](PART_SPECS_T09.md#p0426-cache-coherence) · [self-contained txt](../prompts/P0426_cache_coherence.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0426  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0426 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0426  (26/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Cross-Layer Cache Coherence & Invalidation
file         : parts/t09_latency/P0426_cache_coherence.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.cache_coherence
language     : Rust 1.86
capability   : cap.t09.cache.cache_coherence@1
determinism  : io
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Ten cache layers, zero stale answers.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. global invalidation protocol with versioned epochs
  2. dependency tracking from source data to cached answers
  3. stale-read detection and measurement
  4. invalidation-latency and correctness verification

Expanded obligations:
  1. Implement global invalidation protocol with versioned epochs with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement dependency tracking from source data to cached answers
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement stale-read detection and measurement as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement invalidation-latency and correctness verification, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.cache.cache_coherence@1
  cap.t09.cache.cache_coherence.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.speculative.speculative_ui@1
      if unavailable: use the in-file conservative substitute for
      `speculative_ui` (documented, slower, lower quality) and set
      `degraded['speculative_ui']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t07.context.context_budget_optimiser@1
      if unavailable: use the in-file conservative substitute for
      `context_budget_optimiser` (documented, slower, lower quality) and set
      `degraded['context_budget_optimiser']='local'`

  cap.t08.tokenizer.tokenizer_runtime@1
      if unavailable: use the in-file conservative substitute for
      `tokenizer_runtime` (documented, slower, lower quality) and set
      `degraded['tokenizer_runtime']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - global invalidation protocol with versioned epochs
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - dependency tracking from source data to cached answers
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - stale-read detection and measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - invalidation-latency and correctness verification
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 6000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.cache.cache_coherence@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 6000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0426_cache_coherence.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0427-hot-cold-split

**P0427 · `hot_cold_split` — Hot/Cold Path Separation** · [spec](PART_SPECS_T09.md#p0427-hot-cold-split) · [self-contained txt](../prompts/P0427_hot_cold_split.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0427  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0427 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0427  (27/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Hot/Cold Path Separation
file         : parts/t09_latency/P0427_hot_cold_split.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.hot_cold_split
language     : Rust 1.86
capability   : cap.t09.hot.hot_cold_split@1
determinism  : io
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The 1% of code that runs 99% of the time gets all the attention.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. profile-driven hot-path identification and isolation
  2. cold-path outlining to keep instruction caches warm
  3. branch-layout and code-alignment optimisation
  4. measured instruction-cache-miss reduction

Expanded obligations:
  1. Implement profile-driven hot-path identification and isolation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement cold-path outlining to keep instruction caches warm as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement branch-layout and code-alignment optimisation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured instruction-cache-miss reduction with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Terminal-Bench 2.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.hot.hot_cold_split@1
  cap.t09.hot.hot_cold_split.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.cache.cache_coherence@1
      if unavailable: use the in-file conservative substitute for
      `cache_coherence` (documented, slower, lower quality) and set
      `degraded['cache_coherence']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t07.kv.kv_eviction@1
      if unavailable: use the in-file conservative substitute for
      `kv_eviction` (documented, slower, lower quality) and set
      `degraded['kv_eviction']='local'`

  cap.t08.chunked.chunked_prefill@1
      if unavailable: use the in-file conservative substitute for
      `chunked_prefill` (documented, slower, lower quality) and set
      `degraded['chunked_prefill']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - profile-driven hot-path identification and isolation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cold-path outlining to keep instruction caches warm
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - branch-layout and code-alignment optimisation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured instruction-cache-miss reduction
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 7000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.hot.hot_cold_split@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 7000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0427_hot_cold_split.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0428-lock-free-paths

**P0428 · `lock_free_paths` — Lock-Free Request Path** · [spec](PART_SPECS_T09.md#p0428-lock-free-paths) · [self-contained txt](../prompts/P0428_lock_free_paths.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0428  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0428 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0428  (28/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Lock-Free Request Path
file         : parts/t09_latency/P0428_lock_free_paths.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.lock_free_paths
language     : Rust 1.86
capability   : cap.t09.lock.lock_free_paths@1
determinism  : io
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
No request ever waits for a mutex.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. lock-free data structures on every shared hot structure
  2. contention measurement and elimination
  3. progress guarantees (lock-freedom or wait-freedom) stated per structure
  4. scalability measurement to 256 threads

Expanded obligations:
  1. Implement lock-free data structures on every shared hot structure as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement contention measurement and elimination, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement progress guarantees (lock-freedom or wait-freedom) stated per
     structure with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Terminal-Bench
     2.1 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  4. Implement scalability measurement to 256 threads together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.lock.lock_free_paths@1
  cap.t09.lock.lock_free_paths.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.hot.hot_cold_split@1
      if unavailable: use the in-file conservative substitute for
      `hot_cold_split` (documented, slower, lower quality) and set
      `degraded['hot_cold_split']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t07.procedural.procedural_memory@1
      if unavailable: use the in-file conservative substitute for
      `procedural_memory` (documented, slower, lower quality) and set
      `degraded['procedural_memory']='local'`

  cap.t08.cascade.cascade_acceptance@1
      if unavailable: use the in-file conservative substitute for
      `cascade_acceptance` (documented, slower, lower quality) and set
      `degraded['cascade_acceptance']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - lock-free data structures on every shared hot structure
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - contention measurement and elimination
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - progress guarantees (lock-freedom or wait-freedom) stated per st
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - scalability measurement to 256 threads
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 8000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.lock.lock_free_paths@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 8000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0428_lock_free_paths.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0429-numa-latency

**P0429 · `numa_latency` — Memory Locality Latency Optimisation** · [spec](PART_SPECS_T09.md#p0429-numa-latency) · [self-contained txt](../prompts/P0429_numa_latency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0429  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0429 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0429  (29/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Memory Locality Latency Optimisation
file         : parts/t09_latency/P0429_numa_latency.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.numa_latency
language     : Rust 1.86
capability   : cap.t09.numa.numa_latency@1
determinism  : io
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Every hot access is local.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. access-pattern profiling and remote-access detection
  2. data placement and thread pinning remediation
  3. measured latency improvement from locality fixes
  4. regression detection on placement changes

Expanded obligations:
  1. Implement access-pattern profiling and remote-access detection, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement data placement and thread pinning remediation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Terminal-Bench 2.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement measured latency improvement from locality fixes together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement regression detection on placement changes as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Terminal-Bench
     2.1 — a regression on that benchmark is an automatic rejection of this
     part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.numa.numa_latency@1
  cap.t09.numa.numa_latency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.lock.lock_free_paths@1
      if unavailable: use the in-file conservative substitute for
      `lock_free_paths` (documented, slower, lower quality) and set
      `degraded['lock_free_paths']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t07.chunking.chunking_strategy@1
      if unavailable: use the in-file conservative substitute for
      `chunking_strategy` (documented, slower, lower quality) and set
      `degraded['chunking_strategy']='local'`

  cap.t08.session.session_affinity@1
      if unavailable: use the in-file conservative substitute for
      `session_affinity` (documented, slower, lower quality) and set
      `degraded['session_affinity']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - access-pattern profiling and remote-access detection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - data placement and thread pinning remediation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - measured latency improvement from locality fixes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - regression detection on placement changes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 9000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.numa.numa_latency@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 9000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0429_numa_latency.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0430-io-scheduling

**P0430 · `io_scheduling` — Storage IO Latency Scheduling** · [spec](PART_SPECS_T09.md#p0430-io-scheduling) · [self-contained txt](../prompts/P0430_io_scheduling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0430  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0430 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0430  (30/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Storage IO Latency Scheduling
file         : parts/t09_latency/P0430_io_scheduling.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.io_scheduling
language     : Rust 1.86
capability   : cap.t09.io.io_scheduling@1
determinism  : io
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Disk never stalls a token.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. priority IO scheduling with deadline awareness
  2. readahead tuning from access-pattern prediction
  3. IO-latency percentile measurement per class
  4. stall-free verification under heavy IO load

Expanded obligations:
  1. Implement priority IO scheduling with deadline awareness with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement readahead tuning from access-pattern prediction together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement IO-latency percentile measurement per class as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Terminal-Bench
     2.1 — a regression on that benchmark is an automatic rejection of this
     part.
  4. Implement stall-free verification under heavy IO load, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.io.io_scheduling@1
  cap.t09.io.io_scheduling.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.numa.numa_latency@1
      if unavailable: use the in-file conservative substitute for
      `numa_latency` (documented, slower, lower quality) and set
      `degraded['numa_latency']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t07.memory.memory_encryption@1
      if unavailable: use the in-file conservative substitute for
      `memory_encryption` (documented, slower, lower quality) and set
      `degraded['memory_encryption']='local'`

  cap.t08.multi.multi_gpu_runtime@1
      if unavailable: use the in-file conservative substitute for
      `multi_gpu_runtime` (documented, slower, lower quality) and set
      `degraded['multi_gpu_runtime']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - priority IO scheduling with deadline awareness
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - readahead tuning from access-pattern prediction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - IO-latency percentile measurement per class
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - stall-free verification under heavy IO load
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 10000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.io.io_scheduling@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 10000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0430_io_scheduling.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0431-adaptive-quality

**P0431 · `adaptive_quality` — Adaptive Quality/Latency Controller** · [spec](PART_SPECS_T09.md#p0431-adaptive-quality) · [self-contained txt](../prompts/P0431_adaptive_quality.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0431  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0431 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0431  (31/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Adaptive Quality/Latency Controller
file         : parts/t09_latency/P0431_adaptive_quality.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.adaptive_quality
language     : Rust 1.86
capability   : cap.t09.adaptive.adaptive_quality@1
determinism  : io
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Trades quality for speed only when explicitly permitted, and says so.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. quality-knob inventory with measured latency/quality effects
  2. user-declared preference honoring with transparency
  3. closed-loop control with stability guarantees
  4. measured SLO attainment across preference settings

Expanded obligations:
  1. Implement quality-knob inventory with measured latency/quality effects
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement user-declared preference honoring with transparency as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement closed-loop control with stability guarantees, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured SLO attainment across preference settings with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.adaptive.adaptive_quality@1
  cap.t09.adaptive.adaptive_quality.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.io.io_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `io_scheduling` (documented, slower, lower quality) and set
      `degraded['io_scheduling']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t07.tool.tool_result_cache@1
      if unavailable: use the in-file conservative substitute for
      `tool_result_cache` (documented, slower, lower quality) and set
      `degraded['tool_result_cache']='local'`

  cap.t08.deadline.deadline_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `deadline_scheduling` (documented, slower, lower quality) and set
      `degraded['deadline_scheduling']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - quality-knob inventory with measured latency/quality effects
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - user-declared preference honoring with transparency
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - closed-loop control with stability guarantees
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured SLO attainment across preference settings
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 11000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.adaptive.adaptive_quality@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 11000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0431_adaptive_quality.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0432-slo-manager

**P0432 · `slo_manager` — SLO Definition, Tracking & Error Budgets** · [spec](PART_SPECS_T09.md#p0432-slo-manager) · [self-contained txt](../prompts/P0432_slo_manager.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0432  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0432 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0432  (32/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : SLO Definition, Tracking & Error Budgets
file         : parts/t09_latency/P0432_slo_manager.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.slo_manager
language     : Rust 1.86
capability   : cap.t09.slo.slo_manager@1
determinism  : io
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Turns latency goals into enforced engineering constraints.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. SLO/SLI definitions per endpoint and request class
  2. error-budget accounting and burn-rate alerting
  3. automatic degradation when budget burns too fast
  4. SLO-attainment reporting with statistical rigor

Expanded obligations:
  1. Implement SLO/SLI definitions per endpoint and request class as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement error-budget accounting and burn-rate alerting, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement automatic degradation when budget burns too fast with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement SLO-attainment reporting with statistical rigor together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.slo.slo_manager@1
  cap.t09.slo.slo_manager.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.adaptive.adaptive_quality@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_quality` (documented, slower, lower quality) and set
      `degraded['adaptive_quality']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t07.temporal.temporal_memory@1
      if unavailable: use the in-file conservative substitute for
      `temporal_memory` (documented, slower, lower quality) and set
      `degraded['temporal_memory']='local'`

  cap.t08.engine.engine_determinism@1
      if unavailable: use the in-file conservative substitute for
      `engine_determinism` (documented, slower, lower quality) and set
      `degraded['engine_determinism']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - SLO/SLI definitions per endpoint and request class
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - error-budget accounting and burn-rate alerting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic degradation when budget burns too fast
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - SLO-attainment reporting with statistical rigor
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 12000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.slo.slo_manager@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 12000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0432_slo_manager.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0433-latency-regression-gate

**P0433 · `latency_regression_gate` — Latency Regression Gate for 1000 Parts** · [spec](PART_SPECS_T09.md#p0433-latency-regression-gate) · [self-contained txt](../prompts/P0433_latency_regression_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0433  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0433 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0433  (33/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Latency Regression Gate for 1000 Parts
file         : parts/t09_latency/P0433_latency_regression_gate.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.latency_regression_gate
language     : Rust 1.86
capability   : cap.t09.latency.latency_regression_gate@1
determinism  : io
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
No part can slow the system down without being caught.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-part latency budget enforcement in CI
  2. statistical change detection resistant to machine noise
  3. attribution of end-to-end regressions to specific parts
  4. gate false-positive/false-negative measurement

Expanded obligations:
  1. Implement per-part latency budget enforcement in CI, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement statistical change detection resistant to machine noise with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement attribution of end-to-end regressions to specific parts
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement gate false-positive/false-negative measurement as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.latency.latency_regression_gate@1
  cap.t09.latency.latency_regression_gate.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.slo.slo_manager@1
      if unavailable: use the in-file conservative substitute for
      `slo_manager` (documented, slower, lower quality) and set
      `degraded['slo_manager']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t07.memory.memory_bench@1
      if unavailable: use the in-file conservative substitute for
      `memory_bench` (documented, slower, lower quality) and set
      `degraded['memory_bench']='local'`

  cap.t08.engine.engine_config_tuning@1
      if unavailable: use the in-file conservative substitute for
      `engine_config_tuning` (documented, slower, lower quality) and set
      `degraded['engine_config_tuning']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - per-part latency budget enforcement in CI
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - statistical change detection resistant to machine noise
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - attribution of end-to-end regressions to specific parts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - gate false-positive/false-negative measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 13000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.latency.latency_regression_gate@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 13000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0433_latency_regression_gate.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0434-perf-ci

**P0434 · `perf_ci` — Continuous Performance Integration** · [spec](PART_SPECS_T09.md#p0434-perf-ci) · [self-contained txt](../prompts/P0434_perf_ci.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0434  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0434 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0434  (34/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Continuous Performance Integration
file         : parts/t09_latency/P0434_perf_ci.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.perf_ci
language     : Rust 1.86
capability   : cap.t09.perf.perf_ci@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Performance is tested as rigorously as correctness.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. reproducible benchmark environment definition and fingerprinting
  2. per-commit measurement with variance control
  3. historical performance database and trend analysis
  4. automated bisection of performance regressions

Expanded obligations:
  1. Implement reproducible benchmark environment definition and
     fingerprinting with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement per-commit measurement with variance control together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement historical performance database and trend analysis as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement automated bisection of performance regressions, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.perf.perf_ci@1
  cap.t09.perf.perf_ci.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.latency.latency_regression_gate@1
      if unavailable: use the in-file conservative substitute for
      `latency_regression_gate` (documented, slower, lower quality) and set
      `degraded['latency_regression_gate']='local'`

  cap.t07.kv.kv_paging@1
      if unavailable: use the in-file conservative substitute for
      `kv_paging` (documented, slower, lower quality) and set
      `degraded['kv_paging']='local'`

  cap.t08.continuous.continuous_batching@1
      if unavailable: use the in-file conservative substitute for
      `continuous_batching` (documented, slower, lower quality) and set
      `degraded['continuous_batching']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - reproducible benchmark environment definition and fingerprinting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-commit measurement with variance control
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - historical performance database and trend analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - automated bisection of performance regressions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 14000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.perf.perf_ci@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 14000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0434_perf_ci.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0435-flamegraph-tooling

**P0435 · `flamegraph_tooling` — Profiling & Flamegraph Analysis Tooling** · [spec](PART_SPECS_T09.md#p0435-flamegraph-tooling) · [self-contained txt](../prompts/P0435_flamegraph_tooling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0435  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0435 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0435  (35/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Profiling & Flamegraph Analysis Tooling
file         : parts/t09_latency/P0435_flamegraph_tooling.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.flamegraph_tooling
language     : Rust 1.86
capability   : cap.t09.flamegraph.flamegraph_tooling@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Finds the next optimisation without guessing.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. low-overhead sampling profiler with symbolisation across languages
  2. differential flamegraph comparison between versions
  3. automatic hotspot ranking with estimated payoff
  4. profiler-overhead measurement under 1%

Expanded obligations:
  1. Implement low-overhead sampling profiler with symbolisation across
     languages together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against CursorBench 3.2 — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement differential flamegraph comparison between versions as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement automatic hotspot ranking with estimated payoff, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement profiler-overhead measurement under 1% with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.flamegraph.flamegraph_tooling@1
  cap.t09.flamegraph.flamegraph_tooling.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.perf.perf_ci@1
      if unavailable: use the in-file conservative substitute for `perf_ci`
      (documented, slower, lower quality) and set
      `degraded['perf_ci']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t07.semantic.semantic_memory@1
      if unavailable: use the in-file conservative substitute for
      `semantic_memory` (documented, slower, lower quality) and set
      `degraded['semantic_memory']='local'`

  cap.t08.cascade.cascade_tree_verify@1
      if unavailable: use the in-file conservative substitute for
      `cascade_tree_verify` (documented, slower, lower quality) and set
      `degraded['cascade_tree_verify']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - low-overhead sampling profiler with symbolisation across languag
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - differential flamegraph comparison between versions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic hotspot ranking with estimated payoff
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - profiler-overhead measurement under 1%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 15000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.flamegraph.flamegraph_tooling@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 15000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0435_flamegraph_tooling.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0436-bottleneck-analyser

**P0436 · `bottleneck_analyser` — Automatic Bottleneck Analyser** · [spec](PART_SPECS_T09.md#p0436-bottleneck-analyser) · [self-contained txt](../prompts/P0436_bottleneck_analyser.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0436  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0436 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0436  (36/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Automatic Bottleneck Analyser
file         : parts/t09_latency/P0436_bottleneck_analyser.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.bottleneck_analyser
language     : Rust 1.86
capability   : cap.t09.bottleneck.bottleneck_analyser@1
determinism  : io
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Tells engineers exactly what to fix next, ranked by payoff.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. queueing-network model fitted to telemetry
  2. bottleneck identification with sensitivity analysis
  3. prioritised recommendation list with projected gains
  4. prediction accuracy validation on applied fixes

Expanded obligations:
  1. Implement queueing-network model fitted to telemetry as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement bottleneck identification with sensitivity analysis, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement prioritised recommendation list with projected gains with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement prediction accuracy validation on applied fixes together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.bottleneck.bottleneck_analyser@1
  cap.t09.bottleneck.bottleneck_analyser.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.flamegraph.flamegraph_tooling@1
      if unavailable: use the in-file conservative substitute for
      `flamegraph_tooling` (documented, slower, lower quality) and set
      `degraded['flamegraph_tooling']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t07.query.query_reformulation@1
      if unavailable: use the in-file conservative substitute for
      `query_reformulation` (documented, slower, lower quality) and set
      `degraded['query_reformulation']='local'`

  cap.t08.prefix.prefix_cache_runtime@1
      if unavailable: use the in-file conservative substitute for
      `prefix_cache_runtime` (documented, slower, lower quality) and set
      `degraded['prefix_cache_runtime']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - queueing-network model fitted to telemetry
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - bottleneck identification with sensitivity analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - prioritised recommendation list with projected gains
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - prediction accuracy validation on applied fixes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 16000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.bottleneck.bottleneck_analyser@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 16000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0436_bottleneck_analyser.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0437-throughput-optimiser

**P0437 · `throughput_optimiser` — Throughput Optimisation Engine** · [spec](PART_SPECS_T09.md#p0437-throughput-optimiser) · [self-contained txt](../prompts/P0437_throughput_optimiser.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0437  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0437 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0437  (37/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Throughput Optimisation Engine
file         : parts/t09_latency/P0437_throughput_optimiser.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.throughput_optimiser
language     : Rust 1.86
capability   : cap.t09.throughput.throughput_optimiser@1
determinism  : io
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Maximises tokens per dollar at fixed latency.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capacity-planning model coupling batching, sparsity and precision
  2. constrained optimisation with SLO feasibility checking
  3. measured tokens-per-dollar improvement
  4. sensitivity to traffic-mix changes

Expanded obligations:
  1. Implement capacity-planning model coupling batching, sparsity and
     precision, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement constrained optimisation with SLO feasibility checking with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement measured tokens-per-dollar improvement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement sensitivity to traffic-mix changes as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.throughput.throughput_optimiser@1
  cap.t09.throughput.throughput_optimiser.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.bottleneck.bottleneck_analyser@1
      if unavailable: use the in-file conservative substitute for
      `bottleneck_analyser` (documented, slower, lower quality) and set
      `degraded['bottleneck_analyser']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t07.memory.memory_privacy@1
      if unavailable: use the in-file conservative substitute for
      `memory_privacy` (documented, slower, lower quality) and set
      `degraded['memory_privacy']='local'`

  cap.t08.batch.batch_invariance@1
      if unavailable: use the in-file conservative substitute for
      `batch_invariance` (documented, slower, lower quality) and set
      `degraded['batch_invariance']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - capacity-planning model coupling batching, sparsity and precisio
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - constrained optimisation with SLO feasibility checking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - measured tokens-per-dollar improvement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - sensitivity to traffic-mix changes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 17000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.throughput.throughput_optimiser@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 17000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0437_throughput_optimiser.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0438-energy-efficiency

**P0438 · `energy_efficiency` — Energy per Token Optimisation** · [spec](PART_SPECS_T09.md#p0438-energy-efficiency) · [self-contained txt](../prompts/P0438_energy_efficiency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0438  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0438 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0438  (38/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Energy per Token Optimisation
file         : parts/t09_latency/P0438_energy_efficiency.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.energy_efficiency
language     : Rust 1.86
capability   : cap.t09.energy.energy_efficiency@1
determinism  : io
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Speed that does not come from burning more power.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. joules-per-token measurement methodology and instrumentation
  2. frequency/precision/sparsity joint optimisation for efficiency
  3. carbon accounting integration
  4. measured efficiency improvement at matched quality

Expanded obligations:
  1. Implement joules-per-token measurement methodology and instrumentation
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement frequency/precision/sparsity joint optimisation for efficiency
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement carbon accounting integration as a first-class, fully realised
     mechanism. No stub, no `NotImplementedError`, no configuration flag
     whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement measured efficiency improvement at matched quality, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.energy.energy_efficiency@1
  cap.t09.energy.energy_efficiency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.throughput.throughput_optimiser@1
      if unavailable: use the in-file conservative substitute for
      `throughput_optimiser` (documented, slower, lower quality) and set
      `degraded['throughput_optimiser']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t07.semantic.semantic_cache@1
      if unavailable: use the in-file conservative substitute for
      `semantic_cache` (documented, slower, lower quality) and set
      `degraded['semantic_cache']='local'`

  cap.t08.cancellation.cancellation@1
      if unavailable: use the in-file conservative substitute for
      `cancellation` (documented, slower, lower quality) and set
      `degraded['cancellation']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - joules-per-token measurement methodology and instrumentation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - frequency/precision/sparsity joint optimisation for efficiency
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - carbon accounting integration
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured efficiency improvement at matched quality
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 18000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.energy.energy_efficiency@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 18000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0438_energy_efficiency.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0439-cost-optimiser

**P0439 · `cost_optimiser` — Cost per Solved Task Optimiser** · [spec](PART_SPECS_T09.md#p0439-cost-optimiser) · [self-contained txt](../prompts/P0439_cost_optimiser.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0439  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0439 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0439  (39/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Cost per Solved Task Optimiser
file         : parts/t09_latency/P0439_cost_optimiser.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.cost_optimiser
language     : Rust 1.86
capability   : cap.t09.cost.cost_optimiser@1
determinism  : io
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The only metric that matters: dollars per correct answer.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cost-per-success accounting including retries and verification
  2. policy optimisation over model tier, search depth and tools
  3. comparison against Opus 5 published pricing on identical tasks
  4. target: 100x cheaper per solved task on the benchmark suite

Expanded obligations:
  1. Implement cost-per-success accounting including retries and verification
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement policy optimisation over model tier, search depth and tools as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement comparison against Opus 5 published pricing on identical
     tasks, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     CursorBench 3.2 — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement target: 100x cheaper per solved task on the benchmark suite
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.cost.cost_optimiser@1
  cap.t09.cost.cost_optimiser.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.energy.energy_efficiency@1
      if unavailable: use the in-file conservative substitute for
      `energy_efficiency` (documented, slower, lower quality) and set
      `degraded['energy_efficiency']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t07.graph.graph_memory_queries@1
      if unavailable: use the in-file conservative substitute for
      `graph_memory_queries` (documented, slower, lower quality) and set
      `degraded['graph_memory_queries']='local'`

  cap.t08.overload.overload_shedding@1
      if unavailable: use the in-file conservative substitute for
      `overload_shedding` (documented, slower, lower quality) and set
      `degraded['overload_shedding']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - cost-per-success accounting including retries and verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - policy optimisation over model tier, search depth and tools
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - comparison against Opus 5 published pricing on identical tasks
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: 100x cheaper per solved task on the benchmark suite
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 19000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.cost.cost_optimiser@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 19000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0439_cost_optimiser.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0440-capacity-planner

**P0440 · `capacity_planner` — Capacity Planning & Headroom Model** · [spec](PART_SPECS_T09.md#p0440-capacity-planner) · [self-contained txt](../prompts/P0440_capacity_planner.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0440  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0440 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0440  (40/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Capacity Planning & Headroom Model
file         : parts/t09_latency/P0440_capacity_planner.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.capacity_planner
language     : Rust 1.86
capability   : cap.t09.capacity.capacity_planner@1
determinism  : io
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Enough capacity, never too much.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. demand forecasting with uncertainty quantification
  2. headroom policy derived from failure and burst analysis
  3. cost-of-headroom versus risk-of-shortfall tradeoff
  4. forecast accuracy measurement

Expanded obligations:
  1. Implement demand forecasting with uncertainty quantification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement headroom policy derived from failure and burst analysis, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     CursorBench 3.2 — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement cost-of-headroom versus risk-of-shortfall tradeoff with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement forecast accuracy measurement together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. This mechanism sits on the critical
     path of CursorBench 3.2, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.capacity.capacity_planner@1
  cap.t09.capacity.capacity_planner.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.cost.cost_optimiser@1
      if unavailable: use the in-file conservative substitute for
      `cost_optimiser` (documented, slower, lower quality) and set
      `degraded['cost_optimiser']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t07.provenance.provenance_tracking@1
      if unavailable: use the in-file conservative substitute for
      `provenance_tracking` (documented, slower, lower quality) and set
      `degraded['provenance_tracking']='local'`

  cap.t08.cascade.cascade_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `cascade_speed_proof` (documented, slower, lower quality) and set
      `degraded['cascade_speed_proof']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - demand forecasting with uncertainty quantification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - headroom policy derived from failure and burst analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cost-of-headroom versus risk-of-shortfall tradeoff
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - forecast accuracy measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 20000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.capacity.capacity_planner@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 20000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0440_capacity_planner.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0441-cache-sizing

**P0441 · `cache_sizing` — Cache Sizing & Memory Allocation Optimiser** · [spec](PART_SPECS_T09.md#p0441-cache-sizing) · [self-contained txt](../prompts/P0441_cache_sizing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0441  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0441 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0441  (41/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Cache Sizing & Memory Allocation Optimiser
file         : parts/t09_latency/P0441_cache_sizing.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.cache_sizing
language     : Rust 1.86
capability   : cap.t09.cache.cache_sizing@1
determinism  : io
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Splits limited memory across ten caches optimally.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. marginal-hit-rate curves per cache measured online
  2. global allocation solver maximising total value
  3. dynamic reallocation with hysteresis
  4. measured improvement over fixed allocation

Expanded obligations:
  1. Implement marginal-hit-rate curves per cache measured online, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement global allocation solver maximising total value with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement dynamic reallocation with hysteresis together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured improvement over fixed allocation as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Terminal-Bench
     2.1 — a regression on that benchmark is an automatic rejection of this
     part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.cache.cache_sizing@1
  cap.t09.cache.cache_sizing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.capacity.capacity_planner@1
      if unavailable: use the in-file conservative substitute for
      `capacity_planner` (documented, slower, lower quality) and set
      `degraded['capacity_planner']='local'`

  cap.t07.kv.kv_hierarchy@1
      if unavailable: use the in-file conservative substitute for
      `kv_hierarchy` (documented, slower, lower quality) and set
      `degraded['kv_hierarchy']='local'`

  cap.t08.engine.engine_core@1
      if unavailable: use the in-file conservative substitute for
      `engine_core` (documented, slower, lower quality) and set
      `degraded['engine_core']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - marginal-hit-rate curves per cache measured online
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - global allocation solver maximising total value
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - dynamic reallocation with hysteresis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured improvement over fixed allocation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 21000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.cache.cache_sizing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 21000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0441_cache_sizing.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0442-speculation-budget

**P0442 · `speculation_budget` — Speculation Budget Governor** · [spec](PART_SPECS_T09.md#p0442-speculation-budget) · [self-contained txt](../prompts/P0442_speculation_budget.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0442  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0442 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0442  (42/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Speculation Budget Governor
file         : parts/t09_latency/P0442_speculation_budget.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.speculation_budget
language     : Rust 1.86
capability   : cap.t09.speculation.speculation_budget@1
determinism  : io
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Speculation must never cost more than it saves.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. global speculation budget with per-source accounting
  2. value-of-speculation estimation and dynamic throttling
  3. wasted-work measurement across all speculative subsystems
  4. net-benefit verification with confidence intervals

Expanded obligations:
  1. Implement global speculation budget with per-source accounting with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement value-of-speculation estimation and dynamic throttling
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement wasted-work measurement across all speculative subsystems as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement net-benefit verification with confidence intervals, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.speculation.speculation_budget@1
  cap.t09.speculation.speculation_budget.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.cache.cache_sizing@1
      if unavailable: use the in-file conservative substitute for
      `cache_sizing` (documented, slower, lower quality) and set
      `degraded['cache_sizing']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t07.episodic.episodic_memory@1
      if unavailable: use the in-file conservative substitute for
      `episodic_memory` (documented, slower, lower quality) and set
      `degraded['episodic_memory']='local'`

  cap.t08.cascade.cascade_stage3_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage3_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage3_draft']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - global speculation budget with per-source accounting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - value-of-speculation estimation and dynamic throttling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - wasted-work measurement across all speculative subsystems
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - net-benefit verification with confidence intervals
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 22000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.speculation.speculation_budget@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 22000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0442_speculation_budget.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0443-latency-simulator

**P0443 · `latency_simulator` — Latency Simulator & What-If Engine** · [spec](PART_SPECS_T09.md#p0443-latency-simulator) · [self-contained txt](../prompts/P0443_latency_simulator.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0443  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0443 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0443  (43/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Latency Simulator & What-If Engine
file         : parts/t09_latency/P0443_latency_simulator.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.latency_simulator
language     : Rust 1.86
capability   : cap.t09.latency.latency_simulator@1
determinism  : io
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Tests optimisation ideas before building them.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. discrete-event simulation of the full request path
  2. calibration against production measurements with error bounds
  3. what-if scenario library for planned changes
  4. prediction-accuracy validation on implemented changes

Expanded obligations:
  1. Implement discrete-event simulation of the full request path together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement calibration against production measurements with error bounds
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement what-if scenario library for planned changes, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement prediction-accuracy validation on implemented changes with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.latency.latency_simulator@1
  cap.t09.latency.latency_simulator.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.speculation.speculation_budget@1
      if unavailable: use the in-file conservative substitute for
      `speculation_budget` (documented, slower, lower quality) and set
      `degraded['speculation_budget']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t07.hybrid.hybrid_retrieval@1
      if unavailable: use the in-file conservative substitute for
      `hybrid_retrieval` (documented, slower, lower quality) and set
      `degraded['hybrid_retrieval']='local'`

  cap.t08.paged.paged_attention_runtime@1
      if unavailable: use the in-file conservative substitute for
      `paged_attention_runtime` (documented, slower, lower quality) and set
      `degraded['paged_attention_runtime']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - discrete-event simulation of the full request path
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - calibration against production measurements with error bounds
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - what-if scenario library for planned changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - prediction-accuracy validation on implemented changes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 23000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.latency.latency_simulator@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 23000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0443_latency_simulator.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0444-benchmark-speed-public

**P0444 · `benchmark_speed_public` — Public Speed Comparison Harness** · [spec](PART_SPECS_T09.md#p0444-benchmark-speed-public) · [self-contained txt](../prompts/P0444_benchmark_speed_public.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0444  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0444 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0444  (44/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Public Speed Comparison Harness
file         : parts/t09_latency/P0444_benchmark_speed_public.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.benchmark_speed_public
language     : Rust 1.86
capability   : cap.t09.benchmark.benchmark_speed_public@1
determinism  : io
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Reproducible, fair, third-party-verifiable speed comparisons.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. identical-task-set methodology against Opus-class baselines
  2. measurement of wall-clock, tokens, cost and quality together
  3. publication-ready result artifacts with full provenance
  4. independent-reproduction instructions

Expanded obligations:
  1. Implement identical-task-set methodology against Opus-class baselines as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement measurement of wall-clock, tokens, cost and quality together,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     CursorBench 3.2 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement publication-ready result artifacts with full provenance with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement independent-reproduction instructions together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.benchmark.benchmark_speed_public@1
  cap.t09.benchmark.benchmark_speed_public.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.latency.latency_simulator@1
      if unavailable: use the in-file conservative substitute for
      `latency_simulator` (documented, slower, lower quality) and set
      `degraded['latency_simulator']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t07.conflict.conflict_resolution@1
      if unavailable: use the in-file conservative substitute for
      `conflict_resolution` (documented, slower, lower quality) and set
      `degraded['conflict_resolution']='local'`

  cap.t08.streaming.streaming_output@1
      if unavailable: use the in-file conservative substitute for
      `streaming_output` (documented, slower, lower quality) and set
      `degraded['streaming_output']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - identical-task-set methodology against Opus-class baselines
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - measurement of wall-clock, tokens, cost and quality together
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - publication-ready result artifacts with full provenance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - independent-reproduction instructions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 24000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.benchmark.benchmark_speed_public@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 24000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0444_benchmark_speed_public.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0445-realtime-mode

**P0445 · `realtime_mode` — Real-Time & Voice-Latency Mode** · [spec](PART_SPECS_T09.md#p0445-realtime-mode) · [self-contained txt](../prompts/P0445_realtime_mode.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0445  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0445 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0445  (45/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Real-Time & Voice-Latency Mode
file         : parts/t09_latency/P0445_realtime_mode.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.realtime_mode
language     : Rust 1.86
capability   : cap.t09.realtime.realtime_mode@1
determinism  : io
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Sub-100ms interaction for conversational and control use.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. streaming input processing with incremental commitment
  2. barge-in handling and partial-hypothesis revision
  3. end-to-end audio-to-audio latency measurement
  4. quality-at-latency measurement versus batch mode

Expanded obligations:
  1. Implement streaming input processing with incremental commitment, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     CursorBench 3.2 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement barge-in handling and partial-hypothesis revision with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement end-to-end audio-to-audio latency measurement together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement quality-at-latency measurement versus batch mode as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.realtime.realtime_mode@1
  cap.t09.realtime.realtime_mode.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.benchmark.benchmark_speed_public@1
      if unavailable: use the in-file conservative substitute for
      `benchmark_speed_public` (documented, slower, lower quality) and set
      `degraded['benchmark_speed_public']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t07.cache.cache_warm_predict@1
      if unavailable: use the in-file conservative substitute for
      `cache_warm_predict` (documented, slower, lower quality) and set
      `degraded['cache_warm_predict']='local'`

  cap.t08.request.request_lifecycle@1
      if unavailable: use the in-file conservative substitute for
      `request_lifecycle` (documented, slower, lower quality) and set
      `degraded['request_lifecycle']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - streaming input processing with incremental commitment
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - barge-in handling and partial-hypothesis revision
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - end-to-end audio-to-audio latency measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - quality-at-latency measurement versus batch mode
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 25000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.realtime.realtime_mode@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 25000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0445_realtime_mode.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0446-burst-handling

**P0446 · `burst_handling` — Burst Absorption & Queue Shaping** · [spec](PART_SPECS_T09.md#p0446-burst-handling) · [self-contained txt](../prompts/P0446_burst_handling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0446  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0446 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0446  (46/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Burst Absorption & Queue Shaping
file         : parts/t09_latency/P0446_burst_handling.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.burst_handling
language     : Rust 1.86
capability   : cap.t09.burst.burst_handling@1
determinism  : io
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
A 100x traffic spike is a bump, not an outage.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. burst detection and rapid capacity engagement
  2. queue shaping with explicit wait-time communication
  3. priority preservation during bursts
  4. measured behaviour under synthetic 100x spikes

Expanded obligations:
  1. Implement burst detection and rapid capacity engagement with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement queue shaping with explicit wait-time communication together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement priority preservation during bursts as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured behaviour under synthetic 100x spikes, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.burst.burst_handling@1
  cap.t09.burst.burst_handling.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.realtime.realtime_mode@1
      if unavailable: use the in-file conservative substitute for
      `realtime_mode` (documented, slower, lower quality) and set
      `degraded['realtime_mode']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t07.memory.memory_replication@1
      if unavailable: use the in-file conservative substitute for
      `memory_replication` (documented, slower, lower quality) and set
      `degraded['memory_replication']='local'`

  cap.t08.autoscaling.autoscaling@1
      if unavailable: use the in-file conservative substitute for
      `autoscaling` (documented, slower, lower quality) and set
      `degraded['autoscaling']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - burst detection and rapid capacity engagement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - queue shaping with explicit wait-time communication
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - priority preservation during bursts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured behaviour under synthetic 100x spikes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 26000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.burst.burst_handling@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 26000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0446_burst_handling.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0447-degradation-ladder

**P0447 · `degradation_ladder` — Formal Degradation Ladder** · [spec](PART_SPECS_T09.md#p0447-degradation-ladder) · [self-contained txt](../prompts/P0447_degradation_ladder.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0447  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0447 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0447  (47/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Formal Degradation Ladder
file         : parts/t09_latency/P0447_degradation_ladder.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.degradation_ladder
language     : Rust 1.86
capability   : cap.t09.degradation.degradation_ladder@1
determinism  : io
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Exactly how quality is traded for availability, documented.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. ordered degradation steps with measured quality/latency effects
  2. automatic trigger conditions and recovery criteria
  3. user-visible signalling of the active degradation level
  4. verification that each step behaves as specified

Expanded obligations:
  1. Implement ordered degradation steps with measured quality/latency
     effects together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against CursorBench 3.2 — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement automatic trigger conditions and recovery criteria as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement user-visible signalling of the active degradation level, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement verification that each step behaves as specified with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.degradation.degradation_ladder@1
  cap.t09.degradation.degradation_ladder.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.burst.burst_handling@1
      if unavailable: use the in-file conservative substitute for
      `burst_handling` (documented, slower, lower quality) and set
      `degraded['burst_handling']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t07.dedup.dedup_engine@1
      if unavailable: use the in-file conservative substitute for
      `dedup_engine` (documented, slower, lower quality) and set
      `degraded['dedup_engine']='local'`

  cap.t08.engine.engine_bench_serving@1
      if unavailable: use the in-file conservative substitute for
      `engine_bench_serving` (documented, slower, lower quality) and set
      `degraded['engine_bench_serving']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - ordered degradation steps with measured quality/latency effects
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automatic trigger conditions and recovery criteria
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - user-visible signalling of the active degradation level
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification that each step behaves as specified
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 27000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.degradation.degradation_ladder@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 27000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0447_degradation_ladder.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0448-latency-dashboard

**P0448 · `latency_dashboard` — Latency & Cost Observability Artifacts** · [spec](PART_SPECS_T09.md#p0448-latency-dashboard) · [self-contained txt](../prompts/P0448_latency_dashboard.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0448  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0448 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0448  (48/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Latency & Cost Observability Artifacts
file         : parts/t09_latency/P0448_latency_dashboard.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.latency_dashboard
language     : Rust 1.86
capability   : cap.t09.latency.latency_dashboard@1
determinism  : io
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
One place to see whether the 100x claim still holds.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. metric definitions, aggregation rules and export schemas
  2. per-part and per-phase drilldown data products
  3. regression and anomaly annotation
  4. operator-task usability validation

Expanded obligations:
  1. Implement metric definitions, aggregation rules and export schemas as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement per-part and per-phase drilldown data products, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement regression and anomaly annotation with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement operator-task usability validation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.latency.latency_dashboard@1
  cap.t09.latency.latency_dashboard.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.degradation.degradation_ladder@1
      if unavailable: use the in-file conservative substitute for
      `degradation_ladder` (documented, slower, lower quality) and set
      `degraded['degradation_ladder']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t07.memory.memory_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `memory_spec_doc` (documented, slower, lower quality) and set
      `degraded['memory_spec_doc']='local'`

  cap.t08.engine.engine_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `engine_spec_doc` (documented, slower, lower quality) and set
      `degraded['engine_spec_doc']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - metric definitions, aggregation rules and export schemas
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-part and per-phase drilldown data products
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regression and anomaly annotation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - operator-task usability validation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 28000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.latency.latency_dashboard@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 28000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0448_latency_dashboard.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0449-speed-proof-report

**P0449 · `speed_proof_report` — The 100x Speed Proof Report Generator** · [spec](PART_SPECS_T09.md#p0449-speed-proof-report) · [self-contained txt](../prompts/P0449_speed_proof_report.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0449  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0449 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0449  (49/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : The 100x Speed Proof Report Generator
file         : parts/t09_latency/P0449_speed_proof_report.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.speed_proof_report
language     : Rust 1.86
capability   : cap.t09.speed.speed_proof_report@1
determinism  : io
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
Generates the auditable document proving 100x versus Opus 5.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. measurement collection across all six speed sources
  2. task-matched wall-clock comparison methodology
  3. statistical treatment with confidence intervals and caveats
  4. reproducibility package with scripts and raw data

Expanded obligations:
  1. Implement measurement collection across all six speed sources, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement task-matched wall-clock comparison methodology with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement statistical treatment with confidence intervals and caveats
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement reproducibility package with scripts and raw data as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.speed.speed_proof_report@1
  cap.t09.speed.speed_proof_report.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.latency.latency_dashboard@1
      if unavailable: use the in-file conservative substitute for
      `latency_dashboard` (documented, slower, lower quality) and set
      `degraded['latency_dashboard']='local'`

  cap.t07.summarisation.summarisation_memory@1
      if unavailable: use the in-file conservative substitute for
      `summarisation_memory` (documented, slower, lower quality) and set
      `degraded['summarisation_memory']='local'`

  cap.t08.cascade.cascade_stage2_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage2_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage2_draft']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - measurement collection across all six speed sources
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - task-matched wall-clock comparison methodology
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - statistical treatment with confidence intervals and caveats
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - reproducibility package with scripts and raw data
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 29000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.speed.speed_proof_report@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 29000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0449_speed_proof_report.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0450-latency-spec-doc

**P0450 · `latency_spec_doc` — Latency Engineering Specification & Runbook** · [spec](PART_SPECS_T09.md#p0450-latency-spec-doc) · [self-contained txt](../prompts/P0450_latency_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0450  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0450 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0450  (50/50 of tier T09)
tier         : T09 — Latency Engineering & Ω-Memoize
title        : Latency Engineering Specification & Runbook
file         : parts/t09_latency/P0450_latency_spec_doc.rs          <-- create exactly this path, nothing else
module       : hyperion.t09.latency.latency_spec_doc
language     : Rust 1.86
capability   : cap.t09.latency.latency_spec_doc@1
determinism  : io
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1, CursorBench 3.2

MISSION
-------
The authoritative description of all latency machinery.

Tier context:
  Semantic caching, precomputation, early exit, distilled fast paths and the
  100x latency accounting system. Sources S4 and S6.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. specification of budgets, SLOs, caches and degradation modes
  2. auto-generated budget tables per part and phase
  3. incident runbook for latency regressions
  4. spec-versus-implementation drift detection

Expanded obligations:
  1. Implement specification of budgets, SLOs, caches and degradation modes
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement auto-generated budget tables per part and phase together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement incident runbook for latency regressions as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement spec-versus-implementation drift detection, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
--------------------------------------------------------------------------
  PART_MANIFEST      : a frozen mapping with keys
                       part_id, capability, provides, requires, determinism,
                       latency_ns, loc, contract_version, schema_hash
  register(bus)      : idempotent; publishes `provides` on the Ω-Bus; returns a
                       teardown handle; MUST NOT fail if `requires` are missing
  selftest()         : -> (ok: bool, report: dict); offline; < 60 s; runs in
                       degraded mode when the bus is empty
  microbench(iters)  : -> dict with p50/p99/throughput; asserts
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t09.latency.latency_spec_doc@1
  cap.t09.latency.latency_spec_doc.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t09.speed.speed_proof_report@1
      if unavailable: use the in-file conservative substitute for
      `speed_proof_report` (documented, slower, lower quality) and set
      `degraded['speed_proof_report']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t07.sparse.sparse_retrieval@1
      if unavailable: use the in-file conservative substitute for
      `sparse_retrieval` (documented, slower, lower quality) and set
      `degraded['sparse_retrieval']='local'`

  cap.t08.cascade.cascade_tuning@1
      if unavailable: use the in-file conservative substitute for
      `cascade_tuning` (documented, slower, lower quality) and set
      `degraded['cascade_tuning']='local'`

DETERMINISM
-----------
  io — the part may touch time, devices, sockets or subprocesses, but every
  such touch goes through an injected effect handle so that selftest() runs
  fully offline against a deterministic fake, and a replay log can reproduce
  any production trace.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - specification of budgets, SLOs, caches and degradation modes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - auto-generated budget tables per part and phase
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - incident runbook for latency regressions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - spec-versus-implementation drift detection
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
                     Proves the declared determinism class holds.
  12. [ 440 lines] In-file test suite: >= 40 cases (unit + boundary + regression)
                     pytest/cfg(test)/vitest style per language, no shared fixtures,
                     offline.
  13. [ 250 lines] Property-based tests for every stated invariant
                     Generators + shrinkers; each invariant named in a comment.
  14. [ 170 lines] Adversarial / fuzz tests
                     Coverage-guided in-process fuzzing within the 60s budget.
  15. [ 180 lines] Microbenchmark + latency-budget assertion
                     Asserts p99 <= 30000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Rust 1.86)
------------------------------------------------------------------------------
  tests   : `#[cfg(test)] mod tests` inside the same file, plus `#[bench]`-style criterion-free microbench harness
  format  : rustfmt default + clippy::pedantic clean
  typing  : no `unsafe` outside explicitly documented `// SAFETY:` blocks; every public item documented
  deps    : core+std only, plus optional `libc` behind a feature flag

HARD PROHIBITIONS
-----------------
  * Do NOT import, reference, read or guess the contents of any other parts/** file.
  * Do NOT create, rename or delete any file other than your own.
  * No TODO, FIXME, 'pass  # later', NotImplementedError, or empty except.
  * No global mutable state; no module-level side effects; no printing outside a
    debug guard; no network in selftest(); no wall-clock/RNG outside your class.
  * Do not shorten the file by deleting tests. The line map is the contract.

SELF-VERIFICATION BEFORE YOU EMIT (answer each internally, then fix)
-------------------------------------------------------------------
  1. Does the contract header appear verbatim, and does PART_MANIFEST match this prompt
     exactly (capability == cap.t09.latency.latency_spec_doc@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 30000 ns?
  6. Is the declared determinism class `io` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t09_latency/P0450_latency_spec_doc.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
