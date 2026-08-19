# HYPERION-Ω — Worker prompts · T04 · Hardware Abstraction & Interconnect

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

## PROMPT p0151-device-abstraction

**P0151 · `device_abstraction` — Device Abstraction Layer** · [spec](PART_SPECS_T04.md#p0151-device-abstraction) · [self-contained txt](../prompts/P0151_device_abstraction.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0151  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0151 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0151  (1/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Device Abstraction Layer
file         : parts/t04_hardware/P0151_device_abstraction.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.device_abstraction
language     : Rust 1.86
capability   : cap.t04.device.device_abstraction@1
determinism  : io
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
One uniform device interface over every accelerator vendor and generation.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. device enumeration, capability probing and feature-flag normalisation
  2. context/queue/event lifecycle with RAII-style safety
  3. vendor backend trait with two reference implementations
  4. conformance suite every backend must pass

Expanded obligations:
  1. Implement device enumeration, capability probing and feature-flag
     normalisation together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement context/queue/event lifecycle with RAII-style safety as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement vendor backend trait with two reference implementations, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement conformance suite every backend must pass with an explicit
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.device.device_abstraction@1
  cap.t04.device.device_abstraction.describe@1

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
   3. [ 600 lines] Core implementation A - device enumeration, capability probing and feature-flag normalis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - context/queue/event lifecycle with RAII-style safety
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - vendor backend trait with two reference implementations
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - conformance suite every backend must pass
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
     exactly (capability == cap.t04.device.device_abstraction@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0151_device_abstraction.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0152-topology-discovery

**P0152 · `topology_discovery` — Interconnect Topology Discovery** · [spec](PART_SPECS_T04.md#p0152-topology-discovery) · [self-contained txt](../prompts/P0152_topology_discovery.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0152  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0152 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0152  (2/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Interconnect Topology Discovery
file         : parts/t04_hardware/P0152_topology_discovery.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.topology_discovery
language     : Rust 1.86
capability   : cap.t04.topology.topology_discovery@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Builds an exact machine graph: links, bandwidths, latencies, failure
domains.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. PCIe/NVLink/fabric enumeration with bandwidth probing
  2. multi-node topology assembly from per-node views
  3. distance and bisection-bandwidth computation
  4. topology-vs-measurement validation and anomaly flagging

Expanded obligations:
  1. Implement PCIe/NVLink/fabric enumeration with bandwidth probing as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement multi-node topology assembly from per-node views, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement distance and bisection-bandwidth computation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement topology-vs-measurement validation and anomaly flagging
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.topology.topology_discovery@1
  cap.t04.topology.topology_discovery.describe@1

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

  cap.t04.device.device_abstraction@1
      if unavailable: use the in-file conservative substitute for
      `device_abstraction` (documented, slower, lower quality) and set
      `degraded['device_abstraction']='local'`

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
   3. [ 600 lines] Core implementation A - PCIe/NVLink/fabric enumeration with bandwidth probing
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - multi-node topology assembly from per-node views
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - distance and bisection-bandwidth computation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - topology-vs-measurement validation and anomaly flagging
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
     exactly (capability == cap.t04.topology.topology_discovery@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0152_topology_discovery.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0153-collective-global

**P0153 · `collective_global` — Multi-Node Collective Library** · [spec](PART_SPECS_T04.md#p0153-collective-global) · [self-contained txt](../prompts/P0153_collective_global.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0153  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0153 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0153  (3/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Multi-Node Collective Library
file         : parts/t04_hardware/P0153_collective_global.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.collective_global
language     : Rust 1.86
capability   : cap.t04.collective.collective_global@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Cluster-scale all-reduce/all-gather/all-to-all with topology awareness.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hierarchical algorithms (intra-node then inter-node) with size-based selection
  2. all-to-all optimisation for expert parallelism
  3. deterministic reduction ordering across thousands of ranks
  4. scaling efficiency measurement to 100k ranks

Expanded obligations:
  1. Implement hierarchical algorithms (intra-node then inter-node) with
     size-based selection, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     SWE-bench Verified — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement all-to-all optimisation for expert parallelism with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement deterministic reduction ordering across thousands of ranks
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement scaling efficiency measurement to 100k ranks as a first-class,
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.collective.collective_global@1
  cap.t04.collective.collective_global.describe@1

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

  cap.t04.topology.topology_discovery@1
      if unavailable: use the in-file conservative substitute for
      `topology_discovery` (documented, slower, lower quality) and set
      `degraded['topology_discovery']='local'`

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
   3. [ 600 lines] Core implementation A - hierarchical algorithms (intra-node then inter-node) with size-b
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - all-to-all optimisation for expert parallelism
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deterministic reduction ordering across thousands of ranks
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - scaling efficiency measurement to 100k ranks
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
     exactly (capability == cap.t04.collective.collective_global@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0153_collective_global.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0154-rdma-transport

**P0154 · `rdma_transport` — RDMA & Zero-Copy Network Transport** · [spec](PART_SPECS_T04.md#p0154-rdma-transport) · [self-contained txt](../prompts/P0154_rdma_transport.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0154  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0154 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0154  (4/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : RDMA & Zero-Copy Network Transport
file         : parts/t04_hardware/P0154_rdma_transport.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.rdma_transport
language     : Rust 1.86
capability   : cap.t04.rdma.rdma_transport@1
determinism  : io
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The lowest-latency path for tensors between machines.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. queue-pair management, memory registration and completion handling
  2. zero-copy send/recv with pre-registered buffer pools
  3. congestion control interaction and loss recovery
  4. latency/bandwidth benchmark versus hardware line rate

Expanded obligations:
  1. Implement queue-pair management, memory registration and completion
     handling with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement zero-copy send/recv with pre-registered buffer pools together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement congestion control interaction and loss recovery as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement latency/bandwidth benchmark versus hardware line rate, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.rdma.rdma_transport@1
  cap.t04.rdma.rdma_transport.describe@1

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

  cap.t04.collective.collective_global@1
      if unavailable: use the in-file conservative substitute for
      `collective_global` (documented, slower, lower quality) and set
      `degraded['collective_global']='local'`

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
   3. [ 600 lines] Core implementation A - queue-pair management, memory registration and completion handli
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - zero-copy send/recv with pre-registered buffer pools
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - congestion control interaction and loss recovery
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency/bandwidth benchmark versus hardware line rate
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
     exactly (capability == cap.t04.rdma.rdma_transport@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0154_rdma_transport.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0155-tcp-fallback

**P0155 · `tcp_fallback` — Reliable TCP/QUIC Transport Fallback** · [spec](PART_SPECS_T04.md#p0155-tcp-fallback) · [self-contained txt](../prompts/P0155_tcp_fallback.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0155  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0155 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0155  (5/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Reliable TCP/QUIC Transport Fallback
file         : parts/t04_hardware/P0155_tcp_fallback.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.tcp_fallback
language     : Rust 1.86
capability   : cap.t04.tcp.tcp_fallback@1
determinism  : io
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Works everywhere, degrades predictably when RDMA is unavailable.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. framing, multiplexing and flow control over stream transports
  2. QUIC path with 0-RTT reconnect and stream priorities
  3. adaptive chunk sizing and pacing
  4. measured gap versus RDMA with documented degradation ladder

Expanded obligations:
  1. Implement framing, multiplexing and flow control over stream transports
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement QUIC path with 0-RTT reconnect and stream priorities as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement adaptive chunk sizing and pacing, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's SWE-bench Verified target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement measured gap versus RDMA with documented degradation ladder
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.tcp.tcp_fallback@1
  cap.t04.tcp.tcp_fallback.describe@1

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

  cap.t04.rdma.rdma_transport@1
      if unavailable: use the in-file conservative substitute for
      `rdma_transport` (documented, slower, lower quality) and set
      `degraded['rdma_transport']='local'`

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
   3. [ 600 lines] Core implementation A - framing, multiplexing and flow control over stream transports
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - QUIC path with 0-RTT reconnect and stream priorities
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - adaptive chunk sizing and pacing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured gap versus RDMA with documented degradation ladder
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
     exactly (capability == cap.t04.tcp.tcp_fallback@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0155_tcp_fallback.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0156-comm-scheduler

**P0156 · `comm_scheduler` — Communication Scheduling & Prioritisation** · [spec](PART_SPECS_T04.md#p0156-comm-scheduler) · [self-contained txt](../prompts/P0156_comm_scheduler.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0156  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0156 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0156  (6/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Communication Scheduling & Prioritisation
file         : parts/t04_hardware/P0156_comm_scheduler.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.comm_scheduler
language     : Rust 1.86
capability   : cap.t04.comm.comm_scheduler@1
determinism  : io
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Prevents communication from ever becoming the critical path.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. priority classes for latency-critical versus bulk transfers
  2. bandwidth allocation with work-conserving fairness
  3. deadline-aware scheduling tied to the task DAG
  4. measured critical-path improvement

Expanded obligations:
  1. Implement priority classes for latency-critical versus bulk transfers as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement bandwidth allocation with work-conserving fairness, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement deadline-aware scheduling tied to the task DAG with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured critical-path improvement together with its
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.comm.comm_scheduler@1
  cap.t04.comm.comm_scheduler.describe@1

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

  cap.t04.tcp.tcp_fallback@1
      if unavailable: use the in-file conservative substitute for
      `tcp_fallback` (documented, slower, lower quality) and set
      `degraded['tcp_fallback']='local'`

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
   3. [ 600 lines] Core implementation A - priority classes for latency-critical versus bulk transfers
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - bandwidth allocation with work-conserving fairness
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deadline-aware scheduling tied to the task DAG
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured critical-path improvement
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
     exactly (capability == cap.t04.comm.comm_scheduler@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0156_comm_scheduler.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0157-expert-parallel-fabric

**P0157 · `expert_parallel_fabric` — Expert-Parallel Routing Fabric** · [spec](PART_SPECS_T04.md#p0157-expert-parallel-fabric) · [self-contained txt](../prompts/P0157_expert_parallel_fabric.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0157  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0157 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0157  (7/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Expert-Parallel Routing Fabric
file         : parts/t04_hardware/P0157_expert_parallel_fabric.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.expert_parallel_fabric
language     : Rust 1.86
capability   : cap.t04.expert.expert_parallel_fabric@1
determinism  : io
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Moves tokens to experts across the cluster at MoE speed.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. token dispatch/combine with all-to-all and capacity control
  2. locality-aware expert placement to shorten hops
  3. skew handling with overflow rerouting
  4. throughput at 512 experts across many nodes

Expanded obligations:
  1. Implement token dispatch/combine with all-to-all and capacity control,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement locality-aware expert placement to shorten hops with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement skew handling with overflow rerouting together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement throughput at 512 experts across many nodes as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.

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
  cap.t04.expert.expert_parallel_fabric@1
  cap.t04.expert.expert_parallel_fabric.describe@1

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

  cap.t04.comm.comm_scheduler@1
      if unavailable: use the in-file conservative substitute for
      `comm_scheduler` (documented, slower, lower quality) and set
      `degraded['comm_scheduler']='local'`

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
   3. [ 600 lines] Core implementation A - token dispatch/combine with all-to-all and capacity control
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - locality-aware expert placement to shorten hops
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - skew handling with overflow rerouting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput at 512 experts across many nodes
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
     exactly (capability == cap.t04.expert.expert_parallel_fabric@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0157_expert_parallel_fabric.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0158-sequence-parallel-fabric

**P0158 · `sequence_parallel_fabric` — Sequence & Context Parallel Fabric** · [spec](PART_SPECS_T04.md#p0158-sequence-parallel-fabric) · [self-contained txt](../prompts/P0158_sequence_parallel_fabric.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0158  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0158 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0158  (8/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Sequence & Context Parallel Fabric
file         : parts/t04_hardware/P0158_sequence_parallel_fabric.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.sequence_parallel_fabric
language     : Rust 1.86
capability   : cap.t04.sequence.sequence_parallel_fabric@1
determinism  : io
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Splits a single 1M-token context across machines.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. ring/striped context parallelism with overlapped attention communication
  2. KV shard placement and migration policy
  3. load balance under causal masking
  4. scaling efficiency for very long contexts

Expanded obligations:
  1. Implement ring/striped context parallelism with overlapped attention
     communication with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement KV shard placement and migration policy together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement load balance under causal masking as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement scaling efficiency for very long contexts, and make it correct
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.sequence.sequence_parallel_fabric@1
  cap.t04.sequence.sequence_parallel_fabric.describe@1

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

  cap.t04.expert.expert_parallel_fabric@1
      if unavailable: use the in-file conservative substitute for
      `expert_parallel_fabric` (documented, slower, lower quality) and set
      `degraded['expert_parallel_fabric']='local'`

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
   3. [ 600 lines] Core implementation A - ring/striped context parallelism with overlapped attention commu
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - KV shard placement and migration policy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - load balance under causal masking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - scaling efficiency for very long contexts
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
     exactly (capability == cap.t04.sequence.sequence_parallel_fabric@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0158_sequence_parallel_fabric.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0159-pipeline-fabric

**P0159 · `pipeline_fabric` — Pipeline Stage Transport** · [spec](PART_SPECS_T04.md#p0159-pipeline-fabric) · [self-contained txt](../prompts/P0159_pipeline_fabric.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0159  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0159 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0159  (9/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Pipeline Stage Transport
file         : parts/t04_hardware/P0159_pipeline_fabric.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.pipeline_fabric
language     : Rust 1.86
capability   : cap.t04.pipeline.pipeline_fabric@1
determinism  : io
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Activation and gradient movement between pipeline stages with no bubbles.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. point-to-point transfer with double buffering and prefetch
  2. stage-boundary compression for activation traffic
  3. backpressure integration with the pipeline schedule
  4. bubble-fraction measurement

Expanded obligations:
  1. Implement point-to-point transfer with double buffering and prefetch
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement stage-boundary compression for activation traffic as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement backpressure integration with the pipeline schedule, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement bubble-fraction measurement with an explicit *a-priori* cost
     model. Before doing the work the part must be able to state the tokens,
     FLOPs and microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Its contribution is measured
     against SWE-bench Verified — a regression on that benchmark is an
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.pipeline.pipeline_fabric@1
  cap.t04.pipeline.pipeline_fabric.describe@1

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

  cap.t04.sequence.sequence_parallel_fabric@1
      if unavailable: use the in-file conservative substitute for
      `sequence_parallel_fabric` (documented, slower, lower quality) and set
      `degraded['sequence_parallel_fabric']='local'`

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
   3. [ 600 lines] Core implementation A - point-to-point transfer with double buffering and prefetch
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - stage-boundary compression for activation traffic
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - backpressure integration with the pipeline schedule
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - bubble-fraction measurement
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
     exactly (capability == cap.t04.pipeline.pipeline_fabric@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0159_pipeline_fabric.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0160-param-server-shard

**P0160 · `param_server_shard` — Sharded Parameter Store** · [spec](PART_SPECS_T04.md#p0160-param-server-shard) · [self-contained txt](../prompts/P0160_param_server_shard.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0160  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0160 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0160  (10/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Sharded Parameter Store
file         : parts/t04_hardware/P0160_param_server_shard.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.param_server_shard
language     : Rust 1.86
capability   : cap.t04.param.param_server_shard@1
determinism  : io
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Where the weights live, and how they get to compute fast.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. shard mapping with replication factor and placement policy
  2. fast broadcast/gather of shards with topology awareness
  3. hot-shard replication for skewed access
  4. load time for a full model at cluster scale

Expanded obligations:
  1. Implement shard mapping with replication factor and placement policy as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement fast broadcast/gather of shards with topology awareness, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement hot-shard replication for skewed access with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement load time for a full model at cluster scale together with its
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.param.param_server_shard@1
  cap.t04.param.param_server_shard.describe@1

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

  cap.t04.pipeline.pipeline_fabric@1
      if unavailable: use the in-file conservative substitute for
      `pipeline_fabric` (documented, slower, lower quality) and set
      `degraded['pipeline_fabric']='local'`

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
   3. [ 600 lines] Core implementation A - shard mapping with replication factor and placement policy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fast broadcast/gather of shards with topology awareness
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hot-shard replication for skewed access
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - load time for a full model at cluster scale
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
     exactly (capability == cap.t04.param.param_server_shard@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0160_param_server_shard.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0161-weight-streaming

**P0161 · `weight_streaming` — Weight Streaming & Tiering** · [spec](PART_SPECS_T04.md#p0161-weight-streaming) · [self-contained txt](../prompts/P0161_weight_streaming.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0161  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0161 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0161  (11/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Weight Streaming & Tiering
file         : parts/t04_hardware/P0161_weight_streaming.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.weight_streaming
language     : Rust 1.86
capability   : cap.t04.weight.weight_streaming@1
determinism  : io
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Runs models larger than device memory without stalling.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. prefetch schedule derived from the execution plan
  2. multi-tier residency (device/host/NVMe) with cost-aware placement
  3. double-buffered layer streaming overlapped with compute
  4. stall-time measurement at multiple memory ratios

Expanded obligations:
  1. Implement prefetch schedule derived from the execution plan, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement multi-tier residency (device/host/NVMe) with cost-aware
     placement with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  3. Implement double-buffered layer streaming overlapped with compute
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement stall-time measurement at multiple memory ratios as a
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.weight.weight_streaming@1
  cap.t04.weight.weight_streaming.describe@1

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

  cap.t04.param.param_server_shard@1
      if unavailable: use the in-file conservative substitute for
      `param_server_shard` (documented, slower, lower quality) and set
      `degraded['param_server_shard']='local'`

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
   3. [ 600 lines] Core implementation A - prefetch schedule derived from the execution plan
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - multi-tier residency (device/host/NVMe) with cost-aware placemen
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - double-buffered layer streaming overlapped with compute
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - stall-time measurement at multiple memory ratios
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
     exactly (capability == cap.t04.weight.weight_streaming@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0161_weight_streaming.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0162-nvme-offload

**P0162 · `nvme_offload` — NVMe / Storage Offload Engine** · [spec](PART_SPECS_T04.md#p0162-nvme-offload) · [self-contained txt](../prompts/P0162_nvme_offload.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0162  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0162 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0162  (12/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : NVMe / Storage Offload Engine
file         : parts/t04_hardware/P0162_nvme_offload.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.nvme_offload
language     : Rust 1.86
capability   : cap.t04.nvme.nvme_offload@1
determinism  : io
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
High-throughput spill for KV caches, activations and cold weights.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. direct-IO with queue depth tuning and alignment handling
  2. GPU-direct storage paths where available
  3. wear-aware write policy and lifetime accounting
  4. achieved throughput versus device specification

Expanded obligations:
  1. Implement direct-IO with queue depth tuning and alignment handling with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement GPU-direct storage paths where available together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement wear-aware write policy and lifetime accounting as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement achieved throughput versus device specification, and make it
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.nvme.nvme_offload@1
  cap.t04.nvme.nvme_offload.describe@1

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

  cap.t04.weight.weight_streaming@1
      if unavailable: use the in-file conservative substitute for
      `weight_streaming` (documented, slower, lower quality) and set
      `degraded['weight_streaming']='local'`

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
   3. [ 600 lines] Core implementation A - direct-IO with queue depth tuning and alignment handling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - GPU-direct storage paths where available
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - wear-aware write policy and lifetime accounting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - achieved throughput versus device specification
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
     exactly (capability == cap.t04.nvme.nvme_offload@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0162_nvme_offload.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0163-host-pinned-pool

**P0163 · `host_pinned_pool` — Host Pinned Memory Manager** · [spec](PART_SPECS_T04.md#p0163-host-pinned-pool) · [self-contained txt](../prompts/P0163_host_pinned_pool.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0163  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0163 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0163  (13/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Host Pinned Memory Manager
file         : parts/t04_hardware/P0163_host_pinned_pool.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.host_pinned_pool
language     : Rust 1.86
capability   : cap.t04.host.host_pinned_pool@1
determinism  : io
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Staging memory that never becomes a bottleneck or a leak.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. pinned pool with size classes and NUMA affinity
  2. registration caching across transfers
  3. leak/exhaustion detection with actionable diagnostics
  4. transfer-rate measurement versus unpinned baseline

Expanded obligations:
  1. Implement pinned pool with size classes and NUMA affinity together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement registration caching across transfers as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement leak/exhaustion detection with actionable diagnostics, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement transfer-rate measurement versus unpinned baseline with an
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.host.host_pinned_pool@1
  cap.t04.host.host_pinned_pool.describe@1

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

  cap.t04.nvme.nvme_offload@1
      if unavailable: use the in-file conservative substitute for
      `nvme_offload` (documented, slower, lower quality) and set
      `degraded['nvme_offload']='local'`

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
   3. [ 600 lines] Core implementation A - pinned pool with size classes and NUMA affinity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - registration caching across transfers
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - leak/exhaustion detection with actionable diagnostics
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - transfer-rate measurement versus unpinned baseline
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
     exactly (capability == cap.t04.host.host_pinned_pool@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0163_host_pinned_pool.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0164-device-health

**P0164 · `device_health` — Device Health Monitoring & Prediction** · [spec](PART_SPECS_T04.md#p0164-device-health) · [self-contained txt](../prompts/P0164_device_health.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0164  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0164 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0164  (14/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Device Health Monitoring & Prediction
file         : parts/t04_hardware/P0164_device_health.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.device_health
language     : Rust 1.86
capability   : cap.t04.device.device_health@1
determinism  : io
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Detects a degrading accelerator before it corrupts a run.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. telemetry ingestion: ECC, throttling, clocks, link errors, temperature
  2. anomaly detection and remaining-useful-life estimation
  3. pre-emptive drain recommendation with cost/benefit
  4. detection-rate evaluation on injected degradation

Expanded obligations:
  1. Implement telemetry ingestion: ECC, throttling, clocks, link errors,
     temperature as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement anomaly detection and remaining-useful-life estimation, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement pre-emptive drain recommendation with cost/benefit with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement detection-rate evaluation on injected degradation together
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.device.device_health@1
  cap.t04.device.device_health.describe@1

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

  cap.t04.host.host_pinned_pool@1
      if unavailable: use the in-file conservative substitute for
      `host_pinned_pool` (documented, slower, lower quality) and set
      `degraded['host_pinned_pool']='local'`

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
   3. [ 600 lines] Core implementation A - telemetry ingestion: ECC, throttling, clocks, link errors, tempe
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - anomaly detection and remaining-useful-life estimation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - pre-emptive drain recommendation with cost/benefit
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - detection-rate evaluation on injected degradation
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
     exactly (capability == cap.t04.device.device_health@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0164_device_health.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0165-fault-domains

**P0165 · `fault_domains` — Fault Domain Modelling & Placement** · [spec](PART_SPECS_T04.md#p0165-fault-domains) · [self-contained txt](../prompts/P0165_fault_domains.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0165  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0165 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0165  (15/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Fault Domain Modelling & Placement
file         : parts/t04_hardware/P0165_fault_domains.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.fault_domains
language     : Rust 1.86
capability   : cap.t04.fault.fault_domains@1
determinism  : io
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Places replicas and shards so no single failure stops the assembly.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. failure-domain hierarchy (device, host, rack, zone) modelling
  2. correlated-failure-aware placement solver
  3. blast-radius computation for any single failure
  4. simulated-failure survival testing

Expanded obligations:
  1. Implement failure-domain hierarchy (device, host, rack, zone) modelling,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement correlated-failure-aware placement solver with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement blast-radius computation for any single failure together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement simulated-failure survival testing as a first-class, fully
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.fault.fault_domains@1
  cap.t04.fault.fault_domains.describe@1

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

  cap.t04.device.device_health@1
      if unavailable: use the in-file conservative substitute for
      `device_health` (documented, slower, lower quality) and set
      `degraded['device_health']='local'`

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
   3. [ 600 lines] Core implementation A - failure-domain hierarchy (device, host, rack, zone) modelling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - correlated-failure-aware placement solver
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blast-radius computation for any single failure
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - simulated-failure survival testing
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
     exactly (capability == cap.t04.fault.fault_domains@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0165_fault_domains.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0166-elastic-scaling

**P0166 · `elastic_scaling` — Elastic Membership & Rescaling** · [spec](PART_SPECS_T04.md#p0166-elastic-scaling) · [self-contained txt](../prompts/P0166_elastic_scaling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0166  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0166 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0166  (16/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Elastic Membership & Rescaling
file         : parts/t04_hardware/P0166_elastic_scaling.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.elastic_scaling
language     : Rust 1.86
capability   : cap.t04.elastic.elastic_scaling@1
determinism  : io
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Adds or removes machines mid-run without restarting.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. membership protocol with epochs and consistent views
  2. state redistribution with minimal data movement
  3. in-flight request preservation during rescale
  4. rescale latency and throughput-dip measurement

Expanded obligations:
  1. Implement membership protocol with epochs and consistent views with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement state redistribution with minimal data movement together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement in-flight request preservation during rescale as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement rescale latency and throughput-dip measurement, and make it
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.elastic.elastic_scaling@1
  cap.t04.elastic.elastic_scaling.describe@1

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

  cap.t04.fault.fault_domains@1
      if unavailable: use the in-file conservative substitute for
      `fault_domains` (documented, slower, lower quality) and set
      `degraded['fault_domains']='local'`

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
   3. [ 600 lines] Core implementation A - membership protocol with epochs and consistent views
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - state redistribution with minimal data movement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - in-flight request preservation during rescale
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - rescale latency and throughput-dip measurement
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
     exactly (capability == cap.t04.elastic.elastic_scaling@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0166_elastic_scaling.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0167-checkpoint-transport

**P0167 · `checkpoint_transport` — Distributed Checkpoint IO** · [spec](PART_SPECS_T04.md#p0167-checkpoint-transport) · [self-contained txt](../prompts/P0167_checkpoint_transport.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0167  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0167 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0167  (17/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Distributed Checkpoint IO
file         : parts/t04_hardware/P0167_checkpoint_transport.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.checkpoint_transport
language     : Rust 1.86
capability   : cap.t04.checkpoint.checkpoint_transport@1
determinism  : io
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Saves and restores petabyte-scale state fast and safely.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. sharded parallel write with aggregation to avoid small-file storms
  2. async checkpointing overlapped with compute
  3. integrity verification and partial-corruption recovery
  4. checkpoint/restore wall-clock measurement at scale

Expanded obligations:
  1. Implement sharded parallel write with aggregation to avoid small-file
     storms together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement async checkpointing overlapped with compute as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement integrity verification and partial-corruption recovery, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement checkpoint/restore wall-clock measurement at scale with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.checkpoint.checkpoint_transport@1
  cap.t04.checkpoint.checkpoint_transport.describe@1

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

  cap.t04.elastic.elastic_scaling@1
      if unavailable: use the in-file conservative substitute for
      `elastic_scaling` (documented, slower, lower quality) and set
      `degraded['elastic_scaling']='local'`

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
   3. [ 600 lines] Core implementation A - sharded parallel write with aggregation to avoid small-file stor
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - async checkpointing overlapped with compute
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - integrity verification and partial-corruption recovery
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - checkpoint/restore wall-clock measurement at scale
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
     exactly (capability == cap.t04.checkpoint.checkpoint_transport@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0167_checkpoint_transport.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0168-failure-recovery

**P0168 · `failure_recovery` — Failure Detection & Fast Restart** · [spec](PART_SPECS_T04.md#p0168-failure-recovery) · [self-contained txt](../prompts/P0168_failure_recovery.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0168  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0168 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0168  (18/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Failure Detection & Fast Restart
file         : parts/t04_hardware/P0168_failure_recovery.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.failure_recovery
language     : Rust 1.86
capability   : cap.t04.failure.failure_recovery@1
determinism  : io
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Turns a machine loss into a small hiccup rather than a lost run.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fast failure detection with false-positive suppression
  2. in-memory redundant state for immediate recovery
  3. partial restart limited to affected pipeline stages
  4. mean-time-to-recovery measurement under injected faults

Expanded obligations:
  1. Implement fast failure detection with false-positive suppression as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement in-memory redundant state for immediate recovery, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement partial restart limited to affected pipeline stages with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement mean-time-to-recovery measurement under injected faults
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.failure.failure_recovery@1
  cap.t04.failure.failure_recovery.describe@1

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

  cap.t04.checkpoint.checkpoint_transport@1
      if unavailable: use the in-file conservative substitute for
      `checkpoint_transport` (documented, slower, lower quality) and set
      `degraded['checkpoint_transport']='local'`

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
   3. [ 600 lines] Core implementation A - fast failure detection with false-positive suppression
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - in-memory redundant state for immediate recovery
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partial restart limited to affected pipeline stages
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - mean-time-to-recovery measurement under injected faults
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
     exactly (capability == cap.t04.failure.failure_recovery@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0168_failure_recovery.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0169-straggler-mitigation

**P0169 · `straggler_mitigation` — Straggler Detection & Mitigation** · [spec](PART_SPECS_T04.md#p0169-straggler-mitigation) · [self-contained txt](../prompts/P0169_straggler_mitigation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0169  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0169 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0169  (19/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Straggler Detection & Mitigation
file         : parts/t04_hardware/P0169_straggler_mitigation.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.straggler_mitigation
language     : Rust 1.86
capability   : cap.t04.straggler.straggler_mitigation@1
determinism  : io
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
One slow machine must not slow 100k others.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-rank latency distribution tracking with robust statistics
  2. speculative duplicate execution with first-wins semantics
  3. work stealing/rebalancing across ranks
  4. tail-latency improvement measurement

Expanded obligations:
  1. Implement per-rank latency distribution tracking with robust statistics,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement speculative duplicate execution with first-wins semantics with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement work stealing/rebalancing across ranks together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement tail-latency improvement measurement as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.straggler.straggler_mitigation@1
  cap.t04.straggler.straggler_mitigation.describe@1

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

  cap.t04.failure.failure_recovery@1
      if unavailable: use the in-file conservative substitute for
      `failure_recovery` (documented, slower, lower quality) and set
      `degraded['failure_recovery']='local'`

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
   3. [ 600 lines] Core implementation A - per-rank latency distribution tracking with robust statistics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - speculative duplicate execution with first-wins semantics
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - work stealing/rebalancing across ranks
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - tail-latency improvement measurement
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
     exactly (capability == cap.t04.straggler.straggler_mitigation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0169_straggler_mitigation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0170-power-cluster

**P0170 · `power_cluster` — Cluster Power & Energy Governance** · [spec](PART_SPECS_T04.md#p0170-power-cluster) · [self-contained txt](../prompts/P0170_power_cluster.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0170  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0170 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0170  (20/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Cluster Power & Energy Governance
file         : parts/t04_hardware/P0170_power_cluster.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.power_cluster
language     : Rust 1.86
capability   : cap.t04.power.power_cluster@1
determinism  : io
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Maximises throughput per watt within facility limits.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. power-cap-aware scheduling and frequency policy
  2. energy accounting per request and per part
  3. thermal-headroom-aware placement
  4. measured throughput-per-joule improvement

Expanded obligations:
  1. Implement power-cap-aware scheduling and frequency policy with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement energy accounting per request and per part together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement thermal-headroom-aware placement as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured throughput-per-joule improvement, and make it correct
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.power.power_cluster@1
  cap.t04.power.power_cluster.describe@1

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

  cap.t04.straggler.straggler_mitigation@1
      if unavailable: use the in-file conservative substitute for
      `straggler_mitigation` (documented, slower, lower quality) and set
      `degraded['straggler_mitigation']='local'`

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
   3. [ 600 lines] Core implementation A - power-cap-aware scheduling and frequency policy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - energy accounting per request and per part
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - thermal-headroom-aware placement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured throughput-per-joule improvement
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
     exactly (capability == cap.t04.power.power_cluster@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0170_power_cluster.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0171-network-congestion

**P0171 · `network_congestion` — Congestion Control & Traffic Engineering** · [spec](PART_SPECS_T04.md#p0171-network-congestion) · [self-contained txt](../prompts/P0171_network_congestion.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0171  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0171 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0171  (21/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Congestion Control & Traffic Engineering
file         : parts/t04_hardware/P0171_network_congestion.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.network_congestion
language     : Rust 1.86
capability   : cap.t04.network.network_congestion@1
determinism  : io
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Keeps the fabric out of collapse under all-to-all storms.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. adaptive routing and multipath spraying with reordering handling
  2. incast avoidance via pacing and receiver-driven scheduling
  3. congestion telemetry and hot-link detection
  4. goodput measurement under adversarial traffic patterns

Expanded obligations:
  1. Implement adaptive routing and multipath spraying with reordering
     handling together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement incast avoidance via pacing and receiver-driven scheduling as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement congestion telemetry and hot-link detection, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement goodput measurement under adversarial traffic patterns with an
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.network.network_congestion@1
  cap.t04.network.network_congestion.describe@1

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

  cap.t04.power.power_cluster@1
      if unavailable: use the in-file conservative substitute for
      `power_cluster` (documented, slower, lower quality) and set
      `degraded['power_cluster']='local'`

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
   3. [ 600 lines] Core implementation A - adaptive routing and multipath spraying with reordering handling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - incast avoidance via pacing and receiver-driven scheduling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - congestion telemetry and hot-link detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - goodput measurement under adversarial traffic patterns
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
     exactly (capability == cap.t04.network.network_congestion@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0171_network_congestion.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0172-multi-tenancy

**P0172 · `multi_tenancy` — Multi-Tenant Isolation & QoS** · [spec](PART_SPECS_T04.md#p0172-multi-tenancy) · [self-contained txt](../prompts/P0172_multi_tenancy.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0172  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0172 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0172  (22/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Multi-Tenant Isolation & QoS
file         : parts/t04_hardware/P0172_multi_tenancy.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.multi_tenancy
language     : Rust 1.86
capability   : cap.t04.multi.multi_tenancy@1
determinism  : io
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Many workloads on one cluster with hard performance isolation.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. resource partitioning with enforcement at device and fabric level
  2. QoS classes with latency SLOs and admission control
  3. noisy-neighbour detection and mitigation
  4. SLO-attainment measurement under contention

Expanded obligations:
  1. Implement resource partitioning with enforcement at device and fabric
     level as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement QoS classes with latency SLOs and admission control, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement noisy-neighbour detection and mitigation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement SLO-attainment measurement under contention together with its
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.multi.multi_tenancy@1
  cap.t04.multi.multi_tenancy.describe@1

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

  cap.t04.network.network_congestion@1
      if unavailable: use the in-file conservative substitute for
      `network_congestion` (documented, slower, lower quality) and set
      `degraded['network_congestion']='local'`

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
   3. [ 600 lines] Core implementation A - resource partitioning with enforcement at device and fabric leve
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - QoS classes with latency SLOs and admission control
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - noisy-neighbour detection and mitigation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - SLO-attainment measurement under contention
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
     exactly (capability == cap.t04.multi.multi_tenancy@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0172_multi_tenancy.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0173-device-virtualisation

**P0173 · `device_virtualisation` — Device Partitioning & Virtualisation** · [spec](PART_SPECS_T04.md#p0173-device-virtualisation) · [self-contained txt](../prompts/P0173_device_virtualisation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0173  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0173 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0173  (23/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Device Partitioning & Virtualisation
file         : parts/t04_hardware/P0173_device_virtualisation.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.device_virtualisation
language     : Rust 1.86
capability   : cap.t04.device.device_virtualisation@1
determinism  : io
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Slices accelerators for small requests without waste.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. partition creation, sizing policy and lifecycle
  2. performance-isolation verification between partitions
  3. packing solver maximising utilisation under SLOs
  4. utilisation improvement measurement

Expanded obligations:
  1. Implement partition creation, sizing policy and lifecycle, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement performance-isolation verification between partitions with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement packing solver maximising utilisation under SLOs together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement utilisation improvement measurement as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.device.device_virtualisation@1
  cap.t04.device.device_virtualisation.describe@1

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

  cap.t04.multi.multi_tenancy@1
      if unavailable: use the in-file conservative substitute for
      `multi_tenancy` (documented, slower, lower quality) and set
      `degraded['multi_tenancy']='local'`

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
   3. [ 600 lines] Core implementation A - partition creation, sizing policy and lifecycle
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - performance-isolation verification between partitions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - packing solver maximising utilisation under SLOs
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
     exactly (capability == cap.t04.device.device_virtualisation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0173_device_virtualisation.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0174-heterogeneous-pool

**P0174 · `heterogeneous_pool` — Heterogeneous Hardware Pooling** · [spec](PART_SPECS_T04.md#p0174-heterogeneous-pool) · [self-contained txt](../prompts/P0174_heterogeneous_pool.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0174  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0174 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0174  (24/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Heterogeneous Hardware Pooling
file         : parts/t04_hardware/P0174_heterogeneous_pool.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.heterogeneous_pool
language     : Rust 1.86
capability   : cap.t04.heterogeneous.heterogeneous_pool@1
determinism  : io
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Uses every generation and vendor of accelerator effectively together.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capability-aware work routing with per-device cost models
  2. mixed-generation collective handling with slowest-link awareness
  3. graceful capability degradation for older devices
  4. aggregate-throughput measurement across mixed pools

Expanded obligations:
  1. Implement capability-aware work routing with per-device cost models with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement mixed-generation collective handling with slowest-link
     awareness together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement graceful capability degradation for older devices as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement aggregate-throughput measurement across mixed pools, and make
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.heterogeneous.heterogeneous_pool@1
  cap.t04.heterogeneous.heterogeneous_pool.describe@1

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

  cap.t04.device.device_virtualisation@1
      if unavailable: use the in-file conservative substitute for
      `device_virtualisation` (documented, slower, lower quality) and set
      `degraded['device_virtualisation']='local'`

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
   3. [ 600 lines] Core implementation A - capability-aware work routing with per-device cost models
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - mixed-generation collective handling with slowest-link awareness
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - graceful capability degradation for older devices
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - aggregate-throughput measurement across mixed pools
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
     exactly (capability == cap.t04.heterogeneous.heterogeneous_pool@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0174_heterogeneous_pool.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0175-edge-runtime

**P0175 · `edge_runtime` — Edge & On-Device Runtime** · [spec](PART_SPECS_T04.md#p0175-edge-runtime) · [self-contained txt](../prompts/P0175_edge_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0175  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0175 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0175  (25/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Edge & On-Device Runtime
file         : parts/t04_hardware/P0175_edge_runtime.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.edge_runtime
language     : Rust 1.86
capability   : cap.t04.edge.edge_runtime@1
determinism  : io
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Runs the distilled fast paths on laptops, phones and embedded targets.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tight memory-budget execution with streaming weights
  2. battery/thermal-aware scheduling
  3. capability subset declaration and cloud handoff protocol
  4. latency/quality measurements on constrained targets

Expanded obligations:
  1. Implement tight memory-budget execution with streaming weights together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement battery/thermal-aware scheduling as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement capability subset declaration and cloud handoff protocol, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement latency/quality measurements on constrained targets with an
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.edge.edge_runtime@1
  cap.t04.edge.edge_runtime.describe@1

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

  cap.t04.heterogeneous.heterogeneous_pool@1
      if unavailable: use the in-file conservative substitute for
      `heterogeneous_pool` (documented, slower, lower quality) and set
      `degraded['heterogeneous_pool']='local'`

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
   3. [ 600 lines] Core implementation A - tight memory-budget execution with streaming weights
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - battery/thermal-aware scheduling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - capability subset declaration and cloud handoff protocol
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency/quality measurements on constrained targets
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
     exactly (capability == cap.t04.edge.edge_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0175_edge_runtime.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0176-cloud-provisioner

**P0176 · `cloud_provisioner` — Capacity Provisioning & Placement Planner** · [spec](PART_SPECS_T04.md#p0176-cloud-provisioner) · [self-contained txt](../prompts/P0176_cloud_provisioner.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0176  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0176 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0176  (26/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Capacity Provisioning & Placement Planner
file         : parts/t04_hardware/P0176_cloud_provisioner.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.cloud_provisioner
language     : Rust 1.86
capability   : cap.t04.cloud.cloud_provisioner@1
determinism  : io
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Decides what hardware to acquire and where to run each workload.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. demand forecasting from request traces
  2. cost/latency/carbon multi-objective placement
  3. spot/preemptible capacity strategy with checkpoint coupling
  4. cost-per-request reduction measurement

Expanded obligations:
  1. Implement demand forecasting from request traces as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement cost/latency/carbon multi-objective placement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement spot/preemptible capacity strategy with checkpoint coupling
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement cost-per-request reduction measurement together with its
     verification path, so that anything this mechanism produces can be
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.cloud.cloud_provisioner@1
  cap.t04.cloud.cloud_provisioner.describe@1

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

  cap.t04.edge.edge_runtime@1
      if unavailable: use the in-file conservative substitute for
      `edge_runtime` (documented, slower, lower quality) and set
      `degraded['edge_runtime']='local'`

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
   3. [ 600 lines] Core implementation A - demand forecasting from request traces
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost/latency/carbon multi-objective placement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - spot/preemptible capacity strategy with checkpoint coupling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost-per-request reduction measurement
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
     exactly (capability == cap.t04.cloud.cloud_provisioner@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0176_cloud_provisioner.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0177-scheduler-cluster

**P0177 · `scheduler_cluster` — Cluster Job Scheduler Integration** · [spec](PART_SPECS_T04.md#p0177-scheduler-cluster) · [self-contained txt](../prompts/P0177_scheduler_cluster.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0177  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0177 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0177  (27/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Cluster Job Scheduler Integration
file         : parts/t04_hardware/P0177_scheduler_cluster.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.scheduler_cluster
language     : Rust 1.86
capability   : cap.t04.scheduler.scheduler_cluster@1
determinism  : io
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Plays well with Slurm/Kubernetes-class schedulers without losing control.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gang scheduling and topology-aware allocation requests
  2. preemption handling with fast drain and resume
  3. queue-time prediction and backfill exploitation
  4. allocation-quality measurement (topology compactness)

Expanded obligations:
  1. Implement gang scheduling and topology-aware allocation requests, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement preemption handling with fast drain and resume with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement queue-time prediction and backfill exploitation together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement allocation-quality measurement (topology compactness) as a
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.scheduler.scheduler_cluster@1
  cap.t04.scheduler.scheduler_cluster.describe@1

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

  cap.t04.cloud.cloud_provisioner@1
      if unavailable: use the in-file conservative substitute for
      `cloud_provisioner` (documented, slower, lower quality) and set
      `degraded['cloud_provisioner']='local'`

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
   3. [ 600 lines] Core implementation A - gang scheduling and topology-aware allocation requests
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - preemption handling with fast drain and resume
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - queue-time prediction and backfill exploitation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - allocation-quality measurement (topology compactness)
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
     exactly (capability == cap.t04.scheduler.scheduler_cluster@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0177_scheduler_cluster.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0178-service-discovery

**P0178 · `service_discovery` — Service Discovery & Membership Registry** · [spec](PART_SPECS_T04.md#p0178-service-discovery) · [self-contained txt](../prompts/P0178_service_discovery.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0178  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0178 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0178  (28/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Service Discovery & Membership Registry
file         : parts/t04_hardware/P0178_service_discovery.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.service_discovery
language     : Rust 1.86
capability   : cap.t04.service.service_discovery@1
determinism  : io
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
How 1000 parts across many machines find each other.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gossip/consensus-backed registry with fast convergence
  2. capability-indexed lookup with locality preference
  3. partition tolerance behaviour and split-brain avoidance
  4. convergence-time measurement at 100k nodes

Expanded obligations:
  1. Implement gossip/consensus-backed registry with fast convergence with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement capability-indexed lookup with locality preference together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement partition tolerance behaviour and split-brain avoidance as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement convergence-time measurement at 100k nodes, and make it
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.service.service_discovery@1
  cap.t04.service.service_discovery.describe@1

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

  cap.t04.scheduler.scheduler_cluster@1
      if unavailable: use the in-file conservative substitute for
      `scheduler_cluster` (documented, slower, lower quality) and set
      `degraded['scheduler_cluster']='local'`

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
   3. [ 600 lines] Core implementation A - gossip/consensus-backed registry with fast convergence
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability-indexed lookup with locality preference
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partition tolerance behaviour and split-brain avoidance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - convergence-time measurement at 100k nodes
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
     exactly (capability == cap.t04.service.service_discovery@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0178_service_discovery.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0179-consensus-core

**P0179 · `consensus_core` — Lightweight Consensus & Leader Election** · [spec](PART_SPECS_T04.md#p0179-consensus-core) · [self-contained txt](../prompts/P0179_consensus_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0179  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0179 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0179  (29/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Lightweight Consensus & Leader Election
file         : parts/t04_hardware/P0179_consensus_core.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.consensus_core
language     : Rust 1.86
capability   : cap.t04.consensus.consensus_core@1
determinism  : io
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Consistency for control-plane decisions only, never in the hot path.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. Raft-style log replication with pre-vote and joint consensus
  2. lease-based leadership with clock-skew safety
  3. linearisability testing under partitions
  4. control-plane latency budget enforcement

Expanded obligations:
  1. Implement Raft-style log replication with pre-vote and joint consensus
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement lease-based leadership with clock-skew safety as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement linearisability testing under partitions, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement control-plane latency budget enforcement with an explicit
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
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.consensus.consensus_core@1
  cap.t04.consensus.consensus_core.describe@1

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

  cap.t04.service.service_discovery@1
      if unavailable: use the in-file conservative substitute for
      `service_discovery` (documented, slower, lower quality) and set
      `degraded['service_discovery']='local'`

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
   3. [ 600 lines] Core implementation A - Raft-style log replication with pre-vote and joint consensus
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - lease-based leadership with clock-skew safety
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - linearisability testing under partitions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - control-plane latency budget enforcement
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
     exactly (capability == cap.t04.consensus.consensus_core@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0179_consensus_core.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0180-distributed-lock

**P0180 · `distributed_lock` — Distributed Locking & Fencing** · [spec](PART_SPECS_T04.md#p0180-distributed-lock) · [self-contained txt](../prompts/P0180_distributed_lock.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0180  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0180 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0180  (30/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Distributed Locking & Fencing
file         : parts/t04_hardware/P0180_distributed_lock.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.distributed_lock
language     : Rust 1.86
capability   : cap.t04.distributed.distributed_lock@1
determinism  : io
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Prevents two workers from ever doing the same irreversible thing.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. lease locks with monotonic fencing tokens
  2. lock-holder failure detection and safe takeover
  3. deadlock avoidance with ordered acquisition
  4. safety verification under process pauses and clock jumps

Expanded obligations:
  1. Implement lease locks with monotonic fencing tokens as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement lock-holder failure detection and safe takeover, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement deadlock avoidance with ordered acquisition with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement safety verification under process pauses and clock jumps
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.distributed.distributed_lock@1
  cap.t04.distributed.distributed_lock.describe@1

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

  cap.t04.consensus.consensus_core@1
      if unavailable: use the in-file conservative substitute for
      `consensus_core` (documented, slower, lower quality) and set
      `degraded['consensus_core']='local'`

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
   3. [ 600 lines] Core implementation A - lease locks with monotonic fencing tokens
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - lock-holder failure detection and safe takeover
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deadlock avoidance with ordered acquisition
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - safety verification under process pauses and clock jumps
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
     exactly (capability == cap.t04.distributed.distributed_lock@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0180_distributed_lock.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0181-clock-sync

**P0181 · `clock_sync` — Cluster Clock Synchronisation** · [spec](PART_SPECS_T04.md#p0181-clock-sync) · [self-contained txt](../prompts/P0181_clock_sync.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0181  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0181 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0181  (31/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Cluster Clock Synchronisation
file         : parts/t04_hardware/P0181_clock_sync.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.clock_sync
language     : Rust 1.86
capability   : cap.t04.clock.clock_sync@1
determinism  : io
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Enough time agreement to reason about causality and deadlines.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. PTP/NTP ingestion with uncertainty intervals
  2. hybrid logical clocks for causal ordering
  3. skew-bound enforcement in deadline arithmetic
  4. measured uncertainty and its effect on SLOs

Expanded obligations:
  1. Implement PTP/NTP ingestion with uncertainty intervals, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement hybrid logical clocks for causal ordering with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement skew-bound enforcement in deadline arithmetic together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured uncertainty and its effect on SLOs as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.

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
  cap.t04.clock.clock_sync@1
  cap.t04.clock.clock_sync.describe@1

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

  cap.t04.distributed.distributed_lock@1
      if unavailable: use the in-file conservative substitute for
      `distributed_lock` (documented, slower, lower quality) and set
      `degraded['distributed_lock']='local'`

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
   3. [ 600 lines] Core implementation A - PTP/NTP ingestion with uncertainty intervals
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hybrid logical clocks for causal ordering
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - skew-bound enforcement in deadline arithmetic
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured uncertainty and its effect on SLOs
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
     exactly (capability == cap.t04.clock.clock_sync@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0181_clock_sync.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0182-data-locality

**P0182 · `data_locality` — Data Locality & Cache Affinity Router** · [spec](PART_SPECS_T04.md#p0182-data-locality) · [self-contained txt](../prompts/P0182_data_locality.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0182  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0182 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0182  (32/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Data Locality & Cache Affinity Router
file         : parts/t04_hardware/P0182_data_locality.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.data_locality
language     : Rust 1.86
capability   : cap.t04.data.data_locality@1
determinism  : io
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Routes work to where the bytes already are.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. consistent hashing with bounded loads and affinity keys
  2. KV-cache-aware routing for multi-turn sessions
  3. migration cost estimation versus remote-access cost
  4. cache-hit-rate improvement measurement

Expanded obligations:
  1. Implement consistent hashing with bounded loads and affinity keys with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement KV-cache-aware routing for multi-turn sessions together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement migration cost estimation versus remote-access cost as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement cache-hit-rate improvement measurement, and make it correct
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
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.data.data_locality@1
  cap.t04.data.data_locality.describe@1

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

  cap.t04.clock.clock_sync@1
      if unavailable: use the in-file conservative substitute for
      `clock_sync` (documented, slower, lower quality) and set
      `degraded['clock_sync']='local'`

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
   3. [ 600 lines] Core implementation A - consistent hashing with bounded loads and affinity keys
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - KV-cache-aware routing for multi-turn sessions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - migration cost estimation versus remote-access cost
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cache-hit-rate improvement measurement
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
     exactly (capability == cap.t04.data.data_locality@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0182_data_locality.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0183-bandwidth-accounting

**P0183 · `bandwidth_accounting` — Bandwidth & Interconnect Accounting** · [spec](PART_SPECS_T04.md#p0183-bandwidth-accounting) · [self-contained txt](../prompts/P0183_bandwidth_accounting.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0183  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0183 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0183  (33/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Bandwidth & Interconnect Accounting
file         : parts/t04_hardware/P0183_bandwidth_accounting.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.bandwidth_accounting
language     : Rust 1.86
capability   : cap.t04.bandwidth.bandwidth_accounting@1
determinism  : io
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Makes every byte moved visible and attributable.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-link, per-tier, per-request byte accounting
  2. attribution to parts and phases with negligible overhead
  3. budget enforcement on communication volume
  4. report used by the compiler to reduce traffic

Expanded obligations:
  1. Implement per-link, per-tier, per-request byte accounting together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement attribution to parts and phases with negligible overhead as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement budget enforcement on communication volume, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement report used by the compiler to reduce traffic with an explicit
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.bandwidth.bandwidth_accounting@1
  cap.t04.bandwidth.bandwidth_accounting.describe@1

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

  cap.t04.data.data_locality@1
      if unavailable: use the in-file conservative substitute for
      `data_locality` (documented, slower, lower quality) and set
      `degraded['data_locality']='local'`

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
   3. [ 600 lines] Core implementation A - per-link, per-tier, per-request byte accounting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - attribution to parts and phases with negligible overhead
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - budget enforcement on communication volume
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - report used by the compiler to reduce traffic
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
     exactly (capability == cap.t04.bandwidth.bandwidth_accounting@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0183_bandwidth_accounting.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0184-secure-channel

**P0184 · `secure_channel` — Encrypted Inter-Node Channels** · [spec](PART_SPECS_T04.md#p0184-secure-channel) · [self-contained txt](../prompts/P0184_secure_channel.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0184  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0184 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0184  (34/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Encrypted Inter-Node Channels
file         : parts/t04_hardware/P0184_secure_channel.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.secure_channel
language     : Rust 1.86
capability   : cap.t04.secure.secure_channel@1
determinism  : io
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Confidentiality and integrity without losing throughput.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mutual authentication with short-lived certificates
  2. AEAD framing with hardware offload where available
  3. key rotation without connection drops
  4. throughput cost measurement of encryption

Expanded obligations:
  1. Implement mutual authentication with short-lived certificates as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement AEAD framing with hardware offload where available, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement key rotation without connection drops with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement throughput cost measurement of encryption together with its
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.secure.secure_channel@1
  cap.t04.secure.secure_channel.describe@1

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

  cap.t04.bandwidth.bandwidth_accounting@1
      if unavailable: use the in-file conservative substitute for
      `bandwidth_accounting` (documented, slower, lower quality) and set
      `degraded['bandwidth_accounting']='local'`

  cap.t02.gemm.gemm_int4@1
      if unavailable: use the in-file conservative substitute for
      `gemm_int4` (documented, slower, lower quality) and set
      `degraded['gemm_int4']='local'`

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
   3. [ 600 lines] Core implementation A - mutual authentication with short-lived certificates
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - AEAD framing with hardware offload where available
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - key rotation without connection drops
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput cost measurement of encryption
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
     exactly (capability == cap.t04.secure.secure_channel@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0184_secure_channel.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0185-confidential-compute

**P0185 · `confidential_compute` — Confidential Computing Integration** · [spec](PART_SPECS_T04.md#p0185-confidential-compute) · [self-contained txt](../prompts/P0185_confidential_compute.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0185  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0185 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0185  (35/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Confidential Computing Integration
file         : parts/t04_hardware/P0185_confidential_compute.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.confidential_compute
language     : Rust 1.86
capability   : cap.t04.confidential.confidential_compute@1
determinism  : io
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Runs sensitive workloads inside attested enclaves.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. attestation verification and policy binding
  2. encrypted memory handling and IO shim overhead management
  3. key release conditioned on measurement
  4. performance overhead measurement and mitigation

Expanded obligations:
  1. Implement attestation verification and policy binding, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement encrypted memory handling and IO shim overhead management with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement key release conditioned on measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement performance overhead measurement and mitigation as a
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.confidential.confidential_compute@1
  cap.t04.confidential.confidential_compute.describe@1

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

  cap.t04.secure.secure_channel@1
      if unavailable: use the in-file conservative substitute for
      `secure_channel` (documented, slower, lower quality) and set
      `degraded['secure_channel']='local'`

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
   3. [ 600 lines] Core implementation A - attestation verification and policy binding
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - encrypted memory handling and IO shim overhead management
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - key release conditioned on measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - performance overhead measurement and mitigation
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
     exactly (capability == cap.t04.confidential.confidential_compute@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0185_confidential_compute.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0186-firmware-compat

**P0186 · `firmware_compat` — Driver & Firmware Compatibility Matrix** · [spec](PART_SPECS_T04.md#p0186-firmware-compat) · [self-contained txt](../prompts/P0186_firmware_compat.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0186  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0186 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0186  (36/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Driver & Firmware Compatibility Matrix
file         : parts/t04_hardware/P0186_firmware_compat.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.firmware_compat
language     : Rust 1.86
capability   : cap.t04.firmware.firmware_compat@1
determinism  : io
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Prevents the classic 'works on that node' failure class.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. version detection, known-issue database and hard gating
  2. capability differences normalised into the target description
  3. pre-flight validation suite run at node admission
  4. matrix coverage report

Expanded obligations:
  1. Implement version detection, known-issue database and hard gating with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement capability differences normalised into the target description
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement pre-flight validation suite run at node admission as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement matrix coverage report, and make it correct under concurrency:
     at least 64 in-flight `OmegaEnvelope`s must be able to traverse it
     simultaneously. No lock, mutex or borrow may be held across an `await` /
     `.await` / `yield` boundary, and the part must expose a contention
     counter so T09 can attribute latency to it. Its contribution is measured
     against SWE-bench Verified — a regression on that benchmark is an
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
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.firmware.firmware_compat@1
  cap.t04.firmware.firmware_compat.describe@1

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

  cap.t04.confidential.confidential_compute@1
      if unavailable: use the in-file conservative substitute for
      `confidential_compute` (documented, slower, lower quality) and set
      `degraded['confidential_compute']='local'`

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
   3. [ 600 lines] Core implementation A - version detection, known-issue database and hard gating
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability differences normalised into the target description
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - pre-flight validation suite run at node admission
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - matrix coverage report
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
     exactly (capability == cap.t04.firmware.firmware_compat@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0186_firmware_compat.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0187-nic-offload

**P0187 · `nic_offload` — Network Offload & In-Network Compute** · [spec](PART_SPECS_T04.md#p0187-nic-offload) · [self-contained txt](../prompts/P0187_nic_offload.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0187  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0187 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0187  (37/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Network Offload & In-Network Compute
file         : parts/t04_hardware/P0187_nic_offload.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.nic_offload
language     : Rust 1.86
capability   : cap.t04.nic.nic_offload@1
determinism  : io
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Pushes reductions and packet work into NICs and switches.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. in-network all-reduce integration with fallback
  2. kernel-bypass datapath with poll-mode threads
  3. offload correctness verification versus host computation
  4. measured host-CPU and latency savings

Expanded obligations:
  1. Implement in-network all-reduce integration with fallback together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement kernel-bypass datapath with poll-mode threads as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement offload correctness verification versus host computation, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement measured host-CPU and latency savings with an explicit
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.nic.nic_offload@1
  cap.t04.nic.nic_offload.describe@1

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

  cap.t04.firmware.firmware_compat@1
      if unavailable: use the in-file conservative substitute for
      `firmware_compat` (documented, slower, lower quality) and set
      `degraded['firmware_compat']='local'`

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
   3. [ 600 lines] Core implementation A - in-network all-reduce integration with fallback
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - kernel-bypass datapath with poll-mode threads
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - offload correctness verification versus host computation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured host-CPU and latency savings
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
     exactly (capability == cap.t04.nic.nic_offload@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0187_nic_offload.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0188-device-reset

**P0188 · `device_reset` — Device Reset & Isolation Recovery** · [spec](PART_SPECS_T04.md#p0188-device-reset) · [self-contained txt](../prompts/P0188_device_reset.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0188  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0188 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0188  (38/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Device Reset & Isolation Recovery
file         : parts/t04_hardware/P0188_device_reset.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.device_reset
language     : Rust 1.86
capability   : cap.t04.device.device_reset@1
determinism  : io
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Recovers a wedged accelerator without rebooting the host.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hang detection with watchdogs and progress counters
  2. safe reset sequencing and state reconstruction
  3. poison propagation prevention to healthy devices
  4. recovery-success-rate measurement under injected hangs

Expanded obligations:
  1. Implement hang detection with watchdogs and progress counters as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement safe reset sequencing and state reconstruction, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement poison propagation prevention to healthy devices with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement recovery-success-rate measurement under injected hangs
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.device.device_reset@1
  cap.t04.device.device_reset.describe@1

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

  cap.t04.nic.nic_offload@1
      if unavailable: use the in-file conservative substitute for
      `nic_offload` (documented, slower, lower quality) and set
      `degraded['nic_offload']='local'`

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
   3. [ 600 lines] Core implementation A - hang detection with watchdogs and progress counters
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - safe reset sequencing and state reconstruction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - poison propagation prevention to healthy devices
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - recovery-success-rate measurement under injected hangs
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
     exactly (capability == cap.t04.device.device_reset@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0188_device_reset.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0189-numa-topology-cluster

**P0189 · `numa_topology_cluster` — Host-Level Resource Topology Binding** · [spec](PART_SPECS_T04.md#p0189-numa-topology-cluster) · [self-contained txt](../prompts/P0189_numa_topology_cluster.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0189  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0189 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0189  (39/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Host-Level Resource Topology Binding
file         : parts/t04_hardware/P0189_numa_topology_cluster.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.numa_topology_cluster
language     : Rust 1.86
capability   : cap.t04.numa.numa_topology_cluster@1
determinism  : io
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Binds threads, memory, devices and NICs coherently.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. CPU/GPU/NIC affinity solver from the topology graph
  2. IRQ and interrupt-affinity configuration guidance
  3. hugepage and transparent-hugepage policy
  4. measured latency improvement from correct binding

Expanded obligations:
  1. Implement CPU/GPU/NIC affinity solver from the topology graph, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement IRQ and interrupt-affinity configuration guidance with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement hugepage and transparent-hugepage policy together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured latency improvement from correct binding as a
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.numa.numa_topology_cluster@1
  cap.t04.numa.numa_topology_cluster.describe@1

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

  cap.t04.device.device_reset@1
      if unavailable: use the in-file conservative substitute for
      `device_reset` (documented, slower, lower quality) and set
      `degraded['device_reset']='local'`

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
   3. [ 600 lines] Core implementation A - CPU/GPU/NIC affinity solver from the topology graph
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - IRQ and interrupt-affinity configuration guidance
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hugepage and transparent-hugepage policy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured latency improvement from correct binding
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
     exactly (capability == cap.t04.numa.numa_topology_cluster@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0189_numa_topology_cluster.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0190-telemetry-transport

**P0190 · `telemetry_transport` — High-Volume Telemetry Pipeline** · [spec](PART_SPECS_T04.md#p0190-telemetry-transport) · [self-contained txt](../prompts/P0190_telemetry_transport.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0190  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0190 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0190  (40/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : High-Volume Telemetry Pipeline
file         : parts/t04_hardware/P0190_telemetry_transport.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.telemetry_transport
language     : Rust 1.86
capability   : cap.t04.telemetry.telemetry_transport@1
determinism  : io
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Ships metrics, traces and events from 100k nodes without cost explosion.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. local aggregation and pre-summarisation before egress
  2. adaptive sampling with error-bound guarantees
  3. backpressure and loss accounting
  4. telemetry cost per request measurement

Expanded obligations:
  1. Implement local aggregation and pre-summarisation before egress with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement adaptive sampling with error-bound guarantees together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement backpressure and loss accounting as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement telemetry cost per request measurement, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.telemetry.telemetry_transport@1
  cap.t04.telemetry.telemetry_transport.describe@1

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

  cap.t04.numa.numa_topology_cluster@1
      if unavailable: use the in-file conservative substitute for
      `numa_topology_cluster` (documented, slower, lower quality) and set
      `degraded['numa_topology_cluster']='local'`

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
   3. [ 600 lines] Core implementation A - local aggregation and pre-summarisation before egress
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - adaptive sampling with error-bound guarantees
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - backpressure and loss accounting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - telemetry cost per request measurement
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
     exactly (capability == cap.t04.telemetry.telemetry_transport@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0190_telemetry_transport.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0191-simulation-cluster

**P0191 · `simulation_cluster` — Cluster Simulator** · [spec](PART_SPECS_T04.md#p0191-simulation-cluster) · [self-contained txt](../prompts/P0191_simulation_cluster.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0191  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0191 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0191  (41/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Cluster Simulator
file         : parts/t04_hardware/P0191_simulation_cluster.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.simulation_cluster
language     : Rust 1.86
capability   : cap.t04.simulation.simulation_cluster@1
determinism  : io
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Tests distributed logic at 100k scale on one machine.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. discrete-event simulation of compute, memory and network
  2. fault, straggler and partition injection scenarios
  3. calibration against real measurements with error reporting
  4. scenario library covering all failure modes

Expanded obligations:
  1. Implement discrete-event simulation of compute, memory and network
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement fault, straggler and partition injection scenarios as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement calibration against real measurements with error reporting,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement scenario library covering all failure modes with an explicit
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.simulation.simulation_cluster@1
  cap.t04.simulation.simulation_cluster.describe@1

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

  cap.t04.telemetry.telemetry_transport@1
      if unavailable: use the in-file conservative substitute for
      `telemetry_transport` (documented, slower, lower quality) and set
      `degraded['telemetry_transport']='local'`

  cap.t02.gemm.gemm_fp8@1
      if unavailable: use the in-file conservative substitute for `gemm_fp8`
      (documented, slower, lower quality) and set
      `degraded['gemm_fp8']='local'`

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
   3. [ 600 lines] Core implementation A - discrete-event simulation of compute, memory and network
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fault, straggler and partition injection scenarios
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - calibration against real measurements with error reporting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - scenario library covering all failure modes
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
     exactly (capability == cap.t04.simulation.simulation_cluster@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0191_simulation_cluster.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0192-capacity-benchmarks

**P0192 · `capacity_benchmarks` — Distributed Benchmark Suite** · [spec](PART_SPECS_T04.md#p0192-capacity-benchmarks) · [self-contained txt](../prompts/P0192_capacity_benchmarks.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0192  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0192 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0192  (42/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Distributed Benchmark Suite
file         : parts/t04_hardware/P0192_capacity_benchmarks.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.capacity_benchmarks
language     : Rust 1.86
capability   : cap.t04.capacity.capacity_benchmarks@1
determinism  : io
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The canonical scaling measurements for the whole platform.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. strong/weak scaling harnesses with statistical rigor
  2. communication microbenchmarks per link type
  3. end-to-end throughput and latency at multiple scales
  4. baseline records with machine fingerprints

Expanded obligations:
  1. Implement strong/weak scaling harnesses with statistical rigor as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement communication microbenchmarks per link type, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement end-to-end throughput and latency at multiple scales with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement baseline records with machine fingerprints together with its
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
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.capacity.capacity_benchmarks@1
  cap.t04.capacity.capacity_benchmarks.describe@1

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

  cap.t04.simulation.simulation_cluster@1
      if unavailable: use the in-file conservative substitute for
      `simulation_cluster` (documented, slower, lower quality) and set
      `degraded['simulation_cluster']='local'`

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
   3. [ 600 lines] Core implementation A - strong/weak scaling harnesses with statistical rigor
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - communication microbenchmarks per link type
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - end-to-end throughput and latency at multiple scales
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - baseline records with machine fingerprints
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
     exactly (capability == cap.t04.capacity.capacity_benchmarks@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0192_capacity_benchmarks.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0193-cost-model-cluster

**P0193 · `cost_model_cluster` — Total-Cost-of-Serving Model** · [spec](PART_SPECS_T04.md#p0193-cost-model-cluster) · [self-contained txt](../prompts/P0193_cost_model_cluster.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0193  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0193 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0193  (43/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Total-Cost-of-Serving Model
file         : parts/t04_hardware/P0193_cost_model_cluster.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.cost_model_cluster
language     : Rust 1.86
capability   : cap.t04.cost.cost_model_cluster@1
determinism  : io
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Turns hardware, power and time into dollars per request.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cost decomposition per device-hour, byte moved and joule
  2. amortisation of compilation, warmup and idle capacity
  3. what-if analysis for hardware and plan changes
  4. validation against measured billing data

Expanded obligations:
  1. Implement cost decomposition per device-hour, byte moved and joule, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement amortisation of compilation, warmup and idle capacity with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement what-if analysis for hardware and plan changes together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement validation against measured billing data as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.

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
  cap.t04.cost.cost_model_cluster@1
  cap.t04.cost.cost_model_cluster.describe@1

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

  cap.t04.capacity.capacity_benchmarks@1
      if unavailable: use the in-file conservative substitute for
      `capacity_benchmarks` (documented, slower, lower quality) and set
      `degraded['capacity_benchmarks']='local'`

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
   3. [ 600 lines] Core implementation A - cost decomposition per device-hour, byte moved and joule
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - amortisation of compilation, warmup and idle capacity
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - what-if analysis for hardware and plan changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - validation against measured billing data
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
     exactly (capability == cap.t04.cost.cost_model_cluster@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0193_cost_model_cluster.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0194-request-router

**P0194 · `request_router` — Global Request Router & Load Balancer** · [spec](PART_SPECS_T04.md#p0194-request-router) · [self-contained txt](../prompts/P0194_request_router.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0194  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0194 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0194  (44/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Global Request Router & Load Balancer
file         : parts/t04_hardware/P0194_request_router.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.request_router
language     : Rust 1.86
capability   : cap.t04.request.request_router@1
determinism  : io
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Sends each request to the cheapest machine that meets its SLO.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. latency-aware, cache-affinity-aware, cost-aware routing
  2. queue-length and power-of-two-choices balancing
  3. SLO-class routing with overflow tiers
  4. tail-latency and cost measurement under mixed load

Expanded obligations:
  1. Implement latency-aware, cache-affinity-aware, cost-aware routing with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement queue-length and power-of-two-choices balancing together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement SLO-class routing with overflow tiers as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement tail-latency and cost measurement under mixed load, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
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
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.request.request_router@1
  cap.t04.request.request_router.describe@1

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

  cap.t04.cost.cost_model_cluster@1
      if unavailable: use the in-file conservative substitute for
      `cost_model_cluster` (documented, slower, lower quality) and set
      `degraded['cost_model_cluster']='local'`

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
   3. [ 600 lines] Core implementation A - latency-aware, cache-affinity-aware, cost-aware routing
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - queue-length and power-of-two-choices balancing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - SLO-class routing with overflow tiers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - tail-latency and cost measurement under mixed load
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
     exactly (capability == cap.t04.request.request_router@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0194_request_router.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0195-region-failover

**P0195 · `region_failover` — Multi-Region Replication & Failover** · [spec](PART_SPECS_T04.md#p0195-region-failover) · [self-contained txt](../prompts/P0195_region_failover.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0195  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0195 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0195  (45/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Multi-Region Replication & Failover
file         : parts/t04_hardware/P0195_region_failover.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.region_failover
language     : Rust 1.86
capability   : cap.t04.region.region_failover@1
determinism  : io
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Survives losing an entire datacentre.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. state replication strategy with RPO/RTO targets
  2. traffic shifting with connection draining
  3. consistency model documentation and enforcement
  4. failover drill results and measured RTO

Expanded obligations:
  1. Implement state replication strategy with RPO/RTO targets together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement traffic shifting with connection draining as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement consistency model documentation and enforcement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement failover drill results and measured RTO with an explicit
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.region.region_failover@1
  cap.t04.region.region_failover.describe@1

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

  cap.t04.request.request_router@1
      if unavailable: use the in-file conservative substitute for
      `request_router` (documented, slower, lower quality) and set
      `degraded['request_router']='local'`

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
   3. [ 600 lines] Core implementation A - state replication strategy with RPO/RTO targets
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - traffic shifting with connection draining
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - consistency model documentation and enforcement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - failover drill results and measured RTO
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
     exactly (capability == cap.t04.region.region_failover@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0195_region_failover.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0196-hw-sw-codesign

**P0196 · `hw_sw_codesign` — Hardware/Software Co-Design Specification** · [spec](PART_SPECS_T04.md#p0196-hw-sw-codesign) · [self-contained txt](../prompts/P0196_hw_sw_codesign.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0196  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0196 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0196  (46/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Hardware/Software Co-Design Specification
file         : parts/t04_hardware/P0196_hw_sw_codesign.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.hw_sw_codesign
language     : Rust 1.86
capability   : cap.t04.hw.hw_sw_codesign@1
determinism  : io
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The precise ask to hardware vendors, derived from measured bottlenecks.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. bottleneck attribution from roofline and profiling data
  2. quantified feature requests with projected speedups
  3. custom-accelerator ISA proposal for the hottest kernels
  4. projection methodology and validation plan

Expanded obligations:
  1. Implement bottleneck attribution from roofline and profiling data as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement quantified feature requests with projected speedups, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement custom-accelerator ISA proposal for the hottest kernels with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement projection methodology and validation plan together with its
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.hw.hw_sw_codesign@1
  cap.t04.hw.hw_sw_codesign.describe@1

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

  cap.t04.region.region_failover@1
      if unavailable: use the in-file conservative substitute for
      `region_failover` (documented, slower, lower quality) and set
      `degraded['region_failover']='local'`

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
   3. [ 600 lines] Core implementation A - bottleneck attribution from roofline and profiling data
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quantified feature requests with projected speedups
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - custom-accelerator ISA proposal for the hottest kernels
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - projection methodology and validation plan
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
     exactly (capability == cap.t04.hw.hw_sw_codesign@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0196_hw_sw_codesign.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0197-green-scheduling

**P0197 · `green_scheduling` — Carbon-Aware Scheduling** · [spec](PART_SPECS_T04.md#p0197-green-scheduling) · [self-contained txt](../prompts/P0197_green_scheduling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0197  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0197 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0197  (47/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Carbon-Aware Scheduling
file         : parts/t04_hardware/P0197_green_scheduling.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.green_scheduling
language     : Rust 1.86
capability   : cap.t04.green.green_scheduling@1
determinism  : io
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Same work, less carbon, no SLO loss.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. carbon-intensity signal ingestion and forecasting
  2. deferrable-workload shifting under SLO constraints
  3. carbon accounting per request
  4. measured emissions reduction at constant SLO attainment

Expanded obligations:
  1. Implement carbon-intensity signal ingestion and forecasting, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement deferrable-workload shifting under SLO constraints with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement carbon accounting per request together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Correctness here is what makes the
     tier's SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured emissions reduction at constant SLO attainment as a
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.green.green_scheduling@1
  cap.t04.green.green_scheduling.describe@1

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

  cap.t04.hw.hw_sw_codesign@1
      if unavailable: use the in-file conservative substitute for
      `hw_sw_codesign` (documented, slower, lower quality) and set
      `degraded['hw_sw_codesign']='local'`

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
   3. [ 600 lines] Core implementation A - carbon-intensity signal ingestion and forecasting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deferrable-workload shifting under SLO constraints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - carbon accounting per request
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured emissions reduction at constant SLO attainment
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
     exactly (capability == cap.t04.green.green_scheduling@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0197_green_scheduling.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0198-device-alloc-fair

**P0198 · `device_alloc_fair` — Fair-Share Device Allocation** · [spec](PART_SPECS_T04.md#p0198-device-alloc-fair) · [self-contained txt](../prompts/P0198_device_alloc_fair.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0198  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0198 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0198  (48/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Fair-Share Device Allocation
file         : parts/t04_hardware/P0198_device_alloc_fair.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.device_alloc_fair
language     : Rust 1.86
capability   : cap.t04.device.device_alloc_fair@1
determinism  : io
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Long-term fairness across teams and workloads.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dominant-resource fairness across heterogeneous devices
  2. borrowing/lending with reclaim guarantees
  3. starvation-freedom proof and monitoring
  4. fairness metric measurement over long horizons

Expanded obligations:
  1. Implement dominant-resource fairness across heterogeneous devices with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement borrowing/lending with reclaim guarantees together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement starvation-freedom proof and monitoring as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement fairness metric measurement over long horizons, and make it
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.device.device_alloc_fair@1
  cap.t04.device.device_alloc_fair.describe@1

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

  cap.t04.green.green_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `green_scheduling` (documented, slower, lower quality) and set
      `degraded['green_scheduling']='local'`

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
   3. [ 600 lines] Core implementation A - dominant-resource fairness across heterogeneous devices
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - borrowing/lending with reclaim guarantees
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - starvation-freedom proof and monitoring
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fairness metric measurement over long horizons
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
     exactly (capability == cap.t04.device.device_alloc_fair@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0198_device_alloc_fair.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0199-hpc-interop

**P0199 · `hpc_interop` — HPC & Scientific Stack Interoperability** · [spec](PART_SPECS_T04.md#p0199-hpc-interop) · [self-contained txt](../prompts/P0199_hpc_interop.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0199  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0199 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0199  (49/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : HPC & Scientific Stack Interoperability
file         : parts/t04_hardware/P0199_hpc_interop.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.hpc_interop
language     : Rust 1.86
capability   : cap.t04.hpc.hpc_interop@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Works inside existing supercomputing environments.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. MPI-compatible bootstrap and communicator mapping
  2. shared-filesystem-friendly IO patterns
  3. job-script generation for major HPC sites
  4. validated runs on multiple site configurations

Expanded obligations:
  1. Implement MPI-compatible bootstrap and communicator mapping together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement shared-filesystem-friendly IO patterns as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement job-script generation for major HPC sites, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement validated runs on multiple site configurations with an
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.hpc.hpc_interop@1
  cap.t04.hpc.hpc_interop.describe@1

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

  cap.t04.device.device_alloc_fair@1
      if unavailable: use the in-file conservative substitute for
      `device_alloc_fair` (documented, slower, lower quality) and set
      `degraded['device_alloc_fair']='local'`

  cap.t02.attn.attn_paged_decode@1
      if unavailable: use the in-file conservative substitute for
      `attn_paged_decode` (documented, slower, lower quality) and set
      `degraded['attn_paged_decode']='local'`

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
   3. [ 600 lines] Core implementation A - MPI-compatible bootstrap and communicator mapping
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - shared-filesystem-friendly IO patterns
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - job-script generation for major HPC sites
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - validated runs on multiple site configurations
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
     exactly (capability == cap.t04.hpc.hpc_interop@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0199_hpc_interop.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0200-provision-verify

**P0200 · `provision_verify` — Node Admission & Continuous Verification** · [spec](PART_SPECS_T04.md#p0200-provision-verify) · [self-contained txt](../prompts/P0200_provision_verify.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0200  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0200 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0200  (50/50 of tier T04)
tier         : T04 — Hardware Abstraction & Interconnect
title        : Node Admission & Continuous Verification
file         : parts/t04_hardware/P0200_provision_verify.rs          <-- create exactly this path, nothing else
module       : hyperion.t04.hardware.provision_verify
language     : Rust 1.86
capability   : cap.t04.provision.provision_verify@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Every machine proves it is healthy and correct before and during service.

Tier context:
  Device fabric, topology-aware collectives, RDMA transport, fault domains and
  power/thermal governance across 100k accelerators.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. burn-in suite: numeric correctness, bandwidth, thermal, memory integrity
  2. continuous lightweight verification during production
  3. automatic quarantine on verification failure
  4. escape-rate measurement of bad nodes reaching production

Expanded obligations:
  1. Implement burn-in suite: numeric correctness, bandwidth, thermal, memory
     integrity as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement continuous lightweight verification during production, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement automatic quarantine on verification failure with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement escape-rate measurement of bad nodes reaching production
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t04.provision.provision_verify@1
  cap.t04.provision.provision_verify.describe@1

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

  cap.t04.hpc.hpc_interop@1
      if unavailable: use the in-file conservative substitute for
      `hpc_interop` (documented, slower, lower quality) and set
      `degraded['hpc_interop']='local'`

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
   3. [ 600 lines] Core implementation A - burn-in suite: numeric correctness, bandwidth, thermal, memory i
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - continuous lightweight verification during production
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic quarantine on verification failure
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - escape-rate measurement of bad nodes reaching production
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
     exactly (capability == cap.t04.provision.provision_verify@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t04_hardware/P0200_provision_verify.rs`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
