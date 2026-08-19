# HYPERION-Ω — Worker prompts · T01 · Foundation, ABI & Determinism

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

## PROMPT p0001-abi-types

**P0001 · `abi_types` — Core ABI Scalar & Tensor Type System** · [spec](PART_SPECS_T01.md#p0001-abi-types) · [self-contained txt](../prompts/P0001_abi_types.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0001  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0001 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0001  (1/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Core ABI Scalar & Tensor Type System
file         : parts/t01_foundation/P0001_abi_types.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.abi_types
language     : Python 3.13
capability   : cap.t01.abi.abi_types@1
determinism  : pure
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Define every scalar, vector, tensor, ragged and symbolic dtype used across
all 1000 parts, with exact bit layouts.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fp8-e4m3/e5m2, bf16, fp16, tf32, int4/int8 packed, mx-block formats with shared exponent
  2. shape algebra with symbolic dims, broadcasting lattice, and compile-time rank checking
  3. canonical byte layout + endianness normalisation and zero-copy views
  4. saturating/wrapping cast matrix with round-to-nearest-even and stochastic rounding

Expanded obligations:
  1. Implement fp8-e4m3/e5m2, bf16, fp16, tf32, int4/int8 packed, mx-block
     formats with shared exponent, and make it correct under concurrency: at
     least 64 in-flight `OmegaEnvelope`s must be able to traverse it
     simultaneously. No lock, mutex or borrow may be held across an `await` /
     `.await` / `yield` boundary, and the part must expose a contention
     counter so T09 can attribute latency to it. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement shape algebra with symbolic dims, broadcasting lattice, and
     compile-time rank checking with an explicit *a-priori* cost model.
     Before doing the work the part must be able to state the tokens, FLOPs
     and microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement canonical byte layout + endianness normalisation and zero-copy
     views together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  4. Implement saturating/wrapping cast matrix with round-to-nearest-even and
     stochastic rounding as a first-class, fully realised mechanism. No stub,
     no `NotImplementedError`, no configuration flag whose default disables
     it. Its state must be reportable through `describe()` and it must be
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.abi.abi_types@1
  cap.t01.abi.abi_types.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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
   3. [ 600 lines] Core implementation A - fp8-e4m3/e5m2, bf16, fp16, tf32, int4/int8 packed, mx-block form
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - shape algebra with symbolic dims, broadcasting lattice, and comp
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - canonical byte layout + endianness normalisation and zero-copy v
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - saturating/wrapping cast matrix with round-to-nearest-even and s
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.abi.abi_types@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0001_abi_types.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0002-abi-errors

**P0002 · `abi_errors` — OmegaError Taxonomy & Cause Chains** · [spec](PART_SPECS_T01.md#p0002-abi-errors) · [self-contained txt](../prompts/P0002_abi_errors.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0002  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0002 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0002  (2/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : OmegaError Taxonomy & Cause Chains
file         : parts/t01_foundation/P0002_abi_errors.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.abi_errors
language     : Python 3.13
capability   : cap.t01.abi.abi_errors@1
determinism  : pure
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Implement the 9-range error model with immutable cause chains, remedies and
budget accounting.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. OmegaCode enum with 240 documented codes and stable numeric values
  2. cause-chain builder that is allocation-bounded and cycle-safe
  3. retryability classifier plus exponential-decorrelated-jitter policy objects
  4. redaction pass so errors never leak secrets or user content

Expanded obligations:
  1. Implement OmegaCode enum with 240 documented codes and stable numeric
     values with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement cause-chain builder that is allocation-bounded and cycle-safe
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement retryability classifier plus exponential-decorrelated-jitter
     policy objects as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement redaction pass so errors never leak secrets or user content,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.abi.abi_errors@1
  cap.t01.abi.abi_errors.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

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
   3. [ 600 lines] Core implementation A - OmegaCode enum with 240 documented codes and stable numeric valu
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cause-chain builder that is allocation-bounded and cycle-safe
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - retryability classifier plus exponential-decorrelated-jitter pol
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - redaction pass so errors never leak secrets or user content
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.abi.abi_errors@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0002_abi_errors.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0003-abi-result

**P0003 · `abi_result` — Result / Partial / Budget Monad** · [spec](PART_SPECS_T01.md#p0003-abi-result) · [self-contained txt](../prompts/P0003_abi_result.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0003  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0003 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0003  (3/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Result / Partial / Budget Monad
file         : parts/t01_foundation/P0003_abi_result.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.abi_result
language     : Python 3.13
capability   : cap.t01.abi.abi_result@1
determinism  : pure
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Provide the universal return container carrying value, partiality, budget
spend and provenance.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. Result<T> with Ok/Partial/Err and monadic map/and_then/recover
  2. budget ledger arithmetic with saturating subtraction and overspend detection
  3. partial-result merge semantics for fan-out calls
  4. zero-cost conversion to/from the wire envelope

Expanded obligations:
  1. Implement Result<T> with Ok/Partial/Err and monadic map/and_then/recover
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement budget ledger arithmetic with saturating subtraction and
     overspend detection as a first-class, fully realised mechanism. No stub,
     no `NotImplementedError`, no configuration flag whose default disables
     it. Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement partial-result merge semantics for fan-out calls, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement zero-cost conversion to/from the wire envelope with an
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.abi.abi_result@1
  cap.t01.abi.abi_result.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

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
   3. [ 600 lines] Core implementation A - Result<T> with Ok/Partial/Err and monadic map/and_then/recover
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - budget ledger arithmetic with saturating subtraction and overspe
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partial-result merge semantics for fan-out calls
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - zero-cost conversion to/from the wire envelope
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.abi.abi_result@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0003_abi_result.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0004-cbor-canonical

**P0004 · `cbor_canonical` — Deterministic CBOR Codec** · [spec](PART_SPECS_T01.md#p0004-cbor-canonical) · [self-contained txt](../prompts/P0004_cbor_canonical.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0004  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0004 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0004  (4/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Deterministic CBOR Codec
file         : parts/t01_foundation/P0004_cbor_canonical.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.cbor_canonical
language     : Python 3.13
capability   : cap.t01.cbor.cbor_canonical@1
determinism  : pure
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
RFC 8949 deterministic CBOR encode/decode used for every payload on the
Ω-Bus.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. bytewise-sorted map keys, shortest-form integers, no indefinite lengths
  2. streaming decoder with depth/size limits and no unbounded allocation
  3. schema-guided fast paths for the 40 hottest message types
  4. differential fuzz harness against a naive reference encoder

Expanded obligations:
  1. Implement bytewise-sorted map keys, shortest-form integers, no
     indefinite lengths as a first-class, fully realised mechanism. No stub,
     no `NotImplementedError`, no configuration flag whose default disables
     it. Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement streaming decoder with depth/size limits and no unbounded
     allocation, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement schema-guided fast paths for the 40 hottest message types with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement differential fuzz harness against a naive reference encoder
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
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
  cap.t01.cbor.cbor_canonical@1
  cap.t01.cbor.cbor_canonical.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

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
   3. [ 600 lines] Core implementation A - bytewise-sorted map keys, shortest-form integers, no indefinite 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - streaming decoder with depth/size limits and no unbounded alloca
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - schema-guided fast paths for the 40 hottest message types
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - differential fuzz harness against a naive reference encoder
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.cbor.cbor_canonical@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0004_cbor_canonical.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0005-blake3-hash

**P0005 · `blake3_hash` — BLAKE3 & Merkle Integrity Core** · [spec](PART_SPECS_T01.md#p0005-blake3-hash) · [self-contained txt](../prompts/P0005_blake3_hash.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0005  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0005 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0005  (5/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : BLAKE3 & Merkle Integrity Core
file         : parts/t01_foundation/P0005_blake3_hash.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.blake3_hash
language     : Python 3.13
capability   : cap.t01.blake3.blake3_hash@1
determinism  : pure
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Content hashing, keyed MAC and Merkle trees for envelope integrity and
artifact identity.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. portable BLAKE3 with SIMD-friendly block loop and incremental XOF
  2. Merkle tree over chunked artifacts with inclusion proof generation/verification
  3. keyed derivation for per-part integrity tags
  4. constant-time tag comparison

Expanded obligations:
  1. Implement portable BLAKE3 with SIMD-friendly block loop and incremental
     XOF, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement Merkle tree over chunked artifacts with inclusion proof
     generation/verification with an explicit *a-priori* cost model. Before
     doing the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Its contribution is measured
     against SWE-bench Verified — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement keyed derivation for per-part integrity tags together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement constant-time tag comparison as a first-class, fully realised
     mechanism. No stub, no `NotImplementedError`, no configuration flag
     whose default disables it. Its state must be reportable through
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
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.blake3.blake3_hash@1
  cap.t01.blake3.blake3_hash.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

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
   3. [ 600 lines] Core implementation A - portable BLAKE3 with SIMD-friendly block loop and incremental XO
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - Merkle tree over chunked artifacts with inclusion proof generati
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - keyed derivation for per-part integrity tags
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - constant-time tag comparison
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.blake3.blake3_hash@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0005_blake3_hash.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0006-chacha-seeds

**P0006 · `chacha_seeds` — split_seed Deterministic RNG** · [spec](PART_SPECS_T01.md#p0006-chacha-seeds) · [self-contained txt](../prompts/P0006_chacha_seeds.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0006  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0006 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0006  (6/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : split_seed Deterministic RNG
file         : parts/t01_foundation/P0006_chacha_seeds.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.chacha_seeds
language     : Python 3.13
capability   : cap.t01.chacha.chacha_seeds@1
determinism  : pure
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The one and only randomness source: ChaCha20-based hierarchical seed
splitting.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. split_seed(root, part_id, call_index) with domain separation strings
  2. counter-based streams enabling replay and parallel reproducibility
  3. distributions: uniform, normal (ziggurat), categorical (alias table), gumbel
  4. cross-platform bit-exactness test vectors

Expanded obligations:
  1. Implement split_seed(root, part_id, call_index) with domain separation
     strings with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement counter-based streams enabling replay and parallel
     reproducibility together with its verification path, so that anything
     this mechanism produces can be independently re-checked *inside this
     same file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement distributions: uniform, normal (ziggurat), categorical (alias
     table), gumbel as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement cross-platform bit-exactness test vectors, and make it correct
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
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.chacha.chacha_seeds@1
  cap.t01.chacha.chacha_seeds.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

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
   3. [ 600 lines] Core implementation A - split_seed(root, part_id, call_index) with domain separation str
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - counter-based streams enabling replay and parallel reproducibili
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - distributions: uniform, normal (ziggurat), categorical (alias ta
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cross-platform bit-exactness test vectors
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.chacha.chacha_seeds@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0006_chacha_seeds.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0007-omega-bus-core

**P0007 · `omega_bus_core` — Ω-Bus Capability Registry** · [spec](PART_SPECS_T01.md#p0007-omega-bus-core) · [self-contained txt](../prompts/P0007_omega_bus_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0007  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0007 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0007  (7/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Ω-Bus Capability Registry
file         : parts/t01_foundation/P0007_omega_bus_core.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.omega_bus_core
language     : Python 3.13
capability   : cap.t01.omega.omega_bus_core@1
determinism  : pure
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
In-process capability registry with versioned lookup, fallbacks and
link-time validation.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. acquire/publish with semver major pinning and ambiguity detection
  2. declared-fallback resolution when a capability is absent
  3. topological link validation producing a human-readable unresolved report
  4. handle lifetime, refcounting and safe teardown ordering

Expanded obligations:
  1. Implement acquire/publish with semver major pinning and ambiguity
     detection together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement declared-fallback resolution when a capability is absent as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement topological link validation producing a human-readable
     unresolved report, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     SWE-bench Verified — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement handle lifetime, refcounting and safe teardown ordering with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.omega.omega_bus_core@1
  cap.t01.omega.omega_bus_core.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

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
   3. [ 600 lines] Core implementation A - acquire/publish with semver major pinning and ambiguity detectio
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - declared-fallback resolution when a capability is absent
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - topological link validation producing a human-readable unresolve
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - handle lifetime, refcounting and safe teardown ordering
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.omega.omega_bus_core@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0007_omega_bus_core.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0008-omega-bus-ipc

**P0008 · `omega_bus_ipc` — Cross-Process Ω-Bus Transport** · [spec](PART_SPECS_T01.md#p0008-omega-bus-ipc) · [self-contained txt](../prompts/P0008_omega_bus_ipc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0008  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0008 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0008  (8/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Cross-Process Ω-Bus Transport
file         : parts/t01_foundation/P0008_omega_bus_ipc.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.omega_bus_ipc
language     : Python 3.13
capability   : cap.t01.omega.omega_bus_ipc@1
determinism  : pure
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Shared-memory + unix-socket transport so parts can live in separate
processes/machines.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. ring-buffer SPSC/MPMC queues with cacheline padding and no false sharing
  2. zero-copy payload handoff via memfd/shm segments with lifetime tokens
  3. backpressure, credit-based flow control and head-of-line-blocking avoidance
  4. crash detection with epoch fencing so a dead peer cannot corrupt shared state

Expanded obligations:
  1. Implement ring-buffer SPSC/MPMC queues with cacheline padding and no
     false sharing as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement zero-copy payload handoff via memfd/shm segments with lifetime
     tokens, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement backpressure, credit-based flow control and
     head-of-line-blocking avoidance with an explicit *a-priori* cost model.
     Before doing the work the part must be able to state the tokens, FLOPs
     and microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Correctness here is what makes the
     tier's SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement crash detection with epoch fencing so a dead peer cannot
     corrupt shared state together with its verification path, so that
     anything this mechanism produces can be independently re-checked *inside
     this same file* without contacting any other part. The checker must be
     cheap enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of SWE-bench
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.omega.omega_bus_ipc@1
  cap.t01.omega.omega_bus_ipc.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

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
   3. [ 600 lines] Core implementation A - ring-buffer SPSC/MPMC queues with cacheline padding and no false
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - zero-copy payload handoff via memfd/shm segments with lifetime t
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - backpressure, credit-based flow control and head-of-line-blockin
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - crash detection with epoch fencing so a dead peer cannot corrupt
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.omega.omega_bus_ipc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0008_omega_bus_ipc.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0009-envelope-codec

**P0009 · `envelope_codec` — OmegaEnvelope Encode/Decode** · [spec](PART_SPECS_T01.md#p0009-envelope-codec) · [self-contained txt](../prompts/P0009_envelope_codec.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0009  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0009 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0009  (9/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : OmegaEnvelope Encode/Decode
file         : parts/t01_foundation/P0009_envelope_codec.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.envelope_codec
language     : Python 3.13
capability   : cap.t01.envelope.envelope_codec@1
determinism  : pure
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The wire envelope: trace context, deadline, budget, provenance and integrity
tag.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. fixed-layout header for branch-free parsing plus variable CBOR body
  2. deadline arithmetic on a monotonic clock with skew guards
  3. provenance append with size cap and eviction policy
  4. integrity verify-then-use ordering with tamper telemetry

Expanded obligations:
  1. Implement fixed-layout header for branch-free parsing plus variable CBOR
     body, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement deadline arithmetic on a monotonic clock with skew guards with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement provenance append with size cap and eviction policy together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement integrity verify-then-use ordering with tamper telemetry as a
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.envelope.envelope_codec@1
  cap.t01.envelope.envelope_codec.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

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
   3. [ 600 lines] Core implementation A - fixed-layout header for branch-free parsing plus variable CBOR b
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deadline arithmetic on a monotonic clock with skew guards
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - provenance append with size cap and eviction policy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - integrity verify-then-use ordering with tamper telemetry
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.envelope.envelope_codec@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0009_envelope_codec.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0010-trace-context

**P0010 · `trace_context` — Distributed Trace & Span Model** · [spec](PART_SPECS_T01.md#p0010-trace-context) · [self-contained txt](../prompts/P0010_trace_context.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0010  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0010 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0010  (10/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Distributed Trace & Span Model
file         : parts/t01_foundation/P0010_trace_context.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.trace_context
language     : Python 3.13
capability   : cap.t01.trace.trace_context@1
determinism  : pure
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
128-bit trace ids, causal span trees and sampling that survives 1000-way
fan-out.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. W3C-compatible trace context plus Ω extensions for budget propagation
  2. causal parent tracking across async boundaries and thread hops
  3. adaptive tail-based sampling that always keeps errors and slow spans
  4. span buffer with bounded memory and lock-free append

Expanded obligations:
  1. Implement W3C-compatible trace context plus Ω extensions for budget
     propagation with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement causal parent tracking across async boundaries and thread hops
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement adaptive tail-based sampling that always keeps errors and slow
     spans as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement span buffer with bounded memory and lock-free append, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.trace.trace_context@1
  cap.t01.trace.trace_context.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

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
   3. [ 600 lines] Core implementation A - W3C-compatible trace context plus Ω extensions for budget propag
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - causal parent tracking across async boundaries and thread hops
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - adaptive tail-based sampling that always keeps errors and slow s
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - span buffer with bounded memory and lock-free append
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.trace.trace_context@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0010_trace_context.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0011-clock-time

**P0011 · `clock_time` — Monotonic Clock & Deadline Arithmetic** · [spec](PART_SPECS_T01.md#p0011-clock-time) · [self-contained txt](../prompts/P0011_clock_time.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0011  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0011 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0011  (11/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Monotonic Clock & Deadline Arithmetic
file         : parts/t01_foundation/P0011_clock_time.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.clock_time
language     : Python 3.13
capability   : cap.t01.clock.clock_time@1
determinism  : pure
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Time primitives: monotonic ns, TSC calibration, deadlines, timers and
virtual clocks.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. TSC-to-ns calibration with drift correction and invariant-TSC detection
  2. hierarchical timer wheel for millions of pending deadlines
  3. virtual clock injection for deterministic replay of timeout logic
  4. deadline propagation with reserve-and-release semantics

Expanded obligations:
  1. Implement TSC-to-ns calibration with drift correction and invariant-TSC
     detection together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement hierarchical timer wheel for millions of pending deadlines as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement virtual clock injection for deterministic replay of timeout
     logic, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement deadline propagation with reserve-and-release semantics with
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.clock.clock_time@1
  cap.t01.clock.clock_time.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

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
   3. [ 600 lines] Core implementation A - TSC-to-ns calibration with drift correction and invariant-TSC de
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hierarchical timer wheel for millions of pending deadlines
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - virtual clock injection for deterministic replay of timeout logi
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - deadline propagation with reserve-and-release semantics
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.clock.clock_time@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0011_clock_time.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0012-alloc-arena

**P0012 · `alloc_arena` — Arena & Slab Allocators** · [spec](PART_SPECS_T01.md#p0012-alloc-arena) · [self-contained txt](../prompts/P0012_alloc_arena.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0012  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0012 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0012  (12/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Arena & Slab Allocators
file         : parts/t01_foundation/P0012_alloc_arena.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.alloc_arena
language     : Python 3.13
capability   : cap.t01.alloc.alloc_arena@1
determinism  : pure
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Deterministic allocation: bump arenas, size-class slabs and NUMA-aware
pools.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. bump arena with scope guards and O(1) reset
  2. slab allocator with per-thread magazines and cross-thread free lists
  3. NUMA-local pools with first-touch policy and hugepage backing
  4. allocation accounting with high-water marks and leak assertions

Expanded obligations:
  1. Implement bump arena with scope guards and O(1) reset as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement slab allocator with per-thread magazines and cross-thread free
     lists, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement NUMA-local pools with first-touch policy and hugepage backing
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement allocation accounting with high-water marks and leak
     assertions together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.

REQUIRED SYMBOLS (exact names; the linker looks for these and nothing else)
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
  cap.t01.alloc.alloc_arena@1
  cap.t01.alloc.alloc_arena.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

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
   3. [ 600 lines] Core implementation A - bump arena with scope guards and O(1) reset
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - slab allocator with per-thread magazines and cross-thread free l
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - NUMA-local pools with first-touch policy and hugepage backing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - allocation accounting with high-water marks and leak assertions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.alloc.alloc_arena@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0012_alloc_arena.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0013-mem-layout

**P0013 · `mem_layout` — Cache-Aware Data Layout Toolkit** · [spec](PART_SPECS_T01.md#p0013-mem-layout) · [self-contained txt](../prompts/P0013_mem_layout.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0013  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0013 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0013  (13/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Cache-Aware Data Layout Toolkit
file         : parts/t01_foundation/P0013_mem_layout.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.mem_layout
language     : Python 3.13
capability   : cap.t01.mem.mem_layout@1
determinism  : pure
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
SoA/AoS transforms, tiling and alignment utilities that all hot loops build
on.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. struct-of-arrays generator with padding computation
  2. tile-shape solver for a given cache hierarchy description
  3. software prefetch scheduling helpers with distance tuning
  4. layout equivalence checker used by the compiler tier

Expanded obligations:
  1. Implement struct-of-arrays generator with padding computation, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement tile-shape solver for a given cache hierarchy description with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement software prefetch scheduling helpers with distance tuning
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement layout equivalence checker used by the compiler tier as a
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.mem.mem_layout@1
  cap.t01.mem.mem_layout.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

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
   3. [ 600 lines] Core implementation A - struct-of-arrays generator with padding computation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tile-shape solver for a given cache hierarchy description
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - software prefetch scheduling helpers with distance tuning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - layout equivalence checker used by the compiler tier
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.mem.mem_layout@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0013_mem_layout.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0014-atomics-sync

**P0014 · `atomics_sync` — Lock-Free Synchronisation Primitives** · [spec](PART_SPECS_T01.md#p0014-atomics-sync) · [self-contained txt](../prompts/P0014_atomics_sync.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0014  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0014 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0014  (14/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Lock-Free Synchronisation Primitives
file         : parts/t01_foundation/P0014_atomics_sync.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.atomics_sync
language     : Python 3.13
capability   : cap.t01.atomics.atomics_sync@1
determinism  : pure
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The concurrency toolbox: epochs, seqlocks, hazard pointers, futex parking.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. epoch-based reclamation with bounded garbage
  2. seqlock and versioned snapshot reads for hot config
  3. MCS/ticket locks with adaptive spin-then-park
  4. ABA-safe treiber stack and Michael-Scott queue

Expanded obligations:
  1. Implement epoch-based reclamation with bounded garbage with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement seqlock and versioned snapshot reads for hot config together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement MCS/ticket locks with adaptive spin-then-park as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement ABA-safe treiber stack and Michael-Scott queue, and make it
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.atomics.atomics_sync@1
  cap.t01.atomics.atomics_sync.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

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
   3. [ 600 lines] Core implementation A - epoch-based reclamation with bounded garbage
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - seqlock and versioned snapshot reads for hot config
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - MCS/ticket locks with adaptive spin-then-park
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - ABA-safe treiber stack and Michael-Scott queue
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.atomics.atomics_sync@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0014_atomics_sync.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0015-task-runtime

**P0015 · `task_runtime` — Deterministic Task Scheduler** · [spec](PART_SPECS_T01.md#p0015-task-runtime) · [self-contained txt](../prompts/P0015_task_runtime.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0015  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0015 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0015  (15/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Deterministic Task Scheduler
file         : parts/t01_foundation/P0015_task_runtime.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.task_runtime
language     : Python 3.13
capability   : cap.t01.task.task_runtime@1
determinism  : pure
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Work-stealing runtime with a deterministic mode for reproducible parallel
execution.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. work-stealing deques with random-then-round-robin victim selection
  2. deterministic replay mode with a recorded schedule log
  3. priority classes, deadline-aware admission and starvation freedom proof
  4. structured concurrency scopes with cancellation propagation

Expanded obligations:
  1. Implement work-stealing deques with random-then-round-robin victim
     selection together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement deterministic replay mode with a recorded schedule log as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement priority classes, deadline-aware admission and starvation
     freedom proof, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement structured concurrency scopes with cancellation propagation
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.task.task_runtime@1
  cap.t01.task.task_runtime.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

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
   3. [ 600 lines] Core implementation A - work-stealing deques with random-then-round-robin victim selecti
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deterministic replay mode with a recorded schedule log
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - priority classes, deadline-aware admission and starvation freedo
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - structured concurrency scopes with cancellation propagation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.task.task_runtime@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0015_task_runtime.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0016-dataflow-dag

**P0016 · `dataflow_dag` — Task DAG Representation & Scheduling** · [spec](PART_SPECS_T01.md#p0016-dataflow-dag) · [self-contained txt](../prompts/P0016_dataflow_dag.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0016  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0016 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0016  (16/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Task DAG Representation & Scheduling
file         : parts/t01_foundation/P0016_dataflow_dag.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.dataflow_dag
language     : Python 3.13
capability   : cap.t01.dataflow.dataflow_dag@1
determinism  : pure
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The DAG type that drives 1000-way parallel horizon execution (speed source
S6).

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. immutable DAG builder with cycle detection and critical-path computation
  2. list scheduling with speculative eager start and rollback
  3. resource-constrained scheduling under budget and device limits
  4. DAG diffing for incremental re-execution

Expanded obligations:
  1. Implement immutable DAG builder with cycle detection and critical-path
     computation as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement list scheduling with speculative eager start and rollback, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement resource-constrained scheduling under budget and device limits
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement DAG diffing for incremental re-execution together with its
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.dataflow.dataflow_dag@1
  cap.t01.dataflow.dataflow_dag.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

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
   3. [ 600 lines] Core implementation A - immutable DAG builder with cycle detection and critical-path com
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - list scheduling with speculative eager start and rollback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - resource-constrained scheduling under budget and device limits
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - DAG diffing for incremental re-execution
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.dataflow.dataflow_dag@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0016_dataflow_dag.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0017-fixed-point

**P0017 · `fixed_point` — Certified Fixed-Point & Interval Arithmetic** · [spec](PART_SPECS_T01.md#p0017-fixed-point) · [self-contained txt](../prompts/P0017_fixed_point.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0017  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0017 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0017  (17/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Certified Fixed-Point & Interval Arithmetic
file         : parts/t01_foundation/P0017_fixed_point.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.fixed_point
language     : Python 3.13
capability   : cap.t01.fixed.fixed_point@1
determinism  : pure
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Exact and interval numerics used by verification and certified inference
paths.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. Q-format fixed point with proven bounds and saturation semantics
  2. interval and affine arithmetic with correct outward rounding
  3. error-bound propagation for composed operations
  4. cross-check against arbitrary-precision reference

Expanded obligations:
  1. Implement Q-format fixed point with proven bounds and saturation
     semantics, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement interval and affine arithmetic with correct outward rounding
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement error-bound propagation for composed operations together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement cross-check against arbitrary-precision reference as a
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.fixed.fixed_point@1
  cap.t01.fixed.fixed_point.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

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
   3. [ 600 lines] Core implementation A - Q-format fixed point with proven bounds and saturation semantics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - interval and affine arithmetic with correct outward rounding
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - error-bound propagation for composed operations
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cross-check against arbitrary-precision reference
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.fixed.fixed_point@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0017_fixed_point.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0018-bigint-modmath

**P0018 · `bigint_modmath` — Big Integer & Modular Arithmetic** · [spec](PART_SPECS_T01.md#p0018-bigint-modmath) · [self-contained txt](../prompts/P0018_bigint_modmath.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0018  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0018 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0018  (18/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Big Integer & Modular Arithmetic
file         : parts/t01_foundation/P0018_bigint_modmath.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.bigint_modmath
language     : Python 3.13
capability   : cap.t01.bigint.bigint_modmath@1
determinism  : pure
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Multi-precision integers, modular reduction and NTT used by crypto and exact
reasoning.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. schoolbook/Karatsuba/Toom-Cook thresholds with tuned crossovers
  2. Montgomery and Barrett reduction, constant-time where required
  3. NTT-based multiplication for very large operands
  4. GCD, modular inverse, primality (Miller-Rabin + BPSW)

Expanded obligations:
  1. Implement schoolbook/Karatsuba/Toom-Cook thresholds with tuned
     crossovers with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  2. Implement Montgomery and Barrett reduction, constant-time where required
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement NTT-based multiplication for very large operands as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement GCD, modular inverse, primality (Miller-Rabin + BPSW), and
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.bigint.bigint_modmath@1
  cap.t01.bigint.bigint_modmath.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

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
   3. [ 600 lines] Core implementation A - schoolbook/Karatsuba/Toom-Cook thresholds with tuned crossovers
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - Montgomery and Barrett reduction, constant-time where required
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - NTT-based multiplication for very large operands
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - GCD, modular inverse, primality (Miller-Rabin + BPSW)
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.bigint.bigint_modmath@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0018_bigint_modmath.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0019-bitset-rank

**P0019 · `bitset_rank` — Succinct Bitsets, Rank/Select & Bloom Filters** · [spec](PART_SPECS_T01.md#p0019-bitset-rank) · [self-contained txt](../prompts/P0019_bitset_rank.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0019  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0019 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0019  (19/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Succinct Bitsets, Rank/Select & Bloom Filters
file         : parts/t01_foundation/P0019_bitset_rank.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.bitset_rank
language     : Python 3.13
capability   : cap.t01.bitset.bitset_rank@1
determinism  : pure
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Space-efficient set structures used by routers, caches and retrieval
indexes.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. rank/select with interleaved superblocks and O(1) queries
  2. Roaring-style hybrid containers with adaptive representation
  3. blocked Bloom and cuckoo filters with measured FPR curves
  4. SIMD-friendly population count and set operations

Expanded obligations:
  1. Implement rank/select with interleaved superblocks and O(1) queries
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement Roaring-style hybrid containers with adaptive representation
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement blocked Bloom and cuckoo filters with measured FPR curves, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement SIMD-friendly population count and set operations with an
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.bitset.bitset_rank@1
  cap.t01.bitset.bitset_rank.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

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
   3. [ 600 lines] Core implementation A - rank/select with interleaved superblocks and O(1) queries
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - Roaring-style hybrid containers with adaptive representation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blocked Bloom and cuckoo filters with measured FPR curves
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - SIMD-friendly population count and set operations
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.bitset.bitset_rank@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0019_bitset_rank.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0020-hash-maps

**P0020 · `hash_maps` — High-Performance Hash Containers** · [spec](PART_SPECS_T01.md#p0020-hash-maps) · [self-contained txt](../prompts/P0020_hash_maps.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0020  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0020 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0020  (20/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : High-Performance Hash Containers
file         : parts/t01_foundation/P0020_hash_maps.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.hash_maps
language     : Python 3.13
capability   : cap.t01.hash.hash_maps@1
determinism  : pure
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Open-addressing maps/sets with SIMD probing that back every registry and
cache.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. group-probe (SSE/NEON-style) metadata scanning with tombstone control
  2. seeded hashing with HashDoS resistance
  3. incremental rehashing to avoid latency spikes
  4. concurrent sharded variant with per-shard seqlocks

Expanded obligations:
  1. Implement group-probe (SSE/NEON-style) metadata scanning with tombstone
     control as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement seeded hashing with HashDoS resistance, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement incremental rehashing to avoid latency spikes with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement concurrent sharded variant with per-shard seqlocks together
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.hash.hash_maps@1
  cap.t01.hash.hash_maps.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

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
   3. [ 600 lines] Core implementation A - group-probe (SSE/NEON-style) metadata scanning with tombstone co
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - seeded hashing with HashDoS resistance
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - incremental rehashing to avoid latency spikes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - concurrent sharded variant with per-shard seqlocks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.hash.hash_maps@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0020_hash_maps.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0021-string-interning

**P0021 · `string_interning` — String Interning & Symbol Tables** · [spec](PART_SPECS_T01.md#p0021-string-interning) · [self-contained txt](../prompts/P0021_string_interning.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0021  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0021 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0021  (21/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : String Interning & Symbol Tables
file         : parts/t01_foundation/P0021_string_interning.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.string_interning
language     : Python 3.13
capability   : cap.t01.string.string_interning@1
determinism  : pure
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Global-free symbol interning with stable ids for module, capability and
token names.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. lock-free intern table with generation-stable u32 symbols
  2. prefix-compressed storage and reverse lookup
  3. capability-URI parser producing pre-hashed symbols
  4. collision and exhaustion policies

Expanded obligations:
  1. Implement lock-free intern table with generation-stable u32 symbols, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement prefix-compressed storage and reverse lookup with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement capability-URI parser producing pre-hashed symbols together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement collision and exhaustion policies as a first-class, fully
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.string.string_interning@1
  cap.t01.string.string_interning.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

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
   3. [ 600 lines] Core implementation A - lock-free intern table with generation-stable u32 symbols
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - prefix-compressed storage and reverse lookup
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - capability-URI parser producing pre-hashed symbols
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - collision and exhaustion policies
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.string.string_interning@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0021_string_interning.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0022-arena-graph

**P0022 · `arena_graph` — Generic Graph Store & Algorithms** · [spec](PART_SPECS_T01.md#p0022-arena-graph) · [self-contained txt](../prompts/P0022_arena_graph.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0022  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0022 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0022  (22/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Generic Graph Store & Algorithms
file         : parts/t01_foundation/P0022_arena_graph.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.arena_graph
language     : Python 3.13
capability   : cap.t01.arena.arena_graph@1
determinism  : pure
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
CSR graph storage plus the traversal kernels reused by compiler, memory and
reasoning tiers.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. CSR/CSC build with parallel counting sort
  2. BFS/DFS/SCC/topo-sort/dominator computation
  3. shortest paths (delta-stepping) and min-cut helpers
  4. graph mutation with copy-on-write snapshots

Expanded obligations:
  1. Implement CSR/CSC build with parallel counting sort with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement BFS/DFS/SCC/topo-sort/dominator computation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement shortest paths (delta-stepping) and min-cut helpers as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement graph mutation with copy-on-write snapshots, and make it
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.arena.arena_graph@1
  cap.t01.arena.arena_graph.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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
   3. [ 600 lines] Core implementation A - CSR/CSC build with parallel counting sort
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - BFS/DFS/SCC/topo-sort/dominator computation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - shortest paths (delta-stepping) and min-cut helpers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - graph mutation with copy-on-write snapshots
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.arena.arena_graph@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0022_arena_graph.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0023-serialization-schema

**P0023 · `serialization_schema` — Schema Registry & Evolution Rules** · [spec](PART_SPECS_T01.md#p0023-serialization-schema) · [self-contained txt](../prompts/P0023_serialization_schema.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0023  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0023 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0023  (23/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Schema Registry & Evolution Rules
file         : parts/t01_foundation/P0023_serialization_schema.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.serialization_schema
language     : Python 3.13
capability   : cap.t01.serialization.serialization_schema@1
determinism  : pure
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Machine-readable schemas for every capability, with compatibility checking.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. schema IDL, canonical JSON projection and hash-based schema ids
  2. forward/backward compatibility checker with precise diagnostics
  3. code-generation-free runtime validation with compiled validators
  4. registry snapshot embedding so a part validates offline

Expanded obligations:
  1. Implement schema IDL, canonical JSON projection and hash-based schema
     ids together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement forward/backward compatibility checker with precise
     diagnostics as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement code-generation-free runtime validation with compiled
     validators, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement registry snapshot embedding so a part validates offline with
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.serialization.serialization_schema@1
  cap.t01.serialization.serialization_schema.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

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
   3. [ 600 lines] Core implementation A - schema IDL, canonical JSON projection and hash-based schema ids
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - forward/backward compatibility checker with precise diagnostics
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - code-generation-free runtime validation with compiled validators
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - registry snapshot embedding so a part validates offline
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.serialization.serialization_schema@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0023_serialization_schema.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0024-config-system

**P0024 · `config_system` — Layered Configuration & Feature Flags** · [spec](PART_SPECS_T01.md#p0024-config-system) · [self-contained txt](../prompts/P0024_config_system.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0024  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0024 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0024  (24/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Layered Configuration & Feature Flags
file         : parts/t01_foundation/P0024_config_system.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.config_system
language     : Python 3.13
capability   : cap.t01.config.config_system@1
determinism  : pure
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Deterministic configuration with provenance, validation and hot reload.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. layer merge (defaults < file < env < request) with per-key provenance
  2. typed schema validation and range/unit checks
  3. atomic snapshot swap readable from hot loops without locks
  4. flag lifecycle: default, rollout percentage, kill switch

Expanded obligations:
  1. Implement layer merge (defaults < file < env < request) with per-key
     provenance as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement typed schema validation and range/unit checks, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement atomic snapshot swap readable from hot loops without locks
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement flag lifecycle: default, rollout percentage, kill switch
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.config.config_system@1
  cap.t01.config.config_system.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

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
   3. [ 600 lines] Core implementation A - layer merge (defaults < file < env < request) with per-key prove
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - typed schema validation and range/unit checks
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - atomic snapshot swap readable from hot loops without locks
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - flag lifecycle: default, rollout percentage, kill switch
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.config.config_system@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0024_config_system.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0025-logging-events

**P0025 · `logging_events` — Structured Event Emission Core** · [spec](PART_SPECS_T01.md#p0025-logging-events) · [self-contained txt](../prompts/P0025_logging_events.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0025  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0025 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0025  (25/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Structured Event Emission Core
file         : parts/t01_foundation/P0025_logging_events.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.logging_events
language     : Python 3.13
capability   : cap.t01.logging.logging_events@1
determinism  : pure
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The emit_event pipeline: bounded, lock-free, sampling-aware, never blocking.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-thread ring buffers with a single drain thread
  2. level+code based filtering evaluated before argument formatting
  3. overflow accounting so drops are visible rather than silent
  4. redaction hooks for user content and secrets

Expanded obligations:
  1. Implement per-thread ring buffers with a single drain thread, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement level+code based filtering evaluated before argument
     formatting with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement overflow accounting so drops are visible rather than silent
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement redaction hooks for user content and secrets as a first-class,
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.logging.logging_events@1
  cap.t01.logging.logging_events.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

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
   3. [ 600 lines] Core implementation A - per-thread ring buffers with a single drain thread
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - level+code based filtering evaluated before argument formatting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - overflow accounting so drops are visible rather than silent
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - redaction hooks for user content and secrets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.logging.logging_events@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0025_logging_events.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0026-metrics-core

**P0026 · `metrics_core` — Counters, Gauges & HDR Histograms** · [spec](PART_SPECS_T01.md#p0026-metrics-core) · [self-contained txt](../prompts/P0026_metrics_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0026  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0026 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0026  (26/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Counters, Gauges & HDR Histograms
file         : parts/t01_foundation/P0026_metrics_core.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.metrics_core
language     : Python 3.13
capability   : cap.t01.metrics.metrics_core@1
determinism  : pure
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Numeric telemetry primitives with exact percentiles at nanosecond
resolution.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. striped atomic counters with per-CPU shards
  2. HDR histogram with configurable significant digits and merge
  3. exponentially decaying reservoirs for rate estimation
  4. export snapshot that is allocation-free on the hot path

Expanded obligations:
  1. Implement striped atomic counters with per-CPU shards with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement HDR histogram with configurable significant digits and merge
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement exponentially decaying reservoirs for rate estimation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement export snapshot that is allocation-free on the hot path, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.metrics.metrics_core@1
  cap.t01.metrics.metrics_core.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

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
   3. [ 600 lines] Core implementation A - striped atomic counters with per-CPU shards
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - HDR histogram with configurable significant digits and merge
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - exponentially decaying reservoirs for rate estimation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - export snapshot that is allocation-free on the hot path
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.metrics.metrics_core@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0026_metrics_core.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0027-selftest-harness

**P0027 · `selftest_harness` — In-File Self-Test Framework** · [spec](PART_SPECS_T01.md#p0027-selftest-harness) · [self-contained txt](../prompts/P0027_selftest_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0027  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0027 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0027  (27/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : In-File Self-Test Framework
file         : parts/t01_foundation/P0027_selftest_harness.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.selftest_harness
language     : Python 3.13
capability   : cap.t01.selftest.selftest_harness@1
determinism  : pure
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The tiny test framework every part embeds so tests need no shared fixtures.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. assertion set with structured failure diffs
  2. property-based generator combinators and shrinking
  3. deterministic seed control and failure reproduction strings
  4. SelfTestReport aggregation and machine-readable output

Expanded obligations:
  1. Implement assertion set with structured failure diffs together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement property-based generator combinators and shrinking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement deterministic seed control and failure reproduction strings,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement SelfTestReport aggregation and machine-readable output with an
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.selftest.selftest_harness@1
  cap.t01.selftest.selftest_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

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
   3. [ 600 lines] Core implementation A - assertion set with structured failure diffs
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - property-based generator combinators and shrinking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deterministic seed control and failure reproduction strings
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - SelfTestReport aggregation and machine-readable output
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.selftest.selftest_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0027_selftest_harness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0028-property-gen

**P0028 · `property_gen` — Property Generators & Shrinkers** · [spec](PART_SPECS_T01.md#p0028-property-gen) · [self-contained txt](../prompts/P0028_property_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0028  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0028 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0028  (28/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Property Generators & Shrinkers
file         : parts/t01_foundation/P0028_property_gen.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.property_gen
language     : Python 3.13
capability   : cap.t01.property.property_gen@1
determinism  : pure
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Reusable generators for tensors, graphs, strings, schedules and adversarial
inputs.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. combinator library with size control and coverage feedback
  2. shrinking strategies preserving invariants
  3. domain generators: shapes, dtypes, capability URIs, envelopes
  4. corpus persistence format for regression pinning

Expanded obligations:
  1. Implement combinator library with size control and coverage feedback as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement shrinking strategies preserving invariants, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement domain generators: shapes, dtypes, capability URIs, envelopes
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement corpus persistence format for regression pinning together with
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.property.property_gen@1
  cap.t01.property.property_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

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
   3. [ 600 lines] Core implementation A - combinator library with size control and coverage feedback
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - shrinking strategies preserving invariants
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - domain generators: shapes, dtypes, capability URIs, envelopes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - corpus persistence format for regression pinning
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.property.property_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0028_property_gen.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0029-fuzz-engine

**P0029 · `fuzz_engine` — Coverage-Guided In-Process Fuzzer** · [spec](PART_SPECS_T01.md#p0029-fuzz-engine) · [self-contained txt](../prompts/P0029_fuzz_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0029  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0029 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0029  (29/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Coverage-Guided In-Process Fuzzer
file         : parts/t01_foundation/P0029_fuzz_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.fuzz_engine
language     : Python 3.13
capability   : cap.t01.fuzz.fuzz_engine@1
determinism  : pure
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The fuzzing engine parts use to satisfy the adversarial-test contract
clause.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mutation stack: bitflip, splice, dictionary, structure-aware
  2. in-process coverage feedback via instrumentation shims
  3. crash/hang triage with minimisation
  4. time-boxed budget so it fits the 60 s test limit

Expanded obligations:
  1. Implement mutation stack: bitflip, splice, dictionary, structure-aware,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement in-process coverage feedback via instrumentation shims with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement crash/hang triage with minimisation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement time-boxed budget so it fits the 60 s test limit as a
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.fuzz.fuzz_engine@1
  cap.t01.fuzz.fuzz_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

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
   3. [ 600 lines] Core implementation A - mutation stack: bitflip, splice, dictionary, structure-aware
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - in-process coverage feedback via instrumentation shims
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - crash/hang triage with minimisation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - time-boxed budget so it fits the 60 s test limit
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.fuzz.fuzz_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0029_fuzz_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0030-bench-harness

**P0030 · `bench_harness` — Microbenchmark Harness & Latency Gate** · [spec](PART_SPECS_T01.md#p0030-bench-harness) · [self-contained txt](../prompts/P0030_bench_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0030  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0030 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0030  (30/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Microbenchmark Harness & Latency Gate
file         : parts/t01_foundation/P0030_bench_harness.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.bench_harness
language     : Python 3.13
capability   : cap.t01.bench.bench_harness@1
determinism  : pure
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Statistically sound in-file benchmarking that asserts declared p99 budgets.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. warmup detection, outlier-robust estimation, CI computation
  2. CPU pinning/frequency-noise detection and reporting
  3. regression gate comparing to a checked-in baseline record
  4. BenchReport schema shared by all parts

Expanded obligations:
  1. Implement warmup detection, outlier-robust estimation, CI computation
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement CPU pinning/frequency-noise detection and reporting together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement regression gate comparing to a checked-in baseline record as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement BenchReport schema shared by all parts, and make it correct
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.bench.bench_harness@1
  cap.t01.bench.bench_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

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
   3. [ 600 lines] Core implementation A - warmup detection, outlier-robust estimation, CI computation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - CPU pinning/frequency-noise detection and reporting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regression gate comparing to a checked-in baseline record
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - BenchReport schema shared by all parts
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.bench.bench_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0030_bench_harness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0031-determinism-replay

**P0031 · `determinism_replay` — Record & Replay Engine** · [spec](PART_SPECS_T01.md#p0031-determinism-replay) · [self-contained txt](../prompts/P0031_determinism_replay.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0031  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0031 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0031  (31/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Record & Replay Engine
file         : parts/t01_foundation/P0031_determinism_replay.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.determinism_replay
language     : Python 3.13
capability   : cap.t01.determinism.determinism_replay@1
determinism  : pure
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Records every nondeterminism source so any run can be replayed bit-exactly.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capture of seeds, clocks, schedules, tool results and device order
  2. compact trace format with content-addressed dedup
  3. divergence detector pinpointing the first differing event
  4. replay-under-modification for counterfactual debugging

Expanded obligations:
  1. Implement capture of seeds, clocks, schedules, tool results and device
     order together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement compact trace format with content-addressed dedup as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement divergence detector pinpointing the first differing event, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement replay-under-modification for counterfactual debugging with an
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.determinism.determinism_replay@1
  cap.t01.determinism.determinism_replay.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

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
   3. [ 600 lines] Core implementation A - capture of seeds, clocks, schedules, tool results and device ord
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - compact trace format with content-addressed dedup
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - divergence detector pinpointing the first differing event
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - replay-under-modification for counterfactual debugging
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.determinism.determinism_replay@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0031_determinism_replay.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0032-checksum-verify

**P0032 · `checksum_verify` — Cross-Platform Numeric Equivalence Checker** · [spec](PART_SPECS_T01.md#p0032-checksum-verify) · [self-contained txt](../prompts/P0032_checksum_verify.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0032  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0032 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0032  (32/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Cross-Platform Numeric Equivalence Checker
file         : parts/t01_foundation/P0032_checksum_verify.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.checksum_verify
language     : Python 3.13
capability   : cap.t01.checksum.checksum_verify@1
determinism  : pure
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Proves that a computation is bit-identical across platforms and batch
shapes.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tolerance-free bit comparison plus classified tolerance modes
  2. batch-invariance and thread-count-invariance test drivers
  3. reduction-order pinning helpers
  4. report that localises the first divergent op

Expanded obligations:
  1. Implement tolerance-free bit comparison plus classified tolerance modes
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement batch-invariance and thread-count-invariance test drivers, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement reduction-order pinning helpers with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Correctness here is
     what makes the tier's SWE-bench Verified target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement report that localises the first divergent op together with its
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.checksum.checksum_verify@1
  cap.t01.checksum.checksum_verify.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

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
   3. [ 600 lines] Core implementation A - tolerance-free bit comparison plus classified tolerance modes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - batch-invariance and thread-count-invariance test drivers
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reduction-order pinning helpers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - report that localises the first divergent op
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.checksum.checksum_verify@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0032_checksum_verify.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0033-capability-gate

**P0033 · `capability_gate` — Capability Acquisition Policy & Fallbacks** · [spec](PART_SPECS_T01.md#p0033-capability-gate) · [self-contained txt](../prompts/P0033_capability_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0033  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0033 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0033  (33/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Capability Acquisition Policy & Fallbacks
file         : parts/t01_foundation/P0033_capability_gate.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.capability_gate
language     : Python 3.13
capability   : cap.t01.capability.capability_gate@1
determinism  : pure
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Policy layer over the bus: allowlists, quotas, degradation ladders.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. per-caller capability allowlists with deny-by-default option
  2. quota and rate limiting per capability and per trace
  3. declared degradation ladder execution with quality annotation
  4. audit record for every acquisition decision

Expanded obligations:
  1. Implement per-caller capability allowlists with deny-by-default option,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement quota and rate limiting per capability and per trace with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement declared degradation ladder execution with quality annotation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement audit record for every acquisition decision as a first-class,
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.capability.capability_gate@1
  cap.t01.capability.capability_gate.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

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
   3. [ 600 lines] Core implementation A - per-caller capability allowlists with deny-by-default option
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quota and rate limiting per capability and per trace
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - declared degradation ladder execution with quality annotation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - audit record for every acquisition decision
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.capability.capability_gate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0033_capability_gate.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0034-version-semver

**P0034 · `version_semver` — Semantic Version & Compatibility Engine** · [spec](PART_SPECS_T01.md#p0034-version-semver) · [self-contained txt](../prompts/P0034_version_semver.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0034  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0034 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0034  (34/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Semantic Version & Compatibility Engine
file         : parts/t01_foundation/P0034_version_semver.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.version_semver
language     : Python 3.13
capability   : cap.t01.version.version_semver@1
determinism  : pure
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Version parsing, range solving and the link-time compatibility matrix.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. semver parse/compare with prerelease ordering
  2. range solver for the 1000-part dependency set
  3. breaking-change detector across schema snapshots
  4. diagnostic output naming the exact conflicting parts

Expanded obligations:
  1. Implement semver parse/compare with prerelease ordering with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement range solver for the 1000-part dependency set together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement breaking-change detector across schema snapshots as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement diagnostic output naming the exact conflicting parts, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
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
  cap.t01.version.version_semver@1
  cap.t01.version.version_semver.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

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
   3. [ 600 lines] Core implementation A - semver parse/compare with prerelease ordering
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - range solver for the 1000-part dependency set
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - breaking-change detector across schema snapshots
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - diagnostic output naming the exact conflicting parts
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.version.version_semver@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0034_version_semver.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0035-link-validator

**P0035 · `link_validator` — Static Link Validator for 1000 Parts** · [spec](PART_SPECS_T01.md#p0035-link-validator) · [self-contained txt](../prompts/P0035_link_validator.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0035  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0035 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0035  (35/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Static Link Validator for 1000 Parts
file         : parts/t01_foundation/P0035_link_validator.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.link_validator
language     : Python 3.13
capability   : cap.t01.link.link_validator@1
determinism  : pure
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Validates the whole assembly: every requires resolved, no cycles, no
duplicate provides.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. manifest ingestion and normalisation from all 1000 files
  2. duplicate/ambiguous provider detection with resolution hints
  3. cycle detection with minimal counterexample path
  4. assembly report artifact consumed by the platform tier

Expanded obligations:
  1. Implement manifest ingestion and normalisation from all 1000 files
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement duplicate/ambiguous provider detection with resolution hints
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement cycle detection with minimal counterexample path, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement assembly report artifact consumed by the platform tier with an
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.link.link_validator@1
  cap.t01.link.link_validator.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

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
   3. [ 600 lines] Core implementation A - manifest ingestion and normalisation from all 1000 files
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - duplicate/ambiguous provider detection with resolution hints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cycle detection with minimal counterexample path
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - assembly report artifact consumed by the platform tier
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.link.link_validator@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0035_link_validator.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0036-manifest-parser

**P0036 · `manifest_parser` — PART_MANIFEST Parser & Validator** · [spec](PART_SPECS_T01.md#p0036-manifest-parser) · [self-contained txt](../prompts/P0036_manifest_parser.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0036  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0036 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0036  (36/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : PART_MANIFEST Parser & Validator
file         : parts/t01_foundation/P0036_manifest_parser.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.manifest_parser
language     : Python 3.13
capability   : cap.t01.manifest.manifest_parser@1
determinism  : pure
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Extracts and validates manifests from source files in any of the three
languages.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. language-agnostic extraction with tolerant parsing
  2. field-level validation, URI syntax, budget sanity checks
  3. digest check for the frozen contract header
  4. batch report over 1000 files in under a second

Expanded obligations:
  1. Implement language-agnostic extraction with tolerant parsing as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement field-level validation, URI syntax, budget sanity checks, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement digest check for the frozen contract header with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement batch report over 1000 files in under a second together with
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.manifest.manifest_parser@1
  cap.t01.manifest.manifest_parser.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

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
   3. [ 600 lines] Core implementation A - language-agnostic extraction with tolerant parsing
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - field-level validation, URI syntax, budget sanity checks
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - digest check for the frozen contract header
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - batch report over 1000 files in under a second
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.manifest.manifest_parser@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0036_manifest_parser.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0037-abi-stability

**P0037 · `abi_stability` — ABI Stability & Frozen-Symbol Guard** · [spec](PART_SPECS_T01.md#p0037-abi-stability) · [self-contained txt](../prompts/P0037_abi_stability.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0037  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0037 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0037  (37/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : ABI Stability & Frozen-Symbol Guard
file         : parts/t01_foundation/P0037_abi_stability.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.abi_stability
language     : Python 3.13
capability   : cap.t01.abi.abi_stability@1
determinism  : pure
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Detects any change that would break already-written parts.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. symbol inventory snapshot with signature hashes
  2. additive-only enforcement for frozen namespaces
  3. deprecation ladder with compile-time warnings
  4. waiver file with expiry dates and owners

Expanded obligations:
  1. Implement symbol inventory snapshot with signature hashes, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement additive-only enforcement for frozen namespaces with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement deprecation ladder with compile-time warnings together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement waiver file with expiry dates and owners as a first-class,
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.abi.abi_stability@1
  cap.t01.abi.abi_stability.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

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
   3. [ 600 lines] Core implementation A - symbol inventory snapshot with signature hashes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - additive-only enforcement for frozen namespaces
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deprecation ladder with compile-time warnings
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - waiver file with expiry dates and owners
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.abi.abi_stability@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0037_abi_stability.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0038-compat-shims

**P0038 · `compat_shims` — Cross-Language Interop Shims** · [spec](PART_SPECS_T01.md#p0038-compat-shims) · [self-contained txt](../prompts/P0038_compat_shims.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0038  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0038 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0038  (38/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Cross-Language Interop Shims
file         : parts/t01_foundation/P0038_compat_shims.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.compat_shims
language     : Python 3.13
capability   : cap.t01.compat.compat_shims@1
determinism  : pure
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Uniform FFI surface so Python, Rust and TypeScript parts share the same ABI.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. C-ABI boundary definition with ownership rules
  2. buffer protocol bridging without copies
  3. error mapping across language boundaries preserving cause chains
  4. async bridging with cancellation propagation

Expanded obligations:
  1. Implement C-ABI boundary definition with ownership rules with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement buffer protocol bridging without copies together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement error mapping across language boundaries preserving cause
     chains as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement async bridging with cancellation propagation, and make it
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
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.compat.compat_shims@1
  cap.t01.compat.compat_shims.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

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
   3. [ 600 lines] Core implementation A - C-ABI boundary definition with ownership rules
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - buffer protocol bridging without copies
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - error mapping across language boundaries preserving cause chains
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - async bridging with cancellation propagation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.compat.compat_shims@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0038_compat_shims.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0039-numeric-limits

**P0039 · `numeric_limits` — Numeric Policy, Rounding & Overflow Rules** · [spec](PART_SPECS_T01.md#p0039-numeric-limits) · [self-contained txt](../prompts/P0039_numeric_limits.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0039  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0039 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0039  (39/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Numeric Policy, Rounding & Overflow Rules
file         : parts/t01_foundation/P0039_numeric_limits.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.numeric_limits
language     : Python 3.13
capability   : cap.t01.numeric.numeric_limits@1
determinism  : pure
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
One policy for how every kernel handles rounding, denormals, NaN and
overflow.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. policy objects selecting round mode, denormal handling, FMA use
  2. NaN/Inf propagation contract and quiet/signalling rules
  3. overflow detection strategies per dtype and per op class
  4. conformance suite that all kernels must pass

Expanded obligations:
  1. Implement policy objects selecting round mode, denormal handling, FMA
     use together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement NaN/Inf propagation contract and quiet/signalling rules as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement overflow detection strategies per dtype and per op class, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement conformance suite that all kernels must pass with an explicit
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.numeric.numeric_limits@1
  cap.t01.numeric.numeric_limits.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

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
   3. [ 600 lines] Core implementation A - policy objects selecting round mode, denormal handling, FMA use
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - NaN/Inf propagation contract and quiet/signalling rules
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - overflow detection strategies per dtype and per op class
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - conformance suite that all kernels must pass
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.numeric.numeric_limits@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0039_numeric_limits.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0040-unit-dimensions

**P0040 · `unit_dimensions` — Physical Units & Dimensional Analysis** · [spec](PART_SPECS_T01.md#p0040-unit-dimensions) · [self-contained txt](../prompts/P0040_unit_dimensions.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0040  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0040 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0040  (40/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Physical Units & Dimensional Analysis
file         : parts/t01_foundation/P0040_unit_dimensions.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.unit_dimensions
language     : Python 3.13
capability   : cap.t01.unit.unit_dimensions@1
determinism  : pure
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Compile-time dimension checking used by science, engineering and cost
accounting.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dimension vectors with compile-time (or checked) arithmetic
  2. unit conversion with exact rationals to avoid drift
  3. quantity type that refuses invalid operations
  4. cost/energy/token units treated as first-class dimensions

Expanded obligations:
  1. Implement dimension vectors with compile-time (or checked) arithmetic as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement unit conversion with exact rationals to avoid drift, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement quantity type that refuses invalid operations with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement cost/energy/token units treated as first-class dimensions
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.unit.unit_dimensions@1
  cap.t01.unit.unit_dimensions.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

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
   3. [ 600 lines] Core implementation A - dimension vectors with compile-time (or checked) arithmetic
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - unit conversion with exact rationals to avoid drift
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quantity type that refuses invalid operations
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost/energy/token units treated as first-class dimensions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.unit.unit_dimensions@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0040_unit_dimensions.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0041-budget-ledger

**P0041 · `budget_ledger` — Token / FLOP / Dollar Budget Ledger** · [spec](PART_SPECS_T01.md#p0041-budget-ledger) · [self-contained txt](../prompts/P0041_budget_ledger.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0041  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0041 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0041  (41/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Token / FLOP / Dollar Budget Ledger
file         : parts/t01_foundation/P0041_budget_ledger.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.budget_ledger
language     : Python 3.13
capability   : cap.t01.budget.budget_ledger@1
determinism  : pure
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
The accounting system that makes 'faster and cheaper' measurable and
enforced.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hierarchical budget reservation with parent-child rollup
  2. atomic spend with overspend rejection and partial-result signalling
  3. conversion table between tokens, FLOPs, joules and micro-dollars
  4. postmortem attribution report per part and per span

Expanded obligations:
  1. Implement hierarchical budget reservation with parent-child rollup, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Verified, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement atomic spend with overspend rejection and partial-result
     signalling with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against SWE-bench Verified —
     a regression on that benchmark is an automatic rejection of this part.
  3. Implement conversion table between tokens, FLOPs, joules and
     micro-dollars together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement postmortem attribution report per part and per span as a
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
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.budget.budget_ledger@1
  cap.t01.budget.budget_ledger.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

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
   3. [ 600 lines] Core implementation A - hierarchical budget reservation with parent-child rollup
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - atomic spend with overspend rejection and partial-result signall
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conversion table between tokens, FLOPs, joules and micro-dollars
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - postmortem attribution report per part and per span
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.budget.budget_ledger@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0041_budget_ledger.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0042-rate-limiter

**P0042 · `rate_limiter` — Deterministic Rate Limiting & Admission** · [spec](PART_SPECS_T01.md#p0042-rate-limiter) · [self-contained txt](../prompts/P0042_rate_limiter.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0042  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0042 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0042  (42/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Deterministic Rate Limiting & Admission
file         : parts/t01_foundation/P0042_rate_limiter.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.rate_limiter
language     : Python 3.13
capability   : cap.t01.rate.rate_limiter@1
determinism  : pure
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Token buckets, GCRA and concurrency limiters with deterministic behaviour.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. GCRA with monotonic-clock precision and no drift
  2. hierarchical buckets for nested resource classes
  3. concurrency limiter with latency-target auto-tuning
  4. fair queueing across 1000 concurrent callers

Expanded obligations:
  1. Implement GCRA with monotonic-clock precision and no drift with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement hierarchical buckets for nested resource classes together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement concurrency limiter with latency-target auto-tuning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement fair queueing across 1000 concurrent callers, and make it
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.rate.rate_limiter@1
  cap.t01.rate.rate_limiter.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

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
   3. [ 600 lines] Core implementation A - GCRA with monotonic-clock precision and no drift
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hierarchical buckets for nested resource classes
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - concurrency limiter with latency-target auto-tuning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fair queueing across 1000 concurrent callers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.rate.rate_limiter@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0042_rate_limiter.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0043-circuit-breaker

**P0043 · `circuit_breaker` — Failure Isolation & Circuit Breaking** · [spec](PART_SPECS_T01.md#p0043-circuit-breaker) · [self-contained txt](../prompts/P0043_circuit_breaker.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0043  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0043 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0043  (43/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Failure Isolation & Circuit Breaking
file         : parts/t01_foundation/P0043_circuit_breaker.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.circuit_breaker
language     : Python 3.13
capability   : cap.t01.circuit.circuit_breaker@1
determinism  : pure
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Prevents one failing part from degrading the 1000-part assembly.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. rolling-window failure statistics with EWMA and quantiles
  2. half-open probing with jittered recovery
  3. bulkhead isolation pools per capability
  4. outlier ejection driven by comparative latency

Expanded obligations:
  1. Implement rolling-window failure statistics with EWMA and quantiles
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement half-open probing with jittered recovery as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of SWE-bench
     Verified, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement bulkhead isolation pools per capability, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement outlier ejection driven by comparative latency with an
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.circuit.circuit_breaker@1
  cap.t01.circuit.circuit_breaker.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

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
   3. [ 600 lines] Core implementation A - rolling-window failure statistics with EWMA and quantiles
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - half-open probing with jittered recovery
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - bulkhead isolation pools per capability
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - outlier ejection driven by comparative latency
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.circuit.circuit_breaker@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0043_circuit_breaker.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0044-retry-idempotency

**P0044 · `retry_idempotency` — Retry, Idempotency & Exactly-Once Effects** · [spec](PART_SPECS_T01.md#p0044-retry-idempotency) · [self-contained txt](../prompts/P0044_retry_idempotency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0044  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0044 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0044  (44/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Retry, Idempotency & Exactly-Once Effects
file         : parts/t01_foundation/P0044_retry_idempotency.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.retry_idempotency
language     : Python 3.13
capability   : cap.t01.retry.retry_idempotency@1
determinism  : pure
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Safe retries for tool calls and side-effecting actions.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. idempotency keys with content-derived derivation
  2. effect log with commit/abort and fencing tokens
  3. at-most-once wrapper for irreversible actions
  4. duplicate-suppression window with bounded memory

Expanded obligations:
  1. Implement idempotency keys with content-derived derivation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement effect log with commit/abort and fencing tokens, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Verified — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement at-most-once wrapper for irreversible actions with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement duplicate-suppression window with bounded memory together with
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.retry.retry_idempotency@1
  cap.t01.retry.retry_idempotency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

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
   3. [ 600 lines] Core implementation A - idempotency keys with content-derived derivation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - effect log with commit/abort and fencing tokens
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - at-most-once wrapper for irreversible actions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - duplicate-suppression window with bounded memory
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.retry.retry_idempotency@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0044_retry_idempotency.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0045-secure-zeroize

**P0045 · `secure_zeroize` — Secret Handling & Memory Hygiene** · [spec](PART_SPECS_T01.md#p0045-secure-zeroize) · [self-contained txt](../prompts/P0045_secure_zeroize.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0045  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0045 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0045  (45/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Secret Handling & Memory Hygiene
file         : parts/t01_foundation/P0045_secure_zeroize.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.secure_zeroize
language     : Python 3.13
capability   : cap.t01.secure.secure_zeroize@1
determinism  : pure
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Secrets, key material and user content lifetimes.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. zeroize-on-drop buffers resistant to optimisation removal
  2. mlock/no-swap regions and core-dump exclusion
  3. constant-time comparison and branch-free selection helpers
  4. taint tracking so secrets cannot enter logs or prompts

Expanded obligations:
  1. Implement zeroize-on-drop buffers resistant to optimisation removal, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement mlock/no-swap regions and core-dump exclusion with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's SWE-bench Verified target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement constant-time comparison and branch-free selection helpers
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of SWE-bench Verified, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement taint tracking so secrets cannot enter logs or prompts as a
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
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.secure.secure_zeroize@1
  cap.t01.secure.secure_zeroize.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

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
   3. [ 600 lines] Core implementation A - zeroize-on-drop buffers resistant to optimisation removal
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - mlock/no-swap regions and core-dump exclusion
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - constant-time comparison and branch-free selection helpers
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - taint tracking so secrets cannot enter logs or prompts
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.secure.secure_zeroize@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0045_secure_zeroize.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0046-sandbox-policy

**P0046 · `sandbox_policy` — Process Sandbox & Syscall Policy Descriptors** · [spec](PART_SPECS_T01.md#p0046-sandbox-policy) · [self-contained txt](../prompts/P0046_sandbox_policy.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0046  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0046 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0046  (46/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Process Sandbox & Syscall Policy Descriptors
file         : parts/t01_foundation/P0046_sandbox_policy.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.sandbox_policy
language     : Python 3.13
capability   : cap.t01.sandbox.sandbox_policy@1
determinism  : pure
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Declarative sandbox profiles that agent and tool parts execute under.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capability-to-syscall mapping with deny-by-default profiles
  2. filesystem and network allowlist descriptors
  3. resource rlimits, cgroup descriptors and OOM policy
  4. profile verification tests that assert denied operations fail

Expanded obligations:
  1. Implement capability-to-syscall mapping with deny-by-default profiles
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement filesystem and network allowlist descriptors together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement resource rlimits, cgroup descriptors and OOM policy as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement profile verification tests that assert denied operations fail,
     and make it correct under concurrency: at least 64 in-flight
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.sandbox.sandbox_policy@1
  cap.t01.sandbox.sandbox_policy.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

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
   3. [ 600 lines] Core implementation A - capability-to-syscall mapping with deny-by-default profiles
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - filesystem and network allowlist descriptors
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - resource rlimits, cgroup descriptors and OOM policy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - profile verification tests that assert denied operations fail
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.sandbox.sandbox_policy@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0046_sandbox_policy.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0047-fs-atomic

**P0047 · `fs_atomic` — Atomic Filesystem & Content-Addressed Store** · [spec](PART_SPECS_T01.md#p0047-fs-atomic) · [self-contained txt](../prompts/P0047_fs_atomic.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0047  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0047 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0047  (47/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Atomic Filesystem & Content-Addressed Store
file         : parts/t01_foundation/P0047_fs_atomic.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.fs_atomic
language     : Python 3.13
capability   : cap.t01.fs.fs_atomic@1
determinism  : pure
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Crash-safe artifact storage used for caches, traces and model shards.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. write-temp-fsync-rename with directory fsync ordering
  2. content-addressed layout with hardlink dedup and GC
  3. lock files with stale-owner detection
  4. corruption detection and self-healing repair pass

Expanded obligations:
  1. Implement write-temp-fsync-rename with directory fsync ordering together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement content-addressed layout with hardlink dedup and GC as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement lock files with stale-owner detection, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement corruption detection and self-healing repair pass with an
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.fs.fs_atomic@1
  cap.t01.fs.fs_atomic.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

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
   3. [ 600 lines] Core implementation A - write-temp-fsync-rename with directory fsync ordering
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - content-addressed layout with hardlink dedup and GC
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - lock files with stale-owner detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - corruption detection and self-healing repair pass
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.fs.fs_atomic@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0047_fs_atomic.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0048-compression

**P0048 · `compression` — Streaming Compression & Delta Encoding** · [spec](PART_SPECS_T01.md#p0048-compression) · [self-contained txt](../prompts/P0048_compression.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0048  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0048 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0048  (48/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Streaming Compression & Delta Encoding
file         : parts/t01_foundation/P0048_compression.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.compression
language     : Python 3.13
capability   : cap.t01.compression.compression@1
determinism  : pure
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Compression primitives for KV caches, traces and artifacts.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. LZ77-family streaming codec with dictionary support
  2. delta encoding for near-duplicate tensors and texts
  3. entropy coder (rANS) with speed/ratio presets
  4. throughput/ratio benchmark matrix used for policy selection

Expanded obligations:
  1. Implement LZ77-family streaming codec with dictionary support as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement delta encoding for near-duplicate tensors and texts, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement entropy coder (rANS) with speed/ratio presets with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement throughput/ratio benchmark matrix used for policy selection
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.compression.compression@1
  cap.t01.compression.compression.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

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
   3. [ 600 lines] Core implementation A - LZ77-family streaming codec with dictionary support
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - delta encoding for near-duplicate tensors and texts
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - entropy coder (rANS) with speed/ratio presets
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput/ratio benchmark matrix used for policy selection
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.compression.compression@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0048_compression.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0049-bootstrap-init

**P0049 · `bootstrap_init` — Assembly Bootstrap & Startup Ordering** · [spec](PART_SPECS_T01.md#p0049-bootstrap-init) · [self-contained txt](../prompts/P0049_bootstrap_init.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0049  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0049 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0049  (49/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Assembly Bootstrap & Startup Ordering
file         : parts/t01_foundation/P0049_bootstrap_init.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.bootstrap_init
language     : Python 3.13
capability   : cap.t01.bootstrap.bootstrap_init@1
determinism  : pure
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Brings the 1000 parts up in a correct, fast, observable order.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dependency-ordered register() invocation with parallel waves
  2. readiness/liveness state machine per part
  3. lazy-initialisation policy for cold capabilities
  4. startup latency budget with per-part attribution

Expanded obligations:
  1. Implement dependency-ordered register() invocation with parallel waves,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Verified target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement readiness/liveness state machine per part with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of SWE-bench Verified, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement lazy-initialisation policy for cold capabilities together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement startup latency budget with per-part attribution as a
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.bootstrap.bootstrap_init@1
  cap.t01.bootstrap.bootstrap_init.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

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
   3. [ 600 lines] Core implementation A - dependency-ordered register() invocation with parallel waves
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - readiness/liveness state machine per part
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - lazy-initialisation policy for cold capabilities
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - startup latency budget with per-part attribution
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.bootstrap.bootstrap_init@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0049_bootstrap_init.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0050-shutdown-drain

**P0050 · `shutdown_drain` — Graceful Drain & Crash-Consistency** · [spec](PART_SPECS_T01.md#p0050-shutdown-drain) · [self-contained txt](../prompts/P0050_shutdown_drain.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0050  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0050 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0050  (50/50 of tier T01)
tier         : T01 — Foundation, ABI & Determinism
title        : Graceful Drain & Crash-Consistency
file         : parts/t01_foundation/P0050_shutdown_drain.py          <-- create exactly this path, nothing else
module       : hyperion.t01.foundation.shutdown_drain
language     : Python 3.13
capability   : cap.t01.shutdown.shutdown_drain@1
determinism  : pure
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified

MISSION
-------
Deterministic teardown that never loses an in-flight envelope.

Tier context:
  Frozen type system, capability ABI, deterministic primitives and the Ω-Bus
  reference semantics that every other part links against.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. drain phases: stop-admit, finish-inflight, flush, release
  2. deadline-bounded drain with forced-abort accounting
  3. crash-consistency invariants and recovery replay
  4. shutdown correctness tests under injected faults

Expanded obligations:
  1. Implement drain phases: stop-admit, finish-inflight, flush, release with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement deadline-bounded drain with forced-abort accounting together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement crash-consistency invariants and recovery replay as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement shutdown correctness tests under injected faults, and make it
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t01.shutdown.shutdown_drain@1
  cap.t01.shutdown.shutdown_drain.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

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
   3. [ 600 lines] Core implementation A - drain phases: stop-admit, finish-inflight, flush, release
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deadline-bounded drain with forced-abort accounting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - crash-consistency invariants and recovery replay
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - shutdown correctness tests under injected faults
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t01.shutdown.shutdown_drain@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t01_foundation/P0050_shutdown_drain.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
