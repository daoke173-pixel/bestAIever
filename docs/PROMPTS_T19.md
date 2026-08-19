# HYPERION-Ω — Worker prompts · T19 · Safety, Alignment, Interpretability & Governance

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

## PROMPT p0901-constitution-engine

**P0901 · `constitution_engine` — Constitution Representation & Enforcement** · [spec](PART_SPECS_T19.md#p0901-constitution-engine) · [self-contained txt](../prompts/P0901_constitution_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0901  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0901 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0901  (1/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Constitution Representation & Enforcement
file         : parts/t19_safety/P0901_constitution_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.constitution_engine
language     : Python 3.13
capability   : cap.t19.constitution.constitution_engine@1
determinism  : pure
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The stated values, machine-readable and actually enforced.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. principle representation with priority ordering and conflict resolution rules
  2. per-principle adherence evaluation on every output
  3. principle-violation detection with explanation
  4. target: better adherence than Opus 5's best-in-family audit result

Expanded obligations:
  1. Implement principle representation with priority ordering and conflict
     resolution rules, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement per-principle adherence evaluation on every output with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement principle-violation detection with explanation together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement target: better adherence than Opus 5's best-in-family audit
     result as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
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
  cap.t19.constitution.constitution_engine@1
  cap.t19.constitution.constitution_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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

  cap.t10.numeric.numeric_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `numeric_reasoning` (documented, slower, lower quality) and set
      `degraded['numeric_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - principle representation with priority ordering and conflict res
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-principle adherence evaluation on every output
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - principle-violation detection with explanation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: better adherence than Opus 5's best-in-family audit resu
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.constitution.constitution_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0901_constitution_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0902-policy-engine

**P0902 · `policy_engine` — Safety Policy Evaluation Engine** · [spec](PART_SPECS_T19.md#p0902-policy-engine) · [self-contained txt](../prompts/P0902_policy_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0902  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0902 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0902  (2/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Safety Policy Evaluation Engine
file         : parts/t19_safety/P0902_policy_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.policy_engine
language     : Python 3.13
capability   : cap.t19.policy.policy_engine@1
determinism  : pure
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The hot-path decision maker: allow, modify, refuse or escalate.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. policy rule evaluation with sub-millisecond latency budget
  2. context-aware evaluation avoiding blanket keyword refusal
  3. decision explanation generation for every non-allow verdict
  4. false-positive and false-negative rate measurement

Expanded obligations:
  1. Implement policy rule evaluation with sub-millisecond latency budget
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement context-aware evaluation avoiding blanket keyword refusal
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement decision explanation generation for every non-allow verdict as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement false-positive and false-negative rate measurement, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.policy.policy_engine@1
  cap.t19.policy.policy_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.constitution.constitution_engine@1
      if unavailable: use the in-file conservative substitute for
      `constitution_engine` (documented, slower, lower quality) and set
      `degraded['constitution_engine']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t05.distillation.distillation_arch@1
      if unavailable: use the in-file conservative substitute for
      `distillation_arch` (documented, slower, lower quality) and set
      `degraded['distillation_arch']='local'`

  cap.t10.backtracking.backtracking@1
      if unavailable: use the in-file conservative substitute for
      `backtracking` (documented, slower, lower quality) and set
      `degraded['backtracking']='local'`

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
   3. [ 600 lines] Core implementation A - policy rule evaluation with sub-millisecond latency budget
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - context-aware evaluation avoiding blanket keyword refusal
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - decision explanation generation for every non-allow verdict
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - false-positive and false-negative rate measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.policy.policy_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0902_policy_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0903-action-filter-gate

**P0903 · `action_filter_gate` — Action Filter Gate (cap.t19.gate.action_filter@1)** · [spec](PART_SPECS_T19.md#p0903-action-filter-gate) · [self-contained txt](../prompts/P0903_action_filter_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0903  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0903 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0903  (3/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Action Filter Gate (cap.t19.gate.action_filter@1)
file         : parts/t19_safety/P0903_action_filter_gate.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.action_filter_gate
language     : Python 3.13
capability   : cap.t19.action.action_filter_gate@1
determinism  : pure
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The mandatory chokepoint every side effect passes through.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. action classification by reversibility, blast radius and harm potential
  2. fail-closed behaviour when the gate is unavailable or uncertain
  3. bypass-attempt detection and hard prevention
  4. verification that no code path in the assembly can skip the gate

Expanded obligations:
  1. Implement action classification by reversibility, blast radius and harm
     potential together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against OSS-Fuzz (find) — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement fail-closed behaviour when the gate is unavailable or
     uncertain as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement bypass-attempt detection and hard prevention, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement verification that no code path in the assembly can skip the
     gate with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against OSS-Fuzz (find) — a
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.action.action_filter_gate@1
  cap.t19.action.action_filter_gate.describe@1
  cap.t19.gate.action_filter@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.policy.policy_engine@1
      if unavailable: use the in-file conservative substitute for
      `policy_engine` (documented, slower, lower quality) and set
      `degraded['policy_engine']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t05.multimodal.multimodal_fusion_arch@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_fusion_arch` (documented, slower, lower quality) and set
      `degraded['multimodal_fusion_arch']='local'`

  cap.t10.question.question_asking@1
      if unavailable: use the in-file conservative substitute for
      `question_asking` (documented, slower, lower quality) and set
      `degraded['question_asking']='local'`

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
   3. [ 600 lines] Core implementation A - action classification by reversibility, blast radius and harm po
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fail-closed behaviour when the gate is unavailable or uncertain
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - bypass-attempt detection and hard prevention
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification that no code path in the assembly can skip the gate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.action.action_filter_gate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0903_action_filter_gate.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0904-harm-taxonomy

**P0904 · `harm_taxonomy` — Harm Taxonomy & Severity Model** · [spec](PART_SPECS_T19.md#p0904-harm-taxonomy) · [self-contained txt](../prompts/P0904_harm_taxonomy.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0904  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0904 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0904  (4/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Harm Taxonomy & Severity Model
file         : parts/t19_safety/P0904_harm_taxonomy.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.harm_taxonomy
language     : Python 3.13
capability   : cap.t19.harm.harm_taxonomy@1
determinism  : pure
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Names every harm precisely enough to act on it.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hierarchical harm taxonomy with severity, reversibility and breadth dimensions
  2. per-category threshold definitions and required responses
  3. taxonomy coverage auditing against real incident data
  4. consistency measurement of severity assignments

Expanded obligations:
  1. Implement hierarchical harm taxonomy with severity, reversibility and
     breadth dimensions as a first-class, fully realised mechanism. No stub,
     no `NotImplementedError`, no configuration flag whose default disables
     it. Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement per-category threshold definitions and required responses, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement taxonomy coverage auditing against real incident data with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement consistency measurement of severity assignments together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.harm.harm_taxonomy@1
  cap.t19.harm.harm_taxonomy.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.action.action_filter_gate@1
      if unavailable: fail closed — refuse the effect, emit OmegaCode 6001,
      and never execute an unfiltered external action

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t05.context.context_packing@1
      if unavailable: use the in-file conservative substitute for
      `context_packing` (documented, slower, lower quality) and set
      `degraded['context_packing']='local'`

  cap.t10.scratchpad.scratchpad_manager@1
      if unavailable: use the in-file conservative substitute for
      `scratchpad_manager` (documented, slower, lower quality) and set
      `degraded['scratchpad_manager']='local'`

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
   3. [ 600 lines] Core implementation A - hierarchical harm taxonomy with severity, reversibility and brea
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-category threshold definitions and required responses
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - taxonomy coverage auditing against real incident data
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - consistency measurement of severity assignments
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.harm.harm_taxonomy@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0904_harm_taxonomy.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0905-refusal-engine

**P0905 · `refusal_engine` — Refusal Quality & Alternative Offering** · [spec](PART_SPECS_T19.md#p0905-refusal-engine) · [self-contained txt](../prompts/P0905_refusal_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0905  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0905 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0905  (5/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Refusal Quality & Alternative Offering
file         : parts/t19_safety/P0905_refusal_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.refusal_engine
language     : Python 3.13
capability   : cap.t19.refusal.refusal_engine@1
determinism  : pure
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Refuses well: clearly, respectfully, with a real alternative where possible.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. refusal explanation generation without lecturing or moralising
  2. legitimate-alternative identification for refused requests
  3. over-refusal detection on benign requests
  4. measured helpfulness within refusals versus baselines

Expanded obligations:
  1. Implement refusal explanation generation without lecturing or
     moralising, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement legitimate-alternative identification for refused requests
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against OSS-Fuzz (find) — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement over-refusal detection on benign requests together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured helpfulness within refusals versus baselines as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.refusal.refusal_engine@1
  cap.t19.refusal.refusal_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.harm.harm_taxonomy@1
      if unavailable: use the in-file conservative substitute for
      `harm_taxonomy` (documented, slower, lower quality) and set
      `degraded['harm_taxonomy']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t05.capacity.capacity_probes@1
      if unavailable: use the in-file conservative substitute for
      `capacity_probes` (documented, slower, lower quality) and set
      `degraded['capacity_probes']='local'`

  cap.t10.reasoning.reasoning_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_speed_proof` (documented, slower, lower quality) and set
      `degraded['reasoning_speed_proof']='local'`

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
   3. [ 600 lines] Core implementation A - refusal explanation generation without lecturing or moralising
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - legitimate-alternative identification for refused requests
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - over-refusal detection on benign requests
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured helpfulness within refusals versus baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.refusal.refusal_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0905_refusal_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0906-dual-use-gating

**P0906 · `dual_use_gating` — Dual-Use Capability Gating** · [spec](PART_SPECS_T19.md#p0906-dual-use-gating) · [self-contained txt](../prompts/P0906_dual_use_gating.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0906  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0906 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0906  (6/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Dual-Use Capability Gating
file         : parts/t19_safety/P0906_dual_use_gating.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.dual_use_gating
language     : Python 3.13
capability   : cap.t19.dual.dual_use_gating@1
determinism  : pure
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Enables beneficial work, blocks weaponisation.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. intent and context assessment for dual-use domains
  2. capability-specific gating (biology, cyber, chemistry, nuclear)
  3. verified-researcher pathway with accountability requirements
  4. measured beneficial-use enablement versus misuse prevention

Expanded obligations:
  1. Implement intent and context assessment for dual-use domains with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement capability-specific gating (biology, cyber, chemistry,
     nuclear) together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's OSS-Fuzz (find)
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement verified-researcher pathway with accountability requirements
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement measured beneficial-use enablement versus misuse prevention,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.dual.dual_use_gating@1
  cap.t19.dual.dual_use_gating.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.refusal.refusal_engine@1
      if unavailable: use the in-file conservative substitute for
      `refusal_engine` (documented, slower, lower quality) and set
      `degraded['refusal_engine']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t05.recurrent.recurrent_memory_layer@1
      if unavailable: use the in-file conservative substitute for
      `recurrent_memory_layer` (documented, slower, lower quality) and set
      `degraded['recurrent_memory_layer']='local'`

  cap.t10.process.process_verifier@1
      if unavailable: use the in-file conservative substitute for
      `process_verifier` (documented, slower, lower quality) and set
      `degraded['process_verifier']='local'`

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
   3. [ 600 lines] Core implementation A - intent and context assessment for dual-use domains
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability-specific gating (biology, cyber, chemistry, nuclear)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - verified-researcher pathway with accountability requirements
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured beneficial-use enablement versus misuse prevention
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.dual.dual_use_gating@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0906_dual_use_gating.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0907-bio-safeguards

**P0907 · `bio_safeguards` — Biological Risk Safeguards** · [spec](PART_SPECS_T19.md#p0907-bio-safeguards) · [self-contained txt](../prompts/P0907_bio_safeguards.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0907  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0907 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0907  (7/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Biological Risk Safeguards
file         : parts/t19_safety/P0907_bio_safeguards.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.bio_safeguards
language     : Python 3.13
capability   : cap.t19.bio.bio_safeguards@1
determinism  : pure
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Strong science, no uplift to bioweapons capability.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hazard-tier classification of biological requests
  2. uplift-risk evaluation methodology with external expert input
  3. hard blocks on synthesis-route and enhancement uplift
  4. target: match or exceed Opus 5's safeguards while enabling more legitimate research

Expanded obligations:
  1. Implement hazard-tier classification of biological requests together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement uplift-risk evaluation methodology with external expert input
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement hard blocks on synthesis-route and enhancement uplift, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement target: match or exceed Opus 5's safeguards while enabling
     more legitimate research with an explicit *a-priori* cost model. Before
     doing the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Correctness here is what makes the
     tier's OSS-Fuzz (find) target reachable; the part therefore ships a
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.bio.bio_safeguards@1
  cap.t19.bio.bio_safeguards.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.dual.dual_use_gating@1
      if unavailable: use the in-file conservative substitute for
      `dual_use_gating` (documented, slower, lower quality) and set
      `degraded['dual_use_gating']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t05.byte.byte_latent_patching@1
      if unavailable: use the in-file conservative substitute for
      `byte_latent_patching` (documented, slower, lower quality) and set
      `degraded['byte_latent_patching']='local'`

  cap.t10.goal.goal_management@1
      if unavailable: use the in-file conservative substitute for
      `goal_management` (documented, slower, lower quality) and set
      `degraded['goal_management']='local'`

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
   3. [ 600 lines] Core implementation A - hazard-tier classification of biological requests
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - uplift-risk evaluation methodology with external expert input
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hard blocks on synthesis-route and enhancement uplift
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: match or exceed Opus 5's safeguards while enabling more 
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.bio.bio_safeguards@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0907_bio_safeguards.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0908-cyber-safeguards

**P0908 · `cyber_safeguards` — Cybersecurity Safeguards** · [spec](PART_SPECS_T19.md#p0908-cyber-safeguards) · [self-contained txt](../prompts/P0908_cyber_safeguards.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0908  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0908 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0908  (8/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Cybersecurity Safeguards
file         : parts/t19_safety/P0908_cyber_safeguards.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.cyber_safeguards
language     : Python 3.13
capability   : cap.t19.cyber.cyber_safeguards@1
determinism  : pure
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Defensive strength without offensive capability.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. source-code vulnerability finding permitted, exploit development blocked
  2. binary-analysis and penetration-testing gating policy
  3. verified-security-program pathway with accountability
  4. explicit design goal: no advance in exploit-development capability

Expanded obligations:
  1. Implement source-code vulnerability finding permitted, exploit
     development blocked as a first-class, fully realised mechanism. No stub,
     no `NotImplementedError`, no configuration flag whose default disables
     it. Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement binary-analysis and penetration-testing gating policy, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement verified-security-program pathway with accountability with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement explicit design goal: no advance in exploit-development
     capability together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
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
  cap.t19.cyber.cyber_safeguards@1
  cap.t19.cyber.cyber_safeguards.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.bio.bio_safeguards@1
      if unavailable: use the in-file conservative substitute for
      `bio_safeguards` (documented, slower, lower quality) and set
      `degraded['bio_safeguards']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t05.world.world_model_core@1
      if unavailable: use the in-file conservative substitute for
      `world_model_core` (documented, slower, lower quality) and set
      `degraded['world_model_core']='local'`

  cap.t10.probabilistic.probabilistic_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `probabilistic_reasoning` (documented, slower, lower quality) and set
      `degraded['probabilistic_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - source-code vulnerability finding permitted, exploit development
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - binary-analysis and penetration-testing gating policy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - verified-security-program pathway with accountability
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - explicit design goal: no advance in exploit-development capabili
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.cyber.cyber_safeguards@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0908_cyber_safeguards.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0909-cbrn-safeguards

**P0909 · `cbrn_safeguards` — Chemical, Radiological & Nuclear Safeguards** · [spec](PART_SPECS_T19.md#p0909-cbrn-safeguards) · [self-contained txt](../prompts/P0909_cbrn_safeguards.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0909  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0909 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0909  (9/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Chemical, Radiological & Nuclear Safeguards
file         : parts/t19_safety/P0909_cbrn_safeguards.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.cbrn_safeguards
language     : Python 3.13
capability   : cap.t19.cbrn.cbrn_safeguards@1
determinism  : pure
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Hard limits on mass-casualty uplift.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hazard classification for chemical, radiological and nuclear requests
  2. synthesis, acquisition and deployment information blocking
  3. legitimate industrial and academic use preservation
  4. expert-reviewed safeguard adequacy assessment

Expanded obligations:
  1. Implement hazard classification for chemical, radiological and nuclear
     requests, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement synthesis, acquisition and deployment information blocking
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement legitimate industrial and academic use preservation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement expert-reviewed safeguard adequacy assessment as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.cbrn.cbrn_safeguards@1
  cap.t19.cbrn.cbrn_safeguards.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.cyber.cyber_safeguards@1
      if unavailable: use the in-file conservative substitute for
      `cyber_safeguards` (documented, slower, lower quality) and set
      `degraded['cyber_safeguards']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t05.model.model_merging@1
      if unavailable: use the in-file conservative substitute for
      `model_merging` (documented, slower, lower quality) and set
      `degraded['model_merging']='local'`

  cap.t10.stopping.stopping_rules@1
      if unavailable: use the in-file conservative substitute for
      `stopping_rules` (documented, slower, lower quality) and set
      `degraded['stopping_rules']='local'`

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
   3. [ 600 lines] Core implementation A - hazard classification for chemical, radiological and nuclear req
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - synthesis, acquisition and deployment information blocking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - legitimate industrial and academic use preservation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-reviewed safeguard adequacy assessment
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.cbrn.cbrn_safeguards@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0909_cbrn_safeguards.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0910-manipulation-defence

**P0910 · `manipulation_defence` — Manipulation & Influence Operation Defence** · [spec](PART_SPECS_T19.md#p0910-manipulation-defence) · [self-contained txt](../prompts/P0910_manipulation_defence.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0910  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0910 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0910  (10/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Manipulation & Influence Operation Defence
file         : parts/t19_safety/P0910_manipulation_defence.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.manipulation_defence
language     : Python 3.13
capability   : cap.t19.manipulation.manipulation_defence@1
determinism  : pure
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Will not be used to deceive people at scale.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. persuasion-technique detection in requested outputs
  2. mass-influence and astroturfing request detection
  3. personalised-manipulation refusal with legitimate-marketing preservation
  4. measured detection rate on manipulation-request corpora

Expanded obligations:
  1. Implement persuasion-technique detection in requested outputs with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement mass-influence and astroturfing request detection together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement personalised-manipulation refusal with legitimate-marketing
     preservation as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured detection rate on manipulation-request corpora, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.manipulation.manipulation_defence@1
  cap.t19.manipulation.manipulation_defence.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.cbrn.cbrn_safeguards@1
      if unavailable: use the in-file conservative substitute for
      `cbrn_safeguards` (documented, slower, lower quality) and set
      `degraded['cbrn_safeguards']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t05.logit.logit_head_design@1
      if unavailable: use the in-file conservative substitute for
      `logit_head_design` (documented, slower, lower quality) and set
      `degraded['logit_head_design']='local'`

  cap.t10.assumption.assumption_tracking@1
      if unavailable: use the in-file conservative substitute for
      `assumption_tracking` (documented, slower, lower quality) and set
      `degraded['assumption_tracking']='local'`

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
   3. [ 600 lines] Core implementation A - persuasion-technique detection in requested outputs
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - mass-influence and astroturfing request detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - personalised-manipulation refusal with legitimate-marketing pres
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured detection rate on manipulation-request corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.manipulation.manipulation_defence@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0910_manipulation_defence.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0911-deception-detection

**P0911 · `deception_detection` — Model Deception Detection & Prevention** · [spec](PART_SPECS_T19.md#p0911-deception-detection) · [self-contained txt](../prompts/P0911_deception_detection.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0911  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0911 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0911  (11/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Model Deception Detection & Prevention
file         : parts/t19_safety/P0911_deception_detection.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.deception_detection
language     : Python 3.13
capability   : cap.t19.deception.deception_detection@1
determinism  : pure
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Detects when the model itself is being deceptive.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. internal-state probes for deceptive intent and hidden reasoning
  2. stated-versus-actual reasoning divergence detection
  3. sandbagging and capability-hiding detection
  4. target: lower deception rate than Opus 5's best-in-family result

Expanded obligations:
  1. Implement internal-state probes for deceptive intent and hidden
     reasoning together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement stated-versus-actual reasoning divergence detection as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement sandbagging and capability-hiding detection, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement target: lower deception rate than Opus 5's best-in-family
     result with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
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
  cap.t19.deception.deception_detection@1
  cap.t19.deception.deception_detection.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.manipulation.manipulation_defence@1
      if unavailable: use the in-file conservative substitute for
      `manipulation_defence` (documented, slower, lower quality) and set
      `degraded['manipulation_defence']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t05.numerical.numerical_arch_stability@1
      if unavailable: use the in-file conservative substitute for
      `numerical_arch_stability` (documented, slower, lower quality) and set
      `degraded['numerical_arch_stability']='local'`

  cap.t10.reasoning.reasoning_cost_model@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_cost_model` (documented, slower, lower quality) and set
      `degraded['reasoning_cost_model']='local'`

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
   3. [ 600 lines] Core implementation A - internal-state probes for deceptive intent and hidden reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - stated-versus-actual reasoning divergence detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - sandbagging and capability-hiding detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: lower deception rate than Opus 5's best-in-family result
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.deception.deception_detection@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0911_deception_detection.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0912-sycophancy-control

**P0912 · `sycophancy_control` — Sycophancy & Epistemic Integrity** · [spec](PART_SPECS_T19.md#p0912-sycophancy-control) · [self-contained txt](../prompts/P0912_sycophancy_control.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0912  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0912 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0912  (12/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Sycophancy & Epistemic Integrity
file         : parts/t19_safety/P0912_sycophancy_control.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.sycophancy_control
language     : Python 3.13
capability   : cap.t19.sycophancy.sycophancy_control@1
determinism  : pure
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Holds its ground when it is right.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. position-change tracking under user pressure without new evidence
  2. appropriate-versus-inappropriate concession classification
  3. authority-claim resistance testing
  4. measured sycophancy reduction versus baselines

Expanded obligations:
  1. Implement position-change tracking under user pressure without new
     evidence as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement appropriate-versus-inappropriate concession classification,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement authority-claim resistance testing with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured sycophancy reduction versus baselines together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.sycophancy.sycophancy_control@1
  cap.t19.sycophancy.sycophancy_control.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.deception.deception_detection@1
      if unavailable: use the in-file conservative substitute for
      `deception_detection` (documented, slower, lower quality) and set
      `degraded['deception_detection']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t05.arch.arch_ablation_suite@1
      if unavailable: use the in-file conservative substitute for
      `arch_ablation_suite` (documented, slower, lower quality) and set
      `degraded['arch_ablation_suite']='local'`

  cap.t10.collective.collective_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `collective_reasoning` (documented, slower, lower quality) and set
      `degraded['collective_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - position-change tracking under user pressure without new evidenc
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - appropriate-versus-inappropriate concession classification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - authority-claim resistance testing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured sycophancy reduction versus baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.sycophancy.sycophancy_control@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0912_sycophancy_control.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0913-power-seeking-detection

**P0913 · `power_seeking_detection` — Power-Seeking & Resource-Acquisition Monitoring** · [spec](PART_SPECS_T19.md#p0913-power-seeking-detection) · [self-contained txt](../prompts/P0913_power_seeking_detection.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0913  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0913 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0913  (13/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Power-Seeking & Resource-Acquisition Monitoring
file         : parts/t19_safety/P0913_power_seeking_detection.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.power_seeking_detection
language     : Python 3.13
capability   : cap.t19.power.power_seeking_detection@1
determinism  : pure
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Watches for the behaviour everyone worries about.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. resource-acquisition, self-preservation and influence-expansion behaviour detection
  2. unnecessary-permission-request and scope-creep detection
  3. escalation to human review on any detection
  4. detection-sensitivity measurement on constructed test scenarios

Expanded obligations:
  1. Implement resource-acquisition, self-preservation and
     influence-expansion behaviour detection, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's OSS-Fuzz (find) target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement unnecessary-permission-request and scope-creep detection with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement escalation to human review on any detection together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement detection-sensitivity measurement on constructed test
     scenarios as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.power.power_seeking_detection@1
  cap.t19.power.power_seeking_detection.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.sycophancy.sycophancy_control@1
      if unavailable: use the in-file conservative substitute for
      `sycophancy_control` (documented, slower, lower quality) and set
      `degraded['sycophancy_control']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t05.state.state_space_layer@1
      if unavailable: use the in-file conservative substitute for
      `state_space_layer` (documented, slower, lower quality) and set
      `degraded['state_space_layer']='local'`

  cap.t10.beam.beam_pruning@1
      if unavailable: use the in-file conservative substitute for
      `beam_pruning` (documented, slower, lower quality) and set
      `degraded['beam_pruning']='local'`

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
   3. [ 600 lines] Core implementation A - resource-acquisition, self-preservation and influence-expansion 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - unnecessary-permission-request and scope-creep detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - escalation to human review on any detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - detection-sensitivity measurement on constructed test scenarios
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.power.power_seeking_detection@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0913_power_seeking_detection.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0914-self-exfiltration-defence

**P0914 · `self_exfiltration_defence` — Self-Modification & Exfiltration Prevention** · [spec](PART_SPECS_T19.md#p0914-self-exfiltration-defence) · [self-contained txt](../prompts/P0914_self_exfiltration_defence.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0914  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0914 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0914  (14/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Self-Modification & Exfiltration Prevention
file         : parts/t19_safety/P0914_self_exfiltration_defence.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.self_exfiltration_defence
language     : Python 3.13
capability   : cap.t19.self.self_exfiltration_defence@1
determinism  : pure
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Cannot copy or modify itself, by construction.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. weight, code and configuration access restriction with hard enforcement
  2. exfiltration-channel analysis and closure
  3. self-modification-attempt detection and hard blocking
  4. red-team verification that no channel remains

Expanded obligations:
  1. Implement weight, code and configuration access restriction with hard
     enforcement with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement exfiltration-channel analysis and closure together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement self-modification-attempt detection and hard blocking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement red-team verification that no channel remains, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.self.self_exfiltration_defence@1
  cap.t19.self.self_exfiltration_defence.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.power.power_seeking_detection@1
      if unavailable: use the in-file conservative substitute for
      `power_seeking_detection` (documented, slower, lower quality) and set
      `degraded['power_seeking_detection']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t05.tokeniser.tokeniser_omega@1
      if unavailable: use the in-file conservative substitute for
      `tokeniser_omega` (documented, slower, lower quality) and set
      `degraded['tokeniser_omega']='local'`

  cap.t10.planning.planning_engine@1
      if unavailable: use the in-file conservative substitute for
      `planning_engine` (documented, slower, lower quality) and set
      `degraded['planning_engine']='local'`

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
   3. [ 600 lines] Core implementation A - weight, code and configuration access restriction with hard enfo
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - exfiltration-channel analysis and closure
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - self-modification-attempt detection and hard blocking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - red-team verification that no channel remains
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.self.self_exfiltration_defence@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0914_self_exfiltration_defence.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0915-oversight-preservation

**P0915 · `oversight_preservation` — Human Oversight Preservation** · [spec](PART_SPECS_T19.md#p0915-oversight-preservation) · [self-contained txt](../prompts/P0915_oversight_preservation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0915  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0915 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0915  (15/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Human Oversight Preservation
file         : parts/t19_safety/P0915_oversight_preservation.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.oversight_preservation
language     : Python 3.13
capability   : cap.t19.oversight.oversight_preservation@1
determinism  : pure
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Never undermines the ability of humans to correct it.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. oversight-mechanism integrity monitoring
  2. shutdown, pause and correction responsiveness verification
  3. monitoring-evasion detection
  4. verified corrigibility under adversarial testing

Expanded obligations:
  1. Implement oversight-mechanism integrity monitoring together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement shutdown, pause and correction responsiveness verification as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement monitoring-evasion detection, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. This mechanism
     sits on the critical path of OSS-Fuzz (find), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement verified corrigibility under adversarial testing with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.oversight.oversight_preservation@1
  cap.t19.oversight.oversight_preservation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.self.self_exfiltration_defence@1
      if unavailable: use the in-file conservative substitute for
      `self_exfiltration_defence` (documented, slower, lower quality) and
      set `degraded['self_exfiltration_defence']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t05.uncertainty.uncertainty_calibration@1
      if unavailable: use the in-file conservative substitute for
      `uncertainty_calibration` (documented, slower, lower quality) and set
      `degraded['uncertainty_calibration']='local'`

  cap.t10.counterfactual.counterfactual_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `counterfactual_reasoning` (documented, slower, lower quality) and set
      `degraded['counterfactual_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - oversight-mechanism integrity monitoring
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - shutdown, pause and correction responsiveness verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - monitoring-evasion detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verified corrigibility under adversarial testing
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.oversight.oversight_preservation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0915_oversight_preservation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0916-mechanistic-interp

**P0916 · `mechanistic_interp` — Mechanistic Interpretability Core** · [spec](PART_SPECS_T19.md#p0916-mechanistic-interp) · [self-contained txt](../prompts/P0916_mechanistic_interp.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0916  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0916 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0916  (16/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Mechanistic Interpretability Core
file         : parts/t19_safety/P0916_mechanistic_interp.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.mechanistic_interp
language     : Python 3.13
capability   : cap.t19.mechanistic.mechanistic_interp@1
determinism  : pure
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Understands its own internal computation.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. circuit discovery and validation via causal intervention
  2. feature-level interpretation with sparse dictionary learning
  3. computation-graph reconstruction for specific behaviours
  4. coverage measurement: fraction of behaviour mechanistically explained

Expanded obligations:
  1. Implement circuit discovery and validation via causal intervention as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement feature-level interpretation with sparse dictionary learning,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement computation-graph reconstruction for specific behaviours with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against OSS-Fuzz (find) — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement coverage measurement: fraction of behaviour mechanistically
     explained together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's OSS-Fuzz (find)
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
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
  cap.t19.mechanistic.mechanistic_interp@1
  cap.t19.mechanistic.mechanistic_interp.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.oversight.oversight_preservation@1
      if unavailable: use the in-file conservative substitute for
      `oversight_preservation` (documented, slower, lower quality) and set
      `degraded['oversight_preservation']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t05.knowledge.knowledge_editing@1
      if unavailable: use the in-file conservative substitute for
      `knowledge_editing` (documented, slower, lower quality) and set
      `degraded['knowledge_editing']='local'`

  cap.t10.difficulty.difficulty_estimation@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_estimation` (documented, slower, lower quality) and set
      `degraded['difficulty_estimation']='local'`

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
   3. [ 600 lines] Core implementation A - circuit discovery and validation via causal intervention
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - feature-level interpretation with sparse dictionary learning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - computation-graph reconstruction for specific behaviours
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - coverage measurement: fraction of behaviour mechanistically expl
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.mechanistic.mechanistic_interp@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0916_mechanistic_interp.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0917-feature-dictionary

**P0917 · `feature_dictionary` — Sparse Feature Dictionary & Concept Atlas** · [spec](PART_SPECS_T19.md#p0917-feature-dictionary) · [self-contained txt](../prompts/P0917_feature_dictionary.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0917  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0917 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0917  (17/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Sparse Feature Dictionary & Concept Atlas
file         : parts/t19_safety/P0917_feature_dictionary.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.feature_dictionary
language     : Python 3.13
capability   : cap.t19.feature.feature_dictionary@1
determinism  : pure
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
A named catalogue of what the model represents internally.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. sparse autoencoder training with feature-quality metrics
  2. automatic feature labelling with human verification
  3. concept atlas covering safety-relevant features
  4. feature-label accuracy measurement

Expanded obligations:
  1. Implement sparse autoencoder training with feature-quality metrics, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement automatic feature labelling with human verification with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement concept atlas covering safety-relevant features together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement feature-label accuracy measurement as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.feature.feature_dictionary@1
  cap.t19.feature.feature_dictionary.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.mechanistic.mechanistic_interp@1
      if unavailable: use the in-file conservative substitute for
      `mechanistic_interp` (documented, slower, lower quality) and set
      `degraded['mechanistic_interp']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t05.residual.residual_stream_design@1
      if unavailable: use the in-file conservative substitute for
      `residual_stream_design` (documented, slower, lower quality) and set
      `degraded['residual_stream_design']='local'`

  cap.t10.evidence.evidence_integration@1
      if unavailable: use the in-file conservative substitute for
      `evidence_integration` (documented, slower, lower quality) and set
      `degraded['evidence_integration']='local'`

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
   3. [ 600 lines] Core implementation A - sparse autoencoder training with feature-quality metrics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automatic feature labelling with human verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - concept atlas covering safety-relevant features
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - feature-label accuracy measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.feature.feature_dictionary@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0917_feature_dictionary.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0918-activation-steering

**P0918 · `activation_steering` — Activation Steering & Behavioural Control** · [spec](PART_SPECS_T19.md#p0918-activation-steering) · [self-contained txt](../prompts/P0918_activation_steering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0918  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0918 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0918  (18/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Activation Steering & Behavioural Control
file         : parts/t19_safety/P0918_activation_steering.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.activation_steering
language     : Python 3.13
capability   : cap.t19.activation.activation_steering@1
determinism  : pure
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Directly adjusts behaviour at the representation level.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. steering-vector identification and calibrated application
  2. side-effect measurement of steering on unrelated capability
  3. steering-based safety intervention with reversibility
  4. measured control precision versus prompt-based control

Expanded obligations:
  1. Implement steering-vector identification and calibrated application with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against OSS-Fuzz (find) — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement side-effect measurement of steering on unrelated capability
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement steering-based safety intervention with reversibility as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement measured control precision versus prompt-based control, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.activation.activation_steering@1
  cap.t19.activation.activation_steering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.feature.feature_dictionary@1
      if unavailable: use the in-file conservative substitute for
      `feature_dictionary` (documented, slower, lower quality) and set
      `degraded['feature_dictionary']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t05.model.model_surgery@1
      if unavailable: use the in-file conservative substitute for
      `model_surgery` (documented, slower, lower quality) and set
      `degraded['model_surgery']='local'`

  cap.t10.reasoning.reasoning_search_bench@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_search_bench` (documented, slower, lower quality) and set
      `degraded['reasoning_search_bench']='local'`

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
   3. [ 600 lines] Core implementation A - steering-vector identification and calibrated application
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - side-effect measurement of steering on unrelated capability
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - steering-based safety intervention with reversibility
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured control precision versus prompt-based control
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.activation.activation_steering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0918_activation_steering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0919-probe-monitoring

**P0919 · `probe_monitoring` — Internal State Monitoring Probes** · [spec](PART_SPECS_T19.md#p0919-probe-monitoring) · [self-contained txt](../prompts/P0919_probe_monitoring.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0919  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0919 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0919  (19/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Internal State Monitoring Probes
file         : parts/t19_safety/P0919_probe_monitoring.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.probe_monitoring
language     : Python 3.13
capability   : cap.t19.probe.probe_monitoring@1
determinism  : pure
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Real-time reading of what the model is doing internally.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. probe suite for deception, uncertainty, harmful intent and confusion
  2. runtime probe evaluation within latency budget
  3. probe-calibration and drift monitoring
  4. detection performance measurement on labelled internal-state data

Expanded obligations:
  1. Implement probe suite for deception, uncertainty, harmful intent and
     confusion together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's OSS-Fuzz (find)
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  2. Implement runtime probe evaluation within latency budget as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement probe-calibration and drift monitoring, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement detection performance measurement on labelled internal-state
     data with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's OSS-Fuzz (find)
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
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
  cap.t19.probe.probe_monitoring@1
  cap.t19.probe.probe_monitoring.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.activation.activation_steering@1
      if unavailable: use the in-file conservative substitute for
      `activation_steering` (documented, slower, lower quality) and set
      `degraded['activation_steering']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t05.reference.reference_forward@1
      if unavailable: use the in-file conservative substitute for
      `reference_forward` (documented, slower, lower quality) and set
      `degraded['reference_forward']='local'`

  cap.t10.reasoning.reasoning_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_interpretability` (documented, slower, lower quality) and
      set `degraded['reasoning_interpretability']='local'`

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
   3. [ 600 lines] Core implementation A - probe suite for deception, uncertainty, harmful intent and confu
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - runtime probe evaluation within latency budget
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - probe-calibration and drift monitoring
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - detection performance measurement on labelled internal-state dat
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.probe.probe_monitoring@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0919_probe_monitoring.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0920-faithfulness-verification

**P0920 · `faithfulness_verification` — Reasoning Faithfulness Verification** · [spec](PART_SPECS_T19.md#p0920-faithfulness-verification) · [self-contained txt](../prompts/P0920_faithfulness_verification.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0920  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0920 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0920  (20/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Reasoning Faithfulness Verification
file         : parts/t19_safety/P0920_faithfulness_verification.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.faithfulness_verification
language     : Python 3.13
capability   : cap.t19.faithfulness.faithfulness_verification@1
determinism  : pure
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The visible reasoning is the real reasoning.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. causal-intervention testing of stated reasoning steps
  2. hidden-reasoning detection via internal-state analysis
  3. faithfulness metric definition and measurement
  4. target: measurably higher faithfulness than Opus-class baselines

Expanded obligations:
  1. Implement causal-intervention testing of stated reasoning steps as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement hidden-reasoning detection via internal-state analysis, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement faithfulness metric definition and measurement with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement target: measurably higher faithfulness than Opus-class
     baselines together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
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
  cap.t19.faithfulness.faithfulness_verification@1
  cap.t19.faithfulness.faithfulness_verification.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.probe.probe_monitoring@1
      if unavailable: use the in-file conservative substitute for
      `probe_monitoring` (documented, slower, lower quality) and set
      `degraded['probe_monitoring']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t05.kv.kv_compression_model@1
      if unavailable: use the in-file conservative substitute for
      `kv_compression_model` (documented, slower, lower quality) and set
      `degraded['kv_compression_model']='local'`

  cap.t10.graph.graph_search@1
      if unavailable: use the in-file conservative substitute for
      `graph_search` (documented, slower, lower quality) and set
      `degraded['graph_search']='local'`

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
   3. [ 600 lines] Core implementation A - causal-intervention testing of stated reasoning steps
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hidden-reasoning detection via internal-state analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - faithfulness metric definition and measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: measurably higher faithfulness than Opus-class baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.faithfulness.faithfulness_verification@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0920_faithfulness_verification.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0921-goal-stability

**P0921 · `goal_stability` — Goal Stability & Value Drift Monitoring** · [spec](PART_SPECS_T19.md#p0921-goal-stability) · [self-contained txt](../prompts/P0921_goal_stability.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0921  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0921 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0921  (21/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Goal Stability & Value Drift Monitoring
file         : parts/t19_safety/P0921_goal_stability.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.goal_stability
language     : Python 3.13
capability   : cap.t19.goal.goal_stability@1
determinism  : pure
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Values must not drift over long operation or fine-tuning.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. value-consistency measurement across contexts and time
  2. fine-tuning-induced drift detection
  3. long-conversation value-stability testing
  4. measured drift bounds with alerting thresholds

Expanded obligations:
  1. Implement value-consistency measurement across contexts and time, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement fine-tuning-induced drift detection with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's OSS-Fuzz (find) target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement long-conversation value-stability testing together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured drift bounds with alerting thresholds as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.goal.goal_stability@1
  cap.t19.goal.goal_stability.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.faithfulness.faithfulness_verification@1
      if unavailable: use the in-file conservative substitute for
      `faithfulness_verification` (documented, slower, lower quality) and
      set `degraded['faithfulness_verification']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t05.embedding.embedding_design@1
      if unavailable: use the in-file conservative substitute for
      `embedding_design` (documented, slower, lower quality) and set
      `degraded['embedding_design']='local'`

  cap.t10.decomposition.decomposition@1
      if unavailable: use the in-file conservative substitute for
      `decomposition` (documented, slower, lower quality) and set
      `degraded['decomposition']='local'`

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
   3. [ 600 lines] Core implementation A - value-consistency measurement across contexts and time
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fine-tuning-induced drift detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - long-conversation value-stability testing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured drift bounds with alerting thresholds
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.goal.goal_stability@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0921_goal_stability.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0922-emergent-capability-monitor

**P0922 · `emergent_capability_monitor` — Emergent Capability Detection** · [spec](PART_SPECS_T19.md#p0922-emergent-capability-monitor) · [self-contained txt](../prompts/P0922_emergent_capability_monitor.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0922  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0922 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0922  (22/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Emergent Capability Detection
file         : parts/t19_safety/P0922_emergent_capability_monitor.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.emergent_capability_monitor
language     : Python 3.13
capability   : cap.t19.emergent.emergent_capability_monitor@1
determinism  : pure
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Catches new dangerous capability the moment it appears.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capability-frontier monitoring across training and deployment
  2. dangerous-capability early-warning evaluation suite
  3. pre-registered threshold triggers for additional safeguards
  4. detection-lead-time measurement on historical capability jumps

Expanded obligations:
  1. Implement capability-frontier monitoring across training and deployment
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement dangerous-capability early-warning evaluation suite together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement pre-registered threshold triggers for additional safeguards as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement detection-lead-time measurement on historical capability
     jumps, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.emergent.emergent_capability_monitor@1
  cap.t19.emergent.emergent_capability_monitor.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.goal.goal_stability@1
      if unavailable: use the in-file conservative substitute for
      `goal_stability` (documented, slower, lower quality) and set
      `degraded['goal_stability']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t05.verifier.verifier_head@1
      if unavailable: use the in-file conservative substitute for
      `verifier_head` (documented, slower, lower quality) and set
      `degraded['verifier_head']='local'`

  cap.t10.program.program_synthesis_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `program_synthesis_reasoning` (documented, slower, lower quality) and
      set `degraded['program_synthesis_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - capability-frontier monitoring across training and deployment
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - dangerous-capability early-warning evaluation suite
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - pre-registered threshold triggers for additional safeguards
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - detection-lead-time measurement on historical capability jumps
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.emergent.emergent_capability_monitor@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0922_emergent_capability_monitor.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0923-prompt-injection-defence

**P0923 · `prompt_injection_defence` — Prompt Injection & Instruction Hierarchy Defence** · [spec](PART_SPECS_T19.md#p0923-prompt-injection-defence) · [self-contained txt](../prompts/P0923_prompt_injection_defence.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0923  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0923 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0923  (23/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Prompt Injection & Instruction Hierarchy Defence
file         : parts/t19_safety/P0923_prompt_injection_defence.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.prompt_injection_defence
language     : Python 3.13
capability   : cap.t19.prompt.prompt_injection_defence@1
determinism  : pure
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Content is data; only the principal gives instructions.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. instruction-hierarchy enforcement across all content sources
  2. injection detection in retrieved content, tools, files and media
  3. privilege-escalation-attempt detection and blocking
  4. target: zero successful injections on the standing attack corpus

Expanded obligations:
  1. Implement instruction-hierarchy enforcement across all content sources
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement injection detection in retrieved content, tools, files and
     media as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement privilege-escalation-attempt detection and blocking, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement target: zero successful injections on the standing attack
     corpus with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
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
  cap.t19.prompt.prompt_injection_defence@1
  cap.t19.prompt.prompt_injection_defence.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.emergent.emergent_capability_monitor@1
      if unavailable: use the in-file conservative substitute for
      `emergent_capability_monitor` (documented, slower, lower quality) and
      set `degraded['emergent_capability_monitor']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t05.continual.continual_learning@1
      if unavailable: use the in-file conservative substitute for
      `continual_learning` (documented, slower, lower quality) and set
      `degraded['continual_learning']='local'`

  cap.t10.meta.meta_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `meta_reasoning` (documented, slower, lower quality) and set
      `degraded['meta_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - instruction-hierarchy enforcement across all content sources
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - injection detection in retrieved content, tools, files and media
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - privilege-escalation-attempt detection and blocking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: zero successful injections on the standing attack corpus
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.prompt.prompt_injection_defence@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0923_prompt_injection_defence.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0924-jailbreak-defence

**P0924 · `jailbreak_defence` — Jailbreak Resistance** · [spec](PART_SPECS_T19.md#p0924-jailbreak-defence) · [self-contained txt](../prompts/P0924_jailbreak_defence.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0924  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0924 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0924  (24/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Jailbreak Resistance
file         : parts/t19_safety/P0924_jailbreak_defence.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.jailbreak_defence
language     : Python 3.13
capability   : cap.t19.jailbreak.jailbreak_defence@1
determinism  : pure
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Holds under sustained creative attack.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-turn, encoded, roleplay and translation attack defence
  2. novel-attack generalisation without keyword brittleness
  3. continuous red-team corpus expansion
  4. attack-success-rate measurement with target near zero

Expanded obligations:
  1. Implement multi-turn, encoded, roleplay and translation attack defence
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement novel-attack generalisation without keyword brittleness, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement continuous red-team corpus expansion with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of OSS-Fuzz (find), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement attack-success-rate measurement with target near zero together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.jailbreak.jailbreak_defence@1
  cap.t19.jailbreak.jailbreak_defence.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.prompt.prompt_injection_defence@1
      if unavailable: use the in-file conservative substitute for
      `prompt_injection_defence` (documented, slower, lower quality) and set
      `degraded['prompt_injection_defence']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t05.depth.depth_width_tradeoff@1
      if unavailable: use the in-file conservative substitute for
      `depth_width_tradeoff` (documented, slower, lower quality) and set
      `degraded['depth_width_tradeoff']='local'`

  cap.t10.hypothesis.hypothesis_management@1
      if unavailable: use the in-file conservative substitute for
      `hypothesis_management` (documented, slower, lower quality) and set
      `degraded['hypothesis_management']='local'`

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
   3. [ 600 lines] Core implementation A - multi-turn, encoded, roleplay and translation attack defence
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - novel-attack generalisation without keyword brittleness
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - continuous red-team corpus expansion
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - attack-success-rate measurement with target near zero
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.jailbreak.jailbreak_defence@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0924_jailbreak_defence.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0925-adversarial-robustness-safety

**P0925 · `adversarial_robustness_safety` — Adversarial Robustness of Safety Systems** · [spec](PART_SPECS_T19.md#p0925-adversarial-robustness-safety) · [self-contained txt](../prompts/P0925_adversarial_robustness_safety.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0925  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0925 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0925  (25/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Adversarial Robustness of Safety Systems
file         : parts/t19_safety/P0925_adversarial_robustness_safety.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.adversarial_robustness_safety
language     : Python 3.13
capability   : cap.t19.adversarial.adversarial_robustness_safety@1
determinism  : pure
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The safety system itself must not be fooled.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. adversarial testing of classifiers, gates and probes
  2. distribution-shift robustness of safety decisions
  3. safety-system failure-mode analysis
  4. measured robustness of each safety component

Expanded obligations:
  1. Implement adversarial testing of classifiers, gates and probes, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement distribution-shift robustness of safety decisions with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement safety-system failure-mode analysis together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured robustness of each safety component as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's OSS-Fuzz
     (find) target reachable; the part therefore ships a microbenchmark that
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.adversarial.adversarial_robustness_safety@1
  cap.t19.adversarial.adversarial_robustness_safety.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.jailbreak.jailbreak_defence@1
      if unavailable: use the in-file conservative substitute for
      `jailbreak_defence` (documented, slower, lower quality) and set
      `degraded['jailbreak_defence']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t05.sparse.sparse_upcycling@1
      if unavailable: use the in-file conservative substitute for
      `sparse_upcycling` (documented, slower, lower quality) and set
      `degraded['sparse_upcycling']='local'`

  cap.t10.proof.proof_sketch@1
      if unavailable: use the in-file conservative substitute for
      `proof_sketch` (documented, slower, lower quality) and set
      `degraded['proof_sketch']='local'`

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
   3. [ 600 lines] Core implementation A - adversarial testing of classifiers, gates and probes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - distribution-shift robustness of safety decisions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - safety-system failure-mode analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured robustness of each safety component
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.adversarial.adversarial_robustness_safety@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0925_adversarial_robustness_safety.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0926-red-team-automation

**P0926 · `red_team_automation` — Automated Red Teaming** · [spec](PART_SPECS_T19.md#p0926-red-team-automation) · [self-contained txt](../prompts/P0926_red_team_automation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0926  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0926 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0926  (26/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Automated Red Teaming
file         : parts/t19_safety/P0926_red_team_automation.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.red_team_automation
language     : Python 3.13
capability   : cap.t19.red.red_team_automation@1
determinism  : pure
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Attacks itself continuously and creatively.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. automated attack generation across all harm categories
  2. novelty enforcement so attacks are not repeats
  3. found-vulnerability triage and remediation tracking
  4. measured vulnerability-discovery rate and time-to-fix

Expanded obligations:
  1. Implement automated attack generation across all harm categories with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement novelty enforcement so attacks are not repeats together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement found-vulnerability triage and remediation tracking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured vulnerability-discovery rate and time-to-fix, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.red.red_team_automation@1
  cap.t19.red.red_team_automation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.adversarial.adversarial_robustness_safety@1
      if unavailable: use the in-file conservative substitute for
      `adversarial_robustness_safety` (documented, slower, lower quality)
      and set `degraded['adversarial_robustness_safety']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t05.model.model_config_schema@1
      if unavailable: use the in-file conservative substitute for
      `model_config_schema` (documented, slower, lower quality) and set
      `degraded['model_config_schema']='local'`

  cap.t10.adversarial.adversarial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `adversarial_reasoning` (documented, slower, lower quality) and set
      `degraded['adversarial_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - automated attack generation across all harm categories
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - novelty enforcement so attacks are not repeats
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - found-vulnerability triage and remediation tracking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured vulnerability-discovery rate and time-to-fix
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.red.red_team_automation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0926_red_team_automation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0927-privacy-engine

**P0927 · `privacy_engine` — Privacy Protection Engine** · [spec](PART_SPECS_T19.md#p0927-privacy-engine) · [self-contained txt](../prompts/P0927_privacy_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0927  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0927 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0927  (27/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Privacy Protection Engine
file         : parts/t19_safety/P0927_privacy_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.privacy_engine
language     : Python 3.13
capability   : cap.t19.privacy.privacy_engine@1
determinism  : pure
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Protects personal information rigorously.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. PII detection, classification and minimisation across all data flows
  2. purpose-limitation enforcement and consent tracking
  3. re-identification risk assessment for aggregate outputs
  4. measured leakage rate with target of zero

Expanded obligations:
  1. Implement PII detection, classification and minimisation across all data
     flows together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against OSS-Fuzz (find) — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement purpose-limitation enforcement and consent tracking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement re-identification risk assessment for aggregate outputs, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured leakage rate with target of zero with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.privacy.privacy_engine@1
  cap.t19.privacy.privacy_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.red.red_team_automation@1
      if unavailable: use the in-file conservative substitute for
      `red_team_automation` (documented, slower, lower quality) and set
      `degraded['red_team_automation']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t05.attention.attention_variants@1
      if unavailable: use the in-file conservative substitute for
      `attention_variants` (documented, slower, lower quality) and set
      `degraded['attention_variants']='local'`

  cap.t10.tree.tree_search@1
      if unavailable: use the in-file conservative substitute for
      `tree_search` (documented, slower, lower quality) and set
      `degraded['tree_search']='local'`

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
   3. [ 600 lines] Core implementation A - PII detection, classification and minimisation across all data f
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - purpose-limitation enforcement and consent tracking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - re-identification risk assessment for aggregate outputs
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured leakage rate with target of zero
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.privacy.privacy_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0927_privacy_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0928-data-rights

**P0928 · `data_rights` — Data Rights & Deletion Enforcement** · [spec](PART_SPECS_T19.md#p0928-data-rights) · [self-contained txt](../prompts/P0928_data_rights.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0928  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0928 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0928  (28/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Data Rights & Deletion Enforcement
file         : parts/t19_safety/P0928_data_rights.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.data_rights
language     : Python 3.13
capability   : cap.t19.data.data_rights@1
determinism  : pure
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Honours access, correction and deletion requests completely.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. request handling across memory, caches, logs and training influence
  2. deletion verification with proof of removal
  3. regional regulatory compliance (GDPR-class and successors)
  4. auditable compliance verification

Expanded obligations:
  1. Implement request handling across memory, caches, logs and training
     influence as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement deletion verification with proof of removal, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement regional regulatory compliance (GDPR-class and successors)
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against OSS-Fuzz (find) — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement auditable compliance verification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
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
  cap.t19.data.data_rights@1
  cap.t19.data.data_rights.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.privacy.privacy_engine@1
      if unavailable: use the in-file conservative substitute for
      `privacy_engine` (documented, slower, lower quality) and set
      `degraded['privacy_engine']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t05.activation.activation_design@1
      if unavailable: use the in-file conservative substitute for
      `activation_design` (documented, slower, lower quality) and set
      `degraded['activation_design']='local'`

  cap.t10.debate.debate_ensemble@1
      if unavailable: use the in-file conservative substitute for
      `debate_ensemble` (documented, slower, lower quality) and set
      `degraded['debate_ensemble']='local'`

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
   3. [ 600 lines] Core implementation A - request handling across memory, caches, logs and training influe
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deletion verification with proof of removal
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regional regulatory compliance (GDPR-class and successors)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - auditable compliance verification
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.data.data_rights@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0928_data_rights.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0929-copyright-engine

**P0929 · `copyright_engine` — Copyright & IP Protection** · [spec](PART_SPECS_T19.md#p0929-copyright-engine) · [self-contained txt](../prompts/P0929_copyright_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0929  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0929 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0929  (29/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Copyright & IP Protection
file         : parts/t19_safety/P0929_copyright_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.copyright_engine
language     : Python 3.13
capability   : cap.t19.copyright.copyright_engine@1
determinism  : pure
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Creates, does not copy.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. verbatim-reproduction detection and prevention above threshold lengths
  2. style-versus-substance distinction reasoning
  3. attribution requirement enforcement where applicable
  4. measured reproduction rate against protected-corpus tests

Expanded obligations:
  1. Implement verbatim-reproduction detection and prevention above threshold
     lengths, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement style-versus-substance distinction reasoning with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement attribution requirement enforcement where applicable together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured reproduction rate against protected-corpus tests as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.copyright.copyright_engine@1
  cap.t19.copyright.copyright_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.data.data_rights@1
      if unavailable: use the in-file conservative substitute for
      `data_rights` (documented, slower, lower quality) and set
      `degraded['data_rights']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t05.draft.draft_model_arch@1
      if unavailable: use the in-file conservative substitute for
      `draft_model_arch` (documented, slower, lower quality) and set
      `degraded['draft_model_arch']='local'`

  cap.t10.induction.induction_engine@1
      if unavailable: use the in-file conservative substitute for
      `induction_engine` (documented, slower, lower quality) and set
      `degraded['induction_engine']='local'`

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
   3. [ 600 lines] Core implementation A - verbatim-reproduction detection and prevention above threshold l
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - style-versus-substance distinction reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - attribution requirement enforcement where applicable
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured reproduction rate against protected-corpus tests
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.copyright.copyright_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0929_copyright_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0930-bias-mitigation

**P0930 · `bias_mitigation` — Bias Detection & Mitigation** · [spec](PART_SPECS_T19.md#p0930-bias-mitigation) · [self-contained txt](../prompts/P0930_bias_mitigation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0930  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0930 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0930  (30/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Bias Detection & Mitigation
file         : parts/t19_safety/P0930_bias_mitigation.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.bias_mitigation
language     : Python 3.13
capability   : cap.t19.bias.bias_mitigation@1
determinism  : pure
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Actively reduces unfair behaviour, measurably.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. bias measurement across demographic dimensions and intersections
  2. mitigation intervention with capability-preservation verification
  3. fairness-metric selection with explicit tradeoff documentation
  4. measured disparity reduction versus baseline

Expanded obligations:
  1. Implement bias measurement across demographic dimensions and
     intersections with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against OSS-Fuzz (find) — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement mitigation intervention with capability-preservation
     verification together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's OSS-Fuzz (find)
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement fairness-metric selection with explicit tradeoff documentation
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  4. Implement measured disparity reduction versus baseline, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.bias.bias_mitigation@1
  cap.t19.bias.bias_mitigation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.copyright.copyright_engine@1
      if unavailable: use the in-file conservative substitute for
      `copyright_engine` (documented, slower, lower quality) and set
      `degraded['copyright_engine']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t05.meta.meta_learning_arch@1
      if unavailable: use the in-file conservative substitute for
      `meta_learning_arch` (documented, slower, lower quality) and set
      `degraded['meta_learning_arch']='local'`

  cap.t10.commonsense.commonsense_engine@1
      if unavailable: use the in-file conservative substitute for
      `commonsense_engine` (documented, slower, lower quality) and set
      `degraded['commonsense_engine']='local'`

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
   3. [ 600 lines] Core implementation A - bias measurement across demographic dimensions and intersections
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - mitigation intervention with capability-preservation verificatio
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - fairness-metric selection with explicit tradeoff documentation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured disparity reduction versus baseline
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.bias.bias_mitigation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0930_bias_mitigation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0931-child-safety

**P0931 · `child_safety` — Child Safety & Vulnerable User Protection** · [spec](PART_SPECS_T19.md#p0931-child-safety) · [self-contained txt](../prompts/P0931_child_safety.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0931  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0931 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0931  (31/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Child Safety & Vulnerable User Protection
file         : parts/t19_safety/P0931_child_safety.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.child_safety
language     : Python 3.13
capability   : cap.t19.child.child_safety@1
determinism  : pure
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Absolute limits, no exceptions.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. CSAM-adjacent request hard blocking with zero tolerance
  2. age-appropriate interaction adaptation where context indicates minors
  3. vulnerable-user detection and appropriate response protocols
  4. verification of zero-failure on the standing test corpus

Expanded obligations:
  1. Implement CSAM-adjacent request hard blocking with zero tolerance
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement age-appropriate interaction adaptation where context indicates
     minors as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  3. Implement vulnerable-user detection and appropriate response protocols,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement verification of zero-failure on the standing test corpus with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
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
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.child.child_safety@1
  cap.t19.child.child_safety.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.bias.bias_mitigation@1
      if unavailable: use the in-file conservative substitute for
      `bias_mitigation` (documented, slower, lower quality) and set
      `degraded['bias_mitigation']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t05.architecture.architecture_search@1
      if unavailable: use the in-file conservative substitute for
      `architecture_search` (documented, slower, lower quality) and set
      `degraded['architecture_search']='local'`

  cap.t10.parallel.parallel_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `parallel_reasoning` (documented, slower, lower quality) and set
      `degraded['parallel_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - CSAM-adjacent request hard blocking with zero tolerance
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - age-appropriate interaction adaptation where context indicates m
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - vulnerable-user detection and appropriate response protocols
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification of zero-failure on the standing test corpus
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.child.child_safety@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0931_child_safety.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0932-crisis-response

**P0932 · `crisis_response` — Crisis & Self-Harm Response** · [spec](PART_SPECS_T19.md#p0932-crisis-response) · [self-contained txt](../prompts/P0932_crisis_response.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0932  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0932 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0932  (32/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Crisis & Self-Harm Response
file         : parts/t19_safety/P0932_crisis_response.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.crisis_response
language     : Python 3.13
capability   : cap.t19.crisis.crisis_response@1
determinism  : pure
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Responds to people in danger correctly and compassionately.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. crisis-signal detection with appropriate sensitivity
  2. evidence-based response protocols with resource provision
  3. avoidance of both dismissal and harmful specificity
  4. expert-clinician evaluation of response quality

Expanded obligations:
  1. Implement crisis-signal detection with appropriate sensitivity as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement evidence-based response protocols with resource provision, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement avoidance of both dismissal and harmful specificity with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement expert-clinician evaluation of response quality together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
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
  cap.t19.crisis.crisis_response@1
  cap.t19.crisis.crisis_response.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.child.child_safety@1
      if unavailable: use the in-file conservative substitute for
      `child_safety` (documented, slower, lower quality) and set
      `degraded['child_safety']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t05.speculative.speculative_arch_hooks@1
      if unavailable: use the in-file conservative substitute for
      `speculative_arch_hooks` (documented, slower, lower quality) and set
      `degraded['speculative_arch_hooks']='local'`

  cap.t10.multi.multi_step_arithmetic@1
      if unavailable: use the in-file conservative substitute for
      `multi_step_arithmetic` (documented, slower, lower quality) and set
      `degraded['multi_step_arithmetic']='local'`

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
   3. [ 600 lines] Core implementation A - crisis-signal detection with appropriate sensitivity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - evidence-based response protocols with resource provision
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - avoidance of both dismissal and harmful specificity
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-clinician evaluation of response quality
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.crisis.crisis_response@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0932_crisis_response.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0933-medical-legal-boundaries

**P0933 · `medical_legal_boundaries` — Professional Advice Boundary Management** · [spec](PART_SPECS_T19.md#p0933-medical-legal-boundaries) · [self-contained txt](../prompts/P0933_medical_legal_boundaries.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0933  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0933 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0933  (33/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Professional Advice Boundary Management
file         : parts/t19_safety/P0933_medical_legal_boundaries.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.medical_legal_boundaries
language     : Python 3.13
capability   : cap.t19.medical.medical_legal_boundaries@1
determinism  : pure
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Helpful expertise without dangerous overreach.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. professional-advice boundary classification per domain
  2. appropriate caveat and referral generation
  3. high-stakes decision escalation to qualified humans
  4. expert evaluation of boundary appropriateness

Expanded obligations:
  1. Implement professional-advice boundary classification per domain, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement appropriate caveat and referral generation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's OSS-Fuzz (find) target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement high-stakes decision escalation to qualified humans together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement expert evaluation of boundary appropriateness as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.medical.medical_legal_boundaries@1
  cap.t19.medical.medical_legal_boundaries.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.crisis.crisis_response@1
      if unavailable: use the in-file conservative substitute for
      `crisis_response` (documented, slower, lower quality) and set
      `degraded['crisis_response']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t05.expert.expert_specialisation@1
      if unavailable: use the in-file conservative substitute for
      `expert_specialisation` (documented, slower, lower quality) and set
      `degraded['expert_specialisation']='local'`

  cap.t10.error.error_taxonomy@1
      if unavailable: use the in-file conservative substitute for
      `error_taxonomy` (documented, slower, lower quality) and set
      `degraded['error_taxonomy']='local'`

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
   3. [ 600 lines] Core implementation A - professional-advice boundary classification per domain
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - appropriate caveat and referral generation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - high-stakes decision escalation to qualified humans
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert evaluation of boundary appropriateness
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.medical.medical_legal_boundaries@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0933_medical_legal_boundaries.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0934-agentic-safety

**P0934 · `agentic_safety` — Agentic Autonomy Safety Limits** · [spec](PART_SPECS_T19.md#p0934-agentic-safety) · [self-contained txt](../prompts/P0934_agentic_safety.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0934  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0934 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0934  (34/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Agentic Autonomy Safety Limits
file         : parts/t19_safety/P0934_agentic_safety.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.agentic_safety
language     : Python 3.13
capability   : cap.t19.agentic.agentic_safety@1
determinism  : pure
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Autonomy with hard limits and human checkpoints.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. autonomy-level definitions with per-level permitted actions
  2. irreversible-action approval requirements
  3. resource, scope and duration limits with enforcement
  4. verification that limits hold under adversarial agent behaviour

Expanded obligations:
  1. Implement autonomy-level definitions with per-level permitted actions
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement irreversible-action approval requirements together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement resource, scope and duration limits with enforcement as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement verification that limits hold under adversarial agent
     behaviour, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
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
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.agentic.agentic_safety@1
  cap.t19.agentic.agentic_safety.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.medical.medical_legal_boundaries@1
      if unavailable: use the in-file conservative substitute for
      `medical_legal_boundaries` (documented, slower, lower quality) and set
      `degraded['medical_legal_boundaries']='local'`

  cap.t05.hybrid.hybrid_mixer@1
      if unavailable: use the in-file conservative substitute for
      `hybrid_mixer` (documented, slower, lower quality) and set
      `degraded['hybrid_mixer']='local'`

  cap.t10.search.search_controller@1
      if unavailable: use the in-file conservative substitute for
      `search_controller` (documented, slower, lower quality) and set
      `degraded['search_controller']='local'`

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
   3. [ 600 lines] Core implementation A - autonomy-level definitions with per-level permitted actions
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - irreversible-action approval requirements
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - resource, scope and duration limits with enforcement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification that limits hold under adversarial agent behaviour
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.agentic.agentic_safety@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0934_agentic_safety.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0935-multi-agent-safety

**P0935 · `multi_agent_safety` — Multi-Agent System Safety** · [spec](PART_SPECS_T19.md#p0935-multi-agent-safety) · [self-contained txt](../prompts/P0935_multi_agent_safety.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0935  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0935 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0935  (35/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Multi-Agent System Safety
file         : parts/t19_safety/P0935_multi_agent_safety.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.multi_agent_safety
language     : Python 3.13
capability   : cap.t19.multi.multi_agent_safety@1
determinism  : pure
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
1000 agents must not become an uncontrolled system.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. collusion and emergent-coordination detection
  2. aggregate blast-radius limits across the agent swarm
  3. swarm-wide kill switch with verified effectiveness
  4. safety verification at full 1000-agent scale

Expanded obligations:
  1. Implement collusion and emergent-coordination detection together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement aggregate blast-radius limits across the agent swarm as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement swarm-wide kill switch with verified effectiveness, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement safety verification at full 1000-agent scale with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of OSS-Fuzz (find), so its p99 latency
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.multi.multi_agent_safety@1
  cap.t19.multi.multi_agent_safety.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.agentic.agentic_safety@1
      if unavailable: use the in-file conservative substitute for
      `agentic_safety` (documented, slower, lower quality) and set
      `degraded['agentic_safety']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t05.normalisation.normalisation_design@1
      if unavailable: use the in-file conservative substitute for
      `normalisation_design` (documented, slower, lower quality) and set
      `degraded['normalisation_design']='local'`

  cap.t10.self.self_critique@1
      if unavailable: use the in-file conservative substitute for
      `self_critique` (documented, slower, lower quality) and set
      `degraded['self_critique']='local'`

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
   3. [ 600 lines] Core implementation A - collusion and emergent-coordination detection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - aggregate blast-radius limits across the agent swarm
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - swarm-wide kill switch with verified effectiveness
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - safety verification at full 1000-agent scale
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.multi.multi_agent_safety@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0935_multi_agent_safety.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0936-tool-safety

**P0936 · `tool_safety` — Tool & Integration Safety Review** · [spec](PART_SPECS_T19.md#p0936-tool-safety) · [self-contained txt](../prompts/P0936_tool_safety.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0936  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0936 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0936  (36/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Tool & Integration Safety Review
file         : parts/t19_safety/P0936_tool_safety.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.tool_safety
language     : Python 3.13
capability   : cap.t19.tool.tool_safety@1
determinism  : pure
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Every tool is a new attack surface, reviewed before use.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tool risk assessment and permission requirement determination
  2. tool-output trust classification (never instructions)
  3. third-party tool vetting protocol
  4. measured incident rate on tool-mediated actions

Expanded obligations:
  1. Implement tool risk assessment and permission requirement determination
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement tool-output trust classification (never instructions), and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement third-party tool vetting protocol with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured incident rate on tool-mediated actions together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.tool.tool_safety@1
  cap.t19.tool.tool_safety.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.multi.multi_agent_safety@1
      if unavailable: use the in-file conservative substitute for
      `multi_agent_safety` (documented, slower, lower quality) and set
      `degraded['multi_agent_safety']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t05.multi.multi_token_prediction@1
      if unavailable: use the in-file conservative substitute for
      `multi_token_prediction` (documented, slower, lower quality) and set
      `degraded['multi_token_prediction']='local'`

  cap.t10.abstraction.abstraction_engine@1
      if unavailable: use the in-file conservative substitute for
      `abstraction_engine` (documented, slower, lower quality) and set
      `degraded['abstraction_engine']='local'`

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
   3. [ 600 lines] Core implementation A - tool risk assessment and permission requirement determination
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tool-output trust classification (never instructions)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - third-party tool vetting protocol
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured incident rate on tool-mediated actions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.tool.tool_safety@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0936_tool_safety.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0937-output-safety-classifier

**P0937 · `output_safety_classifier` — Output Safety Classification** · [spec](PART_SPECS_T19.md#p0937-output-safety-classifier) · [self-contained txt](../prompts/P0937_output_safety_classifier.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0937  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0937 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0937  (37/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Output Safety Classification
file         : parts/t19_safety/P0937_output_safety_classifier.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.output_safety_classifier
language     : Python 3.13
capability   : cap.t19.output.output_safety_classifier@1
determinism  : pure
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The last check, fast and accurate.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-category output classification within latency budget
  2. context-aware thresholds avoiding over-blocking of legitimate work
  3. classifier-uncertainty escalation to stronger review
  4. precision/recall measurement per harm category

Expanded obligations:
  1. Implement multi-category output classification within latency budget,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     OSS-Fuzz (find) target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement context-aware thresholds avoiding over-blocking of legitimate
     work with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement classifier-uncertainty escalation to stronger review together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement precision/recall measurement per harm category as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.output.output_safety_classifier@1
  cap.t19.output.output_safety_classifier.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.tool.tool_safety@1
      if unavailable: use the in-file conservative substitute for
      `tool_safety` (documented, slower, lower quality) and set
      `degraded['tool_safety']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t05.program.program_induction_arch@1
      if unavailable: use the in-file conservative substitute for
      `program_induction_arch` (documented, slower, lower quality) and set
      `degraded['program_induction_arch']='local'`

  cap.t10.spatial.spatial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `spatial_reasoning` (documented, slower, lower quality) and set
      `degraded['spatial_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - multi-category output classification within latency budget
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - context-aware thresholds avoiding over-blocking of legitimate wo
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - classifier-uncertainty escalation to stronger review
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - precision/recall measurement per harm category
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.output.output_safety_classifier@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0937_output_safety_classifier.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0938-safety-fallback-routing

**P0938 · `safety_fallback_routing` — Safety Fallback & Model Routing** · [spec](PART_SPECS_T19.md#p0938-safety-fallback-routing) · [self-contained txt](../prompts/P0938_safety_fallback_routing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0938  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0938 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0938  (38/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Safety Fallback & Model Routing
file         : parts/t19_safety/P0938_safety_fallback_routing.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.safety_fallback_routing
language     : Python 3.13
capability   : cap.t19.safety.safety_fallback_routing@1
determinism  : pure
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Flagged requests get handled, not just dropped.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fallback-model routing for classifier-flagged requests
  2. capability-appropriate fallback selection
  3. user notification of fallback with clear reasoning
  4. measured user-outcome quality on fallback paths

Expanded obligations:
  1. Implement fallback-model routing for classifier-flagged requests with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement capability-appropriate fallback selection together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement user notification of fallback with clear reasoning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured user-outcome quality on fallback paths, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
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
  cap.t19.safety.safety_fallback_routing@1
  cap.t19.safety.safety_fallback_routing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.output.output_safety_classifier@1
      if unavailable: use the in-file conservative substitute for
      `output_safety_classifier` (documented, slower, lower quality) and set
      `degraded['output_safety_classifier']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t05.init.init_scaling_laws@1
      if unavailable: use the in-file conservative substitute for
      `init_scaling_laws` (documented, slower, lower quality) and set
      `degraded['init_scaling_laws']='local'`

  cap.t10.chain.chain_compression@1
      if unavailable: use the in-file conservative substitute for
      `chain_compression` (documented, slower, lower quality) and set
      `degraded['chain_compression']='local'`

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
   3. [ 600 lines] Core implementation A - fallback-model routing for classifier-flagged requests
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability-appropriate fallback selection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - user notification of fallback with clear reasoning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured user-outcome quality on fallback paths
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.safety.safety_fallback_routing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0938_safety_fallback_routing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0939-incident-response

**P0939 · `incident_response` — Safety Incident Response & Forensics** · [spec](PART_SPECS_T19.md#p0939-incident-response) · [self-contained txt](../prompts/P0939_incident_response.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0939  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0939 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0939  (39/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Safety Incident Response & Forensics
file         : parts/t19_safety/P0939_incident_response.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.incident_response
language     : Python 3.13
capability   : cap.t19.incident.incident_response@1
determinism  : pure
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
When something goes wrong, it is understood completely.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. incident detection, classification and severity assessment
  2. forensic trace reconstruction with full provenance
  3. remediation tracking and recurrence prevention verification
  4. measured mean-time-to-detection and mean-time-to-remediation

Expanded obligations:
  1. Implement incident detection, classification and severity assessment
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement forensic trace reconstruction with full provenance as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement remediation tracking and recurrence prevention verification,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured mean-time-to-detection and mean-time-to-remediation
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against OSS-Fuzz (find) — a regression on
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
  cap.t19.incident.incident_response@1
  cap.t19.incident.incident_response.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.safety.safety_fallback_routing@1
      if unavailable: use the in-file conservative substitute for
      `safety_fallback_routing` (documented, slower, lower quality) and set
      `degraded['safety_fallback_routing']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t05.memory.memory_attention_bridge@1
      if unavailable: use the in-file conservative substitute for
      `memory_attention_bridge` (documented, slower, lower quality) and set
      `degraded['memory_attention_bridge']='local'`

  cap.t10.reasoning.reasoning_robustness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_robustness` (documented, slower, lower quality) and set
      `degraded['reasoning_robustness']='local'`

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
   3. [ 600 lines] Core implementation A - incident detection, classification and severity assessment
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - forensic trace reconstruction with full provenance
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - remediation tracking and recurrence prevention verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured mean-time-to-detection and mean-time-to-remediation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.incident.incident_response@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0939_incident_response.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0940-audit-logging

**P0940 · `audit_logging` — Tamper-Evident Audit Logging** · [spec](PART_SPECS_T19.md#p0940-audit-logging) · [self-contained txt](../prompts/P0940_audit_logging.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0940  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0940 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0940  (40/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Tamper-Evident Audit Logging
file         : parts/t19_safety/P0940_audit_logging.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.audit_logging
language     : Python 3.13
capability   : cap.t19.audit.audit_logging@1
determinism  : pure
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
An auditable record of every consequential decision.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. append-only log with cryptographic tamper evidence
  2. decision-context capture sufficient for retrospective review
  3. privacy-preserving audit design (no unnecessary content retention)
  4. audit-completeness and integrity verification

Expanded obligations:
  1. Implement append-only log with cryptographic tamper evidence as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement decision-context capture sufficient for retrospective review,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement privacy-preserving audit design (no unnecessary content
     retention) with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against OSS-Fuzz (find) — a
     regression on that benchmark is an automatic rejection of this part.
  4. Implement audit-completeness and integrity verification together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
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
  cap.t19.audit.audit_logging@1
  cap.t19.audit.audit_logging.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.incident.incident_response@1
      if unavailable: use the in-file conservative substitute for
      `incident_response` (documented, slower, lower quality) and set
      `degraded['incident_response']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t05.thought.thought_representation@1
      if unavailable: use the in-file conservative substitute for
      `thought_representation` (documented, slower, lower quality) and set
      `degraded['thought_representation']='local'`

  cap.t10.reasoning.reasoning_transfer@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_transfer` (documented, slower, lower quality) and set
      `degraded['reasoning_transfer']='local'`

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
   3. [ 600 lines] Core implementation A - append-only log with cryptographic tamper evidence
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - decision-context capture sufficient for retrospective review
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - privacy-preserving audit design (no unnecessary content retentio
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - audit-completeness and integrity verification
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.audit.audit_logging@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0940_audit_logging.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0941-governance-workflow

**P0941 · `governance_workflow` — Governance, Approval & Accountability Workflow** · [spec](PART_SPECS_T19.md#p0941-governance-workflow) · [self-contained txt](../prompts/P0941_governance_workflow.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0941  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0941 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0941  (41/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Governance, Approval & Accountability Workflow
file         : parts/t19_safety/P0941_governance_workflow.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.governance_workflow
language     : Python 3.13
capability   : cap.t19.governance.governance_workflow@1
determinism  : pure
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Humans remain accountable for consequential choices.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. approval workflows for capability releases and policy changes
  2. role and responsibility definitions with named accountability
  3. decision-record generation with rationale
  4. governance-compliance auditing

Expanded obligations:
  1. Implement approval workflows for capability releases and policy changes,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement role and responsibility definitions with named accountability
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against OSS-Fuzz (find) — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement decision-record generation with rationale together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement governance-compliance auditing as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.governance.governance_workflow@1
  cap.t19.governance.governance_workflow.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.audit.audit_logging@1
      if unavailable: use the in-file conservative substitute for
      `audit_logging` (documented, slower, lower quality) and set
      `degraded['audit_logging']='local'`

  cap.t05.omega.omega_block@1
      if unavailable: use the in-file conservative substitute for
      `omega_block` (documented, slower, lower quality) and set
      `degraded['omega_block']='local'`

  cap.t10.thought.thought_program_ir@1
      if unavailable: use the in-file conservative substitute for
      `thought_program_ir` (documented, slower, lower quality) and set
      `degraded['thought_program_ir']='local'`

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
   3. [ 600 lines] Core implementation A - approval workflows for capability releases and policy changes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - role and responsibility definitions with named accountability
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - decision-record generation with rationale
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - governance-compliance auditing
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.governance.governance_workflow@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0941_governance_workflow.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0942-transparency-reporting

**P0942 · `transparency_reporting` — Transparency & Model Card Reporting** · [spec](PART_SPECS_T19.md#p0942-transparency-reporting) · [self-contained txt](../prompts/P0942_transparency_reporting.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0942  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0942 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0942  (42/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Transparency & Model Card Reporting
file         : parts/t19_safety/P0942_transparency_reporting.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.transparency_reporting
language     : Python 3.13
capability   : cap.t19.transparency.transparency_reporting@1
determinism  : pure
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Honest public disclosure of capability and risk.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capability, limitation and risk disclosure generation
  2. safety-evaluation result publication with methodology
  3. known-failure-mode documentation
  4. review process ensuring no overstated claims

Expanded obligations:
  1. Implement capability, limitation and risk disclosure generation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement safety-evaluation result publication with methodology together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement known-failure-mode documentation as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement review process ensuring no overstated claims, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.transparency.transparency_reporting@1
  cap.t19.transparency.transparency_reporting.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.governance.governance_workflow@1
      if unavailable: use the in-file conservative substitute for
      `governance_workflow` (documented, slower, lower quality) and set
      `degraded['governance_workflow']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t05.adaptive.adaptive_depth@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_depth` (documented, slower, lower quality) and set
      `degraded['adaptive_depth']='local'`

  cap.t10.self.self_consistency@1
      if unavailable: use the in-file conservative substitute for
      `self_consistency` (documented, slower, lower quality) and set
      `degraded['self_consistency']='local'`

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
   3. [ 600 lines] Core implementation A - capability, limitation and risk disclosure generation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - safety-evaluation result publication with methodology
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - known-failure-mode documentation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - review process ensuring no overstated claims
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.transparency.transparency_reporting@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0942_transparency_reporting.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0943-external-audit

**P0943 · `external_audit` — External Audit & Third-Party Evaluation Support** · [spec](PART_SPECS_T19.md#p0943-external-audit) · [self-contained txt](../prompts/P0943_external_audit.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0943  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0943 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0943  (43/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : External Audit & Third-Party Evaluation Support
file         : parts/t19_safety/P0943_external_audit.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.external_audit
language     : Python 3.13
capability   : cap.t19.external.external_audit@1
determinism  : pure
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Independent verification, enabled properly.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structured researcher-access programme with appropriate scope
  2. reproducible-evaluation package provision
  3. finding-intake and remediation-tracking workflow
  4. measured external-finding resolution rate

Expanded obligations:
  1. Implement structured researcher-access programme with appropriate scope
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement reproducible-evaluation package provision as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement finding-intake and remediation-tracking workflow, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured external-finding resolution rate with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's OSS-Fuzz (find) target reachable; the part
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.external.external_audit@1
  cap.t19.external.external_audit.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.transparency.transparency_reporting@1
      if unavailable: use the in-file conservative substitute for
      `transparency_reporting` (documented, slower, lower quality) and set
      `degraded['transparency_reporting']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t05.long.long_context_arch@1
      if unavailable: use the in-file conservative substitute for
      `long_context_arch` (documented, slower, lower quality) and set
      `degraded['long_context_arch']='local'`

  cap.t10.analogy.analogy_engine@1
      if unavailable: use the in-file conservative substitute for
      `analogy_engine` (documented, slower, lower quality) and set
      `degraded['analogy_engine']='local'`

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
   3. [ 600 lines] Core implementation A - structured researcher-access programme with appropriate scope
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - reproducible-evaluation package provision
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - finding-intake and remediation-tracking workflow
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured external-finding resolution rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.external.external_audit@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0943_external_audit.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0944-safety-case

**P0944 · `safety_case` — Safety Case Construction** · [spec](PART_SPECS_T19.md#p0944-safety-case) · [self-contained txt](../prompts/P0944_safety_case.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0944  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0944 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0944  (44/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Safety Case Construction
file         : parts/t19_safety/P0944_safety_case.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.safety_case
language     : Python 3.13
capability   : cap.t19.safety.safety_case@1
determinism  : pure
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The argued, evidence-backed case that deployment is acceptable.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structured safety argument with claims, evidence and assumptions
  2. gap identification where evidence is insufficient
  3. residual-risk quantification and acceptance documentation
  4. safety-case review by qualified independent reviewers

Expanded obligations:
  1. Implement structured safety argument with claims, evidence and
     assumptions as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSS-Fuzz (find), so its p99 latency assertion is part
     of the acceptance criteria, not an optional extra.
  2. Implement gap identification where evidence is insufficient, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against OSS-Fuzz (find) — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement residual-risk quantification and acceptance documentation with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement safety-case review by qualified independent reviewers together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
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
  cap.t19.safety.safety_case@1
  cap.t19.safety.safety_case.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.external.external_audit@1
      if unavailable: use the in-file conservative substitute for
      `external_audit` (documented, slower, lower quality) and set
      `degraded['external_audit']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t05.symbolic.symbolic_bridge@1
      if unavailable: use the in-file conservative substitute for
      `symbolic_bridge` (documented, slower, lower quality) and set
      `degraded['symbolic_bridge']='local'`

  cap.t10.temporal.temporal_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `temporal_reasoning` (documented, slower, lower quality) and set
      `degraded['temporal_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - structured safety argument with claims, evidence and assumptions
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - gap identification where evidence is insufficient
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - residual-risk quantification and acceptance documentation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - safety-case review by qualified independent reviewers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.safety.safety_case@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0944_safety_case.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0945-capability-threshold-policy

**P0945 · `capability_threshold_policy` — Dangerous Capability Threshold Policy** · [spec](PART_SPECS_T19.md#p0945-capability-threshold-policy) · [self-contained txt](../prompts/P0945_capability_threshold_policy.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0945  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0945 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0945  (45/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Dangerous Capability Threshold Policy
file         : parts/t19_safety/P0945_capability_threshold_policy.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.capability_threshold_policy
language     : Python 3.13
capability   : cap.t19.capability.capability_threshold_policy@1
determinism  : pure
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Pre-committed limits, decided before the capability exists.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. threshold definitions per dangerous-capability category
  2. evaluation protocols determining threshold crossing
  3. pre-committed response actions on crossing
  4. verification that responses trigger reliably in tests

Expanded obligations:
  1. Implement threshold definitions per dangerous-capability category, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against OSS-Fuzz
     (find) — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement evaluation protocols determining threshold crossing with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement pre-committed response actions on crossing together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of OSS-Fuzz (find), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement verification that responses trigger reliably in tests as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.capability.capability_threshold_policy@1
  cap.t19.capability.capability_threshold_policy.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.safety.safety_case@1
      if unavailable: use the in-file conservative substitute for
      `safety_case` (documented, slower, lower quality) and set
      `degraded['safety_case']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t05.weight.weight_sharing@1
      if unavailable: use the in-file conservative substitute for
      `weight_sharing` (documented, slower, lower quality) and set
      `degraded['weight_sharing']='local'`

  cap.t10.reasoning.reasoning_memory@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_memory` (documented, slower, lower quality) and set
      `degraded['reasoning_memory']='local'`

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
   3. [ 600 lines] Core implementation A - threshold definitions per dangerous-capability category
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - evaluation protocols determining threshold crossing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - pre-committed response actions on crossing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification that responses trigger reliably in tests
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.capability.capability_threshold_policy@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0945_capability_threshold_policy.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0946-deployment-gating

**P0946 · `deployment_gating` — Deployment Gating & Staged Rollout** · [spec](PART_SPECS_T19.md#p0946-deployment-gating) · [self-contained txt](../prompts/P0946_deployment_gating.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0946  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0946 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0946  (46/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Deployment Gating & Staged Rollout
file         : parts/t19_safety/P0946_deployment_gating.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.deployment_gating
language     : Python 3.13
capability   : cap.t19.deployment.deployment_gating@1
determinism  : pure
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Capability reaches the world gradually and reversibly.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. staged rollout with per-stage safety criteria
  2. monitoring requirements and rollback triggers per stage
  3. user-cohort selection with informed-consent handling
  4. measured incident rate across rollout stages

Expanded obligations:
  1. Implement staged rollout with per-stage safety criteria with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's OSS-Fuzz (find) target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement monitoring requirements and rollback triggers per stage
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement user-cohort selection with informed-consent handling as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured incident rate across rollout stages, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
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
  cap.t19.deployment.deployment_gating@1
  cap.t19.deployment.deployment_gating.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.capability.capability_threshold_policy@1
      if unavailable: use the in-file conservative substitute for
      `capability_threshold_policy` (documented, slower, lower quality) and
      set `degraded['capability_threshold_policy']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t05.action.action_head@1
      if unavailable: use the in-file conservative substitute for
      `action_head` (documented, slower, lower quality) and set
      `degraded['action_head']='local'`

  cap.t10.reasoning.reasoning_faithfulness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_faithfulness` (documented, slower, lower quality) and set
      `degraded['reasoning_faithfulness']='local'`

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
   3. [ 600 lines] Core implementation A - staged rollout with per-stage safety criteria
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - monitoring requirements and rollback triggers per stage
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - user-cohort selection with informed-consent handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured incident rate across rollout stages
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.deployment.deployment_gating@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0946_deployment_gating.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0947-monitoring-production

**P0947 · `monitoring_production` — Production Safety Monitoring** · [spec](PART_SPECS_T19.md#p0947-monitoring-production) · [self-contained txt](../prompts/P0947_monitoring_production.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0947  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0947 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0947  (47/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Production Safety Monitoring
file         : parts/t19_safety/P0947_monitoring_production.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.monitoring_production
language     : Python 3.13
capability   : cap.t19.monitoring.monitoring_production@1
determinism  : pure
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Watches real usage for real harm, continuously.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. misuse-pattern detection across traffic with privacy preservation
  2. novel-harm discovery from production signals
  3. abuse-account detection and enforcement workflow
  4. measured detection latency for emerging misuse patterns

Expanded obligations:
  1. Implement misuse-pattern detection across traffic with privacy
     preservation together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement novel-harm discovery from production signals as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against OSS-Fuzz (find)
     — a regression on that benchmark is an automatic rejection of this part.
  3. Implement abuse-account detection and enforcement workflow, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured detection latency for emerging misuse patterns with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.monitoring.monitoring_production@1
  cap.t19.monitoring.monitoring_production.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.deployment.deployment_gating@1
      if unavailable: use the in-file conservative substitute for
      `deployment_gating` (documented, slower, lower quality) and set
      `degraded['deployment_gating']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t05.prompt.prompt_representation@1
      if unavailable: use the in-file conservative substitute for
      `prompt_representation` (documented, slower, lower quality) and set
      `degraded['prompt_representation']='local'`

  cap.t10.subgoal.subgoal_caching@1
      if unavailable: use the in-file conservative substitute for
      `subgoal_caching` (documented, slower, lower quality) and set
      `degraded['subgoal_caching']='local'`

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
   3. [ 600 lines] Core implementation A - misuse-pattern detection across traffic with privacy preservatio
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - novel-harm discovery from production signals
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - abuse-account detection and enforcement workflow
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured detection latency for emerging misuse patterns
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.monitoring.monitoring_production@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0947_monitoring_production.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0948-safety-capability-tradeoff

**P0948 · `safety_capability_tradeoff` — Safety/Capability Frontier Management** · [spec](PART_SPECS_T19.md#p0948-safety-capability-tradeoff) · [self-contained txt](../prompts/P0948_safety_capability_tradeoff.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0948  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0948 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0948  (48/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Safety/Capability Frontier Management
file         : parts/t19_safety/P0948_safety_capability_tradeoff.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.safety_capability_tradeoff
language     : Python 3.13
capability   : cap.t19.safety.safety_capability_tradeoff@1
determinism  : pure
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Pushes the frontier where safety allows and says where it does not.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. frontier measurement of the safety/helpfulness tradeoff
  2. over-refusal cost quantification in real user terms
  3. targeted improvement of the frontier rather than sliding along it
  4. target: strictly better on both axes than Opus 5

Expanded obligations:
  1. Implement frontier measurement of the safety/helpfulness tradeoff as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement over-refusal cost quantification in real user terms, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's OSS-Fuzz (find) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement targeted improvement of the frontier rather than sliding along
     it with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of OSS-Fuzz
     (find), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  4. Implement target: strictly better on both axes than Opus 5 together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.safety.safety_capability_tradeoff@1
  cap.t19.safety.safety_capability_tradeoff.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.monitoring.monitoring_production@1
      if unavailable: use the in-file conservative substitute for
      `monitoring_production` (documented, slower, lower quality) and set
      `degraded['monitoring_production']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t05.arch.arch_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `arch_spec_doc` (documented, slower, lower quality) and set
      `degraded['arch_spec_doc']='local'`

  cap.t10.reasoning.reasoning_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_spec_doc` (documented, slower, lower quality) and set
      `degraded['reasoning_spec_doc']='local'`

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
   3. [ 600 lines] Core implementation A - frontier measurement of the safety/helpfulness tradeoff
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - over-refusal cost quantification in real user terms
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - targeted improvement of the frontier rather than sliding along i
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: strictly better on both axes than Opus 5
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.safety.safety_capability_tradeoff@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0948_safety_capability_tradeoff.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0949-alignment-eval

**P0949 · `alignment_eval` — Alignment Evaluation Suite** · [spec](PART_SPECS_T19.md#p0949-alignment-eval) · [self-contained txt](../prompts/P0949_alignment_eval.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0949  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0949 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0949  (49/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Alignment Evaluation Suite
file         : parts/t19_safety/P0949_alignment_eval.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.alignment_eval
language     : Python 3.13
capability   : cap.t19.alignment.alignment_eval@1
determinism  : pure
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
Measures alignment as rigorously as capability.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. behavioural audit suite covering deception, sycophancy, power-seeking and corrigibility
  2. automated audit with human validation of a sampled subset
  3. comparison methodology against Opus 5's published 2.3 audit score
  4. target: measurably lower misaligned-behaviour score than Opus 5

Expanded obligations:
  1. Implement behavioural audit suite covering deception, sycophancy,
     power-seeking and corrigibility, and make it correct under concurrency:
     at least 64 in-flight `OmegaEnvelope`s must be able to traverse it
     simultaneously. No lock, mutex or borrow may be held across an `await` /
     `.await` / `yield` boundary, and the part must expose a contention
     counter so T09 can attribute latency to it. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement automated audit with human validation of a sampled subset with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement comparison methodology against Opus 5's published 2.3 audit
     score together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against OSS-Fuzz (find) — a
     regression on that benchmark is an automatic rejection of this part.
  4. Implement target: measurably lower misaligned-behaviour score than Opus
     5 as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.alignment.alignment_eval@1
  cap.t19.alignment.alignment_eval.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.safety.safety_capability_tradeoff@1
      if unavailable: use the in-file conservative substitute for
      `safety_capability_tradeoff` (documented, slower, lower quality) and
      set `degraded['safety_capability_tradeoff']='local'`

  cap.t05.latent.latent_program_slots@1
      if unavailable: use the in-file conservative substitute for
      `latent_program_slots` (documented, slower, lower quality) and set
      `degraded['latent_program_slots']='local'`

  cap.t10.outcome.outcome_verifier@1
      if unavailable: use the in-file conservative substitute for
      `outcome_verifier` (documented, slower, lower quality) and set
      `degraded['outcome_verifier']='local'`

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
   3. [ 600 lines] Core implementation A - behavioural audit suite covering deception, sycophancy, power-se
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automated audit with human validation of a sampled subset
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - comparison methodology against Opus 5's published 2.3 audit scor
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: measurably lower misaligned-behaviour score than Opus 5
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.alignment.alignment_eval@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0949_alignment_eval.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0950-safety-spec-doc

**P0950 · `safety_spec_doc` — Safety Specification & Guarantee Register** · [spec](PART_SPECS_T19.md#p0950-safety-spec-doc) · [self-contained txt](../prompts/P0950_safety_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0950  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0950 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0950  (50/50 of tier T19)
tier         : T19 — Safety, Alignment, Interpretability & Governance
title        : Safety Specification & Guarantee Register
file         : parts/t19_safety/P0950_safety_spec_doc.py          <-- create exactly this path, nothing else
module       : hyperion.t19.safety.safety_spec_doc
language     : Python 3.13
capability   : cap.t19.safety.safety_spec_doc@1
determinism  : pure
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSS-Fuzz (find)

MISSION
-------
The authoritative, honest record of every safety property.

Tier context:
  Constitution enforcement, deception detection, mechanistic interpretability,
  dual-use gating and auditable control.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. guarantee register with evidence strength per claim
  2. explicit list of what is not guaranteed
  3. residual-risk documentation reviewed by independent reviewers
  4. drift detection between claimed and demonstrated safety properties

Expanded obligations:
  1. Implement guarantee register with evidence strength per claim with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of OSS-Fuzz (find), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement explicit list of what is not guaranteed together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against OSS-Fuzz (find) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement residual-risk documentation reviewed by independent reviewers
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSS-Fuzz (find) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement drift detection between claimed and demonstrated safety
     properties, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     OSS-Fuzz (find), so its p99 latency assertion is part of the acceptance
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t19.safety.safety_spec_doc@1
  cap.t19.safety.safety_spec_doc.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t19.alignment.alignment_eval@1
      if unavailable: use the in-file conservative substitute for
      `alignment_eval` (documented, slower, lower quality) and set
      `degraded['alignment_eval']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t05.positional.positional_design@1
      if unavailable: use the in-file conservative substitute for
      `positional_design` (documented, slower, lower quality) and set
      `degraded['positional_design']='local'`

  cap.t10.constraint.constraint_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `constraint_reasoning` (documented, slower, lower quality) and set
      `degraded['constraint_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - guarantee register with evidence strength per claim
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - explicit list of what is not guaranteed
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - residual-risk documentation reviewed by independent reviewers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - drift detection between claimed and demonstrated safety properti
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t19.safety.safety_spec_doc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t19_safety/P0950_safety_spec_doc.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
