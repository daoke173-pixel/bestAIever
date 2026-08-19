# HYPERION-Ω — Worker prompts · T20 · Platform, SDK, Ops & Distributed Assembly

> 50 prompts · one per part · language TypeScript 5.7 · Ω-CONTRACT v1.0.0-frozen

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

## PROMPT p0951-assembly-manifest

**P0951 · `assembly_manifest` — Assembly Manifest & 1000-Part Registry** · [spec](PART_SPECS_T20.md#p0951-assembly-manifest) · [self-contained txt](../prompts/P0951_assembly_manifest.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0951  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0951 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0951  (1/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Assembly Manifest & 1000-Part Registry
file         : parts/t20_platform/P0951_assembly_manifest.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.assembly_manifest
language     : TypeScript 5.7
capability   : cap.t20.assembly.assembly_manifest@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
The single index of all 1000 parts and their capabilities.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. manifest aggregation from all 1000 part files with validation
  2. capability index with provider/consumer cross-references
  3. completeness verification (all 1000 present, all requires satisfied)
  4. assembly-report artifact consumed by the build and deploy pipeline

Expanded obligations:
  1. Implement manifest aggregation from all 1000 part files with validation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement capability index with provider/consumer cross-references as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement completeness verification (all 1000 present, all requires
     satisfied), and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement assembly-report artifact consumed by the build and deploy
     pipeline with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against CursorBench 3.2 — a
     regression on that benchmark is an automatic rejection of this part.

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
  cap.t20.assembly.assembly_manifest@1
  cap.t20.assembly.assembly_manifest.describe@1

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

  cap.t08.stop.stop_conditions@1
      if unavailable: use the in-file conservative substitute for
      `stop_conditions` (documented, slower, lower quality) and set
      `degraded['stop_conditions']='local'`

  cap.t09.edge.edge_inference@1
      if unavailable: use the in-file conservative substitute for
      `edge_inference` (documented, slower, lower quality) and set
      `degraded['edge_inference']='local'`

  cap.t18.gdpval.gdpval_eval@1
      if unavailable: use the in-file conservative substitute for
      `gdpval_eval` (documented, slower, lower quality) and set
      `degraded['gdpval_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - manifest aggregation from all 1000 part files with validation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability index with provider/consumer cross-references
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - completeness verification (all 1000 present, all requires satisf
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - assembly-report artifact consumed by the build and deploy pipeli
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.assembly.assembly_manifest@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0951_assembly_manifest.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0952-assembly-linker

**P0952 · `assembly_linker` — Runtime Assembly & Capability Wiring** · [spec](PART_SPECS_T20.md#p0952-assembly-linker) · [self-contained txt](../prompts/P0952_assembly_linker.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0952  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0952 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0952  (2/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Runtime Assembly & Capability Wiring
file         : parts/t20_platform/P0952_assembly_linker.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.assembly_linker
language     : TypeScript 5.7
capability   : cap.t20.assembly.assembly_linker@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Fuses 1000 independently authored files into one working system.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dependency-ordered registration with parallel waves
  2. capability resolution with fallback ladders for missing parts
  3. partial-assembly operation (system works with parts missing, degraded)
  4. measured startup time and degradation behaviour per missing part

Expanded obligations:
  1. Implement dependency-ordered registration with parallel waves as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement capability resolution with fallback ladders for missing parts,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement partial-assembly operation (system works with parts missing,
     degraded) with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against CursorBench 3.2 — a
     regression on that benchmark is an automatic rejection of this part.
  4. Implement measured startup time and degradation behaviour per missing
     part together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Zapier
     AutomationBench target reachable; the part therefore ships a
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.assembly.assembly_linker@1
  cap.t20.assembly.assembly_linker.describe@1

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

  cap.t20.assembly.assembly_manifest@1
      if unavailable: use the in-file conservative substitute for
      `assembly_manifest` (documented, slower, lower quality) and set
      `degraded['assembly_manifest']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t08.adapter.adapter_serving@1
      if unavailable: use the in-file conservative substitute for
      `adapter_serving` (documented, slower, lower quality) and set
      `degraded['adapter_serving']='local'`

  cap.t09.lock.lock_free_paths@1
      if unavailable: use the in-file conservative substitute for
      `lock_free_paths` (documented, slower, lower quality) and set
      `degraded['lock_free_paths']='local'`

  cap.t18.robustness.robustness_eval@1
      if unavailable: use the in-file conservative substitute for
      `robustness_eval` (documented, slower, lower quality) and set
      `degraded['robustness_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - dependency-ordered registration with parallel waves
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability resolution with fallback ladders for missing parts
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partial-assembly operation (system works with parts missing, deg
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured startup time and degradation behaviour per missing part
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.assembly.assembly_linker@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0952_assembly_linker.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0953-assembly-validation

**P0953 · `assembly_validation` — Assembly Integration Validation** · [spec](PART_SPECS_T20.md#p0953-assembly-validation) · [self-contained txt](../prompts/P0953_assembly_validation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0953  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0953 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0953  (3/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Assembly Integration Validation
file         : parts/t20_platform/P0953_assembly_validation.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.assembly_validation
language     : TypeScript 5.7
capability   : cap.t20.assembly.assembly_validation@1
determinism  : io
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Proves the whole is coherent, not just the parts.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cross-part contract conformance verification at runtime
  2. integration smoke suite exercising every capability boundary
  3. version and schema compatibility verification across all parts
  4. validation report required before any deployment

Expanded obligations:
  1. Implement cross-part contract conformance verification at runtime, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement integration smoke suite exercising every capability boundary
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against CursorBench 3.2 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement version and schema compatibility verification across all parts
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement validation report required before any deployment as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.

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
  cap.t20.assembly.assembly_validation@1
  cap.t20.assembly.assembly_validation.describe@1

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

  cap.t20.assembly.assembly_linker@1
      if unavailable: use the in-file conservative substitute for
      `assembly_linker` (documented, slower, lower quality) and set
      `degraded['assembly_linker']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t08.engine.engine_telemetry@1
      if unavailable: use the in-file conservative substitute for
      `engine_telemetry` (documented, slower, lower quality) and set
      `degraded['engine_telemetry']='local'`

  cap.t09.flamegraph.flamegraph_tooling@1
      if unavailable: use the in-file conservative substitute for
      `flamegraph_tooling` (documented, slower, lower quality) and set
      `degraded['flamegraph_tooling']='local'`

  cap.t18.canary.canary_eval@1
      if unavailable: use the in-file conservative substitute for
      `canary_eval` (documented, slower, lower quality) and set
      `degraded['canary_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - cross-part contract conformance verification at runtime
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - integration smoke suite exercising every capability boundary
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - version and schema compatibility verification across all parts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - validation report required before any deployment
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.assembly.assembly_validation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0953_assembly_validation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0954-integration-test-matrix

**P0954 · `integration_test_matrix` — Cross-Part Integration Test Matrix** · [spec](PART_SPECS_T20.md#p0954-integration-test-matrix) · [self-contained txt](../prompts/P0954_integration_test_matrix.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0954  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0954 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0954  (4/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Cross-Part Integration Test Matrix
file         : parts/t20_platform/P0954_integration_test_matrix.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.integration_test_matrix
language     : TypeScript 5.7
capability   : cap.t20.integration.integration_test_matrix@1
determinism  : io
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Tests the interfaces, where independently written code actually breaks.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. pairwise and path-based integration test generation from the capability graph
  2. contract-violation detection with precise part attribution
  3. coverage measurement over all capability edges
  4. matrix execution within a bounded time budget

Expanded obligations:
  1. Implement pairwise and path-based integration test generation from the
     capability graph with an explicit *a-priori* cost model. Before doing
     the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Its contribution is measured
     against CursorBench 3.2 — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement contract-violation detection with precise part attribution
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement coverage measurement over all capability edges as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement matrix execution within a bounded time budget, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.

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
  cap.t20.integration.integration_test_matrix@1
  cap.t20.integration.integration_test_matrix.describe@1

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

  cap.t20.assembly.assembly_validation@1
      if unavailable: use the in-file conservative substitute for
      `assembly_validation` (documented, slower, lower quality) and set
      `degraded['assembly_validation']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t08.api.api_gateway_runtime@1
      if unavailable: use the in-file conservative substitute for
      `api_gateway_runtime` (documented, slower, lower quality) and set
      `degraded['api_gateway_runtime']='local'`

  cap.t09.speculation.speculation_budget@1
      if unavailable: use the in-file conservative substitute for
      `speculation_budget` (documented, slower, lower quality) and set
      `degraded['speculation_budget']='local'`

  cap.t18.dynamic.dynamic_benchmark@1
      if unavailable: use the in-file conservative substitute for
      `dynamic_benchmark` (documented, slower, lower quality) and set
      `degraded['dynamic_benchmark']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - pairwise and path-based integration test generation from the cap
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - contract-violation detection with precise part attribution
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - coverage measurement over all capability edges
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - matrix execution within a bounded time budget
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.integration.integration_test_matrix@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0954_integration_test_matrix.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0955-contract-conformance

**P0955 · `contract_conformance` — Ω-Contract Conformance Checker** · [spec](PART_SPECS_T20.md#p0955-contract-conformance) · [self-contained txt](../prompts/P0955_contract_conformance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0955  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0955 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0955  (5/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Ω-Contract Conformance Checker
file         : parts/t20_platform/P0955_contract_conformance.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.contract_conformance
language     : TypeScript 5.7
capability   : cap.t20.contract.contract_conformance@1
determinism  : io
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Machine-verifies all twelve contract clauses in every part.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-clause automated checking (manifest, symbols, errors, determinism, tests, shape)
  2. contract-digest verification detecting header drift
  3. conformance scorecard per part with remediation guidance
  4. gate blocking non-conformant parts from the assembly

Expanded obligations:
  1. Implement per-clause automated checking (manifest, symbols, errors,
     determinism, tests, shape) together with its verification path, so that
     anything this mechanism produces can be independently re-checked *inside
     this same file* without contacting any other part. The checker must be
     cheap enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Zapier
     AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement contract-digest verification detecting header drift as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement conformance scorecard per part with remediation guidance, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement gate blocking non-conformant parts from the assembly with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.contract.contract_conformance@1
  cap.t20.contract.contract_conformance.describe@1

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

  cap.t20.integration.integration_test_matrix@1
      if unavailable: use the in-file conservative substitute for
      `integration_test_matrix` (documented, slower, lower quality) and set
      `degraded['integration_test_matrix']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t08.cost.cost_accounting_runtime@1
      if unavailable: use the in-file conservative substitute for
      `cost_accounting_runtime` (documented, slower, lower quality) and set
      `degraded['cost_accounting_runtime']='local'`

  cap.t09.speed.speed_proof_report@1
      if unavailable: use the in-file conservative substitute for
      `speed_proof_report` (documented, slower, lower quality) and set
      `degraded['speed_proof_report']='local'`

  cap.t18.eval.eval_task_provenance@1
      if unavailable: use the in-file conservative substitute for
      `eval_task_provenance` (documented, slower, lower quality) and set
      `degraded['eval_task_provenance']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - per-clause automated checking (manifest, symbols, errors, determ
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - contract-digest verification detecting header drift
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conformance scorecard per part with remediation guidance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - gate blocking non-conformant parts from the assembly
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.contract.contract_conformance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0955_contract_conformance.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0956-public-api

**P0956 · `public_api` — Public API Surface Definition** · [spec](PART_SPECS_T20.md#p0956-public-api) · [self-contained txt](../prompts/P0956_public_api.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0956  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0956 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0956  (6/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Public API Surface Definition
file         : parts/t20_platform/P0956_public_api.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.public_api
language     : TypeScript 5.7
capability   : cap.t20.public.public_api@1
determinism  : io
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
The interface the world uses.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. endpoint, message and error specification with versioning policy
  2. compatibility guarantees and deprecation timeline rules
  3. OpenAPI-class machine-readable specification generation
  4. API-conformance test suite

Expanded obligations:
  1. Implement endpoint, message and error specification with versioning
     policy as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement compatibility guarantees and deprecation timeline rules, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement OpenAPI-class machine-readable specification generation with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement API-conformance test suite together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. This mechanism sits on the critical
     path of Zapier AutomationBench, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.

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
  cap.t20.public.public_api@1
  cap.t20.public.public_api.describe@1

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

  cap.t20.contract.contract_conformance@1
      if unavailable: use the in-file conservative substitute for
      `contract_conformance` (documented, slower, lower quality) and set
      `degraded['contract_conformance']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t08.cascade.cascade_stage1_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage1_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage1_draft']='local'`

  cap.t09.template.template_cache@1
      if unavailable: use the in-file conservative substitute for
      `template_cache` (documented, slower, lower quality) and set
      `degraded['template_cache']='local'`

  cap.t18.elo.elo_arena@1
      if unavailable: use the in-file conservative substitute for
      `elo_arena` (documented, slower, lower quality) and set
      `degraded['elo_arena']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - endpoint, message and error specification with versioning policy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - compatibility guarantees and deprecation timeline rules
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - OpenAPI-class machine-readable specification generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - API-conformance test suite
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.public.public_api@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0956_public_api.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0957-sdk-typescript

**P0957 · `sdk_typescript` — TypeScript / JavaScript SDK** · [spec](PART_SPECS_T20.md#p0957-sdk-typescript) · [self-contained txt](../prompts/P0957_sdk_typescript.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0957  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0957 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0957  (7/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : TypeScript / JavaScript SDK
file         : parts/t20_platform/P0957_sdk_typescript.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.sdk_typescript
language     : TypeScript 5.7
capability   : cap.t20.sdk.sdk_typescript@1
determinism  : io
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
First-class client library for the largest developer ecosystem.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. typed client with streaming, tools, retries and cancellation
  2. runtime-agnostic implementation (Node, browser, edge, Deno, Bun)
  3. zero-dependency implementation with tree-shakeable modules
  4. example suite and API-conformance verification

Expanded obligations:
  1. Implement typed client with streaming, tools, retries and cancellation,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement runtime-agnostic implementation (Node, browser, edge, Deno,
     Bun) with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's CursorBench 3.2
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement zero-dependency implementation with tree-shakeable modules
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement example suite and API-conformance verification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.sdk.sdk_typescript@1
  cap.t20.sdk.sdk_typescript.describe@1

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

  cap.t20.public.public_api@1
      if unavailable: use the in-file conservative substitute for
      `public_api` (documented, slower, lower quality) and set
      `degraded['public_api']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t08.cascade.cascade_rollback@1
      if unavailable: use the in-file conservative substitute for
      `cascade_rollback` (documented, slower, lower quality) and set
      `degraded['cascade_rollback']='local'`

  cap.t09.dag.dag_critical_path@1
      if unavailable: use the in-file conservative substitute for
      `dag_critical_path` (documented, slower, lower quality) and set
      `degraded['dag_critical_path']='local'`

  cap.t18.terminal.terminal_bench_eval@1
      if unavailable: use the in-file conservative substitute for
      `terminal_bench_eval` (documented, slower, lower quality) and set
      `degraded['terminal_bench_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - typed client with streaming, tools, retries and cancellation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - runtime-agnostic implementation (Node, browser, edge, Deno, Bun)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - zero-dependency implementation with tree-shakeable modules
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - example suite and API-conformance verification
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.sdk.sdk_typescript@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0957_sdk_typescript.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0958-sdk-python

**P0958 · `sdk_python` — Python SDK** · [spec](PART_SPECS_T20.md#p0958-sdk-python) · [self-contained txt](../prompts/P0958_sdk_python.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0958  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0958 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0958  (8/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Python SDK
file         : parts/t20_platform/P0958_sdk_python.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.sdk_python
language     : TypeScript 5.7
capability   : cap.t20.sdk.sdk_python@1
determinism  : io
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
First-class client library for the AI and data ecosystem.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. sync and async clients with identical semantics
  2. streaming, tool-loop and structured-output helpers
  3. typed interfaces with strict type-checker compatibility
  4. example suite and API-conformance verification

Expanded obligations:
  1. Implement sync and async clients with identical semantics with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement streaming, tool-loop and structured-output helpers together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement typed interfaces with strict type-checker compatibility as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement example suite and API-conformance verification, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Zapier AutomationBench target
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
  cap.t20.sdk.sdk_python@1
  cap.t20.sdk.sdk_python.describe@1

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

  cap.t20.sdk.sdk_typescript@1
      if unavailable: use the in-file conservative substitute for
      `sdk_typescript` (documented, slower, lower quality) and set
      `degraded['sdk_typescript']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t08.logit.logit_processor@1
      if unavailable: use the in-file conservative substitute for
      `logit_processor` (documented, slower, lower quality) and set
      `degraded['logit_processor']='local'`

  cap.t09.network.network_latency@1
      if unavailable: use the in-file conservative substitute for
      `network_latency` (documented, slower, lower quality) and set
      `degraded['network_latency']='local'`

  cap.t18.automation.automation_bench_eval@1
      if unavailable: use the in-file conservative substitute for
      `automation_bench_eval` (documented, slower, lower quality) and set
      `degraded['automation_bench_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - sync and async clients with identical semantics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - streaming, tool-loop and structured-output helpers
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - typed interfaces with strict type-checker compatibility
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - example suite and API-conformance verification
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.sdk.sdk_python@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0958_sdk_python.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0959-sdk-other-languages

**P0959 · `sdk_other_languages` — Additional Language SDKs** · [spec](PART_SPECS_T20.md#p0959-sdk-other-languages) · [self-contained txt](../prompts/P0959_sdk_other_languages.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0959  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0959 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0959  (9/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Additional Language SDKs
file         : parts/t20_platform/P0959_sdk_other_languages.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.sdk_other_languages
language     : TypeScript 5.7
capability   : cap.t20.sdk.sdk_other_languages@1
determinism  : io
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Go, Rust, Java, C# and mobile clients from one specification.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. specification-driven client generation with idiomatic hand-tuning
  2. cross-SDK behavioural equivalence testing
  3. language-specific concurrency and error idioms
  4. conformance verification across all SDKs

Expanded obligations:
  1. Implement specification-driven client generation with idiomatic
     hand-tuning together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of Zapier
     AutomationBench, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement cross-SDK behavioural equivalence testing as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against CursorBench 3.2
     — a regression on that benchmark is an automatic rejection of this part.
  3. Implement language-specific concurrency and error idioms, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement conformance verification across all SDKs with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of CursorBench 3.2, so its p99 latency
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
  cap.t20.sdk.sdk_other_languages@1
  cap.t20.sdk.sdk_other_languages.describe@1

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

  cap.t20.sdk.sdk_python@1
      if unavailable: use the in-file conservative substitute for
      `sdk_python` (documented, slower, lower quality) and set
      `degraded['sdk_python']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t08.multi.multi_model_serving@1
      if unavailable: use the in-file conservative substitute for
      `multi_model_serving` (documented, slower, lower quality) and set
      `degraded['multi_model_serving']='local'`

  cap.t09.hot.hot_cold_split@1
      if unavailable: use the in-file conservative substitute for
      `hot_cold_split` (documented, slower, lower quality) and set
      `degraded['hot_cold_split']='local'`

  cap.t18.calibration.calibration_eval@1
      if unavailable: use the in-file conservative substitute for
      `calibration_eval` (documented, slower, lower quality) and set
      `degraded['calibration_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - specification-driven client generation with idiomatic hand-tunin
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-SDK behavioural equivalence testing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - language-specific concurrency and error idioms
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - conformance verification across all SDKs
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.sdk.sdk_other_languages@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0959_sdk_other_languages.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0960-cli-tool

**P0960 · `cli_tool` — Command Line Interface & Developer Tooling** · [spec](PART_SPECS_T20.md#p0960-cli-tool) · [self-contained txt](../prompts/P0960_cli_tool.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0960  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0960 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0960  (10/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Command Line Interface & Developer Tooling
file         : parts/t20_platform/P0960_cli_tool.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.cli_tool
language     : TypeScript 5.7
capability   : cap.t20.cli.cli_tool@1
determinism  : io
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
The terminal-native way to use and operate the system.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. interactive and scriptable modes with structured output options
  2. session, project and configuration management
  3. shell completion, help quality and error-message clarity
  4. usability validation with real developer workflows

Expanded obligations:
  1. Implement interactive and scriptable modes with structured output
     options as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement session, project and configuration management, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement shell completion, help quality and error-message clarity with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement usability validation with real developer workflows together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.cli.cli_tool@1
  cap.t20.cli.cli_tool.describe@1

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

  cap.t20.sdk.sdk_other_languages@1
      if unavailable: use the in-file conservative substitute for
      `sdk_other_languages` (documented, slower, lower quality) and set
      `degraded['sdk_other_languages']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t08.output.output_verification_loop@1
      if unavailable: use the in-file conservative substitute for
      `output_verification_loop` (documented, slower, lower quality) and set
      `degraded['output_verification_loop']='local'`

  cap.t09.perf.perf_ci@1
      if unavailable: use the in-file conservative substitute for `perf_ci`
      (documented, slower, lower quality) and set
      `degraded['perf_ci']='local'`

  cap.t18.regression.regression_suite@1
      if unavailable: use the in-file conservative substitute for
      `regression_suite` (documented, slower, lower quality) and set
      `degraded['regression_suite']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - interactive and scriptable modes with structured output options
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - session, project and configuration management
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - shell completion, help quality and error-message clarity
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - usability validation with real developer workflows
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.cli.cli_tool@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0960_cli_tool.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0961-ide-integration

**P0961 · `ide_integration` — IDE & Editor Integration** · [spec](PART_SPECS_T20.md#p0961-ide-integration) · [self-contained txt](../prompts/P0961_ide_integration.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0961  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0961 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0961  (11/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : IDE & Editor Integration
file         : parts/t20_platform/P0961_ide_integration.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.ide_integration
language     : TypeScript 5.7
capability   : cap.t20.ide.ide_integration@1
determinism  : io
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Where developers actually work.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. language-server-protocol integration with incremental context
  2. inline suggestion, chat and agent-task interfaces
  3. workspace-context management with privacy controls
  4. latency budget for interactive editor operations

Expanded obligations:
  1. Implement language-server-protocol integration with incremental context,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement inline suggestion, chat and agent-task interfaces with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement workspace-context management with privacy controls together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement latency budget for interactive editor operations as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.ide.ide_integration@1
  cap.t20.ide.ide_integration.describe@1

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

  cap.t20.cli.cli_tool@1
      if unavailable: use the in-file conservative substitute for `cli_tool`
      (documented, slower, lower quality) and set
      `degraded['cli_tool']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t08.engine.engine_fault_tolerance@1
      if unavailable: use the in-file conservative substitute for
      `engine_fault_tolerance` (documented, slower, lower quality) and set
      `degraded['engine_fault_tolerance']='local'`

  cap.t09.cache.cache_sizing@1
      if unavailable: use the in-file conservative substitute for
      `cache_sizing` (documented, slower, lower quality) and set
      `degraded['cache_sizing']='local'`

  cap.t18.benchmark.benchmark_construction@1
      if unavailable: use the in-file conservative substitute for
      `benchmark_construction` (documented, slower, lower quality) and set
      `degraded['benchmark_construction']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - language-server-protocol integration with incremental context
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - inline suggestion, chat and agent-task interfaces
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - workspace-context management with privacy controls
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency budget for interactive editor operations
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.ide.ide_integration@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0961_ide_integration.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0962-mcp-interop

**P0962 · `mcp_interop` — Tool Protocol Interoperability** · [spec](PART_SPECS_T20.md#p0962-mcp-interop) · [self-contained txt](../prompts/P0962_mcp_interop.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0962  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0962 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0962  (12/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Tool Protocol Interoperability
file         : parts/t20_platform/P0962_mcp_interop.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.mcp_interop
language     : TypeScript 5.7
capability   : cap.t20.mcp.mcp_interop@1
determinism  : io
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Speaks the ecosystem's tool protocols natively.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. standard tool-protocol server and client implementation
  2. capability negotiation and version compatibility handling
  3. security review of protocol-mediated tool access
  4. interoperability testing against reference implementations

Expanded obligations:
  1. Implement standard tool-protocol server and client implementation with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement capability negotiation and version compatibility handling
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement security review of protocol-mediated tool access as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement interoperability testing against reference implementations,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.mcp.mcp_interop@1
  cap.t20.mcp.mcp_interop.describe@1

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

  cap.t20.ide.ide_integration@1
      if unavailable: use the in-file conservative substitute for
      `ide_integration` (documented, slower, lower quality) and set
      `degraded['ide_integration']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t08.engine.engine_security@1
      if unavailable: use the in-file conservative substitute for
      `engine_security` (documented, slower, lower quality) and set
      `degraded['engine_security']='local'`

  cap.t09.latency.latency_dashboard@1
      if unavailable: use the in-file conservative substitute for
      `latency_dashboard` (documented, slower, lower quality) and set
      `degraded['latency_dashboard']='local'`

  cap.t18.eval.eval_release_report@1
      if unavailable: use the in-file conservative substitute for
      `eval_release_report` (documented, slower, lower quality) and set
      `degraded['eval_release_report']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - standard tool-protocol server and client implementation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability negotiation and version compatibility handling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - security review of protocol-mediated tool access
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - interoperability testing against reference implementations
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.mcp.mcp_interop@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0962_mcp_interop.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0963-webhook-events

**P0963 · `webhook_events` — Webhooks, Events & Async Delivery** · [spec](PART_SPECS_T20.md#p0963-webhook-events) · [self-contained txt](../prompts/P0963_webhook_events.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0963  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0963 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0963  (13/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Webhooks, Events & Async Delivery
file         : parts/t20_platform/P0963_webhook_events.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.webhook_events
language     : TypeScript 5.7
capability   : cap.t20.webhook.webhook_events@1
determinism  : io
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Reliable notification for long-running work.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. event schema, signing and replay-protection
  2. at-least-once delivery with idempotency guidance and retry policy
  3. subscription management and filtering
  4. delivery-reliability measurement

Expanded obligations:
  1. Implement event schema, signing and replay-protection together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement at-least-once delivery with idempotency guidance and retry
     policy as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement subscription management and filtering, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement delivery-reliability measurement with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Its contribution is
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.webhook.webhook_events@1
  cap.t20.webhook.webhook_events.describe@1

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

  cap.t20.mcp.mcp_interop@1
      if unavailable: use the in-file conservative substitute for
      `mcp_interop` (documented, slower, lower quality) and set
      `degraded['mcp_interop']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t08.admission.admission_control@1
      if unavailable: use the in-file conservative substitute for
      `admission_control` (documented, slower, lower quality) and set
      `degraded['admission_control']='local'`

  cap.t09.similarity.similarity_cache@1
      if unavailable: use the in-file conservative substitute for
      `similarity_cache` (documented, slower, lower quality) and set
      `degraded['similarity_cache']='local'`

  cap.t18.expert.expert_eval@1
      if unavailable: use the in-file conservative substitute for
      `expert_eval` (documented, slower, lower quality) and set
      `degraded['expert_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - event schema, signing and replay-protection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - at-least-once delivery with idempotency guidance and retry polic
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - subscription management and filtering
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - delivery-reliability measurement
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.webhook.webhook_events@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0963_webhook_events.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0964-batch-api

**P0964 · `batch_api` — Batch & Asynchronous Job API** · [spec](PART_SPECS_T20.md#p0964-batch-api) · [self-contained txt](../prompts/P0964_batch_api.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0964  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0964 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0964  (14/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Batch & Asynchronous Job API
file         : parts/t20_platform/P0964_batch_api.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.batch_api
language     : TypeScript 5.7
capability   : cap.t20.batch.batch_api@1
determinism  : io
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Cheap, high-throughput processing for non-interactive work.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. job submission, status, cancellation and result retrieval
  2. cost-reduced scheduling into spare capacity
  3. partial-result and per-item error reporting
  4. throughput and cost-saving measurement versus synchronous serving

Expanded obligations:
  1. Implement job submission, status, cancellation and result retrieval as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement cost-reduced scheduling into spare capacity, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement partial-result and per-item error reporting with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement throughput and cost-saving measurement versus synchronous
     serving together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Zapier
     AutomationBench target reachable; the part therefore ships a
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.batch.batch_api@1
  cap.t20.batch.batch_api.describe@1

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

  cap.t20.webhook.webhook_events@1
      if unavailable: use the in-file conservative substitute for
      `webhook_events` (documented, slower, lower quality) and set
      `degraded['webhook_events']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t08.cascade.cascade_batching@1
      if unavailable: use the in-file conservative substitute for
      `cascade_batching` (documented, slower, lower quality) and set
      `degraded['cascade_batching']='local'`

  cap.t09.parallel.parallel_horizon@1
      if unavailable: use the in-file conservative substitute for
      `parallel_horizon` (documented, slower, lower quality) and set
      `degraded['parallel_horizon']='local'`

  cap.t18.frontier.frontier_bench_eval@1
      if unavailable: use the in-file conservative substitute for
      `frontier_bench_eval` (documented, slower, lower quality) and set
      `degraded['frontier_bench_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - job submission, status, cancellation and result retrieval
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost-reduced scheduling into spare capacity
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partial-result and per-item error reporting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput and cost-saving measurement versus synchronous servin
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.batch.batch_api@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0964_batch_api.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0965-auth-identity

**P0965 · `auth_identity` — Authentication, Authorisation & Identity** · [spec](PART_SPECS_T20.md#p0965-auth-identity) · [self-contained txt](../prompts/P0965_auth_identity.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0965  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0965 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0965  (15/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Authentication, Authorisation & Identity
file         : parts/t20_platform/P0965_auth_identity.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.auth_identity
language     : TypeScript 5.7
capability   : cap.t20.auth.auth_identity@1
determinism  : io
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Correct access control at the platform edge.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. key, token and federated-identity authentication with rotation
  2. fine-grained authorisation with least-privilege defaults
  3. organisation, project and user scope hierarchy
  4. authorisation-bypass testing and verification

Expanded obligations:
  1. Implement key, token and federated-identity authentication with
     rotation, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement fine-grained authorisation with least-privilege defaults with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against CursorBench 3.2 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement organisation, project and user scope hierarchy together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Zapier AutomationBench target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement authorisation-bypass testing and verification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.

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
  cap.t20.auth.auth_identity@1
  cap.t20.auth.auth_identity.describe@1

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

  cap.t20.batch.batch_api@1
      if unavailable: use the in-file conservative substitute for
      `batch_api` (documented, slower, lower quality) and set
      `degraded['batch_api']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t08.constrained.constrained_decoding@1
      if unavailable: use the in-file conservative substitute for
      `constrained_decoding` (documented, slower, lower quality) and set
      `degraded['constrained_decoding']='local'`

  cap.t09.syscall.syscall_reduction@1
      if unavailable: use the in-file conservative substitute for
      `syscall_reduction` (documented, slower, lower quality) and set
      `degraded['syscall_reduction']='local'`

  cap.t18.browsecomp.browsecomp_eval@1
      if unavailable: use the in-file conservative substitute for
      `browsecomp_eval` (documented, slower, lower quality) and set
      `degraded['browsecomp_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - key, token and federated-identity authentication with rotation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fine-grained authorisation with least-privilege defaults
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - organisation, project and user scope hierarchy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - authorisation-bypass testing and verification
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.auth.auth_identity@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0965_auth_identity.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0966-tenancy-isolation

**P0966 · `tenancy_isolation` — Multi-Tenant Isolation Guarantees** · [spec](PART_SPECS_T20.md#p0966-tenancy-isolation) · [self-contained txt](../prompts/P0966_tenancy_isolation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0966  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0966 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0966  (16/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Multi-Tenant Isolation Guarantees
file         : parts/t20_platform/P0966_tenancy_isolation.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.tenancy_isolation
language     : TypeScript 5.7
capability   : cap.t20.tenancy.tenancy_isolation@1
determinism  : io
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
One customer can never affect or observe another.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. data, cache, memory and compute isolation enforcement
  2. cross-tenant leakage testing across every shared structure
  3. per-tenant quota and fairness enforcement
  4. isolation-verification report with adversarial test results

Expanded obligations:
  1. Implement data, cache, memory and compute isolation enforcement with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement cross-tenant leakage testing across every shared structure
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement per-tenant quota and fairness enforcement as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement isolation-verification report with adversarial test results,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
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
  cap.t20.tenancy.tenancy_isolation@1
  cap.t20.tenancy.tenancy_isolation.describe@1

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

  cap.t20.auth.auth_identity@1
      if unavailable: use the in-file conservative substitute for
      `auth_identity` (documented, slower, lower quality) and set
      `degraded['auth_identity']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t08.weight.weight_hotswap@1
      if unavailable: use the in-file conservative substitute for
      `weight_hotswap` (documented, slower, lower quality) and set
      `degraded['weight_hotswap']='local'`

  cap.t09.cache.cache_coherence@1
      if unavailable: use the in-file conservative substitute for
      `cache_coherence` (documented, slower, lower quality) and set
      `degraded['cache_coherence']='local'`

  cap.t18.hallucination.hallucination_eval@1
      if unavailable: use the in-file conservative substitute for
      `hallucination_eval` (documented, slower, lower quality) and set
      `degraded['hallucination_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - data, cache, memory and compute isolation enforcement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-tenant leakage testing across every shared structure
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-tenant quota and fairness enforcement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - isolation-verification report with adversarial test results
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.tenancy.tenancy_isolation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0966_tenancy_isolation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0967-quota-billing

**P0967 · `quota_billing` — Quotas, Metering & Billing** · [spec](PART_SPECS_T20.md#p0967-quota-billing) · [self-contained txt](../prompts/P0967_quota_billing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0967  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0967 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0967  (17/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Quotas, Metering & Billing
file         : parts/t20_platform/P0967_quota_billing.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.quota_billing
language     : TypeScript 5.7
capability   : cap.t20.quota.quota_billing@1
determinism  : io
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Accurate, transparent, disputable-free usage accounting.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. usage metering with billing-grade accuracy verification
  2. quota enforcement with clear limit signalling
  3. cost attribution by project, feature and request
  4. reconciliation testing against independent accounting

Expanded obligations:
  1. Implement usage metering with billing-grade accuracy verification
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement quota enforcement with clear limit signalling as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement cost attribution by project, feature and request, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement reconciliation testing against independent accounting with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.quota.quota_billing@1
  cap.t20.quota.quota_billing.describe@1

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

  cap.t20.tenancy.tenancy_isolation@1
      if unavailable: use the in-file conservative substitute for
      `tenancy_isolation` (documented, slower, lower quality) and set
      `degraded['tenancy_isolation']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t08.parallel.parallel_generation@1
      if unavailable: use the in-file conservative substitute for
      `parallel_generation` (documented, slower, lower quality) and set
      `degraded['parallel_generation']='local'`

  cap.t09.latency.latency_regression_gate@1
      if unavailable: use the in-file conservative substitute for
      `latency_regression_gate` (documented, slower, lower quality) and set
      `degraded['latency_regression_gate']='local'`

  cap.t18.speed.speed_eval@1
      if unavailable: use the in-file conservative substitute for
      `speed_eval` (documented, slower, lower quality) and set
      `degraded['speed_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - usage metering with billing-grade accuracy verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quota enforcement with clear limit signalling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cost attribution by project, feature and request
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - reconciliation testing against independent accounting
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.quota.quota_billing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0967_quota_billing.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0968-pricing-engine

**P0968 · `pricing_engine` — Pricing Model & Cost Transparency** · [spec](PART_SPECS_T20.md#p0968-pricing-engine) · [self-contained txt](../prompts/P0968_pricing_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0968  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0968 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0968  (18/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Pricing Model & Cost Transparency
file         : parts/t20_platform/P0968_pricing_engine.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.pricing_engine
language     : TypeScript 5.7
capability   : cap.t20.pricing.pricing_engine@1
determinism  : io
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Users always know what something will cost before running it.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. pre-execution cost estimation with accuracy bounds
  2. pricing-model implementation with cache and batch discounts
  3. cost-optimisation recommendations for users
  4. estimate-versus-actual accuracy measurement

Expanded obligations:
  1. Implement pre-execution cost estimation with accuracy bounds as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement pricing-model implementation with cache and batch discounts,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement cost-optimisation recommendations for users with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's CursorBench 3.2 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement estimate-versus-actual accuracy measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.pricing.pricing_engine@1
  cap.t20.pricing.pricing_engine.describe@1

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

  cap.t20.quota.quota_billing@1
      if unavailable: use the in-file conservative substitute for
      `quota_billing` (documented, slower, lower quality) and set
      `degraded['quota_billing']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t08.quantised.quantised_serving@1
      if unavailable: use the in-file conservative substitute for
      `quantised_serving` (documented, slower, lower quality) and set
      `degraded['quantised_serving']='local'`

  cap.t09.capacity.capacity_planner@1
      if unavailable: use the in-file conservative substitute for
      `capacity_planner` (documented, slower, lower quality) and set
      `degraded['capacity_planner']='local'`

  cap.t18.eval.eval_infrastructure@1
      if unavailable: use the in-file conservative substitute for
      `eval_infrastructure` (documented, slower, lower quality) and set
      `degraded['eval_infrastructure']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - pre-execution cost estimation with accuracy bounds
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - pricing-model implementation with cache and batch discounts
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cost-optimisation recommendations for users
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - estimate-versus-actual accuracy measurement
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.pricing.pricing_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0968_pricing_engine.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0969-rate-limits-public

**P0969 · `rate_limits_public` — Public Rate Limiting & Fair Use** · [spec](PART_SPECS_T20.md#p0969-rate-limits-public) · [self-contained txt](../prompts/P0969_rate_limits_public.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0969  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0969 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0969  (19/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Public Rate Limiting & Fair Use
file         : parts/t20_platform/P0969_rate_limits_public.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.rate_limits_public
language     : TypeScript 5.7
capability   : cap.t20.rate.rate_limits_public@1
determinism  : io
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Protects the system while treating customers fairly.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tiered rate limits with burst allowance and clear headers
  2. graceful limit responses with retry guidance
  3. abuse detection distinguished from legitimate high usage
  4. fairness measurement across customer sizes

Expanded obligations:
  1. Implement tiered rate limits with burst allowance and clear headers, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement graceful limit responses with retry guidance with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's CursorBench 3.2 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement abuse detection distinguished from legitimate high usage
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement fairness measurement across customer sizes as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against CursorBench 3.2
     — a regression on that benchmark is an automatic rejection of this part.

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
  cap.t20.rate.rate_limits_public@1
  cap.t20.rate.rate_limits_public.describe@1

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

  cap.t20.pricing.pricing_engine@1
      if unavailable: use the in-file conservative substitute for
      `pricing_engine` (documented, slower, lower quality) and set
      `degraded['pricing_engine']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t08.prompt.prompt_compilation@1
      if unavailable: use the in-file conservative substitute for
      `prompt_compilation` (documented, slower, lower quality) and set
      `degraded['prompt_compilation']='local'`

  cap.t09.degradation.degradation_ladder@1
      if unavailable: use the in-file conservative substitute for
      `degradation_ladder` (documented, slower, lower quality) and set
      `degraded['degradation_ladder']='local'`

  cap.t18.safety.safety_eval_bridge@1
      if unavailable: use the in-file conservative substitute for
      `safety_eval_bridge` (documented, slower, lower quality) and set
      `degraded['safety_eval_bridge']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - tiered rate limits with burst allowance and clear headers
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - graceful limit responses with retry guidance
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - abuse detection distinguished from legitimate high usage
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fairness measurement across customer sizes
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.rate.rate_limits_public@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0969_rate_limits_public.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0970-deployment-pipeline

**P0970 · `deployment_pipeline` — Build, Test & Deployment Pipeline** · [spec](PART_SPECS_T20.md#p0970-deployment-pipeline) · [self-contained txt](../prompts/P0970_deployment_pipeline.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0970  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0970 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0970  (20/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Build, Test & Deployment Pipeline
file         : parts/t20_platform/P0970_deployment_pipeline.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.deployment_pipeline
language     : TypeScript 5.7
capability   : cap.t20.deployment.deployment_pipeline@1
determinism  : io
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
1000 parts to production, safely, repeatedly.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hermetic reproducible build of the full assembly
  2. staged pipeline with automated gates at every stage
  3. artifact signing, provenance and promotion workflow
  4. measured deployment frequency and change-failure rate

Expanded obligations:
  1. Implement hermetic reproducible build of the full assembly with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement staged pipeline with automated gates at every stage together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement artifact signing, provenance and promotion workflow as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured deployment frequency and change-failure rate, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.deployment.deployment_pipeline@1
  cap.t20.deployment.deployment_pipeline.describe@1

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

  cap.t20.rate.rate_limits_public@1
      if unavailable: use the in-file conservative substitute for
      `rate_limits_public` (documented, slower, lower quality) and set
      `degraded['rate_limits_public']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t08.prefill.prefill_decode_split@1
      if unavailable: use the in-file conservative substitute for
      `prefill_decode_split` (documented, slower, lower quality) and set
      `degraded['prefill_decode_split']='local'`

  cap.t09.exact.exact_cache@1
      if unavailable: use the in-file conservative substitute for
      `exact_cache` (documented, slower, lower quality) and set
      `degraded['exact_cache']='local'`

  cap.t18.human.human_eval_protocol@1
      if unavailable: use the in-file conservative substitute for
      `human_eval_protocol` (documented, slower, lower quality) and set
      `degraded['human_eval_protocol']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - hermetic reproducible build of the full assembly
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - staged pipeline with automated gates at every stage
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - artifact signing, provenance and promotion workflow
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured deployment frequency and change-failure rate
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.deployment.deployment_pipeline@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0970_deployment_pipeline.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0971-release-management

**P0971 · `release_management` — Release Management & Versioning** · [spec](PART_SPECS_T20.md#p0971-release-management) · [self-contained txt](../prompts/P0971_release_management.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0971  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0971 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0971  (21/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Release Management & Versioning
file         : parts/t20_platform/P0971_release_management.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.release_management
language     : TypeScript 5.7
capability   : cap.t20.release.release_management@1
determinism  : io
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Every release identified, documented and reversible.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. semantic versioning policy for the assembly and its API
  2. release-note generation from part-level change data
  3. rollback procedure with verified data compatibility
  4. measured rollback success rate in drills

Expanded obligations:
  1. Implement semantic versioning policy for the assembly and its API
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement release-note generation from part-level change data as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement rollback procedure with verified data compatibility, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured rollback success rate in drills with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of CursorBench 3.2, so its p99 latency
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
  cap.t20.release.release_management@1
  cap.t20.release.release_management.describe@1

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

  cap.t20.deployment.deployment_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `deployment_pipeline` (documented, slower, lower quality) and set
      `degraded['deployment_pipeline']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t08.cascade.cascade_scheduler@1
      if unavailable: use the in-file conservative substitute for
      `cascade_scheduler` (documented, slower, lower quality) and set
      `degraded['cascade_scheduler']='local'`

  cap.t09.prefetch.prefetch_predictor@1
      if unavailable: use the in-file conservative substitute for
      `prefetch_predictor` (documented, slower, lower quality) and set
      `degraded['prefetch_predictor']='local'`

  cap.t18.swe.swe_pro_eval@1
      if unavailable: use the in-file conservative substitute for
      `swe_pro_eval` (documented, slower, lower quality) and set
      `degraded['swe_pro_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - semantic versioning policy for the assembly and its API
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - release-note generation from part-level change data
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - rollback procedure with verified data compatibility
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured rollback success rate in drills
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.release.release_management@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0971_release_management.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0972-canary-deployment

**P0972 · `canary_deployment` — Canary & Progressive Delivery** · [spec](PART_SPECS_T20.md#p0972-canary-deployment) · [self-contained txt](../prompts/P0972_canary_deployment.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0972  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0972 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0972  (22/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Canary & Progressive Delivery
file         : parts/t20_platform/P0972_canary_deployment.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.canary_deployment
language     : TypeScript 5.7
capability   : cap.t20.canary.canary_deployment@1
determinism  : io
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Every change proves itself on a small slice first.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. traffic-splitting with cohort selection and guardrail metrics
  2. automatic promotion and rollback decision logic
  3. blast-radius limitation per stage
  4. measured incident prevention from canary detection

Expanded obligations:
  1. Implement traffic-splitting with cohort selection and guardrail metrics
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement automatic promotion and rollback decision logic, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement blast-radius limitation per stage with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of CursorBench 3.2, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured incident prevention from canary detection together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.canary.canary_deployment@1
  cap.t20.canary.canary_deployment.describe@1

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

  cap.t20.release.release_management@1
      if unavailable: use the in-file conservative substitute for
      `release_management` (documented, slower, lower quality) and set
      `degraded['release_management']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t08.sampler.sampler_engine@1
      if unavailable: use the in-file conservative substitute for
      `sampler_engine` (documented, slower, lower quality) and set
      `degraded['sampler_engine']='local'`

  cap.t09.gc.gc_pause_control@1
      if unavailable: use the in-file conservative substitute for
      `gc_pause_control` (documented, slower, lower quality) and set
      `degraded['gc_pause_control']='local'`

  cap.t18.osworld.osworld_eval@1
      if unavailable: use the in-file conservative substitute for
      `osworld_eval` (documented, slower, lower quality) and set
      `degraded['osworld_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - traffic-splitting with cohort selection and guardrail metrics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automatic promotion and rollback decision logic
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blast-radius limitation per stage
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured incident prevention from canary detection
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.canary.canary_deployment@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0972_canary_deployment.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0973-feature-flags-platform

**P0973 · `feature_flags_platform` — Feature Flag & Experiment Platform** · [spec](PART_SPECS_T20.md#p0973-feature-flags-platform) · [self-contained txt](../prompts/P0973_feature_flags_platform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0973  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0973 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0973  (23/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Feature Flag & Experiment Platform
file         : parts/t20_platform/P0973_feature_flags_platform.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.feature_flags_platform
language     : TypeScript 5.7
capability   : cap.t20.feature.feature_flags_platform@1
determinism  : io
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Ship code continuously, enable behaviour deliberately.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. flag lifecycle with owner, expiry and kill-switch requirements
  2. experiment assignment with correct randomisation and analysis
  3. flag-state consistency across a distributed fleet
  4. flag-debt monitoring and cleanup enforcement

Expanded obligations:
  1. Implement flag lifecycle with owner, expiry and kill-switch
     requirements, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement experiment assignment with correct randomisation and analysis
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement flag-state consistency across a distributed fleet together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement flag-debt monitoring and cleanup enforcement as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's CursorBench
     3.2 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.

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
  cap.t20.feature.feature_flags_platform@1
  cap.t20.feature.feature_flags_platform.describe@1

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

  cap.t20.canary.canary_deployment@1
      if unavailable: use the in-file conservative substitute for
      `canary_deployment` (documented, slower, lower quality) and set
      `degraded['canary_deployment']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t08.model.model_loading@1
      if unavailable: use the in-file conservative substitute for
      `model_loading` (documented, slower, lower quality) and set
      `degraded['model_loading']='local'`

  cap.t09.speculative.speculative_ui@1
      if unavailable: use the in-file conservative substitute for
      `speculative_ui` (documented, slower, lower quality) and set
      `degraded['speculative_ui']='local'`

  cap.t18.instruction.instruction_following_eval@1
      if unavailable: use the in-file conservative substitute for
      `instruction_following_eval` (documented, slower, lower quality) and
      set `degraded['instruction_following_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - flag lifecycle with owner, expiry and kill-switch requirements
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - experiment assignment with correct randomisation and analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - flag-state consistency across a distributed fleet
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - flag-debt monitoring and cleanup enforcement
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.feature.feature_flags_platform@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0973_feature_flags_platform.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0974-config-management-platform

**P0974 · `config_management_platform` — Fleet Configuration Management** · [spec](PART_SPECS_T20.md#p0974-config-management-platform) · [self-contained txt](../prompts/P0974_config_management_platform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0974  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0974 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0974  (24/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Fleet Configuration Management
file         : parts/t20_platform/P0974_config_management_platform.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.config_management_platform
language     : TypeScript 5.7
capability   : cap.t20.config.config_management_platform@1
determinism  : io
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
One coherent configuration across thousands of machines.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. versioned configuration with staged rollout and validation
  2. drift detection and reconciliation across the fleet
  3. emergency-override path with audit requirements
  4. measured configuration-convergence time

Expanded obligations:
  1. Implement versioned configuration with staged rollout and validation
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement drift detection and reconciliation across the fleet together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement emergency-override path with audit requirements as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured configuration-convergence time, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.config.config_management_platform@1
  cap.t20.config.config_management_platform.describe@1

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

  cap.t20.feature.feature_flags_platform@1
      if unavailable: use the in-file conservative substitute for
      `feature_flags_platform` (documented, slower, lower quality) and set
      `degraded['feature_flags_platform']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t08.speculative.speculative_tools@1
      if unavailable: use the in-file conservative substitute for
      `speculative_tools` (documented, slower, lower quality) and set
      `degraded['speculative_tools']='local'`

  cap.t09.slo.slo_manager@1
      if unavailable: use the in-file conservative substitute for
      `slo_manager` (documented, slower, lower quality) and set
      `degraded['slo_manager']='local'`

  cap.t18.efficiency.efficiency_eval@1
      if unavailable: use the in-file conservative substitute for
      `efficiency_eval` (documented, slower, lower quality) and set
      `degraded['efficiency_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - versioned configuration with staged rollout and validation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - drift detection and reconciliation across the fleet
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - emergency-override path with audit requirements
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured configuration-convergence time
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.config.config_management_platform@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0974_config_management_platform.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0975-observability-platform

**P0975 · `observability_platform` — Observability Platform: Metrics, Traces, Logs** · [spec](PART_SPECS_T20.md#p0975-observability-platform) · [self-contained txt](../prompts/P0975_observability_platform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0975  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0975 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0975  (25/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Observability Platform: Metrics, Traces, Logs
file         : parts/t20_platform/P0975_observability_platform.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.observability_platform
language     : TypeScript 5.7
capability   : cap.t20.observability.observability_platform@1
determinism  : io
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Full visibility into a 1000-part distributed system.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. unified telemetry pipeline with cardinality and cost control
  2. cross-part trace stitching with capability-level spans
  3. query interface for incident investigation
  4. measured telemetry cost per request and its reduction

Expanded obligations:
  1. Implement unified telemetry pipeline with cardinality and cost control
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement cross-part trace stitching with capability-level spans as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement query interface for incident investigation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement measured telemetry cost per request and its reduction with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.observability.observability_platform@1
  cap.t20.observability.observability_platform.describe@1

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

  cap.t20.config.config_management_platform@1
      if unavailable: use the in-file conservative substitute for
      `config_management_platform` (documented, slower, lower quality) and
      set `degraded['config_management_platform']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t08.kv.kv_offload_runtime@1
      if unavailable: use the in-file conservative substitute for
      `kv_offload_runtime` (documented, slower, lower quality) and set
      `degraded['kv_offload_runtime']='local'`

  cap.t09.cost.cost_optimiser@1
      if unavailable: use the in-file conservative substitute for
      `cost_optimiser` (documented, slower, lower quality) and set
      `degraded['cost_optimiser']='local'`

  cap.t18.eval.eval_cost_control@1
      if unavailable: use the in-file conservative substitute for
      `eval_cost_control` (documented, slower, lower quality) and set
      `degraded['eval_cost_control']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - unified telemetry pipeline with cardinality and cost control
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-part trace stitching with capability-level spans
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - query interface for incident investigation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured telemetry cost per request and its reduction
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.observability.observability_platform@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0975_observability_platform.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0976-alerting-oncall

**P0976 · `alerting_oncall` — Alerting, Escalation & On-Call Operations** · [spec](PART_SPECS_T20.md#p0976-alerting-oncall) · [self-contained txt](../prompts/P0976_alerting_oncall.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0976  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0976 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0976  (26/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Alerting, Escalation & On-Call Operations
file         : parts/t20_platform/P0976_alerting_oncall.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.alerting_oncall
language     : TypeScript 5.7
capability   : cap.t20.alerting.alerting_oncall@1
determinism  : io
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Humans learn about problems before customers do.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. symptom-based alerting with actionable runbook links
  2. alert-quality management (precision, actionability, fatigue reduction)
  3. escalation policy and paging integration
  4. measured alert precision and mean-time-to-acknowledge

Expanded obligations:
  1. Implement symptom-based alerting with actionable runbook links as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement alert-quality management (precision, actionability, fatigue
     reduction), and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement escalation policy and paging integration with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured alert precision and mean-time-to-acknowledge together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Zapier AutomationBench target reachable; the part
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.alerting.alerting_oncall@1
  cap.t20.alerting.alerting_oncall.describe@1

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

  cap.t20.observability.observability_platform@1
      if unavailable: use the in-file conservative substitute for
      `observability_platform` (documented, slower, lower quality) and set
      `degraded['observability_platform']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t08.tokenizer.tokenizer_runtime@1
      if unavailable: use the in-file conservative substitute for
      `tokenizer_runtime` (documented, slower, lower quality) and set
      `degraded['tokenizer_runtime']='local'`

  cap.t09.burst.burst_handling@1
      if unavailable: use the in-file conservative substitute for
      `burst_handling` (documented, slower, lower quality) and set
      `degraded['burst_handling']='local'`

  cap.t18.eval.eval_meta@1
      if unavailable: use the in-file conservative substitute for
      `eval_meta` (documented, slower, lower quality) and set
      `degraded['eval_meta']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - symptom-based alerting with actionable runbook links
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - alert-quality management (precision, actionability, fatigue redu
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - escalation policy and paging integration
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured alert precision and mean-time-to-acknowledge
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.alerting.alerting_oncall@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0976_alerting_oncall.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0977-incident-management

**P0977 · `incident_management` — Incident Management & Postmortem Process** · [spec](PART_SPECS_T20.md#p0977-incident-management) · [self-contained txt](../prompts/P0977_incident_management.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0977  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0977 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0977  (27/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Incident Management & Postmortem Process
file         : parts/t20_platform/P0977_incident_management.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.incident_management
language     : TypeScript 5.7
capability   : cap.t20.incident.incident_management@1
determinism  : io
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Every outage makes the system stronger.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. incident lifecycle with severity, roles and communication templates
  2. timeline reconstruction from telemetry and audit logs
  3. blameless postmortem with tracked action items
  4. measured recurrence rate of postmortem-covered causes

Expanded obligations:
  1. Implement incident lifecycle with severity, roles and communication
     templates, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement timeline reconstruction from telemetry and audit logs with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement blameless postmortem with tracked action items together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Zapier AutomationBench target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement measured recurrence rate of postmortem-covered causes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.

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
  cap.t20.incident.incident_management@1
  cap.t20.incident.incident_management.describe@1

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

  cap.t20.alerting.alerting_oncall@1
      if unavailable: use the in-file conservative substitute for
      `alerting_oncall` (documented, slower, lower quality) and set
      `degraded['alerting_oncall']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t08.chunked.chunked_prefill@1
      if unavailable: use the in-file conservative substitute for
      `chunked_prefill` (documented, slower, lower quality) and set
      `degraded['chunked_prefill']='local'`

  cap.t09.memoize.memoize_core@1
      if unavailable: use the in-file conservative substitute for
      `memoize_core` (documented, slower, lower quality) and set
      `degraded['memoize_core']='local'`

  cap.t18.grading.grading_engine@1
      if unavailable: use the in-file conservative substitute for
      `grading_engine` (documented, slower, lower quality) and set
      `degraded['grading_engine']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - incident lifecycle with severity, roles and communication templa
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - timeline reconstruction from telemetry and audit logs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blameless postmortem with tracked action items
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured recurrence rate of postmortem-covered causes
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.incident.incident_management@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0977_incident_management.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0978-runbook-automation

**P0978 · `runbook_automation` — Runbook Automation & Self-Healing** · [spec](PART_SPECS_T20.md#p0978-runbook-automation) · [self-contained txt](../prompts/P0978_runbook_automation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0978  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0978 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0978  (28/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Runbook Automation & Self-Healing
file         : parts/t20_platform/P0978_runbook_automation.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.runbook_automation
language     : TypeScript 5.7
capability   : cap.t20.runbook.runbook_automation@1
determinism  : io
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
The system fixes its own routine problems.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. automated remediation for known failure signatures
  2. safety guards preventing automation from worsening incidents
  3. human-approval requirements for risky remediations
  4. measured fraction of incidents auto-remediated

Expanded obligations:
  1. Implement automated remediation for known failure signatures with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement safety guards preventing automation from worsening incidents
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement human-approval requirements for risky remediations as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement measured fraction of incidents auto-remediated, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.

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
  cap.t20.runbook.runbook_automation@1
  cap.t20.runbook.runbook_automation.describe@1

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

  cap.t20.incident.incident_management@1
      if unavailable: use the in-file conservative substitute for
      `incident_management` (documented, slower, lower quality) and set
      `degraded['incident_management']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t08.cascade.cascade_acceptance@1
      if unavailable: use the in-file conservative substitute for
      `cascade_acceptance` (documented, slower, lower quality) and set
      `degraded['cascade_acceptance']='local'`

  cap.t09.precompute.precompute_engine@1
      if unavailable: use the in-file conservative substitute for
      `precompute_engine` (documented, slower, lower quality) and set
      `degraded['precompute_engine']='local'`

  cap.t18.swe.swe_verified_eval@1
      if unavailable: use the in-file conservative substitute for
      `swe_verified_eval` (documented, slower, lower quality) and set
      `degraded['swe_verified_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - automated remediation for known failure signatures
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - safety guards preventing automation from worsening incidents
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - human-approval requirements for risky remediations
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured fraction of incidents auto-remediated
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.runbook.runbook_automation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0978_runbook_automation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0979-chaos-engineering

**P0979 · `chaos_engineering` — Chaos Engineering & Resilience Verification** · [spec](PART_SPECS_T20.md#p0979-chaos-engineering) · [self-contained txt](../prompts/P0979_chaos_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0979  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0979 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0979  (29/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Chaos Engineering & Resilience Verification
file         : parts/t20_platform/P0979_chaos_engineering.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.chaos_engineering
language     : TypeScript 5.7
capability   : cap.t20.chaos.chaos_engineering@1
determinism  : io
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Breaks itself on purpose, in production, safely.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fault-injection experiment framework with blast-radius controls
  2. hypothesis-driven experiment design and result analysis
  3. experiment catalogue covering every dependency and failure mode
  4. measured resilience improvement from findings

Expanded obligations:
  1. Implement fault-injection experiment framework with blast-radius
     controls together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Zapier
     AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement hypothesis-driven experiment design and result analysis as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement experiment catalogue covering every dependency and failure
     mode, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement measured resilience improvement from findings with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's CursorBench 3.2 target reachable; the part
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.chaos.chaos_engineering@1
  cap.t20.chaos.chaos_engineering.describe@1

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

  cap.t20.runbook.runbook_automation@1
      if unavailable: use the in-file conservative substitute for
      `runbook_automation` (documented, slower, lower quality) and set
      `degraded['runbook_automation']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t08.session.session_affinity@1
      if unavailable: use the in-file conservative substitute for
      `session_affinity` (documented, slower, lower quality) and set
      `degraded['session_affinity']='local'`

  cap.t09.warmup.warmup_manager@1
      if unavailable: use the in-file conservative substitute for
      `warmup_manager` (documented, slower, lower quality) and set
      `degraded['warmup_manager']='local'`

  cap.t18.mmmu.mmmu_eval@1
      if unavailable: use the in-file conservative substitute for
      `mmmu_eval` (documented, slower, lower quality) and set
      `degraded['mmmu_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - fault-injection experiment framework with blast-radius controls
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hypothesis-driven experiment design and result analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - experiment catalogue covering every dependency and failure mode
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured resilience improvement from findings
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.chaos.chaos_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0979_chaos_engineering.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0980-disaster-recovery

**P0980 · `disaster_recovery` — Disaster Recovery & Business Continuity** · [spec](PART_SPECS_T20.md#p0980-disaster-recovery) · [self-contained txt](../prompts/P0980_disaster_recovery.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0980  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0980 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0980  (30/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Disaster Recovery & Business Continuity
file         : parts/t20_platform/P0980_disaster_recovery.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.disaster_recovery
language     : TypeScript 5.7
capability   : cap.t20.disaster.disaster_recovery@1
determinism  : io
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Survives losing a region, with proven recovery times.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. recovery objective definitions per system component
  2. backup, replication and restore procedures with integrity verification
  3. regular recovery drills with measured RTO and RPO
  4. drill-result documentation and gap remediation

Expanded obligations:
  1. Implement recovery objective definitions per system component as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement backup, replication and restore procedures with integrity
     verification, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement regular recovery drills with measured RTO and RPO with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement drill-result documentation and gap remediation together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.disaster.disaster_recovery@1
  cap.t20.disaster.disaster_recovery.describe@1

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

  cap.t20.chaos.chaos_engineering@1
      if unavailable: use the in-file conservative substitute for
      `chaos_engineering` (documented, slower, lower quality) and set
      `degraded['chaos_engineering']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t08.multi.multi_gpu_runtime@1
      if unavailable: use the in-file conservative substitute for
      `multi_gpu_runtime` (documented, slower, lower quality) and set
      `degraded['multi_gpu_runtime']='local'`

  cap.t09.priority.priority_lanes@1
      if unavailable: use the in-file conservative substitute for
      `priority_lanes` (documented, slower, lower quality) and set
      `degraded['priority_lanes']='local'`

  cap.t18.longcontext.longcontext_eval@1
      if unavailable: use the in-file conservative substitute for
      `longcontext_eval` (documented, slower, lower quality) and set
      `degraded['longcontext_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - recovery objective definitions per system component
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - backup, replication and restore procedures with integrity verifi
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regular recovery drills with measured RTO and RPO
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - drill-result documentation and gap remediation
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.disaster.disaster_recovery@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0980_disaster_recovery.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0981-capacity-operations

**P0981 · `capacity_operations` — Capacity Operations & Demand Management** · [spec](PART_SPECS_T20.md#p0981-capacity-operations) · [self-contained txt](../prompts/P0981_capacity_operations.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0981  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0981 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0981  (31/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Capacity Operations & Demand Management
file         : parts/t20_platform/P0981_capacity_operations.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.capacity_operations
language     : TypeScript 5.7
capability   : cap.t20.capacity.capacity_operations@1
determinism  : io
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Never runs out, never wastes.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. demand forecasting with uncertainty and lead-time awareness
  2. procurement and allocation planning across hardware generations
  3. utilisation and headroom monitoring with automated recommendations
  4. measured forecast accuracy and utilisation improvement

Expanded obligations:
  1. Implement demand forecasting with uncertainty and lead-time awareness,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement procurement and allocation planning across hardware
     generations with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's CursorBench 3.2
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement utilisation and headroom monitoring with automated
     recommendations together with its verification path, so that anything
     this mechanism produces can be independently re-checked *inside this
     same file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of Zapier
     AutomationBench, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured forecast accuracy and utilisation improvement as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
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
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.capacity.capacity_operations@1
  cap.t20.capacity.capacity_operations.describe@1

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

  cap.t20.disaster.disaster_recovery@1
      if unavailable: use the in-file conservative substitute for
      `disaster_recovery` (documented, slower, lower quality) and set
      `degraded['disaster_recovery']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t08.deadline.deadline_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `deadline_scheduling` (documented, slower, lower quality) and set
      `degraded['deadline_scheduling']='local'`

  cap.t09.adaptive.adaptive_quality@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_quality` (documented, slower, lower quality) and set
      `degraded['adaptive_quality']='local'`

  cap.t18.multilingual.multilingual_eval@1
      if unavailable: use the in-file conservative substitute for
      `multilingual_eval` (documented, slower, lower quality) and set
      `degraded['multilingual_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - demand forecasting with uncertainty and lead-time awareness
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - procurement and allocation planning across hardware generations
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - utilisation and headroom monitoring with automated recommendatio
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured forecast accuracy and utilisation improvement
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.capacity.capacity_operations@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0981_capacity_operations.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0982-cost-operations

**P0982 · `cost_operations` — Cost Operations & Efficiency Programme** · [spec](PART_SPECS_T20.md#p0982-cost-operations) · [self-contained txt](../prompts/P0982_cost_operations.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0982  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0982 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0982  (32/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Cost Operations & Efficiency Programme
file         : parts/t20_platform/P0982_cost_operations.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.cost_operations
language     : TypeScript 5.7
capability   : cap.t20.cost.cost_operations@1
determinism  : io
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Continuous, measured cost reduction.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cost attribution across parts, features and customers
  2. efficiency-opportunity identification with projected savings
  3. savings verification after implementation
  4. measured cost-per-request trend

Expanded obligations:
  1. Implement cost attribution across parts, features and customers with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement efficiency-opportunity identification with projected savings
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement savings verification after implementation as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against CursorBench 3.2
     — a regression on that benchmark is an automatic rejection of this part.
  4. Implement measured cost-per-request trend, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's Zapier AutomationBench target reachable; the
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.cost.cost_operations@1
  cap.t20.cost.cost_operations.describe@1

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

  cap.t20.capacity.capacity_operations@1
      if unavailable: use the in-file conservative substitute for
      `capacity_operations` (documented, slower, lower quality) and set
      `degraded['capacity_operations']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t08.engine.engine_determinism@1
      if unavailable: use the in-file conservative substitute for
      `engine_determinism` (documented, slower, lower quality) and set
      `degraded['engine_determinism']='local'`

  cap.t09.energy.energy_efficiency@1
      if unavailable: use the in-file conservative substitute for
      `energy_efficiency` (documented, slower, lower quality) and set
      `degraded['energy_efficiency']='local'`

  cap.t18.competitor.competitor_tracking@1
      if unavailable: use the in-file conservative substitute for
      `competitor_tracking` (documented, slower, lower quality) and set
      `degraded['competitor_tracking']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - cost attribution across parts, features and customers
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - efficiency-opportunity identification with projected savings
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - savings verification after implementation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured cost-per-request trend
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.cost.cost_operations@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0982_cost_operations.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0983-edge-deployment

**P0983 · `edge_deployment` — Edge & Regional Deployment** · [spec](PART_SPECS_T20.md#p0983-edge-deployment) · [self-contained txt](../prompts/P0983_edge_deployment.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0983  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0983 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0983  (33/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Edge & Regional Deployment
file         : parts/t20_platform/P0983_edge_deployment.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.edge_deployment
language     : TypeScript 5.7
capability   : cap.t20.edge.edge_deployment@1
determinism  : io
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Low latency and data residency worldwide.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. regional deployment topology with data-residency enforcement
  2. edge caching and request-routing policy
  3. per-region capability and compliance differences handling
  4. measured latency improvement per region

Expanded obligations:
  1. Implement regional deployment topology with data-residency enforcement
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement edge caching and request-routing policy as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against CursorBench 3.2
     — a regression on that benchmark is an automatic rejection of this part.
  3. Implement per-region capability and compliance differences handling, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured latency improvement per region with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of CursorBench 3.2, so its p99 latency
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.edge.edge_deployment@1
  cap.t20.edge.edge_deployment.describe@1

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

  cap.t20.cost.cost_operations@1
      if unavailable: use the in-file conservative substitute for
      `cost_operations` (documented, slower, lower quality) and set
      `degraded['cost_operations']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t08.engine.engine_config_tuning@1
      if unavailable: use the in-file conservative substitute for
      `engine_config_tuning` (documented, slower, lower quality) and set
      `degraded['engine_config_tuning']='local'`

  cap.t09.realtime.realtime_mode@1
      if unavailable: use the in-file conservative substitute for
      `realtime_mode` (documented, slower, lower quality) and set
      `degraded['realtime_mode']='local'`

  cap.t18.eval.eval_dashboard@1
      if unavailable: use the in-file conservative substitute for
      `eval_dashboard` (documented, slower, lower quality) and set
      `degraded['eval_dashboard']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - regional deployment topology with data-residency enforcement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - edge caching and request-routing policy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-region capability and compliance differences handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured latency improvement per region
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.edge.edge_deployment@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0983_edge_deployment.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0984-on-prem-deployment

**P0984 · `on_prem_deployment` — Self-Hosted & Air-Gapped Deployment** · [spec](PART_SPECS_T20.md#p0984-on-prem-deployment) · [self-contained txt](../prompts/P0984_on_prem_deployment.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0984  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0984 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0984  (34/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Self-Hosted & Air-Gapped Deployment
file         : parts/t20_platform/P0984_on_prem_deployment.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.on_prem_deployment
language     : TypeScript 5.7
capability   : cap.t20.on.on_prem_deployment@1
determinism  : io
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Runs inside customer environments, fully disconnected.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. deployment packaging with dependency vendoring
  2. air-gapped licensing, updating and telemetry-free operation
  3. hardware-requirement specification and validation tooling
  4. installation success rate across target environments

Expanded obligations:
  1. Implement deployment packaging with dependency vendoring as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement air-gapped licensing, updating and telemetry-free operation,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement hardware-requirement specification and validation tooling with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement installation success rate across target environments together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.on.on_prem_deployment@1
  cap.t20.on.on_prem_deployment.describe@1

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

  cap.t20.edge.edge_deployment@1
      if unavailable: use the in-file conservative substitute for
      `edge_deployment` (documented, slower, lower quality) and set
      `degraded['edge_deployment']='local'`

  cap.t08.continuous.continuous_batching@1
      if unavailable: use the in-file conservative substitute for
      `continuous_batching` (documented, slower, lower quality) and set
      `degraded['continuous_batching']='local'`

  cap.t09.speed.speed_law_model@1
      if unavailable: use the in-file conservative substitute for
      `speed_law_model` (documented, slower, lower quality) and set
      `degraded['speed_law_model']='local'`

  cap.t18.eval.eval_registry@1
      if unavailable: use the in-file conservative substitute for
      `eval_registry` (documented, slower, lower quality) and set
      `degraded['eval_registry']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - deployment packaging with dependency vendoring
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - air-gapped licensing, updating and telemetry-free operation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hardware-requirement specification and validation tooling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - installation success rate across target environments
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.on.on_prem_deployment@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0984_on_prem_deployment.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0985-container-orchestration

**P0985 · `container_orchestration` — Container & Orchestration Integration** · [spec](PART_SPECS_T20.md#p0985-container-orchestration) · [self-contained txt](../prompts/P0985_container_orchestration.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0985  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0985 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0985  (35/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Container & Orchestration Integration
file         : parts/t20_platform/P0985_container_orchestration.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.container_orchestration
language     : TypeScript 5.7
capability   : cap.t20.container.container_orchestration@1
determinism  : io
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Native operation in modern infrastructure.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. container images with minimal surface and reproducible builds
  2. orchestrator manifests with correct probes, limits and topology hints
  3. graceful startup, drain and termination behaviour
  4. verified operation across major orchestration platforms

Expanded obligations:
  1. Implement container images with minimal surface and reproducible builds,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement orchestrator manifests with correct probes, limits and
     topology hints with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of CursorBench
     3.2, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement graceful startup, drain and termination behaviour together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement verified operation across major orchestration platforms as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
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
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.container.container_orchestration@1
  cap.t20.container.container_orchestration.describe@1

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

  cap.t20.on.on_prem_deployment@1
      if unavailable: use the in-file conservative substitute for
      `on_prem_deployment` (documented, slower, lower quality) and set
      `degraded['on_prem_deployment']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t08.cascade.cascade_tree_verify@1
      if unavailable: use the in-file conservative substitute for
      `cascade_tree_verify` (documented, slower, lower quality) and set
      `degraded['cascade_tree_verify']='local'`

  cap.t09.distill.distill_fast_paths@1
      if unavailable: use the in-file conservative substitute for
      `distill_fast_paths` (documented, slower, lower quality) and set
      `degraded['distill_fast_paths']='local'`

  cap.t18.contamination.contamination_audit@1
      if unavailable: use the in-file conservative substitute for
      `contamination_audit` (documented, slower, lower quality) and set
      `degraded['contamination_audit']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - container images with minimal surface and reproducible builds
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - orchestrator manifests with correct probes, limits and topology 
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - graceful startup, drain and termination behaviour
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verified operation across major orchestration platforms
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.container.container_orchestration@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0985_container_orchestration.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0986-infrastructure-as-code

**P0986 · `infrastructure_as_code` — Infrastructure as Code & Environment Definition** · [spec](PART_SPECS_T20.md#p0986-infrastructure-as-code) · [self-contained txt](../prompts/P0986_infrastructure_as_code.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0986  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0986 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0986  (36/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Infrastructure as Code & Environment Definition
file         : parts/t20_platform/P0986_infrastructure_as_code.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.infrastructure_as_code
language     : TypeScript 5.7
capability   : cap.t20.infrastructure.infrastructure_as_code@1
determinism  : io
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Every environment reproducible from source.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. declarative infrastructure definitions for all environments
  2. drift detection between declared and actual infrastructure
  3. environment parity verification (dev, staging, production)
  4. measured environment-provisioning time and reliability

Expanded obligations:
  1. Implement declarative infrastructure definitions for all environments
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement drift detection between declared and actual infrastructure
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement environment parity verification (dev, staging, production) as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured environment-provisioning time and reliability, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.infrastructure.infrastructure_as_code@1
  cap.t20.infrastructure.infrastructure_as_code.describe@1

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

  cap.t20.container.container_orchestration@1
      if unavailable: use the in-file conservative substitute for
      `container_orchestration` (documented, slower, lower quality) and set
      `degraded['container_orchestration']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t08.prefix.prefix_cache_runtime@1
      if unavailable: use the in-file conservative substitute for
      `prefix_cache_runtime` (documented, slower, lower quality) and set
      `degraded['prefix_cache_runtime']='local'`

  cap.t09.jitter.jitter_control@1
      if unavailable: use the in-file conservative substitute for
      `jitter_control` (documented, slower, lower quality) and set
      `degraded['jitter_control']='local'`

  cap.t18.math.math_eval@1
      if unavailable: use the in-file conservative substitute for
      `math_eval` (documented, slower, lower quality) and set
      `degraded['math_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - declarative infrastructure definitions for all environments
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - drift detection between declared and actual infrastructure
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - environment parity verification (dev, staging, production)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured environment-provisioning time and reliability
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.infrastructure.infrastructure_as_code@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0986_infrastructure_as_code.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0987-secrets-management

**P0987 · `secrets_management` — Secrets Management & Key Rotation** · [spec](PART_SPECS_T20.md#p0987-secrets-management) · [self-contained txt](../prompts/P0987_secrets_management.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0987  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0987 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0987  (37/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Secrets Management & Key Rotation
file         : parts/t20_platform/P0987_secrets_management.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.secrets_management
language     : TypeScript 5.7
capability   : cap.t20.secrets.secrets_management@1
determinism  : io
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Operational secret hygiene, enforced.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. central secret storage with scoped access and audit
  2. automatic rotation without service interruption
  3. secret-scanning in code, configs, logs and model outputs
  4. verified zero-secret-exposure across all channels

Expanded obligations:
  1. Implement central secret storage with scoped access and audit together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement automatic rotation without service interruption as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement secret-scanning in code, configs, logs and model outputs, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement verified zero-secret-exposure across all channels with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.secrets.secrets_management@1
  cap.t20.secrets.secrets_management.describe@1

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

  cap.t20.infrastructure.infrastructure_as_code@1
      if unavailable: use the in-file conservative substitute for
      `infrastructure_as_code` (documented, slower, lower quality) and set
      `degraded['infrastructure_as_code']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t08.batch.batch_invariance@1
      if unavailable: use the in-file conservative substitute for
      `batch_invariance` (documented, slower, lower quality) and set
      `degraded['batch_invariance']='local'`

  cap.t09.batch.batch_latency_tradeoff@1
      if unavailable: use the in-file conservative substitute for
      `batch_latency_tradeoff` (documented, slower, lower quality) and set
      `degraded['batch_latency_tradeoff']='local'`

  cap.t18.security.security_eval@1
      if unavailable: use the in-file conservative substitute for
      `security_eval` (documented, slower, lower quality) and set
      `degraded['security_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - central secret storage with scoped access and audit
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automatic rotation without service interruption
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - secret-scanning in code, configs, logs and model outputs
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verified zero-secret-exposure across all channels
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.secrets.secrets_management@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0987_secrets_management.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0988-compliance-platform

**P0988 · `compliance_platform` — Compliance & Certification Support** · [spec](PART_SPECS_T20.md#p0988-compliance-platform) · [self-contained txt](../prompts/P0988_compliance_platform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0988  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0988 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0988  (38/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Compliance & Certification Support
file         : parts/t20_platform/P0988_compliance_platform.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.compliance_platform
language     : TypeScript 5.7
capability   : cap.t20.compliance.compliance_platform@1
determinism  : io
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Meets the standards enterprises require.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. control mapping to major frameworks with evidence collection
  2. continuous control monitoring and exception tracking
  3. audit-evidence package generation
  4. certification-readiness assessment reporting

Expanded obligations:
  1. Implement control mapping to major frameworks with evidence collection
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's CursorBench 3.2 target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement continuous control monitoring and exception tracking, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of Zapier AutomationBench, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement audit-evidence package generation with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement certification-readiness assessment reporting together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Zapier AutomationBench target reachable; the part
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.compliance.compliance_platform@1
  cap.t20.compliance.compliance_platform.describe@1

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

  cap.t20.secrets.secrets_management@1
      if unavailable: use the in-file conservative substitute for
      `secrets_management` (documented, slower, lower quality) and set
      `degraded['secrets_management']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t08.cancellation.cancellation@1
      if unavailable: use the in-file conservative substitute for
      `cancellation` (documented, slower, lower quality) and set
      `degraded['cancellation']='local'`

  cap.t09.io.io_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `io_scheduling` (documented, slower, lower quality) and set
      `degraded['io_scheduling']='local'`

  cap.t18.bias.bias_fairness_eval@1
      if unavailable: use the in-file conservative substitute for
      `bias_fairness_eval` (documented, slower, lower quality) and set
      `degraded['bias_fairness_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - control mapping to major frameworks with evidence collection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - continuous control monitoring and exception tracking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - audit-evidence package generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - certification-readiness assessment reporting
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.compliance.compliance_platform@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0988_compliance_platform.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0989-data-residency

**P0989 · `data_residency` — Data Residency & Sovereignty Controls** · [spec](PART_SPECS_T20.md#p0989-data-residency) · [self-contained txt](../prompts/P0989_data_residency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0989  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0989 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0989  (39/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Data Residency & Sovereignty Controls
file         : parts/t20_platform/P0989_data_residency.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.data_residency
language     : TypeScript 5.7
capability   : cap.t20.data.data_residency@1
determinism  : io
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Data stays where it is legally required to stay.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-request and per-tenant residency policy enforcement
  2. cross-border transfer prevention with verification
  3. regional key management and processing isolation
  4. residency-compliance verification testing

Expanded obligations:
  1. Implement per-request and per-tenant residency policy enforcement, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement cross-border transfer prevention with verification with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement regional key management and processing isolation together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Zapier AutomationBench target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement residency-compliance verification testing as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.data.data_residency@1
  cap.t20.data.data_residency.describe@1

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

  cap.t20.compliance.compliance_platform@1
      if unavailable: use the in-file conservative substitute for
      `compliance_platform` (documented, slower, lower quality) and set
      `degraded['compliance_platform']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t08.overload.overload_shedding@1
      if unavailable: use the in-file conservative substitute for
      `overload_shedding` (documented, slower, lower quality) and set
      `degraded['overload_shedding']='local'`

  cap.t09.throughput.throughput_optimiser@1
      if unavailable: use the in-file conservative substitute for
      `throughput_optimiser` (documented, slower, lower quality) and set
      `degraded['throughput_optimiser']='local'`

  cap.t18.capability.capability_map@1
      if unavailable: use the in-file conservative substitute for
      `capability_map` (documented, slower, lower quality) and set
      `degraded['capability_map']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - per-request and per-tenant residency policy enforcement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-border transfer prevention with verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regional key management and processing isolation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - residency-compliance verification testing
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.data.data_residency@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0989_data_residency.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0990-customer-support-tooling

**P0990 · `customer_support_tooling` — Support Tooling & Diagnostics** · [spec](PART_SPECS_T20.md#p0990-customer-support-tooling) · [self-contained txt](../prompts/P0990_customer_support_tooling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0990  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0990 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0990  (40/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Support Tooling & Diagnostics
file         : parts/t20_platform/P0990_customer_support_tooling.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.customer_support_tooling
language     : TypeScript 5.7
capability   : cap.t20.customer.customer_support_tooling@1
determinism  : io
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Support can answer 'what happened to my request' precisely.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. request-lookup tooling with privacy-preserving access controls
  2. diagnostic bundle generation for customer issues
  3. known-issue matching and resolution suggestion
  4. measured first-contact resolution rate

Expanded obligations:
  1. Implement request-lookup tooling with privacy-preserving access controls
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against CursorBench 3.2 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement diagnostic bundle generation for customer issues together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Zapier AutomationBench target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement known-issue matching and resolution suggestion as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement measured first-contact resolution rate, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.

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
  cap.t20.customer.customer_support_tooling@1
  cap.t20.customer.customer_support_tooling.describe@1

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

  cap.t20.data.data_residency@1
      if unavailable: use the in-file conservative substitute for
      `data_residency` (documented, slower, lower quality) and set
      `degraded['data_residency']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t08.cascade.cascade_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `cascade_speed_proof` (documented, slower, lower quality) and set
      `degraded['cascade_speed_proof']='local'`

  cap.t09.benchmark.benchmark_speed_public@1
      if unavailable: use the in-file conservative substitute for
      `benchmark_speed_public` (documented, slower, lower quality) and set
      `degraded['benchmark_speed_public']='local'`

  cap.t18.dominance.dominance_proof@1
      if unavailable: use the in-file conservative substitute for
      `dominance_proof` (documented, slower, lower quality) and set
      `degraded['dominance_proof']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - request-lookup tooling with privacy-preserving access controls
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - diagnostic bundle generation for customer issues
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - known-issue matching and resolution suggestion
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured first-contact resolution rate
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.customer.customer_support_tooling@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0990_customer_support_tooling.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0991-documentation-platform

**P0991 · `documentation_platform` — Documentation Platform & Content** · [spec](PART_SPECS_T20.md#p0991-documentation-platform) · [self-contained txt](../prompts/P0991_documentation_platform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0991  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0991 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0991  (41/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Documentation Platform & Content
file         : parts/t20_platform/P0991_documentation_platform.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.documentation_platform
language     : TypeScript 5.7
capability   : cap.t20.documentation.documentation_platform@1
determinism  : io
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Documentation that makes the system usable.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. API reference generation from specifications with example verification
  2. conceptual guides, tutorials and cookbook content
  3. documentation testing (every example executes correctly)
  4. measured developer time-to-first-success

Expanded obligations:
  1. Implement API reference generation from specifications with example
     verification together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Zapier
     AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement conceptual guides, tutorials and cookbook content as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of CursorBench 3.2, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement documentation testing (every example executes correctly), and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement measured developer time-to-first-success with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's CursorBench 3.2 target reachable; the part
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
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.documentation.documentation_platform@1
  cap.t20.documentation.documentation_platform.describe@1

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

  cap.t20.customer.customer_support_tooling@1
      if unavailable: use the in-file conservative substitute for
      `customer_support_tooling` (documented, slower, lower quality) and set
      `degraded['customer_support_tooling']='local'`

  cap.t08.engine.engine_core@1
      if unavailable: use the in-file conservative substitute for
      `engine_core` (documented, slower, lower quality) and set
      `degraded['engine_core']='local'`

  cap.t09.latency.latency_accounting@1
      if unavailable: use the in-file conservative substitute for
      `latency_accounting` (documented, slower, lower quality) and set
      `degraded['latency_accounting']='local'`

  cap.t18.eval.eval_framework@1
      if unavailable: use the in-file conservative substitute for
      `eval_framework` (documented, slower, lower quality) and set
      `degraded['eval_framework']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - API reference generation from specifications with example verifi
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - conceptual guides, tutorials and cookbook content
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - documentation testing (every example executes correctly)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured developer time-to-first-success
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.documentation.documentation_platform@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0991_documentation_platform.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0992-developer-onboarding

**P0992 · `developer_onboarding` — Developer Onboarding & Examples** · [spec](PART_SPECS_T20.md#p0992-developer-onboarding) · [self-contained txt](../prompts/P0992_developer_onboarding.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0992  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0992 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0992  (42/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Developer Onboarding & Examples
file         : parts/t20_platform/P0992_developer_onboarding.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.developer_onboarding
language     : TypeScript 5.7
capability   : cap.t20.developer.developer_onboarding@1
determinism  : io
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
From zero to working integration in minutes.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. quickstart paths per language and use case
  2. example application suite with automated verification
  3. common-mistake detection and guidance
  4. measured onboarding completion rate and time

Expanded obligations:
  1. Implement quickstart paths per language and use case as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     CursorBench 3.2, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement example application suite with automated verification, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement common-mistake detection and guidance with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's CursorBench 3.2 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement measured onboarding completion rate and time together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
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
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.developer.developer_onboarding@1
  cap.t20.developer.developer_onboarding.describe@1

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

  cap.t20.documentation.documentation_platform@1
      if unavailable: use the in-file conservative substitute for
      `documentation_platform` (documented, slower, lower quality) and set
      `degraded['documentation_platform']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t08.cascade.cascade_stage3_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage3_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage3_draft']='local'`

  cap.t09.early.early_exit_runtime@1
      if unavailable: use the in-file conservative substitute for
      `early_exit_runtime` (documented, slower, lower quality) and set
      `degraded['early_exit_runtime']='local'`

  cap.t18.variance.variance_control@1
      if unavailable: use the in-file conservative substitute for
      `variance_control` (documented, slower, lower quality) and set
      `degraded['variance_control']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - quickstart paths per language and use case
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - example application suite with automated verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - common-mistake detection and guidance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured onboarding completion rate and time
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.developer.developer_onboarding@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0992_developer_onboarding.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0993-playground-console

**P0993 · `playground_console` — Interactive Console & Playground** · [spec](PART_SPECS_T20.md#p0993-playground-console) · [self-contained txt](../prompts/P0993_playground_console.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0993  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0993 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0993  (43/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Interactive Console & Playground
file         : parts/t20_platform/P0993_playground_console.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.playground_console
language     : TypeScript 5.7
capability   : cap.t20.playground.playground_console@1
determinism  : io
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Try everything before writing code.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. interactive request construction with parameter exploration
  2. cost and latency display before and after execution
  3. code-export in every supported SDK
  4. usability validation with new developers

Expanded obligations:
  1. Implement interactive request construction with parameter exploration,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement cost and latency display before and after execution with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's CursorBench 3.2 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement code-export in every supported SDK together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement usability validation with new developers as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against CursorBench 3.2
     — a regression on that benchmark is an automatic rejection of this part.

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
  cap.t20.playground.playground_console@1
  cap.t20.playground.playground_console.describe@1

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

  cap.t20.developer.developer_onboarding@1
      if unavailable: use the in-file conservative substitute for
      `developer_onboarding` (documented, slower, lower quality) and set
      `degraded['developer_onboarding']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t08.paged.paged_attention_runtime@1
      if unavailable: use the in-file conservative substitute for
      `paged_attention_runtime` (documented, slower, lower quality) and set
      `degraded['paged_attention_runtime']='local'`

  cap.t09.tail.tail_latency@1
      if unavailable: use the in-file conservative substitute for
      `tail_latency` (documented, slower, lower quality) and set
      `degraded['tail_latency']='local'`

  cap.t18.gpqa.gpqa_eval@1
      if unavailable: use the in-file conservative substitute for
      `gpqa_eval` (documented, slower, lower quality) and set
      `degraded['gpqa_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - interactive request construction with parameter exploration
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost and latency display before and after execution
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - code-export in every supported SDK
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - usability validation with new developers
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.playground.playground_console@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0993_playground_console.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0994-model-registry-platform

**P0994 · `model_registry_platform` — Model & Artifact Registry** · [spec](PART_SPECS_T20.md#p0994-model-registry-platform) · [self-contained txt](../prompts/P0994_model_registry_platform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0994  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0994 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0994  (44/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Model & Artifact Registry
file         : parts/t20_platform/P0994_model_registry_platform.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.model_registry_platform
language     : TypeScript 5.7
capability   : cap.t20.model.model_registry_platform@1
determinism  : io
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Every deployed model version tracked and reproducible.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. model artifact storage with lineage, evaluation results and approvals
  2. deployment-to-version mapping with audit history
  3. artifact integrity and signature verification
  4. registry completeness and correctness auditing

Expanded obligations:
  1. Implement model artifact storage with lineage, evaluation results and
     approvals with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's CursorBench 3.2
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  2. Implement deployment-to-version mapping with audit history together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement artifact integrity and signature verification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement registry completeness and correctness auditing, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Zapier AutomationBench target
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
  cap.t20.model.model_registry_platform@1
  cap.t20.model.model_registry_platform.describe@1

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

  cap.t20.playground.playground_console@1
      if unavailable: use the in-file conservative substitute for
      `playground_console` (documented, slower, lower quality) and set
      `degraded['playground_console']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t08.streaming.streaming_output@1
      if unavailable: use the in-file conservative substitute for
      `streaming_output` (documented, slower, lower quality) and set
      `degraded['streaming_output']='local'`

  cap.t09.compression.compression_latency@1
      if unavailable: use the in-file conservative substitute for
      `compression_latency` (documented, slower, lower quality) and set
      `degraded['compression_latency']='local'`

  cap.t18.lifescience.lifescience_eval@1
      if unavailable: use the in-file conservative substitute for
      `lifescience_eval` (documented, slower, lower quality) and set
      `degraded['lifescience_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - model artifact storage with lineage, evaluation results and appr
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deployment-to-version mapping with audit history
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - artifact integrity and signature verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - registry completeness and correctness auditing
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.model.model_registry_platform@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0994_model_registry_platform.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0995-evaluation-integration

**P0995 · `evaluation_integration` — Continuous Evaluation in the Deployment Pipeline** · [spec](PART_SPECS_T20.md#p0995-evaluation-integration) · [self-contained txt](../prompts/P0995_evaluation_integration.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0995  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0995 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0995  (45/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Continuous Evaluation in the Deployment Pipeline
file         : parts/t20_platform/P0995_evaluation_integration.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.evaluation_integration
language     : TypeScript 5.7
capability   : cap.t20.evaluation.evaluation_integration@1
determinism  : io
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Quality gates automated into every deploy.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. pre-deployment benchmark execution with pass criteria
  2. post-deployment online quality monitoring
  3. automatic rollback on quality regression
  4. measured quality-regression escape rate

Expanded obligations:
  1. Implement pre-deployment benchmark execution with pass criteria together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement post-deployment online quality monitoring as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against CursorBench 3.2
     — a regression on that benchmark is an automatic rejection of this part.
  3. Implement automatic rollback on quality regression, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured quality-regression escape rate with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of CursorBench 3.2, so its p99 latency
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.evaluation.evaluation_integration@1
  cap.t20.evaluation.evaluation_integration.describe@1

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

  cap.t20.model.model_registry_platform@1
      if unavailable: use the in-file conservative substitute for
      `model_registry_platform` (documented, slower, lower quality) and set
      `degraded['model_registry_platform']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t08.request.request_lifecycle@1
      if unavailable: use the in-file conservative substitute for
      `request_lifecycle` (documented, slower, lower quality) and set
      `degraded['request_lifecycle']='local'`

  cap.t09.numa.numa_latency@1
      if unavailable: use the in-file conservative substitute for
      `numa_latency` (documented, slower, lower quality) and set
      `degraded['numa_latency']='local'`

  cap.t18.adversarial.adversarial_eval@1
      if unavailable: use the in-file conservative substitute for
      `adversarial_eval` (documented, slower, lower quality) and set
      `degraded['adversarial_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - pre-deployment benchmark execution with pass criteria
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - post-deployment online quality monitoring
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic rollback on quality regression
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured quality-regression escape rate
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.evaluation.evaluation_integration@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0995_evaluation_integration.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0996-distributed-dev-workflow

**P0996 · `distributed_dev_workflow` — 1000-Worker Distributed Development Workflow** · [spec](PART_SPECS_T20.md#p0996-distributed-dev-workflow) · [self-contained txt](../prompts/P0996_distributed_dev_workflow.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0996  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0996 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0996  (46/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : 1000-Worker Distributed Development Workflow
file         : parts/t20_platform/P0996_distributed_dev_workflow.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.distributed_dev_workflow
language     : TypeScript 5.7
capability   : cap.t20.distributed.distributed_dev_workflow@1
determinism  : io
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
The process that lets 1000 isolated authors produce one system.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. work-assignment protocol with contract-frozen briefs per part
  2. submission validation, conformance checking and acceptance criteria
  3. conflict-free integration procedure requiring no shared folders
  4. measured first-submission acceptance rate across parts

Expanded obligations:
  1. Implement work-assignment protocol with contract-frozen briefs per part
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against CursorBench 3.2 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement submission validation, conformance checking and acceptance
     criteria, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement conflict-free integration procedure requiring no shared
     folders with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of CursorBench
     3.2, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  4. Implement measured first-submission acceptance rate across parts
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.

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
  cap.t20.distributed.distributed_dev_workflow@1
  cap.t20.distributed.distributed_dev_workflow.describe@1

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

  cap.t20.evaluation.evaluation_integration@1
      if unavailable: use the in-file conservative substitute for
      `evaluation_integration` (documented, slower, lower quality) and set
      `degraded['evaluation_integration']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t08.autoscaling.autoscaling@1
      if unavailable: use the in-file conservative substitute for
      `autoscaling` (documented, slower, lower quality) and set
      `degraded['autoscaling']='local'`

  cap.t09.bottleneck.bottleneck_analyser@1
      if unavailable: use the in-file conservative substitute for
      `bottleneck_analyser` (documented, slower, lower quality) and set
      `degraded['bottleneck_analyser']='local'`

  cap.t18.failure.failure_taxonomy@1
      if unavailable: use the in-file conservative substitute for
      `failure_taxonomy` (documented, slower, lower quality) and set
      `degraded['failure_taxonomy']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - work-assignment protocol with contract-frozen briefs per part
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - submission validation, conformance checking and acceptance crite
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conflict-free integration procedure requiring no shared folders
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured first-submission acceptance rate across parts
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.distributed.distributed_dev_workflow@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0996_distributed_dev_workflow.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0997-part-submission-gate

**P0997 · `part_submission_gate` — Part Submission Validation Gate** · [spec](PART_SPECS_T20.md#p0997-part-submission-gate) · [self-contained txt](../prompts/P0997_part_submission_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0997  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0997 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0997  (47/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Part Submission Validation Gate
file         : parts/t20_platform/P0997_part_submission_gate.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.part_submission_gate
language     : TypeScript 5.7
capability   : cap.t20.part.part_submission_gate@1
determinism  : io
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Automated acceptance testing for each of the 1000 deliverables.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. line-count, structure and required-symbol verification
  2. in-file test execution with pass and coverage requirements
  3. contract-clause conformance and manifest validation
  4. clear rejection reports enabling one-pass correction

Expanded obligations:
  1. Implement line-count, structure and required-symbol verification, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Zapier AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement in-file test execution with pass and coverage requirements
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement contract-clause conformance and manifest validation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement clear rejection reports enabling one-pass correction as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.part.part_submission_gate@1
  cap.t20.part.part_submission_gate.describe@1

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

  cap.t20.distributed.distributed_dev_workflow@1
      if unavailable: use the in-file conservative substitute for
      `distributed_dev_workflow` (documented, slower, lower quality) and set
      `degraded['distributed_dev_workflow']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t08.engine.engine_bench_serving@1
      if unavailable: use the in-file conservative substitute for
      `engine_bench_serving` (documented, slower, lower quality) and set
      `degraded['engine_bench_serving']='local'`

  cap.t09.latency.latency_simulator@1
      if unavailable: use the in-file conservative substitute for
      `latency_simulator` (documented, slower, lower quality) and set
      `degraded['latency_simulator']='local'`

  cap.t18.eval.eval_reproducibility@1
      if unavailable: use the in-file conservative substitute for
      `eval_reproducibility` (documented, slower, lower quality) and set
      `degraded['eval_reproducibility']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - line-count, structure and required-symbol verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - in-file test execution with pass and coverage requirements
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - contract-clause conformance and manifest validation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - clear rejection reports enabling one-pass correction
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.part.part_submission_gate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0997_part_submission_gate.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0998-assembly-dashboard

**P0998 · `assembly_dashboard` — Assembly Progress & Health Data Products** · [spec](PART_SPECS_T20.md#p0998-assembly-dashboard) · [self-contained txt](../prompts/P0998_assembly_dashboard.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0998  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0998 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0998  (48/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Assembly Progress & Health Data Products
file         : parts/t20_platform/P0998_assembly_dashboard.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.assembly_dashboard
language     : TypeScript 5.7
capability   : cap.t20.assembly.assembly_dashboard@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Live view of 1000 parts: submitted, validated, integrated, degraded.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-part status with blocking-dependency identification
  2. capability-coverage and integration-health reporting
  3. critical-path analysis for remaining work
  4. data-product schemas for external dashboards

Expanded obligations:
  1. Implement per-part status with blocking-dependency identification with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of CursorBench 3.2, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement capability-coverage and integration-health reporting together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement critical-path analysis for remaining work as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's CursorBench
     3.2 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  4. Implement data-product schemas for external dashboards, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.assembly.assembly_dashboard@1
  cap.t20.assembly.assembly_dashboard.describe@1

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

  cap.t20.part.part_submission_gate@1
      if unavailable: use the in-file conservative substitute for
      `part_submission_gate` (documented, slower, lower quality) and set
      `degraded['part_submission_gate']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t08.engine.engine_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `engine_spec_doc` (documented, slower, lower quality) and set
      `degraded['engine_spec_doc']='local'`

  cap.t09.latency.latency_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `latency_spec_doc` (documented, slower, lower quality) and set
      `degraded['latency_spec_doc']='local'`

  cap.t18.eval.eval_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `eval_spec_doc` (documented, slower, lower quality) and set
      `degraded['eval_spec_doc']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - per-part status with blocking-dependency identification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability-coverage and integration-health reporting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - critical-path analysis for remaining work
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - data-product schemas for external dashboards
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.assembly.assembly_dashboard@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0998_assembly_dashboard.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0999-platform-bench

**P0999 · `platform_bench` — Platform Benchmark & SLO Verification** · [spec](PART_SPECS_T20.md#p0999-platform-bench) · [self-contained txt](../prompts/P0999_platform_bench.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0999  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0999 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0999  (49/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Platform Benchmark & SLO Verification
file         : parts/t20_platform/P0999_platform_bench.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.platform_bench
language     : TypeScript 5.7
capability   : cap.t20.platform.platform_bench@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
Measures the platform layer itself.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. API latency, availability and error-rate measurement
  2. SDK overhead measurement across languages
  3. deployment pipeline speed and reliability metrics
  4. SLO-attainment reporting with error budgets

Expanded obligations:
  1. Implement API latency, availability and error-rate measurement together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Zapier AutomationBench — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement SDK overhead measurement across languages as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's CursorBench
     3.2 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  3. Implement deployment pipeline speed and reliability metrics, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement SLO-attainment reporting with error budgets with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.platform.platform_bench@1
  cap.t20.platform.platform_bench.describe@1

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

  cap.t20.assembly.assembly_dashboard@1
      if unavailable: use the in-file conservative substitute for
      `assembly_dashboard` (documented, slower, lower quality) and set
      `degraded['assembly_dashboard']='local'`

  cap.t08.cascade.cascade_stage2_draft@1
      if unavailable: use the in-file conservative substitute for
      `cascade_stage2_draft` (documented, slower, lower quality) and set
      `degraded['cascade_stage2_draft']='local'`

  cap.t09.computation.computation_reuse@1
      if unavailable: use the in-file conservative substitute for
      `computation_reuse` (documented, slower, lower quality) and set
      `degraded['computation_reuse']='local'`

  cap.t18.statistical.statistical_engine@1
      if unavailable: use the in-file conservative substitute for
      `statistical_engine` (documented, slower, lower quality) and set
      `degraded['statistical_engine']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - API latency, availability and error-rate measurement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - SDK overhead measurement across languages
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deployment pipeline speed and reliability metrics
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - SLO-attainment reporting with error budgets
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.platform.platform_bench@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P0999_platform_bench.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p1000-platform-spec-doc

**P1000 · `platform_spec_doc` — Platform Specification, README & Master Index** · [spec](PART_SPECS_T20.md#p1000-platform-spec-doc) · [self-contained txt](../prompts/P1000_platform_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P1000  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P1000 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P1000  (50/50 of tier T20)
tier         : T20 — Platform, SDK, Ops & Distributed Assembly
title        : Platform Specification, README & Master Index
file         : parts/t20_platform/P1000_platform_spec_doc.ts          <-- create exactly this path, nothing else
module       : hyperion.t20.platform.platform_spec_doc
language     : TypeScript 5.7
capability   : cap.t20.platform.platform_spec_doc@1
determinism  : io
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : CursorBench 3.2, Zapier AutomationBench

MISSION
-------
The authoritative top-level document for the whole system.

Tier context:
  Public API, SDKs, deployment, observability, and the assembly/linking
  machinery that fuses 1000 independently authored parts into one binary
  artifact.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. assembly overview with tier and part index
  2. build, deploy and operate instructions verified by execution
  3. guarantee register aggregated from all tiers
  4. drift detection across the entire documentation set

Expanded obligations:
  1. Implement assembly overview with tier and part index as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's CursorBench
     3.2 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement build, deploy and operate instructions verified by execution,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     Zapier AutomationBench, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement guarantee register aggregated from all tiers with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against CursorBench 3.2 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement drift detection across the entire documentation set together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Zapier AutomationBench target reachable; the part
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t20.platform.platform_spec_doc@1
  cap.t20.platform.platform_spec_doc.describe@1

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

  cap.t20.platform.platform_bench@1
      if unavailable: use the in-file conservative substitute for
      `platform_bench` (documented, slower, lower quality) and set
      `degraded['platform_bench']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t08.cascade.cascade_tuning@1
      if unavailable: use the in-file conservative substitute for
      `cascade_tuning` (documented, slower, lower quality) and set
      `degraded['cascade_tuning']='local'`

  cap.t09.async.async_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `async_pipeline` (documented, slower, lower quality) and set
      `degraded['async_pipeline']='local'`

  cap.t18.arc.arc_agi_eval@1
      if unavailable: use the in-file conservative substitute for
      `arc_agi_eval` (documented, slower, lower quality) and set
      `degraded['arc_agi_eval']='local'`

RUNTIME SAFETY OBLIGATION (contract clause C8) — FAIL CLOSED
-----------------------------------------------------------
  Your part performs or enables external effects. Every effect MUST be routed
  through cap.t19.gate.action_filter@1 at CALL TIME (not link time).
  If that capability is absent from the bus you MUST refuse the effect and emit
  OmegaCode 6001. You must NOT fall back to executing the action unfiltered.
  Write at least three tests proving the refusal path, including one that asserts
  no side effect occurred when the gate was missing.

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
   3. [ 600 lines] Core implementation A - assembly overview with tier and part index
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - build, deploy and operate instructions verified by execution
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - guarantee register aggregated from all tiers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - drift detection across the entire documentation set
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

LANGUAGE RULES (TypeScript 5.7)
------------------------------------------------------------------------------
  tests   : vitest-compatible `describe/it` blocks inside the same file behind `if (import.meta.vitest)`
  format  : prettier default + eslint typescript-strict clean
  typing  : `strict: true`, no `any`, exhaustive discriminated unions
  deps    : zero runtime dependencies; Web/Node standard APIs only

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
     exactly (capability == cap.t20.platform.platform_spec_doc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t20_platform/P1000_platform_spec_doc.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
