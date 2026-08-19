# HYPERION-Ω — Worker prompts · T08 · Inference Engine & Ω-Cascade

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

## PROMPT p0351-engine-core

**P0351 · `engine_core` — Inference Engine Core Loop** · [spec](PART_SPECS_T08.md#p0351-engine-core) · [self-contained txt](../prompts/P0351_engine_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0351  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0351 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0351  (1/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Inference Engine Core Loop
file         : parts/t08_inference/P0351_engine_core.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_core
language     : Rust 1.86
capability   : cap.t08.engine.engine_core@1
determinism  : io
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
The top-level serving loop: admit, schedule, step, emit, retire.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. single-threaded-decision / multi-threaded-execution architecture
  2. step-loop with bounded per-iteration work for predictable latency
  3. state machine per sequence with explicit legal transitions
  4. throughput and p99 latency budget assertions

Expanded obligations:
  1. Implement single-threaded-decision / multi-threaded-execution
     architecture together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against Terminal-Bench 2.1 —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement step-loop with bounded per-iteration work for predictable
     latency as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement state machine per sequence with explicit legal transitions,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement throughput and p99 latency budget assertions with an explicit
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_core@1
  cap.t08.engine.engine_core.describe@1

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

  cap.t02.fused.fused_moe_kernel@1
      if unavailable: use the in-file conservative substitute for
      `fused_moe_kernel` (documented, slower, lower quality) and set
      `degraded['fused_moe_kernel']='local'`

  cap.t03.guard.guard_specialise@1
      if unavailable: use the in-file conservative substitute for
      `guard_specialise` (documented, slower, lower quality) and set
      `degraded['guard_specialise']='local'`

  cap.t04.network.network_congestion@1
      if unavailable: use the in-file conservative substitute for
      `network_congestion` (documented, slower, lower quality) and set
      `degraded['network_congestion']='local'`

  cap.t05.causal.causal_model@1
      if unavailable: use the in-file conservative substitute for
      `causal_model` (documented, slower, lower quality) and set
      `degraded['causal_model']='local'`

  cap.t06.conditional.conditional_layers@1
      if unavailable: use the in-file conservative substitute for
      `conditional_layers` (documented, slower, lower quality) and set
      `degraded['conditional_layers']='local'`

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
   3. [ 600 lines] Core implementation A - single-threaded-decision / multi-threaded-execution architecture
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - step-loop with bounded per-iteration work for predictable latenc
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - state machine per sequence with explicit legal transitions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput and p99 latency budget assertions
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
     exactly (capability == cap.t08.engine.engine_core@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0351_engine_core.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0352-continuous-batching

**P0352 · `continuous_batching` — Continuous Batching Scheduler** · [spec](PART_SPECS_T08.md#p0352-continuous-batching) · [self-contained txt](../prompts/P0352_continuous_batching.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0352  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0352 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0352  (2/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Continuous Batching Scheduler
file         : parts/t08_inference/P0352_continuous_batching.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.continuous_batching
language     : Rust 1.86
capability   : cap.t08.continuous.continuous_batching@1
determinism  : io
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Never waits for a batch: sequences join and leave every step.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. iteration-level scheduling with join/leave at any step
  2. batch-composition policy balancing prefill and decode work
  3. fairness and starvation prevention across sequences
  4. measured throughput gain versus static batching

Expanded obligations:
  1. Implement iteration-level scheduling with join/leave at any step as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement batch-composition policy balancing prefill and decode work,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement fairness and starvation prevention across sequences with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured throughput gain versus static batching together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.continuous.continuous_batching@1
  cap.t08.continuous.continuous_batching.describe@1

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

  cap.t08.engine.engine_core@1
      if unavailable: use the in-file conservative substitute for
      `engine_core` (documented, slower, lower quality) and set
      `degraded['engine_core']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t02.numa.numa_placement@1
      if unavailable: use the in-file conservative substitute for
      `numa_placement` (documented, slower, lower quality) and set
      `degraded['numa_placement']='local'`

  cap.t03.constant.constant_folding@1
      if unavailable: use the in-file conservative substitute for
      `constant_folding` (documented, slower, lower quality) and set
      `degraded['constant_folding']='local'`

  cap.t04.service.service_discovery@1
      if unavailable: use the in-file conservative substitute for
      `service_discovery` (documented, slower, lower quality) and set
      `degraded['service_discovery']='local'`

  cap.t05.distillation.distillation_arch@1
      if unavailable: use the in-file conservative substitute for
      `distillation_arch` (documented, slower, lower quality) and set
      `degraded['distillation_arch']='local'`

  cap.t06.moe.moe_training_stability@1
      if unavailable: use the in-file conservative substitute for
      `moe_training_stability` (documented, slower, lower quality) and set
      `degraded['moe_training_stability']='local'`

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
   3. [ 600 lines] Core implementation A - iteration-level scheduling with join/leave at any step
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - batch-composition policy balancing prefill and decode work
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - fairness and starvation prevention across sequences
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured throughput gain versus static batching
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
     exactly (capability == cap.t08.continuous.continuous_batching@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0352_continuous_batching.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0353-chunked-prefill

**P0353 · `chunked_prefill` — Chunked Prefill & Prefill/Decode Interleaving** · [spec](PART_SPECS_T08.md#p0353-chunked-prefill) · [self-contained txt](../prompts/P0353_chunked_prefill.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0353  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0353 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0353  (3/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Chunked Prefill & Prefill/Decode Interleaving
file         : parts/t08_inference/P0353_chunked_prefill.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.chunked_prefill
language     : Rust 1.86
capability   : cap.t08.chunked.chunked_prefill@1
determinism  : io
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Long prompts never block short interactive requests.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. prompt chunking with configurable token budget per step
  2. prefill/decode mixing policy tuned for latency targets
  3. TTFT versus throughput tradeoff measurement
  4. interference measurement on interactive requests

Expanded obligations:
  1. Implement prompt chunking with configurable token budget per step, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement prefill/decode mixing policy tuned for latency targets with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement TTFT versus throughput tradeoff measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement interference measurement on interactive requests as a
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.chunked.chunked_prefill@1
  cap.t08.chunked.chunked_prefill.describe@1

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

  cap.t08.continuous.continuous_batching@1
      if unavailable: use the in-file conservative substitute for
      `continuous_batching` (documented, slower, lower quality) and set
      `degraded['continuous_batching']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t02.kernel.kernel_fusion_rules@1
      if unavailable: use the in-file conservative substitute for
      `kernel_fusion_rules` (documented, slower, lower quality) and set
      `degraded['kernel_fusion_rules']='local'`

  cap.t03.target.target_description@1
      if unavailable: use the in-file conservative substitute for
      `target_description` (documented, slower, lower quality) and set
      `degraded['target_description']='local'`

  cap.t04.confidential.confidential_compute@1
      if unavailable: use the in-file conservative substitute for
      `confidential_compute` (documented, slower, lower quality) and set
      `degraded['confidential_compute']='local'`

  cap.t05.multimodal.multimodal_fusion_arch@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_fusion_arch` (documented, slower, lower quality) and set
      `degraded['multimodal_fusion_arch']='local'`

  cap.t06.ensemble.ensemble_combiner@1
      if unavailable: use the in-file conservative substitute for
      `ensemble_combiner` (documented, slower, lower quality) and set
      `degraded['ensemble_combiner']='local'`

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
   3. [ 600 lines] Core implementation A - prompt chunking with configurable token budget per step
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - prefill/decode mixing policy tuned for latency targets
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - TTFT versus throughput tradeoff measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - interference measurement on interactive requests
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
     exactly (capability == cap.t08.chunked.chunked_prefill@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0353_chunked_prefill.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0354-prefill-decode-split

**P0354 · `prefill_decode_split` — Disaggregated Prefill/Decode Serving** · [spec](PART_SPECS_T08.md#p0354-prefill-decode-split) · [self-contained txt](../prompts/P0354_prefill_decode_split.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0354  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0354 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0354  (4/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Disaggregated Prefill/Decode Serving
file         : parts/t08_inference/P0354_prefill_decode_split.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.prefill_decode_split
language     : Rust 1.86
capability   : cap.t08.prefill.prefill_decode_split@1
determinism  : io
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Separate hardware pools for the two very different phases.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. KV handoff protocol between prefill and decode nodes
  2. pool sizing policy from traffic characteristics
  3. handoff latency and bandwidth accounting
  4. cost-per-token reduction measurement versus colocated serving

Expanded obligations:
  1. Implement KV handoff protocol between prefill and decode nodes with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement pool sizing policy from traffic characteristics together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement handoff latency and bandwidth accounting as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement cost-per-token reduction measurement versus colocated serving,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.prefill.prefill_decode_split@1
  cap.t08.prefill.prefill_decode_split.describe@1

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

  cap.t08.chunked.chunked_prefill@1
      if unavailable: use the in-file conservative substitute for
      `chunked_prefill` (documented, slower, lower quality) and set
      `degraded['chunked_prefill']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t02.sparse.sparse_attention_kernels@1
      if unavailable: use the in-file conservative substitute for
      `sparse_attention_kernels` (documented, slower, lower quality) and set
      `degraded['sparse_attention_kernels']='local'`

  cap.t03.kernel.kernel_template_lib@1
      if unavailable: use the in-file conservative substitute for
      `kernel_template_lib` (documented, slower, lower quality) and set
      `degraded['kernel_template_lib']='local'`

  cap.t04.capacity.capacity_benchmarks@1
      if unavailable: use the in-file conservative substitute for
      `capacity_benchmarks` (documented, slower, lower quality) and set
      `degraded['capacity_benchmarks']='local'`

  cap.t05.context.context_packing@1
      if unavailable: use the in-file conservative substitute for
      `context_packing` (documented, slower, lower quality) and set
      `degraded['context_packing']='local'`

  cap.t06.expert.expert_alignment@1
      if unavailable: use the in-file conservative substitute for
      `expert_alignment` (documented, slower, lower quality) and set
      `degraded['expert_alignment']='local'`

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
   3. [ 600 lines] Core implementation A - KV handoff protocol between prefill and decode nodes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - pool sizing policy from traffic characteristics
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - handoff latency and bandwidth accounting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost-per-token reduction measurement versus colocated serving
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
     exactly (capability == cap.t08.prefill.prefill_decode_split@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0354_prefill_decode_split.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0355-admission-control

**P0355 · `admission_control` — Admission Control & Queue Management** · [spec](PART_SPECS_T08.md#p0355-admission-control) · [self-contained txt](../prompts/P0355_admission_control.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0355  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0355 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0355  (5/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Admission Control & Queue Management
file         : parts/t08_inference/P0355_admission_control.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.admission_control
language     : Rust 1.86
capability   : cap.t08.admission.admission_control@1
determinism  : io
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Says no early rather than failing slowly.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. SLO-aware admission with predicted-latency rejection
  2. priority queues with aging and deadline scheduling
  3. queue-depth control keeping latency bounded under overload
  4. measured SLO attainment during 5x overload

Expanded obligations:
  1. Implement SLO-aware admission with predicted-latency rejection together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement priority queues with aging and deadline scheduling as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement queue-depth control keeping latency bounded under overload,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement measured SLO attainment during 5x overload with an explicit
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.admission.admission_control@1
  cap.t08.admission.admission_control.describe@1

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

  cap.t08.prefill.prefill_decode_split@1
      if unavailable: use the in-file conservative substitute for
      `prefill_decode_split` (documented, slower, lower quality) and set
      `degraded['prefill_decode_split']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t02.tensor.tensor_core_util@1
      if unavailable: use the in-file conservative substitute for
      `tensor_core_util` (documented, slower, lower quality) and set
      `degraded['tensor_core_util']='local'`

  cap.t03.compiler.compiler_fuzzer@1
      if unavailable: use the in-file conservative substitute for
      `compiler_fuzzer` (documented, slower, lower quality) and set
      `degraded['compiler_fuzzer']='local'`

  cap.t04.hpc.hpc_interop@1
      if unavailable: use the in-file conservative substitute for
      `hpc_interop` (documented, slower, lower quality) and set
      `degraded['hpc_interop']='local'`

  cap.t05.capacity.capacity_probes@1
      if unavailable: use the in-file conservative substitute for
      `capacity_probes` (documented, slower, lower quality) and set
      `degraded['capacity_probes']='local'`

  cap.t06.moe.moe_speed_accounting@1
      if unavailable: use the in-file conservative substitute for
      `moe_speed_accounting` (documented, slower, lower quality) and set
      `degraded['moe_speed_accounting']='local'`

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
   3. [ 600 lines] Core implementation A - SLO-aware admission with predicted-latency rejection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - priority queues with aging and deadline scheduling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - queue-depth control keeping latency bounded under overload
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured SLO attainment during 5x overload
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
     exactly (capability == cap.t08.admission.admission_control@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0355_admission_control.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0356-cascade-stage1-draft

**P0356 · `cascade_stage1_draft` — Cascade Stage 1: 1.5B Draft Engine** · [spec](PART_SPECS_T08.md#p0356-cascade-stage1-draft) · [self-contained txt](../prompts/P0356_cascade_stage1_draft.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0356  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0356 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0356  (6/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Cascade Stage 1: 1.5B Draft Engine
file         : parts/t08_inference/P0356_cascade_stage1_draft.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_stage1_draft
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_stage1_draft@1
determinism  : io
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
The fastest drafter: cheap tokens for the easy majority.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. ultra-low-latency decode loop with fused persistent kernel
  2. acceptance-rate measurement and self-tuning draft length
  3. memory co-residency with the core model
  4. contribution measurement to the S1 4.0x factor

Expanded obligations:
  1. Implement ultra-low-latency decode loop with fused persistent kernel as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement acceptance-rate measurement and self-tuning draft length, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement memory co-residency with the core model with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Terminal-Bench 2.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement contribution measurement to the S1 4.0x factor together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_stage1_draft@1
  cap.t08.cascade.cascade_stage1_draft.describe@1

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

  cap.t08.admission.admission_control@1
      if unavailable: use the in-file conservative substitute for
      `admission_control` (documented, slower, lower quality) and set
      `degraded['admission_control']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t02.attn.attn_flash_bwd@1
      if unavailable: use the in-file conservative substitute for
      `attn_flash_bwd` (documented, slower, lower quality) and set
      `degraded['attn_flash_bwd']='local'`

  cap.t03.dtype.dtype_promotion@1
      if unavailable: use the in-file conservative substitute for
      `dtype_promotion` (documented, slower, lower quality) and set
      `degraded['dtype_promotion']='local'`

  cap.t04.comm.comm_scheduler@1
      if unavailable: use the in-file conservative substitute for
      `comm_scheduler` (documented, slower, lower quality) and set
      `degraded['comm_scheduler']='local'`

  cap.t05.recurrent.recurrent_memory_layer@1
      if unavailable: use the in-file conservative substitute for
      `recurrent_memory_layer` (documented, slower, lower quality) and set
      `degraded['recurrent_memory_layer']='local'`

  cap.t06.expert.expert_attention@1
      if unavailable: use the in-file conservative substitute for
      `expert_attention` (documented, slower, lower quality) and set
      `degraded['expert_attention']='local'`

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
   3. [ 600 lines] Core implementation A - ultra-low-latency decode loop with fused persistent kernel
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - acceptance-rate measurement and self-tuning draft length
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - memory co-residency with the core model
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - contribution measurement to the S1 4.0x factor
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
     exactly (capability == cap.t08.cascade.cascade_stage1_draft@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0356_cascade_stage1_draft.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0357-cascade-stage2-draft

**P0357 · `cascade_stage2_draft` — Cascade Stage 2: 7B Draft Engine** · [spec](PART_SPECS_T08.md#p0357-cascade-stage2-draft) · [self-contained txt](../prompts/P0357_cascade_stage2_draft.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0357  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0357 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0357  (7/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Cascade Stage 2: 7B Draft Engine
file         : parts/t08_inference/P0357_cascade_stage2_draft.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_stage2_draft
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_stage2_draft@1
determinism  : io
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
The middle drafter: higher acceptance on harder spans.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. shared-KV-layout draft with the core for zero-copy verification
  2. adaptive escalation from stage 1 based on confidence
  3. per-domain acceptance-rate tables
  4. latency/acceptance tradeoff calibration

Expanded obligations:
  1. Implement shared-KV-layout draft with the core for zero-copy
     verification, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement adaptive escalation from stage 1 based on confidence with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement per-domain acceptance-rate tables together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement latency/acceptance tradeoff calibration as a first-class,
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_stage2_draft@1
  cap.t08.cascade.cascade_stage2_draft.describe@1

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

  cap.t08.cascade.cascade_stage1_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage1_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage1_draft']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t02.reduction.reduction_kernels@1
      if unavailable: use the in-file conservative substitute for
      `reduction_kernels` (documented, slower, lower quality) and set
      `degraded['reduction_kernels']='local'`

  cap.t03.parallel.parallel_partition@1
      if unavailable: use the in-file conservative substitute for
      `parallel_partition` (documented, slower, lower quality) and set
      `degraded['parallel_partition']='local'`

  cap.t04.host.host_pinned_pool@1
      if unavailable: use the in-file conservative substitute for
      `host_pinned_pool` (documented, slower, lower quality) and set
      `degraded['host_pinned_pool']='local'`

  cap.t05.byte.byte_latent_patching@1
      if unavailable: use the in-file conservative substitute for
      `byte_latent_patching` (documented, slower, lower quality) and set
      `degraded['byte_latent_patching']='local'`

  cap.t06.expert.expert_lifecycle@1
      if unavailable: use the in-file conservative substitute for
      `expert_lifecycle` (documented, slower, lower quality) and set
      `degraded['expert_lifecycle']='local'`

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
   3. [ 600 lines] Core implementation A - shared-KV-layout draft with the core for zero-copy verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - adaptive escalation from stage 1 based on confidence
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-domain acceptance-rate tables
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency/acceptance tradeoff calibration
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
     exactly (capability == cap.t08.cascade.cascade_stage2_draft@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0357_cascade_stage2_draft.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0358-cascade-stage3-draft

**P0358 · `cascade_stage3_draft` — Cascade Stage 3: 70B Draft Engine** · [spec](PART_SPECS_T08.md#p0358-cascade-stage3-draft) · [self-contained txt](../prompts/P0358_cascade_stage3_draft.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0358  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0358 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0358  (8/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Cascade Stage 3: 70B Draft Engine
file         : parts/t08_inference/P0358_cascade_stage3_draft.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_stage3_draft
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_stage3_draft@1
determinism  : io
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
The near-core drafter for the hardest content.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. high-acceptance drafting with multi-token prediction heads
  2. cost-benefit gating: only used when it pays off
  3. acceptance measurement on reasoning-heavy traffic
  4. budget accounting versus direct core decoding

Expanded obligations:
  1. Implement high-acceptance drafting with multi-token prediction heads
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement cost-benefit gating: only used when it pays off together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement acceptance measurement on reasoning-heavy traffic as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement budget accounting versus direct core decoding, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_stage3_draft@1
  cap.t08.cascade.cascade_stage3_draft.describe@1

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

  cap.t08.cascade.cascade_stage2_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage2_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage2_draft']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t02.rng.rng_kernels@1
      if unavailable: use the in-file conservative substitute for
      `rng_kernels` (documented, slower, lower quality) and set
      `degraded['rng_kernels']='local'`

  cap.t03.jit.jit_cache_compiler@1
      if unavailable: use the in-file conservative substitute for
      `jit_cache_compiler` (documented, slower, lower quality) and set
      `degraded['jit_cache_compiler']='local'`

  cap.t04.power.power_cluster@1
      if unavailable: use the in-file conservative substitute for
      `power_cluster` (documented, slower, lower quality) and set
      `degraded['power_cluster']='local'`

  cap.t05.world.world_model_core@1
      if unavailable: use the in-file conservative substitute for
      `world_model_core` (documented, slower, lower quality) and set
      `degraded['world_model_core']='local'`

  cap.t06.token.token_dropping@1
      if unavailable: use the in-file conservative substitute for
      `token_dropping` (documented, slower, lower quality) and set
      `degraded['token_dropping']='local'`

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
   3. [ 600 lines] Core implementation A - high-acceptance drafting with multi-token prediction heads
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost-benefit gating: only used when it pays off
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - acceptance measurement on reasoning-heavy traffic
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - budget accounting versus direct core decoding
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
     exactly (capability == cap.t08.cascade.cascade_stage3_draft@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0358_cascade_stage3_draft.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0359-cascade-tree-verify

**P0359 · `cascade_tree_verify` — Tree-Structured Speculative Verification** · [spec](PART_SPECS_T08.md#p0359-cascade-tree-verify) · [self-contained txt](../prompts/P0359_cascade_tree_verify.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0359  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0359 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0359  (9/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Tree-Structured Speculative Verification
file         : parts/t08_inference/P0359_cascade_tree_verify.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_tree_verify
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_tree_verify@1
determinism  : io
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Verifies many candidate continuations in one core forward pass.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. candidate-tree construction with beam and topology policy
  2. tree attention mask construction and batched verification
  3. longest-accepted-path extraction with exact-distribution preservation
  4. measured tokens-accepted-per-core-pass

Expanded obligations:
  1. Implement candidate-tree construction with beam and topology policy
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement tree attention mask construction and batched verification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement longest-accepted-path extraction with exact-distribution
     preservation, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured tokens-accepted-per-core-pass with an explicit
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_tree_verify@1
  cap.t08.cascade.cascade_tree_verify.describe@1

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

  cap.t08.cascade.cascade_stage3_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage3_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage3_draft']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t02.simd.simd_cpu@1
      if unavailable: use the in-file conservative substitute for `simd_cpu`
      (documented, slower, lower quality) and set
      `degraded['simd_cpu']='local'`

  cap.t03.loop.loop_transform@1
      if unavailable: use the in-file conservative substitute for
      `loop_transform` (documented, slower, lower quality) and set
      `degraded['loop_transform']='local'`

  cap.t04.scheduler.scheduler_cluster@1
      if unavailable: use the in-file conservative substitute for
      `scheduler_cluster` (documented, slower, lower quality) and set
      `degraded['scheduler_cluster']='local'`

  cap.t05.model.model_merging@1
      if unavailable: use the in-file conservative substitute for
      `model_merging` (documented, slower, lower quality) and set
      `degraded['model_merging']='local'`

  cap.t06.router.router_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `router_interpretability` (documented, slower, lower quality) and set
      `degraded['router_interpretability']='local'`

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
   3. [ 600 lines] Core implementation A - candidate-tree construction with beam and topology policy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tree attention mask construction and batched verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - longest-accepted-path extraction with exact-distribution preserv
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured tokens-accepted-per-core-pass
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
     exactly (capability == cap.t08.cascade.cascade_tree_verify@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0359_cascade_tree_verify.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0360-cascade-acceptance

**P0360 · `cascade_acceptance` — Acceptance Sampling & Distribution Equivalence** · [spec](PART_SPECS_T08.md#p0360-cascade-acceptance) · [self-contained txt](../prompts/P0360_cascade_acceptance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0360  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0360 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0360  (10/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Acceptance Sampling & Distribution Equivalence
file         : parts/t08_inference/P0360_cascade_acceptance.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_acceptance
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_acceptance@1
determinism  : io
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Proves speculation does not change the output distribution.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. modified rejection sampling with exactness proof
  2. typical-acceptance and lossy modes with declared divergence bounds
  3. statistical equivalence testing versus non-speculative decoding
  4. acceptance-rate optimisation under equivalence constraints

Expanded obligations:
  1. Implement modified rejection sampling with exactness proof as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement typical-acceptance and lossy modes with declared divergence
     bounds, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement statistical equivalence testing versus non-speculative
     decoding with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement acceptance-rate optimisation under equivalence constraints
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_acceptance@1
  cap.t08.cascade.cascade_acceptance.describe@1

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

  cap.t08.cascade.cascade_tree_verify@1
      if unavailable: use the in-file conservative substitute for
      `cascade_tree_verify` (documented, slower, lower quality) and set
      `degraded['cascade_tree_verify']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t02.emulation.emulation_reference@1
      if unavailable: use the in-file conservative substitute for
      `emulation_reference` (documented, slower, lower quality) and set
      `degraded['emulation_reference']='local'`

  cap.t03.profile.profile_guided@1
      if unavailable: use the in-file conservative substitute for
      `profile_guided` (documented, slower, lower quality) and set
      `degraded['profile_guided']='local'`

  cap.t04.secure.secure_channel@1
      if unavailable: use the in-file conservative substitute for
      `secure_channel` (documented, slower, lower quality) and set
      `degraded['secure_channel']='local'`

  cap.t05.logit.logit_head_design@1
      if unavailable: use the in-file conservative substitute for
      `logit_head_design` (documented, slower, lower quality) and set
      `degraded['logit_head_design']='local'`

  cap.t06.model.model_cascade_routing@1
      if unavailable: use the in-file conservative substitute for
      `model_cascade_routing` (documented, slower, lower quality) and set
      `degraded['model_cascade_routing']='local'`

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
   3. [ 600 lines] Core implementation A - modified rejection sampling with exactness proof
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - typical-acceptance and lossy modes with declared divergence boun
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - statistical equivalence testing versus non-speculative decoding
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - acceptance-rate optimisation under equivalence constraints
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
     exactly (capability == cap.t08.cascade.cascade_acceptance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0360_cascade_acceptance.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0361-cascade-scheduler

**P0361 · `cascade_scheduler` — Cascade Stage Selection Policy** · [spec](PART_SPECS_T08.md#p0361-cascade-scheduler) · [self-contained txt](../prompts/P0361_cascade_scheduler.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0361  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0361 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0361  (11/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Cascade Stage Selection Policy
file         : parts/t08_inference/P0361_cascade_scheduler.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_scheduler
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_scheduler@1
determinism  : io
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Picks the right drafter for the current span, per request.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. online bandit selection over stages with cost/acceptance feedback
  2. content-type and difficulty signals driving selection
  3. policy stability and oscillation prevention
  4. end-to-end speedup attribution per stage

Expanded obligations:
  1. Implement online bandit selection over stages with cost/acceptance
     feedback, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement content-type and difficulty signals driving selection with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement policy stability and oscillation prevention together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement end-to-end speedup attribution per stage as a first-class,
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_scheduler@1
  cap.t08.cascade.cascade_scheduler.describe@1

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

  cap.t08.cascade.cascade_acceptance@1
      if unavailable: use the in-file conservative substitute for
      `cascade_acceptance` (documented, slower, lower quality) and set
      `degraded['cascade_acceptance']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t02.kernel.kernel_codegen_rt@1
      if unavailable: use the in-file conservative substitute for
      `kernel_codegen_rt` (documented, slower, lower quality) and set
      `degraded['kernel_codegen_rt']='local'`

  cap.t03.equality.equality_saturation@1
      if unavailable: use the in-file conservative substitute for
      `equality_saturation` (documented, slower, lower quality) and set
      `degraded['equality_saturation']='local'`

  cap.t04.simulation.simulation_cluster@1
      if unavailable: use the in-file conservative substitute for
      `simulation_cluster` (documented, slower, lower quality) and set
      `degraded['simulation_cluster']='local'`

  cap.t05.numerical.numerical_arch_stability@1
      if unavailable: use the in-file conservative substitute for
      `numerical_arch_stability` (documented, slower, lower quality) and set
      `degraded['numerical_arch_stability']='local'`

  cap.t06.sparse.sparse_gradient@1
      if unavailable: use the in-file conservative substitute for
      `sparse_gradient` (documented, slower, lower quality) and set
      `degraded['sparse_gradient']='local'`

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
   3. [ 600 lines] Core implementation A - online bandit selection over stages with cost/acceptance feedbac
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - content-type and difficulty signals driving selection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - policy stability and oscillation prevention
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - end-to-end speedup attribution per stage
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
     exactly (capability == cap.t08.cascade.cascade_scheduler@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0361_cascade_scheduler.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0362-cascade-batching

**P0362 · `cascade_batching` — Batched Speculative Execution** · [spec](PART_SPECS_T08.md#p0362-cascade-batching) · [self-contained txt](../prompts/P0362_cascade_batching.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0362  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0362 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0362  (12/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Batched Speculative Execution
file         : parts/t08_inference/P0362_cascade_batching.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_batching
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_batching@1
determinism  : io
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Speculation that gets better, not worse, with batch size.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-sequence variable draft lengths within one batch
  2. ragged verification with no padding waste
  3. batch-wide acceptance accounting and rebalancing
  4. throughput measurement at batch sizes 1 to 1024

Expanded obligations:
  1. Implement per-sequence variable draft lengths within one batch with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement ragged verification with no padding waste together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement batch-wide acceptance accounting and rebalancing as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement throughput measurement at batch sizes 1 to 1024, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_batching@1
  cap.t08.cascade.cascade_batching.describe@1

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

  cap.t08.cascade.cascade_scheduler@1
      if unavailable: use the in-file conservative substitute for
      `cascade_scheduler` (documented, slower, lower quality) and set
      `degraded['cascade_scheduler']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t02.micro.micro_opt_catalog@1
      if unavailable: use the in-file conservative substitute for
      `micro_opt_catalog` (documented, slower, lower quality) and set
      `degraded['micro_opt_catalog']='local'`

  cap.t03.graph.graph_diff_tool@1
      if unavailable: use the in-file conservative substitute for
      `graph_diff_tool` (documented, slower, lower quality) and set
      `degraded['graph_diff_tool']='local'`

  cap.t04.device.device_alloc_fair@1
      if unavailable: use the in-file conservative substitute for
      `device_alloc_fair` (documented, slower, lower quality) and set
      `degraded['device_alloc_fair']='local'`

  cap.t05.arch.arch_ablation_suite@1
      if unavailable: use the in-file conservative substitute for
      `arch_ablation_suite` (documented, slower, lower quality) and set
      `degraded['arch_ablation_suite']='local'`

  cap.t06.sparsity.sparsity_verification@1
      if unavailable: use the in-file conservative substitute for
      `sparsity_verification` (documented, slower, lower quality) and set
      `degraded['sparsity_verification']='local'`

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
   3. [ 600 lines] Core implementation A - per-sequence variable draft lengths within one batch
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - ragged verification with no padding waste
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - batch-wide acceptance accounting and rebalancing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput measurement at batch sizes 1 to 1024
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
     exactly (capability == cap.t08.cascade.cascade_batching@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0362_cascade_batching.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0363-cascade-rollback

**P0363 · `cascade_rollback` — Speculation Rollback & State Repair** · [spec](PART_SPECS_T08.md#p0363-cascade-rollback) · [self-contained txt](../prompts/P0363_cascade_rollback.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0363  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0363 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0363  (13/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Speculation Rollback & State Repair
file         : parts/t08_inference/P0363_cascade_rollback.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_rollback
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_rollback@1
determinism  : io
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Rejected tokens leave no trace anywhere.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. KV truncation and block-table repair with O(1) cost
  2. sampler and RNG state rollback for exact determinism
  3. rollback-correctness verification via replay
  4. rollback cost measurement as a fraction of step time

Expanded obligations:
  1. Implement KV truncation and block-table repair with O(1) cost together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement sampler and RNG state rollback for exact determinism as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement rollback-correctness verification via replay, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement rollback cost measurement as a fraction of step time with an
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_rollback@1
  cap.t08.cascade.cascade_rollback.describe@1

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

  cap.t08.cascade.cascade_batching@1
      if unavailable: use the in-file conservative substitute for
      `cascade_batching` (documented, slower, lower quality) and set
      `degraded['cascade_batching']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t02.attn.attn_flash_fwd@1
      if unavailable: use the in-file conservative substitute for
      `attn_flash_fwd` (documented, slower, lower quality) and set
      `degraded['attn_flash_fwd']='local'`

  cap.t03.shape.shape_inference@1
      if unavailable: use the in-file conservative substitute for
      `shape_inference` (documented, slower, lower quality) and set
      `degraded['shape_inference']='local'`

  cap.t04.tcp.tcp_fallback@1
      if unavailable: use the in-file conservative substitute for
      `tcp_fallback` (documented, slower, lower quality) and set
      `degraded['tcp_fallback']='local'`

  cap.t05.state.state_space_layer@1
      if unavailable: use the in-file conservative substitute for
      `state_space_layer` (documented, slower, lower quality) and set
      `degraded['state_space_layer']='local'`

  cap.t06.expert.expert_ffn@1
      if unavailable: use the in-file conservative substitute for
      `expert_ffn` (documented, slower, lower quality) and set
      `degraded['expert_ffn']='local'`

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
   3. [ 600 lines] Core implementation A - KV truncation and block-table repair with O(1) cost
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - sampler and RNG state rollback for exact determinism
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - rollback-correctness verification via replay
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - rollback cost measurement as a fraction of step time
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
     exactly (capability == cap.t08.cascade.cascade_rollback@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0363_cascade_rollback.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0364-cascade-tuning

**P0364 · `cascade_tuning` — Draft Length & Depth Auto-Tuning** · [spec](PART_SPECS_T08.md#p0364-cascade-tuning) · [self-contained txt](../prompts/P0364_cascade_tuning.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0364  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0364 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0364  (14/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Draft Length & Depth Auto-Tuning
file         : parts/t08_inference/P0364_cascade_tuning.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_tuning
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_tuning@1
determinism  : io
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Continuously finds the optimal speculation depth.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. closed-loop controller from measured acceptance and latency
  2. per-request-class parameter tables
  3. stability analysis and safe parameter bounds
  4. measured improvement over fixed draft length

Expanded obligations:
  1. Implement closed-loop controller from measured acceptance and latency as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement per-request-class parameter tables, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement stability analysis and safe parameter bounds with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured improvement over fixed draft length together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_tuning@1
  cap.t08.cascade.cascade_tuning.describe@1

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

  cap.t08.cascade.cascade_rollback@1
      if unavailable: use the in-file conservative substitute for
      `cascade_rollback` (documented, slower, lower quality) and set
      `degraded['cascade_rollback']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t02.elementwise.elementwise_fusion@1
      if unavailable: use the in-file conservative substitute for
      `elementwise_fusion` (documented, slower, lower quality) and set
      `degraded['elementwise_fusion']='local'`

  cap.t03.scheduler.scheduler_pass@1
      if unavailable: use the in-file conservative substitute for
      `scheduler_pass` (documented, slower, lower quality) and set
      `degraded['scheduler_pass']='local'`

  cap.t04.nvme.nvme_offload@1
      if unavailable: use the in-file conservative substitute for
      `nvme_offload` (documented, slower, lower quality) and set
      `degraded['nvme_offload']='local'`

  cap.t05.tokeniser.tokeniser_omega@1
      if unavailable: use the in-file conservative substitute for
      `tokeniser_omega` (documented, slower, lower quality) and set
      `degraded['tokeniser_omega']='local'`

  cap.t06.moe.moe_determinism@1
      if unavailable: use the in-file conservative substitute for
      `moe_determinism` (documented, slower, lower quality) and set
      `degraded['moe_determinism']='local'`

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
   3. [ 600 lines] Core implementation A - closed-loop controller from measured acceptance and latency
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-request-class parameter tables
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - stability analysis and safe parameter bounds
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured improvement over fixed draft length
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
     exactly (capability == cap.t08.cascade.cascade_tuning@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0364_cascade_tuning.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0365-paged-attention-runtime

**P0365 · `paged_attention_runtime` — Paged Attention Runtime Integration** · [spec](PART_SPECS_T08.md#p0365-paged-attention-runtime) · [self-contained txt](../prompts/P0365_paged_attention_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0365  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0365 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0365  (15/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Paged Attention Runtime Integration
file         : parts/t08_inference/P0365_paged_attention_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.paged_attention_runtime
language     : Rust 1.86
capability   : cap.t08.paged.paged_attention_runtime@1
determinism  : io
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Wires the T02 paged decode kernel to the block-table manager.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. block-table construction and validation per step
  2. page-fault-free guarantee via pre-reservation
  3. long-context split-KV coordination
  4. kernel-launch overhead elimination measurement

Expanded obligations:
  1. Implement block-table construction and validation per step, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement page-fault-free guarantee via pre-reservation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement long-context split-KV coordination together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement kernel-launch overhead elimination measurement as a
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.paged.paged_attention_runtime@1
  cap.t08.paged.paged_attention_runtime.describe@1

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

  cap.t08.cascade.cascade_tuning@1
      if unavailable: use the in-file conservative substitute for
      `cascade_tuning` (documented, slower, lower quality) and set
      `degraded['cascade_tuning']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t02.transpose.transpose_layout@1
      if unavailable: use the in-file conservative substitute for
      `transpose_layout` (documented, slower, lower quality) and set
      `degraded['transpose_layout']='local'`

  cap.t03.codegen.codegen_cpu@1
      if unavailable: use the in-file conservative substitute for
      `codegen_cpu` (documented, slower, lower quality) and set
      `degraded['codegen_cpu']='local'`

  cap.t04.straggler.straggler_mitigation@1
      if unavailable: use the in-file conservative substitute for
      `straggler_mitigation` (documented, slower, lower quality) and set
      `degraded['straggler_mitigation']='local'`

  cap.t05.uncertainty.uncertainty_calibration@1
      if unavailable: use the in-file conservative substitute for
      `uncertainty_calibration` (documented, slower, lower quality) and set
      `degraded['uncertainty_calibration']='local'`

  cap.t06.moe.moe_batching@1
      if unavailable: use the in-file conservative substitute for
      `moe_batching` (documented, slower, lower quality) and set
      `degraded['moe_batching']='local'`

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
   3. [ 600 lines] Core implementation A - block-table construction and validation per step
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - page-fault-free guarantee via pre-reservation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - long-context split-KV coordination
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - kernel-launch overhead elimination measurement
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
     exactly (capability == cap.t08.paged.paged_attention_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0365_paged_attention_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0366-prefix-cache-runtime

**P0366 · `prefix_cache_runtime` — Prefix Cache Runtime & Radix Matching** · [spec](PART_SPECS_T08.md#p0366-prefix-cache-runtime) · [self-contained txt](../prompts/P0366_prefix_cache_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0366  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0366 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0366  (16/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Prefix Cache Runtime & Radix Matching
file         : parts/t08_inference/P0366_prefix_cache_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.prefix_cache_runtime
language     : Rust 1.86
capability   : cap.t08.prefix.prefix_cache_runtime@1
determinism  : io
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Turns repeated prompts into near-zero prefill cost.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. radix-tree matching with longest-prefix lookup per request
  2. copy-on-write branching for shared prefixes
  3. eviction policy balancing hit rate and memory
  4. measured prefill-compute reduction on real traffic mixes

Expanded obligations:
  1. Implement radix-tree matching with longest-prefix lookup per request
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement copy-on-write branching for shared prefixes together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement eviction policy balancing hit rate and memory as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured prefill-compute reduction on real traffic mixes, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.prefix.prefix_cache_runtime@1
  cap.t08.prefix.prefix_cache_runtime.describe@1

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

  cap.t08.paged.paged_attention_runtime@1
      if unavailable: use the in-file conservative substitute for
      `paged_attention_runtime` (documented, slower, lower quality) and set
      `degraded['paged_attention_runtime']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t02.cache.cache_blocking@1
      if unavailable: use the in-file conservative substitute for
      `cache_blocking` (documented, slower, lower quality) and set
      `degraded['cache_blocking']='local'`

  cap.t03.vectorisation.vectorisation_transform@1
      if unavailable: use the in-file conservative substitute for
      `vectorisation_transform` (documented, slower, lower quality) and set
      `degraded['vectorisation_transform']='local'`

  cap.t04.cloud.cloud_provisioner@1
      if unavailable: use the in-file conservative substitute for
      `cloud_provisioner` (documented, slower, lower quality) and set
      `degraded['cloud_provisioner']='local'`

  cap.t05.knowledge.knowledge_editing@1
      if unavailable: use the in-file conservative substitute for
      `knowledge_editing` (documented, slower, lower quality) and set
      `degraded['knowledge_editing']='local'`

  cap.t06.moe.moe_scaling_laws@1
      if unavailable: use the in-file conservative substitute for
      `moe_scaling_laws` (documented, slower, lower quality) and set
      `degraded['moe_scaling_laws']='local'`

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
   3. [ 600 lines] Core implementation A - radix-tree matching with longest-prefix lookup per request
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - copy-on-write branching for shared prefixes
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - eviction policy balancing hit rate and memory
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured prefill-compute reduction on real traffic mixes
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
     exactly (capability == cap.t08.prefix.prefix_cache_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0366_prefix_cache_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0367-session-affinity

**P0367 · `session_affinity` — Session Affinity & KV Reuse Routing** · [spec](PART_SPECS_T08.md#p0367-session-affinity) · [self-contained txt](../prompts/P0367_session_affinity.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0367  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0367 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0367  (17/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Session Affinity & KV Reuse Routing
file         : parts/t08_inference/P0367_session_affinity.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.session_affinity
language     : Rust 1.86
capability   : cap.t08.session.session_affinity@1
determinism  : io
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Multi-turn conversations return to their own cache.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. affinity routing with cache-locality scoring
  2. KV migration when affinity must break
  3. measured multi-turn latency improvement
  4. load-balance-versus-affinity tradeoff control

Expanded obligations:
  1. Implement affinity routing with cache-locality scoring together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement KV migration when affinity must break as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement measured multi-turn latency improvement, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement load-balance-versus-affinity tradeoff control with an explicit
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
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.session.session_affinity@1
  cap.t08.session.session_affinity.describe@1

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

  cap.t08.prefix.prefix_cache_runtime@1
      if unavailable: use the in-file conservative substitute for
      `prefix_cache_runtime` (documented, slower, lower quality) and set
      `degraded['prefix_cache_runtime']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t02.profiler.profiler_hooks@1
      if unavailable: use the in-file conservative substitute for
      `profiler_hooks` (documented, slower, lower quality) and set
      `degraded['profiler_hooks']='local'`

  cap.t03.compile.compile_time_budget@1
      if unavailable: use the in-file conservative substitute for
      `compile_time_budget` (documented, slower, lower quality) and set
      `degraded['compile_time_budget']='local'`

  cap.t04.bandwidth.bandwidth_accounting@1
      if unavailable: use the in-file conservative substitute for
      `bandwidth_accounting` (documented, slower, lower quality) and set
      `degraded['bandwidth_accounting']='local'`

  cap.t05.residual.residual_stream_design@1
      if unavailable: use the in-file conservative substitute for
      `residual_stream_design` (documented, slower, lower quality) and set
      `degraded['residual_stream_design']='local'`

  cap.t06.cost.cost_aware_routing@1
      if unavailable: use the in-file conservative substitute for
      `cost_aware_routing` (documented, slower, lower quality) and set
      `degraded['cost_aware_routing']='local'`

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
   3. [ 600 lines] Core implementation A - affinity routing with cache-locality scoring
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - KV migration when affinity must break
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - measured multi-turn latency improvement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - load-balance-versus-affinity tradeoff control
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
     exactly (capability == cap.t08.session.session_affinity@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0367_session_affinity.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0368-sampler-engine

**P0368 · `sampler_engine` — Sampling Engine & Decode Policies** · [spec](PART_SPECS_T08.md#p0368-sampler-engine) · [self-contained txt](../prompts/P0368_sampler_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0368  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0368 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0368  (18/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Sampling Engine & Decode Policies
file         : parts/t08_inference/P0368_sampler_engine.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.sampler_engine
language     : Rust 1.86
capability   : cap.t08.sampler.sampler_engine@1
determinism  : io
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Every sampling mode, exact and fast.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. temperature, top-k, top-p, min-p, typical and mirostat implementations
  2. repetition/presence/frequency penalties with correct accounting
  3. deterministic greedy path with tie-breaking rules
  4. distribution-fidelity statistical tests

Expanded obligations:
  1. Implement temperature, top-k, top-p, min-p, typical and mirostat
     implementations as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement repetition/presence/frequency penalties with correct
     accounting, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement deterministic greedy path with tie-breaking rules with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement distribution-fidelity statistical tests together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.sampler.sampler_engine@1
  cap.t08.sampler.sampler_engine.describe@1

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

  cap.t08.session.session_affinity@1
      if unavailable: use the in-file conservative substitute for
      `session_affinity` (documented, slower, lower quality) and set
      `degraded['session_affinity']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t02.error.error_correction@1
      if unavailable: use the in-file conservative substitute for
      `error_correction` (documented, slower, lower quality) and set
      `degraded['error_correction']='local'`

  cap.t03.superoptimiser.superoptimiser@1
      if unavailable: use the in-file conservative substitute for
      `superoptimiser` (documented, slower, lower quality) and set
      `degraded['superoptimiser']='local'`

  cap.t04.telemetry.telemetry_transport@1
      if unavailable: use the in-file conservative substitute for
      `telemetry_transport` (documented, slower, lower quality) and set
      `degraded['telemetry_transport']='local'`

  cap.t05.model.model_surgery@1
      if unavailable: use the in-file conservative substitute for
      `model_surgery` (documented, slower, lower quality) and set
      `degraded['model_surgery']='local'`

  cap.t06.router.router_online_learning@1
      if unavailable: use the in-file conservative substitute for
      `router_online_learning` (documented, slower, lower quality) and set
      `degraded['router_online_learning']='local'`

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
   3. [ 600 lines] Core implementation A - temperature, top-k, top-p, min-p, typical and mirostat implement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - repetition/presence/frequency penalties with correct accounting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deterministic greedy path with tie-breaking rules
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - distribution-fidelity statistical tests
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
     exactly (capability == cap.t08.sampler.sampler_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0368_sampler_engine.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0369-constrained-decoding

**P0369 · `constrained_decoding` — Grammar-Constrained Decoding Engine** · [spec](PART_SPECS_T08.md#p0369-constrained-decoding) · [self-contained txt](../prompts/P0369_constrained_decoding.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0369  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0369 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0369  (19/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Grammar-Constrained Decoding Engine
file         : parts/t08_inference/P0369_constrained_decoding.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.constrained_decoding
language     : Rust 1.86
capability   : cap.t08.constrained.constrained_decoding@1
determinism  : io
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Structured output that is valid by construction, not by luck.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. incremental parser (JSON/regex/CFG/schema) with token-mask computation
  2. precompiled automaton cache for hot schemas
  3. guarantee of syntactic validity with proof
  4. overhead measurement under 3% of decode time

Expanded obligations:
  1. Implement incremental parser (JSON/regex/CFG/schema) with token-mask
     computation, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement precompiled automaton cache for hot schemas with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Terminal-Bench 2.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement guarantee of syntactic validity with proof together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement overhead measurement under 3% of decode time as a first-class,
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.constrained.constrained_decoding@1
  cap.t08.constrained.constrained_decoding.describe@1

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

  cap.t08.sampler.sampler_engine@1
      if unavailable: use the in-file conservative substitute for
      `sampler_engine` (documented, slower, lower quality) and set
      `degraded['sampler_engine']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t02.kernel.kernel_bench_suite@1
      if unavailable: use the in-file conservative substitute for
      `kernel_bench_suite` (documented, slower, lower quality) and set
      `degraded['kernel_bench_suite']='local'`

  cap.t03.op.op_registry@1
      if unavailable: use the in-file conservative substitute for
      `op_registry` (documented, slower, lower quality) and set
      `degraded['op_registry']='local'`

  cap.t04.green.green_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `green_scheduling` (documented, slower, lower quality) and set
      `degraded['green_scheduling']='local'`

  cap.t05.reference.reference_forward@1
      if unavailable: use the in-file conservative substitute for
      `reference_forward` (documented, slower, lower quality) and set
      `degraded['reference_forward']='local'`

  cap.t06.adaptive.adaptive_sparsity@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_sparsity` (documented, slower, lower quality) and set
      `degraded['adaptive_sparsity']='local'`

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
   3. [ 600 lines] Core implementation A - incremental parser (JSON/regex/CFG/schema) with token-mask compu
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - precompiled automaton cache for hot schemas
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - guarantee of syntactic validity with proof
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - overhead measurement under 3% of decode time
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
     exactly (capability == cap.t08.constrained.constrained_decoding@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0369_constrained_decoding.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0370-logit-processor

**P0370 · `logit_processor` — Logit Processing Pipeline** · [spec](PART_SPECS_T08.md#p0370-logit-processor) · [self-contained txt](../prompts/P0370_logit_processor.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0370  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0370 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0370  (20/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Logit Processing Pipeline
file         : parts/t08_inference/P0370_logit_processor.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.logit_processor
language     : Rust 1.86
capability   : cap.t08.logit.logit_processor@1
determinism  : io
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Composable, ordered, auditable logit transformations.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. processor chain with declared ordering semantics
  2. fused GPU-side processing avoiding host round-trips
  3. bias/ban/force-token mechanisms
  4. per-processor latency accounting

Expanded obligations:
  1. Implement processor chain with declared ordering semantics with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement fused GPU-side processing avoiding host round-trips together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement bias/ban/force-token mechanisms as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement per-processor latency accounting, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's Terminal-Bench 2.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.

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
  cap.t08.logit.logit_processor@1
  cap.t08.logit.logit_processor.describe@1

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

  cap.t08.constrained.constrained_decoding@1
      if unavailable: use the in-file conservative substitute for
      `constrained_decoding` (documented, slower, lower quality) and set
      `degraded['constrained_decoding']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t02.gemm.gemm_sparse@1
      if unavailable: use the in-file conservative substitute for
      `gemm_sparse` (documented, slower, lower quality) and set
      `degraded['gemm_sparse']='local'`

  cap.t03.pass.pass_manager@1
      if unavailable: use the in-file conservative substitute for
      `pass_manager` (documented, slower, lower quality) and set
      `degraded['pass_manager']='local'`

  cap.t04.rdma.rdma_transport@1
      if unavailable: use the in-file conservative substitute for
      `rdma_transport` (documented, slower, lower quality) and set
      `degraded['rdma_transport']='local'`

  cap.t05.kv.kv_compression_model@1
      if unavailable: use the in-file conservative substitute for
      `kv_compression_model` (documented, slower, lower quality) and set
      `degraded['kv_compression_model']='local'`

  cap.t06.router.router_hash_hybrid@1
      if unavailable: use the in-file conservative substitute for
      `router_hash_hybrid` (documented, slower, lower quality) and set
      `degraded['router_hash_hybrid']='local'`

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
   3. [ 600 lines] Core implementation A - processor chain with declared ordering semantics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fused GPU-side processing avoiding host round-trips
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - bias/ban/force-token mechanisms
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - per-processor latency accounting
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
     exactly (capability == cap.t08.logit.logit_processor@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0370_logit_processor.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0371-stop-conditions

**P0371 · `stop_conditions` — Stop Criteria & Output Boundary Detection** · [spec](PART_SPECS_T08.md#p0371-stop-conditions) · [self-contained txt](../prompts/P0371_stop_conditions.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0371  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0371 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0371  (21/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Stop Criteria & Output Boundary Detection
file         : parts/t08_inference/P0371_stop_conditions.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.stop_conditions
language     : Rust 1.86
capability   : cap.t08.stop.stop_conditions@1
determinism  : io
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Stops exactly where it should, including mid-token sequences.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-token stop-sequence detection across token boundaries
  2. max-token, deadline and budget stops with partial-result emission
  3. streaming-safe boundary handling for partial UTF-8
  4. exhaustive boundary-case tests

Expanded obligations:
  1. Implement multi-token stop-sequence detection across token boundaries
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement max-token, deadline and budget stops with partial-result
     emission as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement streaming-safe boundary handling for partial UTF-8, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement exhaustive boundary-case tests with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.stop.stop_conditions@1
  cap.t08.stop.stop_conditions.describe@1

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

  cap.t08.logit.logit_processor@1
      if unavailable: use the in-file conservative substitute for
      `logit_processor` (documented, slower, lower quality) and set
      `degraded['logit_processor']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t02.softmax.softmax_norm@1
      if unavailable: use the in-file conservative substitute for
      `softmax_norm` (documented, slower, lower quality) and set
      `degraded['softmax_norm']='local'`

  cap.t03.rematerialisat.rematerialisation@1
      if unavailable: use the in-file conservative substitute for
      `rematerialisation` (documented, slower, lower quality) and set
      `degraded['rematerialisation']='local'`

  cap.t04.weight.weight_streaming@1
      if unavailable: use the in-file conservative substitute for
      `weight_streaming` (documented, slower, lower quality) and set
      `degraded['weight_streaming']='local'`

  cap.t05.embedding.embedding_design@1
      if unavailable: use the in-file conservative substitute for
      `embedding_design` (documented, slower, lower quality) and set
      `degraded['embedding_design']='local'`

  cap.t06.router.router_lookahead@1
      if unavailable: use the in-file conservative substitute for
      `router_lookahead` (documented, slower, lower quality) and set
      `degraded['router_lookahead']='local'`

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
   3. [ 600 lines] Core implementation A - multi-token stop-sequence detection across token boundaries
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - max-token, deadline and budget stops with partial-result emissio
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - streaming-safe boundary handling for partial UTF-8
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - exhaustive boundary-case tests
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
     exactly (capability == cap.t08.stop.stop_conditions@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0371_stop_conditions.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0372-streaming-output

**P0372 · `streaming_output` — Token Streaming & Backpressure** · [spec](PART_SPECS_T08.md#p0372-streaming-output) · [self-contained txt](../prompts/P0372_streaming_output.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0372  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0372 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0372  (22/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Token Streaming & Backpressure
file         : parts/t08_inference/P0372_streaming_output.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.streaming_output
language     : Rust 1.86
capability   : cap.t08.streaming.streaming_output@1
determinism  : io
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
First token fast, every token smooth, never a stall.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. incremental detokenisation with correct multi-byte handling
  2. client-backpressure handling without blocking the engine
  3. chunking policy tuned for perceived latency
  4. inter-token-latency jitter measurement

Expanded obligations:
  1. Implement incremental detokenisation with correct multi-byte handling as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement client-backpressure handling without blocking the engine, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement chunking policy tuned for perceived latency with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement inter-token-latency jitter measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.streaming.streaming_output@1
  cap.t08.streaming.streaming_output.describe@1

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

  cap.t08.stop.stop_conditions@1
      if unavailable: use the in-file conservative substitute for
      `stop_conditions` (documented, slower, lower quality) and set
      `degraded['stop_conditions']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t02.gather.gather_scatter@1
      if unavailable: use the in-file conservative substitute for
      `gather_scatter` (documented, slower, lower quality) and set
      `degraded['gather_scatter']='local'`

  cap.t03.codegen.codegen_gpu@1
      if unavailable: use the in-file conservative substitute for
      `codegen_gpu` (documented, slower, lower quality) and set
      `degraded['codegen_gpu']='local'`

  cap.t04.failure.failure_recovery@1
      if unavailable: use the in-file conservative substitute for
      `failure_recovery` (documented, slower, lower quality) and set
      `degraded['failure_recovery']='local'`

  cap.t05.verifier.verifier_head@1
      if unavailable: use the in-file conservative substitute for
      `verifier_head` (documented, slower, lower quality) and set
      `degraded['verifier_head']='local'`

  cap.t06.expert.expert_offload@1
      if unavailable: use the in-file conservative substitute for
      `expert_offload` (documented, slower, lower quality) and set
      `degraded['expert_offload']='local'`

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
   3. [ 600 lines] Core implementation A - incremental detokenisation with correct multi-byte handling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - client-backpressure handling without blocking the engine
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - chunking policy tuned for perceived latency
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - inter-token-latency jitter measurement
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
     exactly (capability == cap.t08.streaming.streaming_output@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0372_streaming_output.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0373-batch-invariance

**P0373 · `batch_invariance` — Batch-Invariant Inference Mode** · [spec](PART_SPECS_T08.md#p0373-batch-invariance) · [self-contained txt](../prompts/P0373_batch_invariance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0373  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0373 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0373  (23/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Batch-Invariant Inference Mode
file         : parts/t08_inference/P0373_batch_invariance.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.batch_invariance
language     : Rust 1.86
capability   : cap.t08.batch.batch_invariance@1
determinism  : io
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Same answer whether you are alone or one of a thousand.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fixed-split reduction strategies independent of batch size
  2. batch-invariant attention and normalisation paths
  3. bit-exactness verification across batch sizes 1..1024
  4. measured cost of batch invariance

Expanded obligations:
  1. Implement fixed-split reduction strategies independent of batch size,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement batch-invariant attention and normalisation paths with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement bit-exactness verification across batch sizes 1..1024 together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured cost of batch invariance as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.batch.batch_invariance@1
  cap.t08.batch.batch_invariance.describe@1

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

  cap.t08.streaming.streaming_output@1
      if unavailable: use the in-file conservative substitute for
      `streaming_output` (documented, slower, lower quality) and set
      `degraded['streaming_output']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t02.async.async_copy@1
      if unavailable: use the in-file conservative substitute for
      `async_copy` (documented, slower, lower quality) and set
      `degraded['async_copy']='local'`

  cap.t03.differentiatio.differentiation@1
      if unavailable: use the in-file conservative substitute for
      `differentiation` (documented, slower, lower quality) and set
      `degraded['differentiation']='local'`

  cap.t04.edge.edge_runtime@1
      if unavailable: use the in-file conservative substitute for
      `edge_runtime` (documented, slower, lower quality) and set
      `degraded['edge_runtime']='local'`

  cap.t05.continual.continual_learning@1
      if unavailable: use the in-file conservative substitute for
      `continual_learning` (documented, slower, lower quality) and set
      `degraded['continual_learning']='local'`

  cap.t06.expert.expert_choice_routing@1
      if unavailable: use the in-file conservative substitute for
      `expert_choice_routing` (documented, slower, lower quality) and set
      `degraded['expert_choice_routing']='local'`

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
   3. [ 600 lines] Core implementation A - fixed-split reduction strategies independent of batch size
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - batch-invariant attention and normalisation paths
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - bit-exactness verification across batch sizes 1..1024
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured cost of batch invariance
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
     exactly (capability == cap.t08.batch.batch_invariance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0373_batch_invariance.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0374-multi-gpu-runtime

**P0374 · `multi_gpu_runtime` — Multi-Device Execution Runtime** · [spec](PART_SPECS_T08.md#p0374-multi-gpu-runtime) · [self-contained txt](../prompts/P0374_multi_gpu_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0374  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0374 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0374  (24/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Multi-Device Execution Runtime
file         : parts/t08_inference/P0374_multi_gpu_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.multi_gpu_runtime
language     : Rust 1.86
capability   : cap.t08.multi.multi_gpu_runtime@1
determinism  : io
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Tensor, pipeline and expert parallel serving in one runtime.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. parallel-plan execution with collective scheduling
  2. per-device stream coordination and event fencing
  3. rank-failure detection with request preservation
  4. scaling efficiency measurement across devices

Expanded obligations:
  1. Implement parallel-plan execution with collective scheduling with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement per-device stream coordination and event fencing together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement rank-failure detection with request preservation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement scaling efficiency measurement across devices, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
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
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.multi.multi_gpu_runtime@1
  cap.t08.multi.multi_gpu_runtime.describe@1

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

  cap.t08.batch.batch_invariance@1
      if unavailable: use the in-file conservative substitute for
      `batch_invariance` (documented, slower, lower quality) and set
      `degraded['batch_invariance']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t02.roofline.roofline_model@1
      if unavailable: use the in-file conservative substitute for
      `roofline_model` (documented, slower, lower quality) and set
      `degraded['roofline_model']='local'`

  cap.t03.differential.differential_testing@1
      if unavailable: use the in-file conservative substitute for
      `differential_testing` (documented, slower, lower quality) and set
      `degraded['differential_testing']='local'`

  cap.t04.data.data_locality@1
      if unavailable: use the in-file conservative substitute for
      `data_locality` (documented, slower, lower quality) and set
      `degraded['data_locality']='local'`

  cap.t05.depth.depth_width_tradeoff@1
      if unavailable: use the in-file conservative substitute for
      `depth_width_tradeoff` (documented, slower, lower quality) and set
      `degraded['depth_width_tradeoff']='local'`

  cap.t06.difficulty.difficulty_routing@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_routing` (documented, slower, lower quality) and set
      `degraded['difficulty_routing']='local'`

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
   3. [ 600 lines] Core implementation A - parallel-plan execution with collective scheduling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-device stream coordination and event fencing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - rank-failure detection with request preservation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - scaling efficiency measurement across devices
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
     exactly (capability == cap.t08.multi.multi_gpu_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0374_multi_gpu_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0375-model-loading

**P0375 · `model_loading` — Fast Model Loading & Warm Start** · [spec](PART_SPECS_T08.md#p0375-model-loading) · [self-contained txt](../prompts/P0375_model_loading.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0375  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0375 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0375  (25/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Fast Model Loading & Warm Start
file         : parts/t08_inference/P0375_model_loading.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.model_loading
language     : Rust 1.86
capability   : cap.t08.model.model_loading@1
determinism  : io
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
From cold storage to serving in seconds, not minutes.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. memory-mapped shard loading with lazy materialisation
  2. parallel load pipelines saturating storage bandwidth
  3. warmup kernel-compilation and cache priming
  4. cold-start-to-first-token measurement

Expanded obligations:
  1. Implement memory-mapped shard loading with lazy materialisation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement parallel load pipelines saturating storage bandwidth as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement warmup kernel-compilation and cache priming, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement cold-start-to-first-token measurement with an explicit
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.model.model_loading@1
  cap.t08.model.model_loading.describe@1

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

  cap.t08.multi.multi_gpu_runtime@1
      if unavailable: use the in-file conservative substitute for
      `multi_gpu_runtime` (documented, slower, lower quality) and set
      `degraded['multi_gpu_runtime']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t02.power.power_thermal@1
      if unavailable: use the in-file conservative substitute for
      `power_thermal` (documented, slower, lower quality) and set
      `degraded['power_thermal']='local'`

  cap.t03.pass.pass_search@1
      if unavailable: use the in-file conservative substitute for
      `pass_search` (documented, slower, lower quality) and set
      `degraded['pass_search']='local'`

  cap.t04.numa.numa_topology_cluster@1
      if unavailable: use the in-file conservative substitute for
      `numa_topology_cluster` (documented, slower, lower quality) and set
      `degraded['numa_topology_cluster']='local'`

  cap.t05.sparse.sparse_upcycling@1
      if unavailable: use the in-file conservative substitute for
      `sparse_upcycling` (documented, slower, lower quality) and set
      `degraded['sparse_upcycling']='local'`

  cap.t06.moe.moe_memory_budget@1
      if unavailable: use the in-file conservative substitute for
      `moe_memory_budget` (documented, slower, lower quality) and set
      `degraded['moe_memory_budget']='local'`

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
   3. [ 600 lines] Core implementation A - memory-mapped shard loading with lazy materialisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - parallel load pipelines saturating storage bandwidth
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - warmup kernel-compilation and cache priming
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cold-start-to-first-token measurement
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
     exactly (capability == cap.t08.model.model_loading@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0375_model_loading.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0376-weight-hotswap

**P0376 · `weight_hotswap` — Zero-Downtime Weight Hot Swap** · [spec](PART_SPECS_T08.md#p0376-weight-hotswap) · [self-contained txt](../prompts/P0376_weight_hotswap.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0376  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0376 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0376  (26/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Zero-Downtime Weight Hot Swap
file         : parts/t08_inference/P0376_weight_hotswap.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.weight_hotswap
language     : Rust 1.86
capability   : cap.t08.weight.weight_hotswap@1
determinism  : io
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Updates the model without dropping a single request.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dual-residency swap with atomic pointer flip
  2. in-flight-request version pinning for consistency
  3. rollback on quality-metric regression
  4. swap-duration and request-impact measurement

Expanded obligations:
  1. Implement dual-residency swap with atomic pointer flip as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement in-flight-request version pinning for consistency, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement rollback on quality-metric regression with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement swap-duration and request-impact measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.weight.weight_hotswap@1
  cap.t08.weight.weight_hotswap.describe@1

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

  cap.t08.model.model_loading@1
      if unavailable: use the in-file conservative substitute for
      `model_loading` (documented, slower, lower quality) and set
      `degraded['model_loading']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t02.ragged.ragged_batch@1
      if unavailable: use the in-file conservative substitute for
      `ragged_batch` (documented, slower, lower quality) and set
      `degraded['ragged_batch']='local'`

  cap.t03.numeric.numeric_mode_lowering@1
      if unavailable: use the in-file conservative substitute for
      `numeric_mode_lowering` (documented, slower, lower quality) and set
      `degraded['numeric_mode_lowering']='local'`

  cap.t04.hw.hw_sw_codesign@1
      if unavailable: use the in-file conservative substitute for
      `hw_sw_codesign` (documented, slower, lower quality) and set
      `degraded['hw_sw_codesign']='local'`

  cap.t05.model.model_config_schema@1
      if unavailable: use the in-file conservative substitute for
      `model_config_schema` (documented, slower, lower quality) and set
      `degraded['model_config_schema']='local'`

  cap.t06.moe.moe_visualisation@1
      if unavailable: use the in-file conservative substitute for
      `moe_visualisation` (documented, slower, lower quality) and set
      `degraded['moe_visualisation']='local'`

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
   3. [ 600 lines] Core implementation A - dual-residency swap with atomic pointer flip
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - in-flight-request version pinning for consistency
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - rollback on quality-metric regression
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - swap-duration and request-impact measurement
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
     exactly (capability == cap.t08.weight.weight_hotswap@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0376_weight_hotswap.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0377-multi-model-serving

**P0377 · `multi_model_serving` — Multi-Model Co-Residency & Time Slicing** · [spec](PART_SPECS_T08.md#p0377-multi-model-serving) · [self-contained txt](../prompts/P0377_multi_model_serving.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0377  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0377 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0377  (27/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Multi-Model Co-Residency & Time Slicing
file         : parts/t08_inference/P0377_multi_model_serving.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.multi_model_serving
language     : Rust 1.86
capability   : cap.t08.multi.multi_model_serving@1
determinism  : io
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Many models on one machine without thrashing.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. memory-aware model residency planner with LRU eviction
  2. time-slicing with SLO-aware quantum selection
  3. cross-model interference measurement and mitigation
  4. utilisation improvement measurement

Expanded obligations:
  1. Implement memory-aware model residency planner with LRU eviction, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement time-slicing with SLO-aware quantum selection with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement cross-model interference measurement and mitigation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement utilisation improvement measurement as a first-class, fully
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.multi.multi_model_serving@1
  cap.t08.multi.multi_model_serving.describe@1

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

  cap.t08.weight.weight_hotswap@1
      if unavailable: use the in-file conservative substitute for
      `weight_hotswap` (documented, slower, lower quality) and set
      `degraded['weight_hotswap']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t02.gemm.gemm_grouped@1
      if unavailable: use the in-file conservative substitute for
      `gemm_grouped` (documented, slower, lower quality) and set
      `degraded['gemm_grouped']='local'`

  cap.t03.ir.ir_printer@1
      if unavailable: use the in-file conservative substitute for
      `ir_printer` (documented, slower, lower quality) and set
      `degraded['ir_printer']='local'`

  cap.t04.collective.collective_global@1
      if unavailable: use the in-file conservative substitute for
      `collective_global` (documented, slower, lower quality) and set
      `degraded['collective_global']='local'`

  cap.t05.attention.attention_variants@1
      if unavailable: use the in-file conservative substitute for
      `attention_variants` (documented, slower, lower quality) and set
      `degraded['attention_variants']='local'`

  cap.t06.router.router_capacity@1
      if unavailable: use the in-file conservative substitute for
      `router_capacity` (documented, slower, lower quality) and set
      `degraded['router_capacity']='local'`

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
   3. [ 600 lines] Core implementation A - memory-aware model residency planner with LRU eviction
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - time-slicing with SLO-aware quantum selection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cross-model interference measurement and mitigation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - utilisation improvement measurement
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
     exactly (capability == cap.t08.multi.multi_model_serving@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0377_multi_model_serving.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0378-adapter-serving

**P0378 · `adapter_serving` — Adapter & Fine-Tune Multiplexing** · [spec](PART_SPECS_T08.md#p0378-adapter-serving) · [self-contained txt](../prompts/P0378_adapter_serving.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0378  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0378 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0378  (28/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Adapter & Fine-Tune Multiplexing
file         : parts/t08_inference/P0378_adapter_serving.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.adapter_serving
language     : Rust 1.86
capability   : cap.t08.adapter.adapter_serving@1
determinism  : io
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Thousands of customised variants served from one base model.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. batched multi-adapter execution with grouped kernels
  2. adapter cache with predictive loading
  3. per-adapter quality isolation verification
  4. throughput measurement at 1000 concurrent adapters

Expanded obligations:
  1. Implement batched multi-adapter execution with grouped kernels with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement adapter cache with predictive loading together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement per-adapter quality isolation verification as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement throughput measurement at 1000 concurrent adapters, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.adapter.adapter_serving@1
  cap.t08.adapter.adapter_serving.describe@1

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

  cap.t08.multi.multi_model_serving@1
      if unavailable: use the in-file conservative substitute for
      `multi_model_serving` (documented, slower, lower quality) and set
      `degraded['multi_model_serving']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t02.conv.conv_depthwise@1
      if unavailable: use the in-file conservative substitute for
      `conv_depthwise` (documented, slower, lower quality) and set
      `degraded['conv_depthwise']='local'`

  cap.t03.memory.memory_planner@1
      if unavailable: use the in-file conservative substitute for
      `memory_planner` (documented, slower, lower quality) and set
      `degraded['memory_planner']='local'`

  cap.t04.param.param_server_shard@1
      if unavailable: use the in-file conservative substitute for
      `param_server_shard` (documented, slower, lower quality) and set
      `degraded['param_server_shard']='local'`

  cap.t05.activation.activation_design@1
      if unavailable: use the in-file conservative substitute for
      `activation_design` (documented, slower, lower quality) and set
      `degraded['activation_design']='local'`

  cap.t06.expert.expert_prefetch@1
      if unavailable: use the in-file conservative substitute for
      `expert_prefetch` (documented, slower, lower quality) and set
      `degraded['expert_prefetch']='local'`

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
   3. [ 600 lines] Core implementation A - batched multi-adapter execution with grouped kernels
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - adapter cache with predictive loading
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-adapter quality isolation verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput measurement at 1000 concurrent adapters
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
     exactly (capability == cap.t08.adapter.adapter_serving@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0378_adapter_serving.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0379-request-lifecycle

**P0379 · `request_lifecycle` — Request Lifecycle & State Machine** · [spec](PART_SPECS_T08.md#p0379-request-lifecycle) · [self-contained txt](../prompts/P0379_request_lifecycle.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0379  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0379 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0379  (29/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Request Lifecycle & State Machine
file         : parts/t08_inference/P0379_request_lifecycle.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.request_lifecycle
language     : Rust 1.86
capability   : cap.t08.request.request_lifecycle@1
determinism  : io
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Every request's journey is explicit, observable and recoverable.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. state machine with legal transitions and timeout at every state
  2. cancellation propagation with immediate resource release
  3. mid-flight migration between workers
  4. lifecycle-invariant verification under fault injection

Expanded obligations:
  1. Implement state machine with legal transitions and timeout at every
     state together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Terminal-Bench
     2.1 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement cancellation propagation with immediate resource release as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement mid-flight migration between workers, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement lifecycle-invariant verification under fault injection with an
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.request.request_lifecycle@1
  cap.t08.request.request_lifecycle.describe@1

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

  cap.t08.adapter.adapter_serving@1
      if unavailable: use the in-file conservative substitute for
      `adapter_serving` (documented, slower, lower quality) and set
      `degraded['adapter_serving']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t02.rope.rope_embed@1
      if unavailable: use the in-file conservative substitute for
      `rope_embed` (documented, slower, lower quality) and set
      `degraded['rope_embed']='local'`

  cap.t03.cost.cost_model_learned@1
      if unavailable: use the in-file conservative substitute for
      `cost_model_learned` (documented, slower, lower quality) and set
      `degraded['cost_model_learned']='local'`

  cap.t04.checkpoint.checkpoint_transport@1
      if unavailable: use the in-file conservative substitute for
      `checkpoint_transport` (documented, slower, lower quality) and set
      `degraded['checkpoint_transport']='local'`

  cap.t05.draft.draft_model_arch@1
      if unavailable: use the in-file conservative substitute for
      `draft_model_arch` (documented, slower, lower quality) and set
      `degraded['draft_model_arch']='local'`

  cap.t06.moe.moe_quantisation@1
      if unavailable: use the in-file conservative substitute for
      `moe_quantisation` (documented, slower, lower quality) and set
      `degraded['moe_quantisation']='local'`

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
   3. [ 600 lines] Core implementation A - state machine with legal transitions and timeout at every state
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cancellation propagation with immediate resource release
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - mid-flight migration between workers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - lifecycle-invariant verification under fault injection
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
     exactly (capability == cap.t08.request.request_lifecycle@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0379_request_lifecycle.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0380-cancellation

**P0380 · `cancellation` — Cancellation & Resource Reclamation** · [spec](PART_SPECS_T08.md#p0380-cancellation) · [self-contained txt](../prompts/P0380_cancellation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0380  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0380 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0380  (30/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Cancellation & Resource Reclamation
file         : parts/t08_inference/P0380_cancellation.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cancellation
language     : Rust 1.86
capability   : cap.t08.cancellation.cancellation@1
determinism  : io
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
A cancelled request stops costing money immediately.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cooperative cancellation checkpoints in every long operation
  2. in-flight tool-call cancellation with cleanup
  3. resource-reclaim verification (KV, memory, device time)
  4. cancellation-latency measurement

Expanded obligations:
  1. Implement cooperative cancellation checkpoints in every long operation
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement in-flight tool-call cancellation with cleanup, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement resource-reclaim verification (KV, memory, device time) with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement cancellation-latency measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
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
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cancellation.cancellation@1
  cap.t08.cancellation.cancellation.describe@1

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

  cap.t08.request.request_lifecycle@1
      if unavailable: use the in-file conservative substitute for
      `request_lifecycle` (documented, slower, lower quality) and set
      `degraded['request_lifecycle']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t02.mem.mem_pool_device@1
      if unavailable: use the in-file conservative substitute for
      `mem_pool_device` (documented, slower, lower quality) and set
      `degraded['mem_pool_device']='local'`

  cap.t03.dynamic.dynamic_shapes@1
      if unavailable: use the in-file conservative substitute for
      `dynamic_shapes` (documented, slower, lower quality) and set
      `degraded['dynamic_shapes']='local'`

  cap.t04.heterogeneous.heterogeneous_pool@1
      if unavailable: use the in-file conservative substitute for
      `heterogeneous_pool` (documented, slower, lower quality) and set
      `degraded['heterogeneous_pool']='local'`

  cap.t05.meta.meta_learning_arch@1
      if unavailable: use the in-file conservative substitute for
      `meta_learning_arch` (documented, slower, lower quality) and set
      `degraded['meta_learning_arch']='local'`

  cap.t06.gating.gating_alternatives@1
      if unavailable: use the in-file conservative substitute for
      `gating_alternatives` (documented, slower, lower quality) and set
      `degraded['gating_alternatives']='local'`

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
   3. [ 600 lines] Core implementation A - cooperative cancellation checkpoints in every long operation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - in-flight tool-call cancellation with cleanup
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - resource-reclaim verification (KV, memory, device time)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cancellation-latency measurement
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
     exactly (capability == cap.t08.cancellation.cancellation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0380_cancellation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0381-deadline-scheduling

**P0381 · `deadline_scheduling` — Deadline-Aware Execution** · [spec](PART_SPECS_T08.md#p0381-deadline-scheduling) · [self-contained txt](../prompts/P0381_deadline_scheduling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0381  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0381 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0381  (31/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Deadline-Aware Execution
file         : parts/t08_inference/P0381_deadline_scheduling.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.deadline_scheduling
language     : Rust 1.86
capability   : cap.t08.deadline.deadline_scheduling@1
determinism  : io
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Meets stated deadlines by degrading gracefully, never silently.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. deadline propagation into kernel-level work decisions
  2. quality-degradation ladder triggered by deadline pressure
  3. partial-result emission with explicit completeness annotation
  4. deadline-attainment measurement under load

Expanded obligations:
  1. Implement deadline propagation into kernel-level work decisions, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement quality-degradation ladder triggered by deadline pressure with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement partial-result emission with explicit completeness annotation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement deadline-attainment measurement under load as a first-class,
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
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.deadline.deadline_scheduling@1
  cap.t08.deadline.deadline_scheduling.describe@1

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

  cap.t08.cancellation.cancellation@1
      if unavailable: use the in-file conservative substitute for
      `cancellation` (documented, slower, lower quality) and set
      `degraded['cancellation']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t02.kernel.kernel_verify@1
      if unavailable: use the in-file conservative substitute for
      `kernel_verify` (documented, slower, lower quality) and set
      `degraded['kernel_verify']='local'`

  cap.t03.ir.ir_verifier@1
      if unavailable: use the in-file conservative substitute for
      `ir_verifier` (documented, slower, lower quality) and set
      `degraded['ir_verifier']='local'`

  cap.t04.clock.clock_sync@1
      if unavailable: use the in-file conservative substitute for
      `clock_sync` (documented, slower, lower quality) and set
      `degraded['clock_sync']='local'`

  cap.t05.architecture.architecture_search@1
      if unavailable: use the in-file conservative substitute for
      `architecture_search` (documented, slower, lower quality) and set
      `degraded['architecture_search']='local'`

  cap.t06.modality.modality_routing@1
      if unavailable: use the in-file conservative substitute for
      `modality_routing` (documented, slower, lower quality) and set
      `degraded['modality_routing']='local'`

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
   3. [ 600 lines] Core implementation A - deadline propagation into kernel-level work decisions
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quality-degradation ladder triggered by deadline pressure
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partial-result emission with explicit completeness annotation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - deadline-attainment measurement under load
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
     exactly (capability == cap.t08.deadline.deadline_scheduling@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0381_deadline_scheduling.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0382-speculative-tools

**P0382 · `speculative_tools` — Speculative Tool Execution** · [spec](PART_SPECS_T08.md#p0382-speculative-tools) · [self-contained txt](../prompts/P0382_speculative_tools.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0382  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0382 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0382  (32/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Speculative Tool Execution
file         : parts/t08_inference/P0382_speculative_tools.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.speculative_tools
language     : Rust 1.86
capability   : cap.t08.speculative.speculative_tools@1
determinism  : io
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Runs likely tool calls before the model finishes asking (S6 source).

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tool-call prediction from partial generation
  2. side-effect-free-only speculation with strict gating
  3. misprediction cost accounting and cancellation
  4. measured latency reduction on agent workloads

Expanded obligations:
  1. Implement tool-call prediction from partial generation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Terminal-Bench 2.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement side-effect-free-only speculation with strict gating together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement misprediction cost accounting and cancellation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured latency reduction on agent workloads, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
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
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.speculative.speculative_tools@1
  cap.t08.speculative.speculative_tools.describe@1

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

  cap.t08.deadline.deadline_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `deadline_scheduling` (documented, slower, lower quality) and set
      `degraded['deadline_scheduling']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t02.stream.stream_scheduler@1
      if unavailable: use the in-file conservative substitute for
      `stream_scheduler` (documented, slower, lower quality) and set
      `degraded['stream_scheduler']='local'`

  cap.t03.debug.debug_symbols@1
      if unavailable: use the in-file conservative substitute for
      `debug_symbols` (documented, slower, lower quality) and set
      `degraded['debug_symbols']='local'`

  cap.t04.device.device_reset@1
      if unavailable: use the in-file conservative substitute for
      `device_reset` (documented, slower, lower quality) and set
      `degraded['device_reset']='local'`

  cap.t05.speculative.speculative_arch_hooks@1
      if unavailable: use the in-file conservative substitute for
      `speculative_arch_hooks` (documented, slower, lower quality) and set
      `degraded['speculative_arch_hooks']='local'`

  cap.t06.routing.routing_fairness@1
      if unavailable: use the in-file conservative substitute for
      `routing_fairness` (documented, slower, lower quality) and set
      `degraded['routing_fairness']='local'`

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
   3. [ 600 lines] Core implementation A - tool-call prediction from partial generation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - side-effect-free-only speculation with strict gating
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - misprediction cost accounting and cancellation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured latency reduction on agent workloads
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
     exactly (capability == cap.t08.speculative.speculative_tools@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0382_speculative_tools.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0383-parallel-generation

**P0383 · `parallel_generation` — Parallel Multi-Branch Generation** · [spec](PART_SPECS_T08.md#p0383-parallel-generation) · [self-contained txt](../prompts/P0383_parallel_generation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0383  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0383 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0383  (33/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Parallel Multi-Branch Generation
file         : parts/t08_inference/P0383_parallel_generation.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.parallel_generation
language     : Rust 1.86
capability   : cap.t08.parallel.parallel_generation@1
determinism  : io
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Explores several answers at once and keeps the best.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. branch scheduling with shared prefix KV
  2. early pruning from verifier scores
  3. cost-capped exploration with budget accounting
  4. quality gain per extra dollar measurement

Expanded obligations:
  1. Implement branch scheduling with shared prefix KV together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement early pruning from verifier scores as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement cost-capped exploration with budget accounting, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement quality gain per extra dollar measurement with an explicit
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.parallel.parallel_generation@1
  cap.t08.parallel.parallel_generation.describe@1

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

  cap.t08.speculative.speculative_tools@1
      if unavailable: use the in-file conservative substitute for
      `speculative_tools` (documented, slower, lower quality) and set
      `degraded['speculative_tools']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t02.tensor.tensor_view@1
      if unavailable: use the in-file conservative substitute for
      `tensor_view` (documented, slower, lower quality) and set
      `degraded['tensor_view']='local'`

  cap.t03.crosscompile.crosscompile@1
      if unavailable: use the in-file conservative substitute for
      `crosscompile` (documented, slower, lower quality) and set
      `degraded['crosscompile']='local'`

  cap.t04.region.region_failover@1
      if unavailable: use the in-file conservative substitute for
      `region_failover` (documented, slower, lower quality) and set
      `degraded['region_failover']='local'`

  cap.t05.expert.expert_specialisation@1
      if unavailable: use the in-file conservative substitute for
      `expert_specialisation` (documented, slower, lower quality) and set
      `degraded['expert_specialisation']='local'`

  cap.t06.router.router_bench@1
      if unavailable: use the in-file conservative substitute for
      `router_bench` (documented, slower, lower quality) and set
      `degraded['router_bench']='local'`

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
   3. [ 600 lines] Core implementation A - branch scheduling with shared prefix KV
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - early pruning from verifier scores
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cost-capped exploration with budget accounting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - quality gain per extra dollar measurement
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
     exactly (capability == cap.t08.parallel.parallel_generation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0383_parallel_generation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0384-output-verification-loop

**P0384 · `output_verification_loop` — Inline Output Verification Loop** · [spec](PART_SPECS_T08.md#p0384-output-verification-loop) · [self-contained txt](../prompts/P0384_output_verification_loop.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0384  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0384 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0384  (34/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Inline Output Verification Loop
file         : parts/t08_inference/P0384_output_verification_loop.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.output_verification_loop
language     : Rust 1.86
capability   : cap.t08.output.output_verification_loop@1
determinism  : io
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Checks its own answer before the user sees it.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. verifier invocation policy with latency budget
  2. targeted regeneration of only the failing span
  3. convergence guarantees and iteration caps
  4. measured error-rate reduction versus single-pass output

Expanded obligations:
  1. Implement verifier invocation policy with latency budget as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement targeted regeneration of only the failing span, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement convergence guarantees and iteration caps with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured error-rate reduction versus single-pass output
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.output.output_verification_loop@1
  cap.t08.output.output_verification_loop.describe@1

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

  cap.t08.parallel.parallel_generation@1
      if unavailable: use the in-file conservative substitute for
      `parallel_generation` (documented, slower, lower quality) and set
      `degraded['parallel_generation']='local'`

  cap.t02.gemm.gemm_int4@1
      if unavailable: use the in-file conservative substitute for
      `gemm_int4` (documented, slower, lower quality) and set
      `degraded['gemm_int4']='local'`

  cap.t03.ir.ir_builder@1
      if unavailable: use the in-file conservative substitute for
      `ir_builder` (documented, slower, lower quality) and set
      `degraded['ir_builder']='local'`

  cap.t04.topology.topology_discovery@1
      if unavailable: use the in-file conservative substitute for
      `topology_discovery` (documented, slower, lower quality) and set
      `degraded['topology_discovery']='local'`

  cap.t05.hybrid.hybrid_mixer@1
      if unavailable: use the in-file conservative substitute for
      `hybrid_mixer` (documented, slower, lower quality) and set
      `degraded['hybrid_mixer']='local'`

  cap.t06.router.router_balance@1
      if unavailable: use the in-file conservative substitute for
      `router_balance` (documented, slower, lower quality) and set
      `degraded['router_balance']='local'`

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
   3. [ 600 lines] Core implementation A - verifier invocation policy with latency budget
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - targeted regeneration of only the failing span
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - convergence guarantees and iteration caps
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured error-rate reduction versus single-pass output
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
     exactly (capability == cap.t08.output.output_verification_loop@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0384_output_verification_loop.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0385-engine-telemetry

**P0385 · `engine_telemetry` — Engine Observability & Latency Attribution** · [spec](PART_SPECS_T08.md#p0385-engine-telemetry) · [self-contained txt](../prompts/P0385_engine_telemetry.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0385  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0385 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0385  (35/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Engine Observability & Latency Attribution
file         : parts/t08_inference/P0385_engine_telemetry.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_telemetry
language     : Rust 1.86
capability   : cap.t08.engine.engine_telemetry@1
determinism  : io
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Explains exactly where every microsecond went.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-phase latency decomposition (queue, prefill, decode, tools, verify)
  2. per-request cost and token accounting
  3. anomaly detection on latency distributions
  4. overhead under 1% with sampling controls

Expanded obligations:
  1. Implement per-phase latency decomposition (queue, prefill, decode,
     tools, verify), and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement per-request cost and token accounting with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement anomaly detection on latency distributions together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement overhead under 1% with sampling controls as a first-class,
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_telemetry@1
  cap.t08.engine.engine_telemetry.describe@1

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

  cap.t08.output.output_verification_loop@1
      if unavailable: use the in-file conservative substitute for
      `output_verification_loop` (documented, slower, lower quality) and set
      `degraded['output_verification_loop']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t02.ssm.ssm_scan@1
      if unavailable: use the in-file conservative substitute for `ssm_scan`
      (documented, slower, lower quality) and set
      `degraded['ssm_scan']='local'`

  cap.t03.layout.layout_assignment@1
      if unavailable: use the in-file conservative substitute for
      `layout_assignment` (documented, slower, lower quality) and set
      `degraded['layout_assignment']='local'`

  cap.t04.pipeline.pipeline_fabric@1
      if unavailable: use the in-file conservative substitute for
      `pipeline_fabric` (documented, slower, lower quality) and set
      `degraded['pipeline_fabric']='local'`

  cap.t05.normalisation.normalisation_design@1
      if unavailable: use the in-file conservative substitute for
      `normalisation_design` (documented, slower, lower quality) and set
      `degraded['normalisation_design']='local'`

  cap.t06.expert.expert_placement@1
      if unavailable: use the in-file conservative substitute for
      `expert_placement` (documented, slower, lower quality) and set
      `degraded['expert_placement']='local'`

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
   3. [ 600 lines] Core implementation A - per-phase latency decomposition (queue, prefill, decode, tools, 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-request cost and token accounting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - anomaly detection on latency distributions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - overhead under 1% with sampling controls
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
     exactly (capability == cap.t08.engine.engine_telemetry@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0385_engine_telemetry.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0386-autoscaling

**P0386 · `autoscaling` — Load Prediction & Autoscaling Controller** · [spec](PART_SPECS_T08.md#p0386-autoscaling) · [self-contained txt](../prompts/P0386_autoscaling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0386  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0386 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0386  (36/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Load Prediction & Autoscaling Controller
file         : parts/t08_inference/P0386_autoscaling.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.autoscaling
language     : Rust 1.86
capability   : cap.t08.autoscaling.autoscaling@1
determinism  : io
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Right-sizes capacity ahead of demand.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. short-horizon load forecasting with uncertainty
  2. scale-up/down policy with cooldowns and cost constraints
  3. cold-capacity warmup coordination
  4. SLO attainment versus cost measurement

Expanded obligations:
  1. Implement short-horizon load forecasting with uncertainty with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement scale-up/down policy with cooldowns and cost constraints
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement cold-capacity warmup coordination as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement SLO attainment versus cost measurement, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.autoscaling.autoscaling@1
  cap.t08.autoscaling.autoscaling.describe@1

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

  cap.t08.engine.engine_telemetry@1
      if unavailable: use the in-file conservative substitute for
      `engine_telemetry` (documented, slower, lower quality) and set
      `degraded['engine_telemetry']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t02.kv.kv_cache_kernels@1
      if unavailable: use the in-file conservative substitute for
      `kv_cache_kernels` (documented, slower, lower quality) and set
      `degraded['kv_cache_kernels']='local'`

  cap.t03.autotuner.autotuner_core@1
      if unavailable: use the in-file conservative substitute for
      `autotuner_core` (documented, slower, lower quality) and set
      `degraded['autotuner_core']='local'`

  cap.t04.elastic.elastic_scaling@1
      if unavailable: use the in-file conservative substitute for
      `elastic_scaling` (documented, slower, lower quality) and set
      `degraded['elastic_scaling']='local'`

  cap.t05.multi.multi_token_prediction@1
      if unavailable: use the in-file conservative substitute for
      `multi_token_prediction` (documented, slower, lower quality) and set
      `degraded['multi_token_prediction']='local'`

  cap.t06.sparse.sparse_activation_stats@1
      if unavailable: use the in-file conservative substitute for
      `sparse_activation_stats` (documented, slower, lower quality) and set
      `degraded['sparse_activation_stats']='local'`

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
   3. [ 600 lines] Core implementation A - short-horizon load forecasting with uncertainty
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - scale-up/down policy with cooldowns and cost constraints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cold-capacity warmup coordination
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - SLO attainment versus cost measurement
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
     exactly (capability == cap.t08.autoscaling.autoscaling@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0386_autoscaling.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0387-overload-shedding

**P0387 · `overload_shedding` — Overload Protection & Graceful Degradation** · [spec](PART_SPECS_T08.md#p0387-overload-shedding) · [self-contained txt](../prompts/P0387_overload_shedding.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0387  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0387 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0387  (37/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Overload Protection & Graceful Degradation
file         : parts/t08_inference/P0387_overload_shedding.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.overload_shedding
language     : Rust 1.86
capability   : cap.t08.overload.overload_shedding@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Under extreme load it gets slower and cheaper, never broken.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. priority-based load shedding with explicit user signalling
  2. quality-degradation ladder (fewer samples, smaller model, less search)
  3. shedding fairness across tenants
  4. behaviour verification at 10x rated load

Expanded obligations:
  1. Implement priority-based load shedding with explicit user signalling
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement quality-degradation ladder (fewer samples, smaller model, less
     search) as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement shedding fairness across tenants, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement behaviour verification at 10x rated load with an explicit
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.overload.overload_shedding@1
  cap.t08.overload.overload_shedding.describe@1

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

  cap.t08.autoscaling.autoscaling@1
      if unavailable: use the in-file conservative substitute for
      `autoscaling` (documented, slower, lower quality) and set
      `degraded['autoscaling']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t02.graph.graph_capture@1
      if unavailable: use the in-file conservative substitute for
      `graph_capture` (documented, slower, lower quality) and set
      `degraded['graph_capture']='local'`

  cap.t03.graph.graph_partition_device@1
      if unavailable: use the in-file conservative substitute for
      `graph_partition_device` (documented, slower, lower quality) and set
      `degraded['graph_partition_device']='local'`

  cap.t04.device.device_virtualisation@1
      if unavailable: use the in-file conservative substitute for
      `device_virtualisation` (documented, slower, lower quality) and set
      `degraded['device_virtualisation']='local'`

  cap.t05.program.program_induction_arch@1
      if unavailable: use the in-file conservative substitute for
      `program_induction_arch` (documented, slower, lower quality) and set
      `degraded['program_induction_arch']='local'`

  cap.t06.router.router_robustness@1
      if unavailable: use the in-file conservative substitute for
      `router_robustness` (documented, slower, lower quality) and set
      `degraded['router_robustness']='local'`

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
   3. [ 600 lines] Core implementation A - priority-based load shedding with explicit user signalling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quality-degradation ladder (fewer samples, smaller model, less s
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - shedding fairness across tenants
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - behaviour verification at 10x rated load
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
     exactly (capability == cap.t08.overload.overload_shedding@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0387_overload_shedding.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0388-engine-determinism

**P0388 · `engine_determinism` — Deterministic Serving Mode** · [spec](PART_SPECS_T08.md#p0388-engine-determinism) · [self-contained txt](../prompts/P0388_engine_determinism.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0388  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0388 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0388  (38/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Deterministic Serving Mode
file         : parts/t08_inference/P0388_engine_determinism.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_determinism
language     : Rust 1.86
capability   : cap.t08.engine.engine_determinism@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Reproducible outputs for audit, test and legal contexts.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. end-to-end determinism: seeds, batching, reductions, tool order
  2. replay verification producing byte-identical outputs
  3. cost-of-determinism measurement
  4. documented exceptions with justification

Expanded obligations:
  1. Implement end-to-end determinism: seeds, batching, reductions, tool
     order as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement replay verification producing byte-identical outputs, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement cost-of-determinism measurement with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement documented exceptions with justification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_determinism@1
  cap.t08.engine.engine_determinism.describe@1

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

  cap.t08.overload.overload_shedding@1
      if unavailable: use the in-file conservative substitute for
      `overload_shedding` (documented, slower, lower quality) and set
      `degraded['overload_shedding']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t02.kernel.kernel_registry@1
      if unavailable: use the in-file conservative substitute for
      `kernel_registry` (documented, slower, lower quality) and set
      `degraded['kernel_registry']='local'`

  cap.t03.effect.effect_system@1
      if unavailable: use the in-file conservative substitute for
      `effect_system` (documented, slower, lower quality) and set
      `degraded['effect_system']='local'`

  cap.t04.distributed.distributed_lock@1
      if unavailable: use the in-file conservative substitute for
      `distributed_lock` (documented, slower, lower quality) and set
      `degraded['distributed_lock']='local'`

  cap.t05.init.init_scaling_laws@1
      if unavailable: use the in-file conservative substitute for
      `init_scaling_laws` (documented, slower, lower quality) and set
      `degraded['init_scaling_laws']='local'`

  cap.t06.sparse.sparse_kernels_bridge@1
      if unavailable: use the in-file conservative substitute for
      `sparse_kernels_bridge` (documented, slower, lower quality) and set
      `degraded['sparse_kernels_bridge']='local'`

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
   3. [ 600 lines] Core implementation A - end-to-end determinism: seeds, batching, reductions, tool order
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - replay verification producing byte-identical outputs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cost-of-determinism measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - documented exceptions with justification
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
     exactly (capability == cap.t08.engine.engine_determinism@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0388_engine_determinism.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0389-kv-offload-runtime

**P0389 · `kv_offload_runtime` — KV Offload & Recall Runtime** · [spec](PART_SPECS_T08.md#p0389-kv-offload-runtime) · [self-contained txt](../prompts/P0389_kv_offload_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0389  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0389 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0389  (39/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : KV Offload & Recall Runtime
file         : parts/t08_inference/P0389_kv_offload_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.kv_offload_runtime
language     : Rust 1.86
capability   : cap.t08.kv.kv_offload_runtime@1
determinism  : io
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Long conversations live in cheap memory until needed.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. asynchronous KV demotion/promotion overlapped with decode
  2. recall-latency hiding via lookahead prediction
  3. stall-free guarantee under sustained offload
  4. cost reduction measurement at matched latency

Expanded obligations:
  1. Implement asynchronous KV demotion/promotion overlapped with decode, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Terminal-Bench 2.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement recall-latency hiding via lookahead prediction with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement stall-free guarantee under sustained offload together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement cost reduction measurement at matched latency as a
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.kv.kv_offload_runtime@1
  cap.t08.kv.kv_offload_runtime.describe@1

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

  cap.t08.engine.engine_determinism@1
      if unavailable: use the in-file conservative substitute for
      `engine_determinism` (documented, slower, lower quality) and set
      `degraded['engine_determinism']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t02.p2p.p2p_transfer@1
      if unavailable: use the in-file conservative substitute for
      `p2p_transfer` (documented, slower, lower quality) and set
      `degraded['p2p_transfer']='local'`

  cap.t03.bytecode.bytecode_vm@1
      if unavailable: use the in-file conservative substitute for
      `bytecode_vm` (documented, slower, lower quality) and set
      `degraded['bytecode_vm']='local'`

  cap.t04.nic.nic_offload@1
      if unavailable: use the in-file conservative substitute for
      `nic_offload` (documented, slower, lower quality) and set
      `degraded['nic_offload']='local'`

  cap.t05.memory.memory_attention_bridge@1
      if unavailable: use the in-file conservative substitute for
      `memory_attention_bridge` (documented, slower, lower quality) and set
      `degraded['memory_attention_bridge']='local'`

  cap.t06.expert.expert_warmup@1
      if unavailable: use the in-file conservative substitute for
      `expert_warmup` (documented, slower, lower quality) and set
      `degraded['expert_warmup']='local'`

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
   3. [ 600 lines] Core implementation A - asynchronous KV demotion/promotion overlapped with decode
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - recall-latency hiding via lookahead prediction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - stall-free guarantee under sustained offload
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost reduction measurement at matched latency
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
     exactly (capability == cap.t08.kv.kv_offload_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0389_kv_offload_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0390-quantised-serving

**P0390 · `quantised_serving` — Quantised Serving Paths & Quality Gates** · [spec](PART_SPECS_T08.md#p0390-quantised-serving) · [self-contained txt](../prompts/P0390_quantised_serving.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0390  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0390 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0390  (40/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Quantised Serving Paths & Quality Gates
file         : parts/t08_inference/P0390_quantised_serving.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.quantised_serving
language     : Rust 1.86
capability   : cap.t08.quantised.quantised_serving@1
determinism  : io
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Fast, cheap precision without silent quality loss.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-model precision plan execution with runtime verification
  2. canary quality checks comparing against a reference tier
  3. automatic fallback to higher precision on regression
  4. measured cost/quality frontier

Expanded obligations:
  1. Implement per-model precision plan execution with runtime verification
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Terminal-Bench 2.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement canary quality checks comparing against a reference tier
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement automatic fallback to higher precision on regression as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured cost/quality frontier, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against Terminal-Bench 2.1 — a regression on that benchmark
     is an automatic rejection of this part.

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
  cap.t08.quantised.quantised_serving@1
  cap.t08.quantised.quantised_serving.describe@1

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

  cap.t08.kv.kv_offload_runtime@1
      if unavailable: use the in-file conservative substitute for
      `kv_offload_runtime` (documented, slower, lower quality) and set
      `degraded['kv_offload_runtime']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t02.mask.mask_engine@1
      if unavailable: use the in-file conservative substitute for
      `mask_engine` (documented, slower, lower quality) and set
      `degraded['mask_engine']='local'`

  cap.t03.incremental.incremental_build@1
      if unavailable: use the in-file conservative substitute for
      `incremental_build` (documented, slower, lower quality) and set
      `degraded['incremental_build']='local'`

  cap.t04.request.request_router@1
      if unavailable: use the in-file conservative substitute for
      `request_router` (documented, slower, lower quality) and set
      `degraded['request_router']='local'`

  cap.t05.thought.thought_representation@1
      if unavailable: use the in-file conservative substitute for
      `thought_representation` (documented, slower, lower quality) and set
      `degraded['thought_representation']='local'`

  cap.t06.hierarchical.hierarchical_routing@1
      if unavailable: use the in-file conservative substitute for
      `hierarchical_routing` (documented, slower, lower quality) and set
      `degraded['hierarchical_routing']='local'`

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
   3. [ 600 lines] Core implementation A - per-model precision plan execution with runtime verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - canary quality checks comparing against a reference tier
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic fallback to higher precision on regression
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured cost/quality frontier
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
     exactly (capability == cap.t08.quantised.quantised_serving@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0390_quantised_serving.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0391-engine-fault-tolerance

**P0391 · `engine_fault_tolerance` — Engine Fault Tolerance & Request Recovery** · [spec](PART_SPECS_T08.md#p0391-engine-fault-tolerance) · [self-contained txt](../prompts/P0391_engine_fault_tolerance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0391  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0391 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0391  (41/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Engine Fault Tolerance & Request Recovery
file         : parts/t08_inference/P0391_engine_fault_tolerance.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_fault_tolerance
language     : Rust 1.86
capability   : cap.t08.engine.engine_fault_tolerance@1
determinism  : io
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
A crashed worker loses zero requests.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. request journaling with idempotent replay
  2. partial-output checkpointing for long generations
  3. device-failure detection and rapid rescheduling
  4. measured request-loss rate under injected faults

Expanded obligations:
  1. Implement request journaling with idempotent replay together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement partial-output checkpointing for long generations as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement device-failure detection and rapid rescheduling, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured request-loss rate under injected faults with an
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_fault_tolerance@1
  cap.t08.engine.engine_fault_tolerance.describe@1

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

  cap.t08.quantised.quantised_serving@1
      if unavailable: use the in-file conservative substitute for
      `quantised_serving` (documented, slower, lower quality) and set
      `degraded['quantised_serving']='local'`

  cap.t02.gemm.gemm_fp8@1
      if unavailable: use the in-file conservative substitute for `gemm_fp8`
      (documented, slower, lower quality) and set
      `degraded['gemm_fp8']='local'`

  cap.t03.ir.ir_core@1
      if unavailable: use the in-file conservative substitute for `ir_core`
      (documented, slower, lower quality) and set
      `degraded['ir_core']='local'`

  cap.t04.device.device_abstraction@1
      if unavailable: use the in-file conservative substitute for
      `device_abstraction` (documented, slower, lower quality) and set
      `degraded['device_abstraction']='local'`

  cap.t05.omega.omega_block@1
      if unavailable: use the in-file conservative substitute for
      `omega_block` (documented, slower, lower quality) and set
      `degraded['omega_block']='local'`

  cap.t06.router.router_core@1
      if unavailable: use the in-file conservative substitute for
      `router_core` (documented, slower, lower quality) and set
      `degraded['router_core']='local'`

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
   3. [ 600 lines] Core implementation A - request journaling with idempotent replay
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - partial-output checkpointing for long generations
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - device-failure detection and rapid rescheduling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured request-loss rate under injected faults
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
     exactly (capability == cap.t08.engine.engine_fault_tolerance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0391_engine_fault_tolerance.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0392-api-gateway-runtime

**P0392 · `api_gateway_runtime` — Protocol Gateway & Request Normalisation** · [spec](PART_SPECS_T08.md#p0392-api-gateway-runtime) · [self-contained txt](../prompts/P0392_api_gateway_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0392  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0392 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0392  (42/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Protocol Gateway & Request Normalisation
file         : parts/t08_inference/P0392_api_gateway_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.api_gateway_runtime
language     : Rust 1.86
capability   : cap.t08.api.api_gateway_runtime@1
determinism  : io
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
One engine, many API dialects, one internal representation.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. request validation, normalisation and default resolution
  2. streaming-protocol adapters (SSE, websocket, gRPC)
  3. backward-compatibility handling across API versions
  4. gateway overhead measurement under 200 microseconds

Expanded obligations:
  1. Implement request validation, normalisation and default resolution as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement streaming-protocol adapters (SSE, websocket, gRPC), and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement backward-compatibility handling across API versions with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement gateway overhead measurement under 200 microseconds together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.api.api_gateway_runtime@1
  cap.t08.api.api_gateway_runtime.describe@1

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

  cap.t08.engine.engine_fault_tolerance@1
      if unavailable: use the in-file conservative substitute for
      `engine_fault_tolerance` (documented, slower, lower quality) and set
      `degraded['engine_fault_tolerance']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t02.attn.attn_linear@1
      if unavailable: use the in-file conservative substitute for
      `attn_linear` (documented, slower, lower quality) and set
      `degraded['attn_linear']='local'`

  cap.t03.fusion.fusion_pass@1
      if unavailable: use the in-file conservative substitute for
      `fusion_pass` (documented, slower, lower quality) and set
      `degraded['fusion_pass']='local'`

  cap.t04.sequence.sequence_parallel_fabric@1
      if unavailable: use the in-file conservative substitute for
      `sequence_parallel_fabric` (documented, slower, lower quality) and set
      `degraded['sequence_parallel_fabric']='local'`

  cap.t05.adaptive.adaptive_depth@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_depth` (documented, slower, lower quality) and set
      `degraded['adaptive_depth']='local'`

  cap.t06.fine.fine_grained_experts@1
      if unavailable: use the in-file conservative substitute for
      `fine_grained_experts` (documented, slower, lower quality) and set
      `degraded['fine_grained_experts']='local'`

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
   3. [ 600 lines] Core implementation A - request validation, normalisation and default resolution
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - streaming-protocol adapters (SSE, websocket, gRPC)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - backward-compatibility handling across API versions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - gateway overhead measurement under 200 microseconds
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
     exactly (capability == cap.t08.api.api_gateway_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0392_api_gateway_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0393-engine-bench-serving

**P0393 · `engine_bench_serving` — Serving Benchmark & Load Generator** · [spec](PART_SPECS_T08.md#p0393-engine-bench-serving) · [self-contained txt](../prompts/P0393_engine_bench_serving.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0393  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0393 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0393  (43/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Serving Benchmark & Load Generator
file         : parts/t08_inference/P0393_engine_bench_serving.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_bench_serving
language     : Rust 1.86
capability   : cap.t08.engine.engine_bench_serving@1
determinism  : io
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
The canonical performance measurements for the engine.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. realistic traffic generation from production-shaped distributions
  2. TTFT, ITL, throughput and cost metrics with variance bands
  3. comparison harness versus published Opus-class latencies
  4. regression gate with statistical significance

Expanded obligations:
  1. Implement realistic traffic generation from production-shaped
     distributions, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     Terminal-Bench 2.1 — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement TTFT, ITL, throughput and cost metrics with variance bands
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement comparison harness versus published Opus-class latencies
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement regression gate with statistical significance as a
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_bench_serving@1
  cap.t08.engine.engine_bench_serving.describe@1

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

  cap.t08.api.api_gateway_runtime@1
      if unavailable: use the in-file conservative substitute for
      `api_gateway_runtime` (documented, slower, lower quality) and set
      `degraded['api_gateway_runtime']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t02.quantize.quantize_kernels@1
      if unavailable: use the in-file conservative substitute for
      `quantize_kernels` (documented, slower, lower quality) and set
      `degraded['quantize_kernels']='local'`

  cap.t03.collective.collective_insertion@1
      if unavailable: use the in-file conservative substitute for
      `collective_insertion` (documented, slower, lower quality) and set
      `degraded['collective_insertion']='local'`

  cap.t04.fault.fault_domains@1
      if unavailable: use the in-file conservative substitute for
      `fault_domains` (documented, slower, lower quality) and set
      `degraded['fault_domains']='local'`

  cap.t05.long.long_context_arch@1
      if unavailable: use the in-file conservative substitute for
      `long_context_arch` (documented, slower, lower quality) and set
      `degraded['long_context_arch']='local'`

  cap.t06.router.router_temperature@1
      if unavailable: use the in-file conservative substitute for
      `router_temperature` (documented, slower, lower quality) and set
      `degraded['router_temperature']='local'`

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
   3. [ 600 lines] Core implementation A - realistic traffic generation from production-shaped distribution
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - TTFT, ITL, throughput and cost metrics with variance bands
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - comparison harness versus published Opus-class latencies
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - regression gate with statistical significance
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
     exactly (capability == cap.t08.engine.engine_bench_serving@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0393_engine_bench_serving.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0394-cascade-speed-proof

**P0394 · `cascade_speed_proof` — S1 Speedup Proof & Attribution** · [spec](PART_SPECS_T08.md#p0394-cascade-speed-proof) · [self-contained txt](../prompts/P0394_cascade_speed_proof.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0394  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0394 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0394  (44/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : S1 Speedup Proof & Attribution
file         : parts/t08_inference/P0394_cascade_speed_proof.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cascade_speed_proof
language     : Rust 1.86
capability   : cap.t08.cascade.cascade_speed_proof@1
determinism  : io
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Proves the 4.0x speculative-cascade component of the 100x law.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. acceptance-rate to speedup derivation with measured inputs
  2. interaction analysis with batching and sparsity factors
  3. confidence intervals over traffic mixes
  4. attribution report feeding the 100x proof

Expanded obligations:
  1. Implement acceptance-rate to speedup derivation with measured inputs
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement interaction analysis with batching and sparsity factors
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement confidence intervals over traffic mixes as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Terminal-Bench
     2.1 — a regression on that benchmark is an automatic rejection of this
     part.
  4. Implement attribution report feeding the 100x proof, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cascade.cascade_speed_proof@1
  cap.t08.cascade.cascade_speed_proof.describe@1

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

  cap.t08.engine.engine_bench_serving@1
      if unavailable: use the in-file conservative substitute for
      `engine_bench_serving` (documented, slower, lower quality) and set
      `degraded['engine_bench_serving']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t02.fused.fused_decode_step@1
      if unavailable: use the in-file conservative substitute for
      `fused_decode_step` (documented, slower, lower quality) and set
      `degraded['fused_decode_step']='local'`

  cap.t03.kernel.kernel_selection@1
      if unavailable: use the in-file conservative substitute for
      `kernel_selection` (documented, slower, lower quality) and set
      `degraded['kernel_selection']='local'`

  cap.t04.multi.multi_tenancy@1
      if unavailable: use the in-file conservative substitute for
      `multi_tenancy` (documented, slower, lower quality) and set
      `degraded['multi_tenancy']='local'`

  cap.t05.symbolic.symbolic_bridge@1
      if unavailable: use the in-file conservative substitute for
      `symbolic_bridge` (documented, slower, lower quality) and set
      `degraded['symbolic_bridge']='local'`

  cap.t06.mod.mod_routing@1
      if unavailable: use the in-file conservative substitute for
      `mod_routing` (documented, slower, lower quality) and set
      `degraded['mod_routing']='local'`

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
   3. [ 600 lines] Core implementation A - acceptance-rate to speedup derivation with measured inputs
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - interaction analysis with batching and sparsity factors
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - confidence intervals over traffic mixes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - attribution report feeding the 100x proof
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
     exactly (capability == cap.t08.cascade.cascade_speed_proof@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0394_cascade_speed_proof.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0395-engine-config-tuning

**P0395 · `engine_config_tuning` — Engine Configuration Auto-Tuning** · [spec](PART_SPECS_T08.md#p0395-engine-config-tuning) · [self-contained txt](../prompts/P0395_engine_config_tuning.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0395  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0395 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0395  (45/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Engine Configuration Auto-Tuning
file         : parts/t08_inference/P0395_engine_config_tuning.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_config_tuning
language     : Rust 1.86
capability   : cap.t08.engine.engine_config_tuning@1
determinism  : io
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Finds the best of thousands of engine settings automatically.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. parameter space definition with legality constraints
  2. SLO-constrained optimisation via bandit search on live traffic
  3. safe-exploration guardrails and instant rollback
  4. measured improvement over hand-tuned defaults

Expanded obligations:
  1. Implement parameter space definition with legality constraints together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Terminal-Bench 2.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement SLO-constrained optimisation via bandit search on live traffic
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement safe-exploration guardrails and instant rollback, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Terminal-Bench 2.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured improvement over hand-tuned defaults with an explicit
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_config_tuning@1
  cap.t08.engine.engine_config_tuning.describe@1

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

  cap.t08.cascade.cascade_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `cascade_speed_proof` (documented, slower, lower quality) and set
      `degraded['cascade_speed_proof']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t02.bf16.bf16_stability@1
      if unavailable: use the in-file conservative substitute for
      `bf16_stability` (documented, slower, lower quality) and set
      `degraded['bf16_stability']='local'`

  cap.t03.dead.dead_code_dce@1
      if unavailable: use the in-file conservative substitute for
      `dead_code_dce` (documented, slower, lower quality) and set
      `degraded['dead_code_dce']='local'`

  cap.t04.consensus.consensus_core@1
      if unavailable: use the in-file conservative substitute for
      `consensus_core` (documented, slower, lower quality) and set
      `degraded['consensus_core']='local'`

  cap.t05.weight.weight_sharing@1
      if unavailable: use the in-file conservative substitute for
      `weight_sharing` (documented, slower, lower quality) and set
      `degraded['weight_sharing']='local'`

  cap.t06.expert.expert_dropout@1
      if unavailable: use the in-file conservative substitute for
      `expert_dropout` (documented, slower, lower quality) and set
      `degraded['expert_dropout']='local'`

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
   3. [ 600 lines] Core implementation A - parameter space definition with legality constraints
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - SLO-constrained optimisation via bandit search on live traffic
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - safe-exploration guardrails and instant rollback
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured improvement over hand-tuned defaults
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
     exactly (capability == cap.t08.engine.engine_config_tuning@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0395_engine_config_tuning.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0396-tokenizer-runtime

**P0396 · `tokenizer_runtime` — Runtime Tokenisation & Detokenisation** · [spec](PART_SPECS_T08.md#p0396-tokenizer-runtime) · [self-contained txt](../prompts/P0396_tokenizer_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0396  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0396 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0396  (46/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Runtime Tokenisation & Detokenisation
file         : parts/t08_inference/P0396_tokenizer_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.tokenizer_runtime
language     : Rust 1.86
capability   : cap.t08.tokenizer.tokenizer_runtime@1
determinism  : io
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Tokenisation is never the bottleneck, and never wrong.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. high-throughput batched tokenisation with SIMD scanning
  2. incremental detokenisation with correct grapheme handling
  3. cross-language consistency verification
  4. throughput measurement in millions of tokens per second

Expanded obligations:
  1. Implement high-throughput batched tokenisation with SIMD scanning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement incremental detokenisation with correct grapheme handling, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement cross-language consistency verification with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement throughput measurement in millions of tokens per second
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.tokenizer.tokenizer_runtime@1
  cap.t08.tokenizer.tokenizer_runtime.describe@1

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

  cap.t08.engine.engine_config_tuning@1
      if unavailable: use the in-file conservative substitute for
      `engine_config_tuning` (documented, slower, lower quality) and set
      `degraded['engine_config_tuning']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t02.collective.collective_local@1
      if unavailable: use the in-file conservative substitute for
      `collective_local` (documented, slower, lower quality) and set
      `degraded['collective_local']='local'`

  cap.t03.ir.ir_serialization@1
      if unavailable: use the in-file conservative substitute for
      `ir_serialization` (documented, slower, lower quality) and set
      `degraded['ir_serialization']='local'`

  cap.t04.firmware.firmware_compat@1
      if unavailable: use the in-file conservative substitute for
      `firmware_compat` (documented, slower, lower quality) and set
      `degraded['firmware_compat']='local'`

  cap.t05.action.action_head@1
      if unavailable: use the in-file conservative substitute for
      `action_head` (documented, slower, lower quality) and set
      `degraded['action_head']='local'`

  cap.t06.router.router_cache@1
      if unavailable: use the in-file conservative substitute for
      `router_cache` (documented, slower, lower quality) and set
      `degraded['router_cache']='local'`

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
   3. [ 600 lines] Core implementation A - high-throughput batched tokenisation with SIMD scanning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - incremental detokenisation with correct grapheme handling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cross-language consistency verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput measurement in millions of tokens per second
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
     exactly (capability == cap.t08.tokenizer.tokenizer_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0396_tokenizer_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0397-prompt-compilation

**P0397 · `prompt_compilation` — Prompt Compilation & Static Prefill** · [spec](PART_SPECS_T08.md#p0397-prompt-compilation) · [self-contained txt](../prompts/P0397_prompt_compilation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0397  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0397 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0397  (47/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Prompt Compilation & Static Prefill
file         : parts/t08_inference/P0397_prompt_compilation.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.prompt_compilation
language     : Rust 1.86
capability   : cap.t08.prompt.prompt_compilation@1
determinism  : io
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Compiles fixed prompt scaffolding once, forever.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. prompt template compilation into precomputed KV artifacts
  2. slot-filling with position-correct KV splicing
  3. artifact cache with version invalidation
  4. measured prefill saving for templated workloads

Expanded obligations:
  1. Implement prompt template compilation into precomputed KV artifacts, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Terminal-Bench 2.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement slot-filling with position-correct KV splicing with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement artifact cache with version invalidation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Terminal-Bench 2.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured prefill saving for templated workloads as a
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.prompt.prompt_compilation@1
  cap.t08.prompt.prompt_compilation.describe@1

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

  cap.t08.tokenizer.tokenizer_runtime@1
      if unavailable: use the in-file conservative substitute for
      `tokenizer_runtime` (documented, slower, lower quality) and set
      `degraded['tokenizer_runtime']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t02.embedding.embedding_kernels@1
      if unavailable: use the in-file conservative substitute for
      `embedding_kernels` (documented, slower, lower quality) and set
      `degraded['embedding_kernels']='local'`

  cap.t03.linker.linker_omega@1
      if unavailable: use the in-file conservative substitute for
      `linker_omega` (documented, slower, lower quality) and set
      `degraded['linker_omega']='local'`

  cap.t04.cost.cost_model_cluster@1
      if unavailable: use the in-file conservative substitute for
      `cost_model_cluster` (documented, slower, lower quality) and set
      `degraded['cost_model_cluster']='local'`

  cap.t05.prompt.prompt_representation@1
      if unavailable: use the in-file conservative substitute for
      `prompt_representation` (documented, slower, lower quality) and set
      `degraded['prompt_representation']='local'`

  cap.t06.routing.routing_privacy@1
      if unavailable: use the in-file conservative substitute for
      `routing_privacy` (documented, slower, lower quality) and set
      `degraded['routing_privacy']='local'`

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
   3. [ 600 lines] Core implementation A - prompt template compilation into precomputed KV artifacts
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - slot-filling with position-correct KV splicing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - artifact cache with version invalidation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured prefill saving for templated workloads
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
     exactly (capability == cap.t08.prompt.prompt_compilation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0397_prompt_compilation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0398-engine-security

**P0398 · `engine_security` — Serving-Path Security Hardening** · [spec](PART_SPECS_T08.md#p0398-engine-security) · [self-contained txt](../prompts/P0398_engine_security.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0398  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0398 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0398  (48/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Serving-Path Security Hardening
file         : parts/t08_inference/P0398_engine_security.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_security
language     : Rust 1.86
capability   : cap.t08.engine.engine_security@1
determinism  : io
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
The engine is a hostile-input processor: it must be bulletproof.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. input validation, size limits and resource-exhaustion defences
  2. tenant isolation verification at every shared structure
  3. timing-side-channel analysis on shared caches
  4. adversarial-input fuzzing of the whole request path

Expanded obligations:
  1. Implement input validation, size limits and resource-exhaustion defences
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Terminal-Bench 2.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement tenant isolation verification at every shared structure
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement timing-side-channel analysis on shared caches as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement adversarial-input fuzzing of the whole request path, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_security@1
  cap.t08.engine.engine_security.describe@1

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

  cap.t08.prompt.prompt_compilation@1
      if unavailable: use the in-file conservative substitute for
      `prompt_compilation` (documented, slower, lower quality) and set
      `degraded['prompt_compilation']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t02.kernel.kernel_docs_spec@1
      if unavailable: use the in-file conservative substitute for
      `kernel_docs_spec` (documented, slower, lower quality) and set
      `degraded['kernel_docs_spec']='local'`

  cap.t03.build.build_provenance@1
      if unavailable: use the in-file conservative substitute for
      `build_provenance` (documented, slower, lower quality) and set
      `degraded['build_provenance']='local'`

  cap.t04.provision.provision_verify@1
      if unavailable: use the in-file conservative substitute for
      `provision_verify` (documented, slower, lower quality) and set
      `degraded['provision_verify']='local'`

  cap.t05.arch.arch_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `arch_spec_doc` (documented, slower, lower quality) and set
      `degraded['arch_spec_doc']='local'`

  cap.t06.moe.moe_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `moe_spec_doc` (documented, slower, lower quality) and set
      `degraded['moe_spec_doc']='local'`

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
   3. [ 600 lines] Core implementation A - input validation, size limits and resource-exhaustion defences
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tenant isolation verification at every shared structure
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - timing-side-channel analysis on shared caches
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - adversarial-input fuzzing of the whole request path
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
     exactly (capability == cap.t08.engine.engine_security@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0398_engine_security.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0399-cost-accounting-runtime

**P0399 · `cost_accounting_runtime` — Per-Request Cost Accounting** · [spec](PART_SPECS_T08.md#p0399-cost-accounting-runtime) · [self-contained txt](../prompts/P0399_cost_accounting_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0399  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0399 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0399  (49/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Per-Request Cost Accounting
file         : parts/t08_inference/P0399_cost_accounting_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.cost_accounting_runtime
language     : Rust 1.86
capability   : cap.t08.cost.cost_accounting_runtime@1
determinism  : io
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
Every request knows what it cost, to the microdollar.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. token, FLOP, device-time and energy accounting per request
  2. attribution across cascade stages and tool calls
  3. billing-grade accuracy verification
  4. cost-report generation for the platform tier

Expanded obligations:
  1. Implement token, FLOP, device-time and energy accounting per request
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement attribution across cascade stages and tool calls as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement billing-grade accuracy verification, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. This mechanism
     sits on the critical path of Terminal-Bench 2.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement cost-report generation for the platform tier with an explicit
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.cost.cost_accounting_runtime@1
  cap.t08.cost.cost_accounting_runtime.describe@1

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

  cap.t08.engine.engine_security@1
      if unavailable: use the in-file conservative substitute for
      `engine_security` (documented, slower, lower quality) and set
      `degraded['engine_security']='local'`

  cap.t02.attn.attn_paged_decode@1
      if unavailable: use the in-file conservative substitute for
      `attn_paged_decode` (documented, slower, lower quality) and set
      `degraded['attn_paged_decode']='local'`

  cap.t03.algebraic.algebraic_rewrite@1
      if unavailable: use the in-file conservative substitute for
      `algebraic_rewrite` (documented, slower, lower quality) and set
      `degraded['algebraic_rewrite']='local'`

  cap.t04.expert.expert_parallel_fabric@1
      if unavailable: use the in-file conservative substitute for
      `expert_parallel_fabric` (documented, slower, lower quality) and set
      `degraded['expert_parallel_fabric']='local'`

  cap.t05.latent.latent_program_slots@1
      if unavailable: use the in-file conservative substitute for
      `latent_program_slots` (documented, slower, lower quality) and set
      `degraded['latent_program_slots']='local'`

  cap.t06.shared.shared_expert@1
      if unavailable: use the in-file conservative substitute for
      `shared_expert` (documented, slower, lower quality) and set
      `degraded['shared_expert']='local'`

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
   3. [ 600 lines] Core implementation A - token, FLOP, device-time and energy accounting per request
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - attribution across cascade stages and tool calls
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - billing-grade accuracy verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost-report generation for the platform tier
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
     exactly (capability == cap.t08.cost.cost_accounting_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0399_cost_accounting_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0400-engine-spec-doc

**P0400 · `engine_spec_doc` — Inference Engine Specification & Runbook** · [spec](PART_SPECS_T08.md#p0400-engine-spec-doc) · [self-contained txt](../prompts/P0400_engine_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0400  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0400 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0400  (50/50 of tier T08)
tier         : T08 — Inference Engine & Ω-Cascade
title        : Inference Engine Specification & Runbook
file         : parts/t08_inference/P0400_engine_spec_doc.rs          <-- create exactly this path, nothing else
module       : hyperion.t08.inference.engine_spec_doc
language     : Rust 1.86
capability   : cap.t08.engine.engine_spec_doc@1
determinism  : io
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : Terminal-Bench 2.1

MISSION
-------
The authoritative description and operations guide.

Tier context:
  Continuous batching, paged KV, 8-stage speculative cascade, admission
  control. Source of speedup S1.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. specification of scheduling, guarantees, SLOs and degradation modes
  2. auto-generated configuration and capacity tables
  3. incident runbook covering every failure mode
  4. spec-versus-implementation drift detection

Expanded obligations:
  1. Implement specification of scheduling, guarantees, SLOs and degradation
     modes as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Terminal-Bench 2.1 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement auto-generated configuration and capacity tables, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Terminal-Bench 2.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement incident runbook covering every failure mode with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Terminal-Bench 2.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement spec-versus-implementation drift detection together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t08.engine.engine_spec_doc@1
  cap.t08.engine.engine_spec_doc.describe@1

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

  cap.t08.cost.cost_accounting_runtime@1
      if unavailable: use the in-file conservative substitute for
      `cost_accounting_runtime` (documented, slower, lower quality) and set
      `degraded['cost_accounting_runtime']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t02.topk.topk_sort@1
      if unavailable: use the in-file conservative substitute for
      `topk_sort` (documented, slower, lower quality) and set
      `degraded['topk_sort']='local'`

  cap.t03.pipeline.pipeline_planner@1
      if unavailable: use the in-file conservative substitute for
      `pipeline_planner` (documented, slower, lower quality) and set
      `degraded['pipeline_planner']='local'`

  cap.t04.device.device_health@1
      if unavailable: use the in-file conservative substitute for
      `device_health` (documented, slower, lower quality) and set
      `degraded['device_health']='local'`

  cap.t05.positional.positional_design@1
      if unavailable: use the in-file conservative substitute for
      `positional_design` (documented, slower, lower quality) and set
      `degraded['positional_design']='local'`

  cap.t06.expert.expert_diversity@1
      if unavailable: use the in-file conservative substitute for
      `expert_diversity` (documented, slower, lower quality) and set
      `degraded['expert_diversity']='local'`

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
   3. [ 600 lines] Core implementation A - specification of scheduling, guarantees, SLOs and degradation mo
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - auto-generated configuration and capacity tables
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - incident runbook covering every failure mode
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
     exactly (capability == cap.t08.engine.engine_spec_doc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t08_inference/P0400_engine_spec_doc.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
