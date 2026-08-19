# HYPERION-Ω — Worker prompts · T12 · Code Intelligence & Repository Surgery

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

## PROMPT p0551-repo-index

**P0551 · `repo_index` — Whole-Repository Semantic Index** · [spec](PART_SPECS_T12.md#p0551-repo-index) · [self-contained txt](../prompts/P0551_repo_index.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0551  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0551 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0551  (1/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Whole-Repository Semantic Index
file         : parts/t12_code/P0551_repo_index.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.repo_index
language     : Python 3.13
capability   : cap.t12.repo.repo_index@1
determinism  : pure
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Understands a million-file repository as one coherent object.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. incremental multi-language index of symbols, types, references and call graphs
  2. build-system-aware target and dependency extraction
  3. index freshness under concurrent edits with sub-second updates
  4. indexing throughput and query-latency budgets on large monorepos

Expanded obligations:
  1. Implement incremental multi-language index of symbols, types, references
     and call graphs together with its verification path, so that anything
     this mechanism produces can be independently re-checked *inside this
     same file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of FrontierCode
     Diamond, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement build-system-aware target and dependency extraction as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement index freshness under concurrent edits with sub-second
     updates, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement indexing throughput and query-latency budgets on large
     monorepos with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.repo.repo_index@1
  cap.t12.repo.repo_index.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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

  cap.t10.numeric.numeric_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `numeric_reasoning` (documented, slower, lower quality) and set
      `degraded['numeric_reasoning']='local'`

  cap.t11.spec.spec_language@1
      if unavailable: use the in-file conservative substitute for
      `spec_language` (documented, slower, lower quality) and set
      `degraded['spec_language']='local'`

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
   3. [ 600 lines] Core implementation A - incremental multi-language index of symbols, types, references a
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - build-system-aware target and dependency extraction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - index freshness under concurrent edits with sub-second updates
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - indexing throughput and query-latency budgets on large monorepos
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.repo.repo_index@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0551_repo_index.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0552-code-parsing

**P0552 · `code_parsing` — Multi-Language Parsing & Concrete Syntax Trees** · [spec](PART_SPECS_T12.md#p0552-code-parsing) · [self-contained txt](../prompts/P0552_code_parsing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0552  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0552 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0552  (2/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Multi-Language Parsing & Concrete Syntax Trees
file         : parts/t12_code/P0552_code_parsing.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_parsing
language     : Python 3.13
capability   : cap.t12.code.code_parsing@1
determinism  : pure
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Exact, error-tolerant parsing for 40+ languages.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. error-recovering parsers producing full-fidelity trees with trivia
  2. incremental reparse of edited regions only
  3. round-trip guarantee (parse then print equals original bytes)
  4. conformance testing against language test suites

Expanded obligations:
  1. Implement error-recovering parsers producing full-fidelity trees with
     trivia as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement incremental reparse of edited regions only, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement round-trip guarantee (parse then print equals original bytes)
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement conformance testing against language test suites together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.code.code_parsing@1
  cap.t12.code.code_parsing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.repo.repo_index@1
      if unavailable: use the in-file conservative substitute for
      `repo_index` (documented, slower, lower quality) and set
      `degraded['repo_index']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t10.backtracking.backtracking@1
      if unavailable: use the in-file conservative substitute for
      `backtracking` (documented, slower, lower quality) and set
      `degraded['backtracking']='local'`

  cap.t11.verified.verified_kernels@1
      if unavailable: use the in-file conservative substitute for
      `verified_kernels` (documented, slower, lower quality) and set
      `degraded['verified_kernels']='local'`

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
   3. [ 600 lines] Core implementation A - error-recovering parsers producing full-fidelity trees with triv
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - incremental reparse of edited regions only
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - round-trip guarantee (parse then print equals original bytes)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - conformance testing against language test suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_parsing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0552_code_parsing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0553-semantic-analysis

**P0553 · `semantic_analysis` — Cross-Language Semantic Analysis** · [spec](PART_SPECS_T12.md#p0553-semantic-analysis) · [self-contained txt](../prompts/P0553_semantic_analysis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0553  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0553 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0553  (3/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Cross-Language Semantic Analysis
file         : parts/t12_code/P0553_semantic_analysis.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.semantic_analysis
language     : Python 3.13
capability   : cap.t12.semantic.semantic_analysis@1
determinism  : pure
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Types, scopes, effects and data flow, computed not guessed.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. scope and binding resolution with language-specific rules
  2. type inference/checking integration with existing compilers
  3. data-flow and taint analysis across function boundaries
  4. accuracy measurement against compiler ground truth

Expanded obligations:
  1. Implement scope and binding resolution with language-specific rules, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement type inference/checking integration with existing compilers
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement data-flow and taint analysis across function boundaries
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against FrontierCode Diamond — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement accuracy measurement against compiler ground truth as a
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.semantic.semantic_analysis@1
  cap.t12.semantic.semantic_analysis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_parsing@1
      if unavailable: use the in-file conservative substitute for
      `code_parsing` (documented, slower, lower quality) and set
      `degraded['code_parsing']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t10.question.question_asking@1
      if unavailable: use the in-file conservative substitute for
      `question_asking` (documented, slower, lower quality) and set
      `degraded['question_asking']='local'`

  cap.t11.proof.proof_of_work_bounds@1
      if unavailable: use the in-file conservative substitute for
      `proof_of_work_bounds` (documented, slower, lower quality) and set
      `degraded['proof_of_work_bounds']='local'`

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
   3. [ 600 lines] Core implementation A - scope and binding resolution with language-specific rules
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - type inference/checking integration with existing compilers
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - data-flow and taint analysis across function boundaries
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy measurement against compiler ground truth
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.semantic.semantic_analysis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0553_semantic_analysis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0554-call-graph

**P0554 · `call_graph` — Call Graph & Dependency Analysis** · [spec](PART_SPECS_T12.md#p0554-call-graph) · [self-contained txt](../prompts/P0554_call_graph.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0554  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0554 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0554  (4/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Call Graph & Dependency Analysis
file         : parts/t12_code/P0554_call_graph.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.call_graph
language     : Python 3.13
capability   : cap.t12.call.call_graph@1
determinism  : pure
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Knows what calls what, including through dynamic dispatch.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. static call graph with virtual/dynamic dispatch resolution
  2. dynamic-trace-informed graph refinement
  3. reachability, impact and blast-radius queries
  4. precision/recall measurement against runtime traces

Expanded obligations:
  1. Implement static call graph with virtual/dynamic dispatch resolution
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement dynamic-trace-informed graph refinement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement reachability, impact and blast-radius queries as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement precision/recall measurement against runtime traces, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Pro, so its p99
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.call.call_graph@1
  cap.t12.call.call_graph.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.semantic.semantic_analysis@1
      if unavailable: use the in-file conservative substitute for
      `semantic_analysis` (documented, slower, lower quality) and set
      `degraded['semantic_analysis']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t10.scratchpad.scratchpad_manager@1
      if unavailable: use the in-file conservative substitute for
      `scratchpad_manager` (documented, slower, lower quality) and set
      `degraded['scratchpad_manager']='local'`

  cap.t11.math.math_benchmark_formal@1
      if unavailable: use the in-file conservative substitute for
      `math_benchmark_formal` (documented, slower, lower quality) and set
      `degraded['math_benchmark_formal']='local'`

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
   3. [ 600 lines] Core implementation A - static call graph with virtual/dynamic dispatch resolution
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - dynamic-trace-informed graph refinement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reachability, impact and blast-radius queries
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - precision/recall measurement against runtime traces
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.call.call_graph@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0554_call_graph.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0555-code-search

**P0555 · `code_search` — Semantic & Structural Code Search** · [spec](PART_SPECS_T12.md#p0555-code-search) · [self-contained txt](../prompts/P0555_code_search.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0555  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0555 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0555  (5/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Semantic & Structural Code Search
file         : parts/t12_code/P0555_code_search.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_search
language     : Python 3.13
capability   : cap.t12.code.code_search@1
determinism  : pure
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Finds the right code by meaning, structure or behaviour.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structural pattern queries (AST/tree-sitter-style) with variables
  2. semantic search over code embeddings
  3. behavioural search (find functions with this input/output relation)
  4. search-quality measurement on curated developer queries

Expanded obligations:
  1. Implement structural pattern queries (AST/tree-sitter-style) with
     variables together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against FrontierCode Diamond
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement semantic search over code embeddings as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement behavioural search (find functions with this input/output
     relation), and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement search-quality measurement on curated developer queries with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Frontier-Bench v0.1 — a regression
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
  cap.t12.code.code_search@1
  cap.t12.code.code_search.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.call.call_graph@1
      if unavailable: use the in-file conservative substitute for
      `call_graph` (documented, slower, lower quality) and set
      `degraded['call_graph']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t10.reasoning.reasoning_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_speed_proof` (documented, slower, lower quality) and set
      `degraded['reasoning_speed_proof']='local'`

  cap.t11.proof.proof_speed@1
      if unavailable: use the in-file conservative substitute for
      `proof_speed` (documented, slower, lower quality) and set
      `degraded['proof_speed']='local'`

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
   3. [ 600 lines] Core implementation A - structural pattern queries (AST/tree-sitter-style) with variable
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - semantic search over code embeddings
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - behavioural search (find functions with this input/output relati
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - search-quality measurement on curated developer queries
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_search@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0555_code_search.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0556-code-embeddings

**P0556 · `code_embeddings` — Code Representation & Embeddings** · [spec](PART_SPECS_T12.md#p0556-code-embeddings) · [self-contained txt](../prompts/P0556_code_embeddings.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0556  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0556 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0556  (6/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Code Representation & Embeddings
file         : parts/t12_code/P0556_code_embeddings.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_embeddings
language     : Python 3.13
capability   : cap.t12.code.code_embeddings@1
determinism  : pure
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Representations that capture what code does, not how it looks.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structure-aware code embedding training and evaluation
  2. cross-language semantic alignment (same algorithm, different language)
  3. clone and near-clone detection accuracy
  4. retrieval quality on code-search benchmarks

Expanded obligations:
  1. Implement structure-aware code embedding training and evaluation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement cross-language semantic alignment (same algorithm, different
     language), and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement clone and near-clone detection accuracy with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement retrieval quality on code-search benchmarks together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
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
  cap.t12.code.code_embeddings@1
  cap.t12.code.code_embeddings.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_search@1
      if unavailable: use the in-file conservative substitute for
      `code_search` (documented, slower, lower quality) and set
      `degraded['code_search']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t10.process.process_verifier@1
      if unavailable: use the in-file conservative substitute for
      `process_verifier` (documented, slower, lower quality) and set
      `degraded['process_verifier']='local'`

  cap.t11.premise.premise_selection@1
      if unavailable: use the in-file conservative substitute for
      `premise_selection` (documented, slower, lower quality) and set
      `degraded['premise_selection']='local'`

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
   3. [ 600 lines] Core implementation A - structure-aware code embedding training and evaluation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-language semantic alignment (same algorithm, different lan
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - clone and near-clone detection accuracy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - retrieval quality on code-search benchmarks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_embeddings@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0556_code_embeddings.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0557-bug-localisation

**P0557 · `bug_localisation` — Bug Localisation & Root Cause Analysis** · [spec](PART_SPECS_T12.md#p0557-bug-localisation) · [self-contained txt](../prompts/P0557_bug_localisation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0557  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0557 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0557  (7/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Bug Localisation & Root Cause Analysis
file         : parts/t12_code/P0557_bug_localisation.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.bug_localisation
language     : Python 3.13
capability   : cap.t12.bug.bug_localisation@1
determinism  : pure
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Finds the actual cause, not the symptom.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. failure-to-code localisation from tests, traces and stack frames
  2. causal chain reconstruction from symptom to root cause
  3. distinguishing root cause from downstream symptom explicitly
  4. localisation accuracy on curated real-bug datasets

Expanded obligations:
  1. Implement failure-to-code localisation from tests, traces and stack
     frames, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement causal chain reconstruction from symptom to root cause with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement distinguishing root cause from downstream symptom explicitly
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's FrontierCode Diamond target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement localisation accuracy on curated real-bug datasets as a
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.bug.bug_localisation@1
  cap.t12.bug.bug_localisation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_embeddings@1
      if unavailable: use the in-file conservative substitute for
      `code_embeddings` (documented, slower, lower quality) and set
      `degraded['code_embeddings']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t10.goal.goal_management@1
      if unavailable: use the in-file conservative substitute for
      `goal_management` (documented, slower, lower quality) and set
      `degraded['goal_management']='local'`

  cap.t11.dependent.dependent_types@1
      if unavailable: use the in-file conservative substitute for
      `dependent_types` (documented, slower, lower quality) and set
      `degraded['dependent_types']='local'`

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
   3. [ 600 lines] Core implementation A - failure-to-code localisation from tests, traces and stack frames
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - causal chain reconstruction from symptom to root cause
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - distinguishing root cause from downstream symptom explicitly
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - localisation accuracy on curated real-bug datasets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.bug.bug_localisation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0557_bug_localisation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0558-patch-synthesis

**P0558 · `patch_synthesis` — Patch Synthesis Engine** · [spec](PART_SPECS_T12.md#p0558-patch-synthesis) · [self-contained txt](../prompts/P0558_patch_synthesis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0558  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0558 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0558  (8/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Patch Synthesis Engine
file         : parts/t12_code/P0558_patch_synthesis.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.patch_synthesis
language     : Python 3.13
capability   : cap.t12.patch.patch_synthesis@1
determinism  : pure
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Writes the minimal correct fix.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. repair candidate generation from root-cause understanding
  2. minimality and style-consistency constraints
  3. test-driven candidate validation with regression checking
  4. core contributor to SWE-bench Verified 99.8% target

Expanded obligations:
  1. Implement repair candidate generation from root-cause understanding with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Frontier-Bench v0.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement minimality and style-consistency constraints together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement test-driven candidate validation with regression checking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement core contributor to SWE-bench Verified 99.8% target, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
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
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.patch.patch_synthesis@1
  cap.t12.patch.patch_synthesis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.bug.bug_localisation@1
      if unavailable: use the in-file conservative substitute for
      `bug_localisation` (documented, slower, lower quality) and set
      `degraded['bug_localisation']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t10.probabilistic.probabilistic_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `probabilistic_reasoning` (documented, slower, lower quality) and set
      `degraded['probabilistic_reasoning']='local'`

  cap.t11.informalisatio.informalisation@1
      if unavailable: use the in-file conservative substitute for
      `informalisation` (documented, slower, lower quality) and set
      `degraded['informalisation']='local'`

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
   3. [ 600 lines] Core implementation A - repair candidate generation from root-cause understanding
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - minimality and style-consistency constraints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - test-driven candidate validation with regression checking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - core contributor to SWE-bench Verified 99.8% target
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.patch.patch_synthesis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0558_patch_synthesis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0559-patch-validation

**P0559 · `patch_validation` — Patch Validation & Regression Guarding** · [spec](PART_SPECS_T12.md#p0559-patch-validation) · [self-contained txt](../prompts/P0559_patch_validation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0559  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0559 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0559  (9/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Patch Validation & Regression Guarding
file         : parts/t12_code/P0559_patch_validation.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.patch_validation
language     : Python 3.13
capability   : cap.t12.patch.patch_validation@1
determinism  : pure
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Proves the fix fixes it and breaks nothing else.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. targeted test selection plus full-suite validation strategy
  2. behavioural-diff analysis beyond test outcomes
  3. flaky-test detection preventing false verdicts
  4. measured false-positive and false-negative validation rates

Expanded obligations:
  1. Implement targeted test selection plus full-suite validation strategy
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's FrontierCode Diamond target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement behavioural-diff analysis beyond test outcomes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement flaky-test detection preventing false verdicts, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured false-positive and false-negative validation rates
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
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
  cap.t12.patch.patch_validation@1
  cap.t12.patch.patch_validation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.patch.patch_synthesis@1
      if unavailable: use the in-file conservative substitute for
      `patch_synthesis` (documented, slower, lower quality) and set
      `degraded['patch_synthesis']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t10.stopping.stopping_rules@1
      if unavailable: use the in-file conservative substitute for
      `stopping_rules` (documented, slower, lower quality) and set
      `degraded['stopping_rules']='local'`

  cap.t11.proof.proof_compression@1
      if unavailable: use the in-file conservative substitute for
      `proof_compression` (documented, slower, lower quality) and set
      `degraded['proof_compression']='local'`

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
   3. [ 600 lines] Core implementation A - targeted test selection plus full-suite validation strategy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - behavioural-diff analysis beyond test outcomes
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - flaky-test detection preventing false verdicts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured false-positive and false-negative validation rates
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.patch.patch_validation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0559_patch_validation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0560-test-synthesis

**P0560 · `test_synthesis` — Test Generation & Coverage Engineering** · [spec](PART_SPECS_T12.md#p0560-test-synthesis) · [self-contained txt](../prompts/P0560_test_synthesis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0560  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0560 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0560  (10/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Test Generation & Coverage Engineering
file         : parts/t12_code/P0560_test_synthesis.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.test_synthesis
language     : Python 3.13
capability   : cap.t12.test.test_synthesis@1
determinism  : pure
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Writes the tests that would have caught the bug.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. specification-derived and coverage-guided test generation
  2. property-based test synthesis with invariant discovery
  3. assertion-quality scoring (does it actually detect faults)
  4. mutation-score measurement of generated suites

Expanded obligations:
  1. Implement specification-derived and coverage-guided test generation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement property-based test synthesis with invariant discovery, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Pro — a regression on that benchmark is an automatic rejection of this
     part.
  3. Implement assertion-quality scoring (does it actually detect faults)
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement mutation-score measurement of generated suites together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.test.test_synthesis@1
  cap.t12.test.test_synthesis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.patch.patch_validation@1
      if unavailable: use the in-file conservative substitute for
      `patch_validation` (documented, slower, lower quality) and set
      `degraded['patch_validation']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t10.assumption.assumption_tracking@1
      if unavailable: use the in-file conservative substitute for
      `assumption_tracking` (documented, slower, lower quality) and set
      `degraded['assumption_tracking']='local'`

  cap.t11.statistical.statistical_guarantees@1
      if unavailable: use the in-file conservative substitute for
      `statistical_guarantees` (documented, slower, lower quality) and set
      `degraded['statistical_guarantees']='local'`

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
   3. [ 600 lines] Core implementation A - specification-derived and coverage-guided test generation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - property-based test synthesis with invariant discovery
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - assertion-quality scoring (does it actually detect faults)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - mutation-score measurement of generated suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.test.test_synthesis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0560_test_synthesis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0561-mutation-testing

**P0561 · `mutation_testing` — Mutation Testing & Test Quality Assessment** · [spec](PART_SPECS_T12.md#p0561-mutation-testing) · [self-contained txt](../prompts/P0561_mutation_testing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0561  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0561 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0561  (11/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Mutation Testing & Test Quality Assessment
file         : parts/t12_code/P0561_mutation_testing.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.mutation_testing
language     : Python 3.13
capability   : cap.t12.mutation.mutation_testing@1
determinism  : pure
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Measures whether tests are real or decorative.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mutation-operator library per language with realistic faults
  2. equivalent-mutant detection and cost control
  3. test-suite quality scoring and gap identification
  4. correlation between mutation score and real bug detection

Expanded obligations:
  1. Implement mutation-operator library per language with realistic faults,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Pro — a regression on that benchmark is an automatic rejection of this
     part.
  2. Implement equivalent-mutant detection and cost control with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement test-suite quality scoring and gap identification together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  4. Implement correlation between mutation score and real bug detection as a
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.mutation.mutation_testing@1
  cap.t12.mutation.mutation_testing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.test.test_synthesis@1
      if unavailable: use the in-file conservative substitute for
      `test_synthesis` (documented, slower, lower quality) and set
      `degraded['test_synthesis']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t10.reasoning.reasoning_cost_model@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_cost_model` (documented, slower, lower quality) and set
      `degraded['reasoning_cost_model']='local'`

  cap.t11.regression.regression_proofs@1
      if unavailable: use the in-file conservative substitute for
      `regression_proofs` (documented, slower, lower quality) and set
      `degraded['regression_proofs']='local'`

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
   3. [ 600 lines] Core implementation A - mutation-operator library per language with realistic faults
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - equivalent-mutant detection and cost control
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - test-suite quality scoring and gap identification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - correlation between mutation score and real bug detection
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.mutation.mutation_testing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0561_mutation_testing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0562-code-review-engine

**P0562 · `code_review_engine` — Automated Code Review & Hazard Detection** · [spec](PART_SPECS_T12.md#p0562-code-review-engine) · [self-contained txt](../prompts/P0562_code_review_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0562  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0562 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0562  (12/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Automated Code Review & Hazard Detection
file         : parts/t12_code/P0562_code_review_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_review_engine
language     : Python 3.13
capability   : cap.t12.code.code_review_engine@1
determinism  : pure
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Spots the subtle, codebase-specific problem a human reviewer would.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. review-comment generation with severity and confidence
  2. codebase-convention learning and enforcement
  3. hazard classes: concurrency, resource, security, numerical, API misuse
  4. target: 4x fewer missed flaws than Opus-class review baselines

Expanded obligations:
  1. Implement review-comment generation with severity and confidence with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement codebase-convention learning and enforcement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  3. Implement hazard classes: concurrency, resource, security, numerical,
     API misuse as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement target: 4x fewer missed flaws than Opus-class review
     baselines, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
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
  cap.t12.code.code_review_engine@1
  cap.t12.code.code_review_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.mutation.mutation_testing@1
      if unavailable: use the in-file conservative substitute for
      `mutation_testing` (documented, slower, lower quality) and set
      `degraded['mutation_testing']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t10.collective.collective_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `collective_reasoning` (documented, slower, lower quality) and set
      `degraded['collective_reasoning']='local'`

  cap.t11.verification.verification_bench@1
      if unavailable: use the in-file conservative substitute for
      `verification_bench` (documented, slower, lower quality) and set
      `degraded['verification_bench']='local'`

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
   3. [ 600 lines] Core implementation A - review-comment generation with severity and confidence
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - codebase-convention learning and enforcement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hazard classes: concurrency, resource, security, numerical, API 
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: 4x fewer missed flaws than Opus-class review baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_review_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0562_code_review_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0563-static-analysis

**P0563 · `static_analysis` — Static Analysis & Linting Integration** · [spec](PART_SPECS_T12.md#p0563-static-analysis) · [self-contained txt](../prompts/P0563_static_analysis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0563  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0563 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0563  (13/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Static Analysis & Linting Integration
file         : parts/t12_code/P0563_static_analysis.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.static_analysis
language     : Python 3.13
capability   : cap.t12.static.static_analysis@1
determinism  : pure
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
All the cheap checks, deduplicated and prioritised.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-tool orchestration with finding deduplication
  2. false-positive suppression learned from developer feedback
  3. severity ranking by exploitability and blast radius
  4. precision measurement on labelled finding sets

Expanded obligations:
  1. Implement multi-tool orchestration with finding deduplication together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  2. Implement false-positive suppression learned from developer feedback as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement severity ranking by exploitability and blast radius, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement precision measurement on labelled finding sets with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
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
  cap.t12.static.static_analysis@1
  cap.t12.static.static_analysis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_review_engine@1
      if unavailable: use the in-file conservative substitute for
      `code_review_engine` (documented, slower, lower quality) and set
      `degraded['code_review_engine']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t10.beam.beam_pruning@1
      if unavailable: use the in-file conservative substitute for
      `beam_pruning` (documented, slower, lower quality) and set
      `degraded['beam_pruning']='local'`

  cap.t11.proof.proof_search@1
      if unavailable: use the in-file conservative substitute for
      `proof_search` (documented, slower, lower quality) and set
      `degraded['proof_search']='local'`

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
   3. [ 600 lines] Core implementation A - multi-tool orchestration with finding deduplication
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - false-positive suppression learned from developer feedback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - severity ranking by exploitability and blast radius
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - precision measurement on labelled finding sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.static.static_analysis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0563_static_analysis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0564-refactoring-engine

**P0564 · `refactoring_engine` — Semantics-Preserving Refactoring Engine** · [spec](PART_SPECS_T12.md#p0564-refactoring-engine) · [self-contained txt](../prompts/P0564_refactoring_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0564  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0564 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0564  (14/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Semantics-Preserving Refactoring Engine
file         : parts/t12_code/P0564_refactoring_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.refactoring_engine
language     : Python 3.13
capability   : cap.t12.refactoring.refactoring_engine@1
determinism  : pure
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Large-scale changes that provably do not change behaviour.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. refactoring catalogue with precondition checking per transformation
  2. cross-file atomic application with rollback
  3. behaviour-preservation verification (tests plus static equivalence)
  4. success rate on large-scale refactoring tasks

Expanded obligations:
  1. Implement refactoring catalogue with precondition checking per
     transformation as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement cross-file atomic application with rollback, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement behaviour-preservation verification (tests plus static
     equivalence) with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement success rate on large-scale refactoring tasks together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.refactoring.refactoring_engine@1
  cap.t12.refactoring.refactoring_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.static.static_analysis@1
      if unavailable: use the in-file conservative substitute for
      `static_analysis` (documented, slower, lower quality) and set
      `degraded['static_analysis']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t10.planning.planning_engine@1
      if unavailable: use the in-file conservative substitute for
      `planning_engine` (documented, slower, lower quality) and set
      `degraded['planning_engine']='local'`

  cap.t11.refinement.refinement_types@1
      if unavailable: use the in-file conservative substitute for
      `refinement_types` (documented, slower, lower quality) and set
      `degraded['refinement_types']='local'`

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
   3. [ 600 lines] Core implementation A - refactoring catalogue with precondition checking per transformat
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-file atomic application with rollback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - behaviour-preservation verification (tests plus static equivalen
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - success rate on large-scale refactoring tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.refactoring.refactoring_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0564_refactoring_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0565-migration-engine

**P0565 · `migration_engine` — Large-Scale Migration & Codemod Engine** · [spec](PART_SPECS_T12.md#p0565-migration-engine) · [self-contained txt](../prompts/P0565_migration_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0565  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0565 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0565  (15/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Large-Scale Migration & Codemod Engine
file         : parts/t12_code/P0565_migration_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.migration_engine
language     : Python 3.13
capability   : cap.t12.migration.migration_engine@1
determinism  : pure
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Upgrades a million-line codebase in one session.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. codemod authoring from few examples with generalisation
  2. incremental application with continuous validation
  3. progress tracking and partial-migration coherence
  4. measured throughput on real migration corpora

Expanded obligations:
  1. Implement codemod authoring from few examples with generalisation, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement incremental application with continuous validation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement progress tracking and partial-migration coherence together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement measured throughput on real migration corpora as a
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.migration.migration_engine@1
  cap.t12.migration.migration_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.refactoring.refactoring_engine@1
      if unavailable: use the in-file conservative substitute for
      `refactoring_engine` (documented, slower, lower quality) and set
      `degraded['refactoring_engine']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t10.counterfactual.counterfactual_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `counterfactual_reasoning` (documented, slower, lower quality) and set
      `degraded['counterfactual_reasoning']='local'`

  cap.t11.autoformalisat.autoformalisation@1
      if unavailable: use the in-file conservative substitute for
      `autoformalisation` (documented, slower, lower quality) and set
      `degraded['autoformalisation']='local'`

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
   3. [ 600 lines] Core implementation A - codemod authoring from few examples with generalisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - incremental application with continuous validation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - progress tracking and partial-migration coherence
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured throughput on real migration corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.migration.migration_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0565_migration_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0566-api-evolution

**P0566 · `api_evolution` — API Compatibility & Breaking Change Analysis** · [spec](PART_SPECS_T12.md#p0566-api-evolution) · [self-contained txt](../prompts/P0566_api_evolution.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0566  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0566 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0566  (16/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : API Compatibility & Breaking Change Analysis
file         : parts/t12_code/P0566_api_evolution.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.api_evolution
language     : Python 3.13
capability   : cap.t12.api.api_evolution@1
determinism  : pure
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Knows exactly who breaks when an interface changes.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. semantic diff of public interfaces across versions
  2. downstream impact analysis with usage evidence
  3. migration-guide and shim generation
  4. accuracy on curated API-change datasets

Expanded obligations:
  1. Implement semantic diff of public interfaces across versions with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement downstream impact analysis with usage evidence together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement migration-guide and shim generation as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's SWE-bench Verified target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement accuracy on curated API-change datasets, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Pro, so its p99 latency
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.api.api_evolution@1
  cap.t12.api.api_evolution.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.migration.migration_engine@1
      if unavailable: use the in-file conservative substitute for
      `migration_engine` (documented, slower, lower quality) and set
      `degraded['migration_engine']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t10.difficulty.difficulty_estimation@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_estimation` (documented, slower, lower quality) and set
      `degraded['difficulty_estimation']='local'`

  cap.t11.counterexample.counterexample_engine@1
      if unavailable: use the in-file conservative substitute for
      `counterexample_engine` (documented, slower, lower quality) and set
      `degraded['counterexample_engine']='local'`

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
   3. [ 600 lines] Core implementation A - semantic diff of public interfaces across versions
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - downstream impact analysis with usage evidence
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - migration-guide and shim generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on curated API-change datasets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.api.api_evolution@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0566_api_evolution.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0567-dependency-reasoning

**P0567 · `dependency_reasoning` — Dependency & Supply Chain Reasoning** · [spec](PART_SPECS_T12.md#p0567-dependency-reasoning) · [self-contained txt](../prompts/P0567_dependency_reasoning.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0567  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0567 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0567  (17/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Dependency & Supply Chain Reasoning
file         : parts/t12_code/P0567_dependency_reasoning.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.dependency_reasoning
language     : Python 3.13
capability   : cap.t12.dependency.dependency_reasoning@1
determinism  : pure
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Understands the whole dependency tree and its risks.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. version-constraint solving and conflict explanation
  2. vulnerability and license analysis with transitive reach
  3. update-risk assessment with behavioural-change prediction
  4. measured accuracy of update-safety predictions

Expanded obligations:
  1. Implement version-constraint solving and conflict explanation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement vulnerability and license analysis with transitive reach as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement update-risk assessment with behavioural-change prediction, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured accuracy of update-safety predictions with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
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
  cap.t12.dependency.dependency_reasoning@1
  cap.t12.dependency.dependency_reasoning.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.api.api_evolution@1
      if unavailable: use the in-file conservative substitute for
      `api_evolution` (documented, slower, lower quality) and set
      `degraded['api_evolution']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t10.evidence.evidence_integration@1
      if unavailable: use the in-file conservative substitute for
      `evidence_integration` (documented, slower, lower quality) and set
      `degraded['evidence_integration']='local'`

  cap.t11.numeric.numeric_verification_ml@1
      if unavailable: use the in-file conservative substitute for
      `numeric_verification_ml` (documented, slower, lower quality) and set
      `degraded['numeric_verification_ml']='local'`

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
   3. [ 600 lines] Core implementation A - version-constraint solving and conflict explanation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - vulnerability and license analysis with transitive reach
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - update-risk assessment with behavioural-change prediction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured accuracy of update-safety predictions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.dependency.dependency_reasoning@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0567_dependency_reasoning.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0568-build-system

**P0568 · `build_system` — Build System Understanding & Repair** · [spec](PART_SPECS_T12.md#p0568-build-system) · [self-contained txt](../prompts/P0568_build_system.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0568  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0568 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0568  (18/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Build System Understanding & Repair
file         : parts/t12_code/P0568_build_system.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.build_system
language     : Python 3.13
capability   : cap.t12.build.build_system@1
determinism  : pure
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Fixes the build, the hardest part of real engineering work.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. build-graph extraction across major build systems
  2. build-failure diagnosis with actionable remediation
  3. hermeticity and reproducibility analysis
  4. build-repair success rate on curated failure corpora

Expanded obligations:
  1. Implement build-graph extraction across major build systems as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement build-failure diagnosis with actionable remediation, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of SWE-bench Pro, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement hermeticity and reproducibility analysis with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement build-repair success rate on curated failure corpora together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
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
  cap.t12.build.build_system@1
  cap.t12.build.build_system.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.dependency.dependency_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `dependency_reasoning` (documented, slower, lower quality) and set
      `degraded['dependency_reasoning']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t10.reasoning.reasoning_search_bench@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_search_bench` (documented, slower, lower quality) and set
      `degraded['reasoning_search_bench']='local'`

  cap.t11.hybrid.hybrid_verification@1
      if unavailable: use the in-file conservative substitute for
      `hybrid_verification` (documented, slower, lower quality) and set
      `degraded['hybrid_verification']='local'`

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
   3. [ 600 lines] Core implementation A - build-graph extraction across major build systems
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - build-failure diagnosis with actionable remediation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hermeticity and reproducibility analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - build-repair success rate on curated failure corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.build.build_system@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0568_build_system.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0569-code-execution-sandbox

**P0569 · `code_execution_sandbox` — Code Execution & Validation Sandbox** · [spec](PART_SPECS_T12.md#p0569-code-execution-sandbox) · [self-contained txt](../prompts/P0569_code_execution_sandbox.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0569  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0569 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0569  (19/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Code Execution & Validation Sandbox
file         : parts/t12_code/P0569_code_execution_sandbox.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_execution_sandbox
language     : Python 3.13
capability   : cap.t12.code.code_execution_sandbox@1
determinism  : pure
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Runs untrusted code safely, fast, thousands of times.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. isolated execution with resource limits and syscall filtering
  2. snapshot/restore for fast repeated runs
  3. deterministic execution mode for reproducible results
  4. throughput measurement of validation runs per second

Expanded obligations:
  1. Implement isolated execution with resource limits and syscall filtering,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement snapshot/restore for fast repeated runs with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement deterministic execution mode for reproducible results together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement throughput measurement of validation runs per second as a
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
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.code.code_execution_sandbox@1
  cap.t12.code.code_execution_sandbox.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.build.build_system@1
      if unavailable: use the in-file conservative substitute for
      `build_system` (documented, slower, lower quality) and set
      `degraded['build_system']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t10.reasoning.reasoning_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_interpretability` (documented, slower, lower quality) and
      set `degraded['reasoning_interpretability']='local'`

  cap.t11.trust.trust_boundaries@1
      if unavailable: use the in-file conservative substitute for
      `trust_boundaries` (documented, slower, lower quality) and set
      `degraded['trust_boundaries']='local'`

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
   3. [ 600 lines] Core implementation A - isolated execution with resource limits and syscall filtering
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - snapshot/restore for fast repeated runs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deterministic execution mode for reproducible results
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput measurement of validation runs per second
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_execution_sandbox@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0569_code_execution_sandbox.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0570-test-orchestration

**P0570 · `test_orchestration` — Test Selection, Ordering & Parallel Execution** · [spec](PART_SPECS_T12.md#p0570-test-orchestration) · [self-contained txt](../prompts/P0570_test_orchestration.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0570  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0570 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0570  (20/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Test Selection, Ordering & Parallel Execution
file         : parts/t12_code/P0570_test_orchestration.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.test_orchestration
language     : Python 3.13
capability   : cap.t12.test.test_orchestration@1
determinism  : pure
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Runs the right 1% of tests in seconds instead of all of them in hours.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. change-impact-based test selection with safety bounds
  2. failure-probability ordering for fastest feedback
  3. parallel execution with dependency and resource awareness
  4. measured feedback-latency reduction at equal fault detection

Expanded obligations:
  1. Implement change-impact-based test selection with safety bounds with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement failure-probability ordering for fastest feedback together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement parallel execution with dependency and resource awareness as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured feedback-latency reduction at equal fault detection,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Pro — a regression on that benchmark is an automatic rejection of this
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
  cap.t12.test.test_orchestration@1
  cap.t12.test.test_orchestration.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_execution_sandbox@1
      if unavailable: use the in-file conservative substitute for
      `code_execution_sandbox` (documented, slower, lower quality) and set
      `degraded['code_execution_sandbox']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t10.graph.graph_search@1
      if unavailable: use the in-file conservative substitute for
      `graph_search` (documented, slower, lower quality) and set
      `degraded['graph_search']='local'`

  cap.t11.itp.itp_bridge@1
      if unavailable: use the in-file conservative substitute for
      `itp_bridge` (documented, slower, lower quality) and set
      `degraded['itp_bridge']='local'`

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
   3. [ 600 lines] Core implementation A - change-impact-based test selection with safety bounds
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - failure-probability ordering for fastest feedback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - parallel execution with dependency and resource awareness
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured feedback-latency reduction at equal fault detection
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.test.test_orchestration@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0570_test_orchestration.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0571-flaky-detection

**P0571 · `flaky_detection` — Flaky Test Detection & Stabilisation** · [spec](PART_SPECS_T12.md#p0571-flaky-detection) · [self-contained txt](../prompts/P0571_flaky_detection.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0571  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0571 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0571  (21/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Flaky Test Detection & Stabilisation
file         : parts/t12_code/P0571_flaky_detection.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.flaky_detection
language     : Python 3.13
capability   : cap.t12.flaky.flaky_detection@1
determinism  : pure
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Distinguishes real failures from noise, then removes the noise.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. flakiness detection via repeated and varied execution
  2. root-cause classification (timing, order, resource, randomness)
  3. stabilisation patch generation
  4. measured reduction in flaky-failure rate

Expanded obligations:
  1. Implement flakiness detection via repeated and varied execution together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement root-cause classification (timing, order, resource,
     randomness) as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement stabilisation patch generation, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against SWE-bench Pro — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured reduction in flaky-failure rate with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.flaky.flaky_detection@1
  cap.t12.flaky.flaky_detection.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.test.test_orchestration@1
      if unavailable: use the in-file conservative substitute for
      `test_orchestration` (documented, slower, lower quality) and set
      `degraded['test_orchestration']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t10.decomposition.decomposition@1
      if unavailable: use the in-file conservative substitute for
      `decomposition` (documented, slower, lower quality) and set
      `degraded['decomposition']='local'`

  cap.t11.model.model_checking@1
      if unavailable: use the in-file conservative substitute for
      `model_checking` (documented, slower, lower quality) and set
      `degraded['model_checking']='local'`

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
   3. [ 600 lines] Core implementation A - flakiness detection via repeated and varied execution
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - root-cause classification (timing, order, resource, randomness)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - stabilisation patch generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured reduction in flaky-failure rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.flaky.flaky_detection@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0571_flaky_detection.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0572-performance-engineering

**P0572 · `performance_engineering` — Performance Profiling & Optimisation Agent** · [spec](PART_SPECS_T12.md#p0572-performance-engineering) · [self-contained txt](../prompts/P0572_performance_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0572  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0572 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0572  (22/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Performance Profiling & Optimisation Agent
file         : parts/t12_code/P0572_performance_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.performance_engineering
language     : Python 3.13
capability   : cap.t12.performance.performance_engineering@1
determinism  : pure
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Makes other people's code faster, with proof.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. profiling orchestration and bottleneck identification
  2. optimisation candidate generation with correctness preservation
  3. before/after measurement with statistical rigor
  4. measured speedups achieved on real codebases

Expanded obligations:
  1. Implement profiling orchestration and bottleneck identification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement optimisation candidate generation with correctness
     preservation, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     SWE-bench Pro — a regression on that benchmark is an automatic rejection
     of this part.
  3. Implement before/after measurement with statistical rigor with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured speedups achieved on real codebases together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.performance.performance_engineering@1
  cap.t12.performance.performance_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.flaky.flaky_detection@1
      if unavailable: use the in-file conservative substitute for
      `flaky_detection` (documented, slower, lower quality) and set
      `degraded['flaky_detection']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t10.program.program_synthesis_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `program_synthesis_reasoning` (documented, slower, lower quality) and
      set `degraded['program_synthesis_reasoning']='local'`

  cap.t11.theorem.theorem_library@1
      if unavailable: use the in-file conservative substitute for
      `theorem_library` (documented, slower, lower quality) and set
      `degraded['theorem_library']='local'`

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
   3. [ 600 lines] Core implementation A - profiling orchestration and bottleneck identification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - optimisation candidate generation with correctness preservation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - before/after measurement with statistical rigor
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured speedups achieved on real codebases
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.performance.performance_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0572_performance_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0573-concurrency-bugs

**P0573 · `concurrency_bugs` — Concurrency Bug Detection & Repair** · [spec](PART_SPECS_T12.md#p0573-concurrency-bugs) · [self-contained txt](../prompts/P0573_concurrency_bugs.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0573  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0573 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0573  (23/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Concurrency Bug Detection & Repair
file         : parts/t12_code/P0573_concurrency_bugs.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.concurrency_bugs
language     : Python 3.13
capability   : cap.t12.concurrency.concurrency_bugs@1
determinism  : pure
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Finds the race that only happens in production.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. race, deadlock and atomicity-violation detection (static plus dynamic)
  2. schedule exploration with systematic interleaving control
  3. repair synthesis preserving performance
  4. detection rate on curated concurrency bug datasets

Expanded obligations:
  1. Implement race, deadlock and atomicity-violation detection (static plus
     dynamic), and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Pro — a regression on that benchmark is an automatic rejection of this
     part.
  2. Implement schedule exploration with systematic interleaving control with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement repair synthesis preserving performance together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  4. Implement detection rate on curated concurrency bug datasets as a
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
  cap.t12.concurrency.concurrency_bugs@1
  cap.t12.concurrency.concurrency_bugs.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.performance.performance_engineering@1
      if unavailable: use the in-file conservative substitute for
      `performance_engineering` (documented, slower, lower quality) and set
      `degraded['performance_engineering']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t10.meta.meta_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `meta_reasoning` (documented, slower, lower quality) and set
      `degraded['meta_reasoning']='local'`

  cap.t11.proof.proof_repair@1
      if unavailable: use the in-file conservative substitute for
      `proof_repair` (documented, slower, lower quality) and set
      `degraded['proof_repair']='local'`

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
   3. [ 600 lines] Core implementation A - race, deadlock and atomicity-violation detection (static plus dy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - schedule exploration with systematic interleaving control
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - repair synthesis preserving performance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - detection rate on curated concurrency bug datasets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.concurrency.concurrency_bugs@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0573_concurrency_bugs.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0574-memory-safety

**P0574 · `memory_safety` — Memory Safety & Resource Leak Analysis** · [spec](PART_SPECS_T12.md#p0574-memory-safety) · [self-contained txt](../prompts/P0574_memory_safety.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0574  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0574 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0574  (24/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Memory Safety & Resource Leak Analysis
file         : parts/t12_code/P0574_memory_safety.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.memory_safety
language     : Python 3.13
capability   : cap.t12.memory.memory_safety@1
determinism  : pure
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Catches use-after-free, leaks and overflows before shipping.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. ownership and lifetime analysis across languages
  2. leak detection for memory, handles, locks and connections
  3. sanitiser orchestration and finding triage
  4. detection rate on labelled memory-bug corpora

Expanded obligations:
  1. Implement ownership and lifetime analysis across languages with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement leak detection for memory, handles, locks and connections
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of FrontierCode Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement sanitiser orchestration and finding triage as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against SWE-bench
     Verified — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement detection rate on labelled memory-bug corpora, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
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
  cap.t12.memory.memory_safety@1
  cap.t12.memory.memory_safety.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.concurrency.concurrency_bugs@1
      if unavailable: use the in-file conservative substitute for
      `concurrency_bugs` (documented, slower, lower quality) and set
      `degraded['concurrency_bugs']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t10.hypothesis.hypothesis_management@1
      if unavailable: use the in-file conservative substitute for
      `hypothesis_management` (documented, slower, lower quality) and set
      `degraded['hypothesis_management']='local'`

  cap.t11.concurrency.concurrency_verification@1
      if unavailable: use the in-file conservative substitute for
      `concurrency_verification` (documented, slower, lower quality) and set
      `degraded['concurrency_verification']='local'`

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
   3. [ 600 lines] Core implementation A - ownership and lifetime analysis across languages
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - leak detection for memory, handles, locks and connections
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - sanitiser orchestration and finding triage
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - detection rate on labelled memory-bug corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.memory.memory_safety@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0574_memory_safety.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0575-security-code-analysis

**P0575 · `security_code_analysis` — Security Vulnerability Discovery** · [spec](PART_SPECS_T12.md#p0575-security-code-analysis) · [self-contained txt](../prompts/P0575_security_code_analysis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0575  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0575 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0575  (25/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Security Vulnerability Discovery
file         : parts/t12_code/P0575_security_code_analysis.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.security_code_analysis
language     : Python 3.13
capability   : cap.t12.security.security_code_analysis@1
determinism  : pure
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Finds real, exploitable vulnerabilities in source code.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. taint analysis from sources to sinks with sanitiser awareness
  2. vulnerability-class detectors mapped to a standard taxonomy
  3. exploitability triage without generating exploit code
  4. target: OSS-Fuzz find rate 97% versus Opus 5's ~78%

Expanded obligations:
  1. Implement taint analysis from sources to sinks with sanitiser awareness
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of FrontierCode Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement vulnerability-class detectors mapped to a standard taxonomy as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement exploitability triage without generating exploit code, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement target: OSS-Fuzz find rate 97% versus Opus 5's ~78% with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
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
  cap.t12.security.security_code_analysis@1
  cap.t12.security.security_code_analysis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.memory.memory_safety@1
      if unavailable: use the in-file conservative substitute for
      `memory_safety` (documented, slower, lower quality) and set
      `degraded['memory_safety']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t10.proof.proof_sketch@1
      if unavailable: use the in-file conservative substitute for
      `proof_sketch` (documented, slower, lower quality) and set
      `degraded['proof_sketch']='local'`

  cap.t11.verification.verification_scheduling@1
      if unavailable: use the in-file conservative substitute for
      `verification_scheduling` (documented, slower, lower quality) and set
      `degraded['verification_scheduling']='local'`

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
   3. [ 600 lines] Core implementation A - taint analysis from sources to sinks with sanitiser awareness
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - vulnerability-class detectors mapped to a standard taxonomy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - exploitability triage without generating exploit code
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: OSS-Fuzz find rate 97% versus Opus 5's ~78%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.security.security_code_analysis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0575_security_code_analysis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0576-fuzzing-agent

**P0576 · `fuzzing_agent` — Fuzzing Campaign Orchestration** · [spec](PART_SPECS_T12.md#p0576-fuzzing-agent) · [self-contained txt](../prompts/P0576_fuzzing_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0576  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0576 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0576  (26/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Fuzzing Campaign Orchestration
file         : parts/t12_code/P0576_fuzzing_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.fuzzing_agent
language     : Python 3.13
capability   : cap.t12.fuzzing.fuzzing_agent@1
determinism  : pure
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Drives fuzzers to the interesting parts of the code.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. harness generation for arbitrary library entry points
  2. corpus construction, minimisation and seed scheduling
  3. coverage-plateau detection and strategy switching
  4. measured bug-discovery rate per CPU hour

Expanded obligations:
  1. Implement harness generation for arbitrary library entry points as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement corpus construction, minimisation and seed scheduling, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement coverage-plateau detection and strategy switching with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured bug-discovery rate per CPU hour together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.fuzzing.fuzzing_agent@1
  cap.t12.fuzzing.fuzzing_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.security.security_code_analysis@1
      if unavailable: use the in-file conservative substitute for
      `security_code_analysis` (documented, slower, lower quality) and set
      `degraded['security_code_analysis']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t10.adversarial.adversarial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `adversarial_reasoning` (documented, slower, lower quality) and set
      `degraded['adversarial_reasoning']='local'`

  cap.t11.verification.verification_cache@1
      if unavailable: use the in-file conservative substitute for
      `verification_cache` (documented, slower, lower quality) and set
      `degraded['verification_cache']='local'`

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
   3. [ 600 lines] Core implementation A - harness generation for arbitrary library entry points
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - corpus construction, minimisation and seed scheduling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - coverage-plateau detection and strategy switching
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured bug-discovery rate per CPU hour
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.fuzzing.fuzzing_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0576_fuzzing_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0577-crash-triage

**P0577 · `crash_triage` — Crash Triage & Deduplication** · [spec](PART_SPECS_T12.md#p0577-crash-triage) · [self-contained txt](../prompts/P0577_crash_triage.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0577  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0577 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0577  (27/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Crash Triage & Deduplication
file         : parts/t12_code/P0577_crash_triage.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.crash_triage
language     : Python 3.13
capability   : cap.t12.crash.crash_triage@1
determinism  : pure
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Turns 10000 crashes into 12 distinct bugs.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. stack and root-cause based crash clustering
  2. severity and exploitability assessment
  3. minimal reproducer generation
  4. deduplication accuracy on labelled crash corpora

Expanded obligations:
  1. Implement stack and root-cause based crash clustering, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement severity and exploitability assessment with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Frontier-Bench v0.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement minimal reproducer generation together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Its contribution is measured against
     FrontierCode Diamond — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement deduplication accuracy on labelled crash corpora as a
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
  cap.t12.crash.crash_triage@1
  cap.t12.crash.crash_triage.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.fuzzing.fuzzing_agent@1
      if unavailable: use the in-file conservative substitute for
      `fuzzing_agent` (documented, slower, lower quality) and set
      `degraded['fuzzing_agent']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t10.tree.tree_search@1
      if unavailable: use the in-file conservative substitute for
      `tree_search` (documented, slower, lower quality) and set
      `degraded['tree_search']='local'`

  cap.t11.sat.sat_engine@1
      if unavailable: use the in-file conservative substitute for
      `sat_engine` (documented, slower, lower quality) and set
      `degraded['sat_engine']='local'`

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
   3. [ 600 lines] Core implementation A - stack and root-cause based crash clustering
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - severity and exploitability assessment
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - minimal reproducer generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - deduplication accuracy on labelled crash corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.crash.crash_triage@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0577_crash_triage.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0578-code-generation-core

**P0578 · `code_generation_core` — Production Code Generation Engine** · [spec](PART_SPECS_T12.md#p0578-code-generation-core) · [self-contained txt](../prompts/P0578_code_generation_core.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0578  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0578 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0578  (28/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Production Code Generation Engine
file         : parts/t12_code/P0578_code_generation_core.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_generation_core
language     : Python 3.13
capability   : cap.t12.code.code_generation_core@1
determinism  : pure
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Writes code that ships: correct, idiomatic, tested, documented.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. specification-to-implementation generation with design rationale
  2. codebase-convention conformance and API reuse over reinvention
  3. self-verification loop before returning code
  4. measured first-pass acceptance rate by expert reviewers

Expanded obligations:
  1. Implement specification-to-implementation generation with design
     rationale with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement codebase-convention conformance and API reuse over reinvention
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against FrontierCode Diamond — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement self-verification loop before returning code as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's SWE-bench
     Verified target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement measured first-pass acceptance rate by expert reviewers, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.code.code_generation_core@1
  cap.t12.code.code_generation_core.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.crash.crash_triage@1
      if unavailable: use the in-file conservative substitute for
      `crash_triage` (documented, slower, lower quality) and set
      `degraded['crash_triage']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t10.debate.debate_ensemble@1
      if unavailable: use the in-file conservative substitute for
      `debate_ensemble` (documented, slower, lower quality) and set
      `degraded['debate_ensemble']='local'`

  cap.t11.abstract.abstract_interpretation@1
      if unavailable: use the in-file conservative substitute for
      `abstract_interpretation` (documented, slower, lower quality) and set
      `degraded['abstract_interpretation']='local'`

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
   3. [ 600 lines] Core implementation A - specification-to-implementation generation with design rationale
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - codebase-convention conformance and API reuse over reinvention
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - self-verification loop before returning code
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured first-pass acceptance rate by expert reviewers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_generation_core@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0578_code_generation_core.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0579-architecture-design

**P0579 · `architecture_design` — Software Architecture Design & Review** · [spec](PART_SPECS_T12.md#p0579-architecture-design) · [self-contained txt](../prompts/P0579_architecture_design.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0579  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0579 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0579  (29/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Software Architecture Design & Review
file         : parts/t12_code/P0579_architecture_design.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.architecture_design
language     : Python 3.13
capability   : cap.t12.architecture.architecture_design@1
determinism  : pure
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Makes the big decisions well, and explains the tradeoffs.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. design-alternative generation with explicit tradeoff analysis
  2. constraint-driven architecture selection and documentation
  3. architecture-erosion detection against the intended design
  4. expert-evaluation results on real design tasks

Expanded obligations:
  1. Implement design-alternative generation with explicit tradeoff analysis
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against FrontierCode Diamond — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement constraint-driven architecture selection and documentation as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement architecture-erosion detection against the intended design,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement expert-evaluation results on real design tasks with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.architecture.architecture_design@1
  cap.t12.architecture.architecture_design.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_generation_core@1
      if unavailable: use the in-file conservative substitute for
      `code_generation_core` (documented, slower, lower quality) and set
      `degraded['code_generation_core']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t10.induction.induction_engine@1
      if unavailable: use the in-file conservative substitute for
      `induction_engine` (documented, slower, lower quality) and set
      `degraded['induction_engine']='local'`

  cap.t11.computer.computer_algebra@1
      if unavailable: use the in-file conservative substitute for
      `computer_algebra` (documented, slower, lower quality) and set
      `degraded['computer_algebra']='local'`

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
   3. [ 600 lines] Core implementation A - design-alternative generation with explicit tradeoff analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - constraint-driven architecture selection and documentation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - architecture-erosion detection against the intended design
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-evaluation results on real design tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.architecture.architecture_design@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0579_architecture_design.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0580-legacy-comprehension

**P0580 · `legacy_comprehension` — Legacy Code Comprehension** · [spec](PART_SPECS_T12.md#p0580-legacy-comprehension) · [self-contained txt](../prompts/P0580_legacy_comprehension.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0580  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0580 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0580  (30/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Legacy Code Comprehension
file         : parts/t12_code/P0580_legacy_comprehension.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.legacy_comprehension
language     : Python 3.13
capability   : cap.t12.legacy.legacy_comprehension@1
determinism  : pure
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Understands undocumented code nobody remembers writing.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. behaviour reconstruction from code, tests and history
  2. implicit-contract and invariant extraction
  3. documentation generation with accuracy verification
  4. comprehension-accuracy measurement via expert quizzes

Expanded obligations:
  1. Implement behaviour reconstruction from code, tests and history as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement implicit-contract and invariant extraction, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Pro, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement documentation generation with accuracy verification with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement comprehension-accuracy measurement via expert quizzes together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.legacy.legacy_comprehension@1
  cap.t12.legacy.legacy_comprehension.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.architecture.architecture_design@1
      if unavailable: use the in-file conservative substitute for
      `architecture_design` (documented, slower, lower quality) and set
      `degraded['architecture_design']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t10.commonsense.commonsense_engine@1
      if unavailable: use the in-file conservative substitute for
      `commonsense_engine` (documented, slower, lower quality) and set
      `degraded['commonsense_engine']='local'`

  cap.t11.symbolic.symbolic_execution@1
      if unavailable: use the in-file conservative substitute for
      `symbolic_execution` (documented, slower, lower quality) and set
      `degraded['symbolic_execution']='local'`

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
   3. [ 600 lines] Core implementation A - behaviour reconstruction from code, tests and history
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - implicit-contract and invariant extraction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - documentation generation with accuracy verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - comprehension-accuracy measurement via expert quizzes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.legacy.legacy_comprehension@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0580_legacy_comprehension.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0581-code-documentation

**P0581 · `code_documentation` — Documentation Generation & Maintenance** · [spec](PART_SPECS_T12.md#p0581-code-documentation) · [self-contained txt](../prompts/P0581_code_documentation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0581  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0581 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0581  (31/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Documentation Generation & Maintenance
file         : parts/t12_code/P0581_code_documentation.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_documentation
language     : Python 3.13
capability   : cap.t12.code.code_documentation@1
determinism  : pure
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Docs that are correct and stay correct.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. API and design documentation generation from code and intent
  2. doc/code drift detection and automatic repair
  3. example generation with executable verification
  4. accuracy measurement of generated documentation

Expanded obligations:
  1. Implement API and design documentation generation from code and intent,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement doc/code drift detection and automatic repair with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement example generation with executable verification together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement accuracy measurement of generated documentation as a
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
  cap.t12.code.code_documentation@1
  cap.t12.code.code_documentation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.legacy.legacy_comprehension@1
      if unavailable: use the in-file conservative substitute for
      `legacy_comprehension` (documented, slower, lower quality) and set
      `degraded['legacy_comprehension']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t10.parallel.parallel_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `parallel_reasoning` (documented, slower, lower quality) and set
      `degraded['parallel_reasoning']='local'`

  cap.t11.crypto.crypto_verification@1
      if unavailable: use the in-file conservative substitute for
      `crypto_verification` (documented, slower, lower quality) and set
      `degraded['crypto_verification']='local'`

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
   3. [ 600 lines] Core implementation A - API and design documentation generation from code and intent
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - doc/code drift detection and automatic repair
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - example generation with executable verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy measurement of generated documentation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_documentation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0581_code_documentation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0582-commit-history

**P0582 · `commit_history` — Version History Analysis & Blame Reasoning** · [spec](PART_SPECS_T12.md#p0582-commit-history) · [self-contained txt](../prompts/P0582_commit_history.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0582  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0582 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0582  (32/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Version History Analysis & Blame Reasoning
file         : parts/t12_code/P0582_commit_history.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.commit_history
language     : Python 3.13
capability   : cap.t12.commit.commit_history@1
determinism  : pure
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Uses the repository's past to solve its present.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. change-intent reconstruction from commits and reviews
  2. regression introduction identification (bisect-style reasoning)
  3. code-ownership and expertise mapping
  4. accuracy on curated regression-attribution tasks

Expanded obligations:
  1. Implement change-intent reconstruction from commits and reviews with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement regression introduction identification (bisect-style
     reasoning) together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's FrontierCode
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  3. Implement code-ownership and expertise mapping as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of SWE-bench Verified, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement accuracy on curated regression-attribution tasks, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.commit.commit_history@1
  cap.t12.commit.commit_history.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_documentation@1
      if unavailable: use the in-file conservative substitute for
      `code_documentation` (documented, slower, lower quality) and set
      `degraded['code_documentation']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t10.multi.multi_step_arithmetic@1
      if unavailable: use the in-file conservative substitute for
      `multi_step_arithmetic` (documented, slower, lower quality) and set
      `degraded['multi_step_arithmetic']='local'`

  cap.t11.proof.proof_assistant_ux@1
      if unavailable: use the in-file conservative substitute for
      `proof_assistant_ux` (documented, slower, lower quality) and set
      `degraded['proof_assistant_ux']='local'`

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
   3. [ 600 lines] Core implementation A - change-intent reconstruction from commits and reviews
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - regression introduction identification (bisect-style reasoning)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - code-ownership and expertise mapping
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on curated regression-attribution tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.commit.commit_history@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0582_commit_history.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0583-pr-workflow

**P0583 · `pr_workflow` — Pull Request Authoring & Review Workflow** · [spec](PART_SPECS_T12.md#p0583-pr-workflow) · [self-contained txt](../prompts/P0583_pr_workflow.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0583  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0583 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0583  (33/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Pull Request Authoring & Review Workflow
file         : parts/t12_code/P0583_pr_workflow.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.pr_workflow
language     : Python 3.13
capability   : cap.t12.pr.pr_workflow@1
determinism  : pure
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Handles the whole change lifecycle like a careful senior engineer.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. branch hygiene, template conformance and CI-expectation reasoning
  2. PR description generation with testing evidence
  3. review-feedback incorporation with change tracking
  4. measured PR acceptance rate without rework

Expanded obligations:
  1. Implement branch hygiene, template conformance and CI-expectation
     reasoning together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's FrontierCode
     Diamond target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement PR description generation with testing evidence as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement review-feedback incorporation with change tracking, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured PR acceptance rate without rework with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.pr.pr_workflow@1
  cap.t12.pr.pr_workflow.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.commit.commit_history@1
      if unavailable: use the in-file conservative substitute for
      `commit_history` (documented, slower, lower quality) and set
      `degraded['commit_history']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t10.error.error_taxonomy@1
      if unavailable: use the in-file conservative substitute for
      `error_taxonomy` (documented, slower, lower quality) and set
      `degraded['error_taxonomy']='local'`

  cap.t11.financial.financial_verification@1
      if unavailable: use the in-file conservative substitute for
      `financial_verification` (documented, slower, lower quality) and set
      `degraded['financial_verification']='local'`

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
   3. [ 600 lines] Core implementation A - branch hygiene, template conformance and CI-expectation reasonin
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - PR description generation with testing evidence
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - review-feedback incorporation with change tracking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured PR acceptance rate without rework
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.pr.pr_workflow@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0583_pr_workflow.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0584-multi-repo

**P0584 · `multi_repo` — Cross-Repository & Monorepo Coordination** · [spec](PART_SPECS_T12.md#p0584-multi-repo) · [self-contained txt](../prompts/P0584_multi_repo.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0584  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0584 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0584  (34/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Cross-Repository & Monorepo Coordination
file         : parts/t12_code/P0584_multi_repo.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.multi_repo
language     : Python 3.13
capability   : cap.t12.multi.multi_repo@1
determinism  : pure
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Coordinated changes across many repositories at once.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. cross-repo dependency and change-order planning
  2. atomic-ish multi-repo landing strategies
  3. version-skew reasoning during rollout
  4. success rate on multi-repo change tasks

Expanded obligations:
  1. Implement cross-repo dependency and change-order planning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement atomic-ish multi-repo landing strategies, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement version-skew reasoning during rollout with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement success rate on multi-repo change tasks together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.multi.multi_repo@1
  cap.t12.multi.multi_repo.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.pr.pr_workflow@1
      if unavailable: use the in-file conservative substitute for
      `pr_workflow` (documented, slower, lower quality) and set
      `degraded['pr_workflow']='local'`

  cap.t10.search.search_controller@1
      if unavailable: use the in-file conservative substitute for
      `search_controller` (documented, slower, lower quality) and set
      `degraded['search_controller']='local'`

  cap.t11.smt.smt_bridge@1
      if unavailable: use the in-file conservative substitute for
      `smt_bridge` (documented, slower, lower quality) and set
      `degraded['smt_bridge']='local'`

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
   3. [ 600 lines] Core implementation A - cross-repo dependency and change-order planning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - atomic-ish multi-repo landing strategies
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - version-skew reasoning during rollout
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - success rate on multi-repo change tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.multi.multi_repo@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0584_multi_repo.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0585-environment-setup

**P0585 · `environment_setup` — Development Environment Reconstruction** · [spec](PART_SPECS_T12.md#p0585-environment-setup) · [self-contained txt](../prompts/P0585_environment_setup.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0585  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0585 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0585  (35/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Development Environment Reconstruction
file         : parts/t12_code/P0585_environment_setup.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.environment_setup
language     : Python 3.13
capability   : cap.t12.environment.environment_setup@1
determinism  : pure
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Gets an unfamiliar project building and testing from scratch.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. environment inference from repository signals
  2. dependency installation with conflict resolution
  3. container/hermetic environment generation
  4. success rate on a corpus of arbitrary open-source projects

Expanded obligations:
  1. Implement environment inference from repository signals, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement dependency installation with conflict resolution with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement container/hermetic environment generation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  4. Implement success rate on a corpus of arbitrary open-source projects as
     a first-class, fully realised mechanism. No stub, no
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.environment.environment_setup@1
  cap.t12.environment.environment_setup.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.multi.multi_repo@1
      if unavailable: use the in-file conservative substitute for
      `multi_repo` (documented, slower, lower quality) and set
      `degraded['multi_repo']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t10.self.self_critique@1
      if unavailable: use the in-file conservative substitute for
      `self_critique` (documented, slower, lower quality) and set
      `degraded['self_critique']='local'`

  cap.t11.invariant.invariant_inference@1
      if unavailable: use the in-file conservative substitute for
      `invariant_inference` (documented, slower, lower quality) and set
      `degraded['invariant_inference']='local'`

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
   3. [ 600 lines] Core implementation A - environment inference from repository signals
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - dependency installation with conflict resolution
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - container/hermetic environment generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - success rate on a corpus of arbitrary open-source projects
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.environment.environment_setup@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0585_environment_setup.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0586-debugger-agent

**P0586 · `debugger_agent` — Interactive Debugging Agent** · [spec](PART_SPECS_T12.md#p0586-debugger-agent) · [self-contained txt](../prompts/P0586_debugger_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0586  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0586 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0586  (36/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Interactive Debugging Agent
file         : parts/t12_code/P0586_debugger_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.debugger_agent
language     : Python 3.13
capability   : cap.t12.debugger.debugger_agent@1
determinism  : pure
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Uses a real debugger the way an expert does.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. breakpoint/watchpoint strategy from hypotheses about the bug
  2. state inspection and hypothesis-driven experimentation
  3. time-travel debugging where available
  4. measured bug-resolution rate versus print-debugging baselines

Expanded obligations:
  1. Implement breakpoint/watchpoint strategy from hypotheses about the bug
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement state inspection and hypothesis-driven experimentation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of FrontierCode Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement time-travel debugging where available as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement measured bug-resolution rate versus print-debugging baselines,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.debugger.debugger_agent@1
  cap.t12.debugger.debugger_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.environment.environment_setup@1
      if unavailable: use the in-file conservative substitute for
      `environment_setup` (documented, slower, lower quality) and set
      `degraded['environment_setup']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t10.abstraction.abstraction_engine@1
      if unavailable: use the in-file conservative substitute for
      `abstraction_engine` (documented, slower, lower quality) and set
      `degraded['abstraction_engine']='local'`

  cap.t11.exact.exact_arithmetic@1
      if unavailable: use the in-file conservative substitute for
      `exact_arithmetic` (documented, slower, lower quality) and set
      `degraded['exact_arithmetic']='local'`

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
   3. [ 600 lines] Core implementation A - breakpoint/watchpoint strategy from hypotheses about the bug
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - state inspection and hypothesis-driven experimentation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - time-travel debugging where available
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured bug-resolution rate versus print-debugging baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.debugger.debugger_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0586_debugger_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0587-observability-agent

**P0587 · `observability_agent` — Production Debugging from Telemetry** · [spec](PART_SPECS_T12.md#p0587-observability-agent) · [self-contained txt](../prompts/P0587_observability_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0587  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0587 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0587  (37/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Production Debugging from Telemetry
file         : parts/t12_code/P0587_observability_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.observability_agent
language     : Python 3.13
capability   : cap.t12.observability.observability_agent@1
determinism  : pure
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Diagnoses live systems from logs, metrics and traces.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-signal correlation and anomaly localisation
  2. hypothesis generation and validation from telemetry queries
  3. incident-timeline reconstruction
  4. diagnosis accuracy on labelled incident corpora

Expanded obligations:
  1. Implement multi-signal correlation and anomaly localisation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  2. Implement hypothesis generation and validation from telemetry queries as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement incident-timeline reconstruction, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's SWE-bench Pro target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement diagnosis accuracy on labelled incident corpora with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
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
  cap.t12.observability.observability_agent@1
  cap.t12.observability.observability_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.debugger.debugger_agent@1
      if unavailable: use the in-file conservative substitute for
      `debugger_agent` (documented, slower, lower quality) and set
      `degraded['debugger_agent']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t10.spatial.spatial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `spatial_reasoning` (documented, slower, lower quality) and set
      `degraded['spatial_reasoning']='local'`

  cap.t11.property.property_testing_formal@1
      if unavailable: use the in-file conservative substitute for
      `property_testing_formal` (documented, slower, lower quality) and set
      `degraded['property_testing_formal']='local'`

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
   3. [ 600 lines] Core implementation A - multi-signal correlation and anomaly localisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hypothesis generation and validation from telemetry queries
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - incident-timeline reconstruction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - diagnosis accuracy on labelled incident corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.observability.observability_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0587_observability_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0588-data-pipeline-code

**P0588 · `data_pipeline_code` — Data & ML Pipeline Engineering** · [spec](PART_SPECS_T12.md#p0588-data-pipeline-code) · [self-contained txt](../prompts/P0588_data_pipeline_code.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0588  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0588 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0588  (38/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Data & ML Pipeline Engineering
file         : parts/t12_code/P0588_data_pipeline_code.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.data_pipeline_code
language     : Python 3.13
capability   : cap.t12.data.data_pipeline_code@1
determinism  : pure
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Correct data code: schemas, joins, leakage, reproducibility.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. schema and data-contract validation with drift detection
  2. join-correctness and cardinality reasoning
  3. train/test leakage detection in ML pipelines
  4. error detection rate on seeded data-bug corpora

Expanded obligations:
  1. Implement schema and data-contract validation with drift detection as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement join-correctness and cardinality reasoning, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement train/test leakage detection in ML pipelines with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Frontier-Bench v0.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement error detection rate on seeded data-bug corpora together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.data.data_pipeline_code@1
  cap.t12.data.data_pipeline_code.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.observability.observability_agent@1
      if unavailable: use the in-file conservative substitute for
      `observability_agent` (documented, slower, lower quality) and set
      `degraded['observability_agent']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t10.chain.chain_compression@1
      if unavailable: use the in-file conservative substitute for
      `chain_compression` (documented, slower, lower quality) and set
      `degraded['chain_compression']='local'`

  cap.t11.type.type_safety_proofs@1
      if unavailable: use the in-file conservative substitute for
      `type_safety_proofs` (documented, slower, lower quality) and set
      `degraded['type_safety_proofs']='local'`

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
   3. [ 600 lines] Core implementation A - schema and data-contract validation with drift detection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - join-correctness and cardinality reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - train/test leakage detection in ML pipelines
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - error detection rate on seeded data-bug corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.data.data_pipeline_code@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0588_data_pipeline_code.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0589-notebook-engineering

**P0589 · `notebook_engineering` — Notebook & Exploratory Code Quality** · [spec](PART_SPECS_T12.md#p0589-notebook-engineering) · [self-contained txt](../prompts/P0589_notebook_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0589  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0589 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0589  (39/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Notebook & Exploratory Code Quality
file         : parts/t12_code/P0589_notebook_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.notebook_engineering
language     : Python 3.13
capability   : cap.t12.notebook.notebook_engineering@1
determinism  : pure
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Turns exploratory analysis into reproducible engineering.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. execution-order and hidden-state hazard detection
  2. notebook-to-module refactoring with equivalence checking
  3. result reproducibility verification
  4. measured reproducibility improvement

Expanded obligations:
  1. Implement execution-order and hidden-state hazard detection, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement notebook-to-module refactoring with equivalence checking with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement result reproducibility verification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement measured reproducibility improvement as a first-class, fully
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.notebook.notebook_engineering@1
  cap.t12.notebook.notebook_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.data.data_pipeline_code@1
      if unavailable: use the in-file conservative substitute for
      `data_pipeline_code` (documented, slower, lower quality) and set
      `degraded['data_pipeline_code']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t10.reasoning.reasoning_robustness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_robustness` (documented, slower, lower quality) and set
      `degraded['reasoning_robustness']='local'`

  cap.t11.rewriting.rewriting_systems@1
      if unavailable: use the in-file conservative substitute for
      `rewriting_systems` (documented, slower, lower quality) and set
      `degraded['rewriting_systems']='local'`

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
   3. [ 600 lines] Core implementation A - execution-order and hidden-state hazard detection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - notebook-to-module refactoring with equivalence checking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - result reproducibility verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured reproducibility improvement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.notebook.notebook_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0589_notebook_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0590-frontend-engineering

**P0590 · `frontend_engineering` — Frontend & UI Code Engineering** · [spec](PART_SPECS_T12.md#p0590-frontend-engineering) · [self-contained txt](../prompts/P0590_frontend_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0590  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0590 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0590  (40/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Frontend & UI Code Engineering
file         : parts/t12_code/P0590_frontend_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.frontend_engineering
language     : Python 3.13
capability   : cap.t12.frontend.frontend_engineering@1
determinism  : pure
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Builds interfaces that actually work at every viewport.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. component architecture with accessibility and state-management rigor
  2. browser-based self-verification at multiple viewports
  3. visual-regression and layout-hazard detection
  4. measured defect rate versus Opus-class frontend baselines

Expanded obligations:
  1. Implement component architecture with accessibility and state-management
     rigor with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement browser-based self-verification at multiple viewports together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement visual-regression and layout-hazard detection as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured defect rate versus Opus-class frontend baselines, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.frontend.frontend_engineering@1
  cap.t12.frontend.frontend_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.notebook.notebook_engineering@1
      if unavailable: use the in-file conservative substitute for
      `notebook_engineering` (documented, slower, lower quality) and set
      `degraded['notebook_engineering']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t10.reasoning.reasoning_transfer@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_transfer` (documented, slower, lower quality) and set
      `degraded['reasoning_transfer']='local'`

  cap.t11.legal.legal_formalisation@1
      if unavailable: use the in-file conservative substitute for
      `legal_formalisation` (documented, slower, lower quality) and set
      `degraded['legal_formalisation']='local'`

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
   3. [ 600 lines] Core implementation A - component architecture with accessibility and state-management r
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - browser-based self-verification at multiple viewports
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - visual-regression and layout-hazard detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured defect rate versus Opus-class frontend baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.frontend.frontend_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0590_frontend_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0591-systems-programming

**P0591 · `systems_programming` — Systems & Low-Level Code Engineering** · [spec](PART_SPECS_T12.md#p0591-systems-programming) · [self-contained txt](../prompts/P0591_systems_programming.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0591  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0591 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0591  (41/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Systems & Low-Level Code Engineering
file         : parts/t12_code/P0591_systems_programming.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.systems_programming
language     : Python 3.13
capability   : cap.t12.systems.systems_programming@1
determinism  : pure
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Correct code where correctness is hardest.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. memory model, alignment and undefined-behaviour reasoning
  2. driver, embedded and kernel-adjacent code patterns
  3. hardware-interaction correctness verification
  4. success rate on systems-programming task suites

Expanded obligations:
  1. Implement memory model, alignment and undefined-behaviour reasoning
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against FrontierCode Diamond — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement driver, embedded and kernel-adjacent code patterns as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement hardware-interaction correctness verification, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Pro, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement success rate on systems-programming task suites with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
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
  cap.t12.systems.systems_programming@1
  cap.t12.systems.systems_programming.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.frontend.frontend_engineering@1
      if unavailable: use the in-file conservative substitute for
      `frontend_engineering` (documented, slower, lower quality) and set
      `degraded['frontend_engineering']='local'`

  cap.t10.thought.thought_program_ir@1
      if unavailable: use the in-file conservative substitute for
      `thought_program_ir` (documented, slower, lower quality) and set
      `degraded['thought_program_ir']='local'`

  cap.t11.logic.logic_core@1
      if unavailable: use the in-file conservative substitute for
      `logic_core` (documented, slower, lower quality) and set
      `degraded['logic_core']='local'`

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
   3. [ 600 lines] Core implementation A - memory model, alignment and undefined-behaviour reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - driver, embedded and kernel-adjacent code patterns
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - hardware-interaction correctness verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - success rate on systems-programming task suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.systems.systems_programming@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0591_systems_programming.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0592-scientific-computing-code

**P0592 · `scientific_computing_code` — Scientific & Numerical Code Engineering** · [spec](PART_SPECS_T12.md#p0592-scientific-computing-code) · [self-contained txt](../prompts/P0592_scientific_computing_code.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0592  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0592 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0592  (42/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Scientific & Numerical Code Engineering
file         : parts/t12_code/P0592_scientific_computing_code.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.scientific_computing_code
language     : Python 3.13
capability   : cap.t12.scientific.scientific_computing_code@1
determinism  : pure
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Numerically correct, not just syntactically correct.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. numerical stability and conditioning analysis of implementations
  2. unit and dimensional correctness enforcement
  3. reproducibility and determinism engineering
  4. error detection rate on seeded numerical-bug corpora

Expanded obligations:
  1. Implement numerical stability and conditioning analysis of
     implementations as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's SWE-bench Verified target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement unit and dimensional correctness enforcement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of SWE-bench Pro, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement reproducibility and determinism engineering with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement error detection rate on seeded numerical-bug corpora together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.scientific.scientific_computing_code@1
  cap.t12.scientific.scientific_computing_code.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.systems.systems_programming@1
      if unavailable: use the in-file conservative substitute for
      `systems_programming` (documented, slower, lower quality) and set
      `degraded['systems_programming']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t10.self.self_consistency@1
      if unavailable: use the in-file conservative substitute for
      `self_consistency` (documented, slower, lower quality) and set
      `degraded['self_consistency']='local'`

  cap.t11.verification.verification_conditions@1
      if unavailable: use the in-file conservative substitute for
      `verification_conditions` (documented, slower, lower quality) and set
      `degraded['verification_conditions']='local'`

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
   3. [ 600 lines] Core implementation A - numerical stability and conditioning analysis of implementations
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - unit and dimensional correctness enforcement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reproducibility and determinism engineering
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - error detection rate on seeded numerical-bug corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.scientific.scientific_computing_code@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0592_scientific_computing_code.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0593-competitive-programming

**P0593 · `competitive_programming` — Algorithmic Problem Solving Engine** · [spec](PART_SPECS_T12.md#p0593-competitive-programming) · [self-contained txt](../prompts/P0593_competitive_programming.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0593  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0593 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0593  (43/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Algorithmic Problem Solving Engine
file         : parts/t12_code/P0593_competitive_programming.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.competitive_programming
language     : Python 3.13
capability   : cap.t12.competitive.competitive_programming@1
determinism  : pure
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Solves hard algorithmic problems with proven complexity.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. algorithm selection with complexity analysis against constraints
  2. edge-case enumeration and stress testing against brute force
  3. proof of correctness for the chosen approach
  4. solve rate on contest-problem benchmark sets

Expanded obligations:
  1. Implement algorithm selection with complexity analysis against
     constraints, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. This mechanism sits on the critical path of
     SWE-bench Pro, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement edge-case enumeration and stress testing against brute force
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Frontier-Bench v0.1 — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement proof of correctness for the chosen approach together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement solve rate on contest-problem benchmark sets as a first-class,
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.competitive.competitive_programming@1
  cap.t12.competitive.competitive_programming.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.scientific.scientific_computing_code@1
      if unavailable: use the in-file conservative substitute for
      `scientific_computing_code` (documented, slower, lower quality) and
      set `degraded['scientific_computing_code']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t10.analogy.analogy_engine@1
      if unavailable: use the in-file conservative substitute for
      `analogy_engine` (documented, slower, lower quality) and set
      `degraded['analogy_engine']='local'`

  cap.t11.certified.certified_numerics@1
      if unavailable: use the in-file conservative substitute for
      `certified_numerics` (documented, slower, lower quality) and set
      `degraded['certified_numerics']='local'`

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
   3. [ 600 lines] Core implementation A - algorithm selection with complexity analysis against constraints
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - edge-case enumeration and stress testing against brute force
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - proof of correctness for the chosen approach
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - solve rate on contest-problem benchmark sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.competitive.competitive_programming@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0593_competitive_programming.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0594-code-translation

**P0594 · `code_translation` — Cross-Language Code Translation** · [spec](PART_SPECS_T12.md#p0594-code-translation) · [self-contained txt](../prompts/P0594_code_translation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0594  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0594 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0594  (44/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Cross-Language Code Translation
file         : parts/t12_code/P0594_code_translation.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_translation
language     : Python 3.13
capability   : cap.t12.code.code_translation@1
determinism  : pure
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Ports code between languages without changing behaviour.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. idiomatic translation preserving semantics and performance characteristics
  2. behavioural-equivalence verification via differential testing
  3. unsupported-construct handling with explicit reporting
  4. equivalence rate measurement on translation benchmarks

Expanded obligations:
  1. Implement idiomatic translation preserving semantics and performance
     characteristics with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Frontier-Bench v0.1
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement behavioural-equivalence verification via differential testing
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's FrontierCode Diamond target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement unsupported-construct handling with explicit reporting as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement equivalence rate measurement on translation benchmarks, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Pro — a regression on that benchmark is an automatic rejection of this
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.code.code_translation@1
  cap.t12.code.code_translation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.competitive.competitive_programming@1
      if unavailable: use the in-file conservative substitute for
      `competitive_programming` (documented, slower, lower quality) and set
      `degraded['competitive_programming']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t10.temporal.temporal_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `temporal_reasoning` (documented, slower, lower quality) and set
      `degraded['temporal_reasoning']='local'`

  cap.t11.contract.contract_checking@1
      if unavailable: use the in-file conservative substitute for
      `contract_checking` (documented, slower, lower quality) and set
      `degraded['contract_checking']='local'`

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
   3. [ 600 lines] Core implementation A - idiomatic translation preserving semantics and performance chara
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - behavioural-equivalence verification via differential testing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - unsupported-construct handling with explicit reporting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - equivalence rate measurement on translation benchmarks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_translation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0594_code_translation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0595-codebase-metrics

**P0595 · `codebase_metrics` — Codebase Health Metrics & Technical Debt** · [spec](PART_SPECS_T12.md#p0595-codebase-metrics) · [self-contained txt](../prompts/P0595_codebase_metrics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0595  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0595 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0595  (45/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Codebase Health Metrics & Technical Debt
file         : parts/t12_code/P0595_codebase_metrics.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.codebase_metrics
language     : Python 3.13
capability   : cap.t12.codebase.codebase_metrics@1
determinism  : pure
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Quantifies what is wrong with a codebase and what to fix first.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. complexity, coupling, duplication and churn metrics
  2. technical-debt quantification with remediation cost estimates
  3. prioritised remediation roadmap generation
  4. validation that metric-driven fixes reduce real defect rates

Expanded obligations:
  1. Implement complexity, coupling, duplication and churn metrics together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's FrontierCode Diamond target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement technical-debt quantification with remediation cost estimates
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement prioritised remediation roadmap generation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement validation that metric-driven fixes reduce real defect rates
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
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
  cap.t12.codebase.codebase_metrics@1
  cap.t12.codebase.codebase_metrics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_translation@1
      if unavailable: use the in-file conservative substitute for
      `code_translation` (documented, slower, lower quality) and set
      `degraded['code_translation']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t10.reasoning.reasoning_memory@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_memory` (documented, slower, lower quality) and set
      `degraded['reasoning_memory']='local'`

  cap.t11.hoare.hoare_logic_engine@1
      if unavailable: use the in-file conservative substitute for
      `hoare_logic_engine` (documented, slower, lower quality) and set
      `degraded['hoare_logic_engine']='local'`

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
   3. [ 600 lines] Core implementation A - complexity, coupling, duplication and churn metrics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - technical-debt quantification with remediation cost estimates
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - prioritised remediation roadmap generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - validation that metric-driven fixes reduce real defect rates
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.codebase.codebase_metrics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0595_codebase_metrics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0596-swe-bench-harness

**P0596 · `swe_bench_harness` — SWE-bench Family Harness** · [spec](PART_SPECS_T12.md#p0596-swe-bench-harness) · [self-contained txt](../prompts/P0596_swe_bench_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0596  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0596 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0596  (46/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : SWE-bench Family Harness
file         : parts/t12_code/P0596_swe_bench_harness.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.swe_bench_harness
language     : Python 3.13
capability   : cap.t12.swe.swe_bench_harness@1
determinism  : pure
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Reproducible measurement on the benchmarks that define coding ability.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. SWE-bench Verified/Pro harnesses with containerised evaluation
  2. minimal-bash-agent and full-scaffold modes for fair comparison
  3. per-instance failure analysis and error taxonomy
  4. targets: Verified 99.8% (Opus 5: 97.0%), Pro 96.5%

Expanded obligations:
  1. Implement SWE-bench Verified/Pro harnesses with containerised evaluation
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of SWE-bench Verified, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement minimal-bash-agent and full-scaffold modes for fair
     comparison, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against SWE-bench
     Pro — a regression on that benchmark is an automatic rejection of this
     part.
  3. Implement per-instance failure analysis and error taxonomy with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement targets: Verified 99.8% (Opus 5: 97.0%), Pro 96.5% together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.swe.swe_bench_harness@1
  cap.t12.swe.swe_bench_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.codebase.codebase_metrics@1
      if unavailable: use the in-file conservative substitute for
      `codebase_metrics` (documented, slower, lower quality) and set
      `degraded['codebase_metrics']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t10.reasoning.reasoning_faithfulness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_faithfulness` (documented, slower, lower quality) and set
      `degraded['reasoning_faithfulness']='local'`

  cap.t11.decision.decision_procedures@1
      if unavailable: use the in-file conservative substitute for
      `decision_procedures` (documented, slower, lower quality) and set
      `degraded['decision_procedures']='local'`

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
   3. [ 600 lines] Core implementation A - SWE-bench Verified/Pro harnesses with containerised evaluation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - minimal-bash-agent and full-scaffold modes for fair comparison
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-instance failure analysis and error taxonomy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - targets: Verified 99.8% (Opus 5: 97.0%), Pro 96.5%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.swe.swe_bench_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0596_swe_bench_harness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0597-frontier-bench-harness

**P0597 · `frontier_bench_harness` — Frontier-Bench & Terminal Coding Harness** · [spec](PART_SPECS_T12.md#p0597-frontier-bench-harness) · [self-contained txt](../prompts/P0597_frontier_bench_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0597  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0597 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0597  (47/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Frontier-Bench & Terminal Coding Harness
file         : parts/t12_code/P0597_frontier_bench_harness.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.frontier_bench_harness
language     : Python 3.13
capability   : cap.t12.frontier.frontier_bench_harness@1
determinism  : pure
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
The hardest agentic coding evaluations.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. Frontier-Bench v0.1 style long-horizon task harness
  2. Terminal-Bench 2.1 harness with environment fidelity
  3. task-level diagnostics and capability attribution
  4. targets: Frontier-Bench 92% (Opus 5: 43.3%), Terminal-Bench 98.5%

Expanded obligations:
  1. Implement Frontier-Bench v0.1 style long-horizon task harness, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against SWE-bench Pro — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement Terminal-Bench 2.1 harness with environment fidelity with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement task-level diagnostics and capability attribution together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of FrontierCode Diamond, so its p99 latency assertion
     is part of the acceptance criteria, not an optional extra.
  4. Implement targets: Frontier-Bench 92% (Opus 5: 43.3%), Terminal-Bench
     98.5% as a first-class, fully realised mechanism. No stub, no
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.frontier.frontier_bench_harness@1
  cap.t12.frontier.frontier_bench_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.swe.swe_bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `swe_bench_harness` (documented, slower, lower quality) and set
      `degraded['swe_bench_harness']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t10.subgoal.subgoal_caching@1
      if unavailable: use the in-file conservative substitute for
      `subgoal_caching` (documented, slower, lower quality) and set
      `degraded['subgoal_caching']='local'`

  cap.t11.scientific.scientific_verification@1
      if unavailable: use the in-file conservative substitute for
      `scientific_verification` (documented, slower, lower quality) and set
      `degraded['scientific_verification']='local'`

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
   3. [ 600 lines] Core implementation A - Frontier-Bench v0.1 style long-horizon task harness
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - Terminal-Bench 2.1 harness with environment fidelity
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - task-level diagnostics and capability attribution
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - targets: Frontier-Bench 92% (Opus 5: 43.3%), Terminal-Bench 98.5
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.frontier.frontier_bench_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0597_frontier_bench_harness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0598-cursorbench-harness

**P0598 · `cursorbench_harness` — IDE-Integrated Coding Evaluation** · [spec](PART_SPECS_T12.md#p0598-cursorbench-harness) · [self-contained txt](../prompts/P0598_cursorbench_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0598  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0598 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0598  (48/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : IDE-Integrated Coding Evaluation
file         : parts/t12_code/P0598_cursorbench_harness.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.cursorbench_harness
language     : Python 3.13
capability   : cap.t12.cursorbench.cursorbench_harness@1
determinism  : pure
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Measures real developer-workflow performance, not just benchmarks.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. CursorBench-style harness with edit-application fidelity
  2. latency and cost-per-task measurement alongside quality
  3. developer-workflow task library
  4. target: 140% of Opus 5's CursorBench-relative score at lower cost

Expanded obligations:
  1. Implement CursorBench-style harness with edit-application fidelity with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement latency and cost-per-task measurement alongside quality
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of FrontierCode Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement developer-workflow task library as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against SWE-bench Verified — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement target: 140% of Opus 5's CursorBench-relative score at lower
     cost, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     SWE-bench Pro target reachable; the part therefore ships a
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.cursorbench.cursorbench_harness@1
  cap.t12.cursorbench.cursorbench_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.frontier.frontier_bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `frontier_bench_harness` (documented, slower, lower quality) and set
      `degraded['frontier_bench_harness']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t10.reasoning.reasoning_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_spec_doc` (documented, slower, lower quality) and set
      `degraded['reasoning_spec_doc']='local'`

  cap.t11.formal.formal_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `formal_spec_doc` (documented, slower, lower quality) and set
      `degraded['formal_spec_doc']='local'`

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
   3. [ 600 lines] Core implementation A - CursorBench-style harness with edit-application fidelity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - latency and cost-per-task measurement alongside quality
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - developer-workflow task library
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: 140% of Opus 5's CursorBench-relative score at lower cos
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.cursorbench.cursorbench_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0598_cursorbench_harness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0599-code-quality-gate

**P0599 · `code_quality_gate` — Code Quality Gate for the 1000-Part Assembly** · [spec](PART_SPECS_T12.md#p0599-code-quality-gate) · [self-contained txt](../prompts/P0599_code_quality_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0599  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0599 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0599  (49/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Code Quality Gate for the 1000-Part Assembly
file         : parts/t12_code/P0599_code_quality_gate.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_quality_gate
language     : Python 3.13
capability   : cap.t12.code.code_quality_gate@1
determinism  : pure
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
Applies this tier's own capabilities to the project itself.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. automated review of all 1000 part files against the Ω-Contract
  2. cross-part consistency and duplication detection
  3. per-part quality scorecard with remediation guidance
  4. assembly-wide quality report generation

Expanded obligations:
  1. Implement automated review of all 1000 part files against the Ω-Contract
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of FrontierCode Diamond, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement cross-part consistency and duplication detection as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement per-part quality scorecard with remediation guidance, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's SWE-bench Pro target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement assembly-wide quality report generation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Frontier-Bench v0.1, so its p99 latency
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.code.code_quality_gate@1
  cap.t12.code.code_quality_gate.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.cursorbench.cursorbench_harness@1
      if unavailable: use the in-file conservative substitute for
      `cursorbench_harness` (documented, slower, lower quality) and set
      `degraded['cursorbench_harness']='local'`

  cap.t10.outcome.outcome_verifier@1
      if unavailable: use the in-file conservative substitute for
      `outcome_verifier` (documented, slower, lower quality) and set
      `degraded['outcome_verifier']='local'`

  cap.t11.proof.proof_certificate@1
      if unavailable: use the in-file conservative substitute for
      `proof_certificate` (documented, slower, lower quality) and set
      `degraded['proof_certificate']='local'`

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
   3. [ 600 lines] Core implementation A - automated review of all 1000 part files against the Ω-Contract
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-part consistency and duplication detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-part quality scorecard with remediation guidance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - assembly-wide quality report generation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_quality_gate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0599_code_quality_gate.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0600-code-spec-doc

**P0600 · `code_spec_doc` — Code Intelligence Specification & Capability Register** · [spec](PART_SPECS_T12.md#p0600-code-spec-doc) · [self-contained txt](../prompts/P0600_code_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0600  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0600 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0600  (50/50 of tier T12)
tier         : T12 — Code Intelligence & Repository Surgery
title        : Code Intelligence Specification & Capability Register
file         : parts/t12_code/P0600_code_spec_doc.py          <-- create exactly this path, nothing else
module       : hyperion.t12.code.code_spec_doc
language     : Python 3.13
capability   : cap.t12.code.code_spec_doc@1
determinism  : pure
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

MISSION
-------
The authoritative description of all code capabilities and their limits.

Tier context:
  Whole-repository semantic understanding, patch synthesis, test synthesis and
  root-cause analysis. Owns the SWE/Frontier benchmark family.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capability register with measured performance per task class
  2. honest limitation documentation
  3. benchmark-result aggregation with provenance
  4. drift detection between claims and measurements

Expanded obligations:
  1. Implement capability register with measured performance per task class
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against SWE-bench Verified — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement honest limitation documentation, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's SWE-bench Pro target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement benchmark-result aggregation with provenance with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Frontier-Bench v0.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement drift detection between claims and measurements together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against FrontierCode Diamond — a regression on that benchmark
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t12.code.code_spec_doc@1
  cap.t12.code.code_spec_doc.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t12.code.code_quality_gate@1
      if unavailable: use the in-file conservative substitute for
      `code_quality_gate` (documented, slower, lower quality) and set
      `degraded['code_quality_gate']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t10.constraint.constraint_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `constraint_reasoning` (documented, slower, lower quality) and set
      `degraded['constraint_reasoning']='local'`

  cap.t11.termination.termination_analysis@1
      if unavailable: use the in-file conservative substitute for
      `termination_analysis` (documented, slower, lower quality) and set
      `degraded['termination_analysis']='local'`

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
   3. [ 600 lines] Core implementation A - capability register with measured performance per task class
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - honest limitation documentation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - benchmark-result aggregation with provenance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - drift detection between claims and measurements
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t12.code.code_spec_doc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t12_code/P0600_code_spec_doc.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
