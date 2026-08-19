# HYPERION-Ω — Worker prompts · T03 · Graph IR, Compiler & Autotuner

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

## PROMPT p0101-ir-core

**P0101 · `ir_core` — Ω-IR Core Data Structures** · [spec](PART_SPECS_T03.md#p0101-ir-core) · [self-contained txt](../prompts/P0101_ir_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0101  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0101 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0101  (1/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Ω-IR Core Data Structures
file         : parts/t03_compiler/P0101_ir_core.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.ir_core
language     : Rust 1.86
capability   : cap.t03.ir.ir_core@1
determinism  : pure
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The SSA-based graph IR that all compilation and optimisation operates on.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. typed SSA with regions, blocks and explicit effect edges
  2. shape/dtype/device/determinism attributes on every value
  3. structural hashing and interning for O(1) equality
  4. verifier catching every malformed-IR class with precise diagnostics

Expanded obligations:
  1. Implement typed SSA with regions, blocks and explicit effect edges, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement shape/dtype/device/determinism attributes on every value with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement structural hashing and interning for O(1) equality together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement verifier catching every malformed-IR class with precise
     diagnostics as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.ir.ir_core@1
  cap.t03.ir.ir_core.describe@1

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

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - typed SSA with regions, blocks and explicit effect edges
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - shape/dtype/device/determinism attributes on every value
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - structural hashing and interning for O(1) equality
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verifier catching every malformed-IR class with precise diagnost
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
     exactly (capability == cap.t03.ir.ir_core@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 10000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0101_ir_core.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0102-ir-builder

**P0102 · `ir_builder` — IR Construction & Tracing Frontend** · [spec](PART_SPECS_T03.md#p0102-ir-builder) · [self-contained txt](../prompts/P0102_ir_builder.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0102  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0102 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0102  (2/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : IR Construction & Tracing Frontend
file         : parts/t03_compiler/P0102_ir_builder.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.ir_builder
language     : Rust 1.86
capability   : cap.t03.ir.ir_builder@1
determinism  : pure
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Captures model code into Ω-IR without behavioural surprises.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tracing with control-flow capture and guard generation
  2. symbolic-shape propagation during capture
  3. side-effect ordering preservation and explicit barriers
  4. trace-vs-eager equivalence differential tests

Expanded obligations:
  1. Implement tracing with control-flow capture and guard generation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement symbolic-shape propagation during capture together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement side-effect ordering preservation and explicit barriers as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement trace-vs-eager equivalence differential tests, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
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
  cap.t03.ir.ir_builder@1
  cap.t03.ir.ir_builder.describe@1

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

  cap.t03.ir.ir_core@1
      if unavailable: use the in-file conservative substitute for `ir_core`
      (documented, slower, lower quality) and set
      `degraded['ir_core']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t02.numa.numa_placement@1
      if unavailable: use the in-file conservative substitute for
      `numa_placement` (documented, slower, lower quality) and set
      `degraded['numa_placement']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - tracing with control-flow capture and guard generation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - symbolic-shape propagation during capture
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - side-effect ordering preservation and explicit barriers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - trace-vs-eager equivalence differential tests
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
     exactly (capability == cap.t03.ir.ir_builder@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 11000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0102_ir_builder.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0103-ir-printer

**P0103 · `ir_printer` — IR Textual Format, Parser & Round-Trip** · [spec](PART_SPECS_T03.md#p0103-ir-printer) · [self-contained txt](../prompts/P0103_ir_printer.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0103  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0103 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0103  (3/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : IR Textual Format, Parser & Round-Trip
file         : parts/t03_compiler/P0103_ir_printer.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.ir_printer
language     : Rust 1.86
capability   : cap.t03.ir.ir_printer@1
determinism  : pure
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Human-readable IR that round-trips exactly, essential for 1000-way
debugging.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. stable textual syntax with attribute pretty-printing
  2. parser accepting the full grammar with error recovery
  3. round-trip fidelity property test over random IR
  4. diff-friendly canonical ordering

Expanded obligations:
  1. Implement stable textual syntax with attribute pretty-printing together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement parser accepting the full grammar with error recovery as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement round-trip fidelity property test over random IR, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement diff-friendly canonical ordering with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Correctness here is
     what makes the tier's SWE-bench Verified target reachable; the part
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.ir.ir_printer@1
  cap.t03.ir.ir_printer.describe@1

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

  cap.t03.ir.ir_builder@1
      if unavailable: use the in-file conservative substitute for
      `ir_builder` (documented, slower, lower quality) and set
      `degraded['ir_builder']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t02.kernel.kernel_fusion_rules@1
      if unavailable: use the in-file conservative substitute for
      `kernel_fusion_rules` (documented, slower, lower quality) and set
      `degraded['kernel_fusion_rules']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - stable textual syntax with attribute pretty-printing
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - parser accepting the full grammar with error recovery
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - round-trip fidelity property test over random IR
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - diff-friendly canonical ordering
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
     exactly (capability == cap.t03.ir.ir_printer@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 12000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0103_ir_printer.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0104-pass-manager

**P0104 · `pass_manager` — Pass Manager & Optimisation Pipelines** · [spec](PART_SPECS_T03.md#p0104-pass-manager) · [self-contained txt](../prompts/P0104_pass_manager.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0104  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0104 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0104  (4/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Pass Manager & Optimisation Pipelines
file         : parts/t03_compiler/P0104_pass_manager.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.pass_manager
language     : Rust 1.86
capability   : cap.t03.pass.pass_manager@1
determinism  : pure
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Orchestrates passes with dependency, invalidation and instrumentation
support.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. analysis caching with precise invalidation
  2. pipeline description language and preset pipelines
  3. per-pass timing, IR-size and diagnostic capture
  4. pass-ordering search harness for pipeline tuning

Expanded obligations:
  1. Implement analysis caching with precise invalidation as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement pipeline description language and preset pipelines, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement per-pass timing, IR-size and diagnostic capture with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement pass-ordering search harness for pipeline tuning together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.pass.pass_manager@1
  cap.t03.pass.pass_manager.describe@1

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

  cap.t03.ir.ir_printer@1
      if unavailable: use the in-file conservative substitute for
      `ir_printer` (documented, slower, lower quality) and set
      `degraded['ir_printer']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t02.sparse.sparse_attention_kernels@1
      if unavailable: use the in-file conservative substitute for
      `sparse_attention_kernels` (documented, slower, lower quality) and set
      `degraded['sparse_attention_kernels']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - analysis caching with precise invalidation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - pipeline description language and preset pipelines
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-pass timing, IR-size and diagnostic capture
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - pass-ordering search harness for pipeline tuning
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
     exactly (capability == cap.t03.pass.pass_manager@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 13000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0104_pass_manager.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0105-shape-inference

**P0105 · `shape_inference` — Symbolic Shape Inference & Constraint Solver** · [spec](PART_SPECS_T03.md#p0105-shape-inference) · [self-contained txt](../prompts/P0105_shape_inference.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0105  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0105 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0105  (5/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Symbolic Shape Inference & Constraint Solver
file         : parts/t03_compiler/P0105_shape_inference.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.shape_inference
language     : Rust 1.86
capability   : cap.t03.shape.shape_inference@1
determinism  : pure
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Resolves dynamic shapes to a small set of specialised plans.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. symbolic dimension algebra with guard accumulation
  2. constraint solving for divisibility and bounds
  3. shape-bucket selection minimising padding and recompiles
  4. unsat diagnosis pointing at the offending op

Expanded obligations:
  1. Implement symbolic dimension algebra with guard accumulation, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement constraint solving for divisibility and bounds with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement shape-bucket selection minimising padding and recompiles
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement unsat diagnosis pointing at the offending op as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.

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
  cap.t03.shape.shape_inference@1
  cap.t03.shape.shape_inference.describe@1

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

  cap.t03.pass.pass_manager@1
      if unavailable: use the in-file conservative substitute for
      `pass_manager` (documented, slower, lower quality) and set
      `degraded['pass_manager']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t02.tensor.tensor_core_util@1
      if unavailable: use the in-file conservative substitute for
      `tensor_core_util` (documented, slower, lower quality) and set
      `degraded['tensor_core_util']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - symbolic dimension algebra with guard accumulation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - constraint solving for divisibility and bounds
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - shape-bucket selection minimising padding and recompiles
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - unsat diagnosis pointing at the offending op
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
     exactly (capability == cap.t03.shape.shape_inference@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 14000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0105_shape_inference.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0106-dtype-promotion

**P0106 · `dtype_promotion` — Precision Assignment & Mixed-Precision Planner** · [spec](PART_SPECS_T03.md#p0106-dtype-promotion) · [self-contained txt](../prompts/P0106_dtype_promotion.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0106  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0106 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0106  (6/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Precision Assignment & Mixed-Precision Planner
file         : parts/t03_compiler/P0106_dtype_promotion.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.dtype_promotion
language     : Rust 1.86
capability   : cap.t03.dtype.dtype_promotion@1
determinism  : pure
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Chooses the cheapest precision per op that still meets the accuracy
contract.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. sensitivity analysis via perturbation and gradient proxies
  2. ILP/greedy solver over the precision-assignment space
  3. accuracy constraint verification against a reference run
  4. measured speedup at certified accuracy parity

Expanded obligations:
  1. Implement sensitivity analysis via perturbation and gradient proxies
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement ILP/greedy solver over the precision-assignment space together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement accuracy constraint verification against a reference run as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured speedup at certified accuracy parity, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.dtype.dtype_promotion@1
  cap.t03.dtype.dtype_promotion.describe@1

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

  cap.t03.shape.shape_inference@1
      if unavailable: use the in-file conservative substitute for
      `shape_inference` (documented, slower, lower quality) and set
      `degraded['shape_inference']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t02.attn.attn_flash_bwd@1
      if unavailable: use the in-file conservative substitute for
      `attn_flash_bwd` (documented, slower, lower quality) and set
      `degraded['attn_flash_bwd']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - sensitivity analysis via perturbation and gradient proxies
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - ILP/greedy solver over the precision-assignment space
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accuracy constraint verification against a reference run
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured speedup at certified accuracy parity
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
     exactly (capability == cap.t03.dtype.dtype_promotion@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 15000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0106_dtype_promotion.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0107-algebraic-rewrite

**P0107 · `algebraic_rewrite` — Algebraic Simplification & Rewrite Engine** · [spec](PART_SPECS_T03.md#p0107-algebraic-rewrite) · [self-contained txt](../prompts/P0107_algebraic_rewrite.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0107  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0107 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0107  (7/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Algebraic Simplification & Rewrite Engine
file         : parts/t03_compiler/P0107_algebraic_rewrite.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.algebraic_rewrite
language     : Rust 1.86
capability   : cap.t03.algebraic.algebraic_rewrite@1
determinism  : pure
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The rule-based optimiser: hundreds of semantics-preserving rewrites.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. e-graph saturation with cost-based extraction
  2. rule library covering linear algebra, softmax, norms and gating identities
  3. confluence/termination handling with iteration limits
  4. semantics-preservation tests per rule

Expanded obligations:
  1. Implement e-graph saturation with cost-based extraction together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement rule library covering linear algebra, softmax, norms and
     gating identities as a first-class, fully realised mechanism. No stub,
     no `NotImplementedError`, no configuration flag whose default disables
     it. Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement confluence/termination handling with iteration limits, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement semantics-preservation tests per rule with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.algebraic.algebraic_rewrite@1
  cap.t03.algebraic.algebraic_rewrite.describe@1

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

  cap.t03.dtype.dtype_promotion@1
      if unavailable: use the in-file conservative substitute for
      `dtype_promotion` (documented, slower, lower quality) and set
      `degraded['dtype_promotion']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t02.reduction.reduction_kernels@1
      if unavailable: use the in-file conservative substitute for
      `reduction_kernels` (documented, slower, lower quality) and set
      `degraded['reduction_kernels']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - e-graph saturation with cost-based extraction
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - rule library covering linear algebra, softmax, norms and gating 
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - confluence/termination handling with iteration limits
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - semantics-preservation tests per rule
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
     exactly (capability == cap.t03.algebraic.algebraic_rewrite@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 16000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0107_algebraic_rewrite.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0108-fusion-pass

**P0108 · `fusion_pass` — Operator Fusion Pass** · [spec](PART_SPECS_T03.md#p0108-fusion-pass) · [self-contained txt](../prompts/P0108_fusion_pass.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0108  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0108 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0108  (8/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Operator Fusion Pass
file         : parts/t03_compiler/P0108_fusion_pass.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.fusion_pass
language     : Rust 1.86
capability   : cap.t03.fusion.fusion_pass@1
determinism  : pure
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Merges ops into single-pass kernels using the T02 legality rules.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fusion group formation with cut-based partitioning
  2. profitability model from arithmetic intensity and memory traffic
  3. recomputation-vs-materialisation decisions
  4. measured memory-traffic reduction on the benchmark corpus

Expanded obligations:
  1. Implement fusion group formation with cut-based partitioning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement profitability model from arithmetic intensity and memory
     traffic, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement recomputation-vs-materialisation decisions with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured memory-traffic reduction on the benchmark corpus
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.fusion.fusion_pass@1
  cap.t03.fusion.fusion_pass.describe@1

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

  cap.t03.algebraic.algebraic_rewrite@1
      if unavailable: use the in-file conservative substitute for
      `algebraic_rewrite` (documented, slower, lower quality) and set
      `degraded['algebraic_rewrite']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t02.rng.rng_kernels@1
      if unavailable: use the in-file conservative substitute for
      `rng_kernels` (documented, slower, lower quality) and set
      `degraded['rng_kernels']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - fusion group formation with cut-based partitioning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - profitability model from arithmetic intensity and memory traffic
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - recomputation-vs-materialisation decisions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured memory-traffic reduction on the benchmark corpus
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
     exactly (capability == cap.t03.fusion.fusion_pass@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 17000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0108_fusion_pass.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0109-layout-assignment

**P0109 · `layout_assignment` — Layout Assignment & Relayout Minimisation** · [spec](PART_SPECS_T03.md#p0109-layout-assignment) · [self-contained txt](../prompts/P0109_layout_assignment.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0109  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0109 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0109  (9/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Layout Assignment & Relayout Minimisation
file         : parts/t03_compiler/P0109_layout_assignment.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.layout_assignment
language     : Rust 1.86
capability   : cap.t03.layout.layout_assignment@1
determinism  : pure
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Picks tensor layouts globally to eliminate transposes.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. layout constraint propagation across the whole graph
  2. min-cut formulation for relayout placement
  3. blocked/padded layout selection for tensor cores
  4. count of eliminated relayouts as the gate metric

Expanded obligations:
  1. Implement layout constraint propagation across the whole graph, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement min-cut formulation for relayout placement with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement blocked/padded layout selection for tensor cores together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement count of eliminated relayouts as the gate metric as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.layout.layout_assignment@1
  cap.t03.layout.layout_assignment.describe@1

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

  cap.t03.fusion.fusion_pass@1
      if unavailable: use the in-file conservative substitute for
      `fusion_pass` (documented, slower, lower quality) and set
      `degraded['fusion_pass']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t02.simd.simd_cpu@1
      if unavailable: use the in-file conservative substitute for `simd_cpu`
      (documented, slower, lower quality) and set
      `degraded['simd_cpu']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - layout constraint propagation across the whole graph
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - min-cut formulation for relayout placement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blocked/padded layout selection for tensor cores
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - count of eliminated relayouts as the gate metric
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
     exactly (capability == cap.t03.layout.layout_assignment@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 18000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0109_layout_assignment.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0110-memory-planner

**P0110 · `memory_planner` — Static Memory Planner & Liveness Allocator** · [spec](PART_SPECS_T03.md#p0110-memory-planner) · [self-contained txt](../prompts/P0110_memory_planner.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0110  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0110 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0110  (10/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Static Memory Planner & Liveness Allocator
file         : parts/t03_compiler/P0110_memory_planner.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.memory_planner
language     : Rust 1.86
capability   : cap.t03.memory.memory_planner@1
determinism  : pure
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Assigns every buffer an offset with minimal peak memory.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. liveness analysis with interval graph construction
  2. best-fit-by-size allocation with proven bounds
  3. in-place and aliasing opportunity detection
  4. peak-memory reduction versus naive allocation

Expanded obligations:
  1. Implement liveness analysis with interval graph construction with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement best-fit-by-size allocation with proven bounds together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement in-place and aliasing opportunity detection as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement peak-memory reduction versus naive allocation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.memory.memory_planner@1
  cap.t03.memory.memory_planner.describe@1

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

  cap.t03.layout.layout_assignment@1
      if unavailable: use the in-file conservative substitute for
      `layout_assignment` (documented, slower, lower quality) and set
      `degraded['layout_assignment']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t02.emulation.emulation_reference@1
      if unavailable: use the in-file conservative substitute for
      `emulation_reference` (documented, slower, lower quality) and set
      `degraded['emulation_reference']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - liveness analysis with interval graph construction
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - best-fit-by-size allocation with proven bounds
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - in-place and aliasing opportunity detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - peak-memory reduction versus naive allocation
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
     exactly (capability == cap.t03.memory.memory_planner@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 19000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0110_memory_planner.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0111-rematerialisation

**P0111 · `rematerialisation` — Activation Rematerialisation Planner** · [spec](PART_SPECS_T03.md#p0111-rematerialisation) · [self-contained txt](../prompts/P0111_rematerialisation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0111  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0111 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0111  (11/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Activation Rematerialisation Planner
file         : parts/t03_compiler/P0111_rematerialisation.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.rematerialisation
language     : Rust 1.86
capability   : cap.t03.rematerialisat.rematerialisation@1
determinism  : pure
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Trades compute for memory optimally during training and long-context
inference.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cost-model-driven checkpoint selection (dynamic programming)
  2. segment-based recompute schedules with nested checkpoints
  3. memory-budget-constrained optimisation
  4. measured memory/compute Pareto frontier

Expanded obligations:
  1. Implement cost-model-driven checkpoint selection (dynamic programming)
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement segment-based recompute schedules with nested checkpoints as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement memory-budget-constrained optimisation, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured memory/compute Pareto frontier with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.rematerialisat.rematerialisation@1
  cap.t03.rematerialisat.rematerialisation.describe@1

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

  cap.t03.memory.memory_planner@1
      if unavailable: use the in-file conservative substitute for
      `memory_planner` (documented, slower, lower quality) and set
      `degraded['memory_planner']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t02.kernel.kernel_codegen_rt@1
      if unavailable: use the in-file conservative substitute for
      `kernel_codegen_rt` (documented, slower, lower quality) and set
      `degraded['kernel_codegen_rt']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - cost-model-driven checkpoint selection (dynamic programming)
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - segment-based recompute schedules with nested checkpoints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - memory-budget-constrained optimisation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured memory/compute Pareto frontier
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
     exactly (capability == cap.t03.rematerialisat.rematerialisation@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 20000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0111_rematerialisation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0112-scheduler-pass

**P0112 · `scheduler_pass` — Instruction Scheduling & Overlap Pass** · [spec](PART_SPECS_T03.md#p0112-scheduler-pass) · [self-contained txt](../prompts/P0112_scheduler_pass.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0112  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0112 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0112  (12/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Instruction Scheduling & Overlap Pass
file         : parts/t03_compiler/P0112_scheduler_pass.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.scheduler_pass
language     : Rust 1.86
capability   : cap.t03.scheduler.scheduler_pass@1
determinism  : pure
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Orders operations to hide latency and maximise concurrency.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. list scheduling with a machine model of latencies and ports
  2. communication/compute overlap insertion
  3. critical-path shortening with resource constraints
  4. achieved-overlap metric versus theoretical ideal

Expanded obligations:
  1. Implement list scheduling with a machine model of latencies and ports as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement communication/compute overlap insertion, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement critical-path shortening with resource constraints with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement achieved-overlap metric versus theoretical ideal together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.scheduler.scheduler_pass@1
  cap.t03.scheduler.scheduler_pass.describe@1

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

  cap.t03.rematerialisat.rematerialisation@1
      if unavailable: use the in-file conservative substitute for
      `rematerialisation` (documented, slower, lower quality) and set
      `degraded['rematerialisation']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t02.micro.micro_opt_catalog@1
      if unavailable: use the in-file conservative substitute for
      `micro_opt_catalog` (documented, slower, lower quality) and set
      `degraded['micro_opt_catalog']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - list scheduling with a machine model of latencies and ports
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - communication/compute overlap insertion
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - critical-path shortening with resource constraints
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - achieved-overlap metric versus theoretical ideal
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
     exactly (capability == cap.t03.scheduler.scheduler_pass@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 21000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0112_scheduler_pass.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0113-parallel-partition

**P0113 · `parallel_partition` — Automatic Parallelism Partitioner** · [spec](PART_SPECS_T03.md#p0113-parallel-partition) · [self-contained txt](../prompts/P0113_parallel_partition.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0113  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0113 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0113  (13/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Automatic Parallelism Partitioner
file         : parts/t03_compiler/P0113_parallel_partition.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.parallel_partition
language     : Rust 1.86
capability   : cap.t03.parallel.parallel_partition@1
determinism  : pure
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Derives tensor/pipeline/expert/sequence parallel plans automatically.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. sharding-propagation solver over annotated inputs and outputs
  2. cost model including collective volume and bubble time
  3. hybrid-plan search across 4 parallelism axes
  4. plan quality versus hand-tuned expert baselines

Expanded obligations:
  1. Implement sharding-propagation solver over annotated inputs and outputs,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement cost model including collective volume and bubble time with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement hybrid-plan search across 4 parallelism axes together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement plan quality versus hand-tuned expert baselines as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.parallel.parallel_partition@1
  cap.t03.parallel.parallel_partition.describe@1

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

  cap.t03.scheduler.scheduler_pass@1
      if unavailable: use the in-file conservative substitute for
      `scheduler_pass` (documented, slower, lower quality) and set
      `degraded['scheduler_pass']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t02.attn.attn_flash_fwd@1
      if unavailable: use the in-file conservative substitute for
      `attn_flash_fwd` (documented, slower, lower quality) and set
      `degraded['attn_flash_fwd']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - sharding-propagation solver over annotated inputs and outputs
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost model including collective volume and bubble time
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hybrid-plan search across 4 parallelism axes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - plan quality versus hand-tuned expert baselines
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
     exactly (capability == cap.t03.parallel.parallel_partition@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 22000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0113_parallel_partition.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0114-pipeline-planner

**P0114 · `pipeline_planner` — Pipeline Parallel Schedule Synthesiser** · [spec](PART_SPECS_T03.md#p0114-pipeline-planner) · [self-contained txt](../prompts/P0114_pipeline_planner.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0114  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0114 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0114  (14/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Pipeline Parallel Schedule Synthesiser
file         : parts/t03_compiler/P0114_pipeline_planner.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.pipeline_planner
language     : Rust 1.86
capability   : cap.t03.pipeline.pipeline_planner@1
determinism  : pure
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Generates bubble-minimal pipeline schedules.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. 1F1B, interleaved and zero-bubble schedule generation
  2. stage-balancing partitioner using measured per-layer costs
  3. activation-memory accounting per schedule
  4. bubble-fraction measurement and target enforcement

Expanded obligations:
  1. Implement 1F1B, interleaved and zero-bubble schedule generation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement stage-balancing partitioner using measured per-layer costs
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement activation-memory accounting per schedule as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement bubble-fraction measurement and target enforcement, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
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
  cap.t03.pipeline.pipeline_planner@1
  cap.t03.pipeline.pipeline_planner.describe@1

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

  cap.t03.parallel.parallel_partition@1
      if unavailable: use the in-file conservative substitute for
      `parallel_partition` (documented, slower, lower quality) and set
      `degraded['parallel_partition']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t02.elementwise.elementwise_fusion@1
      if unavailable: use the in-file conservative substitute for
      `elementwise_fusion` (documented, slower, lower quality) and set
      `degraded['elementwise_fusion']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - 1F1B, interleaved and zero-bubble schedule generation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - stage-balancing partitioner using measured per-layer costs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - activation-memory accounting per schedule
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - bubble-fraction measurement and target enforcement
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
     exactly (capability == cap.t03.pipeline.pipeline_planner@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 23000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0114_pipeline_planner.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0115-collective-insertion

**P0115 · `collective_insertion` — Collective Communication Insertion & Fusion** · [spec](PART_SPECS_T03.md#p0115-collective-insertion) · [self-contained txt](../prompts/P0115_collective_insertion.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0115  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0115 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0115  (15/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Collective Communication Insertion & Fusion
file         : parts/t03_compiler/P0115_collective_insertion.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.collective_insertion
language     : Rust 1.86
capability   : cap.t03.collective.collective_insertion@1
determinism  : pure
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Places, fuses and overlaps every collective operation.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. all-reduce/all-gather/reduce-scatter insertion from sharding specs
  2. collective fusion with bucketing to amortise latency
  3. overlap with compute via async handles and dependency edges
  4. communication-volume reduction measurement

Expanded obligations:
  1. Implement all-reduce/all-gather/reduce-scatter insertion from sharding
     specs together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement collective fusion with bucketing to amortise latency as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement overlap with compute via async handles and dependency edges,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement communication-volume reduction measurement with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.collective.collective_insertion@1
  cap.t03.collective.collective_insertion.describe@1

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

  cap.t03.pipeline.pipeline_planner@1
      if unavailable: use the in-file conservative substitute for
      `pipeline_planner` (documented, slower, lower quality) and set
      `degraded['pipeline_planner']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t02.transpose.transpose_layout@1
      if unavailable: use the in-file conservative substitute for
      `transpose_layout` (documented, slower, lower quality) and set
      `degraded['transpose_layout']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - all-reduce/all-gather/reduce-scatter insertion from sharding spe
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - collective fusion with bucketing to amortise latency
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - overlap with compute via async handles and dependency edges
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - communication-volume reduction measurement
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
     exactly (capability == cap.t03.collective.collective_insertion@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 24000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0115_collective_insertion.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0116-autotuner-core

**P0116 · `autotuner_core` — Autotuning Search Engine** · [spec](PART_SPECS_T03.md#p0116-autotuner-core) · [self-contained txt](../prompts/P0116_autotuner_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0116  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0116 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0116  (16/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Autotuning Search Engine
file         : parts/t03_compiler/P0116_autotuner_core.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.autotuner_core
language     : Rust 1.86
capability   : cap.t03.autotuner.autotuner_core@1
determinism  : pure
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Finds the best kernel configuration per shape with a small measurement
budget.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. search over tile/stage/precision spaces with pruning by legality and cost model
  2. bayesian/bandit search with transfer from similar shapes
  3. measurement harness with noise handling and early stopping
  4. tuning-budget-vs-quality curves

Expanded obligations:
  1. Implement search over tile/stage/precision spaces with pruning by
     legality and cost model as a first-class, fully realised mechanism. No
     stub, no `NotImplementedError`, no configuration flag whose default
     disables it. Its state must be reportable through `describe()` and it
     must be exercised by at least eight in-file tests, including one that
     fails loudly if the mechanism is silently bypassed. This mechanism sits
     on the critical path of SWE-bench Verified, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  2. Implement bayesian/bandit search with transfer from similar shapes, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement measurement harness with noise handling and early stopping
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement tuning-budget-vs-quality curves together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. This mechanism sits on the critical
     path of SWE-bench Verified, so its p99 latency assertion is part of the
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
  cap.t03.autotuner.autotuner_core@1
  cap.t03.autotuner.autotuner_core.describe@1

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

  cap.t03.collective.collective_insertion@1
      if unavailable: use the in-file conservative substitute for
      `collective_insertion` (documented, slower, lower quality) and set
      `degraded['collective_insertion']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t02.cache.cache_blocking@1
      if unavailable: use the in-file conservative substitute for
      `cache_blocking` (documented, slower, lower quality) and set
      `degraded['cache_blocking']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - search over tile/stage/precision spaces with pruning by legality
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - bayesian/bandit search with transfer from similar shapes
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - measurement harness with noise handling and early stopping
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - tuning-budget-vs-quality curves
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
     exactly (capability == cap.t03.autotuner.autotuner_core@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 25000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0116_autotuner_core.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0117-cost-model-learned

**P0117 · `cost_model_learned` — Learned Cost Model** · [spec](PART_SPECS_T03.md#p0117-cost-model-learned) · [self-contained txt](../prompts/P0117_cost_model_learned.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0117  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0117 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0117  (17/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Learned Cost Model
file         : parts/t03_compiler/P0117_cost_model_learned.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.cost_model_learned
language     : Rust 1.86
capability   : cap.t03.cost.cost_model_learned@1
determinism  : pure
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Predicts kernel runtime accurately enough to skip most measurements.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. feature extraction from IR and target description
  2. regression model with uncertainty estimates for search guidance
  3. online updating from production measurements
  4. prediction-error target under 8% on held-out shapes

Expanded obligations:
  1. Implement feature extraction from IR and target description, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement regression model with uncertainty estimates for search
     guidance with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement online updating from production measurements together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement prediction-error target under 8% on held-out shapes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.cost.cost_model_learned@1
  cap.t03.cost.cost_model_learned.describe@1

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

  cap.t03.autotuner.autotuner_core@1
      if unavailable: use the in-file conservative substitute for
      `autotuner_core` (documented, slower, lower quality) and set
      `degraded['autotuner_core']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t02.profiler.profiler_hooks@1
      if unavailable: use the in-file conservative substitute for
      `profiler_hooks` (documented, slower, lower quality) and set
      `degraded['profiler_hooks']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - feature extraction from IR and target description
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - regression model with uncertainty estimates for search guidance
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - online updating from production measurements
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - prediction-error target under 8% on held-out shapes
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
     exactly (capability == cap.t03.cost.cost_model_learned@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 26000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0117_cost_model_learned.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0118-codegen-gpu

**P0118 · `codegen_gpu` — Accelerator Code Generator** · [spec](PART_SPECS_T03.md#p0118-codegen-gpu) · [self-contained txt](../prompts/P0118_codegen_gpu.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0118  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0118 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0118  (18/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Accelerator Code Generator
file         : parts/t03_compiler/P0118_codegen_gpu.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.codegen_gpu
language     : Rust 1.86
capability   : cap.t03.codegen.codegen_gpu@1
determinism  : pure
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Emits high-performance device code from scheduled Ω-IR.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tile-level IR lowering with explicit memory-hierarchy staging
  2. async-copy/barrier/pipeline emission and register allocation hints
  3. vendor-neutral backend interface with two concrete targets
  4. generated-vs-handwritten performance comparison

Expanded obligations:
  1. Implement tile-level IR lowering with explicit memory-hierarchy staging
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement async-copy/barrier/pipeline emission and register allocation
     hints together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement vendor-neutral backend interface with two concrete targets as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement generated-vs-handwritten performance comparison, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.codegen.codegen_gpu@1
  cap.t03.codegen.codegen_gpu.describe@1

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

  cap.t03.cost.cost_model_learned@1
      if unavailable: use the in-file conservative substitute for
      `cost_model_learned` (documented, slower, lower quality) and set
      `degraded['cost_model_learned']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t02.error.error_correction@1
      if unavailable: use the in-file conservative substitute for
      `error_correction` (documented, slower, lower quality) and set
      `degraded['error_correction']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - tile-level IR lowering with explicit memory-hierarchy staging
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - async-copy/barrier/pipeline emission and register allocation hin
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - vendor-neutral backend interface with two concrete targets
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - generated-vs-handwritten performance comparison
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
     exactly (capability == cap.t03.codegen.codegen_gpu@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 27000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0118_codegen_gpu.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0119-codegen-cpu

**P0119 · `codegen_cpu` — CPU Code Generator** · [spec](PART_SPECS_T03.md#p0119-codegen-cpu) · [self-contained txt](../prompts/P0119_codegen_cpu.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0119  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0119 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0119  (19/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : CPU Code Generator
file         : parts/t03_compiler/P0119_codegen_cpu.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.codegen_cpu
language     : Rust 1.86
capability   : cap.t03.codegen.codegen_cpu@1
determinism  : pure
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Vectorised CPU codegen for small-batch, edge and reference execution.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. loop vectorisation with ISA-specific intrinsic selection
  2. cache blocking and prefetch insertion from the machine model
  3. multi-threading with deterministic work partitioning
  4. efficiency versus tuned BLAS baselines

Expanded obligations:
  1. Implement loop vectorisation with ISA-specific intrinsic selection
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement cache blocking and prefetch insertion from the machine model
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement multi-threading with deterministic work partitioning, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement efficiency versus tuned BLAS baselines with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.codegen.codegen_cpu@1
  cap.t03.codegen.codegen_cpu.describe@1

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

  cap.t03.codegen.codegen_gpu@1
      if unavailable: use the in-file conservative substitute for
      `codegen_gpu` (documented, slower, lower quality) and set
      `degraded['codegen_gpu']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t02.kernel.kernel_bench_suite@1
      if unavailable: use the in-file conservative substitute for
      `kernel_bench_suite` (documented, slower, lower quality) and set
      `degraded['kernel_bench_suite']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - loop vectorisation with ISA-specific intrinsic selection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cache blocking and prefetch insertion from the machine model
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - multi-threading with deterministic work partitioning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - efficiency versus tuned BLAS baselines
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
     exactly (capability == cap.t03.codegen.codegen_cpu@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 28000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0119_codegen_cpu.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0120-jit-cache-compiler

**P0120 · `jit_cache_compiler` — Compilation Cache & Warm Start** · [spec](PART_SPECS_T03.md#p0120-jit-cache-compiler) · [self-contained txt](../prompts/P0120_jit_cache_compiler.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0120  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0120 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0120  (20/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Compilation Cache & Warm Start
file         : parts/t03_compiler/P0120_jit_cache_compiler.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.jit_cache_compiler
language     : Rust 1.86
capability   : cap.t03.jit.jit_cache_compiler@1
determinism  : pure
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Never compiles the same thing twice, across processes and machines.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. content-addressed cache keyed by IR hash + target + flags
  2. shared cache protocol safe for concurrent writers
  3. profile-guided precompilation of the hot shape set
  4. cold-start compile-time reduction measurement

Expanded obligations:
  1. Implement content-addressed cache keyed by IR hash + target + flags as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement shared cache protocol safe for concurrent writers, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement profile-guided precompilation of the hot shape set with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement cold-start compile-time reduction measurement together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.jit.jit_cache_compiler@1
  cap.t03.jit.jit_cache_compiler.describe@1

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

  cap.t03.codegen.codegen_cpu@1
      if unavailable: use the in-file conservative substitute for
      `codegen_cpu` (documented, slower, lower quality) and set
      `degraded['codegen_cpu']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t02.gemm.gemm_sparse@1
      if unavailable: use the in-file conservative substitute for
      `gemm_sparse` (documented, slower, lower quality) and set
      `degraded['gemm_sparse']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - content-addressed cache keyed by IR hash + target + flags
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - shared cache protocol safe for concurrent writers
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - profile-guided precompilation of the hot shape set
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cold-start compile-time reduction measurement
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
     exactly (capability == cap.t03.jit.jit_cache_compiler@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 29000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0120_jit_cache_compiler.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0121-guard-specialise

**P0121 · `guard_specialise` — Guarded Specialisation & Recompilation Policy** · [spec](PART_SPECS_T03.md#p0121-guard-specialise) · [self-contained txt](../prompts/P0121_guard_specialise.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0121  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0121 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0121  (21/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Guarded Specialisation & Recompilation Policy
file         : parts/t03_compiler/P0121_guard_specialise.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.guard_specialise
language     : Rust 1.86
capability   : cap.t03.guard.guard_specialise@1
determinism  : pure
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Specialises aggressively while staying correct under shape/flag changes.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. guard generation, minimisation and cheap runtime evaluation
  2. specialisation-cache with LRU and recompile-storm prevention
  3. deoptimisation path preserving semantics
  4. guard-overhead measurement under 1% of step time

Expanded obligations:
  1. Implement guard generation, minimisation and cheap runtime evaluation,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement specialisation-cache with LRU and recompile-storm prevention
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement deoptimisation path preserving semantics together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement guard-overhead measurement under 1% of step time as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.guard.guard_specialise@1
  cap.t03.guard.guard_specialise.describe@1

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

  cap.t03.jit.jit_cache_compiler@1
      if unavailable: use the in-file conservative substitute for
      `jit_cache_compiler` (documented, slower, lower quality) and set
      `degraded['jit_cache_compiler']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t02.softmax.softmax_norm@1
      if unavailable: use the in-file conservative substitute for
      `softmax_norm` (documented, slower, lower quality) and set
      `degraded['softmax_norm']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - guard generation, minimisation and cheap runtime evaluation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - specialisation-cache with LRU and recompile-storm prevention
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deoptimisation path preserving semantics
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - guard-overhead measurement under 1% of step time
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
     exactly (capability == cap.t03.guard.guard_specialise@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 30000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0121_guard_specialise.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0122-kernel-selection

**P0122 · `kernel_selection` — Global Kernel Selection Optimiser** · [spec](PART_SPECS_T03.md#p0122-kernel-selection) · [self-contained txt](../prompts/P0122_kernel_selection.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0122  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0122 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0122  (22/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Global Kernel Selection Optimiser
file         : parts/t03_compiler/P0122_kernel_selection.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.kernel_selection
language     : Rust 1.86
capability   : cap.t03.kernel.kernel_selection@1
determinism  : pure
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Chooses kernels jointly rather than greedily, accounting for layout
coupling.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. joint selection formulated over the layout/precision/kernel product space
  2. beam search with cost-model pruning
  3. constraint handling for determinism and accuracy modes
  4. end-to-end gain versus greedy selection

Expanded obligations:
  1. Implement joint selection formulated over the layout/precision/kernel
     product space with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement beam search with cost-model pruning together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement constraint handling for determinism and accuracy modes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement end-to-end gain versus greedy selection, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.kernel.kernel_selection@1
  cap.t03.kernel.kernel_selection.describe@1

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

  cap.t03.guard.guard_specialise@1
      if unavailable: use the in-file conservative substitute for
      `guard_specialise` (documented, slower, lower quality) and set
      `degraded['guard_specialise']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t02.gather.gather_scatter@1
      if unavailable: use the in-file conservative substitute for
      `gather_scatter` (documented, slower, lower quality) and set
      `degraded['gather_scatter']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - joint selection formulated over the layout/precision/kernel prod
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - beam search with cost-model pruning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - constraint handling for determinism and accuracy modes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - end-to-end gain versus greedy selection
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
     exactly (capability == cap.t03.kernel.kernel_selection@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 31000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0122_kernel_selection.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0123-graph-partition-device

**P0123 · `graph_partition_device` — Device Placement & Graph Partitioning** · [spec](PART_SPECS_T03.md#p0123-graph-partition-device) · [self-contained txt](../prompts/P0123_graph_partition_device.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0123  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0123 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0123  (23/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Device Placement & Graph Partitioning
file         : parts/t03_compiler/P0123_graph_partition_device.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.graph_partition_device
language     : Rust 1.86
capability   : cap.t03.graph.graph_partition_device@1
determinism  : pure
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Assigns subgraphs to heterogeneous devices under memory and bandwidth
limits.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-constraint partitioning with communication minimisation
  2. heterogeneous-device cost modelling
  3. memory-feasibility checking with rematerialisation coupling
  4. placement quality versus exhaustive search on small graphs

Expanded obligations:
  1. Implement multi-constraint partitioning with communication minimisation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement heterogeneous-device cost modelling as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement memory-feasibility checking with rematerialisation coupling,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement placement quality versus exhaustive search on small graphs
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.graph.graph_partition_device@1
  cap.t03.graph.graph_partition_device.describe@1

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

  cap.t03.kernel.kernel_selection@1
      if unavailable: use the in-file conservative substitute for
      `kernel_selection` (documented, slower, lower quality) and set
      `degraded['kernel_selection']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t02.async.async_copy@1
      if unavailable: use the in-file conservative substitute for
      `async_copy` (documented, slower, lower quality) and set
      `degraded['async_copy']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - multi-constraint partitioning with communication minimisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - heterogeneous-device cost modelling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - memory-feasibility checking with rematerialisation coupling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - placement quality versus exhaustive search on small graphs
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
     exactly (capability == cap.t03.graph.graph_partition_device@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 32000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0123_graph_partition_device.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0124-dynamic-shapes

**P0124 · `dynamic_shapes` — Dynamic Shape Execution Strategy** · [spec](PART_SPECS_T03.md#p0124-dynamic-shapes) · [self-contained txt](../prompts/P0124_dynamic_shapes.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0124  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0124 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0124  (24/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Dynamic Shape Execution Strategy
file         : parts/t03_compiler/P0124_dynamic_shapes.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.dynamic_shapes
language     : Rust 1.86
capability   : cap.t03.dynamic.dynamic_shapes@1
determinism  : pure
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Handles unbounded shape variety with bounded compilation cost.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. bucketing policy with padding-cost/recompile-cost tradeoff
  2. fully dynamic fallback kernels with acceptable efficiency
  3. shape-distribution learning from production traces
  4. tail-latency impact measurement

Expanded obligations:
  1. Implement bucketing policy with padding-cost/recompile-cost tradeoff as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement fully dynamic fallback kernels with acceptable efficiency, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement shape-distribution learning from production traces with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement tail-latency impact measurement together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Correctness here is what makes the
     tier's SWE-bench Verified target reachable; the part therefore ships a
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
  cap.t03.dynamic.dynamic_shapes@1
  cap.t03.dynamic.dynamic_shapes.describe@1

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

  cap.t03.graph.graph_partition_device@1
      if unavailable: use the in-file conservative substitute for
      `graph_partition_device` (documented, slower, lower quality) and set
      `degraded['graph_partition_device']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t02.roofline.roofline_model@1
      if unavailable: use the in-file conservative substitute for
      `roofline_model` (documented, slower, lower quality) and set
      `degraded['roofline_model']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - bucketing policy with padding-cost/recompile-cost tradeoff
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fully dynamic fallback kernels with acceptable efficiency
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - shape-distribution learning from production traces
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - tail-latency impact measurement
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
     exactly (capability == cap.t03.dynamic.dynamic_shapes@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 33000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0124_dynamic_shapes.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0125-differentiation

**P0125 · `differentiation` — Automatic Differentiation on Ω-IR** · [spec](PART_SPECS_T03.md#p0125-differentiation) · [self-contained txt](../prompts/P0125_differentiation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0125  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0125 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0125  (25/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Automatic Differentiation on Ω-IR
file         : parts/t03_compiler/P0125_differentiation.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.differentiation
language     : Rust 1.86
capability   : cap.t03.differentiatio.differentiation@1
determinism  : pure
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Reverse and forward mode AD with checkpointing integration.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. reverse-mode transformation with correct effect and control-flow handling
  2. forward-mode and JVP/VJP composition for higher-order needs
  3. custom-gradient registration and verification
  4. gradient correctness versus numerical differentiation

Expanded obligations:
  1. Implement reverse-mode transformation with correct effect and
     control-flow handling, and make it correct under concurrency: at least
     64 in-flight `OmegaEnvelope`s must be able to traverse it
     simultaneously. No lock, mutex or borrow may be held across an `await` /
     `.await` / `yield` boundary, and the part must expose a contention
     counter so T09 can attribute latency to it. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement forward-mode and JVP/VJP composition for higher-order needs
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement custom-gradient registration and verification together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement gradient correctness versus numerical differentiation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.differentiatio.differentiation@1
  cap.t03.differentiatio.differentiation.describe@1

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

  cap.t03.dynamic.dynamic_shapes@1
      if unavailable: use the in-file conservative substitute for
      `dynamic_shapes` (documented, slower, lower quality) and set
      `degraded['dynamic_shapes']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t02.power.power_thermal@1
      if unavailable: use the in-file conservative substitute for
      `power_thermal` (documented, slower, lower quality) and set
      `degraded['power_thermal']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - reverse-mode transformation with correct effect and control-flow
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - forward-mode and JVP/VJP composition for higher-order needs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - custom-gradient registration and verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - gradient correctness versus numerical differentiation
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
     exactly (capability == cap.t03.differentiatio.differentiation@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 34000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0125_differentiation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0126-vectorisation-transform

**P0126 · `vectorisation_transform` — Batching & Vectorisation Transform** · [spec](PART_SPECS_T03.md#p0126-vectorisation-transform) · [self-contained txt](../prompts/P0126_vectorisation_transform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0126  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0126 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0126  (26/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Batching & Vectorisation Transform
file         : parts/t03_compiler/P0126_vectorisation_transform.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.vectorisation_transform
language     : Rust 1.86
capability   : cap.t03.vectorisation.vectorisation_transform@1
determinism  : pure
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Automatic vmap-style batching over arbitrary subgraphs.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. rank-polymorphic transformation with batching rules per op
  2. nested batching composition
  3. fallback loop generation with clear performance warnings
  4. equivalence tests against explicit loops

Expanded obligations:
  1. Implement rank-polymorphic transformation with batching rules per op
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement nested batching composition together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Correctness here is what makes the
     tier's SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement fallback loop generation with clear performance warnings as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement equivalence tests against explicit loops, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.vectorisation.vectorisation_transform@1
  cap.t03.vectorisation.vectorisation_transform.describe@1

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

  cap.t03.differentiatio.differentiation@1
      if unavailable: use the in-file conservative substitute for
      `differentiation` (documented, slower, lower quality) and set
      `degraded['differentiation']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t02.ragged.ragged_batch@1
      if unavailable: use the in-file conservative substitute for
      `ragged_batch` (documented, slower, lower quality) and set
      `degraded['ragged_batch']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - rank-polymorphic transformation with batching rules per op
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - nested batching composition
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - fallback loop generation with clear performance warnings
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - equivalence tests against explicit loops
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
     exactly (capability == cap.t03.vectorisation.vectorisation_transform@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 35000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0126_vectorisation_transform.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0127-loop-transform

**P0127 · `loop_transform` — Polyhedral Loop Transformation** · [spec](PART_SPECS_T03.md#p0127-loop-transform) · [self-contained txt](../prompts/P0127_loop_transform.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0127  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0127 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0127  (27/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Polyhedral Loop Transformation
file         : parts/t03_compiler/P0127_loop_transform.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.loop_transform
language     : Rust 1.86
capability   : cap.t03.loop.loop_transform@1
determinism  : pure
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Tiling, fusion, interchange and skewing with dependence legality.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dependence analysis and legality checking
  2. tiling/skewing/interchange transformation composition
  3. objective functions for locality and parallelism
  4. transformation legality proofs on a benchmark set

Expanded obligations:
  1. Implement dependence analysis and legality checking together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement tiling/skewing/interchange transformation composition as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement objective functions for locality and parallelism, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement transformation legality proofs on a benchmark set with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.loop.loop_transform@1
  cap.t03.loop.loop_transform.describe@1

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

  cap.t03.vectorisation.vectorisation_transform@1
      if unavailable: use the in-file conservative substitute for
      `vectorisation_transform` (documented, slower, lower quality) and set
      `degraded['vectorisation_transform']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t02.gemm.gemm_grouped@1
      if unavailable: use the in-file conservative substitute for
      `gemm_grouped` (documented, slower, lower quality) and set
      `degraded['gemm_grouped']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - dependence analysis and legality checking
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tiling/skewing/interchange transformation composition
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - objective functions for locality and parallelism
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - transformation legality proofs on a benchmark set
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
     exactly (capability == cap.t03.loop.loop_transform@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 36000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0127_loop_transform.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0128-constant-folding

**P0128 · `constant_folding` — Constant Folding & Weight Preprocessing** · [spec](PART_SPECS_T03.md#p0128-constant-folding) · [self-contained txt](../prompts/P0128_constant_folding.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0128  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0128 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0128  (28/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Constant Folding & Weight Preprocessing
file         : parts/t03_compiler/P0128_constant_folding.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.constant_folding
language     : Rust 1.86
capability   : cap.t03.constant.constant_folding@1
determinism  : pure
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Precomputes everything that does not depend on the request.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. exact constant evaluation with the same numerics as runtime
  2. weight transformation baking (layout, quantisation, fusion of scales)
  3. memory-bounded folding policy
  4. startup-time and per-request savings measurement

Expanded obligations:
  1. Implement exact constant evaluation with the same numerics as runtime as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement weight transformation baking (layout, quantisation, fusion of
     scales), and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement memory-bounded folding policy with an explicit *a-priori* cost
     model. Before doing the work the part must be able to state the tokens,
     FLOPs and microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Correctness here is what makes the
     tier's SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement startup-time and per-request savings measurement together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.constant.constant_folding@1
  cap.t03.constant.constant_folding.describe@1

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

  cap.t03.loop.loop_transform@1
      if unavailable: use the in-file conservative substitute for
      `loop_transform` (documented, slower, lower quality) and set
      `degraded['loop_transform']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t02.conv.conv_depthwise@1
      if unavailable: use the in-file conservative substitute for
      `conv_depthwise` (documented, slower, lower quality) and set
      `degraded['conv_depthwise']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - exact constant evaluation with the same numerics as runtime
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - weight transformation baking (layout, quantisation, fusion of sc
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - memory-bounded folding policy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - startup-time and per-request savings measurement
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
     exactly (capability == cap.t03.constant.constant_folding@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 37000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0128_constant_folding.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0129-dead-code-dce

**P0129 · `dead_code_dce` — Dead Code, CSE & Canonicalisation** · [spec](PART_SPECS_T03.md#p0129-dead-code-dce) · [self-contained txt](../prompts/P0129_dead_code_dce.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0129  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0129 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0129  (29/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Dead Code, CSE & Canonicalisation
file         : parts/t03_compiler/P0129_dead_code_dce.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.dead_code_dce
language     : Rust 1.86
capability   : cap.t03.dead.dead_code_dce@1
determinism  : pure
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The classic cleanups, made effect-aware and determinism-safe.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. effect-aware DCE preserving observable behaviour
  2. global value numbering and common-subexpression elimination
  3. canonicalisation to a normal form enabling later matches
  4. IR-size and op-count reduction metrics

Expanded obligations:
  1. Implement effect-aware DCE preserving observable behaviour, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement global value numbering and common-subexpression elimination
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement canonicalisation to a normal form enabling later matches
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement IR-size and op-count reduction metrics as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against SWE-bench Verified — a regression
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.dead.dead_code_dce@1
  cap.t03.dead.dead_code_dce.describe@1

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

  cap.t03.constant.constant_folding@1
      if unavailable: use the in-file conservative substitute for
      `constant_folding` (documented, slower, lower quality) and set
      `degraded['constant_folding']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t02.rope.rope_embed@1
      if unavailable: use the in-file conservative substitute for
      `rope_embed` (documented, slower, lower quality) and set
      `degraded['rope_embed']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - effect-aware DCE preserving observable behaviour
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - global value numbering and common-subexpression elimination
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - canonicalisation to a normal form enabling later matches
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - IR-size and op-count reduction metrics
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
     exactly (capability == cap.t03.dead.dead_code_dce@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 38000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0129_dead_code_dce.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0130-effect-system

**P0130 · `effect_system` — Effect & Purity Analysis** · [spec](PART_SPECS_T03.md#p0130-effect-system) · [self-contained txt](../prompts/P0130_effect_system.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0130  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0130 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0130  (30/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Effect & Purity Analysis
file         : parts/t03_compiler/P0130_effect_system.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.effect_system
language     : Rust 1.86
capability   : cap.t03.effect.effect_system@1
determinism  : pure
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Tracks IO, randomness, mutation and safety effects through the graph.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. effect lattice with precise join semantics
  2. purity inference enabling reordering and caching
  3. randomness-source tracking tied to split_seed
  4. misclassification detection tests

Expanded obligations:
  1. Implement effect lattice with precise join semantics with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement purity inference enabling reordering and caching together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement randomness-source tracking tied to split_seed as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement misclassification detection tests, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's SWE-bench Verified target reachable; the part
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
  cap.t03.effect.effect_system@1
  cap.t03.effect.effect_system.describe@1

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

  cap.t03.dead.dead_code_dce@1
      if unavailable: use the in-file conservative substitute for
      `dead_code_dce` (documented, slower, lower quality) and set
      `degraded['dead_code_dce']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t02.mem.mem_pool_device@1
      if unavailable: use the in-file conservative substitute for
      `mem_pool_device` (documented, slower, lower quality) and set
      `degraded['mem_pool_device']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - effect lattice with precise join semantics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - purity inference enabling reordering and caching
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - randomness-source tracking tied to split_seed
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - misclassification detection tests
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
     exactly (capability == cap.t03.effect.effect_system@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 39000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0130_effect_system.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0131-ir-verifier

**P0131 · `ir_verifier` — IR Verification & Invariant Checking** · [spec](PART_SPECS_T03.md#p0131-ir-verifier) · [self-contained txt](../prompts/P0131_ir_verifier.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0131  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0131 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0131  (31/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : IR Verification & Invariant Checking
file         : parts/t03_compiler/P0131_ir_verifier.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.ir_verifier
language     : Rust 1.86
capability   : cap.t03.ir.ir_verifier@1
determinism  : pure
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Catches compiler bugs before they become model bugs.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structural, type, shape, effect and determinism invariants
  2. pass-boundary verification with cheap and thorough modes
  3. counterexample minimisation for failed invariants
  4. verifier coverage over a mutation-generated bad-IR corpus

Expanded obligations:
  1. Implement structural, type, shape, effect and determinism invariants
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement pass-boundary verification with cheap and thorough modes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement counterexample minimisation for failed invariants, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement verifier coverage over a mutation-generated bad-IR corpus with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.ir.ir_verifier@1
  cap.t03.ir.ir_verifier.describe@1

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

  cap.t03.effect.effect_system@1
      if unavailable: use the in-file conservative substitute for
      `effect_system` (documented, slower, lower quality) and set
      `degraded['effect_system']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t02.kernel.kernel_verify@1
      if unavailable: use the in-file conservative substitute for
      `kernel_verify` (documented, slower, lower quality) and set
      `degraded['kernel_verify']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - structural, type, shape, effect and determinism invariants
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - pass-boundary verification with cheap and thorough modes
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - counterexample minimisation for failed invariants
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verifier coverage over a mutation-generated bad-IR corpus
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
     exactly (capability == cap.t03.ir.ir_verifier@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 40000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0131_ir_verifier.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0132-differential-testing

**P0132 · `differential_testing` — Compiler Differential Test Harness** · [spec](PART_SPECS_T03.md#p0132-differential-testing) · [self-contained txt](../prompts/P0132_differential_testing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0132  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0132 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0132  (32/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Compiler Differential Test Harness
file         : parts/t03_compiler/P0132_differential_testing.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.differential_testing
language     : Rust 1.86
capability   : cap.t03.differential.differential_testing@1
determinism  : pure
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Proves optimised execution matches reference execution exactly.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. random IR generation with realistic op distributions
  2. optimisation-level differential comparison with tolerance classes
  3. bisection over the pass pipeline to localise miscompiles
  4. nightly-scale corpus with pinned regressions

Expanded obligations:
  1. Implement random IR generation with realistic op distributions as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement optimisation-level differential comparison with tolerance
     classes, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement bisection over the pass pipeline to localise miscompiles with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement nightly-scale corpus with pinned regressions together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
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
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.differential.differential_testing@1
  cap.t03.differential.differential_testing.describe@1

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

  cap.t03.ir.ir_verifier@1
      if unavailable: use the in-file conservative substitute for
      `ir_verifier` (documented, slower, lower quality) and set
      `degraded['ir_verifier']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t02.stream.stream_scheduler@1
      if unavailable: use the in-file conservative substitute for
      `stream_scheduler` (documented, slower, lower quality) and set
      `degraded['stream_scheduler']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - random IR generation with realistic op distributions
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - optimisation-level differential comparison with tolerance classe
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - bisection over the pass pipeline to localise miscompiles
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - nightly-scale corpus with pinned regressions
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
     exactly (capability == cap.t03.differential.differential_testing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 41000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0132_differential_testing.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0133-compile-time-budget

**P0133 · `compile_time_budget` — Compilation Time Budget Manager** · [spec](PART_SPECS_T03.md#p0133-compile-time-budget) · [self-contained txt](../prompts/P0133_compile_time_budget.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0133  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0133 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0133  (33/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Compilation Time Budget Manager
file         : parts/t03_compiler/P0133_compile_time_budget.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.compile_time_budget
language     : Rust 1.86
capability   : cap.t03.compile.compile_time_budget@1
determinism  : pure
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Keeps compile time predictable, even under aggressive optimisation.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-pass time budgeting with graceful degradation
  2. priority ordering so the hottest subgraphs get the most effort
  3. background/incremental compilation with hot swap
  4. compile-time distribution measurement and tail control

Expanded obligations:
  1. Implement per-pass time budgeting with graceful degradation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement priority ordering so the hottest subgraphs get the most effort
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement background/incremental compilation with hot swap together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement compile-time distribution measurement and tail control as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.compile.compile_time_budget@1
  cap.t03.compile.compile_time_budget.describe@1

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

  cap.t03.differential.differential_testing@1
      if unavailable: use the in-file conservative substitute for
      `differential_testing` (documented, slower, lower quality) and set
      `degraded['differential_testing']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t02.tensor.tensor_view@1
      if unavailable: use the in-file conservative substitute for
      `tensor_view` (documented, slower, lower quality) and set
      `degraded['tensor_view']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - per-pass time budgeting with graceful degradation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - priority ordering so the hottest subgraphs get the most effort
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - background/incremental compilation with hot swap
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - compile-time distribution measurement and tail control
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
     exactly (capability == cap.t03.compile.compile_time_budget@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 42000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0133_compile_time_budget.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0134-profile-guided

**P0134 · `profile_guided` — Profile-Guided Optimisation Pipeline** · [spec](PART_SPECS_T03.md#p0134-profile-guided) · [self-contained txt](../prompts/P0134_profile_guided.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0134  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0134 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0134  (34/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Profile-Guided Optimisation Pipeline
file         : parts/t03_compiler/P0134_profile_guided.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.profile_guided
language     : Rust 1.86
capability   : cap.t03.profile.profile_guided@1
determinism  : pure
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Feeds production behaviour back into compilation decisions.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. execution profile collection and aggregation format
  2. hot-path specialisation and branch-probability propagation
  3. profile-staleness detection and safe reuse
  4. measured gain from PGO versus static heuristics

Expanded obligations:
  1. Implement execution profile collection and aggregation format with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement hot-path specialisation and branch-probability propagation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement profile-staleness detection and safe reuse as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement measured gain from PGO versus static heuristics, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.profile.profile_guided@1
  cap.t03.profile.profile_guided.describe@1

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

  cap.t03.compile.compile_time_budget@1
      if unavailable: use the in-file conservative substitute for
      `compile_time_budget` (documented, slower, lower quality) and set
      `degraded['compile_time_budget']='local'`

  cap.t02.gemm.gemm_int4@1
      if unavailable: use the in-file conservative substitute for
      `gemm_int4` (documented, slower, lower quality) and set
      `degraded['gemm_int4']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - execution profile collection and aggregation format
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hot-path specialisation and branch-probability propagation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - profile-staleness detection and safe reuse
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured gain from PGO versus static heuristics
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
     exactly (capability == cap.t03.profile.profile_guided@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 43000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0134_profile_guided.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0135-target-description

**P0135 · `target_description` — Target Machine Description Language** · [spec](PART_SPECS_T03.md#p0135-target-description) · [self-contained txt](../prompts/P0135_target_description.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0135  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0135 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0135  (35/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Target Machine Description Language
file         : parts/t03_compiler/P0135_target_description.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.target_description
language     : Rust 1.86
capability   : cap.t03.target.target_description@1
determinism  : pure
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
One declarative description per accelerator drives all target-specific
decisions.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hierarchical description: compute units, memories, bandwidths, latencies, ISA features
  2. capability queries used by passes instead of hardcoded checks
  3. validation of a description against measured microbenchmarks
  4. new-target onboarding checklist and conformance suite

Expanded obligations:
  1. Implement hierarchical description: compute units, memories, bandwidths,
     latencies, ISA features together with its verification path, so that
     anything this mechanism produces can be independently re-checked *inside
     this same file* without contacting any other part. The checker must be
     cheap enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement capability queries used by passes instead of hardcoded checks
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement validation of a description against measured microbenchmarks,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement new-target onboarding checklist and conformance suite with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
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
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.target.target_description@1
  cap.t03.target.target_description.describe@1

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

  cap.t03.profile.profile_guided@1
      if unavailable: use the in-file conservative substitute for
      `profile_guided` (documented, slower, lower quality) and set
      `degraded['profile_guided']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t02.ssm.ssm_scan@1
      if unavailable: use the in-file conservative substitute for `ssm_scan`
      (documented, slower, lower quality) and set
      `degraded['ssm_scan']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - hierarchical description: compute units, memories, bandwidths, l
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability queries used by passes instead of hardcoded checks
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - validation of a description against measured microbenchmarks
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - new-target onboarding checklist and conformance suite
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
     exactly (capability == cap.t03.target.target_description@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 44000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0135_target_description.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0136-ir-serialization

**P0136 · `ir_serialization` — IR Serialisation & Portable Artifact Format** · [spec](PART_SPECS_T03.md#p0136-ir-serialization) · [self-contained txt](../prompts/P0136_ir_serialization.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0136  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0136 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0136  (36/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : IR Serialisation & Portable Artifact Format
file         : parts/t03_compiler/P0136_ir_serialization.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.ir_serialization
language     : Rust 1.86
capability   : cap.t03.ir.ir_serialization@1
determinism  : pure
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Compiled artifacts that ship, version and verify.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. compact binary format with schema versioning and forward compat
  2. embedded provenance, guards and target requirements
  3. signature and integrity verification before load
  4. cross-version load tests

Expanded obligations:
  1. Implement compact binary format with schema versioning and forward
     compat as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement embedded provenance, guards and target requirements, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement signature and integrity verification before load with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement cross-version load tests together with its verification path,
     so that anything this mechanism produces can be independently re-checked
     *inside this same file* without contacting any other part. The checker
     must be cheap enough to run on every call in debug mode and must be
     wired into `selftest()`. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.ir.ir_serialization@1
  cap.t03.ir.ir_serialization.describe@1

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

  cap.t03.target.target_description@1
      if unavailable: use the in-file conservative substitute for
      `target_description` (documented, slower, lower quality) and set
      `degraded['target_description']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t02.kv.kv_cache_kernels@1
      if unavailable: use the in-file conservative substitute for
      `kv_cache_kernels` (documented, slower, lower quality) and set
      `degraded['kv_cache_kernels']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - compact binary format with schema versioning and forward compat
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - embedded provenance, guards and target requirements
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - signature and integrity verification before load
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cross-version load tests
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
     exactly (capability == cap.t03.ir.ir_serialization@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 45000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0136_ir_serialization.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0137-bytecode-vm

**P0137 · `bytecode_vm` — Ω Execution Bytecode & Interpreter** · [spec](PART_SPECS_T03.md#p0137-bytecode-vm) · [self-contained txt](../prompts/P0137_bytecode_vm.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0137  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0137 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0137  (37/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Ω Execution Bytecode & Interpreter
file         : parts/t03_compiler/P0137_bytecode_vm.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.bytecode_vm
language     : Rust 1.86
capability   : cap.t03.bytecode.bytecode_vm@1
determinism  : pure
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The portable, debuggable execution path used as the correctness oracle.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. compact bytecode with explicit buffer and effect operands
  2. interpreter with single-step, breakpoint and watch support
  3. identical numerics to compiled paths in reference mode
  4. interpretive overhead documented and bounded

Expanded obligations:
  1. Implement compact bytecode with explicit buffer and effect operands, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement interpreter with single-step, breakpoint and watch support
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement identical numerics to compiled paths in reference mode
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement interpretive overhead documented and bounded as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.bytecode.bytecode_vm@1
  cap.t03.bytecode.bytecode_vm.describe@1

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

  cap.t03.ir.ir_serialization@1
      if unavailable: use the in-file conservative substitute for
      `ir_serialization` (documented, slower, lower quality) and set
      `degraded['ir_serialization']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t02.graph.graph_capture@1
      if unavailable: use the in-file conservative substitute for
      `graph_capture` (documented, slower, lower quality) and set
      `degraded['graph_capture']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - compact bytecode with explicit buffer and effect operands
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - interpreter with single-step, breakpoint and watch support
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - identical numerics to compiled paths in reference mode
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - interpretive overhead documented and bounded
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
     exactly (capability == cap.t03.bytecode.bytecode_vm@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 46000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0137_bytecode_vm.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0138-debug-symbols

**P0138 · `debug_symbols` — Debug Info, Source Mapping & Blame** · [spec](PART_SPECS_T03.md#p0138-debug-symbols) · [self-contained txt](../prompts/P0138_debug_symbols.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0138  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0138 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0138  (38/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Debug Info, Source Mapping & Blame
file         : parts/t03_compiler/P0138_debug_symbols.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.debug_symbols
language     : Rust 1.86
capability   : cap.t03.debug.debug_symbols@1
determinism  : pure
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Maps any runtime anomaly back to a source line in one of 1000 files.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. source-location propagation surviving every transformation
  2. inlining and fusion attribution with multi-origin support
  3. blame report generation for numerical anomalies
  4. attribution accuracy tests through deep pass pipelines

Expanded obligations:
  1. Implement source-location propagation surviving every transformation
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement inlining and fusion attribution with multi-origin support
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement blame report generation for numerical anomalies as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement attribution accuracy tests through deep pass pipelines, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.

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
  cap.t03.debug.debug_symbols@1
  cap.t03.debug.debug_symbols.describe@1

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

  cap.t03.bytecode.bytecode_vm@1
      if unavailable: use the in-file conservative substitute for
      `bytecode_vm` (documented, slower, lower quality) and set
      `degraded['bytecode_vm']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t02.kernel.kernel_registry@1
      if unavailable: use the in-file conservative substitute for
      `kernel_registry` (documented, slower, lower quality) and set
      `degraded['kernel_registry']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - source-location propagation surviving every transformation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - inlining and fusion attribution with multi-origin support
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blame report generation for numerical anomalies
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - attribution accuracy tests through deep pass pipelines
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
     exactly (capability == cap.t03.debug.debug_symbols@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 47000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0138_debug_symbols.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0139-pass-search

**P0139 · `pass_search` — Automated Pass Pipeline Search** · [spec](PART_SPECS_T03.md#p0139-pass-search) · [self-contained txt](../prompts/P0139_pass_search.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0139  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0139 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0139  (39/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Automated Pass Pipeline Search
file         : parts/t03_compiler/P0139_pass_search.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.pass_search
language     : Rust 1.86
capability   : cap.t03.pass.pass_search@1
determinism  : pure
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Discovers better optimisation pipelines than hand-written ones.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. pipeline space definition with legality and idempotence constraints
  2. evolutionary/bandit search with early stopping
  3. generalisation validation across model families
  4. measured improvement over the default pipeline

Expanded obligations:
  1. Implement pipeline space definition with legality and idempotence
     constraints together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement evolutionary/bandit search with early stopping as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement generalisation validation across model families, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured improvement over the default pipeline with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
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
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.pass.pass_search@1
  cap.t03.pass.pass_search.describe@1

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

  cap.t03.debug.debug_symbols@1
      if unavailable: use the in-file conservative substitute for
      `debug_symbols` (documented, slower, lower quality) and set
      `degraded['debug_symbols']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t02.p2p.p2p_transfer@1
      if unavailable: use the in-file conservative substitute for
      `p2p_transfer` (documented, slower, lower quality) and set
      `degraded['p2p_transfer']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - pipeline space definition with legality and idempotence constrai
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - evolutionary/bandit search with early stopping
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - generalisation validation across model families
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured improvement over the default pipeline
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
     exactly (capability == cap.t03.pass.pass_search@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 48000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0139_pass_search.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0140-superoptimiser

**P0140 · `superoptimiser` — Bounded Superoptimiser for Hot Kernels** · [spec](PART_SPECS_T03.md#p0140-superoptimiser) · [self-contained txt](../prompts/P0140_superoptimiser.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0140  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0140 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0140  (40/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Bounded Superoptimiser for Hot Kernels
file         : parts/t03_compiler/P0140_superoptimiser.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.superoptimiser
language     : Rust 1.86
capability   : cap.t03.superoptimiser.superoptimiser@1
determinism  : pure
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Exhaustively searches for optimal instruction sequences on small critical
regions.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. region selection by profile contribution and size bound
  2. enumerative/SMT-based equivalent-sequence search
  3. verified equivalence before adoption
  4. catalogue of discovered sequences with measured wins

Expanded obligations:
  1. Implement region selection by profile contribution and size bound as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement enumerative/SMT-based equivalent-sequence search, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement verified equivalence before adoption with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement catalogue of discovered sequences with measured wins together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.superoptimiser.superoptimiser@1
  cap.t03.superoptimiser.superoptimiser.describe@1

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

  cap.t03.pass.pass_search@1
      if unavailable: use the in-file conservative substitute for
      `pass_search` (documented, slower, lower quality) and set
      `degraded['pass_search']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t02.mask.mask_engine@1
      if unavailable: use the in-file conservative substitute for
      `mask_engine` (documented, slower, lower quality) and set
      `degraded['mask_engine']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - region selection by profile contribution and size bound
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - enumerative/SMT-based equivalent-sequence search
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - verified equivalence before adoption
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - catalogue of discovered sequences with measured wins
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
     exactly (capability == cap.t03.superoptimiser.superoptimiser@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 49000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0140_superoptimiser.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0141-equality-saturation

**P0141 · `equality_saturation` — E-Graph Engine & Extraction** · [spec](PART_SPECS_T03.md#p0141-equality-saturation) · [self-contained txt](../prompts/P0141_equality_saturation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0141  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0141 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0141  (41/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : E-Graph Engine & Extraction
file         : parts/t03_compiler/P0141_equality_saturation.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.equality_saturation
language     : Rust 1.86
capability   : cap.t03.equality.equality_saturation@1
determinism  : pure
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The rewriting substrate: saturate, then extract the cheapest equivalent
program.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. congruence-closure e-graph with efficient rebuild
  2. cost function plugins including learned costs
  3. extraction with cycle avoidance and global optimality bounds
  4. saturation-limit policies and quality-vs-time curves

Expanded obligations:
  1. Implement congruence-closure e-graph with efficient rebuild, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement cost function plugins including learned costs with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement extraction with cycle avoidance and global optimality bounds
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement saturation-limit policies and quality-vs-time curves as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.equality.equality_saturation@1
  cap.t03.equality.equality_saturation.describe@1

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

  cap.t03.superoptimiser.superoptimiser@1
      if unavailable: use the in-file conservative substitute for
      `superoptimiser` (documented, slower, lower quality) and set
      `degraded['superoptimiser']='local'`

  cap.t02.gemm.gemm_fp8@1
      if unavailable: use the in-file conservative substitute for `gemm_fp8`
      (documented, slower, lower quality) and set
      `degraded['gemm_fp8']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - congruence-closure e-graph with efficient rebuild
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost function plugins including learned costs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - extraction with cycle avoidance and global optimality bounds
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - saturation-limit policies and quality-vs-time curves
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
     exactly (capability == cap.t03.equality.equality_saturation@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 3000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0141_equality_saturation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0142-kernel-template-lib

**P0142 · `kernel_template_lib` — Kernel Template Library** · [spec](PART_SPECS_T03.md#p0142-kernel-template-lib) · [self-contained txt](../prompts/P0142_kernel_template_lib.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0142  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0142 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0142  (42/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Kernel Template Library
file         : parts/t03_compiler/P0142_kernel_template_lib.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.kernel_template_lib
language     : Rust 1.86
capability   : cap.t03.kernel.kernel_template_lib@1
determinism  : pure
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Parameterised templates the codegen instantiates for any shape.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. template families for GEMM, attention, scan, reduction, elementwise
  2. parameter validity constraints and default heuristics
  3. instantiation cost and code-size control
  4. coverage report over the benchmark shape corpus

Expanded obligations:
  1. Implement template families for GEMM, attention, scan, reduction,
     elementwise with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement parameter validity constraints and default heuristics together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement instantiation cost and code-size control as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement coverage report over the benchmark shape corpus, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.kernel.kernel_template_lib@1
  cap.t03.kernel.kernel_template_lib.describe@1

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

  cap.t03.equality.equality_saturation@1
      if unavailable: use the in-file conservative substitute for
      `equality_saturation` (documented, slower, lower quality) and set
      `degraded['equality_saturation']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t02.attn.attn_linear@1
      if unavailable: use the in-file conservative substitute for
      `attn_linear` (documented, slower, lower quality) and set
      `degraded['attn_linear']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - template families for GEMM, attention, scan, reduction, elementw
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - parameter validity constraints and default heuristics
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - instantiation cost and code-size control
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - coverage report over the benchmark shape corpus
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
     exactly (capability == cap.t03.kernel.kernel_template_lib@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 4000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0142_kernel_template_lib.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0143-linker-omega

**P0143 · `linker_omega` — Ω-Linker for 1000 Compiled Parts** · [spec](PART_SPECS_T03.md#p0143-linker-omega) · [self-contained txt](../prompts/P0143_linker_omega.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0143  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0143 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0143  (43/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Ω-Linker for 1000 Compiled Parts
file         : parts/t03_compiler/P0143_linker_omega.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.linker_omega
language     : Rust 1.86
capability   : cap.t03.linker.linker_omega@1
determinism  : pure
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Links independently compiled part artifacts into one executable assembly.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capability symbol resolution across artifact boundaries
  2. cross-part inlining and whole-assembly optimisation
  3. version/ABI compatibility enforcement at link time
  4. link-time report: unresolved, duplicate, degraded capabilities

Expanded obligations:
  1. Implement capability symbol resolution across artifact boundaries
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement cross-part inlining and whole-assembly optimisation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement version/ABI compatibility enforcement at link time, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement link-time report: unresolved, duplicate, degraded capabilities
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
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
  cap.t03.linker.linker_omega@1
  cap.t03.linker.linker_omega.describe@1

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

  cap.t03.kernel.kernel_template_lib@1
      if unavailable: use the in-file conservative substitute for
      `kernel_template_lib` (documented, slower, lower quality) and set
      `degraded['kernel_template_lib']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t02.quantize.quantize_kernels@1
      if unavailable: use the in-file conservative substitute for
      `quantize_kernels` (documented, slower, lower quality) and set
      `degraded['quantize_kernels']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - capability symbol resolution across artifact boundaries
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-part inlining and whole-assembly optimisation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - version/ABI compatibility enforcement at link time
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - link-time report: unresolved, duplicate, degraded capabilities
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
     exactly (capability == cap.t03.linker.linker_omega@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 5000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0143_linker_omega.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0144-incremental-build

**P0144 · `incremental_build` — Incremental Compilation & Change Impact** · [spec](PART_SPECS_T03.md#p0144-incremental-build) · [self-contained txt](../prompts/P0144_incremental_build.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0144  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0144 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0144  (44/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Incremental Compilation & Change Impact
file         : parts/t03_compiler/P0144_incremental_build.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.incremental_build
language     : Rust 1.86
capability   : cap.t03.incremental.incremental_build@1
determinism  : pure
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Recompiles only what 1 changed part affects, across the 1000-part assembly.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fine-grained dependency graph with content hashing
  2. change-impact analysis and minimal rebuild set computation
  3. cache reuse across branches and machines
  4. rebuild-time measurement for single-part edits

Expanded obligations:
  1. Implement fine-grained dependency graph with content hashing as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement change-impact analysis and minimal rebuild set computation,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement cache reuse across branches and machines with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement rebuild-time measurement for single-part edits together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.incremental.incremental_build@1
  cap.t03.incremental.incremental_build.describe@1

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

  cap.t03.linker.linker_omega@1
      if unavailable: use the in-file conservative substitute for
      `linker_omega` (documented, slower, lower quality) and set
      `degraded['linker_omega']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t02.fused.fused_decode_step@1
      if unavailable: use the in-file conservative substitute for
      `fused_decode_step` (documented, slower, lower quality) and set
      `degraded['fused_decode_step']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - fine-grained dependency graph with content hashing
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - change-impact analysis and minimal rebuild set computation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cache reuse across branches and machines
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - rebuild-time measurement for single-part edits
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
     exactly (capability == cap.t03.incremental.incremental_build@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 6000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0144_incremental_build.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0145-crosscompile

**P0145 · `crosscompile` — Cross-Compilation & Target Matrix** · [spec](PART_SPECS_T03.md#p0145-crosscompile) · [self-contained txt](../prompts/P0145_crosscompile.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0145  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0145 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0145  (45/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Cross-Compilation & Target Matrix
file         : parts/t03_compiler/P0145_crosscompile.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.crosscompile
language     : Rust 1.86
capability   : cap.t03.crosscompile.crosscompile@1
determinism  : pure
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Build once, run on every supported accelerator and CPU.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hermetic toolchain description and pinned versions
  2. multi-target artifact bundling with runtime selection
  3. reproducible-build verification (identical bytes)
  4. target-matrix CI definition

Expanded obligations:
  1. Implement hermetic toolchain description and pinned versions, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement multi-target artifact bundling with runtime selection with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement reproducible-build verification (identical bytes) together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement target-matrix CI definition as a first-class, fully realised
     mechanism. No stub, no `NotImplementedError`, no configuration flag
     whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's SWE-bench Verified target
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
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.crosscompile.crosscompile@1
  cap.t03.crosscompile.crosscompile.describe@1

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

  cap.t03.incremental.incremental_build@1
      if unavailable: use the in-file conservative substitute for
      `incremental_build` (documented, slower, lower quality) and set
      `degraded['incremental_build']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t02.bf16.bf16_stability@1
      if unavailable: use the in-file conservative substitute for
      `bf16_stability` (documented, slower, lower quality) and set
      `degraded['bf16_stability']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - hermetic toolchain description and pinned versions
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - multi-target artifact bundling with runtime selection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reproducible-build verification (identical bytes)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target-matrix CI definition
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
     exactly (capability == cap.t03.crosscompile.crosscompile@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 7000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0145_crosscompile.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0146-numeric-mode-lowering

**P0146 · `numeric_mode_lowering` — Determinism-Mode Lowering** · [spec](PART_SPECS_T03.md#p0146-numeric-mode-lowering) · [self-contained txt](../prompts/P0146_numeric_mode_lowering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0146  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0146 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0146  (46/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Determinism-Mode Lowering
file         : parts/t03_compiler/P0146_numeric_mode_lowering.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.numeric_mode_lowering
language     : Rust 1.86
capability   : cap.t03.numeric.numeric_mode_lowering@1
determinism  : pure
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Compiles the same graph into deterministic or fast variants with declared
differences.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mode-aware lowering rules for reductions, atomics and scheduling
  2. cost-of-determinism measurement per model region
  3. mode conformance verification (bit-exactness in deterministic mode)
  4. policy for mixed-mode graphs

Expanded obligations:
  1. Implement mode-aware lowering rules for reductions, atomics and
     scheduling with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement cost-of-determinism measurement per model region together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement mode conformance verification (bit-exactness in deterministic
     mode) as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement policy for mixed-mode graphs, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
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
  cap.t03.numeric.numeric_mode_lowering@1
  cap.t03.numeric.numeric_mode_lowering.describe@1

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

  cap.t03.crosscompile.crosscompile@1
      if unavailable: use the in-file conservative substitute for
      `crosscompile` (documented, slower, lower quality) and set
      `degraded['crosscompile']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t02.collective.collective_local@1
      if unavailable: use the in-file conservative substitute for
      `collective_local` (documented, slower, lower quality) and set
      `degraded['collective_local']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - mode-aware lowering rules for reductions, atomics and scheduling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost-of-determinism measurement per model region
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - mode conformance verification (bit-exactness in deterministic mo
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - policy for mixed-mode graphs
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
     exactly (capability == cap.t03.numeric.numeric_mode_lowering@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 8000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0146_numeric_mode_lowering.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0147-op-registry

**P0147 · `op_registry` — Operator Registry & Semantics Database** · [spec](PART_SPECS_T03.md#p0147-op-registry) · [self-contained txt](../prompts/P0147_op_registry.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0147  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0147 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0147  (47/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Operator Registry & Semantics Database
file         : parts/t03_compiler/P0147_op_registry.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.op_registry
language     : Rust 1.86
capability   : cap.t03.op.op_registry@1
determinism  : pure
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The canonical definition of every operator in Ω-IR.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. op schema: signature, semantics, effects, error bounds, determinism
  2. reference implementation link and lowering candidates
  3. registry consistency checks and completeness audit
  4. documentation generation for all operators

Expanded obligations:
  1. Implement op schema: signature, semantics, effects, error bounds,
     determinism together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement reference implementation link and lowering candidates as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement registry consistency checks and completeness audit, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement documentation generation for all operators with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
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
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.op.op_registry@1
  cap.t03.op.op_registry.describe@1

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

  cap.t03.numeric.numeric_mode_lowering@1
      if unavailable: use the in-file conservative substitute for
      `numeric_mode_lowering` (documented, slower, lower quality) and set
      `degraded['numeric_mode_lowering']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t02.embedding.embedding_kernels@1
      if unavailable: use the in-file conservative substitute for
      `embedding_kernels` (documented, slower, lower quality) and set
      `degraded['embedding_kernels']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - op schema: signature, semantics, effects, error bounds, determin
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - reference implementation link and lowering candidates
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - registry consistency checks and completeness audit
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - documentation generation for all operators
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
     exactly (capability == cap.t03.op.op_registry@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 9000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0147_op_registry.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0148-graph-diff-tool

**P0148 · `graph_diff_tool` — Graph Diff & Optimisation Explainer** · [spec](PART_SPECS_T03.md#p0148-graph-diff-tool) · [self-contained txt](../prompts/P0148_graph_diff_tool.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0148  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0148 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0148  (48/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Graph Diff & Optimisation Explainer
file         : parts/t03_compiler/P0148_graph_diff_tool.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.graph_diff_tool
language     : Rust 1.86
capability   : cap.t03.graph.graph_diff_tool@1
determinism  : pure
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Explains, in human terms, what the compiler did and why.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structural graph diff with matching heuristics
  2. per-decision rationale capture during passes
  3. human-readable optimisation report with measured impact
  4. explanation fidelity tests against pass logs

Expanded obligations:
  1. Implement structural graph diff with matching heuristics as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement per-decision rationale capture during passes, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement human-readable optimisation report with measured impact with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement explanation fidelity tests against pass logs together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.graph.graph_diff_tool@1
  cap.t03.graph.graph_diff_tool.describe@1

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

  cap.t03.op.op_registry@1
      if unavailable: use the in-file conservative substitute for
      `op_registry` (documented, slower, lower quality) and set
      `degraded['op_registry']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t02.kernel.kernel_docs_spec@1
      if unavailable: use the in-file conservative substitute for
      `kernel_docs_spec` (documented, slower, lower quality) and set
      `degraded['kernel_docs_spec']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - structural graph diff with matching heuristics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-decision rationale capture during passes
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - human-readable optimisation report with measured impact
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - explanation fidelity tests against pass logs
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
     exactly (capability == cap.t03.graph.graph_diff_tool@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 10000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0148_graph_diff_tool.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0149-compiler-fuzzer

**P0149 · `compiler_fuzzer` — Compiler Fuzzer & Miscompile Hunter** · [spec](PART_SPECS_T03.md#p0149-compiler-fuzzer) · [self-contained txt](../prompts/P0149_compiler_fuzzer.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0149  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0149 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0149  (49/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Compiler Fuzzer & Miscompile Hunter
file         : parts/t03_compiler/P0149_compiler_fuzzer.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.compiler_fuzzer
language     : Rust 1.86
capability   : cap.t03.compiler.compiler_fuzzer@1
determinism  : pure
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Continuously attacks the compiler with generated programs.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. grammar-based IR generation with semantic validity
  2. metamorphic testing (equivalent programs must agree)
  3. automatic reduction of miscompile cases
  4. found-bug corpus with pinned regression tests

Expanded obligations:
  1. Implement grammar-based IR generation with semantic validity, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement metamorphic testing (equivalent programs must agree) with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement automatic reduction of miscompile cases together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement found-bug corpus with pinned regression tests as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.compiler.compiler_fuzzer@1
  cap.t03.compiler.compiler_fuzzer.describe@1

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

  cap.t03.graph.graph_diff_tool@1
      if unavailable: use the in-file conservative substitute for
      `graph_diff_tool` (documented, slower, lower quality) and set
      `degraded['graph_diff_tool']='local'`

  cap.t02.attn.attn_paged_decode@1
      if unavailable: use the in-file conservative substitute for
      `attn_paged_decode` (documented, slower, lower quality) and set
      `degraded['attn_paged_decode']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - grammar-based IR generation with semantic validity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - metamorphic testing (equivalent programs must agree)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic reduction of miscompile cases
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - found-bug corpus with pinned regression tests
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
     exactly (capability == cap.t03.compiler.compiler_fuzzer@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 11000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0149_compiler_fuzzer.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0150-build-provenance

**P0150 · `build_provenance` — Build Provenance & Reproducibility Attestation** · [spec](PART_SPECS_T03.md#p0150-build-provenance) · [self-contained txt](../prompts/P0150_build_provenance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0150  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0150 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0150  (50/50 of tier T03)
tier         : T03 — Graph IR, Compiler & Autotuner
title        : Build Provenance & Reproducibility Attestation
file         : parts/t03_compiler/P0150_build_provenance.rs          <-- create exactly this path, nothing else
module       : hyperion.t03.compiler.build_provenance
language     : Rust 1.86
capability   : cap.t03.build.build_provenance@1
determinism  : pure
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Every artifact proves exactly how it was produced.

Tier context:
  Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and
  codegen for every accelerator target.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. full input hashing: sources, toolchains, flags, target descriptions
  2. in-toto-style attestation generation and verification
  3. bit-identical rebuild verification across machines
  4. provenance query interface for audits

Expanded obligations:
  1. Implement full input hashing: sources, toolchains, flags, target
     descriptions with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement in-toto-style attestation generation and verification together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement bit-identical rebuild verification across machines as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement provenance query interface for audits, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t03.build.build_provenance@1
  cap.t03.build.build_provenance.describe@1

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

  cap.t03.compiler.compiler_fuzzer@1
      if unavailable: use the in-file conservative substitute for
      `compiler_fuzzer` (documented, slower, lower quality) and set
      `degraded['compiler_fuzzer']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t02.topk.topk_sort@1
      if unavailable: use the in-file conservative substitute for
      `topk_sort` (documented, slower, lower quality) and set
      `degraded['topk_sort']='local'`

DETERMINISM
-----------
  pure — byte-identical output for byte-identical input, on every machine,
  forever. No clock, no RNG, no environment reads, no hash-order iteration,
  no floating-point reduction whose order depends on thread count.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - full input hashing: sources, toolchains, flags, target descripti
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - in-toto-style attestation generation and verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - bit-identical rebuild verification across machines
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - provenance query interface for audits
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
     exactly (capability == cap.t03.build.build_provenance@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 12000 ns?
  6. Is the declared determinism class `pure` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t03_compiler/P0150_build_provenance.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
