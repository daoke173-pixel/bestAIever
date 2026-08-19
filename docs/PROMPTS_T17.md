# HYPERION-Ω — Worker prompts · T17 · Training, Data & Recursive Self-Improvement

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

## PROMPT p0801-data-sourcing

**P0801 · `data_sourcing` — Training Data Sourcing & Licensing** · [spec](PART_SPECS_T17.md#p0801-data-sourcing) · [self-contained txt](../prompts/P0801_data_sourcing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0801  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0801 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0801  (1/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Data Sourcing & Licensing
file         : parts/t17_training/P0801_data_sourcing.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_sourcing
language     : Python 3.13
capability   : cap.t17.data.data_sourcing@1
determinism  : io
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Legally clean, high-quality data at petabyte scale.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. source inventory with license classification and permission tracking
  2. acquisition pipeline with robots/terms compliance verification
  3. provenance recording at document granularity
  4. auditable license-compliance report for the whole corpus

Expanded obligations:
  1. Implement source inventory with license classification and permission
     tracking, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement acquisition pipeline with robots/terms compliance verification
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement provenance recording at document granularity together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of ARC-AGI-3, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement auditable license-compliance report for the whole corpus as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.data.data_sourcing@1
  cap.t17.data.data_sourcing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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

  cap.t06.conditional.conditional_layers@1
      if unavailable: use the in-file conservative substitute for
      `conditional_layers` (documented, slower, lower quality) and set
      `degraded['conditional_layers']='local'`

  cap.t10.numeric.numeric_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `numeric_reasoning` (documented, slower, lower quality) and set
      `degraded['numeric_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - source inventory with license classification and permission trac
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - acquisition pipeline with robots/terms compliance verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - provenance recording at document granularity
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - auditable license-compliance report for the whole corpus
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_sourcing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0801_data_sourcing.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0802-data-extraction-pipeline-train

**P0802 · `data_extraction_pipeline_train` — Corpus Extraction & Normalisation** · [spec](PART_SPECS_T17.md#p0802-data-extraction-pipeline-train) · [self-contained txt](../prompts/P0802_data_extraction_pipeline_train.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0802  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0802 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0802  (2/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Corpus Extraction & Normalisation
file         : parts/t17_training/P0802_data_extraction_pipeline_train.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_extraction_pipeline_train
language     : Python 3.13
capability   : cap.t17.data.data_extraction_pipeline_train@1
determinism  : io
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Turns raw web, code and document archives into clean text.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. format-specific extraction (HTML, PDF, code, notebooks, media transcripts)
  2. boilerplate removal and content-quality preservation
  3. encoding, language and script normalisation
  4. extraction-quality measurement against human-audited samples

Expanded obligations:
  1. Implement format-specific extraction (HTML, PDF, code, notebooks, media
     transcripts) with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Frontier-Bench
     v0.1 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement boilerplate removal and content-quality preservation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of ARC-AGI-3, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  3. Implement encoding, language and script normalisation as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Frontier-Bench
     v0.1 — a regression on that benchmark is an automatic rejection of this
     part.
  4. Implement extraction-quality measurement against human-audited samples,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.data.data_extraction_pipeline_train@1
  cap.t17.data.data_extraction_pipeline_train.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_sourcing@1
      if unavailable: use the in-file conservative substitute for
      `data_sourcing` (documented, slower, lower quality) and set
      `degraded['data_sourcing']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t05.distillation.distillation_arch@1
      if unavailable: use the in-file conservative substitute for
      `distillation_arch` (documented, slower, lower quality) and set
      `degraded['distillation_arch']='local'`

  cap.t06.moe.moe_training_stability@1
      if unavailable: use the in-file conservative substitute for
      `moe_training_stability` (documented, slower, lower quality) and set
      `degraded['moe_training_stability']='local'`

  cap.t10.backtracking.backtracking@1
      if unavailable: use the in-file conservative substitute for
      `backtracking` (documented, slower, lower quality) and set
      `degraded['backtracking']='local'`

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
   3. [ 600 lines] Core implementation A - format-specific extraction (HTML, PDF, code, notebooks, media tr
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - boilerplate removal and content-quality preservation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - encoding, language and script normalisation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - extraction-quality measurement against human-audited samples
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_extraction_pipeline_train@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0802_data_extraction_pipeline_train.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0803-data-quality-filter

**P0803 · `data_quality_filter` — Data Quality Filtering & Scoring** · [spec](PART_SPECS_T17.md#p0803-data-quality-filter) · [self-contained txt](../prompts/P0803_data_quality_filter.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0803  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0803 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0803  (3/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Data Quality Filtering & Scoring
file         : parts/t17_training/P0803_data_quality_filter.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_quality_filter
language     : Python 3.13
capability   : cap.t17.data.data_quality_filter@1
determinism  : io
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Keeps the good 5% instead of the whole 100%.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-signal quality scoring (fluency, informativeness, correctness proxies)
  2. learned quality classifiers calibrated against human judgment
  3. domain-balanced filtering avoiding distribution collapse
  4. measured downstream-quality gain per filtering policy

Expanded obligations:
  1. Implement multi-signal quality scoring (fluency, informativeness,
     correctness proxies) together with its verification path, so that
     anything this mechanism produces can be independently re-checked *inside
     this same file* without contacting any other part. The checker must be
     cheap enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of ARC-AGI-3, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement learned quality classifiers calibrated against human judgment
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement domain-balanced filtering avoiding distribution collapse, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement measured downstream-quality gain per filtering policy with an
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
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.data.data_quality_filter@1
  cap.t17.data.data_quality_filter.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_extraction_pipeline_train@1
      if unavailable: use the in-file conservative substitute for
      `data_extraction_pipeline_train` (documented, slower, lower quality)
      and set `degraded['data_extraction_pipeline_train']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t05.multimodal.multimodal_fusion_arch@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_fusion_arch` (documented, slower, lower quality) and set
      `degraded['multimodal_fusion_arch']='local'`

  cap.t06.ensemble.ensemble_combiner@1
      if unavailable: use the in-file conservative substitute for
      `ensemble_combiner` (documented, slower, lower quality) and set
      `degraded['ensemble_combiner']='local'`

  cap.t10.question.question_asking@1
      if unavailable: use the in-file conservative substitute for
      `question_asking` (documented, slower, lower quality) and set
      `degraded['question_asking']='local'`

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
   3. [ 600 lines] Core implementation A - multi-signal quality scoring (fluency, informativeness, correctn
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - learned quality classifiers calibrated against human judgment
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - domain-balanced filtering avoiding distribution collapse
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured downstream-quality gain per filtering policy
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_quality_filter@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0803_data_quality_filter.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0804-data-dedup-train

**P0804 · `data_dedup_train` — Corpus Deduplication at Scale** · [spec](PART_SPECS_T17.md#p0804-data-dedup-train) · [self-contained txt](../prompts/P0804_data_dedup_train.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0804  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0804 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0804  (4/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Corpus Deduplication at Scale
file         : parts/t17_training/P0804_data_dedup_train.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_dedup_train
language     : Python 3.13
capability   : cap.t17.data.data_dedup_train@1
determinism  : io
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The same document ten times teaches nothing new.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. exact, near-duplicate and substring deduplication at petabyte scale
  2. cross-source and cross-modality duplicate detection
  3. deduplication effect on memorisation and generalisation measurement
  4. throughput and cost measurement per terabyte

Expanded obligations:
  1. Implement exact, near-duplicate and substring deduplication at petabyte
     scale as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement cross-source and cross-modality duplicate detection, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement deduplication effect on memorisation and generalisation
     measurement with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement throughput and cost measurement per terabyte together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
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
  cap.t17.data.data_dedup_train@1
  cap.t17.data.data_dedup_train.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_quality_filter@1
      if unavailable: use the in-file conservative substitute for
      `data_quality_filter` (documented, slower, lower quality) and set
      `degraded['data_quality_filter']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t05.context.context_packing@1
      if unavailable: use the in-file conservative substitute for
      `context_packing` (documented, slower, lower quality) and set
      `degraded['context_packing']='local'`

  cap.t06.expert.expert_alignment@1
      if unavailable: use the in-file conservative substitute for
      `expert_alignment` (documented, slower, lower quality) and set
      `degraded['expert_alignment']='local'`

  cap.t10.scratchpad.scratchpad_manager@1
      if unavailable: use the in-file conservative substitute for
      `scratchpad_manager` (documented, slower, lower quality) and set
      `degraded['scratchpad_manager']='local'`

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
   3. [ 600 lines] Core implementation A - exact, near-duplicate and substring deduplication at petabyte sc
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-source and cross-modality duplicate detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deduplication effect on memorisation and generalisation measurem
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput and cost measurement per terabyte
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_dedup_train@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0804_data_dedup_train.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0805-data-decontamination

**P0805 · `data_decontamination` — Benchmark Decontamination** · [spec](PART_SPECS_T17.md#p0805-data-decontamination) · [self-contained txt](../prompts/P0805_data_decontamination.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0805  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0805 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0805  (5/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Benchmark Decontamination
file         : parts/t17_training/P0805_data_decontamination.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_decontamination
language     : Python 3.13
capability   : cap.t17.data.data_decontamination@1
determinism  : io
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Guarantees benchmark results mean something.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. n-gram, embedding and paraphrase-level contamination detection
  2. held-out benchmark protection with sealed test sets
  3. contamination-report generation per benchmark
  4. verification that reported scores are contamination-free

Expanded obligations:
  1. Implement n-gram, embedding and paraphrase-level contamination
     detection, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement held-out benchmark protection with sealed test sets with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement contamination-report generation per benchmark together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement verification that reported scores are contamination-free as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
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
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.data.data_decontamination@1
  cap.t17.data.data_decontamination.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_dedup_train@1
      if unavailable: use the in-file conservative substitute for
      `data_dedup_train` (documented, slower, lower quality) and set
      `degraded['data_dedup_train']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t05.capacity.capacity_probes@1
      if unavailable: use the in-file conservative substitute for
      `capacity_probes` (documented, slower, lower quality) and set
      `degraded['capacity_probes']='local'`

  cap.t06.moe.moe_speed_accounting@1
      if unavailable: use the in-file conservative substitute for
      `moe_speed_accounting` (documented, slower, lower quality) and set
      `degraded['moe_speed_accounting']='local'`

  cap.t10.reasoning.reasoning_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_speed_proof` (documented, slower, lower quality) and set
      `degraded['reasoning_speed_proof']='local'`

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
   3. [ 600 lines] Core implementation A - n-gram, embedding and paraphrase-level contamination detection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - held-out benchmark protection with sealed test sets
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - contamination-report generation per benchmark
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification that reported scores are contamination-free
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_decontamination@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0805_data_decontamination.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0806-data-mixture

**P0806 · `data_mixture` — Data Mixture Optimisation** · [spec](PART_SPECS_T17.md#p0806-data-mixture) · [self-contained txt](../prompts/P0806_data_mixture.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0806  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0806 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0806  (6/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Data Mixture Optimisation
file         : parts/t17_training/P0806_data_mixture.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_mixture
language     : Python 3.13
capability   : cap.t17.data.data_mixture@1
determinism  : io
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The recipe matters as much as the amount.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mixture-weight optimisation against downstream capability targets
  2. curriculum scheduling across training phases
  3. domain-repetition policy with memorisation monitoring
  4. measured capability gain from optimised mixtures

Expanded obligations:
  1. Implement mixture-weight optimisation against downstream capability
     targets with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement curriculum scheduling across training phases together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement domain-repetition policy with memorisation monitoring as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement measured capability gain from optimised mixtures, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
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
  cap.t17.data.data_mixture@1
  cap.t17.data.data_mixture.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_decontamination@1
      if unavailable: use the in-file conservative substitute for
      `data_decontamination` (documented, slower, lower quality) and set
      `degraded['data_decontamination']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t05.recurrent.recurrent_memory_layer@1
      if unavailable: use the in-file conservative substitute for
      `recurrent_memory_layer` (documented, slower, lower quality) and set
      `degraded['recurrent_memory_layer']='local'`

  cap.t06.expert.expert_attention@1
      if unavailable: use the in-file conservative substitute for
      `expert_attention` (documented, slower, lower quality) and set
      `degraded['expert_attention']='local'`

  cap.t10.process.process_verifier@1
      if unavailable: use the in-file conservative substitute for
      `process_verifier` (documented, slower, lower quality) and set
      `degraded['process_verifier']='local'`

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
   3. [ 600 lines] Core implementation A - mixture-weight optimisation against downstream capability target
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - curriculum scheduling across training phases
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - domain-repetition policy with memorisation monitoring
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured capability gain from optimised mixtures
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_mixture@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0806_data_mixture.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0807-synthetic-data-engine

**P0807 · `synthetic_data_engine` — Synthetic Data Generation Engine** · [spec](PART_SPECS_T17.md#p0807-synthetic-data-engine) · [self-contained txt](../prompts/P0807_synthetic_data_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0807  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0807 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0807  (7/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Synthetic Data Generation Engine
file         : parts/t17_training/P0807_synthetic_data_engine.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.synthetic_data_engine
language     : Python 3.13
capability   : cap.t17.synthetic.synthetic_data_engine@1
determinism  : io
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Generates the data that closes each measured capability gap.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gap-targeted generation with difficulty and diversity control
  2. quality verification and filtering of generated data
  3. model-collapse prevention via grounding and diversity metrics
  4. measured capability gain per synthetic campaign

Expanded obligations:
  1. Implement gap-targeted generation with difficulty and diversity control
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement quality verification and filtering of generated data as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement model-collapse prevention via grounding and diversity metrics,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured capability gain per synthetic campaign with an
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.synthetic.synthetic_data_engine@1
  cap.t17.synthetic.synthetic_data_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_mixture@1
      if unavailable: use the in-file conservative substitute for
      `data_mixture` (documented, slower, lower quality) and set
      `degraded['data_mixture']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t05.byte.byte_latent_patching@1
      if unavailable: use the in-file conservative substitute for
      `byte_latent_patching` (documented, slower, lower quality) and set
      `degraded['byte_latent_patching']='local'`

  cap.t06.expert.expert_lifecycle@1
      if unavailable: use the in-file conservative substitute for
      `expert_lifecycle` (documented, slower, lower quality) and set
      `degraded['expert_lifecycle']='local'`

  cap.t10.goal.goal_management@1
      if unavailable: use the in-file conservative substitute for
      `goal_management` (documented, slower, lower quality) and set
      `degraded['goal_management']='local'`

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
   3. [ 600 lines] Core implementation A - gap-targeted generation with difficulty and diversity control
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quality verification and filtering of generated data
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - model-collapse prevention via grounding and diversity metrics
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured capability gain per synthetic campaign
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.synthetic.synthetic_data_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0807_synthetic_data_engine.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0808-verifiable-task-gen

**P0808 · `verifiable_task_gen` — Verifiable Task & Reward Generation** · [spec](PART_SPECS_T17.md#p0808-verifiable-task-gen) · [self-contained txt](../prompts/P0808_verifiable_task_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0808  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0808 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0808  (8/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Verifiable Task & Reward Generation
file         : parts/t17_training/P0808_verifiable_task_gen.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.verifiable_task_gen
language     : Python 3.13
capability   : cap.t17.verifiable.verifiable_task_gen@1
determinism  : io
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Millions of problems with automatically checkable answers.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. automatic task generation with programmatic verifiers
  2. difficulty calibration against current model capability
  3. verifier-correctness auditing (no reward hacking loopholes)
  4. measured RL-training gain from generated task sets

Expanded obligations:
  1. Implement automatic task generation with programmatic verifiers as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement difficulty calibration against current model capability, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement verifier-correctness auditing (no reward hacking loopholes)
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Frontier-Bench v0.1 — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement measured RL-training gain from generated task sets together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's ARC-AGI-3 target reachable; the part therefore ships a
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
  cap.t17.verifiable.verifiable_task_gen@1
  cap.t17.verifiable.verifiable_task_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.synthetic.synthetic_data_engine@1
      if unavailable: use the in-file conservative substitute for
      `synthetic_data_engine` (documented, slower, lower quality) and set
      `degraded['synthetic_data_engine']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t05.world.world_model_core@1
      if unavailable: use the in-file conservative substitute for
      `world_model_core` (documented, slower, lower quality) and set
      `degraded['world_model_core']='local'`

  cap.t06.token.token_dropping@1
      if unavailable: use the in-file conservative substitute for
      `token_dropping` (documented, slower, lower quality) and set
      `degraded['token_dropping']='local'`

  cap.t10.probabilistic.probabilistic_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `probabilistic_reasoning` (documented, slower, lower quality) and set
      `degraded['probabilistic_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - automatic task generation with programmatic verifiers
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - difficulty calibration against current model capability
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - verifier-correctness auditing (no reward hacking loopholes)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured RL-training gain from generated task sets
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.verifiable.verifiable_task_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0808_verifiable_task_gen.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0809-data-augmentation

**P0809 · `data_augmentation` — Data Augmentation & Transformation** · [spec](PART_SPECS_T17.md#p0809-data-augmentation) · [self-contained txt](../prompts/P0809_data_augmentation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0809  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0809 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0809  (9/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Data Augmentation & Transformation
file         : parts/t17_training/P0809_data_augmentation.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_augmentation
language     : Python 3.13
capability   : cap.t17.data.data_augmentation@1
determinism  : io
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Multiplies useful data without multiplying noise.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. semantics-preserving transformation library per data type
  2. adversarial and robustness-targeted augmentation
  3. augmentation-quality verification
  4. measured robustness improvement per augmentation type

Expanded obligations:
  1. Implement semantics-preserving transformation library per data type, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement adversarial and robustness-targeted augmentation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement augmentation-quality verification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's ARC-AGI-3 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured robustness improvement per augmentation type as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
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
  cap.t17.data.data_augmentation@1
  cap.t17.data.data_augmentation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.verifiable.verifiable_task_gen@1
      if unavailable: use the in-file conservative substitute for
      `verifiable_task_gen` (documented, slower, lower quality) and set
      `degraded['verifiable_task_gen']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t05.model.model_merging@1
      if unavailable: use the in-file conservative substitute for
      `model_merging` (documented, slower, lower quality) and set
      `degraded['model_merging']='local'`

  cap.t06.router.router_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `router_interpretability` (documented, slower, lower quality) and set
      `degraded['router_interpretability']='local'`

  cap.t10.stopping.stopping_rules@1
      if unavailable: use the in-file conservative substitute for
      `stopping_rules` (documented, slower, lower quality) and set
      `degraded['stopping_rules']='local'`

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
   3. [ 600 lines] Core implementation A - semantics-preserving transformation library per data type
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - adversarial and robustness-targeted augmentation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - augmentation-quality verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured robustness improvement per augmentation type
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_augmentation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0809_data_augmentation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0810-tokenizer-training

**P0810 · `tokenizer_training` — Tokeniser Training & Evaluation** · [spec](PART_SPECS_T17.md#p0810-tokenizer-training) · [self-contained txt](../prompts/P0810_tokenizer_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0810  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0810 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0810  (10/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Tokeniser Training & Evaluation
file         : parts/t17_training/P0810_tokenizer_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.tokenizer_training
language     : Python 3.13
capability   : cap.t17.tokenizer.tokenizer_training@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Trains the Ω-tokeniser that fixes the token tax.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. vocabulary learning with multilingual and code fairness objectives
  2. compression-rate measurement per language and domain
  3. boundary-quality evaluation for math, code and rare scripts
  4. target: significantly fewer tokens per text than the Opus 4.7+ tokenizer

Expanded obligations:
  1. Implement vocabulary learning with multilingual and code fairness
     objectives with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Frontier-Bench v0.1
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement compression-rate measurement per language and domain together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's ARC-AGI-3 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement boundary-quality evaluation for math, code and rare scripts as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement target: significantly fewer tokens per text than the Opus 4.7+
     tokenizer, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.tokenizer.tokenizer_training@1
  cap.t17.tokenizer.tokenizer_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_augmentation@1
      if unavailable: use the in-file conservative substitute for
      `data_augmentation` (documented, slower, lower quality) and set
      `degraded['data_augmentation']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t05.logit.logit_head_design@1
      if unavailable: use the in-file conservative substitute for
      `logit_head_design` (documented, slower, lower quality) and set
      `degraded['logit_head_design']='local'`

  cap.t06.model.model_cascade_routing@1
      if unavailable: use the in-file conservative substitute for
      `model_cascade_routing` (documented, slower, lower quality) and set
      `degraded['model_cascade_routing']='local'`

  cap.t10.assumption.assumption_tracking@1
      if unavailable: use the in-file conservative substitute for
      `assumption_tracking` (documented, slower, lower quality) and set
      `degraded['assumption_tracking']='local'`

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
   3. [ 600 lines] Core implementation A - vocabulary learning with multilingual and code fairness objectiv
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - compression-rate measurement per language and domain
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - boundary-quality evaluation for math, code and rare scripts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: significantly fewer tokens per text than the Opus 4.7+ t
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.tokenizer.tokenizer_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0810_tokenizer_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0811-data-loader

**P0811 · `data_loader` — High-Throughput Training Data Loader** · [spec](PART_SPECS_T17.md#p0811-data-loader) · [self-contained txt](../prompts/P0811_data_loader.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0811  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0811 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0811  (11/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : High-Throughput Training Data Loader
file         : parts/t17_training/P0811_data_loader.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.data_loader
language     : Python 3.13
capability   : cap.t17.data.data_loader@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Never starves 100k accelerators.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. streaming loader with deterministic shuffling and exact resumption
  2. on-the-fly packing, masking and augmentation
  3. throughput measurement saturating training compute
  4. determinism verification across restarts and rescales

Expanded obligations:
  1. Implement streaming loader with deterministic shuffling and exact
     resumption together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's ARC-AGI-3 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement on-the-fly packing, masking and augmentation as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement throughput measurement saturating training compute, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement determinism verification across restarts and rescales with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.data.data_loader@1
  cap.t17.data.data_loader.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.tokenizer.tokenizer_training@1
      if unavailable: use the in-file conservative substitute for
      `tokenizer_training` (documented, slower, lower quality) and set
      `degraded['tokenizer_training']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t05.numerical.numerical_arch_stability@1
      if unavailable: use the in-file conservative substitute for
      `numerical_arch_stability` (documented, slower, lower quality) and set
      `degraded['numerical_arch_stability']='local'`

  cap.t06.sparse.sparse_gradient@1
      if unavailable: use the in-file conservative substitute for
      `sparse_gradient` (documented, slower, lower quality) and set
      `degraded['sparse_gradient']='local'`

  cap.t10.reasoning.reasoning_cost_model@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_cost_model` (documented, slower, lower quality) and set
      `degraded['reasoning_cost_model']='local'`

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
   3. [ 600 lines] Core implementation A - streaming loader with deterministic shuffling and exact resumpti
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - on-the-fly packing, masking and augmentation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - throughput measurement saturating training compute
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - determinism verification across restarts and rescales
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.data.data_loader@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0811_data_loader.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0812-pretraining-loop

**P0812 · `pretraining_loop` — Pretraining Loop & Orchestration** · [spec](PART_SPECS_T17.md#p0812-pretraining-loop) · [self-contained txt](../prompts/P0812_pretraining_loop.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0812  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0812 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0812  (12/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Pretraining Loop & Orchestration
file         : parts/t17_training/P0812_pretraining_loop.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.pretraining_loop
language     : Python 3.13
capability   : cap.t17.pretraining.pretraining_loop@1
determinism  : io
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The main training run: stable, observable, restartable.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. training step orchestration with gradient accumulation and clipping
  2. loss-spike detection with automatic rollback and data skipping
  3. checkpoint policy with fast resumption
  4. measured stability over trillion-token runs

Expanded obligations:
  1. Implement training step orchestration with gradient accumulation and
     clipping as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement loss-spike detection with automatic rollback and data
     skipping, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
     — a regression on that benchmark is an automatic rejection of this part.
  3. Implement checkpoint policy with fast resumption with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured stability over trillion-token runs together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of ARC-AGI-3, so its p99 latency assertion is part of
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.pretraining.pretraining_loop@1
  cap.t17.pretraining.pretraining_loop.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.data.data_loader@1
      if unavailable: use the in-file conservative substitute for
      `data_loader` (documented, slower, lower quality) and set
      `degraded['data_loader']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t05.arch.arch_ablation_suite@1
      if unavailable: use the in-file conservative substitute for
      `arch_ablation_suite` (documented, slower, lower quality) and set
      `degraded['arch_ablation_suite']='local'`

  cap.t06.sparsity.sparsity_verification@1
      if unavailable: use the in-file conservative substitute for
      `sparsity_verification` (documented, slower, lower quality) and set
      `degraded['sparsity_verification']='local'`

  cap.t10.collective.collective_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `collective_reasoning` (documented, slower, lower quality) and set
      `degraded['collective_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - training step orchestration with gradient accumulation and clipp
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - loss-spike detection with automatic rollback and data skipping
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - checkpoint policy with fast resumption
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured stability over trillion-token runs
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.pretraining.pretraining_loop@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0812_pretraining_loop.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0813-optimiser-design

**P0813 · `optimiser_design` — Optimiser Design & Implementation** · [spec](PART_SPECS_T17.md#p0813-optimiser-design) · [self-contained txt](../prompts/P0813_optimiser_design.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0813  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0813 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0813  (13/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Optimiser Design & Implementation
file         : parts/t17_training/P0813_optimiser_design.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.optimiser_design
language     : Python 3.13
capability   : cap.t17.optimiser.optimiser_design@1
determinism  : io
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The update rule, chosen and tuned by measurement.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. second-order-informed and adaptive optimiser implementations
  2. hyperparameter transfer across scale via muP-style parameterisation
  3. memory-efficient optimiser state (sharded, quantised)
  4. convergence-speed comparison across optimisers at matched compute

Expanded obligations:
  1. Implement second-order-informed and adaptive optimiser implementations,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement hyperparameter transfer across scale via muP-style
     parameterisation with an explicit *a-priori* cost model. Before doing
     the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Correctness here is what makes the
     tier's Frontier-Bench v0.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement memory-efficient optimiser state (sharded, quantised) together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of ARC-AGI-3, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement convergence-speed comparison across optimisers at matched
     compute as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.optimiser.optimiser_design@1
  cap.t17.optimiser.optimiser_design.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.pretraining.pretraining_loop@1
      if unavailable: use the in-file conservative substitute for
      `pretraining_loop` (documented, slower, lower quality) and set
      `degraded['pretraining_loop']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t05.state.state_space_layer@1
      if unavailable: use the in-file conservative substitute for
      `state_space_layer` (documented, slower, lower quality) and set
      `degraded['state_space_layer']='local'`

  cap.t06.expert.expert_ffn@1
      if unavailable: use the in-file conservative substitute for
      `expert_ffn` (documented, slower, lower quality) and set
      `degraded['expert_ffn']='local'`

  cap.t10.beam.beam_pruning@1
      if unavailable: use the in-file conservative substitute for
      `beam_pruning` (documented, slower, lower quality) and set
      `degraded['beam_pruning']='local'`

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
   3. [ 600 lines] Core implementation A - second-order-informed and adaptive optimiser implementations
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - hyperparameter transfer across scale via muP-style parameterisat
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - memory-efficient optimiser state (sharded, quantised)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - convergence-speed comparison across optimisers at matched comput
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.optimiser.optimiser_design@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0813_optimiser_design.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0814-lr-schedule

**P0814 · `lr_schedule` — Learning Rate & Schedule Optimisation** · [spec](PART_SPECS_T17.md#p0814-lr-schedule) · [self-contained txt](../prompts/P0814_lr_schedule.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0814  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0814 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0814  (14/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Learning Rate & Schedule Optimisation
file         : parts/t17_training/P0814_lr_schedule.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.lr_schedule
language     : Python 3.13
capability   : cap.t17.lr.lr_schedule@1
determinism  : io
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Schedules derived from theory and validated by runs.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. warmup, decay and cyclical schedule families with selection criteria
  2. schedule-adaptation from observed loss dynamics
  3. batch-size/learning-rate scaling relationships
  4. measured final-quality effect per schedule

Expanded obligations:
  1. Implement warmup, decay and cyclical schedule families with selection
     criteria with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Frontier-Bench
     v0.1 target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  2. Implement schedule-adaptation from observed loss dynamics together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of ARC-AGI-3, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  3. Implement batch-size/learning-rate scaling relationships as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured final-quality effect per schedule, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.lr.lr_schedule@1
  cap.t17.lr.lr_schedule.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.optimiser.optimiser_design@1
      if unavailable: use the in-file conservative substitute for
      `optimiser_design` (documented, slower, lower quality) and set
      `degraded['optimiser_design']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t05.tokeniser.tokeniser_omega@1
      if unavailable: use the in-file conservative substitute for
      `tokeniser_omega` (documented, slower, lower quality) and set
      `degraded['tokeniser_omega']='local'`

  cap.t06.moe.moe_determinism@1
      if unavailable: use the in-file conservative substitute for
      `moe_determinism` (documented, slower, lower quality) and set
      `degraded['moe_determinism']='local'`

  cap.t10.planning.planning_engine@1
      if unavailable: use the in-file conservative substitute for
      `planning_engine` (documented, slower, lower quality) and set
      `degraded['planning_engine']='local'`

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
   3. [ 600 lines] Core implementation A - warmup, decay and cyclical schedule families with selection crit
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - schedule-adaptation from observed loss dynamics
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - batch-size/learning-rate scaling relationships
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured final-quality effect per schedule
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.lr.lr_schedule@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0814_lr_schedule.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0815-gradient-engineering

**P0815 · `gradient_engineering` — Gradient Processing & Stability** · [spec](PART_SPECS_T17.md#p0815-gradient-engineering) · [self-contained txt](../prompts/P0815_gradient_engineering.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0815  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0815 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0815  (15/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Gradient Processing & Stability
file         : parts/t17_training/P0815_gradient_engineering.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.gradient_engineering
language     : Python 3.13
capability   : cap.t17.gradient.gradient_engineering@1
determinism  : io
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Keeps a trillion-parameter sparse model training.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gradient clipping, normalisation and spike handling policies
  2. low-precision gradient handling with error feedback
  3. gradient-noise and signal-to-noise diagnostics
  4. stability evidence at extreme scale

Expanded obligations:
  1. Implement gradient clipping, normalisation and spike handling policies
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement low-precision gradient handling with error feedback as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement gradient-noise and signal-to-noise diagnostics, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement stability evidence at extreme scale with an explicit
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.gradient.gradient_engineering@1
  cap.t17.gradient.gradient_engineering.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.lr.lr_schedule@1
      if unavailable: use the in-file conservative substitute for
      `lr_schedule` (documented, slower, lower quality) and set
      `degraded['lr_schedule']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t05.uncertainty.uncertainty_calibration@1
      if unavailable: use the in-file conservative substitute for
      `uncertainty_calibration` (documented, slower, lower quality) and set
      `degraded['uncertainty_calibration']='local'`

  cap.t06.moe.moe_batching@1
      if unavailable: use the in-file conservative substitute for
      `moe_batching` (documented, slower, lower quality) and set
      `degraded['moe_batching']='local'`

  cap.t10.counterfactual.counterfactual_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `counterfactual_reasoning` (documented, slower, lower quality) and set
      `degraded['counterfactual_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - gradient clipping, normalisation and spike handling policies
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - low-precision gradient handling with error feedback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - gradient-noise and signal-to-noise diagnostics
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - stability evidence at extreme scale
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.gradient.gradient_engineering@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0815_gradient_engineering.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0816-training-parallelism

**P0816 · `training_parallelism` — Training Parallelism Strategy** · [spec](PART_SPECS_T17.md#p0816-training-parallelism) · [self-contained txt](../prompts/P0816_training_parallelism.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0816  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0816 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0816  (16/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Parallelism Strategy
file         : parts/t17_training/P0816_training_parallelism.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_parallelism
language     : Python 3.13
capability   : cap.t17.training.training_parallelism@1
determinism  : io
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Uses 100k accelerators efficiently.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hybrid data/tensor/pipeline/expert/sequence parallel configuration
  2. communication-computation overlap maximisation
  3. memory-optimiser (sharding, offload, remat) integration
  4. measured hardware-utilisation percentage at full scale

Expanded obligations:
  1. Implement hybrid data/tensor/pipeline/expert/sequence parallel
     configuration as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement communication-computation overlap maximisation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement memory-optimiser (sharding, offload, remat) integration with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement measured hardware-utilisation percentage at full scale
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against ARC-AGI-3 — a regression on that
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.training.training_parallelism@1
  cap.t17.training.training_parallelism.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.gradient.gradient_engineering@1
      if unavailable: use the in-file conservative substitute for
      `gradient_engineering` (documented, slower, lower quality) and set
      `degraded['gradient_engineering']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t05.knowledge.knowledge_editing@1
      if unavailable: use the in-file conservative substitute for
      `knowledge_editing` (documented, slower, lower quality) and set
      `degraded['knowledge_editing']='local'`

  cap.t06.moe.moe_scaling_laws@1
      if unavailable: use the in-file conservative substitute for
      `moe_scaling_laws` (documented, slower, lower quality) and set
      `degraded['moe_scaling_laws']='local'`

  cap.t10.difficulty.difficulty_estimation@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_estimation` (documented, slower, lower quality) and set
      `degraded['difficulty_estimation']='local'`

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
   3. [ 600 lines] Core implementation A - hybrid data/tensor/pipeline/expert/sequence parallel configurati
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - communication-computation overlap maximisation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - memory-optimiser (sharding, offload, remat) integration
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured hardware-utilisation percentage at full scale
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_parallelism@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0816_training_parallelism.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0817-training-efficiency

**P0817 · `training_efficiency` — Training Compute Efficiency** · [spec](PART_SPECS_T17.md#p0817-training-efficiency) · [self-contained txt](../prompts/P0817_training_efficiency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0817  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0817 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0817  (17/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Compute Efficiency
file         : parts/t17_training/P0817_training_efficiency.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_efficiency
language     : Python 3.13
capability   : cap.t17.training.training_efficiency@1
determinism  : io
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Every FLOP must earn its place.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. model-FLOPs-utilisation measurement and optimisation
  2. wasted-compute identification (padding, bubbles, recompute, restarts)
  3. efficiency comparison against published large-run baselines
  4. measured cost-per-capability improvement

Expanded obligations:
  1. Implement model-FLOPs-utilisation measurement and optimisation, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement wasted-compute identification (padding, bubbles, recompute,
     restarts) with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement efficiency comparison against published large-run baselines
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured cost-per-capability improvement as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's
     Frontier-Bench v0.1 target reachable; the part therefore ships a
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.training.training_efficiency@1
  cap.t17.training.training_efficiency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.training.training_parallelism@1
      if unavailable: use the in-file conservative substitute for
      `training_parallelism` (documented, slower, lower quality) and set
      `degraded['training_parallelism']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t05.residual.residual_stream_design@1
      if unavailable: use the in-file conservative substitute for
      `residual_stream_design` (documented, slower, lower quality) and set
      `degraded['residual_stream_design']='local'`

  cap.t06.cost.cost_aware_routing@1
      if unavailable: use the in-file conservative substitute for
      `cost_aware_routing` (documented, slower, lower quality) and set
      `degraded['cost_aware_routing']='local'`

  cap.t10.evidence.evidence_integration@1
      if unavailable: use the in-file conservative substitute for
      `evidence_integration` (documented, slower, lower quality) and set
      `degraded['evidence_integration']='local'`

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
   3. [ 600 lines] Core implementation A - model-FLOPs-utilisation measurement and optimisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - wasted-compute identification (padding, bubbles, recompute, rest
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - efficiency comparison against published large-run baselines
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured cost-per-capability improvement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_efficiency@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0817_training_efficiency.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0818-checkpoint-management

**P0818 · `checkpoint_management` — Checkpoint Management & Model Registry** · [spec](PART_SPECS_T17.md#p0818-checkpoint-management) · [self-contained txt](../prompts/P0818_checkpoint_management.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0818  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0818 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0818  (18/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Checkpoint Management & Model Registry
file         : parts/t17_training/P0818_checkpoint_management.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.checkpoint_management
language     : Python 3.13
capability   : cap.t17.checkpoint.checkpoint_management@1
determinism  : io
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Every model version tracked, evaluated and reproducible.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. checkpoint storage with metadata, lineage and evaluation results
  2. checkpoint averaging and selection methodology
  3. reproducibility metadata sufficient to recreate any checkpoint
  4. registry integrity and retention policy

Expanded obligations:
  1. Implement checkpoint storage with metadata, lineage and evaluation
     results with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement checkpoint averaging and selection methodology together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement reproducibility metadata sufficient to recreate any checkpoint
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement registry integrity and retention policy, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
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
  cap.t17.checkpoint.checkpoint_management@1
  cap.t17.checkpoint.checkpoint_management.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.training.training_efficiency@1
      if unavailable: use the in-file conservative substitute for
      `training_efficiency` (documented, slower, lower quality) and set
      `degraded['training_efficiency']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t05.model.model_surgery@1
      if unavailable: use the in-file conservative substitute for
      `model_surgery` (documented, slower, lower quality) and set
      `degraded['model_surgery']='local'`

  cap.t06.router.router_online_learning@1
      if unavailable: use the in-file conservative substitute for
      `router_online_learning` (documented, slower, lower quality) and set
      `degraded['router_online_learning']='local'`

  cap.t10.reasoning.reasoning_search_bench@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_search_bench` (documented, slower, lower quality) and set
      `degraded['reasoning_search_bench']='local'`

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
   3. [ 600 lines] Core implementation A - checkpoint storage with metadata, lineage and evaluation results
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - checkpoint averaging and selection methodology
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reproducibility metadata sufficient to recreate any checkpoint
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - registry integrity and retention policy
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.checkpoint.checkpoint_management@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0818_checkpoint_management.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0819-training-monitoring

**P0819 · `training_monitoring` — Training Observability & Diagnostics** · [spec](PART_SPECS_T17.md#p0819-training-monitoring) · [self-contained txt](../prompts/P0819_training_monitoring.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0819  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0819 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0819  (19/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Observability & Diagnostics
file         : parts/t17_training/P0819_training_monitoring.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_monitoring
language     : Python 3.13
capability   : cap.t17.training.training_monitoring@1
determinism  : io
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Sees problems in hours, not weeks.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. loss, gradient, activation and routing diagnostics with alerting
  2. capability-emergence tracking via periodic evaluations
  3. anomaly detection on training dynamics
  4. measured mean-time-to-detection of training pathologies

Expanded obligations:
  1. Implement loss, gradient, activation and routing diagnostics with
     alerting together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against ARC-AGI-3 — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement capability-emergence tracking via periodic evaluations as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement anomaly detection on training dynamics, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured mean-time-to-detection of training pathologies with
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.training.training_monitoring@1
  cap.t17.training.training_monitoring.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.checkpoint.checkpoint_management@1
      if unavailable: use the in-file conservative substitute for
      `checkpoint_management` (documented, slower, lower quality) and set
      `degraded['checkpoint_management']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t05.reference.reference_forward@1
      if unavailable: use the in-file conservative substitute for
      `reference_forward` (documented, slower, lower quality) and set
      `degraded['reference_forward']='local'`

  cap.t06.adaptive.adaptive_sparsity@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_sparsity` (documented, slower, lower quality) and set
      `degraded['adaptive_sparsity']='local'`

  cap.t10.reasoning.reasoning_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_interpretability` (documented, slower, lower quality) and
      set `degraded['reasoning_interpretability']='local'`

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
   3. [ 600 lines] Core implementation A - loss, gradient, activation and routing diagnostics with alerting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability-emergence tracking via periodic evaluations
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - anomaly detection on training dynamics
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured mean-time-to-detection of training pathologies
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_monitoring@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0819_training_monitoring.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0820-sft-pipeline

**P0820 · `sft_pipeline` — Supervised Fine-Tuning Pipeline** · [spec](PART_SPECS_T17.md#p0820-sft-pipeline) · [self-contained txt](../prompts/P0820_sft_pipeline.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0820  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0820 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0820  (20/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Supervised Fine-Tuning Pipeline
file         : parts/t17_training/P0820_sft_pipeline.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.sft_pipeline
language     : Python 3.13
capability   : cap.t17.sft.sft_pipeline@1
determinism  : io
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Teaches the model to be useful, not just predictive.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. demonstration-data curation with quality and diversity control
  2. multi-task instruction tuning with capability-balance measurement
  3. overfitting and capability-regression monitoring
  4. measured instruction-following improvement

Expanded obligations:
  1. Implement demonstration-data curation with quality and diversity control
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement multi-task instruction tuning with capability-balance
     measurement, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement overfitting and capability-regression monitoring with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured instruction-following improvement together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's ARC-AGI-3 target reachable; the part therefore ships a
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.sft.sft_pipeline@1
  cap.t17.sft.sft_pipeline.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.training.training_monitoring@1
      if unavailable: use the in-file conservative substitute for
      `training_monitoring` (documented, slower, lower quality) and set
      `degraded['training_monitoring']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t05.kv.kv_compression_model@1
      if unavailable: use the in-file conservative substitute for
      `kv_compression_model` (documented, slower, lower quality) and set
      `degraded['kv_compression_model']='local'`

  cap.t06.router.router_hash_hybrid@1
      if unavailable: use the in-file conservative substitute for
      `router_hash_hybrid` (documented, slower, lower quality) and set
      `degraded['router_hash_hybrid']='local'`

  cap.t10.graph.graph_search@1
      if unavailable: use the in-file conservative substitute for
      `graph_search` (documented, slower, lower quality) and set
      `degraded['graph_search']='local'`

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
   3. [ 600 lines] Core implementation A - demonstration-data curation with quality and diversity control
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - multi-task instruction tuning with capability-balance measuremen
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - overfitting and capability-regression monitoring
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured instruction-following improvement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.sft.sft_pipeline@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0820_sft_pipeline.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0821-rlvr-pipeline

**P0821 · `rlvr_pipeline` — RL from Verifiable Rewards** · [spec](PART_SPECS_T17.md#p0821-rlvr-pipeline) · [self-contained txt](../prompts/P0821_rlvr_pipeline.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0821  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0821 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0821  (21/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : RL from Verifiable Rewards
file         : parts/t17_training/P0821_rlvr_pipeline.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.rlvr_pipeline
language     : Python 3.13
capability   : cap.t17.rlvr.rlvr_pipeline@1
determinism  : io
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The engine behind superhuman coding, math and agent performance.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. policy optimisation against programmatic verifiers at scale
  2. reward-hacking detection and verifier hardening
  3. credit assignment over long multi-step trajectories
  4. measured capability gain on verifiable-task benchmarks

Expanded obligations:
  1. Implement policy optimisation against programmatic verifiers at scale,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement reward-hacking detection and verifier hardening with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement credit assignment over long multi-step trajectories together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's ARC-AGI-3 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured capability gain on verifiable-task benchmarks as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
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
                       p99 <= 25000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.rlvr.rlvr_pipeline@1
  cap.t17.rlvr.rlvr_pipeline.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.sft.sft_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `sft_pipeline` (documented, slower, lower quality) and set
      `degraded['sft_pipeline']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t05.embedding.embedding_design@1
      if unavailable: use the in-file conservative substitute for
      `embedding_design` (documented, slower, lower quality) and set
      `degraded['embedding_design']='local'`

  cap.t06.router.router_lookahead@1
      if unavailable: use the in-file conservative substitute for
      `router_lookahead` (documented, slower, lower quality) and set
      `degraded['router_lookahead']='local'`

  cap.t10.decomposition.decomposition@1
      if unavailable: use the in-file conservative substitute for
      `decomposition` (documented, slower, lower quality) and set
      `degraded['decomposition']='local'`

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
   3. [ 600 lines] Core implementation A - policy optimisation against programmatic verifiers at scale
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - reward-hacking detection and verifier hardening
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - credit assignment over long multi-step trajectories
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured capability gain on verifiable-task benchmarks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.rlvr.rlvr_pipeline@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0821_rlvr_pipeline.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0822-rlhf-pipeline

**P0822 · `rlhf_pipeline` — RL from Human & AI Feedback** · [spec](PART_SPECS_T17.md#p0822-rlhf-pipeline) · [self-contained txt](../prompts/P0822_rlhf_pipeline.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0822  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0822 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0822  (22/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : RL from Human & AI Feedback
file         : parts/t17_training/P0822_rlhf_pipeline.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.rlhf_pipeline
language     : Python 3.13
capability   : cap.t17.rlhf.rlhf_pipeline@1
determinism  : io
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Aligns quality and behaviour to what people actually want.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. preference-data collection protocol with rater-quality control
  2. reward-model training with calibration and robustness testing
  3. policy optimisation with KL control and over-optimisation detection
  4. measured preference-win-rate improvement

Expanded obligations:
  1. Implement preference-data collection protocol with rater-quality control
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Frontier-Bench v0.1 — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement reward-model training with calibration and robustness testing
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement policy optimisation with KL control and over-optimisation
     detection as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured preference-win-rate improvement, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
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
  cap.t17.rlhf.rlhf_pipeline@1
  cap.t17.rlhf.rlhf_pipeline.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.rlvr.rlvr_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `rlvr_pipeline` (documented, slower, lower quality) and set
      `degraded['rlvr_pipeline']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t05.verifier.verifier_head@1
      if unavailable: use the in-file conservative substitute for
      `verifier_head` (documented, slower, lower quality) and set
      `degraded['verifier_head']='local'`

  cap.t06.expert.expert_offload@1
      if unavailable: use the in-file conservative substitute for
      `expert_offload` (documented, slower, lower quality) and set
      `degraded['expert_offload']='local'`

  cap.t10.program.program_synthesis_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `program_synthesis_reasoning` (documented, slower, lower quality) and
      set `degraded['program_synthesis_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - preference-data collection protocol with rater-quality control
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - reward-model training with calibration and robustness testing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - policy optimisation with KL control and over-optimisation detect
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured preference-win-rate improvement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.rlhf.rlhf_pipeline@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0822_rlhf_pipeline.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0823-reward-model

**P0823 · `reward_model` — Reward Model Design & Robustness** · [spec](PART_SPECS_T17.md#p0823-reward-model) · [self-contained txt](../prompts/P0823_reward_model.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0823  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0823 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0823  (23/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Reward Model Design & Robustness
file         : parts/t17_training/P0823_reward_model.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.reward_model
language     : Python 3.13
capability   : cap.t17.reward.reward_model@1
determinism  : io
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
A reward model that cannot be gamed.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-objective reward modelling (correctness, helpfulness, safety, style)
  2. adversarial robustness testing against reward hacking
  3. calibration and disagreement-aware ensembling
  4. measured correlation with expert human judgment

Expanded obligations:
  1. Implement multi-objective reward modelling (correctness, helpfulness,
     safety, style) together with its verification path, so that anything
     this mechanism produces can be independently re-checked *inside this
     same file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's ARC-AGI-3 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement adversarial robustness testing against reward hacking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement calibration and disagreement-aware ensembling, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured correlation with expert human judgment with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.reward.reward_model@1
  cap.t17.reward.reward_model.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.rlhf.rlhf_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `rlhf_pipeline` (documented, slower, lower quality) and set
      `degraded['rlhf_pipeline']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t05.continual.continual_learning@1
      if unavailable: use the in-file conservative substitute for
      `continual_learning` (documented, slower, lower quality) and set
      `degraded['continual_learning']='local'`

  cap.t06.expert.expert_choice_routing@1
      if unavailable: use the in-file conservative substitute for
      `expert_choice_routing` (documented, slower, lower quality) and set
      `degraded['expert_choice_routing']='local'`

  cap.t10.meta.meta_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `meta_reasoning` (documented, slower, lower quality) and set
      `degraded['meta_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - multi-objective reward modelling (correctness, helpfulness, safe
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - adversarial robustness testing against reward hacking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - calibration and disagreement-aware ensembling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured correlation with expert human judgment
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.reward.reward_model@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0823_reward_model.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0824-constitutional-training

**P0824 · `constitutional_training` — Constitutional & Principle-Based Training** · [spec](PART_SPECS_T17.md#p0824-constitutional-training) · [self-contained txt](../prompts/P0824_constitutional_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0824  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0824 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0824  (24/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Constitutional & Principle-Based Training
file         : parts/t17_training/P0824_constitutional_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.constitutional_training
language     : Python 3.13
capability   : cap.t17.constitutional.constitutional_training@1
determinism  : io
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Trains behaviour from stated principles, auditably.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. principle set with operationalisation into training signals
  2. self-critique and revision training loops
  3. principle-adherence measurement per principle
  4. target: measurably better constitution adherence than Opus 5's audit score

Expanded obligations:
  1. Implement principle set with operationalisation into training signals as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement self-critique and revision training loops, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement principle-adherence measurement per principle with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement target: measurably better constitution adherence than Opus 5's
     audit score together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of ARC-AGI-3, so
     its p99 latency assertion is part of the acceptance criteria, not an
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.constitutional.constitutional_training@1
  cap.t17.constitutional.constitutional_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.reward.reward_model@1
      if unavailable: use the in-file conservative substitute for
      `reward_model` (documented, slower, lower quality) and set
      `degraded['reward_model']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t05.depth.depth_width_tradeoff@1
      if unavailable: use the in-file conservative substitute for
      `depth_width_tradeoff` (documented, slower, lower quality) and set
      `degraded['depth_width_tradeoff']='local'`

  cap.t06.difficulty.difficulty_routing@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_routing` (documented, slower, lower quality) and set
      `degraded['difficulty_routing']='local'`

  cap.t10.hypothesis.hypothesis_management@1
      if unavailable: use the in-file conservative substitute for
      `hypothesis_management` (documented, slower, lower quality) and set
      `degraded['hypothesis_management']='local'`

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
   3. [ 600 lines] Core implementation A - principle set with operationalisation into training signals
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - self-critique and revision training loops
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - principle-adherence measurement per principle
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: measurably better constitution adherence than Opus 5's a
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.constitutional.constitutional_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0824_constitutional_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0825-process-supervision-training

**P0825 · `process_supervision_training` — Process Supervision Training** · [spec](PART_SPECS_T17.md#p0825-process-supervision-training) · [self-contained txt](../prompts/P0825_process_supervision_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0825  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0825 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0825  (25/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Process Supervision Training
file         : parts/t17_training/P0825_process_supervision_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.process_supervision_training
language     : Python 3.13
capability   : cap.t17.process.process_supervision_training@1
determinism  : io
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Rewards good reasoning, not just lucky answers.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. step-level label generation at scale with automatic verification
  2. process reward model training and calibration
  3. reasoning-quality improvement measurement independent of final accuracy
  4. measured reduction in right-answer-wrong-reasoning cases

Expanded obligations:
  1. Implement step-level label generation at scale with automatic
     verification, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     ARC-AGI-3 — a regression on that benchmark is an automatic rejection of
     this part.
  2. Implement process reward model training and calibration with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement reasoning-quality improvement measurement independent of final
     accuracy together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of ARC-AGI-3, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement measured reduction in right-answer-wrong-reasoning cases as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
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
  cap.t17.process.process_supervision_training@1
  cap.t17.process.process_supervision_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.constitutional.constitutional_training@1
      if unavailable: use the in-file conservative substitute for
      `constitutional_training` (documented, slower, lower quality) and set
      `degraded['constitutional_training']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t05.sparse.sparse_upcycling@1
      if unavailable: use the in-file conservative substitute for
      `sparse_upcycling` (documented, slower, lower quality) and set
      `degraded['sparse_upcycling']='local'`

  cap.t06.moe.moe_memory_budget@1
      if unavailable: use the in-file conservative substitute for
      `moe_memory_budget` (documented, slower, lower quality) and set
      `degraded['moe_memory_budget']='local'`

  cap.t10.proof.proof_sketch@1
      if unavailable: use the in-file conservative substitute for
      `proof_sketch` (documented, slower, lower quality) and set
      `degraded['proof_sketch']='local'`

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
   3. [ 600 lines] Core implementation A - step-level label generation at scale with automatic verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - process reward model training and calibration
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reasoning-quality improvement measurement independent of final a
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured reduction in right-answer-wrong-reasoning cases
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.process.process_supervision_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0825_process_supervision_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0826-self-play-training

**P0826 · `self_play_training` — Self-Play & Adversarial Curriculum** · [spec](PART_SPECS_T17.md#p0826-self-play-training) · [self-contained txt](../prompts/P0826_self_play_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0826  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0826 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0826  (26/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Self-Play & Adversarial Curriculum
file         : parts/t17_training/P0826_self_play_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.self_play_training
language     : Python 3.13
capability   : cap.t17.self.self_play_training@1
determinism  : io
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The model generates its own increasingly hard curriculum.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. proposer/solver self-play with difficulty auto-calibration
  2. adversarial example generation targeting current weaknesses
  3. curriculum-progress measurement and plateau detection
  4. measured capability gain per self-play generation

Expanded obligations:
  1. Implement proposer/solver self-play with difficulty auto-calibration
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement adversarial example generation targeting current weaknesses
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement curriculum-progress measurement and plateau detection as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured capability gain per self-play generation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.self.self_play_training@1
  cap.t17.self.self_play_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.process.process_supervision_training@1
      if unavailable: use the in-file conservative substitute for
      `process_supervision_training` (documented, slower, lower quality) and
      set `degraded['process_supervision_training']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t05.model.model_config_schema@1
      if unavailable: use the in-file conservative substitute for
      `model_config_schema` (documented, slower, lower quality) and set
      `degraded['model_config_schema']='local'`

  cap.t06.moe.moe_visualisation@1
      if unavailable: use the in-file conservative substitute for
      `moe_visualisation` (documented, slower, lower quality) and set
      `degraded['moe_visualisation']='local'`

  cap.t10.adversarial.adversarial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `adversarial_reasoning` (documented, slower, lower quality) and set
      `degraded['adversarial_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - proposer/solver self-play with difficulty auto-calibration
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - adversarial example generation targeting current weaknesses
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - curriculum-progress measurement and plateau detection
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured capability gain per self-play generation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.self.self_play_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0826_self_play_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0827-distillation-training

**P0827 · `distillation_training` — Distillation Training Pipeline** · [spec](PART_SPECS_T17.md#p0827-distillation-training) · [self-contained txt](../prompts/P0827_distillation_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0827  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0827 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0827  (27/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Distillation Training Pipeline
file         : parts/t17_training/P0827_distillation_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.distillation_training
language     : Python 3.13
capability   : cap.t17.distillation.distillation_training@1
determinism  : io
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Compresses the frontier into the fast paths (enables S1 and S4).

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. teacher-trace generation including search and verification behaviour
  2. student training with capability-retention targets per tier
  3. acceptance-rate optimisation for cascade drafters
  4. measured quality retention and speedup contribution

Expanded obligations:
  1. Implement teacher-trace generation including search and verification
     behaviour together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of ARC-AGI-3, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement student training with capability-retention targets per tier as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement acceptance-rate optimisation for cascade drafters, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured quality retention and speedup contribution with an
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.distillation.distillation_training@1
  cap.t17.distillation.distillation_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.self.self_play_training@1
      if unavailable: use the in-file conservative substitute for
      `self_play_training` (documented, slower, lower quality) and set
      `degraded['self_play_training']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t05.attention.attention_variants@1
      if unavailable: use the in-file conservative substitute for
      `attention_variants` (documented, slower, lower quality) and set
      `degraded['attention_variants']='local'`

  cap.t06.router.router_capacity@1
      if unavailable: use the in-file conservative substitute for
      `router_capacity` (documented, slower, lower quality) and set
      `degraded['router_capacity']='local'`

  cap.t10.tree.tree_search@1
      if unavailable: use the in-file conservative substitute for
      `tree_search` (documented, slower, lower quality) and set
      `degraded['tree_search']='local'`

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
   3. [ 600 lines] Core implementation A - teacher-trace generation including search and verification behav
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - student training with capability-retention targets per tier
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - acceptance-rate optimisation for cascade drafters
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured quality retention and speedup contribution
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.distillation.distillation_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0827_distillation_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0828-quantisation-training

**P0828 · `quantisation_training` — Quantisation-Aware Training** · [spec](PART_SPECS_T17.md#p0828-quantisation-training) · [self-contained txt](../prompts/P0828_quantisation_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0828  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0828 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0828  (28/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Quantisation-Aware Training
file         : parts/t17_training/P0828_quantisation_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.quantisation_training
language     : Python 3.13
capability   : cap.t17.quantisation.quantisation_training@1
determinism  : io
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Makes low precision free instead of costly.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. QAT with learned scales and outlier handling
  2. per-layer precision-plan co-training
  3. accuracy-parity verification against full precision
  4. measured inference cost reduction at matched quality

Expanded obligations:
  1. Implement QAT with learned scales and outlier handling as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Frontier-Bench
     v0.1 — a regression on that benchmark is an automatic rejection of this
     part.
  2. Implement per-layer precision-plan co-training, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement accuracy-parity verification against full precision with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured inference cost reduction at matched quality together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
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
  cap.t17.quantisation.quantisation_training@1
  cap.t17.quantisation.quantisation_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.distillation.distillation_training@1
      if unavailable: use the in-file conservative substitute for
      `distillation_training` (documented, slower, lower quality) and set
      `degraded['distillation_training']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t05.activation.activation_design@1
      if unavailable: use the in-file conservative substitute for
      `activation_design` (documented, slower, lower quality) and set
      `degraded['activation_design']='local'`

  cap.t06.expert.expert_prefetch@1
      if unavailable: use the in-file conservative substitute for
      `expert_prefetch` (documented, slower, lower quality) and set
      `degraded['expert_prefetch']='local'`

  cap.t10.debate.debate_ensemble@1
      if unavailable: use the in-file conservative substitute for
      `debate_ensemble` (documented, slower, lower quality) and set
      `degraded['debate_ensemble']='local'`

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
   3. [ 600 lines] Core implementation A - QAT with learned scales and outlier handling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - per-layer precision-plan co-training
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accuracy-parity verification against full precision
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured inference cost reduction at matched quality
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.quantisation.quantisation_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0828_quantisation_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0829-long-context-training

**P0829 · `long_context_training` — Long Context Training Curriculum** · [spec](PART_SPECS_T17.md#p0829-long-context-training) · [self-contained txt](../prompts/P0829_long_context_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0829  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0829 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0829  (29/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Long Context Training Curriculum
file         : parts/t17_training/P0829_long_context_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.long_context_training
language     : Python 3.13
capability   : cap.t17.long.long_context_training@1
determinism  : io
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Trains genuine 1M+ token competence, not just capacity.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. progressive length curriculum with position-scaling adaptation
  2. long-range dependency task construction for training signal
  3. recall and reasoning evaluation across context positions
  4. measured elimination of lost-in-the-middle degradation

Expanded obligations:
  1. Implement progressive length curriculum with position-scaling
     adaptation, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement long-range dependency task construction for training signal
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement recall and reasoning evaluation across context positions
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured elimination of lost-in-the-middle degradation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
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
                       p99 <= 33000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.long.long_context_training@1
  cap.t17.long.long_context_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.quantisation.quantisation_training@1
      if unavailable: use the in-file conservative substitute for
      `quantisation_training` (documented, slower, lower quality) and set
      `degraded['quantisation_training']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t05.draft.draft_model_arch@1
      if unavailable: use the in-file conservative substitute for
      `draft_model_arch` (documented, slower, lower quality) and set
      `degraded['draft_model_arch']='local'`

  cap.t06.moe.moe_quantisation@1
      if unavailable: use the in-file conservative substitute for
      `moe_quantisation` (documented, slower, lower quality) and set
      `degraded['moe_quantisation']='local'`

  cap.t10.induction.induction_engine@1
      if unavailable: use the in-file conservative substitute for
      `induction_engine` (documented, slower, lower quality) and set
      `degraded['induction_engine']='local'`

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
   3. [ 600 lines] Core implementation A - progressive length curriculum with position-scaling adaptation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - long-range dependency task construction for training signal
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - recall and reasoning evaluation across context positions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured elimination of lost-in-the-middle degradation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.long.long_context_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0829_long_context_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0830-multimodal-training

**P0830 · `multimodal_training` — Multimodal Training Pipeline** · [spec](PART_SPECS_T17.md#p0830-multimodal-training) · [self-contained txt](../prompts/P0830_multimodal_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0830  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0830 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0830  (30/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Multimodal Training Pipeline
file         : parts/t17_training/P0830_multimodal_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.multimodal_training
language     : Python 3.13
capability   : cap.t17.multimodal.multimodal_training@1
determinism  : io
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Trains all senses jointly without any modality suffering.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. modality-balanced batching and loss weighting
  2. cross-modal alignment objectives with measured transfer
  3. modality-specific data curation and quality control
  4. per-modality capability measurement across training

Expanded obligations:
  1. Implement modality-balanced batching and loss weighting with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Frontier-Bench v0.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement cross-modal alignment objectives with measured transfer
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement modality-specific data curation and quality control as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement per-modality capability measurement across training, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of ARC-AGI-3, so its p99
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.multimodal.multimodal_training@1
  cap.t17.multimodal.multimodal_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.long.long_context_training@1
      if unavailable: use the in-file conservative substitute for
      `long_context_training` (documented, slower, lower quality) and set
      `degraded['long_context_training']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t05.meta.meta_learning_arch@1
      if unavailable: use the in-file conservative substitute for
      `meta_learning_arch` (documented, slower, lower quality) and set
      `degraded['meta_learning_arch']='local'`

  cap.t06.gating.gating_alternatives@1
      if unavailable: use the in-file conservative substitute for
      `gating_alternatives` (documented, slower, lower quality) and set
      `degraded['gating_alternatives']='local'`

  cap.t10.commonsense.commonsense_engine@1
      if unavailable: use the in-file conservative substitute for
      `commonsense_engine` (documented, slower, lower quality) and set
      `degraded['commonsense_engine']='local'`

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
   3. [ 600 lines] Core implementation A - modality-balanced batching and loss weighting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cross-modal alignment objectives with measured transfer
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - modality-specific data curation and quality control
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - per-modality capability measurement across training
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.multimodal.multimodal_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0830_multimodal_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0831-agentic-training

**P0831 · `agentic_training` — Agentic & Tool-Use Training** · [spec](PART_SPECS_T17.md#p0831-agentic-training) · [self-contained txt](../prompts/P0831_agentic_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0831  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0831 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0831  (31/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Agentic & Tool-Use Training
file         : parts/t17_training/P0831_agentic_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.agentic_training
language     : Python 3.13
capability   : cap.t17.agentic.agentic_training@1
determinism  : io
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Trains long-horizon autonomy in real environments.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. environment-based trajectory collection at scale
  2. outcome-based reward with process shaping for long horizons
  3. tool-use competence training across thousands of tools
  4. measured agent-benchmark improvement per training phase

Expanded obligations:
  1. Implement environment-based trajectory collection at scale together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement outcome-based reward with process shaping for long horizons as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement tool-use competence training across thousands of tools, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured agent-benchmark improvement per training phase with
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.agentic.agentic_training@1
  cap.t17.agentic.agentic_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.multimodal.multimodal_training@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_training` (documented, slower, lower quality) and set
      `degraded['multimodal_training']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t05.architecture.architecture_search@1
      if unavailable: use the in-file conservative substitute for
      `architecture_search` (documented, slower, lower quality) and set
      `degraded['architecture_search']='local'`

  cap.t06.modality.modality_routing@1
      if unavailable: use the in-file conservative substitute for
      `modality_routing` (documented, slower, lower quality) and set
      `degraded['modality_routing']='local'`

  cap.t10.parallel.parallel_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `parallel_reasoning` (documented, slower, lower quality) and set
      `degraded['parallel_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - environment-based trajectory collection at scale
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - outcome-based reward with process shaping for long horizons
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - tool-use competence training across thousands of tools
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured agent-benchmark improvement per training phase
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.agentic.agentic_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0831_agentic_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0832-safety-training

**P0832 · `safety_training` — Safety & Refusal Training** · [spec](PART_SPECS_T17.md#p0832-safety-training) · [self-contained txt](../prompts/P0832_safety_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0832  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0832 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0832  (32/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Safety & Refusal Training
file         : parts/t17_training/P0832_safety_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.safety_training
language     : Python 3.13
capability   : cap.t17.safety.safety_training@1
determinism  : io
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Trains judgment, not keyword blocking.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. harm-taxonomy-aligned training data with borderline cases
  2. over-refusal prevention with dual-use legitimate-use training
  3. jailbreak robustness training against evolving attacks
  4. measured safety/helpfulness Pareto improvement over Opus 5

Expanded obligations:
  1. Implement harm-taxonomy-aligned training data with borderline cases as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement over-refusal prevention with dual-use legitimate-use training,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement jailbreak robustness training against evolving attacks with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured safety/helpfulness Pareto improvement over Opus 5
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.safety.safety_training@1
  cap.t17.safety.safety_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.agentic.agentic_training@1
      if unavailable: use the in-file conservative substitute for
      `agentic_training` (documented, slower, lower quality) and set
      `degraded['agentic_training']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t05.speculative.speculative_arch_hooks@1
      if unavailable: use the in-file conservative substitute for
      `speculative_arch_hooks` (documented, slower, lower quality) and set
      `degraded['speculative_arch_hooks']='local'`

  cap.t06.routing.routing_fairness@1
      if unavailable: use the in-file conservative substitute for
      `routing_fairness` (documented, slower, lower quality) and set
      `degraded['routing_fairness']='local'`

  cap.t10.multi.multi_step_arithmetic@1
      if unavailable: use the in-file conservative substitute for
      `multi_step_arithmetic` (documented, slower, lower quality) and set
      `degraded['multi_step_arithmetic']='local'`

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
   3. [ 600 lines] Core implementation A - harm-taxonomy-aligned training data with borderline cases
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - over-refusal prevention with dual-use legitimate-use training
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - jailbreak robustness training against evolving attacks
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured safety/helpfulness Pareto improvement over Opus 5
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.safety.safety_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0832_safety_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0833-honesty-training

**P0833 · `honesty_training` — Honesty & Calibration Training** · [spec](PART_SPECS_T17.md#p0833-honesty-training) · [self-contained txt](../prompts/P0833_honesty_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0833  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0833 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0833  (33/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Honesty & Calibration Training
file         : parts/t17_training/P0833_honesty_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.honesty_training
language     : Python 3.13
capability   : cap.t17.honesty.honesty_training@1
determinism  : io
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Trains the model to know and say what it does not know.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. calibration training with abstention rewards
  2. sycophancy and false-agreement suppression training
  3. faithful-reasoning training via causal-intervention signals
  4. measured calibration and honesty metric improvements

Expanded obligations:
  1. Implement calibration training with abstention rewards, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement sycophancy and false-agreement suppression training with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement faithful-reasoning training via causal-intervention signals
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured calibration and honesty metric improvements as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
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
  cap.t17.honesty.honesty_training@1
  cap.t17.honesty.honesty_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.safety.safety_training@1
      if unavailable: use the in-file conservative substitute for
      `safety_training` (documented, slower, lower quality) and set
      `degraded['safety_training']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t05.expert.expert_specialisation@1
      if unavailable: use the in-file conservative substitute for
      `expert_specialisation` (documented, slower, lower quality) and set
      `degraded['expert_specialisation']='local'`

  cap.t06.router.router_bench@1
      if unavailable: use the in-file conservative substitute for
      `router_bench` (documented, slower, lower quality) and set
      `degraded['router_bench']='local'`

  cap.t10.error.error_taxonomy@1
      if unavailable: use the in-file conservative substitute for
      `error_taxonomy` (documented, slower, lower quality) and set
      `degraded['error_taxonomy']='local'`

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
   3. [ 600 lines] Core implementation A - calibration training with abstention rewards
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - sycophancy and false-agreement suppression training
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - faithful-reasoning training via causal-intervention signals
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured calibration and honesty metric improvements
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.honesty.honesty_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0833_honesty_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0834-continual-pretraining

**P0834 · `continual_pretraining` — Continual Pretraining & Knowledge Refresh** · [spec](PART_SPECS_T17.md#p0834-continual-pretraining) · [self-contained txt](../prompts/P0834_continual_pretraining.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0834  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0834 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0834  (34/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Continual Pretraining & Knowledge Refresh
file         : parts/t17_training/P0834_continual_pretraining.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.continual_pretraining
language     : Python 3.13
capability   : cap.t17.continual.continual_pretraining@1
determinism  : io
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Stays current without forgetting or destabilising.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. knowledge-refresh data pipeline with recency weighting
  2. catastrophic-forgetting prevention with measured retention
  3. stability of established capabilities across refreshes
  4. measured freshness improvement with retained capability

Expanded obligations:
  1. Implement knowledge-refresh data pipeline with recency weighting with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  2. Implement catastrophic-forgetting prevention with measured retention
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement stability of established capabilities across refreshes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement measured freshness improvement with retained capability, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.continual.continual_pretraining@1
  cap.t17.continual.continual_pretraining.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.honesty.honesty_training@1
      if unavailable: use the in-file conservative substitute for
      `honesty_training` (documented, slower, lower quality) and set
      `degraded['honesty_training']='local'`

  cap.t05.hybrid.hybrid_mixer@1
      if unavailable: use the in-file conservative substitute for
      `hybrid_mixer` (documented, slower, lower quality) and set
      `degraded['hybrid_mixer']='local'`

  cap.t06.router.router_balance@1
      if unavailable: use the in-file conservative substitute for
      `router_balance` (documented, slower, lower quality) and set
      `degraded['router_balance']='local'`

  cap.t10.search.search_controller@1
      if unavailable: use the in-file conservative substitute for
      `search_controller` (documented, slower, lower quality) and set
      `degraded['search_controller']='local'`

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
   3. [ 600 lines] Core implementation A - knowledge-refresh data pipeline with recency weighting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - catastrophic-forgetting prevention with measured retention
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - stability of established capabilities across refreshes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured freshness improvement with retained capability
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.continual.continual_pretraining@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0834_continual_pretraining.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0835-hyperparameter-search

**P0835 · `hyperparameter_search` — Hyperparameter Optimisation at Scale** · [spec](PART_SPECS_T17.md#p0835-hyperparameter-search) · [self-contained txt](../prompts/P0835_hyperparameter_search.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0835  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0835 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0835  (35/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Hyperparameter Optimisation at Scale
file         : parts/t17_training/P0835_hyperparameter_search.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.hyperparameter_search
language     : Python 3.13
capability   : cap.t17.hyperparameter.hyperparameter_search@1
determinism  : io
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Finds the right settings without wasting a full run.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. small-scale proxy experiments with validated extrapolation
  2. multi-fidelity search with early stopping
  3. transfer of found settings across scale and architecture changes
  4. measured savings versus naive search

Expanded obligations:
  1. Implement small-scale proxy experiments with validated extrapolation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement multi-fidelity search with early stopping as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
     Frontier-Bench v0.1, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement transfer of found settings across scale and architecture
     changes, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
     — a regression on that benchmark is an automatic rejection of this part.
  4. Implement measured savings versus naive search with an explicit
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.hyperparameter.hyperparameter_search@1
  cap.t17.hyperparameter.hyperparameter_search.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.continual.continual_pretraining@1
      if unavailable: use the in-file conservative substitute for
      `continual_pretraining` (documented, slower, lower quality) and set
      `degraded['continual_pretraining']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t05.normalisation.normalisation_design@1
      if unavailable: use the in-file conservative substitute for
      `normalisation_design` (documented, slower, lower quality) and set
      `degraded['normalisation_design']='local'`

  cap.t06.expert.expert_placement@1
      if unavailable: use the in-file conservative substitute for
      `expert_placement` (documented, slower, lower quality) and set
      `degraded['expert_placement']='local'`

  cap.t10.self.self_critique@1
      if unavailable: use the in-file conservative substitute for
      `self_critique` (documented, slower, lower quality) and set
      `degraded['self_critique']='local'`

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
   3. [ 600 lines] Core implementation A - small-scale proxy experiments with validated extrapolation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - multi-fidelity search with early stopping
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - transfer of found settings across scale and architecture changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured savings versus naive search
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.hyperparameter.hyperparameter_search@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0835_hyperparameter_search.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0836-experiment-tracking

**P0836 · `experiment_tracking` — Experiment Management & Provenance** · [spec](PART_SPECS_T17.md#p0836-experiment-tracking) · [self-contained txt](../prompts/P0836_experiment_tracking.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0836  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0836 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0836  (36/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Experiment Management & Provenance
file         : parts/t17_training/P0836_experiment_tracking.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.experiment_tracking
language     : Python 3.13
capability   : cap.t17.experiment.experiment_tracking@1
determinism  : io
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Thousands of experiments, all reproducible.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. experiment metadata, code, data and config versioning
  2. result database with statistical comparison tooling
  3. reproducibility verification by re-running sampled experiments
  4. provenance completeness audit

Expanded obligations:
  1. Implement experiment metadata, code, data and config versioning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement result database with statistical comparison tooling, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement reproducibility verification by re-running sampled experiments
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement provenance completeness audit together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. This mechanism sits on the critical
     path of ARC-AGI-3, so its p99 latency assertion is part of the
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.experiment.experiment_tracking@1
  cap.t17.experiment.experiment_tracking.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.hyperparameter.hyperparameter_search@1
      if unavailable: use the in-file conservative substitute for
      `hyperparameter_search` (documented, slower, lower quality) and set
      `degraded['hyperparameter_search']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t05.multi.multi_token_prediction@1
      if unavailable: use the in-file conservative substitute for
      `multi_token_prediction` (documented, slower, lower quality) and set
      `degraded['multi_token_prediction']='local'`

  cap.t06.sparse.sparse_activation_stats@1
      if unavailable: use the in-file conservative substitute for
      `sparse_activation_stats` (documented, slower, lower quality) and set
      `degraded['sparse_activation_stats']='local'`

  cap.t10.abstraction.abstraction_engine@1
      if unavailable: use the in-file conservative substitute for
      `abstraction_engine` (documented, slower, lower quality) and set
      `degraded['abstraction_engine']='local'`

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
   3. [ 600 lines] Core implementation A - experiment metadata, code, data and config versioning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - result database with statistical comparison tooling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reproducibility verification by re-running sampled experiments
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - provenance completeness audit
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.experiment.experiment_tracking@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0836_experiment_tracking.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0837-ablation-framework

**P0837 · `ablation_framework` — Systematic Ablation Framework** · [spec](PART_SPECS_T17.md#p0837-ablation-framework) · [self-contained txt](../prompts/P0837_ablation_framework.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0837  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0837 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0837  (37/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Systematic Ablation Framework
file         : parts/t17_training/P0837_ablation_framework.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.ablation_framework
language     : Python 3.13
capability   : cap.t17.ablation.ablation_framework@1
determinism  : io
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Every claimed improvement isolated and proven.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. automated ablation-matrix execution with matched compute
  2. variance estimation and significance testing
  3. interaction-effect detection between changes
  4. ablation-report generation for every major decision

Expanded obligations:
  1. Implement automated ablation-matrix execution with matched compute, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement variance estimation and significance testing with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Frontier-Bench v0.1 target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement interaction-effect detection between changes together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of ARC-AGI-3, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement ablation-report generation for every major decision as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
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
  cap.t17.ablation.ablation_framework@1
  cap.t17.ablation.ablation_framework.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.experiment.experiment_tracking@1
      if unavailable: use the in-file conservative substitute for
      `experiment_tracking` (documented, slower, lower quality) and set
      `degraded['experiment_tracking']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t05.program.program_induction_arch@1
      if unavailable: use the in-file conservative substitute for
      `program_induction_arch` (documented, slower, lower quality) and set
      `degraded['program_induction_arch']='local'`

  cap.t06.router.router_robustness@1
      if unavailable: use the in-file conservative substitute for
      `router_robustness` (documented, slower, lower quality) and set
      `degraded['router_robustness']='local'`

  cap.t10.spatial.spatial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `spatial_reasoning` (documented, slower, lower quality) and set
      `degraded['spatial_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - automated ablation-matrix execution with matched compute
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - variance estimation and significance testing
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - interaction-effect detection between changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - ablation-report generation for every major decision
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.ablation.ablation_framework@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0837_ablation_framework.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0838-scaling-prediction

**P0838 · `scaling_prediction` — Scaling Prediction & Run Planning** · [spec](PART_SPECS_T17.md#p0838-scaling-prediction) · [self-contained txt](../prompts/P0838_scaling_prediction.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0838  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0838 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0838  (38/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Scaling Prediction & Run Planning
file         : parts/t17_training/P0838_scaling_prediction.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.scaling_prediction
language     : Python 3.13
capability   : cap.t17.scaling.scaling_prediction@1
determinism  : io
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Knows what a run will produce before spending on it.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. scaling-law fitting with uncertainty for each capability
  2. compute-allocation planning across model, data and RL phases
  3. prediction-accuracy tracking against realised runs
  4. measured planning accuracy improvement over time

Expanded obligations:
  1. Implement scaling-law fitting with uncertainty for each capability with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement compute-allocation planning across model, data and RL phases
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement prediction-accuracy tracking against realised runs as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured planning accuracy improvement over time, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.scaling.scaling_prediction@1
  cap.t17.scaling.scaling_prediction.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.ablation.ablation_framework@1
      if unavailable: use the in-file conservative substitute for
      `ablation_framework` (documented, slower, lower quality) and set
      `degraded['ablation_framework']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t05.init.init_scaling_laws@1
      if unavailable: use the in-file conservative substitute for
      `init_scaling_laws` (documented, slower, lower quality) and set
      `degraded['init_scaling_laws']='local'`

  cap.t06.sparse.sparse_kernels_bridge@1
      if unavailable: use the in-file conservative substitute for
      `sparse_kernels_bridge` (documented, slower, lower quality) and set
      `degraded['sparse_kernels_bridge']='local'`

  cap.t10.chain.chain_compression@1
      if unavailable: use the in-file conservative substitute for
      `chain_compression` (documented, slower, lower quality) and set
      `degraded['chain_compression']='local'`

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
   3. [ 600 lines] Core implementation A - scaling-law fitting with uncertainty for each capability
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - compute-allocation planning across model, data and RL phases
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - prediction-accuracy tracking against realised runs
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured planning accuracy improvement over time
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.scaling.scaling_prediction@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0838_scaling_prediction.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0839-self-improvement-loop

**P0839 · `self_improvement_loop` — Recursive Self-Improvement Loop** · [spec](PART_SPECS_T17.md#p0839-self-improvement-loop) · [self-contained txt](../prompts/P0839_self_improvement_loop.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0839  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0839 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0839  (39/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Recursive Self-Improvement Loop
file         : parts/t17_training/P0839_self_improvement_loop.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.self_improvement_loop
language     : Python 3.13
capability   : cap.t17.self.self_improvement_loop@1
determinism  : io
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The system improves itself, measurably and safely.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. gap identification from benchmark and production failure analysis
  2. automated improvement-hypothesis generation and experiment execution
  3. human-approval gates before any weight-affecting change
  4. measured improvement rate per cycle with safety verification

Expanded obligations:
  1. Implement gap identification from benchmark and production failure
     analysis together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of ARC-AGI-3, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement automated improvement-hypothesis generation and experiment
     execution as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement human-approval gates before any weight-affecting change, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement measured improvement rate per cycle with safety verification
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.self.self_improvement_loop@1
  cap.t17.self.self_improvement_loop.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.scaling.scaling_prediction@1
      if unavailable: use the in-file conservative substitute for
      `scaling_prediction` (documented, slower, lower quality) and set
      `degraded['scaling_prediction']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t05.memory.memory_attention_bridge@1
      if unavailable: use the in-file conservative substitute for
      `memory_attention_bridge` (documented, slower, lower quality) and set
      `degraded['memory_attention_bridge']='local'`

  cap.t06.expert.expert_warmup@1
      if unavailable: use the in-file conservative substitute for
      `expert_warmup` (documented, slower, lower quality) and set
      `degraded['expert_warmup']='local'`

  cap.t10.reasoning.reasoning_robustness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_robustness` (documented, slower, lower quality) and set
      `degraded['reasoning_robustness']='local'`

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
   3. [ 600 lines] Core implementation A - gap identification from benchmark and production failure analysi
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automated improvement-hypothesis generation and experiment execu
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - human-approval gates before any weight-affecting change
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured improvement rate per cycle with safety verification
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.self.self_improvement_loop@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0839_self_improvement_loop.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0840-automated-research

**P0840 · `automated_research` — Automated ML Research Agent** · [spec](PART_SPECS_T17.md#p0840-automated-research) · [self-contained txt](../prompts/P0840_automated_research.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0840  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0840 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0840  (40/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Automated ML Research Agent
file         : parts/t17_training/P0840_automated_research.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.automated_research
language     : Python 3.13
capability   : cap.t17.automated.automated_research@1
determinism  : io
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Uses the system's own agent capability to advance itself.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. literature synthesis and idea generation with novelty checking
  2. experiment implementation, execution and honest analysis
  3. negative-result reporting and hypothesis retirement
  4. measured research-throughput and hit-rate

Expanded obligations:
  1. Implement literature synthesis and idea generation with novelty checking
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against Frontier-Bench v0.1 — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement experiment implementation, execution and honest analysis, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement negative-result reporting and hypothesis retirement with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Frontier-Bench v0.1, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured research-throughput and hit-rate together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
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
  cap.t17.automated.automated_research@1
  cap.t17.automated.automated_research.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.self.self_improvement_loop@1
      if unavailable: use the in-file conservative substitute for
      `self_improvement_loop` (documented, slower, lower quality) and set
      `degraded['self_improvement_loop']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t05.thought.thought_representation@1
      if unavailable: use the in-file conservative substitute for
      `thought_representation` (documented, slower, lower quality) and set
      `degraded['thought_representation']='local'`

  cap.t06.hierarchical.hierarchical_routing@1
      if unavailable: use the in-file conservative substitute for
      `hierarchical_routing` (documented, slower, lower quality) and set
      `degraded['hierarchical_routing']='local'`

  cap.t10.reasoning.reasoning_transfer@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_transfer` (documented, slower, lower quality) and set
      `degraded['reasoning_transfer']='local'`

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
   3. [ 600 lines] Core implementation A - literature synthesis and idea generation with novelty checking
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - experiment implementation, execution and honest analysis
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - negative-result reporting and hypothesis retirement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured research-throughput and hit-rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.automated.automated_research@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0840_automated_research.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0841-capability-gap-analysis

**P0841 · `capability_gap_analysis` — Capability Gap Analysis & Prioritisation** · [spec](PART_SPECS_T17.md#p0841-capability-gap-analysis) · [self-contained txt](../prompts/P0841_capability_gap_analysis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0841  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0841 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0841  (41/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Capability Gap Analysis & Prioritisation
file         : parts/t17_training/P0841_capability_gap_analysis.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.capability_gap_analysis
language     : Python 3.13
capability   : cap.t17.capability.capability_gap_analysis@1
determinism  : io
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Always knows the single highest-value thing to improve.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. benchmark and production failure taxonomy with volume weighting
  2. gap-to-target quantification per capability
  3. prioritised improvement roadmap with projected impact
  4. prediction accuracy of projected impact versus realised

Expanded obligations:
  1. Implement benchmark and production failure taxonomy with volume
     weighting, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement gap-to-target quantification per capability with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Frontier-Bench v0.1, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement prioritised improvement roadmap with projected impact together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement prediction accuracy of projected impact versus realised as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.capability.capability_gap_analysis@1
  cap.t17.capability.capability_gap_analysis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.automated.automated_research@1
      if unavailable: use the in-file conservative substitute for
      `automated_research` (documented, slower, lower quality) and set
      `degraded['automated_research']='local'`

  cap.t05.omega.omega_block@1
      if unavailable: use the in-file conservative substitute for
      `omega_block` (documented, slower, lower quality) and set
      `degraded['omega_block']='local'`

  cap.t06.router.router_core@1
      if unavailable: use the in-file conservative substitute for
      `router_core` (documented, slower, lower quality) and set
      `degraded['router_core']='local'`

  cap.t10.thought.thought_program_ir@1
      if unavailable: use the in-file conservative substitute for
      `thought_program_ir` (documented, slower, lower quality) and set
      `degraded['thought_program_ir']='local'`

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
   3. [ 600 lines] Core implementation A - benchmark and production failure taxonomy with volume weighting
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - gap-to-target quantification per capability
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - prioritised improvement roadmap with projected impact
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - prediction accuracy of projected impact versus realised
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.capability.capability_gap_analysis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0841_capability_gap_analysis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0842-training-data-governance

**P0842 · `training_data_governance` — Data Governance, Consent & Deletion** · [spec](PART_SPECS_T17.md#p0842-training-data-governance) · [self-contained txt](../prompts/P0842_training_data_governance.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0842  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0842 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0842  (42/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Data Governance, Consent & Deletion
file         : parts/t17_training/P0842_training_data_governance.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_data_governance
language     : Python 3.13
capability   : cap.t17.training.training_data_governance@1
determinism  : io
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Respects data rights throughout the model lifecycle.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. consent and opt-out tracking through to training influence
  2. deletion-request handling including influence-removal strategy
  3. regional data-residency and regulatory compliance
  4. auditable governance-compliance report

Expanded obligations:
  1. Implement consent and opt-out tracking through to training influence
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement deletion-request handling including influence-removal strategy
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement regional data-residency and regulatory compliance as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  4. Implement auditable governance-compliance report, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
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
  cap.t17.training.training_data_governance@1
  cap.t17.training.training_data_governance.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.capability.capability_gap_analysis@1
      if unavailable: use the in-file conservative substitute for
      `capability_gap_analysis` (documented, slower, lower quality) and set
      `degraded['capability_gap_analysis']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t05.adaptive.adaptive_depth@1
      if unavailable: use the in-file conservative substitute for
      `adaptive_depth` (documented, slower, lower quality) and set
      `degraded['adaptive_depth']='local'`

  cap.t06.fine.fine_grained_experts@1
      if unavailable: use the in-file conservative substitute for
      `fine_grained_experts` (documented, slower, lower quality) and set
      `degraded['fine_grained_experts']='local'`

  cap.t10.self.self_consistency@1
      if unavailable: use the in-file conservative substitute for
      `self_consistency` (documented, slower, lower quality) and set
      `degraded['self_consistency']='local'`

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
   3. [ 600 lines] Core implementation A - consent and opt-out tracking through to training influence
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deletion-request handling including influence-removal strategy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - regional data-residency and regulatory compliance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - auditable governance-compliance report
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_data_governance@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0842_training_data_governance.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0843-memorisation-analysis

**P0843 · `memorisation_analysis` — Memorisation & Privacy Leakage Analysis** · [spec](PART_SPECS_T17.md#p0843-memorisation-analysis) · [self-contained txt](../prompts/P0843_memorisation_analysis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0843  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0843 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0843  (43/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Memorisation & Privacy Leakage Analysis
file         : parts/t17_training/P0843_memorisation_analysis.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.memorisation_analysis
language     : Python 3.13
capability   : cap.t17.memorisation.memorisation_analysis@1
determinism  : io
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Ensures training data cannot be extracted.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. extraction-attack testing across data types
  2. memorisation measurement and per-example influence estimation
  3. differential-privacy option with utility-cost measurement
  4. measured extraction resistance versus baselines

Expanded obligations:
  1. Implement extraction-attack testing across data types together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against ARC-AGI-3 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement memorisation measurement and per-example influence estimation
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  3. Implement differential-privacy option with utility-cost measurement, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured extraction resistance versus baselines with an
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.memorisation.memorisation_analysis@1
  cap.t17.memorisation.memorisation_analysis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.training.training_data_governance@1
      if unavailable: use the in-file conservative substitute for
      `training_data_governance` (documented, slower, lower quality) and set
      `degraded['training_data_governance']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t05.long.long_context_arch@1
      if unavailable: use the in-file conservative substitute for
      `long_context_arch` (documented, slower, lower quality) and set
      `degraded['long_context_arch']='local'`

  cap.t06.router.router_temperature@1
      if unavailable: use the in-file conservative substitute for
      `router_temperature` (documented, slower, lower quality) and set
      `degraded['router_temperature']='local'`

  cap.t10.analogy.analogy_engine@1
      if unavailable: use the in-file conservative substitute for
      `analogy_engine` (documented, slower, lower quality) and set
      `degraded['analogy_engine']='local'`

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
   3. [ 600 lines] Core implementation A - extraction-attack testing across data types
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - memorisation measurement and per-example influence estimation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - differential-privacy option with utility-cost measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured extraction resistance versus baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.memorisation.memorisation_analysis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0843_memorisation_analysis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0844-training-reproducibility

**P0844 · `training_reproducibility` — Training Reproducibility & Determinism** · [spec](PART_SPECS_T17.md#p0844-training-reproducibility) · [self-contained txt](../prompts/P0844_training_reproducibility.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0844  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0844 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0844  (44/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Reproducibility & Determinism
file         : parts/t17_training/P0844_training_reproducibility.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_reproducibility
language     : Python 3.13
capability   : cap.t17.training.training_reproducibility@1
determinism  : io
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The same run twice produces the same model.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. full nondeterminism-source control (seeds, data order, kernels, collectives)
  2. bit-exact reproduction verification at reduced scale
  3. documented exceptions with quantified variance
  4. reproducibility package for every released model

Expanded obligations:
  1. Implement full nondeterminism-source control (seeds, data order,
     kernels, collectives) as a first-class, fully realised mechanism. No
     stub, no `NotImplementedError`, no configuration flag whose default
     disables it. Its state must be reportable through `describe()` and it
     must be exercised by at least eight in-file tests, including one that
     fails loudly if the mechanism is silently bypassed. Correctness here is
     what makes the tier's Frontier-Bench v0.1 target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement bit-exact reproduction verification at reduced scale, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of ARC-AGI-3, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement documented exceptions with quantified variance with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement reproducibility package for every released model together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's ARC-AGI-3 target reachable; the part therefore ships a
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
  cap.t17.training.training_reproducibility@1
  cap.t17.training.training_reproducibility.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.memorisation.memorisation_analysis@1
      if unavailable: use the in-file conservative substitute for
      `memorisation_analysis` (documented, slower, lower quality) and set
      `degraded['memorisation_analysis']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t05.symbolic.symbolic_bridge@1
      if unavailable: use the in-file conservative substitute for
      `symbolic_bridge` (documented, slower, lower quality) and set
      `degraded['symbolic_bridge']='local'`

  cap.t06.mod.mod_routing@1
      if unavailable: use the in-file conservative substitute for
      `mod_routing` (documented, slower, lower quality) and set
      `degraded['mod_routing']='local'`

  cap.t10.temporal.temporal_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `temporal_reasoning` (documented, slower, lower quality) and set
      `degraded['temporal_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - full nondeterminism-source control (seeds, data order, kernels, 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - bit-exact reproduction verification at reduced scale
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - documented exceptions with quantified variance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - reproducibility package for every released model
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_reproducibility@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0844_training_reproducibility.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0845-model-release-gate

**P0845 · `model_release_gate` — Model Release Gate & Sign-Off** · [spec](PART_SPECS_T17.md#p0845-model-release-gate) · [self-contained txt](../prompts/P0845_model_release_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0845  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0845 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0845  (45/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Model Release Gate & Sign-Off
file         : parts/t17_training/P0845_model_release_gate.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.model_release_gate
language     : Python 3.13
capability   : cap.t17.model.model_release_gate@1
determinism  : io
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Nothing ships without passing every gate.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. release-criteria checklist across capability, safety and efficiency
  2. regression detection against the previous release
  3. sign-off workflow with documented accountability
  4. post-release monitoring plan requirement

Expanded obligations:
  1. Implement release-criteria checklist across capability, safety and
     efficiency, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     ARC-AGI-3, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement regression detection against the previous release with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Frontier-Bench v0.1 — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement sign-off workflow with documented accountability together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's ARC-AGI-3 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement post-release monitoring plan requirement as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.model.model_release_gate@1
  cap.t17.model.model_release_gate.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.training.training_reproducibility@1
      if unavailable: use the in-file conservative substitute for
      `training_reproducibility` (documented, slower, lower quality) and set
      `degraded['training_reproducibility']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t05.weight.weight_sharing@1
      if unavailable: use the in-file conservative substitute for
      `weight_sharing` (documented, slower, lower quality) and set
      `degraded['weight_sharing']='local'`

  cap.t06.expert.expert_dropout@1
      if unavailable: use the in-file conservative substitute for
      `expert_dropout` (documented, slower, lower quality) and set
      `degraded['expert_dropout']='local'`

  cap.t10.reasoning.reasoning_memory@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_memory` (documented, slower, lower quality) and set
      `degraded['reasoning_memory']='local'`

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
   3. [ 600 lines] Core implementation A - release-criteria checklist across capability, safety and efficie
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - regression detection against the previous release
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - sign-off workflow with documented accountability
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - post-release monitoring plan requirement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.model.model_release_gate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0845_model_release_gate.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0846-training-cost-model

**P0846 · `training_cost_model` — Training Cost & Carbon Accounting** · [spec](PART_SPECS_T17.md#p0846-training-cost-model) · [self-contained txt](../prompts/P0846_training_cost_model.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0846  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0846 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0846  (46/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Cost & Carbon Accounting
file         : parts/t17_training/P0846_training_cost_model.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_cost_model
language     : Python 3.13
capability   : cap.t17.training.training_cost_model@1
determinism  : io
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Full transparency on what building this costs.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. compute, energy and carbon accounting per run and per capability gain
  2. cost-efficiency comparison against published frontier runs
  3. forecast accuracy for planned runs
  4. efficiency-improvement tracking over time

Expanded obligations:
  1. Implement compute, energy and carbon accounting per run and per
     capability gain with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Frontier-Bench v0.1
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement cost-efficiency comparison against published frontier runs
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement forecast accuracy for planned runs as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of Frontier-Bench v0.1, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement efficiency-improvement tracking over time, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
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
  cap.t17.training.training_cost_model@1
  cap.t17.training.training_cost_model.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.model.model_release_gate@1
      if unavailable: use the in-file conservative substitute for
      `model_release_gate` (documented, slower, lower quality) and set
      `degraded['model_release_gate']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t05.action.action_head@1
      if unavailable: use the in-file conservative substitute for
      `action_head` (documented, slower, lower quality) and set
      `degraded['action_head']='local'`

  cap.t06.router.router_cache@1
      if unavailable: use the in-file conservative substitute for
      `router_cache` (documented, slower, lower quality) and set
      `degraded['router_cache']='local'`

  cap.t10.reasoning.reasoning_faithfulness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_faithfulness` (documented, slower, lower quality) and set
      `degraded['reasoning_faithfulness']='local'`

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
   3. [ 600 lines] Core implementation A - compute, energy and carbon accounting per run and per capability
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost-efficiency comparison against published frontier runs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - forecast accuracy for planned runs
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - efficiency-improvement tracking over time
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_cost_model@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0846_training_cost_model.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0847-fine-tune-service

**P0847 · `fine_tune_service` — Customer Fine-Tuning Infrastructure** · [spec](PART_SPECS_T17.md#p0847-fine-tune-service) · [self-contained txt](../prompts/P0847_fine_tune_service.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0847  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0847 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0847  (47/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Customer Fine-Tuning Infrastructure
file         : parts/t17_training/P0847_fine_tune_service.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.fine_tune_service
language     : Python 3.13
capability   : cap.t17.fine.fine_tune_service@1
determinism  : io
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Lets others specialise the model safely.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. adapter and full fine-tune pipelines with isolation guarantees
  2. safety-property preservation verification after customer tuning
  3. quality-regression detection and customer reporting
  4. measured customisation quality and safety retention

Expanded obligations:
  1. Implement adapter and full fine-tune pipelines with isolation guarantees
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's ARC-AGI-3 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement safety-property preservation verification after customer
     tuning as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement quality-regression detection and customer reporting, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured customisation quality and safety retention with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.fine.fine_tune_service@1
  cap.t17.fine.fine_tune_service.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.training.training_cost_model@1
      if unavailable: use the in-file conservative substitute for
      `training_cost_model` (documented, slower, lower quality) and set
      `degraded['training_cost_model']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t05.prompt.prompt_representation@1
      if unavailable: use the in-file conservative substitute for
      `prompt_representation` (documented, slower, lower quality) and set
      `degraded['prompt_representation']='local'`

  cap.t06.routing.routing_privacy@1
      if unavailable: use the in-file conservative substitute for
      `routing_privacy` (documented, slower, lower quality) and set
      `degraded['routing_privacy']='local'`

  cap.t10.subgoal.subgoal_caching@1
      if unavailable: use the in-file conservative substitute for
      `subgoal_caching` (documented, slower, lower quality) and set
      `degraded['subgoal_caching']='local'`

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
   3. [ 600 lines] Core implementation A - adapter and full fine-tune pipelines with isolation guarantees
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - safety-property preservation verification after customer tuning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality-regression detection and customer reporting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured customisation quality and safety retention
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.fine.fine_tune_service@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0847_fine_tune_service.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0848-eval-driven-training

**P0848 · `eval_driven_training` — Evaluation-Driven Training Loop** · [spec](PART_SPECS_T17.md#p0848-eval-driven-training) · [self-contained txt](../prompts/P0848_eval_driven_training.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0848  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0848 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0848  (48/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Evaluation-Driven Training Loop
file         : parts/t17_training/P0848_eval_driven_training.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.eval_driven_training
language     : Python 3.13
capability   : cap.t17.eval.eval_driven_training@1
determinism  : io
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Closes the loop between measurement and improvement.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. automatic training-signal generation from evaluation failures
  2. contamination-safe use of evaluation-derived data
  3. improvement verification on sealed held-out sets
  4. measured gain rate with contamination guarantees

Expanded obligations:
  1. Implement automatic training-signal generation from evaluation failures
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of Frontier-Bench v0.1, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement contamination-safe use of evaluation-derived data, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against ARC-AGI-3 — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement improvement verification on sealed held-out sets with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured gain rate with contamination guarantees together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of ARC-AGI-3, so its p99 latency assertion is part of
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.eval.eval_driven_training@1
  cap.t17.eval.eval_driven_training.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.fine.fine_tune_service@1
      if unavailable: use the in-file conservative substitute for
      `fine_tune_service` (documented, slower, lower quality) and set
      `degraded['fine_tune_service']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t05.arch.arch_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `arch_spec_doc` (documented, slower, lower quality) and set
      `degraded['arch_spec_doc']='local'`

  cap.t06.moe.moe_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `moe_spec_doc` (documented, slower, lower quality) and set
      `degraded['moe_spec_doc']='local'`

  cap.t10.reasoning.reasoning_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_spec_doc` (documented, slower, lower quality) and set
      `degraded['reasoning_spec_doc']='local'`

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
   3. [ 600 lines] Core implementation A - automatic training-signal generation from evaluation failures
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - contamination-safe use of evaluation-derived data
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - improvement verification on sealed held-out sets
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured gain rate with contamination guarantees
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.eval.eval_driven_training@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0848_eval_driven_training.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0849-training-bench

**P0849 · `training_bench` — Training Infrastructure Benchmark Suite** · [spec](PART_SPECS_T17.md#p0849-training-bench) · [self-contained txt](../prompts/P0849_training_bench.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0849  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0849 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0849  (49/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Infrastructure Benchmark Suite
file         : parts/t17_training/P0849_training_bench.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_bench
language     : Python 3.13
capability   : cap.t17.training.training_bench@1
determinism  : io
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
Measures the training system itself.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. throughput, utilisation and scaling-efficiency benchmarks
  2. stability and recovery benchmarks under injected faults
  3. comparison against published large-scale training efficiency
  4. regression gates for infrastructure changes

Expanded obligations:
  1. Implement throughput, utilisation and scaling-efficiency benchmarks, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against ARC-AGI-3
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement stability and recovery benchmarks under injected faults with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Frontier-Bench v0.1 target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement comparison against published large-scale training efficiency
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement regression gates for infrastructure changes as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against Frontier-Bench
     v0.1 — a regression on that benchmark is an automatic rejection of this
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.training.training_bench@1
  cap.t17.training.training_bench.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.eval.eval_driven_training@1
      if unavailable: use the in-file conservative substitute for
      `eval_driven_training` (documented, slower, lower quality) and set
      `degraded['eval_driven_training']='local'`

  cap.t05.latent.latent_program_slots@1
      if unavailable: use the in-file conservative substitute for
      `latent_program_slots` (documented, slower, lower quality) and set
      `degraded['latent_program_slots']='local'`

  cap.t06.shared.shared_expert@1
      if unavailable: use the in-file conservative substitute for
      `shared_expert` (documented, slower, lower quality) and set
      `degraded['shared_expert']='local'`

  cap.t10.outcome.outcome_verifier@1
      if unavailable: use the in-file conservative substitute for
      `outcome_verifier` (documented, slower, lower quality) and set
      `degraded['outcome_verifier']='local'`

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
   3. [ 600 lines] Core implementation A - throughput, utilisation and scaling-efficiency benchmarks
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - stability and recovery benchmarks under injected faults
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - comparison against published large-scale training efficiency
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - regression gates for infrastructure changes
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_bench@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0849_training_bench.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0850-training-spec-doc

**P0850 · `training_spec_doc` — Training Specification & Model Card Generator** · [spec](PART_SPECS_T17.md#p0850-training-spec-doc) · [self-contained txt](../prompts/P0850_training_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0850  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0850 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0850  (50/50 of tier T17)
tier         : T17 — Training, Data & Recursive Self-Improvement
title        : Training Specification & Model Card Generator
file         : parts/t17_training/P0850_training_spec_doc.py          <-- create exactly this path, nothing else
module       : hyperion.t17.training.training_spec_doc
language     : Python 3.13
capability   : cap.t17.training.training_spec_doc@1
determinism  : io
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : Frontier-Bench v0.1, ARC-AGI-3

MISSION
-------
The authoritative record of how the model was made.

Tier context:
  Pretraining, RL from verifiable reward, distillation into the fast paths,
  and the closed self-improvement loop.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. model card generation with data, method, evaluation and limitation sections
  2. training-decision rationale documentation with evidence links
  3. honest capability and risk disclosure
  4. drift detection between documentation and actual training

Expanded obligations:
  1. Implement model card generation with data, method, evaluation and
     limitation sections with an explicit *a-priori* cost model. Before doing
     the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Correctness here is what makes the
     tier's Frontier-Bench v0.1 target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement training-decision rationale documentation with evidence links
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of ARC-AGI-3, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement honest capability and risk disclosure as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against Frontier-Bench v0.1 — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement drift detection between documentation and actual training, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     ARC-AGI-3 target reachable; the part therefore ships a microbenchmark
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
                       p99 <= 7000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t17.training.training_spec_doc@1
  cap.t17.training.training_spec_doc.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t17.training.training_bench@1
      if unavailable: use the in-file conservative substitute for
      `training_bench` (documented, slower, lower quality) and set
      `degraded['training_bench']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t05.positional.positional_design@1
      if unavailable: use the in-file conservative substitute for
      `positional_design` (documented, slower, lower quality) and set
      `degraded['positional_design']='local'`

  cap.t06.expert.expert_diversity@1
      if unavailable: use the in-file conservative substitute for
      `expert_diversity` (documented, slower, lower quality) and set
      `degraded['expert_diversity']='local'`

  cap.t10.constraint.constraint_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `constraint_reasoning` (documented, slower, lower quality) and set
      `degraded['constraint_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - model card generation with data, method, evaluation and limitati
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - training-decision rationale documentation with evidence links
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - honest capability and risk disclosure
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - drift detection between documentation and actual training
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t17.training.training_spec_doc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t17_training/P0850_training_spec_doc.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
