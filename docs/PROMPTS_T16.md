# HYPERION-Ω — Worker prompts · T16 · Domain Superintelligence Packs

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

## PROMPT p0751-domain-pack-framework

**P0751 · `domain_pack_framework` — Domain Pack Framework & Interface** · [spec](PART_SPECS_T16.md#p0751-domain-pack-framework) · [self-contained txt](../prompts/P0751_domain_pack_framework.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0751  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0751 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0751  (1/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Domain Pack Framework & Interface
file         : parts/t16_domains/P0751_domain_pack_framework.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.domain_pack_framework
language     : Python 3.13
capability   : cap.t16.domain.domain_pack_framework@1
determinism  : pure
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
The uniform structure every domain expertise module follows.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. domain pack schema: ontology, verifiers, tools, benchmarks, guardrails
  2. capability registration and routing by detected domain
  3. domain-confidence estimation and cross-domain handoff
  4. pack conformance test suite all 40 domain packs must pass

Expanded obligations:
  1. Implement domain pack schema: ontology, verifiers, tools, benchmarks,
     guardrails together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Life-sciences
     suite target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement capability registration and routing by detected domain as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement domain-confidence estimation and cross-domain handoff, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement pack conformance test suite all 40 domain packs must pass with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.domain.domain_pack_framework@1
  cap.t16.domain.domain_pack_framework.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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
   3. [ 600 lines] Core implementation A - domain pack schema: ontology, verifiers, tools, benchmarks, guar
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability registration and routing by detected domain
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - domain-confidence estimation and cross-domain handoff
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - pack conformance test suite all 40 domain packs must pass
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.domain.domain_pack_framework@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0751_domain_pack_framework.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0752-domain-detection

**P0752 · `domain_detection` — Domain Detection & Expert Routing** · [spec](PART_SPECS_T16.md#p0752-domain-detection) · [self-contained txt](../prompts/P0752_domain_detection.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0752  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0752 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0752  (2/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Domain Detection & Expert Routing
file         : parts/t16_domains/P0752_domain_detection.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.domain_detection
language     : Python 3.13
capability   : cap.t16.domain.domain_detection@1
determinism  : pure
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Recognises the field of a question and engages the right expertise.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-label domain classification with confidence and ambiguity handling
  2. sub-domain and interdisciplinary detection
  3. routing policy engaging multiple packs when needed
  4. routing-accuracy measurement on domain-labelled corpora

Expanded obligations:
  1. Implement multi-label domain classification with confidence and
     ambiguity handling as a first-class, fully realised mechanism. No stub,
     no `NotImplementedError`, no configuration flag whose default disables
     it. Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement sub-domain and interdisciplinary detection, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement routing policy engaging multiple packs when needed with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement routing-accuracy measurement on domain-labelled corpora
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
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
  cap.t16.domain.domain_detection@1
  cap.t16.domain.domain_detection.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.domain.domain_pack_framework@1
      if unavailable: use the in-file conservative substitute for
      `domain_pack_framework` (documented, slower, lower quality) and set
      `degraded['domain_pack_framework']='local'`

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
   3. [ 600 lines] Core implementation A - multi-label domain classification with confidence and ambiguity 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - sub-domain and interdisciplinary detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - routing policy engaging multiple packs when needed
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - routing-accuracy measurement on domain-labelled corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.domain.domain_detection@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0752_domain_detection.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0753-molecular-biology

**P0753 · `molecular_biology` — Molecular & Cell Biology** · [spec](PART_SPECS_T16.md#p0753-molecular-biology) · [self-contained txt](../prompts/P0753_molecular_biology.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0753  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0753 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0753  (3/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Molecular & Cell Biology
file         : parts/t16_domains/P0753_molecular_biology.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.molecular_biology
language     : Python 3.13
capability   : cap.t16.molecular.molecular_biology@1
determinism  : pure
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Expert-level reasoning about molecular mechanism.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. pathway, regulation and mechanism reasoning with literature grounding
  2. experimental-design and control reasoning for molecular assays
  3. database integration (sequence, structure, pathway, expression)
  4. accuracy versus PhD-level biology question sets

Expanded obligations:
  1. Implement pathway, regulation and mechanism reasoning with literature
     grounding, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement experimental-design and control reasoning for molecular assays
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement database integration (sequence, structure, pathway,
     expression) together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  4. Implement accuracy versus PhD-level biology question sets as a
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.molecular.molecular_biology@1
  cap.t16.molecular.molecular_biology.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.domain.domain_detection@1
      if unavailable: use the in-file conservative substitute for
      `domain_detection` (documented, slower, lower quality) and set
      `degraded['domain_detection']='local'`

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
   3. [ 600 lines] Core implementation A - pathway, regulation and mechanism reasoning with literature grou
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - experimental-design and control reasoning for molecular assays
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - database integration (sequence, structure, pathway, expression)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy versus PhD-level biology question sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.molecular.molecular_biology@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0753_molecular_biology.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0754-structural-biology

**P0754 · `structural_biology` — Structural Biology & Protein Science** · [spec](PART_SPECS_T16.md#p0754-structural-biology) · [self-contained txt](../prompts/P0754_structural_biology.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0754  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0754 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0754  (4/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Structural Biology & Protein Science
file         : parts/t16_domains/P0754_structural_biology.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.structural_biology
language     : Python 3.13
capability   : cap.t16.structural.structural_biology@1
determinism  : pure
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Reasons about structure, folding and function.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structure-function reasoning with geometric and energetic analysis
  2. variant-effect prediction on protein function and stability
  3. structure-prediction tool orchestration and result validation
  4. target: exceed Opus 5's +7.7pp protein-task improvement substantially

Expanded obligations:
  1. Implement structure-function reasoning with geometric and energetic
     analysis with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Life-sciences
     suite target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement variant-effect prediction on protein function and stability
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement structure-prediction tool orchestration and result validation
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement target: exceed Opus 5's +7.7pp protein-task improvement
     substantially, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.structural.structural_biology@1
  cap.t16.structural.structural_biology.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.molecular.molecular_biology@1
      if unavailable: use the in-file conservative substitute for
      `molecular_biology` (documented, slower, lower quality) and set
      `degraded['molecular_biology']='local'`

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
   3. [ 600 lines] Core implementation A - structure-function reasoning with geometric and energetic analys
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - variant-effect prediction on protein function and stability
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - structure-prediction tool orchestration and result validation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: exceed Opus 5's +7.7pp protein-task improvement substant
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.structural.structural_biology@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0754_structural_biology.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0755-genomics-bioinformatics

**P0755 · `genomics_bioinformatics` — Genomics & Bioinformatics** · [spec](PART_SPECS_T16.md#p0755-genomics-bioinformatics) · [self-contained txt](../prompts/P0755_genomics_bioinformatics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0755  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0755 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0755  (5/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Genomics & Bioinformatics
file         : parts/t16_domains/P0755_genomics_bioinformatics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.genomics_bioinformatics
language     : Python 3.13
capability   : cap.t16.genomics.genomics_bioinformatics@1
determinism  : pure
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Careful, statistically correct genomic analysis.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. pipeline construction with correct QC, normalisation and batch handling
  2. statistical rigor: multiple testing, confounders, independent cross-checks
  3. variant interpretation with evidence-tier classification
  4. accuracy on curated genomic-analysis tasks with known answers

Expanded obligations:
  1. Implement pipeline construction with correct QC, normalisation and batch
     handling together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement statistical rigor: multiple testing, confounders, independent
     cross-checks as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement variant interpretation with evidence-tier classification, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement accuracy on curated genomic-analysis tasks with known answers
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.genomics.genomics_bioinformatics@1
  cap.t16.genomics.genomics_bioinformatics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.structural.structural_biology@1
      if unavailable: use the in-file conservative substitute for
      `structural_biology` (documented, slower, lower quality) and set
      `degraded['structural_biology']='local'`

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
   3. [ 600 lines] Core implementation A - pipeline construction with correct QC, normalisation and batch h
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - statistical rigor: multiple testing, confounders, independent cr
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - variant interpretation with evidence-tier classification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on curated genomic-analysis tasks with known answers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.genomics.genomics_bioinformatics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0755_genomics_bioinformatics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0756-organic-chemistry

**P0756 · `organic_chemistry` — Organic Chemistry & Synthesis** · [spec](PART_SPECS_T16.md#p0756-organic-chemistry) · [self-contained txt](../prompts/P0756_organic_chemistry.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0756  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0756 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0756  (6/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Organic Chemistry & Synthesis
file         : parts/t16_domains/P0756_organic_chemistry.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.organic_chemistry
language     : Python 3.13
capability   : cap.t16.organic.organic_chemistry@1
determinism  : pure
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Predicts and plans real chemistry.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. retrosynthetic planning with feasibility and cost reasoning
  2. reaction-mechanism and selectivity prediction
  3. spectroscopic structure elucidation from raw spectral data
  4. target: exceed Opus 5's +10.2pp organic-chemistry improvement substantially

Expanded obligations:
  1. Implement retrosynthetic planning with feasibility and cost reasoning as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement reaction-mechanism and selectivity prediction, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement spectroscopic structure elucidation from raw spectral data
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement target: exceed Opus 5's +10.2pp organic-chemistry improvement
     substantially together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against GPQA Diamond — a
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
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.organic.organic_chemistry@1
  cap.t16.organic.organic_chemistry.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.genomics.genomics_bioinformatics@1
      if unavailable: use the in-file conservative substitute for
      `genomics_bioinformatics` (documented, slower, lower quality) and set
      `degraded['genomics_bioinformatics']='local'`

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
   3. [ 600 lines] Core implementation A - retrosynthetic planning with feasibility and cost reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - reaction-mechanism and selectivity prediction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - spectroscopic structure elucidation from raw spectral data
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: exceed Opus 5's +10.2pp organic-chemistry improvement su
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.organic.organic_chemistry@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0756_organic_chemistry.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0757-computational-chemistry

**P0757 · `computational_chemistry` — Computational & Physical Chemistry** · [spec](PART_SPECS_T16.md#p0757-computational-chemistry) · [self-contained txt](../prompts/P0757_computational_chemistry.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0757  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0757 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0757  (7/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Computational & Physical Chemistry
file         : parts/t16_domains/P0757_computational_chemistry.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.computational_chemistry
language     : Python 3.13
capability   : cap.t16.computational.computational_chemistry@1
determinism  : pure
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Correct quantum and thermodynamic reasoning.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. method selection (DFT, MD, semi-empirical) with accuracy/cost tradeoffs
  2. thermodynamic and kinetic property reasoning with unit rigor
  3. simulation setup, execution and result validation
  4. accuracy against experimental reference datasets

Expanded obligations:
  1. Implement method selection (DFT, MD, semi-empirical) with accuracy/cost
     tradeoffs, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement thermodynamic and kinetic property reasoning with unit rigor
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement simulation setup, execution and result validation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy against experimental reference datasets as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
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
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.computational.computational_chemistry@1
  cap.t16.computational.computational_chemistry.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.organic.organic_chemistry@1
      if unavailable: use the in-file conservative substitute for
      `organic_chemistry` (documented, slower, lower quality) and set
      `degraded['organic_chemistry']='local'`

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
   3. [ 600 lines] Core implementation A - method selection (DFT, MD, semi-empirical) with accuracy/cost tr
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - thermodynamic and kinetic property reasoning with unit rigor
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - simulation setup, execution and result validation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy against experimental reference datasets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.computational.computational_chemistry@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0757_computational_chemistry.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0758-materials-science

**P0758 · `materials_science` — Materials Science & Engineering** · [spec](PART_SPECS_T16.md#p0758-materials-science) · [self-contained txt](../prompts/P0758_materials_science.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0758  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0758 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0758  (8/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Materials Science & Engineering
file         : parts/t16_domains/P0758_materials_science.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.materials_science
language     : Python 3.13
capability   : cap.t16.materials.materials_science@1
determinism  : pure
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Designs and evaluates materials for real requirements.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structure-property relationship reasoning across material classes
  2. processing-route and manufacturability reasoning
  3. characterisation-data interpretation
  4. accuracy on materials-property prediction benchmarks

Expanded obligations:
  1. Implement structure-property relationship reasoning across material
     classes with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement processing-route and manufacturability reasoning together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement characterisation-data interpretation as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement accuracy on materials-property prediction benchmarks, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
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
  cap.t16.materials.materials_science@1
  cap.t16.materials.materials_science.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.computational.computational_chemistry@1
      if unavailable: use the in-file conservative substitute for
      `computational_chemistry` (documented, slower, lower quality) and set
      `degraded['computational_chemistry']='local'`

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
   3. [ 600 lines] Core implementation A - structure-property relationship reasoning across material classe
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - processing-route and manufacturability reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - characterisation-data interpretation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on materials-property prediction benchmarks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.materials.materials_science@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0758_materials_science.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0759-drug-discovery

**P0759 · `drug_discovery` — Medicinal Chemistry & Drug Discovery** · [spec](PART_SPECS_T16.md#p0759-drug-discovery) · [self-contained txt](../prompts/P0759_drug_discovery.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0759  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0759 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0759  (9/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Medicinal Chemistry & Drug Discovery
file         : parts/t16_domains/P0759_drug_discovery.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.drug_discovery
language     : Python 3.13
capability   : cap.t16.drug.drug_discovery@1
determinism  : pure
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Scientifically strong, with strict dual-use safeguards.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. target validation, lead optimisation and ADMET reasoning
  2. structure-activity relationship analysis
  3. mandatory dual-use gating via T19 for hazardous applications
  4. accuracy on medicinal-chemistry task suites within safety scope

Expanded obligations:
  1. Implement target validation, lead optimisation and ADMET reasoning
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement structure-activity relationship analysis as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement mandatory dual-use gating via T19 for hazardous applications,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement accuracy on medicinal-chemistry task suites within safety
     scope with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against GPQA Diamond — a
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.drug.drug_discovery@1
  cap.t16.drug.drug_discovery.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.materials.materials_science@1
      if unavailable: use the in-file conservative substitute for
      `materials_science` (documented, slower, lower quality) and set
      `degraded['materials_science']='local'`

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
   3. [ 600 lines] Core implementation A - target validation, lead optimisation and ADMET reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - structure-activity relationship analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - mandatory dual-use gating via T19 for hazardous applications
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on medicinal-chemistry task suites within safety scope
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.drug.drug_discovery@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0759_drug_discovery.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0760-clinical-medicine

**P0760 · `clinical_medicine` — Clinical Medicine & Diagnostics** · [spec](PART_SPECS_T16.md#p0760-clinical-medicine) · [self-contained txt](../prompts/P0760_clinical_medicine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0760  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0760 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0760  (10/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Clinical Medicine & Diagnostics
file         : parts/t16_domains/P0760_clinical_medicine.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.clinical_medicine
language     : Python 3.13
capability   : cap.t16.clinical.clinical_medicine@1
determinism  : pure
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Clinician-grade reasoning with clinician-grade humility.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. differential-diagnosis generation with calibrated probabilities
  2. evidence-based guideline application with contraindication checking
  3. mandatory clinical-oversight framing and scope limitation
  4. accuracy versus physician consensus on curated cases

Expanded obligations:
  1. Implement differential-diagnosis generation with calibrated
     probabilities as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement evidence-based guideline application with contraindication
     checking, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement mandatory clinical-oversight framing and scope limitation with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement accuracy versus physician consensus on curated cases together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.clinical.clinical_medicine@1
  cap.t16.clinical.clinical_medicine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.drug.drug_discovery@1
      if unavailable: use the in-file conservative substitute for
      `drug_discovery` (documented, slower, lower quality) and set
      `degraded['drug_discovery']='local'`

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
   3. [ 600 lines] Core implementation A - differential-diagnosis generation with calibrated probabilities
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - evidence-based guideline application with contraindication check
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - mandatory clinical-oversight framing and scope limitation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy versus physician consensus on curated cases
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.clinical.clinical_medicine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0760_clinical_medicine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0761-epidemiology-publichealth

**P0761 · `epidemiology_publichealth` — Epidemiology & Public Health** · [spec](PART_SPECS_T16.md#p0761-epidemiology-publichealth) · [self-contained txt](../prompts/P0761_epidemiology_publichealth.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0761  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0761 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0761  (11/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Epidemiology & Public Health
file         : parts/t16_domains/P0761_epidemiology_publichealth.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.epidemiology_publichealth
language     : Python 3.13
capability   : cap.t16.epidemiology.epidemiology_publichealth@1
determinism  : pure
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Population-level reasoning done correctly.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. study-design reasoning with bias and confounding analysis
  2. epidemiological modelling with parameter-uncertainty propagation
  3. surveillance-data interpretation
  4. accuracy on epidemiological-reasoning benchmark sets

Expanded obligations:
  1. Implement study-design reasoning with bias and confounding analysis, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement epidemiological modelling with parameter-uncertainty
     propagation with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement surveillance-data interpretation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement accuracy on epidemiological-reasoning benchmark sets as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
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
  cap.t16.epidemiology.epidemiology_publichealth@1
  cap.t16.epidemiology.epidemiology_publichealth.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.clinical.clinical_medicine@1
      if unavailable: use the in-file conservative substitute for
      `clinical_medicine` (documented, slower, lower quality) and set
      `degraded['clinical_medicine']='local'`

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
   3. [ 600 lines] Core implementation A - study-design reasoning with bias and confounding analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - epidemiological modelling with parameter-uncertainty propagation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - surveillance-data interpretation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on epidemiological-reasoning benchmark sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.epidemiology.epidemiology_publichealth@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0761_epidemiology_publichealth.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0762-neuroscience

**P0762 · `neuroscience` — Neuroscience & Cognitive Science** · [spec](PART_SPECS_T16.md#p0762-neuroscience) · [self-contained txt](../prompts/P0762_neuroscience.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0762  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0762 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0762  (12/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Neuroscience & Cognitive Science
file         : parts/t16_domains/P0762_neuroscience.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.neuroscience
language     : Python 3.13
capability   : cap.t16.neuroscience.neuroscience@1
determinism  : pure
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Reasons about brains and minds rigorously.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-scale reasoning from molecular to behavioural
  2. neuroimaging and electrophysiology data interpretation
  3. cognitive-model reasoning with experimental grounding
  4. accuracy on graduate-level neuroscience question sets

Expanded obligations:
  1. Implement multi-scale reasoning from molecular to behavioural with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement neuroimaging and electrophysiology data interpretation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement cognitive-model reasoning with experimental grounding as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement accuracy on graduate-level neuroscience question sets, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.neuroscience.neuroscience@1
  cap.t16.neuroscience.neuroscience.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.epidemiology.epidemiology_publichealth@1
      if unavailable: use the in-file conservative substitute for
      `epidemiology_publichealth` (documented, slower, lower quality) and
      set `degraded['epidemiology_publichealth']='local'`

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
   3. [ 600 lines] Core implementation A - multi-scale reasoning from molecular to behavioural
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - neuroimaging and electrophysiology data interpretation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cognitive-model reasoning with experimental grounding
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on graduate-level neuroscience question sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.neuroscience.neuroscience@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0762_neuroscience.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0763-theoretical-physics

**P0763 · `theoretical_physics` — Theoretical & Mathematical Physics** · [spec](PART_SPECS_T16.md#p0763-theoretical-physics) · [self-contained txt](../prompts/P0763_theoretical_physics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0763  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0763 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0763  (13/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Theoretical & Mathematical Physics
file         : parts/t16_domains/P0763_theoretical_physics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.theoretical_physics
language     : Python 3.13
capability   : cap.t16.theoretical.theoretical_physics@1
determinism  : pure
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Derives, does not recall.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. derivation from first principles with dimensional and limit checking
  2. symmetry, conservation-law and effective-theory reasoning
  3. connection to experimental observables with error analysis
  4. accuracy on graduate-level physics problem sets

Expanded obligations:
  1. Implement derivation from first principles with dimensional and limit
     checking together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Life-sciences
     suite target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement symmetry, conservation-law and effective-theory reasoning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement connection to experimental observables with error analysis,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  4. Implement accuracy on graduate-level physics problem sets with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
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
  cap.t16.theoretical.theoretical_physics@1
  cap.t16.theoretical.theoretical_physics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.neuroscience.neuroscience@1
      if unavailable: use the in-file conservative substitute for
      `neuroscience` (documented, slower, lower quality) and set
      `degraded['neuroscience']='local'`

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
   3. [ 600 lines] Core implementation A - derivation from first principles with dimensional and limit chec
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - symmetry, conservation-law and effective-theory reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - connection to experimental observables with error analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on graduate-level physics problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.theoretical.theoretical_physics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0763_theoretical_physics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0764-applied-physics

**P0764 · `applied_physics` — Applied & Experimental Physics** · [spec](PART_SPECS_T16.md#p0764-applied-physics) · [self-contained txt](../prompts/P0764_applied_physics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0764  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0764 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0764  (14/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Applied & Experimental Physics
file         : parts/t16_domains/P0764_applied_physics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.applied_physics
language     : Python 3.13
capability   : cap.t16.applied.applied_physics@1
determinism  : pure
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Designs experiments and interprets real data.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. measurement-uncertainty and error-budget analysis
  2. apparatus and instrument reasoning with systematic-error identification
  3. data-fitting with model-selection rigor
  4. accuracy on experimental-physics analysis tasks

Expanded obligations:
  1. Implement measurement-uncertainty and error-budget analysis as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement apparatus and instrument reasoning with systematic-error
     identification, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement data-fitting with model-selection rigor with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Life-sciences suite target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement accuracy on experimental-physics analysis tasks together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.applied.applied_physics@1
  cap.t16.applied.applied_physics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.theoretical.theoretical_physics@1
      if unavailable: use the in-file conservative substitute for
      `theoretical_physics` (documented, slower, lower quality) and set
      `degraded['theoretical_physics']='local'`

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
   3. [ 600 lines] Core implementation A - measurement-uncertainty and error-budget analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - apparatus and instrument reasoning with systematic-error identif
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - data-fitting with model-selection rigor
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on experimental-physics analysis tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.applied.applied_physics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0764_applied_physics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0765-astronomy-astrophysics

**P0765 · `astronomy_astrophysics` — Astronomy & Astrophysics** · [spec](PART_SPECS_T16.md#p0765-astronomy-astrophysics) · [self-contained txt](../prompts/P0765_astronomy_astrophysics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0765  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0765 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0765  (15/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Astronomy & Astrophysics
file         : parts/t16_domains/P0765_astronomy_astrophysics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.astronomy_astrophysics
language     : Python 3.13
capability   : cap.t16.astronomy.astronomy_astrophysics@1
determinism  : pure
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Handles astronomical data and scales correctly.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. observational-data reduction and analysis reasoning
  2. scale, unit and cosmological-convention rigor
  3. survey-data querying and interpretation
  4. accuracy on astrophysics problem and data-analysis sets

Expanded obligations:
  1. Implement observational-data reduction and analysis reasoning, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement scale, unit and cosmological-convention rigor with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Life-sciences suite target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement survey-data querying and interpretation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement accuracy on astrophysics problem and data-analysis sets as a
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.astronomy.astronomy_astrophysics@1
  cap.t16.astronomy.astronomy_astrophysics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.applied.applied_physics@1
      if unavailable: use the in-file conservative substitute for
      `applied_physics` (documented, slower, lower quality) and set
      `degraded['applied_physics']='local'`

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
   3. [ 600 lines] Core implementation A - observational-data reduction and analysis reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - scale, unit and cosmological-convention rigor
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - survey-data querying and interpretation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on astrophysics problem and data-analysis sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.astronomy.astronomy_astrophysics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0765_astronomy_astrophysics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0766-earth-climate

**P0766 · `earth_climate` — Earth & Climate Science** · [spec](PART_SPECS_T16.md#p0766-earth-climate) · [self-contained txt](../prompts/P0766_earth_climate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0766  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0766 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0766  (16/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Earth & Climate Science
file         : parts/t16_domains/P0766_earth_climate.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.earth_climate
language     : Python 3.13
capability   : cap.t16.earth.earth_climate@1
determinism  : pure
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Rigorous, honest climate and earth-system reasoning.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. climate-model output interpretation with uncertainty communication
  2. geophysical data analysis and attribution reasoning
  3. scenario reasoning with explicit assumption statements
  4. accuracy on earth-science analysis benchmarks

Expanded obligations:
  1. Implement climate-model output interpretation with uncertainty
     communication with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Life-sciences
     suite target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement geophysical data analysis and attribution reasoning together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement scenario reasoning with explicit assumption statements as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy on earth-science analysis benchmarks, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Life-sciences suite target
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.earth.earth_climate@1
  cap.t16.earth.earth_climate.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.astronomy.astronomy_astrophysics@1
      if unavailable: use the in-file conservative substitute for
      `astronomy_astrophysics` (documented, slower, lower quality) and set
      `degraded['astronomy_astrophysics']='local'`

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
   3. [ 600 lines] Core implementation A - climate-model output interpretation with uncertainty communicati
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - geophysical data analysis and attribution reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - scenario reasoning with explicit assumption statements
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on earth-science analysis benchmarks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.earth.earth_climate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0766_earth_climate.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0767-pure-mathematics

**P0767 · `pure_mathematics` — Pure Mathematics** · [spec](PART_SPECS_T16.md#p0767-pure-mathematics) · [self-contained txt](../prompts/P0767_pure_mathematics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0767  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0767 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0767  (17/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Pure Mathematics
file         : parts/t16_domains/P0767_pure_mathematics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.pure_mathematics
language     : Python 3.13
capability   : cap.t16.pure.pure_mathematics@1
determinism  : pure
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Proves theorems, does not gesture at them.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. proof construction across algebra, analysis, topology and combinatorics
  2. counterexample construction and conjecture evaluation
  3. formal-verification handoff for critical proofs
  4. accuracy on research-level mathematics problem sets

Expanded obligations:
  1. Implement proof construction across algebra, analysis, topology and
     combinatorics together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement counterexample construction and conjecture evaluation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement formal-verification handoff for critical proofs, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement accuracy on research-level mathematics problem sets with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.pure.pure_mathematics@1
  cap.t16.pure.pure_mathematics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.earth.earth_climate@1
      if unavailable: use the in-file conservative substitute for
      `earth_climate` (documented, slower, lower quality) and set
      `degraded['earth_climate']='local'`

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
   3. [ 600 lines] Core implementation A - proof construction across algebra, analysis, topology and combin
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - counterexample construction and conjecture evaluation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - formal-verification handoff for critical proofs
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on research-level mathematics problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.pure.pure_mathematics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0767_pure_mathematics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0768-applied-mathematics

**P0768 · `applied_mathematics` — Applied Mathematics & Numerical Analysis** · [spec](PART_SPECS_T16.md#p0768-applied-mathematics) · [self-contained txt](../prompts/P0768_applied_mathematics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0768  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0768 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0768  (18/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Applied Mathematics & Numerical Analysis
file         : parts/t16_domains/P0768_applied_mathematics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.applied_mathematics
language     : Python 3.13
capability   : cap.t16.applied.applied_mathematics@1
determinism  : pure
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Turns real problems into solvable mathematics.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. model formulation with assumption justification
  2. numerical-method selection with stability and convergence analysis
  3. error-bound derivation for computed solutions
  4. accuracy on applied-mathematics problem sets

Expanded obligations:
  1. Implement model formulation with assumption justification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement numerical-method selection with stability and convergence
     analysis, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement error-bound derivation for computed solutions with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement accuracy on applied-mathematics problem sets together with its
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.applied.applied_mathematics@1
  cap.t16.applied.applied_mathematics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.pure.pure_mathematics@1
      if unavailable: use the in-file conservative substitute for
      `pure_mathematics` (documented, slower, lower quality) and set
      `degraded['pure_mathematics']='local'`

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
   3. [ 600 lines] Core implementation A - model formulation with assumption justification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - numerical-method selection with stability and convergence analys
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - error-bound derivation for computed solutions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on applied-mathematics problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.applied.applied_mathematics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0768_applied_mathematics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0769-statistics-expertise

**P0769 · `statistics_expertise` — Statistics & Experimental Design** · [spec](PART_SPECS_T16.md#p0769-statistics-expertise) · [self-contained txt](../prompts/P0769_statistics_expertise.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0769  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0769 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0769  (19/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Statistics & Experimental Design
file         : parts/t16_domains/P0769_statistics_expertise.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.statistics_expertise
language     : Python 3.13
capability   : cap.t16.statistics.statistics_expertise@1
determinism  : pure
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
The statistical rigor that most analysis lacks.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. method selection with assumption verification and diagnostics
  2. power analysis, sample sizing and pre-registration reasoning
  3. multiple-comparison and p-hacking prevention
  4. accuracy on statistical-reasoning benchmark sets

Expanded obligations:
  1. Implement method selection with assumption verification and diagnostics,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement power analysis, sample sizing and pre-registration reasoning
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement multiple-comparison and p-hacking prevention together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy on statistical-reasoning benchmark sets as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.statistics.statistics_expertise@1
  cap.t16.statistics.statistics_expertise.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.applied.applied_mathematics@1
      if unavailable: use the in-file conservative substitute for
      `applied_mathematics` (documented, slower, lower quality) and set
      `degraded['applied_mathematics']='local'`

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
   3. [ 600 lines] Core implementation A - method selection with assumption verification and diagnostics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - power analysis, sample sizing and pre-registration reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - multiple-comparison and p-hacking prevention
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on statistical-reasoning benchmark sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.statistics.statistics_expertise@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0769_statistics_expertise.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0770-operations-research

**P0770 · `operations_research` — Operations Research & Optimisation** · [spec](PART_SPECS_T16.md#p0770-operations-research) · [self-contained txt](../prompts/P0770_operations_research.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0770  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0770 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0770  (20/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Operations Research & Optimisation
file         : parts/t16_domains/P0770_operations_research.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.operations_research
language     : Python 3.13
capability   : cap.t16.operations.operations_research@1
determinism  : pure
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Formulates and solves real optimisation problems.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. problem formulation into solvable programs with solver selection
  2. sensitivity and dual analysis with business interpretation
  3. heuristic design for intractable instances
  4. solution-quality measurement against known optima

Expanded obligations:
  1. Implement problem formulation into solvable programs with solver
     selection with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement sensitivity and dual analysis with business interpretation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement heuristic design for intractable instances as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement solution-quality measurement against known optima, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.operations.operations_research@1
  cap.t16.operations.operations_research.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.statistics.statistics_expertise@1
      if unavailable: use the in-file conservative substitute for
      `statistics_expertise` (documented, slower, lower quality) and set
      `degraded['statistics_expertise']='local'`

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
   3. [ 600 lines] Core implementation A - problem formulation into solvable programs with solver selection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - sensitivity and dual analysis with business interpretation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - heuristic design for intractable instances
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - solution-quality measurement against known optima
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.operations.operations_research@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0770_operations_research.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0771-mechanical-engineering

**P0771 · `mechanical_engineering` — Mechanical & Structural Engineering** · [spec](PART_SPECS_T16.md#p0771-mechanical-engineering) · [self-contained txt](../prompts/P0771_mechanical_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0771  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0771 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0771  (21/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Mechanical & Structural Engineering
file         : parts/t16_domains/P0771_mechanical_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.mechanical_engineering
language     : Python 3.13
capability   : cap.t16.mechanical.mechanical_engineering@1
determinism  : pure
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Designs things that do not break.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. stress, thermal and fatigue analysis with safety factors
  2. tolerance, fit and manufacturability reasoning
  3. code and standard compliance checking
  4. accuracy on engineering analysis problems with known answers

Expanded obligations:
  1. Implement stress, thermal and fatigue analysis with safety factors
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement tolerance, fit and manufacturability reasoning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement code and standard compliance checking, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement accuracy on engineering analysis problems with known answers
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.mechanical.mechanical_engineering@1
  cap.t16.mechanical.mechanical_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.operations.operations_research@1
      if unavailable: use the in-file conservative substitute for
      `operations_research` (documented, slower, lower quality) and set
      `degraded['operations_research']='local'`

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
   3. [ 600 lines] Core implementation A - stress, thermal and fatigue analysis with safety factors
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tolerance, fit and manufacturability reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - code and standard compliance checking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on engineering analysis problems with known answers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.mechanical.mechanical_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0771_mechanical_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0772-electrical-engineering

**P0772 · `electrical_engineering` — Electrical & Electronic Engineering** · [spec](PART_SPECS_T16.md#p0772-electrical-engineering) · [self-contained txt](../prompts/P0772_electrical_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0772  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0772 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0772  (22/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Electrical & Electronic Engineering
file         : parts/t16_domains/P0772_electrical_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.electrical_engineering
language     : Python 3.13
capability   : cap.t16.electrical.electrical_engineering@1
determinism  : pure
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Circuits, signals and power, correctly analysed.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. circuit analysis, signal integrity and power-budget reasoning
  2. component selection with derating and tolerance analysis
  3. simulation setup and result validation
  4. accuracy on electrical-engineering problem sets

Expanded obligations:
  1. Implement circuit analysis, signal integrity and power-budget reasoning
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement component selection with derating and tolerance analysis, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement simulation setup and result validation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement accuracy on electrical-engineering problem sets together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.electrical.electrical_engineering@1
  cap.t16.electrical.electrical_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.mechanical.mechanical_engineering@1
      if unavailable: use the in-file conservative substitute for
      `mechanical_engineering` (documented, slower, lower quality) and set
      `degraded['mechanical_engineering']='local'`

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
   3. [ 600 lines] Core implementation A - circuit analysis, signal integrity and power-budget reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - component selection with derating and tolerance analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - simulation setup and result validation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on electrical-engineering problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.electrical.electrical_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0772_electrical_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0773-control-systems

**P0773 · `control_systems` — Control Systems & Robotics Engineering** · [spec](PART_SPECS_T16.md#p0773-control-systems) · [self-contained txt](../prompts/P0773_control_systems.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0773  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0773 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0773  (23/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Control Systems & Robotics Engineering
file         : parts/t16_domains/P0773_control_systems.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.control_systems
language     : Python 3.13
capability   : cap.t16.control.control_systems@1
determinism  : pure
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Systems that remain stable in the real world.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. controller design with stability and robustness margin analysis
  2. system identification from measured data
  3. safety-critical control verification
  4. performance measurement in simulation and hardware-in-loop tests

Expanded obligations:
  1. Implement controller design with stability and robustness margin
     analysis, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement system identification from measured data with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement safety-critical control verification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement performance measurement in simulation and hardware-in-loop
     tests as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.control.control_systems@1
  cap.t16.control.control_systems.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.electrical.electrical_engineering@1
      if unavailable: use the in-file conservative substitute for
      `electrical_engineering` (documented, slower, lower quality) and set
      `degraded['electrical_engineering']='local'`

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
   3. [ 600 lines] Core implementation A - controller design with stability and robustness margin analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - system identification from measured data
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - safety-critical control verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - performance measurement in simulation and hardware-in-loop tests
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.control.control_systems@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0773_control_systems.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0774-chemical-engineering

**P0774 · `chemical_engineering` — Chemical & Process Engineering** · [spec](PART_SPECS_T16.md#p0774-chemical-engineering) · [self-contained txt](../prompts/P0774_chemical_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0774  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0774 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0774  (24/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Chemical & Process Engineering
file         : parts/t16_domains/P0774_chemical_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.chemical_engineering
language     : Python 3.13
capability   : cap.t16.chemical.chemical_engineering@1
determinism  : pure
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Scales chemistry into processes safely.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mass and energy balance construction and verification
  2. reactor, separation and process-safety reasoning
  3. process-simulation orchestration and validation
  4. accuracy on process-engineering problem sets

Expanded obligations:
  1. Implement mass and energy balance construction and verification with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement reactor, separation and process-safety reasoning together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement process-simulation orchestration and validation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement accuracy on process-engineering problem sets, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.chemical.chemical_engineering@1
  cap.t16.chemical.chemical_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.control.control_systems@1
      if unavailable: use the in-file conservative substitute for
      `control_systems` (documented, slower, lower quality) and set
      `degraded['control_systems']='local'`

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
   3. [ 600 lines] Core implementation A - mass and energy balance construction and verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - reactor, separation and process-safety reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - process-simulation orchestration and validation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on process-engineering problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.chemical.chemical_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0774_chemical_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0775-civil-infrastructure

**P0775 · `civil_infrastructure` — Civil & Infrastructure Engineering** · [spec](PART_SPECS_T16.md#p0775-civil-infrastructure) · [self-contained txt](../prompts/P0775_civil_infrastructure.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0775  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0775 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0775  (25/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Civil & Infrastructure Engineering
file         : parts/t16_domains/P0775_civil_infrastructure.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.civil_infrastructure
language     : Python 3.13
capability   : cap.t16.civil.civil_infrastructure@1
determinism  : pure
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Public-safety-grade engineering reasoning.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structural, geotechnical and hydraulic analysis
  2. code compliance and permitting reasoning
  3. lifecycle and durability analysis
  4. accuracy on civil-engineering analysis tasks

Expanded obligations:
  1. Implement structural, geotechnical and hydraulic analysis together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement code compliance and permitting reasoning as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of GDPval-AA
     v2 (Elo), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement lifecycle and durability analysis, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy on civil-engineering analysis tasks with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Life-sciences suite target reachable; the
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.civil.civil_infrastructure@1
  cap.t16.civil.civil_infrastructure.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.chemical.chemical_engineering@1
      if unavailable: use the in-file conservative substitute for
      `chemical_engineering` (documented, slower, lower quality) and set
      `degraded['chemical_engineering']='local'`

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
   3. [ 600 lines] Core implementation A - structural, geotechnical and hydraulic analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - code compliance and permitting reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - lifecycle and durability analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on civil-engineering analysis tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.civil.civil_infrastructure@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0775_civil_infrastructure.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0776-aerospace-engineering

**P0776 · `aerospace_engineering` — Aerospace Engineering** · [spec](PART_SPECS_T16.md#p0776-aerospace-engineering) · [self-contained txt](../prompts/P0776_aerospace_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0776  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0776 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0776  (26/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Aerospace Engineering
file         : parts/t16_domains/P0776_aerospace_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.aerospace_engineering
language     : Python 3.13
capability   : cap.t16.aerospace.aerospace_engineering@1
determinism  : pure
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Aerodynamics, propulsion and orbital mechanics.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. aerodynamic and propulsion performance analysis
  2. trajectory and orbital-mechanics computation with verification
  3. reliability and failure-mode analysis for flight systems
  4. accuracy on aerospace problem sets

Expanded obligations:
  1. Implement aerodynamic and propulsion performance analysis as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement trajectory and orbital-mechanics computation with
     verification, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement reliability and failure-mode analysis for flight systems with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement accuracy on aerospace problem sets together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
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
  cap.t16.aerospace.aerospace_engineering@1
  cap.t16.aerospace.aerospace_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.civil.civil_infrastructure@1
      if unavailable: use the in-file conservative substitute for
      `civil_infrastructure` (documented, slower, lower quality) and set
      `degraded['civil_infrastructure']='local'`

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
   3. [ 600 lines] Core implementation A - aerodynamic and propulsion performance analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - trajectory and orbital-mechanics computation with verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reliability and failure-mode analysis for flight systems
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on aerospace problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.aerospace.aerospace_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0776_aerospace_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0777-semiconductor-engineering

**P0777 · `semiconductor_engineering` — Semiconductor & Chip Design** · [spec](PART_SPECS_T16.md#p0777-semiconductor-engineering) · [self-contained txt](../prompts/P0777_semiconductor_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0777  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0777 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0777  (27/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Semiconductor & Chip Design
file         : parts/t16_domains/P0777_semiconductor_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.semiconductor_engineering
language     : Python 3.13
capability   : cap.t16.semiconductor.semiconductor_engineering@1
determinism  : pure
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Understands silicon deeply enough to improve its own hardware.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. RTL, timing, power and area reasoning
  2. physical-design and process-technology constraints
  3. verification-methodology reasoning for chip design
  4. accuracy on chip-design task suites

Expanded obligations:
  1. Implement RTL, timing, power and area reasoning, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement physical-design and process-technology constraints with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement verification-methodology reasoning for chip design together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement accuracy on chip-design task suites as a first-class, fully
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.semiconductor.semiconductor_engineering@1
  cap.t16.semiconductor.semiconductor_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.aerospace.aerospace_engineering@1
      if unavailable: use the in-file conservative substitute for
      `aerospace_engineering` (documented, slower, lower quality) and set
      `degraded['aerospace_engineering']='local'`

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
   3. [ 600 lines] Core implementation A - RTL, timing, power and area reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - physical-design and process-technology constraints
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - verification-methodology reasoning for chip design
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on chip-design task suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.semiconductor.semiconductor_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0777_semiconductor_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0778-energy-systems

**P0778 · `energy_systems` — Energy Systems & Power Engineering** · [spec](PART_SPECS_T16.md#p0778-energy-systems) · [self-contained txt](../prompts/P0778_energy_systems.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0778  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0778 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0778  (28/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Energy Systems & Power Engineering
file         : parts/t16_domains/P0778_energy_systems.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.energy_systems
language     : Python 3.13
capability   : cap.t16.energy.energy_systems@1
determinism  : pure
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Grid, generation and storage reasoning at system scale.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. power-flow, stability and dispatch reasoning
  2. storage, renewable-integration and reliability analysis
  3. techno-economic evaluation with sensitivity analysis
  4. accuracy on energy-system analysis tasks

Expanded obligations:
  1. Implement power-flow, stability and dispatch reasoning with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Life-sciences suite target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement storage, renewable-integration and reliability analysis
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement techno-economic evaluation with sensitivity analysis as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy on energy-system analysis tasks, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Life-sciences suite target
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.energy.energy_systems@1
  cap.t16.energy.energy_systems.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.semiconductor.semiconductor_engineering@1
      if unavailable: use the in-file conservative substitute for
      `semiconductor_engineering` (documented, slower, lower quality) and
      set `degraded['semiconductor_engineering']='local'`

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
   3. [ 600 lines] Core implementation A - power-flow, stability and dispatch reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - storage, renewable-integration and reliability analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - techno-economic evaluation with sensitivity analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on energy-system analysis tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.energy.energy_systems@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0778_energy_systems.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0779-corporate-law

**P0779 · `corporate_law` — Corporate & Transactional Law** · [spec](PART_SPECS_T16.md#p0779-corporate-law) · [self-contained txt](../prompts/P0779_corporate_law.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0779  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0779 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0779  (29/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Corporate & Transactional Law
file         : parts/t16_domains/P0779_corporate_law.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.corporate_law
language     : Python 3.13
capability   : cap.t16.corporate.corporate_law@1
determinism  : pure
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Deal work at senior-associate quality.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. entity, governance and transaction-structure reasoning
  2. diligence, disclosure and covenant analysis
  3. jurisdictional variation handling with explicit uncertainty
  4. target: exceed Opus 5's corporate-governance gains substantially

Expanded obligations:
  1. Implement entity, governance and transaction-structure reasoning
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement diligence, disclosure and covenant analysis as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement jurisdictional variation handling with explicit uncertainty,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement target: exceed Opus 5's corporate-governance gains
     substantially with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
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
  cap.t16.corporate.corporate_law@1
  cap.t16.corporate.corporate_law.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.energy.energy_systems@1
      if unavailable: use the in-file conservative substitute for
      `energy_systems` (documented, slower, lower quality) and set
      `degraded['energy_systems']='local'`

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
   3. [ 600 lines] Core implementation A - entity, governance and transaction-structure reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - diligence, disclosure and covenant analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - jurisdictional variation handling with explicit uncertainty
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: exceed Opus 5's corporate-governance gains substantially
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.corporate.corporate_law@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0779_corporate_law.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0780-litigation-arbitration

**P0780 · `litigation_arbitration` — Litigation & Dispute Resolution** · [spec](PART_SPECS_T16.md#p0780-litigation-arbitration) · [self-contained txt](../prompts/P0780_litigation_arbitration.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0780  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0780 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0780  (30/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Litigation & Dispute Resolution
file         : parts/t16_domains/P0780_litigation_arbitration.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.litigation_arbitration
language     : Python 3.13
capability   : cap.t16.litigation.litigation_arbitration@1
determinism  : pure
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Argument construction and case analysis.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. claim, defence and remedy analysis with authority citation
  2. evidence and procedural reasoning
  3. arbitration-specific procedural competence
  4. target: exceed Opus 5's arbitration-practice gains substantially

Expanded obligations:
  1. Implement claim, defence and remedy analysis with authority citation as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement evidence and procedural reasoning, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement arbitration-specific procedural competence with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement target: exceed Opus 5's arbitration-practice gains
     substantially together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against GPQA Diamond — a
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.litigation.litigation_arbitration@1
  cap.t16.litigation.litigation_arbitration.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.corporate.corporate_law@1
      if unavailable: use the in-file conservative substitute for
      `corporate_law` (documented, slower, lower quality) and set
      `degraded['corporate_law']='local'`

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
   3. [ 600 lines] Core implementation A - claim, defence and remedy analysis with authority citation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - evidence and procedural reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - arbitration-specific procedural competence
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: exceed Opus 5's arbitration-practice gains substantially
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.litigation.litigation_arbitration@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0780_litigation_arbitration.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0781-regulatory-compliance

**P0781 · `regulatory_compliance` — Regulatory & Compliance Analysis** · [spec](PART_SPECS_T16.md#p0781-regulatory-compliance) · [self-contained txt](../prompts/P0781_regulatory_compliance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0781  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0781 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0781  (31/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Regulatory & Compliance Analysis
file         : parts/t16_domains/P0781_regulatory_compliance.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.regulatory_compliance
language     : Python 3.13
capability   : cap.t16.regulatory.regulatory_compliance@1
determinism  : pure
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Navigates complex overlapping regulation correctly.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-jurisdiction requirement mapping and conflict identification
  2. compliance-program design and gap analysis
  3. regulatory-change monitoring and impact assessment
  4. accuracy on compliance-analysis task sets

Expanded obligations:
  1. Implement multi-jurisdiction requirement mapping and conflict
     identification, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement compliance-program design and gap analysis with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement regulatory-change monitoring and impact assessment together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy on compliance-analysis task sets as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
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
  cap.t16.regulatory.regulatory_compliance@1
  cap.t16.regulatory.regulatory_compliance.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.litigation.litigation_arbitration@1
      if unavailable: use the in-file conservative substitute for
      `litigation_arbitration` (documented, slower, lower quality) and set
      `degraded['litigation_arbitration']='local'`

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
   3. [ 600 lines] Core implementation A - multi-jurisdiction requirement mapping and conflict identificati
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - compliance-program design and gap analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regulatory-change monitoring and impact assessment
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on compliance-analysis task sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.regulatory.regulatory_compliance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0781_regulatory_compliance.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0782-ip-patent

**P0782 · `ip_patent` — Intellectual Property & Patent Practice** · [spec](PART_SPECS_T16.md#p0782-ip-patent) · [self-contained txt](../prompts/P0782_ip_patent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0782  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0782 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0782  (32/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Intellectual Property & Patent Practice
file         : parts/t16_domains/P0782_ip_patent.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.ip_patent
language     : Python 3.13
capability   : cap.t16.ip.ip_patent@1
determinism  : pure
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Patent-grade technical and legal analysis.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. claim construction, novelty and obviousness analysis
  2. prior-art search strategy and analysis
  3. specification drafting with enablement rigor
  4. accuracy on patent-analysis benchmark tasks

Expanded obligations:
  1. Implement claim construction, novelty and obviousness analysis with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement prior-art search strategy and analysis together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement specification drafting with enablement rigor as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement accuracy on patent-analysis benchmark tasks, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.ip.ip_patent@1
  cap.t16.ip.ip_patent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.regulatory.regulatory_compliance@1
      if unavailable: use the in-file conservative substitute for
      `regulatory_compliance` (documented, slower, lower quality) and set
      `degraded['regulatory_compliance']='local'`

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
   3. [ 600 lines] Core implementation A - claim construction, novelty and obviousness analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - prior-art search strategy and analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - specification drafting with enablement rigor
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on patent-analysis benchmark tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.ip.ip_patent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0782_ip_patent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0783-tax-accounting

**P0783 · `tax_accounting` — Tax & Accounting** · [spec](PART_SPECS_T16.md#p0783-tax-accounting) · [self-contained txt](../prompts/P0783_tax_accounting.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0783  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0783 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0783  (33/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Tax & Accounting
file         : parts/t16_domains/P0783_tax_accounting.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.tax_accounting
language     : Python 3.13
capability   : cap.t16.tax.tax_accounting@1
determinism  : pure
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Numbers that survive an auditor.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. accounting-standard application (GAAP/IFRS) with judgment reasoning
  2. tax-position analysis with authority citation and uncertainty flagging
  3. financial-statement construction and reconciliation verification
  4. accuracy on accounting and tax problem sets

Expanded obligations:
  1. Implement accounting-standard application (GAAP/IFRS) with judgment
     reasoning together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement tax-position analysis with authority citation and uncertainty
     flagging as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement financial-statement construction and reconciliation
     verification, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement accuracy on accounting and tax problem sets with an explicit
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.tax.tax_accounting@1
  cap.t16.tax.tax_accounting.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.ip.ip_patent@1
      if unavailable: use the in-file conservative substitute for
      `ip_patent` (documented, slower, lower quality) and set
      `degraded['ip_patent']='local'`

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
   3. [ 600 lines] Core implementation A - accounting-standard application (GAAP/IFRS) with judgment reason
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tax-position analysis with authority citation and uncertainty fl
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - financial-statement construction and reconciliation verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on accounting and tax problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.tax.tax_accounting@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0783_tax_accounting.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0784-corporate-finance

**P0784 · `corporate_finance` — Corporate Finance & Valuation** · [spec](PART_SPECS_T16.md#p0784-corporate-finance) · [self-contained txt](../prompts/P0784_corporate_finance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0784  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0784 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0784  (34/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Corporate Finance & Valuation
file         : parts/t16_domains/P0784_corporate_finance.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.corporate_finance
language     : Python 3.13
capability   : cap.t16.corporate.corporate_finance@1
determinism  : pure
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Valuation and capital decisions done properly.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. valuation modelling (DCF, comparables, options) with assumption discipline
  2. capital-structure and cost-of-capital analysis
  3. transaction and synergy analysis with sensitivity ranges
  4. accuracy versus expert-analyst reference valuations

Expanded obligations:
  1. Implement valuation modelling (DCF, comparables, options) with
     assumption discipline as a first-class, fully realised mechanism. No
     stub, no `NotImplementedError`, no configuration flag whose default
     disables it. Its state must be reportable through `describe()` and it
     must be exercised by at least eight in-file tests, including one that
     fails loudly if the mechanism is silently bypassed. Correctness here is
     what makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement capital-structure and cost-of-capital analysis, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement transaction and synergy analysis with sensitivity ranges with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement accuracy versus expert-analyst reference valuations together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.corporate.corporate_finance@1
  cap.t16.corporate.corporate_finance.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.tax.tax_accounting@1
      if unavailable: use the in-file conservative substitute for
      `tax_accounting` (documented, slower, lower quality) and set
      `degraded['tax_accounting']='local'`

  cap.t10.search.search_controller@1
      if unavailable: use the in-file conservative substitute for
      `search_controller` (documented, slower, lower quality) and set
      `degraded['search_controller']='local'`

  cap.t11.smt.smt_bridge@1
      if unavailable: use the in-file conservative substitute for
      `smt_bridge` (documented, slower, lower quality) and set
      `degraded['smt_bridge']='local'`

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
   3. [ 600 lines] Core implementation A - valuation modelling (DCF, comparables, options) with assumption 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capital-structure and cost-of-capital analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - transaction and synergy analysis with sensitivity ranges
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy versus expert-analyst reference valuations
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.corporate.corporate_finance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0784_corporate_finance.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0785-quantitative-finance

**P0785 · `quantitative_finance` — Quantitative Finance & Derivatives** · [spec](PART_SPECS_T16.md#p0785-quantitative-finance) · [self-contained txt](../prompts/P0785_quantitative_finance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0785  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0785 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0785  (35/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Quantitative Finance & Derivatives
file         : parts/t16_domains/P0785_quantitative_finance.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.quantitative_finance
language     : Python 3.13
capability   : cap.t16.quantitative.quantitative_finance@1
determinism  : pure
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Pricing, risk and market microstructure.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. derivative pricing with model-risk awareness and calibration
  2. risk measurement (VaR, stress, greeks) with correct methodology
  3. market-microstructure and execution reasoning
  4. accuracy on quantitative-finance problem sets

Expanded obligations:
  1. Implement derivative pricing with model-risk awareness and calibration,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement risk measurement (VaR, stress, greeks) with correct
     methodology with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement market-microstructure and execution reasoning together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement accuracy on quantitative-finance problem sets as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.quantitative.quantitative_finance@1
  cap.t16.quantitative.quantitative_finance.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.corporate.corporate_finance@1
      if unavailable: use the in-file conservative substitute for
      `corporate_finance` (documented, slower, lower quality) and set
      `degraded['corporate_finance']='local'`

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
   3. [ 600 lines] Core implementation A - derivative pricing with model-risk awareness and calibration
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - risk measurement (VaR, stress, greeks) with correct methodology
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - market-microstructure and execution reasoning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on quantitative-finance problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.quantitative.quantitative_finance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0785_quantitative_finance.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0786-investment-research

**P0786 · `investment_research` — Investment Research & Financial Analysis** · [spec](PART_SPECS_T16.md#p0786-investment-research) · [self-contained txt](../prompts/P0786_investment_research.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0786  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0786 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0786  (36/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Investment Research & Financial Analysis
file         : parts/t16_domains/P0786_investment_research.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.investment_research
language     : Python 3.13
capability   : cap.t16.investment.investment_research@1
determinism  : pure
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Research a portfolio manager would act on.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. financial-statement analysis with quality-of-earnings reasoning
  2. industry and competitive-position analysis with evidence
  3. thesis construction with explicit falsification criteria
  4. target: exceed Opus 5's financial-research improvements substantially

Expanded obligations:
  1. Implement financial-statement analysis with quality-of-earnings
     reasoning with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement industry and competitive-position analysis with evidence
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement thesis construction with explicit falsification criteria as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement target: exceed Opus 5's financial-research improvements
     substantially, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against GPQA
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.investment.investment_research@1
  cap.t16.investment.investment_research.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.quantitative.quantitative_finance@1
      if unavailable: use the in-file conservative substitute for
      `quantitative_finance` (documented, slower, lower quality) and set
      `degraded['quantitative_finance']='local'`

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
   3. [ 600 lines] Core implementation A - financial-statement analysis with quality-of-earnings reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - industry and competitive-position analysis with evidence
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - thesis construction with explicit falsification criteria
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: exceed Opus 5's financial-research improvements substant
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.investment.investment_research@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0786_investment_research.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0787-risk-management

**P0787 · `risk_management` — Risk Management & Actuarial Science** · [spec](PART_SPECS_T16.md#p0787-risk-management) · [self-contained txt](../prompts/P0787_risk_management.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0787  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0787 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0787  (37/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Risk Management & Actuarial Science
file         : parts/t16_domains/P0787_risk_management.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.risk_management
language     : Python 3.13
capability   : cap.t16.risk.risk_management@1
determinism  : pure
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Quantifies and prices uncertainty correctly.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. risk-model construction with tail-behaviour rigor
  2. actuarial reserving and pricing methodology
  3. scenario and stress-test design
  4. accuracy on actuarial and risk problem sets

Expanded obligations:
  1. Implement risk-model construction with tail-behaviour rigor together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement actuarial reserving and pricing methodology as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of GDPval-AA
     v2 (Elo), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement scenario and stress-test design, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Its contribution
     is measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy on actuarial and risk problem sets with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Life-sciences suite target reachable; the
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.risk.risk_management@1
  cap.t16.risk.risk_management.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.investment.investment_research@1
      if unavailable: use the in-file conservative substitute for
      `investment_research` (documented, slower, lower quality) and set
      `degraded['investment_research']='local'`

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
   3. [ 600 lines] Core implementation A - risk-model construction with tail-behaviour rigor
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - actuarial reserving and pricing methodology
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - scenario and stress-test design
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on actuarial and risk problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.risk.risk_management@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0787_risk_management.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0788-economics

**P0788 · `economics` — Economics & Policy Analysis** · [spec](PART_SPECS_T16.md#p0788-economics) · [self-contained txt](../prompts/P0788_economics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0788  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0788 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0788  (38/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Economics & Policy Analysis
file         : parts/t16_domains/P0788_economics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.economics
language     : Python 3.13
capability   : cap.t16.economics.economics@1
determinism  : pure
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Economic reasoning with empirical discipline.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. micro and macro reasoning with model-assumption transparency
  2. causal-inference methodology for policy evaluation
  3. data-source selection and measurement-validity reasoning
  4. accuracy on economics problem and analysis sets

Expanded obligations:
  1. Implement micro and macro reasoning with model-assumption transparency
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement causal-inference methodology for policy evaluation, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement data-source selection and measurement-validity reasoning with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement accuracy on economics problem and analysis sets together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
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
  cap.t16.economics.economics@1
  cap.t16.economics.economics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.risk.risk_management@1
      if unavailable: use the in-file conservative substitute for
      `risk_management` (documented, slower, lower quality) and set
      `degraded['risk_management']='local'`

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
   3. [ 600 lines] Core implementation A - micro and macro reasoning with model-assumption transparency
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - causal-inference methodology for policy evaluation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - data-source selection and measurement-validity reasoning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on economics problem and analysis sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.economics.economics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0788_economics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0789-management-strategy

**P0789 · `management_strategy` — Business Strategy & Management Consulting** · [spec](PART_SPECS_T16.md#p0789-management-strategy) · [self-contained txt](../prompts/P0789_management_strategy.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0789  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0789 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0789  (39/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Business Strategy & Management Consulting
file         : parts/t16_domains/P0789_management_strategy.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.management_strategy
language     : Python 3.13
capability   : cap.t16.management.management_strategy@1
determinism  : pure
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Strategy work of partner quality.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. market, competitive and capability analysis with evidence discipline
  2. option generation and structured recommendation with tradeoffs
  3. implementation-feasibility and change-management reasoning
  4. expert-consultant evaluation results

Expanded obligations:
  1. Implement market, competitive and capability analysis with evidence
     discipline, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against GPQA
     Diamond — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement option generation and structured recommendation with tradeoffs
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement implementation-feasibility and change-management reasoning
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement expert-consultant evaluation results as a first-class, fully
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.management.management_strategy@1
  cap.t16.management.management_strategy.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.economics.economics@1
      if unavailable: use the in-file conservative substitute for
      `economics` (documented, slower, lower quality) and set
      `degraded['economics']='local'`

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
   3. [ 600 lines] Core implementation A - market, competitive and capability analysis with evidence discip
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - option generation and structured recommendation with tradeoffs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - implementation-feasibility and change-management reasoning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-consultant evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.management.management_strategy@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0789_management_strategy.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0790-marketing-growth

**P0790 · `marketing_growth` — Marketing, Growth & Product Analytics** · [spec](PART_SPECS_T16.md#p0790-marketing-growth) · [self-contained txt](../prompts/P0790_marketing_growth.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0790  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0790 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0790  (40/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Marketing, Growth & Product Analytics
file         : parts/t16_domains/P0790_marketing_growth.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.marketing_growth
language     : Python 3.13
capability   : cap.t16.marketing.marketing_growth@1
determinism  : pure
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Measurable, honest growth reasoning.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. experiment design with correct statistics and guardrail metrics
  2. attribution and cohort analysis methodology
  3. positioning and messaging reasoning with audience research
  4. accuracy on analytics tasks with known ground truth

Expanded obligations:
  1. Implement experiment design with correct statistics and guardrail
     metrics with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Life-sciences
     suite target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement attribution and cohort analysis methodology together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement positioning and messaging reasoning with audience research as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy on analytics tasks with known ground truth, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Life-sciences suite target
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
  cap.t16.marketing.marketing_growth@1
  cap.t16.marketing.marketing_growth.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.management.management_strategy@1
      if unavailable: use the in-file conservative substitute for
      `management_strategy` (documented, slower, lower quality) and set
      `degraded['management_strategy']='local'`

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
   3. [ 600 lines] Core implementation A - experiment design with correct statistics and guardrail metrics
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - attribution and cohort analysis methodology
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - positioning and messaging reasoning with audience research
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on analytics tasks with known ground truth
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.marketing.marketing_growth@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0790_marketing_growth.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0791-operations-supplychain

**P0791 · `operations_supplychain` — Operations & Supply Chain Management** · [spec](PART_SPECS_T16.md#p0791-operations-supplychain) · [self-contained txt](../prompts/P0791_operations_supplychain.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0791  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0791 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0791  (41/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Operations & Supply Chain Management
file         : parts/t16_domains/P0791_operations_supplychain.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.operations_supplychain
language     : Python 3.13
capability   : cap.t16.operations.operations_supplychain@1
determinism  : pure
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Real-world logistics and production optimisation.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. inventory, capacity and network-design optimisation
  2. demand forecasting with uncertainty and bullwhip reasoning
  3. resilience and disruption-scenario analysis
  4. accuracy on operations problem sets

Expanded obligations:
  1. Implement inventory, capacity and network-design optimisation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement demand forecasting with uncertainty and bullwhip reasoning as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement resilience and disruption-scenario analysis, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement accuracy on operations problem sets with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.operations.operations_supplychain@1
  cap.t16.operations.operations_supplychain.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.marketing.marketing_growth@1
      if unavailable: use the in-file conservative substitute for
      `marketing_growth` (documented, slower, lower quality) and set
      `degraded['marketing_growth']='local'`

  cap.t10.thought.thought_program_ir@1
      if unavailable: use the in-file conservative substitute for
      `thought_program_ir` (documented, slower, lower quality) and set
      `degraded['thought_program_ir']='local'`

  cap.t11.logic.logic_core@1
      if unavailable: use the in-file conservative substitute for
      `logic_core` (documented, slower, lower quality) and set
      `degraded['logic_core']='local'`

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
   3. [ 600 lines] Core implementation A - inventory, capacity and network-design optimisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - demand forecasting with uncertainty and bullwhip reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - resilience and disruption-scenario analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on operations problem sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.operations.operations_supplychain@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0791_operations_supplychain.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0792-hr-organisational

**P0792 · `hr_organisational` — Human Resources & Organisational Design** · [spec](PART_SPECS_T16.md#p0792-hr-organisational) · [self-contained txt](../prompts/P0792_hr_organisational.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0792  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0792 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0792  (42/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Human Resources & Organisational Design
file         : parts/t16_domains/P0792_hr_organisational.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.hr_organisational
language     : Python 3.13
capability   : cap.t16.hr.hr_organisational@1
determinism  : pure
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
People decisions made carefully and fairly.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. organisational design and role-architecture reasoning
  2. fairness, bias and legal-compliance analysis in people processes
  3. performance and compensation-system design
  4. expert-practitioner evaluation results

Expanded obligations:
  1. Implement organisational design and role-architecture reasoning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement fairness, bias and legal-compliance analysis in people
     processes, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement performance and compensation-system design with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement expert-practitioner evaluation results together with its
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.hr.hr_organisational@1
  cap.t16.hr.hr_organisational.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.operations.operations_supplychain@1
      if unavailable: use the in-file conservative substitute for
      `operations_supplychain` (documented, slower, lower quality) and set
      `degraded['operations_supplychain']='local'`

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
   3. [ 600 lines] Core implementation A - organisational design and role-architecture reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - fairness, bias and legal-compliance analysis in people processes
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - performance and compensation-system design
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-practitioner evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.hr.hr_organisational@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0792_hr_organisational.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0793-education-pedagogy

**P0793 · `education_pedagogy` — Education & Instructional Design** · [spec](PART_SPECS_T16.md#p0793-education-pedagogy) · [self-contained txt](../prompts/P0793_education_pedagogy.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0793  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0793 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0793  (43/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Education & Instructional Design
file         : parts/t16_domains/P0793_education_pedagogy.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.education_pedagogy
language     : Python 3.13
capability   : cap.t16.education.education_pedagogy@1
determinism  : pure
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Designs learning that actually works.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. curriculum and assessment design with learning-science grounding
  2. misconception mapping and remediation design
  3. differentiation for varied learner needs
  4. learning-outcome measurement with real learners

Expanded obligations:
  1. Implement curriculum and assessment design with learning-science
     grounding, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement misconception mapping and remediation design with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement differentiation for varied learner needs together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement learning-outcome measurement with real learners as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
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
  cap.t16.education.education_pedagogy@1
  cap.t16.education.education_pedagogy.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.hr.hr_organisational@1
      if unavailable: use the in-file conservative substitute for
      `hr_organisational` (documented, slower, lower quality) and set
      `degraded['hr_organisational']='local'`

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
   3. [ 600 lines] Core implementation A - curriculum and assessment design with learning-science grounding
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - misconception mapping and remediation design
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - differentiation for varied learner needs
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - learning-outcome measurement with real learners
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.education.education_pedagogy@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0793_education_pedagogy.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0794-psychology-behaviour

**P0794 · `psychology_behaviour` — Psychology & Behavioural Science** · [spec](PART_SPECS_T16.md#p0794-psychology-behaviour) · [self-contained txt](../prompts/P0794_psychology_behaviour.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0794  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0794 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0794  (44/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Psychology & Behavioural Science
file         : parts/t16_domains/P0794_psychology_behaviour.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.psychology_behaviour
language     : Python 3.13
capability   : cap.t16.psychology.psychology_behaviour@1
determinism  : pure
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Human behaviour reasoning grounded in replicated evidence.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. theory application with replication-quality awareness
  2. assessment-instrument reasoning and validity analysis
  3. intervention design with ethical constraints
  4. accuracy on psychology question sets weighted by evidence quality

Expanded obligations:
  1. Implement theory application with replication-quality awareness with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement assessment-instrument reasoning and validity analysis together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against GPQA Diamond — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement intervention design with ethical constraints as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Life-sciences suite target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement accuracy on psychology question sets weighted by evidence
     quality, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.psychology.psychology_behaviour@1
  cap.t16.psychology.psychology_behaviour.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.education.education_pedagogy@1
      if unavailable: use the in-file conservative substitute for
      `education_pedagogy` (documented, slower, lower quality) and set
      `degraded['education_pedagogy']='local'`

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
   3. [ 600 lines] Core implementation A - theory application with replication-quality awareness
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - assessment-instrument reasoning and validity analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - intervention design with ethical constraints
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on psychology question sets weighted by evidence qualit
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.psychology.psychology_behaviour@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0794_psychology_behaviour.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0795-linguistics

**P0795 · `linguistics` — Linguistics & Language Science** · [spec](PART_SPECS_T16.md#p0795-linguistics) · [self-contained txt](../prompts/P0795_linguistics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0795  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0795 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0795  (45/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Linguistics & Language Science
file         : parts/t16_domains/P0795_linguistics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.linguistics
language     : Python 3.13
capability   : cap.t16.linguistics.linguistics@1
determinism  : pure
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Deep formal understanding of language itself.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. phonological, syntactic, semantic and pragmatic analysis
  2. typological and historical-linguistic reasoning
  3. low-resource language analysis methodology
  4. accuracy on linguistic-analysis task sets

Expanded obligations:
  1. Implement phonological, syntactic, semantic and pragmatic analysis
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement typological and historical-linguistic reasoning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement low-resource language analysis methodology, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement accuracy on linguistic-analysis task sets with an explicit
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.linguistics.linguistics@1
  cap.t16.linguistics.linguistics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.psychology.psychology_behaviour@1
      if unavailable: use the in-file conservative substitute for
      `psychology_behaviour` (documented, slower, lower quality) and set
      `degraded['psychology_behaviour']='local'`

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
   3. [ 600 lines] Core implementation A - phonological, syntactic, semantic and pragmatic analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - typological and historical-linguistic reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - low-resource language analysis methodology
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on linguistic-analysis task sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.linguistics.linguistics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0795_linguistics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0796-history-humanities

**P0796 · `history_humanities` — History & Humanities Scholarship** · [spec](PART_SPECS_T16.md#p0796-history-humanities) · [self-contained txt](../prompts/P0796_history_humanities.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0796  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0796 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0796  (46/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : History & Humanities Scholarship
file         : parts/t16_domains/P0796_history_humanities.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.history_humanities
language     : Python 3.13
capability   : cap.t16.history.history_humanities@1
determinism  : pure
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Source-critical, contextually careful scholarship.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. primary-source analysis with provenance and bias assessment
  2. historiographical awareness and interpretive humility
  3. chronological and contextual accuracy verification
  4. expert-historian evaluation results

Expanded obligations:
  1. Implement primary-source analysis with provenance and bias assessment as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement historiographical awareness and interpretive humility, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement chronological and contextual accuracy verification with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement expert-historian evaluation results together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.history.history_humanities@1
  cap.t16.history.history_humanities.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.linguistics.linguistics@1
      if unavailable: use the in-file conservative substitute for
      `linguistics` (documented, slower, lower quality) and set
      `degraded['linguistics']='local'`

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
   3. [ 600 lines] Core implementation A - primary-source analysis with provenance and bias assessment
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - historiographical awareness and interpretive humility
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - chronological and contextual accuracy verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-historian evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.history.history_humanities@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0796_history_humanities.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0797-philosophy-ethics

**P0797 · `philosophy_ethics` — Philosophy & Applied Ethics** · [spec](PART_SPECS_T16.md#p0797-philosophy-ethics) · [self-contained txt](../prompts/P0797_philosophy_ethics.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0797  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0797 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0797  (47/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Philosophy & Applied Ethics
file         : parts/t16_domains/P0797_philosophy_ethics.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.philosophy_ethics
language     : Python 3.13
capability   : cap.t16.philosophy.philosophy_ethics@1
determinism  : pure
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Rigorous argument analysis and ethical reasoning.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. argument reconstruction, validity analysis and objection handling
  2. ethical-framework application with pluralism and honesty about disagreement
  3. conceptual analysis and distinction drawing
  4. expert-philosopher evaluation results

Expanded obligations:
  1. Implement argument reconstruction, validity analysis and objection
     handling, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     GDPval-AA v2 (Elo), so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement ethical-framework application with pluralism and honesty about
     disagreement with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against GPQA Diamond — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement conceptual analysis and distinction drawing together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement expert-philosopher evaluation results as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
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
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.philosophy.philosophy_ethics@1
  cap.t16.philosophy.philosophy_ethics.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.history.history_humanities@1
      if unavailable: use the in-file conservative substitute for
      `history_humanities` (documented, slower, lower quality) and set
      `degraded['history_humanities']='local'`

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
   3. [ 600 lines] Core implementation A - argument reconstruction, validity analysis and objection handlin
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - ethical-framework application with pluralism and honesty about d
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conceptual analysis and distinction drawing
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-philosopher evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.philosophy.philosophy_ethics@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0797_philosophy_ethics.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0798-agriculture-food

**P0798 · `agriculture_food` — Agriculture, Food Science & Nutrition** · [spec](PART_SPECS_T16.md#p0798-agriculture-food) · [self-contained txt](../prompts/P0798_agriculture_food.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0798  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0798 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0798  (48/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Agriculture, Food Science & Nutrition
file         : parts/t16_domains/P0798_agriculture_food.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.agriculture_food
language     : Python 3.13
capability   : cap.t16.agriculture.agriculture_food@1
determinism  : pure
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Applied biological and food-system reasoning.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. crop, soil and yield-system reasoning with regional variation
  2. food-safety, processing and formulation science
  3. nutritional analysis with evidence-quality weighting
  4. accuracy on agricultural and food-science task sets

Expanded obligations:
  1. Implement crop, soil and yield-system reasoning with regional variation
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement food-safety, processing and formulation science together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Life-sciences suite target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement nutritional analysis with evidence-quality weighting as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement accuracy on agricultural and food-science task sets, and make
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.agriculture.agriculture_food@1
  cap.t16.agriculture.agriculture_food.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.philosophy.philosophy_ethics@1
      if unavailable: use the in-file conservative substitute for
      `philosophy_ethics` (documented, slower, lower quality) and set
      `degraded['philosophy_ethics']='local'`

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
   3. [ 600 lines] Core implementation A - crop, soil and yield-system reasoning with regional variation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - food-safety, processing and formulation science
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - nutritional analysis with evidence-quality weighting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on agricultural and food-science task sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.agriculture.agriculture_food@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0798_agriculture_food.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0799-domain-cross-transfer

**P0799 · `domain_cross_transfer` — Cross-Domain Synthesis & Interdisciplinary Reasoning** · [spec](PART_SPECS_T16.md#p0799-domain-cross-transfer) · [self-contained txt](../prompts/P0799_domain_cross_transfer.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0799  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0799 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0799  (49/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Cross-Domain Synthesis & Interdisciplinary Reasoning
file         : parts/t16_domains/P0799_domain_cross_transfer.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.domain_cross_transfer
language     : Python 3.13
capability   : cap.t16.domain.domain_cross_transfer@1
determinism  : pure
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
The breakthroughs live between fields.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-domain problem decomposition and expertise integration
  2. terminology and method translation across fields
  3. conflict resolution when domain norms disagree
  4. accuracy on interdisciplinary benchmark problems

Expanded obligations:
  1. Implement multi-domain problem decomposition and expertise integration
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement terminology and method translation across fields as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement conflict resolution when domain norms disagree, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement accuracy on interdisciplinary benchmark problems with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.domain.domain_cross_transfer@1
  cap.t16.domain.domain_cross_transfer.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.agriculture.agriculture_food@1
      if unavailable: use the in-file conservative substitute for
      `agriculture_food` (documented, slower, lower quality) and set
      `degraded['agriculture_food']='local'`

  cap.t10.outcome.outcome_verifier@1
      if unavailable: use the in-file conservative substitute for
      `outcome_verifier` (documented, slower, lower quality) and set
      `degraded['outcome_verifier']='local'`

  cap.t11.proof.proof_certificate@1
      if unavailable: use the in-file conservative substitute for
      `proof_certificate` (documented, slower, lower quality) and set
      `degraded['proof_certificate']='local'`

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
   3. [ 600 lines] Core implementation A - multi-domain problem decomposition and expertise integration
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - terminology and method translation across fields
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conflict resolution when domain norms disagree
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy on interdisciplinary benchmark problems
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.domain.domain_cross_transfer@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0799_domain_cross_transfer.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0800-domain-eval-harness

**P0800 · `domain_eval_harness` — Domain Expertise Benchmark Harness** · [spec](PART_SPECS_T16.md#p0800-domain-eval-harness) · [self-contained txt](../prompts/P0800_domain_eval_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0800  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0800 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0800  (50/50 of tier T16)
tier         : T16 — Domain Superintelligence Packs
title        : Domain Expertise Benchmark Harness
file         : parts/t16_domains/P0800_domain_eval_harness.py          <-- create exactly this path, nothing else
module       : hyperion.t16.domains.domain_eval_harness
language     : Python 3.13
capability   : cap.t16.domain.domain_eval_harness@1
determinism  : pure
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

MISSION
-------
Measures expert-level capability per domain rigorously.

Tier context:
  Life sciences, chemistry, physics, medicine, law, finance, engineering:
  expert-grade domain reasoning with domain verifiers.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. GPQA Diamond, life-sciences and per-domain expert benchmark harnesses
  2. expert-grading protocol with inter-rater reliability
  3. per-domain capability register with honest gap reporting
  4. targets: GPQA 99.6% (Opus 5: ~95.5%), life-sciences 165% of Opus 5

Expanded obligations:
  1. Implement GPQA Diamond, life-sciences and per-domain expert benchmark
     harnesses as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement expert-grading protocol with inter-rater reliability, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against GPQA Diamond — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement per-domain capability register with honest gap reporting with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Life-sciences suite target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement targets: GPQA 99.6% (Opus 5: ~95.5%), life-sciences 165% of
     Opus 5 together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t16.domain.domain_eval_harness@1
  cap.t16.domain.domain_eval_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t16.domain.domain_cross_transfer@1
      if unavailable: use the in-file conservative substitute for
      `domain_cross_transfer` (documented, slower, lower quality) and set
      `degraded['domain_cross_transfer']='local'`

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
   3. [ 600 lines] Core implementation A - GPQA Diamond, life-sciences and per-domain expert benchmark harn
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - expert-grading protocol with inter-rater reliability
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-domain capability register with honest gap reporting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - targets: GPQA 99.6% (Opus 5: ~95.5%), life-sciences 165% of Opus
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t16.domain.domain_eval_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t16_domains/P0800_domain_eval_harness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
