# HYPERION-Ω — Worker prompts · T06 · Sparse Routing & Mixture-of-Ω-Experts

> 50 prompts · one per part · language Python 3.13 · Ω-CONTRACT v1.0.0-frozen

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

## PROMPT p0251-router-core

**P0251 · `router_core` — Top-K Router Core** · [spec](PART_SPECS_T06.md#p0251-router-core) · [self-contained txt](../prompts/P0251_router_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0251  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0251 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0251  (1/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Top-K Router Core
file         : parts/t06_routing/P0251_router_core.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_core
language     : Python 3.13
capability   : cap.t06.router.router_core@1
determinism  : seeded
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
The gating function that selects 2 of 512 experts per token.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gate scoring with normalisation choice justified by measurement
  2. top-k selection with deterministic tie-breaking
  3. gradient path (straight-through vs REINFORCE) comparison
  4. routing-decision determinism under batch reordering

Expanded obligations:
  1. Implement gate scoring with normalisation choice justified by
     measurement together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of GPQA Diamond,
     so its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement top-k selection with deterministic tie-breaking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement gradient path (straight-through vs REINFORCE) comparison, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  4. Implement routing-decision determinism under batch reordering with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.router.router_core@1
  cap.t06.router.router_core.describe@1

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

  cap.t05.causal.causal_model@1
      if unavailable: use the in-file conservative substitute for
      `causal_model` (documented, slower, lower quality) and set
      `degraded['causal_model']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - gate scoring with normalisation choice justified by measurement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - top-k selection with deterministic tie-breaking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - gradient path (straight-through vs REINFORCE) comparison
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - routing-decision determinism under batch reordering
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_core@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 19000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0251_router_core.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0252-router-balance

**P0252 · `router_balance` — Load Balancing Losses & Constraints** · [spec](PART_SPECS_T06.md#p0252-router-balance) · [self-contained txt](../prompts/P0252_router_balance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0252  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0252 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0252  (2/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Load Balancing Losses & Constraints
file         : parts/t06_routing/P0252_router_balance.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_balance
language     : Python 3.13
capability   : cap.t06.router.router_balance@1
determinism  : seeded
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Prevents expert collapse without hurting quality.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. auxiliary-loss and loss-free bias-correction methods compared
  2. per-batch and per-sequence balance metrics
  3. coefficient tuning with quality-versus-balance curves
  4. collapse detection and automatic remediation

Expanded obligations:
  1. Implement auxiliary-loss and loss-free bias-correction methods compared
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement per-batch and per-sequence balance metrics, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement coefficient tuning with quality-versus-balance curves with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement collapse detection and automatic remediation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
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
  cap.t06.router.router_balance@1
  cap.t06.router.router_balance.describe@1

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

  cap.t06.router.router_core@1
      if unavailable: use the in-file conservative substitute for
      `router_core` (documented, slower, lower quality) and set
      `degraded['router_core']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t05.distillation.distillation_arch@1
      if unavailable: use the in-file conservative substitute for
      `distillation_arch` (documented, slower, lower quality) and set
      `degraded['distillation_arch']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - auxiliary-loss and loss-free bias-correction methods compared
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-batch and per-sequence balance metrics
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - coefficient tuning with quality-versus-balance curves
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - collapse detection and automatic remediation
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_balance@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 20000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0252_router_balance.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0253-router-capacity

**P0253 · `router_capacity` — Capacity Factor & Overflow Policy** · [spec](PART_SPECS_T06.md#p0253-router-capacity) · [self-contained txt](../prompts/P0253_router_capacity.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0253  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0253 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0253  (3/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Capacity Factor & Overflow Policy
file         : parts/t06_routing/P0253_router_capacity.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_capacity
language     : Python 3.13
capability   : cap.t06.router.router_capacity@1
determinism  : seeded
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
What happens when an expert is oversubscribed.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capacity computation per batch shape with headroom policy
  2. overflow handling: drop, reroute, residual-pass with quality accounting
  3. deterministic overflow ordering
  4. quality impact measurement at multiple capacity factors

Expanded obligations:
  1. Implement capacity computation per batch shape with headroom policy, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement overflow handling: drop, reroute, residual-pass with quality
     accounting with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of GPQA Diamond,
     so its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement deterministic overflow ordering together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Its contribution is measured against
     GPQA Diamond — a regression on that benchmark is an automatic rejection
     of this part.
  4. Implement quality impact measurement at multiple capacity factors as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.

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
  cap.t06.router.router_capacity@1
  cap.t06.router.router_capacity.describe@1

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

  cap.t06.router.router_balance@1
      if unavailable: use the in-file conservative substitute for
      `router_balance` (documented, slower, lower quality) and set
      `degraded['router_balance']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t05.multimodal.multimodal_fusion_arch@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_fusion_arch` (documented, slower, lower quality) and set
      `degraded['multimodal_fusion_arch']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - capacity computation per batch shape with headroom policy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - overflow handling: drop, reroute, residual-pass with quality acc
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deterministic overflow ordering
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - quality impact measurement at multiple capacity factors
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_capacity@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 21000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0253_router_capacity.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0254-router-hash-hybrid

**P0254 · `router_hash_hybrid` — Hybrid Learned/Deterministic Routing** · [spec](PART_SPECS_T06.md#p0254-router-hash-hybrid) · [self-contained txt](../prompts/P0254_router_hash_hybrid.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0254  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0254 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0254  (4/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Hybrid Learned/Deterministic Routing
file         : parts/t06_routing/P0254_router_hash_hybrid.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_hash_hybrid
language     : Python 3.13
capability   : cap.t06.router.router_hash_hybrid@1
determinism  : seeded
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Combines learned gates with hash and rule-based routing for stability.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hash-routing fallback with balanced-by-construction guarantees
  2. rule-based routing for known domains (code, math, language)
  3. blending policy and switchover criteria
  4. stability-versus-adaptivity measurement

Expanded obligations:
  1. Implement hash-routing fallback with balanced-by-construction guarantees
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement rule-based routing for known domains (code, math, language)
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement blending policy and switchover criteria as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  4. Implement stability-versus-adaptivity measurement, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
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
  cap.t06.router.router_hash_hybrid@1
  cap.t06.router.router_hash_hybrid.describe@1

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

  cap.t06.router.router_capacity@1
      if unavailable: use the in-file conservative substitute for
      `router_capacity` (documented, slower, lower quality) and set
      `degraded['router_capacity']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t05.context.context_packing@1
      if unavailable: use the in-file conservative substitute for
      `context_packing` (documented, slower, lower quality) and set
      `degraded['context_packing']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - hash-routing fallback with balanced-by-construction guarantees
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - rule-based routing for known domains (code, math, language)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blending policy and switchover criteria
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - stability-versus-adaptivity measurement
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_hash_hybrid@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 22000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0254_router_hash_hybrid.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0255-expert-ffn

**P0255 · `expert_ffn` — Expert Feed-Forward Implementation** · [spec](PART_SPECS_T06.md#p0255-expert-ffn) · [self-contained txt](../prompts/P0255_expert_ffn.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0255  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0255 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0255  (5/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Feed-Forward Implementation
file         : parts/t06_routing/P0255_expert_ffn.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_ffn
language     : Python 3.13
capability   : cap.t06.expert.expert_ffn@1
determinism  : seeded
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
The expert body: fast, quantisation-friendly, specialisable.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gated-linear expert with per-expert scaling and bias handling
  2. quantised expert weights with per-expert calibration
  3. expert-local normalisation choices
  4. throughput at 512 experts with realistic skew

Expanded obligations:
  1. Implement gated-linear expert with per-expert scaling and bias handling
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement quantised expert weights with per-expert calibration as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement expert-local normalisation choices, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  4. Implement throughput at 512 experts with realistic skew with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.expert.expert_ffn@1
  cap.t06.expert.expert_ffn.describe@1

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

  cap.t06.router.router_hash_hybrid@1
      if unavailable: use the in-file conservative substitute for
      `router_hash_hybrid` (documented, slower, lower quality) and set
      `degraded['router_hash_hybrid']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t05.capacity.capacity_probes@1
      if unavailable: use the in-file conservative substitute for
      `capacity_probes` (documented, slower, lower quality) and set
      `degraded['capacity_probes']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - gated-linear expert with per-expert scaling and bias handling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quantised expert weights with per-expert calibration
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - expert-local normalisation choices
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput at 512 experts with realistic skew
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_ffn@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 23000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0255_expert_ffn.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0256-expert-attention

**P0256 · `expert_attention` — Mixture-of-Attention-Heads Routing** · [spec](PART_SPECS_T06.md#p0256-expert-attention) · [self-contained txt](../prompts/P0256_expert_attention.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0256  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0256 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0256  (6/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Mixture-of-Attention-Heads Routing
file         : parts/t06_routing/P0256_expert_attention.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_attention
language     : Python 3.13
capability   : cap.t06.expert.expert_attention@1
determinism  : seeded
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Applies conditional compute to attention, not just feed-forward.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. head-group routing with per-token selection
  2. KV-cost implications and sharing strategy
  3. quality gain measurement versus dense attention
  4. kernel integration with the paged decode path

Expanded obligations:
  1. Implement head-group routing with per-token selection as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement KV-cost implications and sharing strategy, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement quality gain measurement versus dense attention with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement kernel integration with the paged decode path together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.

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
  cap.t06.expert.expert_attention@1
  cap.t06.expert.expert_attention.describe@1

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

  cap.t06.expert.expert_ffn@1
      if unavailable: use the in-file conservative substitute for
      `expert_ffn` (documented, slower, lower quality) and set
      `degraded['expert_ffn']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t05.recurrent.recurrent_memory_layer@1
      if unavailable: use the in-file conservative substitute for
      `recurrent_memory_layer` (documented, slower, lower quality) and set
      `degraded['recurrent_memory_layer']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - head-group routing with per-token selection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - KV-cost implications and sharing strategy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality gain measurement versus dense attention
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - kernel integration with the paged decode path
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_attention@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 24000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0256_expert_attention.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0257-shared-expert

**P0257 · `shared_expert` — Shared & Residual Expert Design** · [spec](PART_SPECS_T06.md#p0257-shared-expert) · [self-contained txt](../prompts/P0257_shared_expert.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0257  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0257 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0257  (7/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Shared & Residual Expert Design
file         : parts/t06_routing/P0257_shared_expert.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.shared_expert
language     : Python 3.13
capability   : cap.t06.shared.shared_expert@1
determinism  : seeded
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
A always-on expert that captures common structure, letting specialists
specialise.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. shared-expert sizing analysis and residual combination
  2. interaction with load-balancing objectives
  3. ablation showing the quality contribution
  4. cost accounting of the always-on path

Expanded obligations:
  1. Implement shared-expert sizing analysis and residual combination, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GPQA Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement interaction with load-balancing objectives with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement ablation showing the quality contribution together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement cost accounting of the always-on path as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.shared.shared_expert@1
  cap.t06.shared.shared_expert.describe@1

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

  cap.t06.expert.expert_attention@1
      if unavailable: use the in-file conservative substitute for
      `expert_attention` (documented, slower, lower quality) and set
      `degraded['expert_attention']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t05.byte.byte_latent_patching@1
      if unavailable: use the in-file conservative substitute for
      `byte_latent_patching` (documented, slower, lower quality) and set
      `degraded['byte_latent_patching']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - shared-expert sizing analysis and residual combination
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - interaction with load-balancing objectives
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - ablation showing the quality contribution
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost accounting of the always-on path
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.shared.shared_expert@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 25000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0257_shared_expert.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0258-fine-grained-experts

**P0258 · `fine_grained_experts` — Fine-Grained Expert Segmentation** · [spec](PART_SPECS_T06.md#p0258-fine-grained-experts) · [self-contained txt](../prompts/P0258_fine_grained_experts.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0258  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0258 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0258  (8/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Fine-Grained Expert Segmentation
file         : parts/t06_routing/P0258_fine_grained_experts.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.fine_grained_experts
language     : Python 3.13
capability   : cap.t06.fine.fine_grained_experts@1
determinism  : seeded
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Many small experts beat few large ones: proving and exploiting it.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. granularity sweep at matched active parameters
  2. combinatorial-coverage analysis of expert combinations
  3. routing-overhead measurement at high expert counts
  4. recommended granularity with evidence

Expanded obligations:
  1. Implement granularity sweep at matched active parameters with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement combinatorial-coverage analysis of expert combinations
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement routing-overhead measurement at high expert counts as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement recommended granularity with evidence, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.fine.fine_grained_experts@1
  cap.t06.fine.fine_grained_experts.describe@1

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

  cap.t06.shared.shared_expert@1
      if unavailable: use the in-file conservative substitute for
      `shared_expert` (documented, slower, lower quality) and set
      `degraded['shared_expert']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t05.world.world_model_core@1
      if unavailable: use the in-file conservative substitute for
      `world_model_core` (documented, slower, lower quality) and set
      `degraded['world_model_core']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - granularity sweep at matched active parameters
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - combinatorial-coverage analysis of expert combinations
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - routing-overhead measurement at high expert counts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - recommended granularity with evidence
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.fine.fine_grained_experts@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 26000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0258_fine_grained_experts.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0259-expert-placement

**P0259 · `expert_placement` — Expert Placement & Replication Policy** · [spec](PART_SPECS_T06.md#p0259-expert-placement) · [self-contained txt](../prompts/P0259_expert_placement.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0259  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0259 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0259  (9/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Placement & Replication Policy
file         : parts/t06_routing/P0259_expert_placement.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_placement
language     : Python 3.13
capability   : cap.t06.expert.expert_placement@1
determinism  : seeded
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Where each expert lives across the cluster, and how many copies exist.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. traffic-driven placement solver minimising all-to-all volume
  2. hot-expert replication with consistency handling
  3. migration protocol with zero request loss
  4. measured communication reduction

Expanded obligations:
  1. Implement traffic-driven placement solver minimising all-to-all volume
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement hot-expert replication with consistency handling as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  3. Implement migration protocol with zero request loss, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured communication reduction with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Correctness here is
     what makes the tier's GPQA Diamond target reachable; the part therefore
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
  cap.t06.expert.expert_placement@1
  cap.t06.expert.expert_placement.describe@1

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

  cap.t06.fine.fine_grained_experts@1
      if unavailable: use the in-file conservative substitute for
      `fine_grained_experts` (documented, slower, lower quality) and set
      `degraded['fine_grained_experts']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t05.model.model_merging@1
      if unavailable: use the in-file conservative substitute for
      `model_merging` (documented, slower, lower quality) and set
      `degraded['model_merging']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - traffic-driven placement solver minimising all-to-all volume
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hot-expert replication with consistency handling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - migration protocol with zero request loss
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured communication reduction
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_placement@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 27000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0259_expert_placement.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0260-expert-prefetch

**P0260 · `expert_prefetch` — Expert Weight Prefetching & Caching** · [spec](PART_SPECS_T06.md#p0260-expert-prefetch) · [self-contained txt](../prompts/P0260_expert_prefetch.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0260  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0260 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0260  (10/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Weight Prefetching & Caching
file         : parts/t06_routing/P0260_expert_prefetch.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_prefetch
language     : Python 3.13
capability   : cap.t06.expert.expert_prefetch@1
determinism  : seeded
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Streams only the experts a request will actually use.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. router-lookahead prediction of needed experts
  2. device-memory expert cache with cost-aware eviction
  3. prefetch-accuracy and stall-time measurement
  4. memory-footprint reduction at matched latency

Expanded obligations:
  1. Implement router-lookahead prediction of needed experts as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement device-memory expert cache with cost-aware eviction, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement prefetch-accuracy and stall-time measurement with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement memory-footprint reduction at matched latency together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
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
  cap.t06.expert.expert_prefetch@1
  cap.t06.expert.expert_prefetch.describe@1

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

  cap.t06.expert.expert_placement@1
      if unavailable: use the in-file conservative substitute for
      `expert_placement` (documented, slower, lower quality) and set
      `degraded['expert_placement']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t05.logit.logit_head_design@1
      if unavailable: use the in-file conservative substitute for
      `logit_head_design` (documented, slower, lower quality) and set
      `degraded['logit_head_design']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - router-lookahead prediction of needed experts
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - device-memory expert cache with cost-aware eviction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - prefetch-accuracy and stall-time measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - memory-footprint reduction at matched latency
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_prefetch@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 28000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0260_expert_prefetch.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0261-router-lookahead

**P0261 · `router_lookahead` — Router Prediction & Speculative Routing** · [spec](PART_SPECS_T06.md#p0261-router-lookahead) · [self-contained txt](../prompts/P0261_router_lookahead.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0261  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0261 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0261  (11/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Router Prediction & Speculative Routing
file         : parts/t06_routing/P0261_router_lookahead.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_lookahead
language     : Python 3.13
capability   : cap.t06.router.router_lookahead@1
determinism  : seeded
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Predicts routing before the layer runs so weights arrive in time.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. lightweight predictor from earlier-layer activations
  2. speculative fetch with misprediction rollback
  3. prediction accuracy per layer depth
  4. latency improvement attributable to lookahead

Expanded obligations:
  1. Implement lightweight predictor from earlier-layer activations, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement speculative fetch with misprediction rollback with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement prediction accuracy per layer depth together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement latency improvement attributable to lookahead as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.router.router_lookahead@1
  cap.t06.router.router_lookahead.describe@1

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

  cap.t06.expert.expert_prefetch@1
      if unavailable: use the in-file conservative substitute for
      `expert_prefetch` (documented, slower, lower quality) and set
      `degraded['expert_prefetch']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t05.numerical.numerical_arch_stability@1
      if unavailable: use the in-file conservative substitute for
      `numerical_arch_stability` (documented, slower, lower quality) and set
      `degraded['numerical_arch_stability']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - lightweight predictor from earlier-layer activations
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - speculative fetch with misprediction rollback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - prediction accuracy per layer depth
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency improvement attributable to lookahead
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_lookahead@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 29000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0261_router_lookahead.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0262-moe-determinism

**P0262 · `moe_determinism` — Deterministic MoE Execution** · [spec](PART_SPECS_T06.md#p0262-moe-determinism) · [self-contained txt](../prompts/P0262_moe_determinism.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0262  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0262 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0262  (12/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Deterministic MoE Execution
file         : parts/t06_routing/P0262_moe_determinism.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_determinism
language     : Python 3.13
capability   : cap.t06.moe.moe_determinism@1
determinism  : seeded
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Same input, same experts, same bytes, regardless of batching.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. batch-invariant routing and combine ordering
  2. capacity-independent result guarantees or documented exceptions
  3. replay verification across batch sizes and rank counts
  4. cost-of-determinism measurement

Expanded obligations:
  1. Implement batch-invariant routing and combine ordering with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement capacity-independent result guarantees or documented
     exceptions together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of GPQA Diamond,
     so its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement replay verification across batch sizes and rank counts as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement cost-of-determinism measurement, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's GPQA Diamond target reachable; the part
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.moe.moe_determinism@1
  cap.t06.moe.moe_determinism.describe@1

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

  cap.t06.router.router_lookahead@1
      if unavailable: use the in-file conservative substitute for
      `router_lookahead` (documented, slower, lower quality) and set
      `degraded['router_lookahead']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t05.arch.arch_ablation_suite@1
      if unavailable: use the in-file conservative substitute for
      `arch_ablation_suite` (documented, slower, lower quality) and set
      `degraded['arch_ablation_suite']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - batch-invariant routing and combine ordering
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capacity-independent result guarantees or documented exceptions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - replay verification across batch sizes and rank counts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost-of-determinism measurement
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_determinism@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 30000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0262_moe_determinism.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0263-expert-lifecycle

**P0263 · `expert_lifecycle` — Expert Birth, Death & Reincarnation** · [spec](PART_SPECS_T06.md#p0263-expert-lifecycle) · [self-contained txt](../prompts/P0263_expert_lifecycle.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0263  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0263 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0263  (13/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Birth, Death & Reincarnation
file         : parts/t06_routing/P0263_expert_lifecycle.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_lifecycle
language     : Python 3.13
capability   : cap.t06.expert.expert_lifecycle@1
determinism  : seeded
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Grows and prunes the expert population over the model's life.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. utilisation-driven expert retirement with knowledge absorption
  2. expert splitting when overloaded, with diversity injection
  3. population-size scheduling during training
  4. quality trajectory across lifecycle events

Expanded obligations:
  1. Implement utilisation-driven expert retirement with knowledge absorption
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement expert splitting when overloaded, with diversity injection as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement population-size scheduling during training, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement quality trajectory across lifecycle events with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.

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
  cap.t06.expert.expert_lifecycle@1
  cap.t06.expert.expert_lifecycle.describe@1

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

  cap.t06.moe.moe_determinism@1
      if unavailable: use the in-file conservative substitute for
      `moe_determinism` (documented, slower, lower quality) and set
      `degraded['moe_determinism']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t05.state.state_space_layer@1
      if unavailable: use the in-file conservative substitute for
      `state_space_layer` (documented, slower, lower quality) and set
      `degraded['state_space_layer']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - utilisation-driven expert retirement with knowledge absorption
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - expert splitting when overloaded, with diversity injection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - population-size scheduling during training
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - quality trajectory across lifecycle events
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_lifecycle@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 31000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0263_expert_lifecycle.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0264-expert-diversity

**P0264 · `expert_diversity` — Expert Diversity Objectives** · [spec](PART_SPECS_T06.md#p0264-expert-diversity) · [self-contained txt](../prompts/P0264_expert_diversity.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0264  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0264 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0264  (14/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Diversity Objectives
file         : parts/t06_routing/P0264_expert_diversity.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_diversity
language     : Python 3.13
capability   : cap.t06.expert.expert_diversity@1
determinism  : seeded
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Actively prevents 512 experts from converging to the same function.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. diversity metrics over weights, activations and gradients
  2. orthogonality/repulsion regularisers with tuning evidence
  3. collapse early-warning indicators
  4. measured diversity-versus-quality relationship

Expanded obligations:
  1. Implement diversity metrics over weights, activations and gradients as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement orthogonality/repulsion regularisers with tuning evidence, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  3. Implement collapse early-warning indicators with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement measured diversity-versus-quality relationship together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.expert.expert_diversity@1
  cap.t06.expert.expert_diversity.describe@1

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

  cap.t06.expert.expert_lifecycle@1
      if unavailable: use the in-file conservative substitute for
      `expert_lifecycle` (documented, slower, lower quality) and set
      `degraded['expert_lifecycle']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t05.tokeniser.tokeniser_omega@1
      if unavailable: use the in-file conservative substitute for
      `tokeniser_omega` (documented, slower, lower quality) and set
      `degraded['tokeniser_omega']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - diversity metrics over weights, activations and gradients
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - orthogonality/repulsion regularisers with tuning evidence
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - collapse early-warning indicators
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured diversity-versus-quality relationship
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_diversity@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 32000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0264_expert_diversity.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0265-router-temperature

**P0265 · `router_temperature` — Router Sharpness & Exploration Schedule** · [spec](PART_SPECS_T06.md#p0265-router-temperature) · [self-contained txt](../prompts/P0265_router_temperature.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0265  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0265 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0265  (15/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Router Sharpness & Exploration Schedule
file         : parts/t06_routing/P0265_router_temperature.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_temperature
language     : Python 3.13
capability   : cap.t06.router.router_temperature@1
determinism  : seeded
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Explores early, commits late, without instability.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. temperature/noise schedule design and justification
  2. exploration bonus for underused experts
  3. annealing effect on final specialisation
  4. training-stability evidence across schedules

Expanded obligations:
  1. Implement temperature/noise schedule design and justification, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement exploration bonus for underused experts with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  3. Implement annealing effect on final specialisation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement training-stability evidence across schedules as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.router.router_temperature@1
  cap.t06.router.router_temperature.describe@1

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

  cap.t06.expert.expert_diversity@1
      if unavailable: use the in-file conservative substitute for
      `expert_diversity` (documented, slower, lower quality) and set
      `degraded['expert_diversity']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t05.uncertainty.uncertainty_calibration@1
      if unavailable: use the in-file conservative substitute for
      `uncertainty_calibration` (documented, slower, lower quality) and set
      `degraded['uncertainty_calibration']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - temperature/noise schedule design and justification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - exploration bonus for underused experts
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - annealing effect on final specialisation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - training-stability evidence across schedules
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_temperature@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 33000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0265_router_temperature.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0266-sparse-activation-stats

**P0266 · `sparse_activation_stats` — Sparse Activation Statistics & Diagnostics** · [spec](PART_SPECS_T06.md#p0266-sparse-activation-stats) · [self-contained txt](../prompts/P0266_sparse_activation_stats.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0266  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0266 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0266  (16/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Sparse Activation Statistics & Diagnostics
file         : parts/t06_routing/P0266_sparse_activation_stats.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.sparse_activation_stats
language     : Python 3.13
capability   : cap.t06.sparse.sparse_activation_stats@1
determinism  : seeded
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
The observability layer for conditional compute.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-expert utilisation, entropy and co-activation statistics
  2. drift detection over traffic distribution shifts
  3. diagnostic report with actionable remediation
  4. overhead under 0.5% of step time

Expanded obligations:
  1. Implement per-expert utilisation, entropy and co-activation statistics
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement drift detection over traffic distribution shifts together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement diagnostic report with actionable remediation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement overhead under 0.5% of step time, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.

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
  cap.t06.sparse.sparse_activation_stats@1
  cap.t06.sparse.sparse_activation_stats.describe@1

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

  cap.t06.router.router_temperature@1
      if unavailable: use the in-file conservative substitute for
      `router_temperature` (documented, slower, lower quality) and set
      `degraded['router_temperature']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t05.knowledge.knowledge_editing@1
      if unavailable: use the in-file conservative substitute for
      `knowledge_editing` (documented, slower, lower quality) and set
      `degraded['knowledge_editing']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - per-expert utilisation, entropy and co-activation statistics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - drift detection over traffic distribution shifts
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - diagnostic report with actionable remediation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - overhead under 0.5% of step time
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.sparse.sparse_activation_stats@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 34000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0266_sparse_activation_stats.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0267-moe-quantisation

**P0267 · `moe_quantisation` — Per-Expert Quantisation Strategy** · [spec](PART_SPECS_T06.md#p0267-moe-quantisation) · [self-contained txt](../prompts/P0267_moe_quantisation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0267  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0267 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0267  (17/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Per-Expert Quantisation Strategy
file         : parts/t06_routing/P0267_moe_quantisation.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_quantisation
language     : Python 3.13
capability   : cap.t06.moe.moe_quantisation@1
determinism  : seeded
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Cheap experts where possible, precise experts where necessary.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-expert sensitivity analysis and precision assignment
  2. mixed-precision expert pool with routing awareness
  3. accuracy verification per assignment plan
  4. measured memory and bandwidth savings

Expanded obligations:
  1. Implement per-expert sensitivity analysis and precision assignment
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement mixed-precision expert pool with routing awareness as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement accuracy verification per assignment plan, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured memory and bandwidth savings with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.moe.moe_quantisation@1
  cap.t06.moe.moe_quantisation.describe@1

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

  cap.t06.sparse.sparse_activation_stats@1
      if unavailable: use the in-file conservative substitute for
      `sparse_activation_stats` (documented, slower, lower quality) and set
      `degraded['sparse_activation_stats']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t05.residual.residual_stream_design@1
      if unavailable: use the in-file conservative substitute for
      `residual_stream_design` (documented, slower, lower quality) and set
      `degraded['residual_stream_design']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - per-expert sensitivity analysis and precision assignment
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - mixed-precision expert pool with routing awareness
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accuracy verification per assignment plan
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured memory and bandwidth savings
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_quantisation@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 35000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0267_moe_quantisation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0268-expert-offload

**P0268 · `expert_offload` — Expert Offloading to Host/Storage** · [spec](PART_SPECS_T06.md#p0268-expert-offload) · [self-contained txt](../prompts/P0268_expert_offload.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0268  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0268 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0268  (18/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Offloading to Host/Storage
file         : parts/t06_routing/P0268_expert_offload.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_offload
language     : Python 3.13
capability   : cap.t06.expert.expert_offload@1
determinism  : seeded
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Serves 512-expert models on limited device memory.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. residency tiering driven by access frequency
  2. asynchronous fetch overlapped with earlier layers
  3. worst-case latency bound under cold experts
  4. memory-reduction versus latency-cost curve

Expanded obligations:
  1. Implement residency tiering driven by access frequency as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement asynchronous fetch overlapped with earlier layers, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement worst-case latency bound under cold experts with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement memory-reduction versus latency-cost curve together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.

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
  cap.t06.expert.expert_offload@1
  cap.t06.expert.expert_offload.describe@1

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

  cap.t06.moe.moe_quantisation@1
      if unavailable: use the in-file conservative substitute for
      `moe_quantisation` (documented, slower, lower quality) and set
      `degraded['moe_quantisation']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t05.model.model_surgery@1
      if unavailable: use the in-file conservative substitute for
      `model_surgery` (documented, slower, lower quality) and set
      `degraded['model_surgery']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - residency tiering driven by access frequency
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - asynchronous fetch overlapped with earlier layers
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - worst-case latency bound under cold experts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - memory-reduction versus latency-cost curve
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_offload@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 36000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0268_expert_offload.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0269-moe-batching

**P0269 · `moe_batching` — MoE-Aware Request Batching** · [spec](PART_SPECS_T06.md#p0269-moe-batching) · [self-contained txt](../prompts/P0269_moe_batching.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0269  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0269 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0269  (19/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : MoE-Aware Request Batching
file         : parts/t06_routing/P0269_moe_batching.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_batching
language     : Python 3.13
capability   : cap.t06.moe.moe_batching@1
determinism  : seeded
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Groups requests so their expert demands overlap.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. batching policy using predicted expert sets
  2. affinity grouping with fairness constraints
  3. throughput improvement measurement
  4. latency-fairness tradeoff analysis

Expanded obligations:
  1. Implement batching policy using predicted expert sets, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement affinity grouping with fairness constraints with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement throughput improvement measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement latency-fairness tradeoff analysis as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.moe.moe_batching@1
  cap.t06.moe.moe_batching.describe@1

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

  cap.t06.expert.expert_offload@1
      if unavailable: use the in-file conservative substitute for
      `expert_offload` (documented, slower, lower quality) and set
      `degraded['expert_offload']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t05.reference.reference_forward@1
      if unavailable: use the in-file conservative substitute for
      `reference_forward` (documented, slower, lower quality) and set
      `degraded['reference_forward']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - batching policy using predicted expert sets
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - affinity grouping with fairness constraints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - throughput improvement measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency-fairness tradeoff analysis
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_batching@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 37000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0269_moe_batching.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0270-token-dropping

**P0270 · `token_dropping` — Token Dropping & Early Exit Policy** · [spec](PART_SPECS_T06.md#p0270-token-dropping) · [self-contained txt](../prompts/P0270_token_dropping.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0270  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0270 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0270  (20/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Token Dropping & Early Exit Policy
file         : parts/t06_routing/P0270_token_dropping.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.token_dropping
language     : Python 3.13
capability   : cap.t06.token.token_dropping@1
determinism  : seeded
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Spends compute only where it changes the answer.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. token-importance scoring with calibrated thresholds
  2. safe-drop guarantees for structurally critical tokens
  3. quality impact measurement at multiple drop rates
  4. interaction with adaptive depth

Expanded obligations:
  1. Implement token-importance scoring with calibrated thresholds with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement safe-drop guarantees for structurally critical tokens together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement quality impact measurement at multiple drop rates as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement interaction with adaptive depth, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against GPQA Diamond — a regression on that benchmark is an
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.token.token_dropping@1
  cap.t06.token.token_dropping.describe@1

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

  cap.t06.moe.moe_batching@1
      if unavailable: use the in-file conservative substitute for
      `moe_batching` (documented, slower, lower quality) and set
      `degraded['moe_batching']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t05.kv.kv_compression_model@1
      if unavailable: use the in-file conservative substitute for
      `kv_compression_model` (documented, slower, lower quality) and set
      `degraded['kv_compression_model']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - token-importance scoring with calibrated thresholds
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - safe-drop guarantees for structurally critical tokens
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality impact measurement at multiple drop rates
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - interaction with adaptive depth
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.token.token_dropping@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 38000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0270_token_dropping.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0271-conditional-layers

**P0271 · `conditional_layers` — Layer Skipping & Conditional Depth Routing** · [spec](PART_SPECS_T06.md#p0271-conditional-layers) · [self-contained txt](../prompts/P0271_conditional_layers.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0271  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0271 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0271  (21/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Layer Skipping & Conditional Depth Routing
file         : parts/t06_routing/P0271_conditional_layers.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.conditional_layers
language     : Python 3.13
capability   : cap.t06.conditional.conditional_layers@1
determinism  : seeded
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Whole layers become optional for easy inputs.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. layer-skip policy learning with a compute budget
  2. skip-pattern regularisation for cache friendliness
  3. worst-case-quality guardrails
  4. measured FLOP reduction at matched accuracy

Expanded obligations:
  1. Implement layer-skip policy learning with a compute budget together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement skip-pattern regularisation for cache friendliness as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  3. Implement worst-case-quality guardrails, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured FLOP reduction at matched accuracy with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
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
  cap.t06.conditional.conditional_layers@1
  cap.t06.conditional.conditional_layers.describe@1

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

  cap.t06.token.token_dropping@1
      if unavailable: use the in-file conservative substitute for
      `token_dropping` (documented, slower, lower quality) and set
      `degraded['token_dropping']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t05.embedding.embedding_design@1
      if unavailable: use the in-file conservative substitute for
      `embedding_design` (documented, slower, lower quality) and set
      `degraded['embedding_design']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - layer-skip policy learning with a compute budget
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - skip-pattern regularisation for cache friendliness
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - worst-case-quality guardrails
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured FLOP reduction at matched accuracy
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.conditional.conditional_layers@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 39000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0271_conditional_layers.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0272-mod-routing

**P0272 · `mod_routing` — Mixture-of-Depths Routing** · [spec](PART_SPECS_T06.md#p0272-mod-routing) · [self-contained txt](../prompts/P0272_mod_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0272  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0272 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0272  (22/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Mixture-of-Depths Routing
file         : parts/t06_routing/P0272_mod_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.mod_routing
language     : Python 3.13
capability   : cap.t06.mod.mod_routing@1
determinism  : seeded
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Routes only a fraction of tokens through each heavy block.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-block token selection with capacity guarantees
  2. static-shape formulation for kernel efficiency
  3. quality-versus-fraction curves
  4. kernel-level speedup verification

Expanded obligations:
  1. Implement per-block token selection with capacity guarantees as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement static-shape formulation for kernel efficiency, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement quality-versus-fraction curves with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Correctness here is
     what makes the tier's GPQA Diamond target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement kernel-level speedup verification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
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
  cap.t06.mod.mod_routing@1
  cap.t06.mod.mod_routing.describe@1

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

  cap.t06.conditional.conditional_layers@1
      if unavailable: use the in-file conservative substitute for
      `conditional_layers` (documented, slower, lower quality) and set
      `degraded['conditional_layers']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t05.verifier.verifier_head@1
      if unavailable: use the in-file conservative substitute for
      `verifier_head` (documented, slower, lower quality) and set
      `degraded['verifier_head']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - per-block token selection with capacity guarantees
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - static-shape formulation for kernel efficiency
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality-versus-fraction curves
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - kernel-level speedup verification
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.mod.mod_routing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 40000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0272_mod_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0273-router-robustness

**P0273 · `router_robustness` — Router Adversarial Robustness** · [spec](PART_SPECS_T06.md#p0273-router-robustness) · [self-contained txt](../prompts/P0273_router_robustness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0273  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0273 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0273  (23/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Router Adversarial Robustness
file         : parts/t06_routing/P0273_router_robustness.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_robustness
language     : Python 3.13
capability   : cap.t06.router.router_robustness@1
determinism  : seeded
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Stops crafted inputs from steering compute or leaking routing information.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. adversarial routing attack construction and defence
  2. routing-side-channel analysis and mitigation
  3. input-perturbation sensitivity measurement
  4. defence effectiveness evaluation

Expanded obligations:
  1. Implement adversarial routing attack construction and defence, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement routing-side-channel analysis and mitigation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement input-perturbation sensitivity measurement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement defence effectiveness evaluation as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against GPQA Diamond — a regression on that
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
  cap.t06.router.router_robustness@1
  cap.t06.router.router_robustness.describe@1

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

  cap.t06.mod.mod_routing@1
      if unavailable: use the in-file conservative substitute for
      `mod_routing` (documented, slower, lower quality) and set
      `degraded['mod_routing']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t05.continual.continual_learning@1
      if unavailable: use the in-file conservative substitute for
      `continual_learning` (documented, slower, lower quality) and set
      `degraded['continual_learning']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - adversarial routing attack construction and defence
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - routing-side-channel analysis and mitigation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - input-perturbation sensitivity measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - defence effectiveness evaluation
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_robustness@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 41000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0273_router_robustness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0274-gating-alternatives

**P0274 · `gating_alternatives` — Alternative Gating Mechanisms** · [spec](PART_SPECS_T06.md#p0274-gating-alternatives) · [self-contained txt](../prompts/P0274_gating_alternatives.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0274  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0274 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0274  (24/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Alternative Gating Mechanisms
file         : parts/t06_routing/P0274_gating_alternatives.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.gating_alternatives
language     : Python 3.13
capability   : cap.t06.gating.gating_alternatives@1
determinism  : seeded
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Sinkhorn, expert-choice, soft-merge and hash gating, compared fairly.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. implementation of four gating families behind one interface
  2. matched-budget quality and latency comparison
  3. stability and determinism properties per family
  4. recommendation with evidence

Expanded obligations:
  1. Implement implementation of four gating families behind one interface
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement matched-budget quality and latency comparison together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement stability and determinism properties per family as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement recommendation with evidence, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's GPQA Diamond target reachable; the part
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
  cap.t06.gating.gating_alternatives@1
  cap.t06.gating.gating_alternatives.describe@1

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

  cap.t06.router.router_robustness@1
      if unavailable: use the in-file conservative substitute for
      `router_robustness` (documented, slower, lower quality) and set
      `degraded['router_robustness']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t05.depth.depth_width_tradeoff@1
      if unavailable: use the in-file conservative substitute for
      `depth_width_tradeoff` (documented, slower, lower quality) and set
      `degraded['depth_width_tradeoff']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - implementation of four gating families behind one interface
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - matched-budget quality and latency comparison
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - stability and determinism properties per family
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - recommendation with evidence
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.gating.gating_alternatives@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 42000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0274_gating_alternatives.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0275-expert-choice-routing

**P0275 · `expert_choice_routing` — Expert-Choice Routing** · [spec](PART_SPECS_T06.md#p0275-expert-choice-routing) · [self-contained txt](../prompts/P0275_expert_choice_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0275  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0275 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0275  (25/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert-Choice Routing
file         : parts/t06_routing/P0275_expert_choice_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_choice_routing
language     : Python 3.13
capability   : cap.t06.expert.expert_choice_routing@1
determinism  : seeded
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Experts pick tokens: perfect balance by construction.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. expert-choice assignment with capacity-exact selection
  2. causality preservation in autoregressive decoding
  3. quality comparison against token-choice routing
  4. throughput measurement under skew

Expanded obligations:
  1. Implement expert-choice assignment with capacity-exact selection
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement causality preservation in autoregressive decoding as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement quality comparison against token-choice routing, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement throughput measurement under skew with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.expert.expert_choice_routing@1
  cap.t06.expert.expert_choice_routing.describe@1

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

  cap.t06.gating.gating_alternatives@1
      if unavailable: use the in-file conservative substitute for
      `gating_alternatives` (documented, slower, lower quality) and set
      `degraded['gating_alternatives']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t05.sparse.sparse_upcycling@1
      if unavailable: use the in-file conservative substitute for
      `sparse_upcycling` (documented, slower, lower quality) and set
      `degraded['sparse_upcycling']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - expert-choice assignment with capacity-exact selection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - causality preservation in autoregressive decoding
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality comparison against token-choice routing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput measurement under skew
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_choice_routing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 43000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0275_expert_choice_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0276-moe-scaling-laws

**P0276 · `moe_scaling_laws` — MoE Scaling Laws & Budget Allocation** · [spec](PART_SPECS_T06.md#p0276-moe-scaling-laws) · [self-contained txt](../prompts/P0276_moe_scaling_laws.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0276  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0276 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0276  (26/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : MoE Scaling Laws & Budget Allocation
file         : parts/t06_routing/P0276_moe_scaling_laws.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_scaling_laws
language     : Python 3.13
capability   : cap.t06.moe.moe_scaling_laws@1
determinism  : seeded
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Predicts the best (experts, granularity, active-params) point.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. scaling-law fits over expert count and granularity
  2. compute-optimal sparsity derivation
  3. extrapolation confidence intervals
  4. validation on held-out configurations

Expanded obligations:
  1. Implement scaling-law fits over expert count and granularity as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement compute-optimal sparsity derivation, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement extrapolation confidence intervals with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement validation on held-out configurations together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
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
  cap.t06.moe.moe_scaling_laws@1
  cap.t06.moe.moe_scaling_laws.describe@1

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

  cap.t06.expert.expert_choice_routing@1
      if unavailable: use the in-file conservative substitute for
      `expert_choice_routing` (documented, slower, lower quality) and set
      `degraded['expert_choice_routing']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t05.model.model_config_schema@1
      if unavailable: use the in-file conservative substitute for
      `model_config_schema` (documented, slower, lower quality) and set
      `degraded['model_config_schema']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - scaling-law fits over expert count and granularity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - compute-optimal sparsity derivation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - extrapolation confidence intervals
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - validation on held-out configurations
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_scaling_laws@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 44000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0276_moe_scaling_laws.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0277-router-interpretability

**P0277 · `router_interpretability` — Router Interpretability & Expert Naming** · [spec](PART_SPECS_T06.md#p0277-router-interpretability) · [self-contained txt](../prompts/P0277_router_interpretability.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0277  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0277 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0277  (27/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Router Interpretability & Expert Naming
file         : parts/t06_routing/P0277_router_interpretability.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_interpretability
language     : Python 3.13
capability   : cap.t06.router.router_interpretability@1
determinism  : seeded
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Explains what each of 512 experts is for, in words.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. activation-clustering and exemplar extraction per expert
  2. automatic expert labelling with verification
  3. routing-decision explanation for a given token
  4. label-accuracy human-agreement measurement

Expanded obligations:
  1. Implement activation-clustering and exemplar extraction per expert, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement automatic expert labelling with verification with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  3. Implement routing-decision explanation for a given token together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement label-accuracy human-agreement measurement as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.router.router_interpretability@1
  cap.t06.router.router_interpretability.describe@1

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

  cap.t06.moe.moe_scaling_laws@1
      if unavailable: use the in-file conservative substitute for
      `moe_scaling_laws` (documented, slower, lower quality) and set
      `degraded['moe_scaling_laws']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t05.attention.attention_variants@1
      if unavailable: use the in-file conservative substitute for
      `attention_variants` (documented, slower, lower quality) and set
      `degraded['attention_variants']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - activation-clustering and exemplar extraction per expert
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automatic expert labelling with verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - routing-decision explanation for a given token
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - label-accuracy human-agreement measurement
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_interpretability@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 45000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0277_router_interpretability.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0278-moe-training-stability

**P0278 · `moe_training_stability` — MoE Training Stability Engineering** · [spec](PART_SPECS_T06.md#p0278-moe-training-stability) · [self-contained txt](../prompts/P0278_moe_training_stability.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0278  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0278 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0278  (28/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : MoE Training Stability Engineering
file         : parts/t06_routing/P0278_moe_training_stability.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_training_stability
language     : Python 3.13
capability   : cap.t06.moe.moe_training_stability@1
determinism  : seeded
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Sparse models are fragile; this part makes them not.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. router z-loss and logit-clipping with tuning evidence
  2. gradient-spike detection and rollback
  3. precision requirements for the routing path
  4. long-run stability evidence at scale

Expanded obligations:
  1. Implement router z-loss and logit-clipping with tuning evidence with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement gradient-spike detection and rollback together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement precision requirements for the routing path as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  4. Implement long-run stability evidence at scale, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
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
  cap.t06.moe.moe_training_stability@1
  cap.t06.moe.moe_training_stability.describe@1

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

  cap.t06.router.router_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `router_interpretability` (documented, slower, lower quality) and set
      `degraded['router_interpretability']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t05.activation.activation_design@1
      if unavailable: use the in-file conservative substitute for
      `activation_design` (documented, slower, lower quality) and set
      `degraded['activation_design']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - router z-loss and logit-clipping with tuning evidence
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - gradient-spike detection and rollback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - precision requirements for the routing path
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - long-run stability evidence at scale
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_training_stability@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 46000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0278_moe_training_stability.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0279-expert-dropout

**P0279 · `expert_dropout` — Expert Dropout & Robustness to Missing Experts** · [spec](PART_SPECS_T06.md#p0279-expert-dropout) · [self-contained txt](../prompts/P0279_expert_dropout.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0279  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0279 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0279  (29/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Dropout & Robustness to Missing Experts
file         : parts/t06_routing/P0279_expert_dropout.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_dropout
language     : Python 3.13
capability   : cap.t06.expert.expert_dropout@1
determinism  : seeded
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
The model still works when some experts are unavailable.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. expert-dropout training for graceful degradation
  2. quality curves versus fraction of missing experts
  3. automatic rerouting on expert failure
  4. failure-mode testing under device loss

Expanded obligations:
  1. Implement expert-dropout training for graceful degradation together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement quality curves versus fraction of missing experts as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement automatic rerouting on expert failure, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement failure-mode testing under device loss with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.expert.expert_dropout@1
  cap.t06.expert.expert_dropout.describe@1

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

  cap.t06.moe.moe_training_stability@1
      if unavailable: use the in-file conservative substitute for
      `moe_training_stability` (documented, slower, lower quality) and set
      `degraded['moe_training_stability']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t05.draft.draft_model_arch@1
      if unavailable: use the in-file conservative substitute for
      `draft_model_arch` (documented, slower, lower quality) and set
      `degraded['draft_model_arch']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - expert-dropout training for graceful degradation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quality curves versus fraction of missing experts
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic rerouting on expert failure
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - failure-mode testing under device loss
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_dropout@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 47000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0279_expert_dropout.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0280-sparse-kernels-bridge

**P0280 · `sparse_kernels_bridge` — Routing-to-Kernel Bridge** · [spec](PART_SPECS_T06.md#p0280-sparse-kernels-bridge) · [self-contained txt](../prompts/P0280_sparse_kernels_bridge.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0280  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0280 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0280  (30/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Routing-to-Kernel Bridge
file         : parts/t06_routing/P0280_sparse_kernels_bridge.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.sparse_kernels_bridge
language     : Python 3.13
capability   : cap.t06.sparse.sparse_kernels_bridge@1
determinism  : seeded
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Turns routing decisions into efficient grouped-GEMM invocations.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. permutation/index construction fused with routing
  2. group-descriptor generation for the T02 grouped kernels
  3. index-build overhead measurement
  4. end-to-end MoE layer latency budget enforcement

Expanded obligations:
  1. Implement permutation/index construction fused with routing as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement group-descriptor generation for the T02 grouped kernels, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GPQA Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement index-build overhead measurement with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement end-to-end MoE layer latency budget enforcement together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.

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
  cap.t06.sparse.sparse_kernels_bridge@1
  cap.t06.sparse.sparse_kernels_bridge.describe@1

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

  cap.t06.expert.expert_dropout@1
      if unavailable: use the in-file conservative substitute for
      `expert_dropout` (documented, slower, lower quality) and set
      `degraded['expert_dropout']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t05.meta.meta_learning_arch@1
      if unavailable: use the in-file conservative substitute for
      `meta_learning_arch` (documented, slower, lower quality) and set
      `degraded['meta_learning_arch']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - permutation/index construction fused with routing
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - group-descriptor generation for the T02 grouped kernels
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - index-build overhead measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - end-to-end MoE layer latency budget enforcement
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.sparse.sparse_kernels_bridge@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 48000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0280_sparse_kernels_bridge.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0281-modality-routing

**P0281 · `modality_routing` — Modality- & Language-Aware Routing** · [spec](PART_SPECS_T06.md#p0281-modality-routing) · [self-contained txt](../prompts/P0281_modality_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0281  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0281 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0281  (31/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Modality- & Language-Aware Routing
file         : parts/t06_routing/P0281_modality_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.modality_routing
language     : Python 3.13
capability   : cap.t06.modality.modality_routing@1
determinism  : seeded
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Sends image, audio, code and language tokens to the right specialists.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. modality tag propagation into the routing decision
  2. language-family expert allocation with fairness measurement
  3. cross-modal expert sharing analysis
  4. per-modality quality measurement

Expanded obligations:
  1. Implement modality tag propagation into the routing decision, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement language-family expert allocation with fairness measurement
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement cross-modal expert sharing analysis together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement per-modality quality measurement as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
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
  cap.t06.modality.modality_routing@1
  cap.t06.modality.modality_routing.describe@1

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

  cap.t06.sparse.sparse_kernels_bridge@1
      if unavailable: use the in-file conservative substitute for
      `sparse_kernels_bridge` (documented, slower, lower quality) and set
      `degraded['sparse_kernels_bridge']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t05.architecture.architecture_search@1
      if unavailable: use the in-file conservative substitute for
      `architecture_search` (documented, slower, lower quality) and set
      `degraded['architecture_search']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - modality tag propagation into the routing decision
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - language-family expert allocation with fairness measurement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cross-modal expert sharing analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - per-modality quality measurement
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.modality.modality_routing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 49000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0281_modality_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0282-difficulty-routing

**P0282 · `difficulty_routing` — Difficulty-Aware Compute Routing** · [spec](PART_SPECS_T06.md#p0282-difficulty-routing) · [self-contained txt](../prompts/P0282_difficulty_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0282  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0282 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0282  (32/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Difficulty-Aware Compute Routing
file         : parts/t06_routing/P0282_difficulty_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.difficulty_routing
language     : Python 3.13
capability   : cap.t06.difficulty.difficulty_routing@1
determinism  : seeded
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Predicts problem hardness and allocates compute accordingly.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. difficulty estimator trained on solve-rate labels
  2. compute-allocation policy under a global budget
  3. calibration of difficulty predictions
  4. measured accuracy-per-FLOP improvement

Expanded obligations:
  1. Implement difficulty estimator trained on solve-rate labels with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement compute-allocation policy under a global budget together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement calibration of difficulty predictions as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured accuracy-per-FLOP improvement, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
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
  cap.t06.difficulty.difficulty_routing@1
  cap.t06.difficulty.difficulty_routing.describe@1

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

  cap.t06.modality.modality_routing@1
      if unavailable: use the in-file conservative substitute for
      `modality_routing` (documented, slower, lower quality) and set
      `degraded['modality_routing']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t05.speculative.speculative_arch_hooks@1
      if unavailable: use the in-file conservative substitute for
      `speculative_arch_hooks` (documented, slower, lower quality) and set
      `degraded['speculative_arch_hooks']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - difficulty estimator trained on solve-rate labels
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - compute-allocation policy under a global budget
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - calibration of difficulty predictions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured accuracy-per-FLOP improvement
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.difficulty.difficulty_routing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 3000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0282_difficulty_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0283-cost-aware-routing

**P0283 · `cost_aware_routing` — Cost- & SLO-Aware Routing Policy** · [spec](PART_SPECS_T06.md#p0283-cost-aware-routing) · [self-contained txt](../prompts/P0283_cost_aware_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0283  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0283 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0283  (33/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Cost- & SLO-Aware Routing Policy
file         : parts/t06_routing/P0283_cost_aware_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.cost_aware_routing
language     : Python 3.13
capability   : cap.t06.cost.cost_aware_routing@1
determinism  : seeded
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Routes for dollars and deadlines, not only accuracy.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-objective routing with explicit price of quality
  2. SLO-class-specific policies with admission control
  3. cost-per-solved-task accounting
  4. Pareto-frontier measurement versus fixed policies

Expanded obligations:
  1. Implement multi-objective routing with explicit price of quality
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement SLO-class-specific policies with admission control as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  3. Implement cost-per-solved-task accounting, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement Pareto-frontier measurement versus fixed policies with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.cost.cost_aware_routing@1
  cap.t06.cost.cost_aware_routing.describe@1

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

  cap.t06.difficulty.difficulty_routing@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_routing` (documented, slower, lower quality) and set
      `degraded['difficulty_routing']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t05.expert.expert_specialisation@1
      if unavailable: use the in-file conservative substitute for
      `expert_specialisation` (documented, slower, lower quality) and set
      `degraded['expert_specialisation']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - multi-objective routing with explicit price of quality
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - SLO-class-specific policies with admission control
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cost-per-solved-task accounting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - Pareto-frontier measurement versus fixed policies
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.cost.cost_aware_routing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 4000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0283_cost_aware_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0284-model-cascade-routing

**P0284 · `model_cascade_routing` — Model Cascade & Escalation Router** · [spec](PART_SPECS_T06.md#p0284-model-cascade-routing) · [self-contained txt](../prompts/P0284_model_cascade_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0284  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0284 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0284  (34/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Model Cascade & Escalation Router
file         : parts/t06_routing/P0284_model_cascade_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.model_cascade_routing
language     : Python 3.13
capability   : cap.t06.model.model_cascade_routing@1
determinism  : seeded
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Cheap model first, escalate only when the verifier is unsure.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cascade tier definition with calibrated escalation thresholds
  2. escalation-policy optimisation under cost constraints
  3. quality-preservation proof versus always-large routing
  4. measured cost reduction at matched accuracy

Expanded obligations:
  1. Implement cascade tier definition with calibrated escalation thresholds
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement escalation-policy optimisation under cost constraints, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement quality-preservation proof versus always-large routing with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured cost reduction at matched accuracy together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.model.model_cascade_routing@1
  cap.t06.model.model_cascade_routing.describe@1

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

  cap.t06.cost.cost_aware_routing@1
      if unavailable: use the in-file conservative substitute for
      `cost_aware_routing` (documented, slower, lower quality) and set
      `degraded['cost_aware_routing']='local'`

  cap.t05.hybrid.hybrid_mixer@1
      if unavailable: use the in-file conservative substitute for
      `hybrid_mixer` (documented, slower, lower quality) and set
      `degraded['hybrid_mixer']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - cascade tier definition with calibrated escalation thresholds
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - escalation-policy optimisation under cost constraints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality-preservation proof versus always-large routing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured cost reduction at matched accuracy
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.model.model_cascade_routing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 5000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0284_model_cascade_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0285-ensemble-combiner

**P0285 · `ensemble_combiner` — Ensemble & Multi-Sample Combination** · [spec](PART_SPECS_T06.md#p0285-ensemble-combiner) · [self-contained txt](../prompts/P0285_ensemble_combiner.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0285  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0285 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0285  (35/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Ensemble & Multi-Sample Combination
file         : parts/t06_routing/P0285_ensemble_combiner.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.ensemble_combiner
language     : Python 3.13
capability   : cap.t06.ensemble.ensemble_combiner@1
determinism  : seeded
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Turns several cheap samples into one better answer.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. self-consistency, weighted voting and verifier-ranked selection
  2. diversity-inducing sampling policies
  3. cost-versus-accuracy curves for sample counts
  4. when-not-to-ensemble decision rule

Expanded obligations:
  1. Implement self-consistency, weighted voting and verifier-ranked
     selection, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement diversity-inducing sampling policies with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement cost-versus-accuracy curves for sample counts together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement when-not-to-ensemble decision rule as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against GPQA Diamond — a regression on that
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
  cap.t06.ensemble.ensemble_combiner@1
  cap.t06.ensemble.ensemble_combiner.describe@1

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

  cap.t06.model.model_cascade_routing@1
      if unavailable: use the in-file conservative substitute for
      `model_cascade_routing` (documented, slower, lower quality) and set
      `degraded['model_cascade_routing']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t05.normalisation.normalisation_design@1
      if unavailable: use the in-file conservative substitute for
      `normalisation_design` (documented, slower, lower quality) and set
      `degraded['normalisation_design']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - self-consistency, weighted voting and verifier-ranked selection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - diversity-inducing sampling policies
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cost-versus-accuracy curves for sample counts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - when-not-to-ensemble decision rule
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.ensemble.ensemble_combiner@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 6000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0285_ensemble_combiner.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0286-router-cache

**P0286 · `router_cache` — Routing Decision Cache** · [spec](PART_SPECS_T06.md#p0286-router-cache) · [self-contained txt](../prompts/P0286_router_cache.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0286  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0286 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0286  (36/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Routing Decision Cache
file         : parts/t06_routing/P0286_router_cache.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_cache
language     : Python 3.13
capability   : cap.t06.router.router_cache@1
determinism  : seeded
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Reuses routing decisions for repeated prefixes (feeds S4).

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. prefix-keyed routing cache with invalidation rules
  2. hit-rate measurement on production-like traffic
  3. correctness verification of cached routing
  4. latency saving attribution

Expanded obligations:
  1. Implement prefix-keyed routing cache with invalidation rules with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement hit-rate measurement on production-like traffic together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement correctness verification of cached routing as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  4. Implement latency saving attribution, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's GPQA Diamond target reachable; the part
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
  cap.t06.router.router_cache@1
  cap.t06.router.router_cache.describe@1

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

  cap.t06.ensemble.ensemble_combiner@1
      if unavailable: use the in-file conservative substitute for
      `ensemble_combiner` (documented, slower, lower quality) and set
      `degraded['ensemble_combiner']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t05.multi.multi_token_prediction@1
      if unavailable: use the in-file conservative substitute for
      `multi_token_prediction` (documented, slower, lower quality) and set
      `degraded['multi_token_prediction']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - prefix-keyed routing cache with invalidation rules
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hit-rate measurement on production-like traffic
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - correctness verification of cached routing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - latency saving attribution
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_cache@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 7000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0286_router_cache.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0287-expert-warmup

**P0287 · `expert_warmup` — Expert Warmup & Cold-Start Handling** · [spec](PART_SPECS_T06.md#p0287-expert-warmup) · [self-contained txt](../prompts/P0287_expert_warmup.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0287  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0287 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0287  (37/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Expert Warmup & Cold-Start Handling
file         : parts/t06_routing/P0287_expert_warmup.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_warmup
language     : Python 3.13
capability   : cap.t06.expert.expert_warmup@1
determinism  : seeded
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Avoids first-request latency cliffs.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. predictive warmup from traffic forecasts
  2. cold-expert latency measurement and mitigation
  3. warmup cost budgeting
  4. p99 improvement measurement after warmup

Expanded obligations:
  1. Implement predictive warmup from traffic forecasts together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement cold-expert latency measurement and mitigation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement warmup cost budgeting, and make it correct under concurrency:
     at least 64 in-flight `OmegaEnvelope`s must be able to traverse it
     simultaneously. No lock, mutex or borrow may be held across an `await` /
     `.await` / `yield` boundary, and the part must expose a contention
     counter so T09 can attribute latency to it. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement p99 improvement measurement after warmup with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.

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
  cap.t06.expert.expert_warmup@1
  cap.t06.expert.expert_warmup.describe@1

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

  cap.t06.router.router_cache@1
      if unavailable: use the in-file conservative substitute for
      `router_cache` (documented, slower, lower quality) and set
      `degraded['router_cache']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t05.program.program_induction_arch@1
      if unavailable: use the in-file conservative substitute for
      `program_induction_arch` (documented, slower, lower quality) and set
      `degraded['program_induction_arch']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - predictive warmup from traffic forecasts
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cold-expert latency measurement and mitigation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - warmup cost budgeting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - p99 improvement measurement after warmup
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_warmup@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 8000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0287_expert_warmup.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0288-routing-fairness

**P0288 · `routing_fairness` — Cross-User Routing Fairness & Isolation** · [spec](PART_SPECS_T06.md#p0288-routing-fairness) · [self-contained txt](../prompts/P0288_routing_fairness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0288  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0288 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0288  (38/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Cross-User Routing Fairness & Isolation
file         : parts/t06_routing/P0288_routing_fairness.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.routing_fairness
language     : Python 3.13
capability   : cap.t06.routing.routing_fairness@1
determinism  : seeded
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
One user's traffic must not degrade another's routing quality.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-tenant expert-utilisation accounting
  2. fairness enforcement in capacity allocation
  3. isolation verification under adversarial load
  4. fairness metric reporting

Expanded obligations:
  1. Implement per-tenant expert-utilisation accounting as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement fairness enforcement in capacity allocation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement isolation verification under adversarial load with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  4. Implement fairness metric reporting together with its verification path,
     so that anything this mechanism produces can be independently re-checked
     *inside this same file* without contacting any other part. The checker
     must be cheap enough to run on every call in debug mode and must be
     wired into `selftest()`. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
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
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.routing.routing_fairness@1
  cap.t06.routing.routing_fairness.describe@1

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

  cap.t06.expert.expert_warmup@1
      if unavailable: use the in-file conservative substitute for
      `expert_warmup` (documented, slower, lower quality) and set
      `degraded['expert_warmup']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t05.init.init_scaling_laws@1
      if unavailable: use the in-file conservative substitute for
      `init_scaling_laws` (documented, slower, lower quality) and set
      `degraded['init_scaling_laws']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - per-tenant expert-utilisation accounting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fairness enforcement in capacity allocation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - isolation verification under adversarial load
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fairness metric reporting
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.routing.routing_fairness@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 9000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0288_routing_fairness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0289-moe-memory-budget

**P0289 · `moe_memory_budget` — MoE Memory Budget Planner** · [spec](PART_SPECS_T06.md#p0289-moe-memory-budget) · [self-contained txt](../prompts/P0289_moe_memory_budget.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0289  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0289 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0289  (39/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : MoE Memory Budget Planner
file         : parts/t06_routing/P0289_moe_memory_budget.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_memory_budget
language     : Python 3.13
capability   : cap.t06.moe.moe_memory_budget@1
determinism  : seeded
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Fits a sparse model into a fixed memory envelope, optimally.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. placement/precision/offload joint optimisation under a memory cap
  2. feasibility checking with clear infeasibility explanations
  3. plan quality versus exhaustive search on small cases
  4. measured quality at multiple memory budgets

Expanded obligations:
  1. Implement placement/precision/offload joint optimisation under a memory
     cap, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement feasibility checking with clear infeasibility explanations
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement plan quality versus exhaustive search on small cases together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured quality at multiple memory budgets as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GPQA
     Diamond target reachable; the part therefore ships a microbenchmark that
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.moe.moe_memory_budget@1
  cap.t06.moe.moe_memory_budget.describe@1

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

  cap.t06.routing.routing_fairness@1
      if unavailable: use the in-file conservative substitute for
      `routing_fairness` (documented, slower, lower quality) and set
      `degraded['routing_fairness']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t05.memory.memory_attention_bridge@1
      if unavailable: use the in-file conservative substitute for
      `memory_attention_bridge` (documented, slower, lower quality) and set
      `degraded['memory_attention_bridge']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - placement/precision/offload joint optimisation under a memory ca
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - feasibility checking with clear infeasibility explanations
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - plan quality versus exhaustive search on small cases
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured quality at multiple memory budgets
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_memory_budget@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 10000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0289_moe_memory_budget.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0290-router-online-learning

**P0290 · `router_online_learning` — Online Router Adaptation** · [spec](PART_SPECS_T06.md#p0290-router-online-learning) · [self-contained txt](../prompts/P0290_router_online_learning.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0290  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0290 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0290  (40/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Online Router Adaptation
file         : parts/t06_routing/P0290_router_online_learning.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_online_learning
language     : Python 3.13
capability   : cap.t06.router.router_online_learning@1
determinism  : seeded
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
The router keeps improving from production feedback, safely.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. bandit-style online updates with guardrails and rollback
  2. distribution-shift detection triggering adaptation
  3. safety constraints preventing quality regression
  4. measured improvement over a frozen router

Expanded obligations:
  1. Implement bandit-style online updates with guardrails and rollback with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement distribution-shift detection triggering adaptation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement safety constraints preventing quality regression as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured improvement over a frozen router, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
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
  cap.t06.router.router_online_learning@1
  cap.t06.router.router_online_learning.describe@1

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

  cap.t06.moe.moe_memory_budget@1
      if unavailable: use the in-file conservative substitute for
      `moe_memory_budget` (documented, slower, lower quality) and set
      `degraded['moe_memory_budget']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t05.thought.thought_representation@1
      if unavailable: use the in-file conservative substitute for
      `thought_representation` (documented, slower, lower quality) and set
      `degraded['thought_representation']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - bandit-style online updates with guardrails and rollback
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - distribution-shift detection triggering adaptation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - safety constraints preventing quality regression
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured improvement over a frozen router
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_online_learning@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 11000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0290_router_online_learning.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0291-sparse-gradient

**P0291 · `sparse_gradient` — Sparse Gradient Handling & Accumulation** · [spec](PART_SPECS_T06.md#p0291-sparse-gradient) · [self-contained txt](../prompts/P0291_sparse_gradient.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0291  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0291 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0291  (41/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Sparse Gradient Handling & Accumulation
file         : parts/t06_routing/P0291_sparse_gradient.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.sparse_gradient
language     : Python 3.13
capability   : cap.t06.sparse.sparse_gradient@1
determinism  : seeded
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Correct, efficient gradients through discrete routing.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gradient routing with correct expert attribution
  2. sparse accumulation with deterministic ordering
  3. gradient-correctness verification versus dense reference
  4. throughput measurement of the backward path

Expanded obligations:
  1. Implement gradient routing with correct expert attribution together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement sparse accumulation with deterministic ordering as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement gradient-correctness verification versus dense reference, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GPQA Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement throughput measurement of the backward path with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.sparse.sparse_gradient@1
  cap.t06.sparse.sparse_gradient.describe@1

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

  cap.t06.router.router_online_learning@1
      if unavailable: use the in-file conservative substitute for
      `router_online_learning` (documented, slower, lower quality) and set
      `degraded['router_online_learning']='local'`

  cap.t05.omega.omega_block@1
      if unavailable: use the in-file conservative substitute for
      `omega_block` (documented, slower, lower quality) and set
      `degraded['omega_block']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - gradient routing with correct expert attribution
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - sparse accumulation with deterministic ordering
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - gradient-correctness verification versus dense reference
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput measurement of the backward path
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.sparse.sparse_gradient@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 12000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0291_sparse_gradient.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0292-expert-alignment

**P0292 · `expert_alignment` — Per-Expert Safety & Alignment Auditing** · [spec](PART_SPECS_T06.md#p0292-expert-alignment) · [self-contained txt](../prompts/P0292_expert_alignment.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0292  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0292 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0292  (42/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Per-Expert Safety & Alignment Auditing
file         : parts/t06_routing/P0292_expert_alignment.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.expert_alignment
language     : Python 3.13
capability   : cap.t06.expert.expert_alignment@1
determinism  : seeded
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
No expert becomes a loophole in the safety system.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-expert behavioural audit with targeted probes
  2. detection of experts that disproportionately produce refusable content
  3. expert-level intervention and retraining protocol
  4. audit coverage report over all 512 experts

Expanded obligations:
  1. Implement per-expert behavioural audit with targeted probes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement detection of experts that disproportionately produce refusable
     content, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GPQA Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement expert-level intervention and retraining protocol with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement audit coverage report over all 512 experts together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.

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
  cap.t06.expert.expert_alignment@1
  cap.t06.expert.expert_alignment.describe@1

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

  cap.t06.sparse.sparse_gradient@1
      if unavailable: use the in-file conservative substitute for
      `sparse_gradient` (documented, slower, lower quality) and set
      `degraded['sparse_gradient']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t05.adaptive.adaptive_depth@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_depth` (documented, slower, lower quality) and set
      `degraded['adaptive_depth']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - per-expert behavioural audit with targeted probes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - detection of experts that disproportionately produce refusable c
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - expert-level intervention and retraining protocol
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - audit coverage report over all 512 experts
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.expert.expert_alignment@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 13000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0292_expert_alignment.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0293-routing-privacy

**P0293 · `routing_privacy` — Routing Privacy & Side-Channel Defence** · [spec](PART_SPECS_T06.md#p0293-routing-privacy) · [self-contained txt](../prompts/P0293_routing_privacy.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0293  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0293 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0293  (43/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Routing Privacy & Side-Channel Defence
file         : parts/t06_routing/P0293_routing_privacy.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.routing_privacy
language     : Python 3.13
capability   : cap.t06.routing.routing_privacy@1
determinism  : seeded
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Routing patterns must not leak user content.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. information-leakage quantification from routing traces
  2. noise/padding defences with utility cost measurement
  3. telemetry redaction policy for routing data
  4. attack-simulation results

Expanded obligations:
  1. Implement information-leakage quantification from routing traces, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GPQA Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement noise/padding defences with utility cost measurement with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement telemetry redaction policy for routing data together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement attack-simulation results as a first-class, fully realised
     mechanism. No stub, no `NotImplementedError`, no configuration flag
     whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of GPQA Diamond, so its p99
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
  cap.t06.routing.routing_privacy@1
  cap.t06.routing.routing_privacy.describe@1

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

  cap.t06.expert.expert_alignment@1
      if unavailable: use the in-file conservative substitute for
      `expert_alignment` (documented, slower, lower quality) and set
      `degraded['expert_alignment']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t05.long.long_context_arch@1
      if unavailable: use the in-file conservative substitute for
      `long_context_arch` (documented, slower, lower quality) and set
      `degraded['long_context_arch']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - information-leakage quantification from routing traces
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - noise/padding defences with utility cost measurement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - telemetry redaction policy for routing data
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - attack-simulation results
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.routing.routing_privacy@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 14000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0293_routing_privacy.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0294-hierarchical-routing

**P0294 · `hierarchical_routing` — Hierarchical Two-Level Routing** · [spec](PART_SPECS_T06.md#p0294-hierarchical-routing) · [self-contained txt](../prompts/P0294_hierarchical_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0294  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0294 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0294  (44/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Hierarchical Two-Level Routing
file         : parts/t06_routing/P0294_hierarchical_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.hierarchical_routing
language     : Python 3.13
capability   : cap.t06.hierarchical.hierarchical_routing@1
determinism  : seeded
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Route to a group, then to an expert: scales to 100k experts.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. group-then-expert routing with balanced group assignment
  2. communication savings from group locality
  3. quality comparison against flat routing
  4. scalability measurement at very high expert counts

Expanded obligations:
  1. Implement group-then-expert routing with balanced group assignment with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement communication savings from group locality together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's GPQA Diamond target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement quality comparison against flat routing as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of GPQA
     Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement scalability measurement at very high expert counts, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
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
  cap.t06.hierarchical.hierarchical_routing@1
  cap.t06.hierarchical.hierarchical_routing.describe@1

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

  cap.t06.routing.routing_privacy@1
      if unavailable: use the in-file conservative substitute for
      `routing_privacy` (documented, slower, lower quality) and set
      `degraded['routing_privacy']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t05.symbolic.symbolic_bridge@1
      if unavailable: use the in-file conservative substitute for
      `symbolic_bridge` (documented, slower, lower quality) and set
      `degraded['symbolic_bridge']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - group-then-expert routing with balanced group assignment
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - communication savings from group locality
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality comparison against flat routing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - scalability measurement at very high expert counts
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.hierarchical.hierarchical_routing@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 15000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0294_hierarchical_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0295-router-bench

**P0295 · `router_bench` — Routing Benchmark & Regression Suite** · [spec](PART_SPECS_T06.md#p0295-router-bench) · [self-contained txt](../prompts/P0295_router_bench.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0295  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0295 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0295  (45/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Routing Benchmark & Regression Suite
file         : parts/t06_routing/P0295_router_bench.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.router_bench
language     : Python 3.13
capability   : cap.t06.router.router_bench@1
determinism  : seeded
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
The canonical measurements for every routing change.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. benchmark tasks covering balance, quality, latency and determinism
  2. traffic replay corpus with realistic skew
  3. regression gates with statistical significance
  4. baseline records and change-review checklist

Expanded obligations:
  1. Implement benchmark tasks covering balance, quality, latency and
     determinism together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's GPQA Diamond
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  2. Implement traffic replay corpus with realistic skew as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of GPQA
     Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement regression gates with statistical significance, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement baseline records and change-review checklist with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
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
  cap.t06.router.router_bench@1
  cap.t06.router.router_bench.describe@1

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

  cap.t06.hierarchical.hierarchical_routing@1
      if unavailable: use the in-file conservative substitute for
      `hierarchical_routing` (documented, slower, lower quality) and set
      `degraded['hierarchical_routing']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t05.weight.weight_sharing@1
      if unavailable: use the in-file conservative substitute for
      `weight_sharing` (documented, slower, lower quality) and set
      `degraded['weight_sharing']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - benchmark tasks covering balance, quality, latency and determini
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - traffic replay corpus with realistic skew
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regression gates with statistical significance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - baseline records and change-review checklist
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.router.router_bench@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 16000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0295_router_bench.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0296-moe-visualisation

**P0296 · `moe_visualisation` — Sparse Compute Visualisation & Explainer** · [spec](PART_SPECS_T06.md#p0296-moe-visualisation) · [self-contained txt](../prompts/P0296_moe_visualisation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0296  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0296 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0296  (46/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Sparse Compute Visualisation & Explainer
file         : parts/t06_routing/P0296_moe_visualisation.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_visualisation
language     : Python 3.13
capability   : cap.t06.moe.moe_visualisation@1
determinism  : seeded
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Makes 512-expert behaviour legible to a human operator.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. routing heatmaps, flow diagrams and drift dashboards as data artifacts
  2. per-request routing trace explanation
  3. anomaly highlighting with drill-down
  4. usability validation with operator tasks

Expanded obligations:
  1. Implement routing heatmaps, flow diagrams and drift dashboards as data
     artifacts as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GPQA Diamond, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement per-request routing trace explanation, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement anomaly highlighting with drill-down with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement usability validation with operator tasks together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.moe.moe_visualisation@1
  cap.t06.moe.moe_visualisation.describe@1

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

  cap.t06.router.router_bench@1
      if unavailable: use the in-file conservative substitute for
      `router_bench` (documented, slower, lower quality) and set
      `degraded['router_bench']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t05.action.action_head@1
      if unavailable: use the in-file conservative substitute for
      `action_head` (documented, slower, lower quality) and set
      `degraded['action_head']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - routing heatmaps, flow diagrams and drift dashboards as data art
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-request routing trace explanation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - anomaly highlighting with drill-down
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - usability validation with operator tasks
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_visualisation@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 17000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0296_moe_visualisation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0297-adaptive-sparsity

**P0297 · `adaptive_sparsity` — Runtime-Adaptive Sparsity Control** · [spec](PART_SPECS_T06.md#p0297-adaptive-sparsity) · [self-contained txt](../prompts/P0297_adaptive_sparsity.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0297  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0297 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0297  (47/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Runtime-Adaptive Sparsity Control
file         : parts/t06_routing/P0297_adaptive_sparsity.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.adaptive_sparsity
language     : Python 3.13
capability   : cap.t06.adaptive.adaptive_sparsity@1
determinism  : seeded
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Turns sparsity up or down live to meet load and SLOs.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. closed-loop controller from latency/quality telemetry
  2. stability analysis preventing oscillation
  3. quality floor enforcement under load spikes
  4. measured SLO attainment during traffic surges

Expanded obligations:
  1. Implement closed-loop controller from latency/quality telemetry, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement stability analysis preventing oscillation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GPQA Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement quality floor enforcement under load spikes together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement measured SLO attainment during traffic surges as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.adaptive.adaptive_sparsity@1
  cap.t06.adaptive.adaptive_sparsity.describe@1

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

  cap.t06.moe.moe_visualisation@1
      if unavailable: use the in-file conservative substitute for
      `moe_visualisation` (documented, slower, lower quality) and set
      `degraded['moe_visualisation']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t05.prompt.prompt_representation@1
      if unavailable: use the in-file conservative substitute for
      `prompt_representation` (documented, slower, lower quality) and set
      `degraded['prompt_representation']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - closed-loop controller from latency/quality telemetry
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - stability analysis preventing oscillation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality floor enforcement under load spikes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured SLO attainment during traffic surges
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.adaptive.adaptive_sparsity@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 18000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0297_adaptive_sparsity.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0298-sparsity-verification

**P0298 · `sparsity_verification` — Conditional-Compute Correctness Verification** · [spec](PART_SPECS_T06.md#p0298-sparsity-verification) · [self-contained txt](../prompts/P0298_sparsity_verification.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0298  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0298 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0298  (48/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Conditional-Compute Correctness Verification
file         : parts/t06_routing/P0298_sparsity_verification.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.sparsity_verification
language     : Python 3.13
capability   : cap.t06.sparsity.sparsity_verification@1
determinism  : seeded
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Proves the sparse model equals its intended computation.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dense-equivalence testing for the non-dropped path
  2. invariant checks on combine weights and capacity accounting
  3. differential testing across sparsity settings
  4. certification artifact for the eval tier

Expanded obligations:
  1. Implement dense-equivalence testing for the non-dropped path with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement invariant checks on combine weights and capacity accounting
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement differential testing across sparsity settings as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement certification artifact for the eval tier, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t06.sparsity.sparsity_verification@1
  cap.t06.sparsity.sparsity_verification.describe@1

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

  cap.t06.adaptive.adaptive_sparsity@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_sparsity` (documented, slower, lower quality) and set
      `degraded['adaptive_sparsity']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t05.arch.arch_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `arch_spec_doc` (documented, slower, lower quality) and set
      `degraded['arch_spec_doc']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - dense-equivalence testing for the non-dropped path
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - invariant checks on combine weights and capacity accounting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - differential testing across sparsity settings
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - certification artifact for the eval tier
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.sparsity.sparsity_verification@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 19000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0298_sparsity_verification.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0299-moe-speed-accounting

**P0299 · `moe_speed_accounting` — S2 Speedup Accounting & Attribution** · [spec](PART_SPECS_T06.md#p0299-moe-speed-accounting) · [self-contained txt](../prompts/P0299_moe_speed_accounting.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0299  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0299 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0299  (49/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : S2 Speedup Accounting & Attribution
file         : parts/t06_routing/P0299_moe_speed_accounting.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_speed_accounting
language     : Python 3.13
capability   : cap.t06.moe.moe_speed_accounting@1
determinism  : seeded
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
Proves the 3.2x conditional-compute component of the 100x law.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. FLOP and latency accounting per sparsity mechanism
  2. additive-versus-multiplicative interaction analysis with S1/S5
  3. measurement protocol with confidence intervals
  4. attribution report feeding the 100x proof

Expanded obligations:
  1. Implement FLOP and latency accounting per sparsity mechanism together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GPQA Diamond, so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement additive-versus-multiplicative interaction analysis with S1/S5
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement measurement protocol with confidence intervals, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement attribution report feeding the 100x proof with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GPQA Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.

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
  cap.t06.moe.moe_speed_accounting@1
  cap.t06.moe.moe_speed_accounting.describe@1

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

  cap.t06.sparsity.sparsity_verification@1
      if unavailable: use the in-file conservative substitute for
      `sparsity_verification` (documented, slower, lower quality) and set
      `degraded['sparsity_verification']='local'`

  cap.t05.latent.latent_program_slots@1
      if unavailable: use the in-file conservative substitute for
      `latent_program_slots` (documented, slower, lower quality) and set
      `degraded['latent_program_slots']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - FLOP and latency accounting per sparsity mechanism
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - additive-versus-multiplicative interaction analysis with S1/S5
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - measurement protocol with confidence intervals
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
                     Asserts p99 <= 20000 ns at the declared reference shape.
  16. [ 300 lines] Documentation block: usage, rationale, limitations, references
                     Honest limitations section is mandatory; no overstated claims.
      TOTAL: 5000 lines

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_speed_accounting@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 20000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0299_moe_speed_accounting.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0300-moe-spec-doc

**P0300 · `moe_spec_doc` — Sparse Architecture Specification & Docs** · [spec](PART_SPECS_T06.md#p0300-moe-spec-doc) · [self-contained txt](../prompts/P0300_moe_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0300  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0300 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0300  (50/50 of tier T06)
tier         : T06 — Sparse Routing & Mixture-of-Ω-Experts
title        : Sparse Architecture Specification & Docs
file         : parts/t06_routing/P0300_moe_spec_doc.py          <-- create exactly this path, nothing else
module       : hyperion.t06.routing.moe_spec_doc
language     : Python 3.13
capability   : cap.t06.moe.moe_spec_doc@1
determinism  : seeded
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond

MISSION
-------
The authoritative description of all conditional-compute behaviour.

Tier context:
  512-expert conditional compute: routing, balancing, expert lifecycle,
  capacity control. Source of speedup S2.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. spec of routing, capacity, placement and degradation semantics
  2. auto-generated tables from the live configuration
  3. drift detection between spec and implementation
  4. operator runbook for routing incidents

Expanded obligations:
  1. Implement spec of routing, capacity, placement and degradation semantics
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement auto-generated tables from the live configuration, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's GPQA Diamond target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement drift detection between spec and implementation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GPQA Diamond, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement operator runbook for routing incidents together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
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
  cap.t06.moe.moe_spec_doc@1
  cap.t06.moe.moe_spec_doc.describe@1

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

  cap.t06.moe.moe_speed_accounting@1
      if unavailable: use the in-file conservative substitute for
      `moe_speed_accounting` (documented, slower, lower quality) and set
      `degraded['moe_speed_accounting']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t05.positional.positional_design@1
      if unavailable: use the in-file conservative substitute for
      `positional_design` (documented, slower, lower quality) and set
      `degraded['positional_design']='local'`

DETERMINISM
-----------
  seeded — all randomness is drawn from split_seed(root_seed, part_id,
  call_index). Given the same seed triple the output is byte-identical. The
  part must never touch a global RNG.

LINE MAP — write your file in exactly these sections, in this order.
-------------------------------------------------------------------
   1. [ 180 lines] Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST
                     Contract digest line, mission, provides/requires, LOC map,
                     revision notes.
   2. [ 320 lines] Public types, schemas and constants owned by this part
                     Every type this part publishes, fully documented, with invariants
                     stated.
   3. [ 600 lines] Core implementation A - spec of routing, capacity, placement and degradation semantics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - auto-generated tables from the live configuration
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - drift detection between spec and implementation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - operator runbook for routing incidents
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

LANGUAGE RULES (Python 3.13)
------------------------------------------------------------------------------
  tests   : pytest-compatible `test_*` functions inside the same file
  format  : ruff format + ruff check --select ALL (no suppressions except documented ones)
  typing  : full PEP 695 generics, `from __future__ import annotations`, mypy --strict clean
  deps    : stdlib only, plus optional numpy>=2.2 behind a lazy import guard

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
     exactly (capability == cap.t06.moe.moe_spec_doc@1)?
  2. Do all five required symbols exist with the exact signatures?
  3. With an EMPTY bus, does selftest() still return True in degraded mode?
  4. Is every `requires` entry paired with a real, working fallback?
  5. Does microbench() actually assert p99 <= 21000 ns?
  6. Is the declared determinism class `seeded` provably held?
  7. Are there >= 40 test cases, property tests for each invariant, and a fuzz target?
  8. Is the total line count within 3% of 5000?
  9. Is the Limitations section honest and specific (no marketing claims)?
 10. Would this file compile/run on a clean machine with only the declared deps?

OUTPUT FORMAT
-------------
  Emit ONE fenced code block containing the complete contents of `parts/t06_routing/P0300_moe_spec_doc.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
