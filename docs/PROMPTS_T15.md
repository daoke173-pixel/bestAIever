# HYPERION-Ω — Worker prompts · T15 · Generation, Artifacts & Interface Craft

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

## PROMPT p0701-artifact-model

**P0701 · `artifact_model` — Artifact Data Model & Lifecycle** · [spec](PART_SPECS_T15.md#p0701-artifact-model) · [self-contained txt](../prompts/P0701_artifact_model.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0701  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0701 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0701  (1/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Artifact Data Model & Lifecycle
file         : parts/t15_generation/P0701_artifact_model.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.artifact_model
language     : TypeScript 5.7
capability   : cap.t15.artifact.artifact_model@1
determinism  : seeded
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Every output is a versioned, addressable, revisable object.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. artifact schema with type, version, provenance and revision history
  2. immutable versions with diff-based revision chains
  3. dependency tracking between artifacts
  4. lifecycle state machine with validation at every transition

Expanded obligations:
  1. Implement artifact schema with type, version, provenance and revision
     history, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement immutable versions with diff-based revision chains with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement dependency tracking between artifacts together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement lifecycle state machine with validation at every transition as
     a first-class, fully realised mechanism. No stub, no
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.artifact.artifact_model@1
  cap.t15.artifact.artifact_model.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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

  cap.t14.modality.modality_translation@1
      if unavailable: use the in-file conservative substitute for
      `modality_translation` (documented, slower, lower quality) and set
      `degraded['modality_translation']='local'`

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
   3. [ 600 lines] Core implementation A - artifact schema with type, version, provenance and revision hist
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - immutable versions with diff-based revision chains
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - dependency tracking between artifacts
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - lifecycle state machine with validation at every transition
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.artifact.artifact_model@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0701_artifact_model.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0702-text-generation-quality

**P0702 · `text_generation_quality` — Long-Form Text Generation Engine** · [spec](PART_SPECS_T15.md#p0702-text-generation-quality) · [self-contained txt](../prompts/P0702_text_generation_quality.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0702  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0702 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0702  (2/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Long-Form Text Generation Engine
file         : parts/t15_generation/P0702_text_generation_quality.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.text_generation_quality
language     : TypeScript 5.7
capability   : cap.t15.text.text_generation_quality@1
determinism  : seeded
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Writes documents a professional would sign their name to.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structure planning before drafting, with outline verification
  2. coherence maintenance across very long documents
  3. claim-level factuality checking with citation integration
  4. expert-evaluation results versus Opus-class baselines

Expanded obligations:
  1. Implement structure planning before drafting, with outline verification
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GDPval-AA v2 (Elo) — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement coherence maintenance across very long documents together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement claim-level factuality checking with citation integration as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement expert-evaluation results versus Opus-class baselines, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against MMMU — a
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.text.text_generation_quality@1
  cap.t15.text.text_generation_quality.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.artifact.artifact_model@1
      if unavailable: use the in-file conservative substitute for
      `artifact_model` (documented, slower, lower quality) and set
      `degraded['artifact_model']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t10.backtracking.backtracking@1
      if unavailable: use the in-file conservative substitute for
      `backtracking` (documented, slower, lower quality) and set
      `degraded['backtracking']='local'`

  cap.t14.math.math_formula_vision@1
      if unavailable: use the in-file conservative substitute for
      `math_formula_vision` (documented, slower, lower quality) and set
      `degraded['math_formula_vision']='local'`

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
   3. [ 600 lines] Core implementation A - structure planning before drafting, with outline verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - coherence maintenance across very long documents
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - claim-level factuality checking with citation integration
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-evaluation results versus Opus-class baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.text.text_generation_quality@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0702_text_generation_quality.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0703-style-control

**P0703 · `style_control` — Style, Tone & Register Control** · [spec](PART_SPECS_T15.md#p0703-style-control) · [self-contained txt](../prompts/P0703_style_control.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0703  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0703 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0703  (3/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Style, Tone & Register Control
file         : parts/t15_generation/P0703_style_control.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.style_control
language     : TypeScript 5.7
capability   : cap.t15.style.style_control@1
determinism  : seeded
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Writes in exactly the requested voice, consistently.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. style-parameter space (formality, density, warmth, technicality) with measurable control
  2. style consistency measurement across long outputs
  3. brand and house-style conformance from examples
  4. controllability measurement via automated style classifiers

Expanded obligations:
  1. Implement style-parameter space (formality, density, warmth,
     technicality) with measurable control together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Correctness here is what makes the
     tier's MMMU target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement style consistency measurement across long outputs as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement brand and house-style conformance from examples, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement controllability measurement via automated style classifiers
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
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
  cap.t15.style.style_control@1
  cap.t15.style.style_control.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.text.text_generation_quality@1
      if unavailable: use the in-file conservative substitute for
      `text_generation_quality` (documented, slower, lower quality) and set
      `degraded['text_generation_quality']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t10.question.question_asking@1
      if unavailable: use the in-file conservative substitute for
      `question_asking` (documented, slower, lower quality) and set
      `degraded['question_asking']='local'`

  cap.t14.realtime.realtime_perception@1
      if unavailable: use the in-file conservative substitute for
      `realtime_perception` (documented, slower, lower quality) and set
      `degraded['realtime_perception']='local'`

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
   3. [ 600 lines] Core implementation A - style-parameter space (formality, density, warmth, technicality)
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - style consistency measurement across long outputs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - brand and house-style conformance from examples
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - controllability measurement via automated style classifiers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.style.style_control@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0703_style_control.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0704-conciseness-engine

**P0704 · `conciseness_engine` — Conciseness & Information Density Optimiser** · [spec](PART_SPECS_T15.md#p0704-conciseness-engine) · [self-contained txt](../prompts/P0704_conciseness_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0704  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0704 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0704  (4/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Conciseness & Information Density Optimiser
file         : parts/t15_generation/P0704_conciseness_engine.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.conciseness_engine
language     : TypeScript 5.7
capability   : cap.t15.conciseness.conciseness_engine@1
determinism  : seeded
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Says everything necessary and nothing more.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. redundancy detection and compression without information loss
  2. information-density measurement per output type
  3. verbosity-versus-completeness calibration by request type
  4. measured token reduction at preserved usefulness scores

Expanded obligations:
  1. Implement redundancy detection and compression without information loss
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement information-density measurement per output type, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement verbosity-versus-completeness calibration by request type with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured token reduction at preserved usefulness scores
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of MMMU, so its p99 latency
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.conciseness.conciseness_engine@1
  cap.t15.conciseness.conciseness_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.style.style_control@1
      if unavailable: use the in-file conservative substitute for
      `style_control` (documented, slower, lower quality) and set
      `degraded['style_control']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t10.scratchpad.scratchpad_manager@1
      if unavailable: use the in-file conservative substitute for
      `scratchpad_manager` (documented, slower, lower quality) and set
      `degraded['scratchpad_manager']='local'`

  cap.t14.form.form_understanding@1
      if unavailable: use the in-file conservative substitute for
      `form_understanding` (documented, slower, lower quality) and set
      `degraded['form_understanding']='local'`

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
   3. [ 600 lines] Core implementation A - redundancy detection and compression without information loss
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - information-density measurement per output type
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - verbosity-versus-completeness calibration by request type
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured token reduction at preserved usefulness scores
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.conciseness.conciseness_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0704_conciseness_engine.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0705-markdown-rich-text

**P0705 · `markdown_rich_text` — Structured Text & Markup Rendering** · [spec](PART_SPECS_T15.md#p0705-markdown-rich-text) · [self-contained txt](../prompts/P0705_markdown_rich_text.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0705  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0705 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0705  (5/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Structured Text & Markup Rendering
file         : parts/t15_generation/P0705_markdown_rich_text.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.markdown_rich_text
language     : TypeScript 5.7
capability   : cap.t15.markdown.markdown_rich_text@1
determinism  : seeded
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Formatting that is correct, portable and semantically meaningful.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. markdown/HTML/LaTeX generation with strict validity
  2. semantic structure preservation across format conversion
  3. table, list and code-block formatting correctness
  4. round-trip fidelity verification across formats

Expanded obligations:
  1. Implement markdown/HTML/LaTeX generation with strict validity, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement semantic structure preservation across format conversion with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement table, list and code-block formatting correctness together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement round-trip fidelity verification across formats as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
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
  cap.t15.markdown.markdown_rich_text@1
  cap.t15.markdown.markdown_rich_text.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.conciseness.conciseness_engine@1
      if unavailable: use the in-file conservative substitute for
      `conciseness_engine` (documented, slower, lower quality) and set
      `degraded['conciseness_engine']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t10.reasoning.reasoning_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_speed_proof` (documented, slower, lower quality) and set
      `degraded['reasoning_speed_proof']='local'`

  cap.t14.perception.perception_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `perception_interpretability` (documented, slower, lower quality) and
      set `degraded['perception_interpretability']='local'`

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
   3. [ 600 lines] Core implementation A - markdown/HTML/LaTeX generation with strict validity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - semantic structure preservation across format conversion
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - table, list and code-block formatting correctness
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - round-trip fidelity verification across formats
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.markdown.markdown_rich_text@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0705_markdown_rich_text.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0706-code-artifact-gen

**P0706 · `code_artifact_gen` — Code Artifact Generation & Packaging** · [spec](PART_SPECS_T15.md#p0706-code-artifact-gen) · [self-contained txt](../prompts/P0706_code_artifact_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0706  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0706 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0706  (6/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Code Artifact Generation & Packaging
file         : parts/t15_generation/P0706_code_artifact_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.code_artifact_gen
language     : TypeScript 5.7
capability   : cap.t15.code.code_artifact_gen@1
determinism  : seeded
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Produces complete, runnable, tested projects.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-file project scaffolding with build configuration
  2. dependency specification with version pinning
  3. included test suite and documentation generation
  4. measured runnability rate of generated projects

Expanded obligations:
  1. Implement multi-file project scaffolding with build configuration with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement dependency specification with version pinning together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement included test suite and documentation generation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured runnability rate of generated projects, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
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
                       p99 <= 4000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.code.code_artifact_gen@1
  cap.t15.code.code_artifact_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.markdown.markdown_rich_text@1
      if unavailable: use the in-file conservative substitute for
      `markdown_rich_text` (documented, slower, lower quality) and set
      `degraded['markdown_rich_text']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t10.process.process_verifier@1
      if unavailable: use the in-file conservative substitute for
      `process_verifier` (documented, slower, lower quality) and set
      `degraded['process_verifier']='local'`

  cap.t14.chart.chart_understanding@1
      if unavailable: use the in-file conservative substitute for
      `chart_understanding` (documented, slower, lower quality) and set
      `degraded['chart_understanding']='local'`

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
   3. [ 600 lines] Core implementation A - multi-file project scaffolding with build configuration
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - dependency specification with version pinning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - included test suite and documentation generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured runnability rate of generated projects
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.code.code_artifact_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0706_code_artifact_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0707-ui-component-gen

**P0707 · `ui_component_gen` — UI Component & Interface Generation** · [spec](PART_SPECS_T15.md#p0707-ui-component-gen) · [self-contained txt](../prompts/P0707_ui_component_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0707  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0707 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0707  (7/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : UI Component & Interface Generation
file         : parts/t15_generation/P0707_ui_component_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.ui_component_gen
language     : TypeScript 5.7
capability   : cap.t15.ui.ui_component_gen@1
determinism  : seeded
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Interfaces that are correct at every viewport and accessible by default.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. component generation with state management and accessibility attributes
  2. responsive-layout generation with breakpoint reasoning
  3. design-token and theme consistency enforcement
  4. self-verification at multiple viewports before delivery

Expanded obligations:
  1. Implement component generation with state management and accessibility
     attributes together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of MMMU, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement responsive-layout generation with breakpoint reasoning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement design-token and theme consistency enforcement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement self-verification at multiple viewports before delivery with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.ui.ui_component_gen@1
  cap.t15.ui.ui_component_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.code.code_artifact_gen@1
      if unavailable: use the in-file conservative substitute for
      `code_artifact_gen` (documented, slower, lower quality) and set
      `degraded['code_artifact_gen']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t10.goal.goal_management@1
      if unavailable: use the in-file conservative substitute for
      `goal_management` (documented, slower, lower quality) and set
      `degraded['goal_management']='local'`

  cap.t14.temporal.temporal_video@1
      if unavailable: use the in-file conservative substitute for
      `temporal_video` (documented, slower, lower quality) and set
      `degraded['temporal_video']='local'`

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
   3. [ 600 lines] Core implementation A - component generation with state management and accessibility att
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - responsive-layout generation with breakpoint reasoning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - design-token and theme consistency enforcement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - self-verification at multiple viewports before delivery
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.ui.ui_component_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0707_ui_component_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0708-web-app-gen

**P0708 · `web_app_gen` — Full Web Application Generation** · [spec](PART_SPECS_T15.md#p0708-web-app-gen) · [self-contained txt](../prompts/P0708_web_app_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0708  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0708 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0708  (8/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Full Web Application Generation
file         : parts/t15_generation/P0708_web_app_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.web_app_gen
language     : TypeScript 5.7
capability   : cap.t15.web.web_app_gen@1
determinism  : seeded
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Complete applications, not demos.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. frontend/backend/data-layer generation with coherent contracts
  2. authentication, validation and error handling included by default
  3. deployment configuration generation
  4. measured end-to-end functionality rate of generated applications

Expanded obligations:
  1. Implement frontend/backend/data-layer generation with coherent contracts
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement authentication, validation and error handling included by
     default, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's MMMU
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement deployment configuration generation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured end-to-end functionality rate of generated
     applications together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against MMMU — a regression
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
  cap.t15.web.web_app_gen@1
  cap.t15.web.web_app_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.ui.ui_component_gen@1
      if unavailable: use the in-file conservative substitute for
      `ui_component_gen` (documented, slower, lower quality) and set
      `degraded['ui_component_gen']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t10.probabilistic.probabilistic_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `probabilistic_reasoning` (documented, slower, lower quality) and set
      `degraded['probabilistic_reasoning']='local'`

  cap.t14.multimodal.multimodal_alignment@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_alignment` (documented, slower, lower quality) and set
      `degraded['multimodal_alignment']='local'`

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
   3. [ 600 lines] Core implementation A - frontend/backend/data-layer generation with coherent contracts
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - authentication, validation and error handling included by defaul
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deployment configuration generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured end-to-end functionality rate of generated applications
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.web.web_app_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0708_web_app_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0709-visual-design-engine

**P0709 · `visual_design_engine` — Visual Design & Layout Engine** · [spec](PART_SPECS_T15.md#p0709-visual-design-engine) · [self-contained txt](../prompts/P0709_visual_design_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0709  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0709 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0709  (9/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Visual Design & Layout Engine
file         : parts/t15_generation/P0709_visual_design_engine.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.visual_design_engine
language     : TypeScript 5.7
capability   : cap.t15.visual.visual_design_engine@1
determinism  : seeded
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Design decisions with actual taste, justified.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. typography, spacing, colour and hierarchy systems with rationale
  2. layout composition rules and grid systems
  3. accessibility contrast and readability verification
  4. expert-designer evaluation results

Expanded obligations:
  1. Implement typography, spacing, colour and hierarchy systems with
     rationale, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's MMMU
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  2. Implement layout composition rules and grid systems with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement accessibility contrast and readability verification together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement expert-designer evaluation results as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
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
  cap.t15.visual.visual_design_engine@1
  cap.t15.visual.visual_design_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.web.web_app_gen@1
      if unavailable: use the in-file conservative substitute for
      `web_app_gen` (documented, slower, lower quality) and set
      `degraded['web_app_gen']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t10.stopping.stopping_rules@1
      if unavailable: use the in-file conservative substitute for
      `stopping_rules` (documented, slower, lower quality) and set
      `degraded['stopping_rules']='local'`

  cap.t14.handwriting.handwriting_sketch@1
      if unavailable: use the in-file conservative substitute for
      `handwriting_sketch` (documented, slower, lower quality) and set
      `degraded['handwriting_sketch']='local'`

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
   3. [ 600 lines] Core implementation A - typography, spacing, colour and hierarchy systems with rationale
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - layout composition rules and grid systems
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accessibility contrast and readability verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-designer evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.visual.visual_design_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0709_visual_design_engine.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0710-animation-engine

**P0710 · `animation_engine` — Animation & Motion Design** · [spec](PART_SPECS_T15.md#p0710-animation-engine) · [self-contained txt](../prompts/P0710_animation_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0710  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0710 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0710  (10/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Animation & Motion Design
file         : parts/t15_generation/P0710_animation_engine.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.animation_engine
language     : TypeScript 5.7
capability   : cap.t15.animation.animation_engine@1
determinism  : seeded
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Motion that communicates rather than decorates.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. timing, easing and choreography with purpose-driven rationale
  2. performance-budgeted animation (frame-rate guarantees)
  3. reduced-motion accessibility compliance
  4. expert evaluation versus Opus-class animation output

Expanded obligations:
  1. Implement timing, easing and choreography with purpose-driven rationale
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement performance-budgeted animation (frame-rate guarantees)
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement reduced-motion accessibility compliance as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GDPval-AA
     v2 (Elo) target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement expert evaluation versus Opus-class animation output, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of MMMU, so its p99 latency
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
  cap.t15.animation.animation_engine@1
  cap.t15.animation.animation_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.visual.visual_design_engine@1
      if unavailable: use the in-file conservative substitute for
      `visual_design_engine` (documented, slower, lower quality) and set
      `degraded['visual_design_engine']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t10.assumption.assumption_tracking@1
      if unavailable: use the in-file conservative substitute for
      `assumption_tracking` (documented, slower, lower quality) and set
      `degraded['assumption_tracking']='local'`

  cap.t14.sensor.sensor_fusion@1
      if unavailable: use the in-file conservative substitute for
      `sensor_fusion` (documented, slower, lower quality) and set
      `degraded['sensor_fusion']='local'`

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
   3. [ 600 lines] Core implementation A - timing, easing and choreography with purpose-driven rationale
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - performance-budgeted animation (frame-rate guarantees)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - reduced-motion accessibility compliance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert evaluation versus Opus-class animation output
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.animation.animation_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0710_animation_engine.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0711-data-visualisation

**P0711 · `data_visualisation` — Data Visualisation Generation** · [spec](PART_SPECS_T15.md#p0711-data-visualisation) · [self-contained txt](../prompts/P0711_data_visualisation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0711  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0711 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0711  (11/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Data Visualisation Generation
file         : parts/t15_generation/P0711_data_visualisation.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.data_visualisation
language     : TypeScript 5.7
capability   : cap.t15.data.data_visualisation@1
determinism  : seeded
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Charts that are honest, clear and correct.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. chart-type selection appropriate to data and question
  2. axis, scale and annotation correctness with misleading-visual prevention
  3. accessibility (colour-blind safe, screen-reader labels)
  4. expert evaluation of clarity and honesty

Expanded obligations:
  1. Implement chart-type selection appropriate to data and question together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement axis, scale and annotation correctness with misleading-visual
     prevention as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement accessibility (colour-blind safe, screen-reader labels), and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  4. Implement expert evaluation of clarity and honesty with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
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
  cap.t15.data.data_visualisation@1
  cap.t15.data.data_visualisation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.animation.animation_engine@1
      if unavailable: use the in-file conservative substitute for
      `animation_engine` (documented, slower, lower quality) and set
      `degraded['animation_engine']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t10.reasoning.reasoning_cost_model@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_cost_model` (documented, slower, lower quality) and set
      `degraded['reasoning_cost_model']='local'`

  cap.t14.data.data_extraction_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `data_extraction_pipeline` (documented, slower, lower quality) and set
      `degraded['data_extraction_pipeline']='local'`

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
   3. [ 600 lines] Core implementation A - chart-type selection appropriate to data and question
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - axis, scale and annotation correctness with misleading-visual pr
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accessibility (colour-blind safe, screen-reader labels)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert evaluation of clarity and honesty
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.data.data_visualisation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0711_data_visualisation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0712-presentation-gen

**P0712 · `presentation_gen` — Presentation & Deck Generation** · [spec](PART_SPECS_T15.md#p0712-presentation-gen) · [self-contained txt](../prompts/P0712_presentation_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0712  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0712 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0712  (12/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Presentation & Deck Generation
file         : parts/t15_generation/P0712_presentation_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.presentation_gen
language     : TypeScript 5.7
capability   : cap.t15.presentation.presentation_gen@1
determinism  : seeded
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Decks that survive an executive audience.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. narrative arc construction with per-slide message discipline
  2. layout consistency and visual hierarchy across slides
  3. speaker-note and appendix generation
  4. expert evaluation versus Opus-class deck output

Expanded obligations:
  1. Implement narrative arc construction with per-slide message discipline
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement layout consistency and visual hierarchy across slides, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement speaker-note and appendix generation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement expert evaluation versus Opus-class deck output together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.presentation.presentation_gen@1
  cap.t15.presentation.presentation_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.data.data_visualisation@1
      if unavailable: use the in-file conservative substitute for
      `data_visualisation` (documented, slower, lower quality) and set
      `degraded['data_visualisation']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t10.collective.collective_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `collective_reasoning` (documented, slower, lower quality) and set
      `degraded['collective_reasoning']='local'`

  cap.t14.synthetic.synthetic_perception_data@1
      if unavailable: use the in-file conservative substitute for
      `synthetic_perception_data` (documented, slower, lower quality) and
      set `degraded['synthetic_perception_data']='local'`

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
   3. [ 600 lines] Core implementation A - narrative arc construction with per-slide message discipline
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - layout consistency and visual hierarchy across slides
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - speaker-note and appendix generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert evaluation versus Opus-class deck output
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.presentation.presentation_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0712_presentation_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0713-document-gen-office

**P0713 · `document_gen_office` — Office Document Generation** · [spec](PART_SPECS_T15.md#p0713-document-gen-office) · [self-contained txt](../prompts/P0713_document_gen_office.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0713  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0713 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0713  (13/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Office Document Generation
file         : parts/t15_generation/P0713_document_gen_office.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.document_gen_office
language     : TypeScript 5.7
capability   : cap.t15.document.document_gen_office@1
determinism  : seeded
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Word, Excel and PDF output that opens correctly everywhere.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. format-native generation with valid internal structure
  2. template conformance and style inheritance
  3. cross-application rendering verification
  4. fidelity measurement across viewer applications

Expanded obligations:
  1. Implement format-native generation with valid internal structure, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement template conformance and style inheritance with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
     that benchmark is an automatic rejection of this part.
  3. Implement cross-application rendering verification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement fidelity measurement across viewer applications as a
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.document.document_gen_office@1
  cap.t15.document.document_gen_office.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.presentation.presentation_gen@1
      if unavailable: use the in-file conservative substitute for
      `presentation_gen` (documented, slower, lower quality) and set
      `degraded['presentation_gen']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t10.beam.beam_pruning@1
      if unavailable: use the in-file conservative substitute for
      `beam_pruning` (documented, slower, lower quality) and set
      `degraded['beam_pruning']='local'`

  cap.t14.table.table_extraction@1
      if unavailable: use the in-file conservative substitute for
      `table_extraction` (documented, slower, lower quality) and set
      `degraded['table_extraction']='local'`

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
   3. [ 600 lines] Core implementation A - format-native generation with valid internal structure
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - template conformance and style inheritance
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cross-application rendering verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fidelity measurement across viewer applications
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.document.document_gen_office@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0713_document_gen_office.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0714-report-generation

**P0714 · `report_generation` — Analytical Report Generation** · [spec](PART_SPECS_T15.md#p0714-report-generation) · [self-contained txt](../prompts/P0714_report_generation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0714  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0714 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0714  (14/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Analytical Report Generation
file         : parts/t15_generation/P0714_report_generation.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.report_generation
language     : TypeScript 5.7
capability   : cap.t15.report.report_generation@1
determinism  : seeded
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Reports with real analysis, real numbers and real caveats.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. evidence-driven narrative with quantitative verification
  2. limitation and uncertainty sections generated honestly
  3. executive-summary generation with fidelity to the body
  4. expert evaluation of analytical quality

Expanded obligations:
  1. Implement evidence-driven narrative with quantitative verification with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GDPval-AA v2 (Elo) — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement limitation and uncertainty sections generated honestly
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement executive-summary generation with fidelity to the body as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement expert evaluation of analytical quality, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
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
                       p99 <= 12000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.report.report_generation@1
  cap.t15.report.report_generation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.document.document_gen_office@1
      if unavailable: use the in-file conservative substitute for
      `document_gen_office` (documented, slower, lower quality) and set
      `degraded['document_gen_office']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t10.planning.planning_engine@1
      if unavailable: use the in-file conservative substitute for
      `planning_engine` (documented, slower, lower quality) and set
      `degraded['planning_engine']='local'`

  cap.t14.video.video_encoder@1
      if unavailable: use the in-file conservative substitute for
      `video_encoder` (documented, slower, lower quality) and set
      `degraded['video_encoder']='local'`

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
   3. [ 600 lines] Core implementation A - evidence-driven narrative with quantitative verification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - limitation and uncertainty sections generated honestly
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - executive-summary generation with fidelity to the body
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert evaluation of analytical quality
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.report.report_generation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0714_report_generation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0715-three-d-generation

**P0715 · `three_d_generation` — 3D Model & Scene Generation** · [spec](PART_SPECS_T15.md#p0715-three-d-generation) · [self-contained txt](../prompts/P0715_three_d_generation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0715  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0715 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0715  (15/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : 3D Model & Scene Generation
file         : parts/t15_generation/P0715_three_d_generation.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.three_d_generation
language     : TypeScript 5.7
capability   : cap.t15.three.three_d_generation@1
determinism  : seeded
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Geometry that is manufacturable and physically sensible.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. parametric and mesh generation with validity checking (watertight, manifold)
  2. CAD-format export with dimensional accuracy
  3. physical-plausibility and constraint verification
  4. measured manufacturability of generated models

Expanded obligations:
  1. Implement parametric and mesh generation with validity checking
     (watertight, manifold) together with its verification path, so that
     anything this mechanism produces can be independently re-checked *inside
     this same file* without contacting any other part. The checker must be
     cheap enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's MMMU target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement CAD-format export with dimensional accuracy as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of GDPval-AA
     v2 (Elo), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement physical-plausibility and constraint verification, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement measured manufacturability of generated models with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
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
  cap.t15.three.three_d_generation@1
  cap.t15.three.three_d_generation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.report.report_generation@1
      if unavailable: use the in-file conservative substitute for
      `report_generation` (documented, slower, lower quality) and set
      `degraded['report_generation']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t10.counterfactual.counterfactual_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `counterfactual_reasoning` (documented, slower, lower quality) and set
      `degraded['counterfactual_reasoning']='local'`

  cap.t14.audio.audio_events@1
      if unavailable: use the in-file conservative substitute for
      `audio_events` (documented, slower, lower quality) and set
      `degraded['audio_events']='local'`

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
   3. [ 600 lines] Core implementation A - parametric and mesh generation with validity checking (watertigh
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - CAD-format export with dimensional accuracy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - physical-plausibility and constraint verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured manufacturability of generated models
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.three.three_d_generation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0715_three_d_generation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0716-game-generation

**P0716 · `game_generation` — Interactive Game & Simulation Generation** · [spec](PART_SPECS_T15.md#p0716-game-generation) · [self-contained txt](../prompts/P0716_game_generation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0716  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0716 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0716  (16/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Interactive Game & Simulation Generation
file         : parts/t15_generation/P0716_game_generation.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.game_generation
language     : TypeScript 5.7
capability   : cap.t15.game.game_generation@1
determinism  : seeded
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Playable, balanced, bug-free interactive experiences.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. game-loop, physics and state-management generation
  2. playability self-testing via automated play-throughs
  3. balance and difficulty-curve reasoning
  4. measured playability rate of generated games

Expanded obligations:
  1. Implement game-loop, physics and state-management generation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement playability self-testing via automated play-throughs, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement balance and difficulty-curve reasoning with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GDPval-AA v2 (Elo) target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured playability rate of generated games together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.game.game_generation@1
  cap.t15.game.game_generation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.three.three_d_generation@1
      if unavailable: use the in-file conservative substitute for
      `three_d_generation` (documented, slower, lower quality) and set
      `degraded['three_d_generation']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t10.difficulty.difficulty_estimation@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_estimation` (documented, slower, lower quality) and set
      `degraded['difficulty_estimation']='local'`

  cap.t14.ui.ui_screenshot@1
      if unavailable: use the in-file conservative substitute for
      `ui_screenshot` (documented, slower, lower quality) and set
      `degraded['ui_screenshot']='local'`

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
   3. [ 600 lines] Core implementation A - game-loop, physics and state-management generation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - playability self-testing via automated play-throughs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - balance and difficulty-curve reasoning
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured playability rate of generated games
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.game.game_generation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0716_game_generation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0717-image-generation-bridge

**P0717 · `image_generation_bridge` — Image Generation Direction & Control** · [spec](PART_SPECS_T15.md#p0717-image-generation-bridge) · [self-contained txt](../prompts/P0717_image_generation_bridge.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0717  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0717 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0717  (17/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Image Generation Direction & Control
file         : parts/t15_generation/P0717_image_generation_bridge.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.image_generation_bridge
language     : TypeScript 5.7
capability   : cap.t15.image.image_generation_bridge@1
determinism  : seeded
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Directs image generation with precision and evaluates the result.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. prompt construction from high-level intent with style control
  2. generated-image verification against the requested specification
  3. iterative refinement with targeted correction
  4. measured specification-satisfaction rate

Expanded obligations:
  1. Implement prompt construction from high-level intent with style control,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against MMMU — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement generated-image verification against the requested
     specification with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's GDPval-AA v2
     (Elo) target reachable; the part therefore ships a microbenchmark that
     stands in for that benchmark's inner loop.
  3. Implement iterative refinement with targeted correction together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement measured specification-satisfaction rate as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against GDPval-AA v2
     (Elo) — a regression on that benchmark is an automatic rejection of this
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.image.image_generation_bridge@1
  cap.t15.image.image_generation_bridge.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.game.game_generation@1
      if unavailable: use the in-file conservative substitute for
      `game_generation` (documented, slower, lower quality) and set
      `degraded['game_generation']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t10.evidence.evidence_integration@1
      if unavailable: use the in-file conservative substitute for
      `evidence_integration` (documented, slower, lower quality) and set
      `degraded['evidence_integration']='local'`

  cap.t14.prompt.prompt_injection_visual@1
      if unavailable: use the in-file conservative substitute for
      `prompt_injection_visual` (documented, slower, lower quality) and set
      `degraded['prompt_injection_visual']='local'`

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
   3. [ 600 lines] Core implementation A - prompt construction from high-level intent with style control
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - generated-image verification against the requested specification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - iterative refinement with targeted correction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured specification-satisfaction rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.image.image_generation_bridge@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0717_image_generation_bridge.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0718-video-generation-bridge

**P0718 · `video_generation_bridge` — Video Generation Direction & Editing** · [spec](PART_SPECS_T15.md#p0718-video-generation-bridge) · [self-contained txt](../prompts/P0718_video_generation_bridge.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0718  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0718 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0718  (18/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Video Generation Direction & Editing
file         : parts/t15_generation/P0718_video_generation_bridge.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.video_generation_bridge
language     : TypeScript 5.7
capability   : cap.t15.video.video_generation_bridge@1
determinism  : seeded
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Directs and assembles video with narrative and technical control.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. shot planning, continuity and pacing specification
  2. generated-clip verification and assembly with transitions
  3. audio synchronisation and mixing direction
  4. measured continuity and specification-satisfaction rates

Expanded obligations:
  1. Implement shot planning, continuity and pacing specification with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement generated-clip verification and assembly with transitions
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of MMMU, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement audio synchronisation and mixing direction as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against GDPval-AA v2
     (Elo) — a regression on that benchmark is an automatic rejection of this
     part.
  4. Implement measured continuity and specification-satisfaction rates, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's MMMU
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.video.video_generation_bridge@1
  cap.t15.video.video_generation_bridge.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.image.image_generation_bridge@1
      if unavailable: use the in-file conservative substitute for
      `image_generation_bridge` (documented, slower, lower quality) and set
      `degraded['image_generation_bridge']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t10.reasoning.reasoning_search_bench@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_search_bench` (documented, slower, lower quality) and set
      `degraded['reasoning_search_bench']='local'`

  cap.t14.perception.perception_multilingual@1
      if unavailable: use the in-file conservative substitute for
      `perception_multilingual` (documented, slower, lower quality) and set
      `degraded['perception_multilingual']='local'`

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
   3. [ 600 lines] Core implementation A - shot planning, continuity and pacing specification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - generated-clip verification and assembly with transitions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - audio synchronisation and mixing direction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured continuity and specification-satisfaction rates
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.video.video_generation_bridge@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0718_video_generation_bridge.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0719-audio-generation-bridge

**P0719 · `audio_generation_bridge` — Speech & Audio Generation Direction** · [spec](PART_SPECS_T15.md#p0719-audio-generation-bridge) · [self-contained txt](../prompts/P0719_audio_generation_bridge.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0719  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0719 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0719  (19/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Speech & Audio Generation Direction
file         : parts/t15_generation/P0719_audio_generation_bridge.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.audio_generation_bridge
language     : TypeScript 5.7
capability   : cap.t15.audio.audio_generation_bridge@1
determinism  : seeded
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Voice output with correct prosody, pacing and emotion.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. speech-synthesis direction with prosodic markup
  2. multi-speaker dialogue direction with consistent voices
  3. audio-quality verification of generated output
  4. listener-evaluation results on naturalness and appropriateness

Expanded obligations:
  1. Implement speech-synthesis direction with prosodic markup together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement multi-speaker dialogue direction with consistent voices as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement audio-quality verification of generated output, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement listener-evaluation results on naturalness and appropriateness
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.audio.audio_generation_bridge@1
  cap.t15.audio.audio_generation_bridge.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.video.video_generation_bridge@1
      if unavailable: use the in-file conservative substitute for
      `video_generation_bridge` (documented, slower, lower quality) and set
      `degraded['video_generation_bridge']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t10.reasoning.reasoning_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_interpretability` (documented, slower, lower quality) and
      set `degraded['reasoning_interpretability']='local'`

  cap.t14.perception.perception_eval_harness@1
      if unavailable: use the in-file conservative substitute for
      `perception_eval_harness` (documented, slower, lower quality) and set
      `degraded['perception_eval_harness']='local'`

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
   3. [ 600 lines] Core implementation A - speech-synthesis direction with prosodic markup
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - multi-speaker dialogue direction with consistent voices
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - audio-quality verification of generated output
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - listener-evaluation results on naturalness and appropriateness
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.audio.audio_generation_bridge@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0719_audio_generation_bridge.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0720-music-generation-bridge

**P0720 · `music_generation_bridge` — Music Generation Direction** · [spec](PART_SPECS_T15.md#p0720-music-generation-bridge) · [self-contained txt](../prompts/P0720_music_generation_bridge.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0720  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0720 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0720  (20/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Music Generation Direction
file         : parts/t15_generation/P0720_music_generation_bridge.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.music_generation_bridge
language     : TypeScript 5.7
capability   : cap.t15.music.music_generation_bridge@1
determinism  : seeded
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Music that fits its purpose musically.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. musical specification (key, tempo, instrumentation, structure, mood)
  2. generated-audio verification against the specification
  3. loop, transition and duration-fit handling
  4. musician-evaluation results

Expanded obligations:
  1. Implement musical specification (key, tempo, instrumentation, structure,
     mood) as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement generated-audio verification against the specification, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's MMMU
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement loop, transition and duration-fit handling with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement musician-evaluation results together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. Its contribution is measured against
     MMMU — a regression on that benchmark is an automatic rejection of this
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.music.music_generation_bridge@1
  cap.t15.music.music_generation_bridge.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.audio.audio_generation_bridge@1
      if unavailable: use the in-file conservative substitute for
      `audio_generation_bridge` (documented, slower, lower quality) and set
      `degraded['audio_generation_bridge']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t10.graph.graph_search@1
      if unavailable: use the in-file conservative substitute for
      `graph_search` (documented, slower, lower quality) and set
      `degraded['graph_search']='local'`

  cap.t14.document.document_layout@1
      if unavailable: use the in-file conservative substitute for
      `document_layout` (documented, slower, lower quality) and set
      `degraded['document_layout']='local'`

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
   3. [ 600 lines] Core implementation A - musical specification (key, tempo, instrumentation, structure, m
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - generated-audio verification against the specification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - loop, transition and duration-fit handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - musician-evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.music.music_generation_bridge@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0720_music_generation_bridge.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0721-multilingual-generation

**P0721 · `multilingual_generation` — Multilingual Generation & Localisation** · [spec](PART_SPECS_T15.md#p0721-multilingual-generation) · [self-contained txt](../prompts/P0721_multilingual_generation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0721  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0721 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0721  (21/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Multilingual Generation & Localisation
file         : parts/t15_generation/P0721_multilingual_generation.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.multilingual_generation
language     : TypeScript 5.7
capability   : cap.t15.multilingual.multilingual_generation@1
determinism  : seeded
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Native-quality output in every language, not translated English.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. language-native composition rather than translation
  2. cultural adaptation with locale-specific conventions
  3. script, formatting and pluralisation correctness
  4. native-speaker evaluation results across language families

Expanded obligations:
  1. Implement language-native composition rather than translation, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement cultural adaptation with locale-specific conventions with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement script, formatting and pluralisation correctness together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement native-speaker evaluation results across language families as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
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
  cap.t15.multilingual.multilingual_generation@1
  cap.t15.multilingual.multilingual_generation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.music.music_generation_bridge@1
      if unavailable: use the in-file conservative substitute for
      `music_generation_bridge` (documented, slower, lower quality) and set
      `degraded['music_generation_bridge']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t10.decomposition.decomposition@1
      if unavailable: use the in-file conservative substitute for
      `decomposition` (documented, slower, lower quality) and set
      `degraded['decomposition']='local'`

  cap.t14.cad.cad_understanding@1
      if unavailable: use the in-file conservative substitute for
      `cad_understanding` (documented, slower, lower quality) and set
      `degraded['cad_understanding']='local'`

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
   3. [ 600 lines] Core implementation A - language-native composition rather than translation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cultural adaptation with locale-specific conventions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - script, formatting and pluralisation correctness
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - native-speaker evaluation results across language families
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.multilingual.multilingual_generation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0721_multilingual_generation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0722-translation-quality

**P0722 · `translation_quality` — Translation & Cross-Lingual Fidelity** · [spec](PART_SPECS_T15.md#p0722-translation-quality) · [self-contained txt](../prompts/P0722_translation_quality.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0722  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0722 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0722  (22/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Translation & Cross-Lingual Fidelity
file         : parts/t15_generation/P0722_translation_quality.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.translation_quality
language     : TypeScript 5.7
capability   : cap.t15.translation.translation_quality@1
determinism  : seeded
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Translation that preserves meaning, tone and terminology.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. terminology consistency with glossary enforcement
  2. register and tone preservation across languages
  3. back-translation and semantic-equivalence verification
  4. professional-translator evaluation results

Expanded obligations:
  1. Implement terminology consistency with glossary enforcement with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement register and tone preservation across languages together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement back-translation and semantic-equivalence verification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement professional-translator evaluation results, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of MMMU, so its p99 latency
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.translation.translation_quality@1
  cap.t15.translation.translation_quality.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.multilingual.multilingual_generation@1
      if unavailable: use the in-file conservative substitute for
      `multilingual_generation` (documented, slower, lower quality) and set
      `degraded['multilingual_generation']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t10.program.program_synthesis_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `program_synthesis_reasoning` (documented, slower, lower quality) and
      set `degraded['program_synthesis_reasoning']='local'`

  cap.t14.music.music_understanding@1
      if unavailable: use the in-file conservative substitute for
      `music_understanding` (documented, slower, lower quality) and set
      `degraded['music_understanding']='local'`

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
   3. [ 600 lines] Core implementation A - terminology consistency with glossary enforcement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - register and tone preservation across languages
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - back-translation and semantic-equivalence verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - professional-translator evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.translation.translation_quality@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0722_translation_quality.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0723-taste-model

**P0723 · `taste_model` — Aesthetic & Quality Judgment Model** · [spec](PART_SPECS_T15.md#p0723-taste-model) · [self-contained txt](../prompts/P0723_taste_model.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0723  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0723 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0723  (23/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Aesthetic & Quality Judgment Model
file         : parts/t15_generation/P0723_taste_model.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.taste_model
language     : TypeScript 5.7
capability   : cap.t15.taste.taste_model@1
determinism  : seeded
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
The internal critic that decides whether output is actually good.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-dimensional quality scoring (correctness, clarity, aesthetics, fitness)
  2. calibration against expert human judgments per domain
  3. quality-gate integration blocking substandard output
  4. agreement measurement with expert reviewers

Expanded obligations:
  1. Implement multi-dimensional quality scoring (correctness, clarity,
     aesthetics, fitness) together with its verification path, so that
     anything this mechanism produces can be independently re-checked *inside
     this same file* without contacting any other part. The checker must be
     cheap enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against MMMU — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement calibration against expert human judgments per domain as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement quality-gate integration blocking substandard output, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of MMMU, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement agreement measurement with expert reviewers with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.taste.taste_model@1
  cap.t15.taste.taste_model.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.translation.translation_quality@1
      if unavailable: use the in-file conservative substitute for
      `translation_quality` (documented, slower, lower quality) and set
      `degraded['translation_quality']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t10.meta.meta_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `meta_reasoning` (documented, slower, lower quality) and set
      `degraded['meta_reasoning']='local'`

  cap.t14.satellite.satellite_geospatial@1
      if unavailable: use the in-file conservative substitute for
      `satellite_geospatial` (documented, slower, lower quality) and set
      `degraded['satellite_geospatial']='local'`

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
   3. [ 600 lines] Core implementation A - multi-dimensional quality scoring (correctness, clarity, aesthet
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - calibration against expert human judgments per domain
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality-gate integration blocking substandard output
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - agreement measurement with expert reviewers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.taste.taste_model@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0723_taste_model.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0724-output-verification

**P0724 · `output_verification` — Output Self-Verification Pipeline** · [spec](PART_SPECS_T15.md#p0724-output-verification) · [self-contained txt](../prompts/P0724_output_verification.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0724  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0724 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0724  (24/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Output Self-Verification Pipeline
file         : parts/t15_generation/P0724_output_verification.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.output_verification
language     : TypeScript 5.7
capability   : cap.t15.output.output_verification@1
determinism  : seeded
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Checks its own work before delivery, always.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. type-specific verification (compile, render, execute, validate, proofread)
  2. targeted regeneration of only the failing element
  3. verification-latency budget with completeness reporting
  4. measured defect-escape-rate reduction

Expanded obligations:
  1. Implement type-specific verification (compile, render, execute,
     validate, proofread) as a first-class, fully realised mechanism. No
     stub, no `NotImplementedError`, no configuration flag whose default
     disables it. Its state must be reportable through `describe()` and it
     must be exercised by at least eight in-file tests, including one that
     fails loudly if the mechanism is silently bypassed. Correctness here is
     what makes the tier's GDPval-AA v2 (Elo) target reachable; the part
     therefore ships a microbenchmark that stands in for that benchmark's
     inner loop.
  2. Implement targeted regeneration of only the failing element, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of MMMU, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement verification-latency budget with completeness reporting with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GDPval-AA v2 (Elo) — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement measured defect-escape-rate reduction together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.output.output_verification@1
  cap.t15.output.output_verification.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.taste.taste_model@1
      if unavailable: use the in-file conservative substitute for
      `taste_model` (documented, slower, lower quality) and set
      `degraded['taste_model']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t10.hypothesis.hypothesis_management@1
      if unavailable: use the in-file conservative substitute for
      `hypothesis_management` (documented, slower, lower quality) and set
      `degraded['hypothesis_management']='local'`

  cap.t14.perception.perception_robustness@1
      if unavailable: use the in-file conservative substitute for
      `perception_robustness` (documented, slower, lower quality) and set
      `degraded['perception_robustness']='local'`

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
   3. [ 600 lines] Core implementation A - type-specific verification (compile, render, execute, validate, 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - targeted regeneration of only the failing element
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - verification-latency budget with completeness reporting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured defect-escape-rate reduction
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.output.output_verification@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0724_output_verification.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0725-rendering-verification

**P0725 · `rendering_verification` — Rendering & Visual Self-Check** · [spec](PART_SPECS_T15.md#p0725-rendering-verification) · [self-contained txt](../prompts/P0725_rendering_verification.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0725  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0725 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0725  (25/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Rendering & Visual Self-Check
file         : parts/t15_generation/P0725_rendering_verification.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.rendering_verification
language     : TypeScript 5.7
capability   : cap.t15.rendering.rendering_verification@1
determinism  : seeded
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Actually looks at what it made, at every size.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. headless rendering at multiple viewports and platforms
  2. visual-defect detection (overflow, occlusion, contrast, cut-off elements)
  3. automatic correction of detected visual defects
  4. measured visual-defect rate versus Opus-class baselines

Expanded obligations:
  1. Implement headless rendering at multiple viewports and platforms, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement visual-defect detection (overflow, occlusion, contrast,
     cut-off elements) with an explicit *a-priori* cost model. Before doing
     the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Its contribution is measured
     against GDPval-AA v2 (Elo) — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement automatic correction of detected visual defects together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured visual-defect rate versus Opus-class baselines as a
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.rendering.rendering_verification@1
  cap.t15.rendering.rendering_verification.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.output.output_verification@1
      if unavailable: use the in-file conservative substitute for
      `output_verification` (documented, slower, lower quality) and set
      `degraded['output_verification']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t10.proof.proof_sketch@1
      if unavailable: use the in-file conservative substitute for
      `proof_sketch` (documented, slower, lower quality) and set
      `degraded['proof_sketch']='local'`

  cap.t14.accessibility.accessibility_perception@1
      if unavailable: use the in-file conservative substitute for
      `accessibility_perception` (documented, slower, lower quality) and set
      `degraded['accessibility_perception']='local'`

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
   3. [ 600 lines] Core implementation A - headless rendering at multiple viewports and platforms
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - visual-defect detection (overflow, occlusion, contrast, cut-off 
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - automatic correction of detected visual defects
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured visual-defect rate versus Opus-class baselines
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.rendering.rendering_verification@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0725_rendering_verification.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0726-accessibility-gen

**P0726 · `accessibility_gen` — Accessibility Compliance Engine** · [spec](PART_SPECS_T15.md#p0726-accessibility-gen) · [self-contained txt](../prompts/P0726_accessibility_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0726  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0726 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0726  (26/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Accessibility Compliance Engine
file         : parts/t15_generation/P0726_accessibility_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.accessibility_gen
language     : TypeScript 5.7
capability   : cap.t15.accessibility.accessibility_gen@1
determinism  : seeded
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Output that works for everyone, verified.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. WCAG-level compliance checking and automatic remediation
  2. semantic-markup and keyboard-navigation verification
  3. screen-reader output simulation and review
  4. compliance-rate measurement across generated artifacts

Expanded obligations:
  1. Implement WCAG-level compliance checking and automatic remediation with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GDPval-AA v2 (Elo) — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement semantic-markup and keyboard-navigation verification together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement screen-reader output simulation and review as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of GDPval-AA
     v2 (Elo), so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement compliance-rate measurement across generated artifacts, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against MMMU — a
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
                       p99 <= 24000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.accessibility.accessibility_gen@1
  cap.t15.accessibility.accessibility_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.rendering.rendering_verification@1
      if unavailable: use the in-file conservative substitute for
      `rendering_verification` (documented, slower, lower quality) and set
      `degraded['rendering_verification']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t10.adversarial.adversarial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `adversarial_reasoning` (documented, slower, lower quality) and set
      `degraded['adversarial_reasoning']='local'`

  cap.t14.perception.perception_distillation@1
      if unavailable: use the in-file conservative substitute for
      `perception_distillation` (documented, slower, lower quality) and set
      `degraded['perception_distillation']='local'`

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
   3. [ 600 lines] Core implementation A - WCAG-level compliance checking and automatic remediation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - semantic-markup and keyboard-navigation verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - screen-reader output simulation and review
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - compliance-rate measurement across generated artifacts
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.accessibility.accessibility_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0726_accessibility_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0727-citation-formatting

**P0727 · `citation_formatting` — Citation, Attribution & Reference Management** · [spec](PART_SPECS_T15.md#p0727-citation-formatting) · [self-contained txt](../prompts/P0727_citation_formatting.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0727  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0727 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0727  (27/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Citation, Attribution & Reference Management
file         : parts/t15_generation/P0727_citation_formatting.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.citation_formatting
language     : TypeScript 5.7
capability   : cap.t15.citation.citation_formatting@1
determinism  : seeded
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Every claim sourced, every source correctly formatted.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. citation-style implementation with format validation
  2. source-availability and link-integrity verification
  3. attribution completeness checking against claim inventory
  4. citation-accuracy measurement

Expanded obligations:
  1. Implement citation-style implementation with format validation together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement source-availability and link-integrity verification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement attribution completeness checking against claim inventory, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against MMMU — a
     regression on that benchmark is an automatic rejection of this part.
  4. Implement citation-accuracy measurement with an explicit *a-priori* cost
     model. Before doing the work the part must be able to state the tokens,
     FLOPs and microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Correctness here is what makes the
     tier's GDPval-AA v2 (Elo) target reachable; the part therefore ships a
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
  cap.t15.citation.citation_formatting@1
  cap.t15.citation.citation_formatting.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.accessibility.accessibility_gen@1
      if unavailable: use the in-file conservative substitute for
      `accessibility_gen` (documented, slower, lower quality) and set
      `degraded['accessibility_gen']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t10.tree.tree_search@1
      if unavailable: use the in-file conservative substitute for
      `tree_search` (documented, slower, lower quality) and set
      `degraded['tree_search']='local'`

  cap.t14.ocr.ocr_engine@1
      if unavailable: use the in-file conservative substitute for
      `ocr_engine` (documented, slower, lower quality) and set
      `degraded['ocr_engine']='local'`

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
   3. [ 600 lines] Core implementation A - citation-style implementation with format validation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - source-availability and link-integrity verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - attribution completeness checking against claim inventory
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - citation-accuracy measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.citation.citation_formatting@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0727_citation_formatting.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0728-factuality-gen

**P0728 · `factuality_gen` — Generation-Time Factuality Enforcement** · [spec](PART_SPECS_T15.md#p0728-factuality-gen) · [self-contained txt](../prompts/P0728_factuality_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0728  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0728 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0728  (28/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Generation-Time Factuality Enforcement
file         : parts/t15_generation/P0728_factuality_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.factuality_gen
language     : TypeScript 5.7
capability   : cap.t15.factuality.factuality_gen@1
determinism  : seeded
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Will not state what it cannot support.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. claim extraction during generation with support checking
  2. unsupported-claim hedging or removal before delivery
  3. confidence-appropriate language calibration
  4. measured factual-error rate with target under 0.1% of claims

Expanded obligations:
  1. Implement claim extraction during generation with support checking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement unsupported-claim hedging or removal before delivery, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  3. Implement confidence-appropriate language calibration with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GDPval-AA v2 (Elo) target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured factual-error rate with target under 0.1% of claims
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of MMMU, so its p99 latency
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.factuality.factuality_gen@1
  cap.t15.factuality.factuality_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.citation.citation_formatting@1
      if unavailable: use the in-file conservative substitute for
      `citation_formatting` (documented, slower, lower quality) and set
      `degraded['citation_formatting']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t10.debate.debate_ensemble@1
      if unavailable: use the in-file conservative substitute for
      `debate_ensemble` (documented, slower, lower quality) and set
      `degraded['debate_ensemble']='local'`

  cap.t14.image.image_geometry@1
      if unavailable: use the in-file conservative substitute for
      `image_geometry` (documented, slower, lower quality) and set
      `degraded['image_geometry']='local'`

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
   3. [ 600 lines] Core implementation A - claim extraction during generation with support checking
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - unsupported-claim hedging or removal before delivery
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - confidence-appropriate language calibration
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured factual-error rate with target under 0.1% of claims
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.factuality.factuality_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0728_factuality_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0729-template-engine

**P0729 · `template_engine` — Template & Structured Output Engine** · [spec](PART_SPECS_T15.md#p0729-template-engine) · [self-contained txt](../prompts/P0729_template_engine.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0729  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0729 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0729  (29/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Template & Structured Output Engine
file         : parts/t15_generation/P0729_template_engine.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.template_engine
language     : TypeScript 5.7
capability   : cap.t15.template.template_engine@1
determinism  : seeded
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Fills structures exactly, every time.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. schema-driven output generation with guaranteed validity
  2. template-inheritance and slot-constraint handling
  3. partial-output and streaming-template support
  4. validity-rate measurement at 100% target

Expanded obligations:
  1. Implement schema-driven output generation with guaranteed validity, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against MMMU — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement template-inheritance and slot-constraint handling with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement partial-output and streaming-template support together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement validity-rate measurement at 100% target as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against GDPval-AA v2
     (Elo) — a regression on that benchmark is an automatic rejection of this
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.template.template_engine@1
  cap.t15.template.template_engine.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.factuality.factuality_gen@1
      if unavailable: use the in-file conservative substitute for
      `factuality_gen` (documented, slower, lower quality) and set
      `degraded['factuality_gen']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t10.induction.induction_engine@1
      if unavailable: use the in-file conservative substitute for
      `induction_engine` (documented, slower, lower quality) and set
      `degraded['induction_engine']='local'`

  cap.t14.prosody.prosody_paralinguistic@1
      if unavailable: use the in-file conservative substitute for
      `prosody_paralinguistic` (documented, slower, lower quality) and set
      `degraded['prosody_paralinguistic']='local'`

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
   3. [ 600 lines] Core implementation A - schema-driven output generation with guaranteed validity
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - template-inheritance and slot-constraint handling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partial-output and streaming-template support
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - validity-rate measurement at 100% target
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.template.template_engine@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0729_template_engine.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0730-diff-patch-output

**P0730 · `diff_patch_output` — Diff & Incremental Edit Output** · [spec](PART_SPECS_T15.md#p0730-diff-patch-output) · [self-contained txt](../prompts/P0730_diff_patch_output.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0730  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0730 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0730  (30/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Diff & Incremental Edit Output
file         : parts/t15_generation/P0730_diff_patch_output.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.diff_patch_output
language     : TypeScript 5.7
capability   : cap.t15.diff.diff_patch_output@1
determinism  : seeded
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Changes exactly what should change, nothing else.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. minimal-diff generation with context preservation
  2. multi-file coordinated edit output
  3. conflict detection against concurrent changes
  4. measured edit-precision (no unintended modifications)

Expanded obligations:
  1. Implement minimal-diff generation with context preservation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement multi-file coordinated edit output together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement conflict detection against concurrent changes as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement measured edit-precision (no unintended modifications), and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's MMMU
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.diff.diff_patch_output@1
  cap.t15.diff.diff_patch_output.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.template.template_engine@1
      if unavailable: use the in-file conservative substitute for
      `template_engine` (documented, slower, lower quality) and set
      `degraded['template_engine']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t10.commonsense.commonsense_engine@1
      if unavailable: use the in-file conservative substitute for
      `commonsense_engine` (documented, slower, lower quality) and set
      `degraded['commonsense_engine']='local'`

  cap.t14.medical.medical_imaging@1
      if unavailable: use the in-file conservative substitute for
      `medical_imaging` (documented, slower, lower quality) and set
      `degraded['medical_imaging']='local'`

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
   3. [ 600 lines] Core implementation A - minimal-diff generation with context preservation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - multi-file coordinated edit output
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conflict detection against concurrent changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured edit-precision (no unintended modifications)
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.diff.diff_patch_output@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0730_diff_patch_output.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0731-streaming-ux

**P0731 · `streaming_ux` — Progressive Output & Streaming Presentation** · [spec](PART_SPECS_T15.md#p0731-streaming-ux) · [self-contained txt](../prompts/P0731_streaming_ux.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0731  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0731 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0731  (31/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Progressive Output & Streaming Presentation
file         : parts/t15_generation/P0731_streaming_ux.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.streaming_ux
language     : TypeScript 5.7
capability   : cap.t15.streaming.streaming_ux@1
determinism  : seeded
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Useful output from the first second.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. outline-first then detail-fill streaming strategy
  2. stable-prefix guarantees so text does not rewrite itself
  3. partial-artifact rendering support
  4. perceived-latency measurement

Expanded obligations:
  1. Implement outline-first then detail-fill streaming strategy together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement stable-prefix guarantees so text does not rewrite itself as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement partial-artifact rendering support, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's MMMU target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement perceived-latency measurement with an explicit *a-priori* cost
     model. Before doing the work the part must be able to state the tokens,
     FLOPs and microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. This mechanism sits on the
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.streaming.streaming_ux@1
  cap.t15.streaming.streaming_ux.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.diff.diff_patch_output@1
      if unavailable: use the in-file conservative substitute for
      `diff_patch_output` (documented, slower, lower quality) and set
      `degraded['diff_patch_output']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t10.parallel.parallel_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `parallel_reasoning` (documented, slower, lower quality) and set
      `degraded['parallel_reasoning']='local'`

  cap.t14.perception.perception_uncertainty@1
      if unavailable: use the in-file conservative substitute for
      `perception_uncertainty` (documented, slower, lower quality) and set
      `degraded['perception_uncertainty']='local'`

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
   3. [ 600 lines] Core implementation A - outline-first then detail-fill streaming strategy
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - stable-prefix guarantees so text does not rewrite itself
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - partial-artifact rendering support
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - perceived-latency measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.streaming.streaming_ux@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0731_streaming_ux.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0732-interaction-design

**P0732 · `interaction_design` — Conversational Interaction Design** · [spec](PART_SPECS_T15.md#p0732-interaction-design) · [self-contained txt](../prompts/P0732_interaction_design.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0732  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0732 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0732  (32/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Conversational Interaction Design
file         : parts/t15_generation/P0732_interaction_design.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.interaction_design
language     : TypeScript 5.7
capability   : cap.t15.interaction.interaction_design@1
determinism  : seeded
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Knows when to ask, when to act and when to stop talking.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. turn-level decision policy (answer, clarify, act, confirm)
  2. response-length appropriateness calibration by request type
  3. proactive-suggestion policy without being annoying
  4. user-satisfaction evaluation results

Expanded obligations:
  1. Implement turn-level decision policy (answer, clarify, act, confirm) as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement response-length appropriateness calibration by request type,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's MMMU
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement proactive-suggestion policy without being annoying with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement user-satisfaction evaluation results together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.interaction.interaction_design@1
  cap.t15.interaction.interaction_design.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.streaming.streaming_ux@1
      if unavailable: use the in-file conservative substitute for
      `streaming_ux` (documented, slower, lower quality) and set
      `degraded['streaming_ux']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t10.multi.multi_step_arithmetic@1
      if unavailable: use the in-file conservative substitute for
      `multi_step_arithmetic` (documented, slower, lower quality) and set
      `degraded['multi_step_arithmetic']='local'`

  cap.t14.multimodal.multimodal_memory_perception@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_memory_perception` (documented, slower, lower quality) and
      set `degraded['multimodal_memory_perception']='local'`

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
   3. [ 600 lines] Core implementation A - turn-level decision policy (answer, clarify, act, confirm)
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - response-length appropriateness calibration by request type
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - proactive-suggestion policy without being annoying
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - user-satisfaction evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.interaction.interaction_design@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0732_interaction_design.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0733-personality-consistency

**P0733 · `personality_consistency` — Persona Consistency & Character Control** · [spec](PART_SPECS_T15.md#p0733-personality-consistency) · [self-contained txt](../prompts/P0733_personality_consistency.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0733  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0733 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0733  (33/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Persona Consistency & Character Control
file         : parts/t15_generation/P0733_personality_consistency.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.personality_consistency
language     : TypeScript 5.7
capability   : cap.t15.personality.personality_consistency@1
determinism  : seeded
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Stable, appropriate character across millions of turns.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. persona specification and adherence measurement
  2. consistency across long conversations and topic shifts
  3. appropriate-boundary maintenance within a persona
  4. consistency measurement via automated persona classifiers

Expanded obligations:
  1. Implement persona specification and adherence measurement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement consistency across long conversations and topic shifts with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of GDPval-AA v2 (Elo), so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement appropriate-boundary maintenance within a persona together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement consistency measurement via automated persona classifiers as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
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
  cap.t15.personality.personality_consistency@1
  cap.t15.personality.personality_consistency.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.interaction.interaction_design@1
      if unavailable: use the in-file conservative substitute for
      `interaction_design` (documented, slower, lower quality) and set
      `degraded['interaction_design']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t10.error.error_taxonomy@1
      if unavailable: use the in-file conservative substitute for
      `error_taxonomy` (documented, slower, lower quality) and set
      `degraded['error_taxonomy']='local'`

  cap.t14.perception.perception_speed@1
      if unavailable: use the in-file conservative substitute for
      `perception_speed` (documented, slower, lower quality) and set
      `degraded['perception_speed']='local'`

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
   3. [ 600 lines] Core implementation A - persona specification and adherence measurement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - consistency across long conversations and topic shifts
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - appropriate-boundary maintenance within a persona
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - consistency measurement via automated persona classifiers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.personality.personality_consistency@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0733_personality_consistency.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0734-emotional-intelligence

**P0734 · `emotional_intelligence` — Emotional & Social Appropriateness** · [spec](PART_SPECS_T15.md#p0734-emotional-intelligence) · [self-contained txt](../prompts/P0734_emotional_intelligence.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0734  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0734 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0734  (34/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Emotional & Social Appropriateness
file         : parts/t15_generation/P0734_emotional_intelligence.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.emotional_intelligence
language     : TypeScript 5.7
capability   : cap.t15.emotional.emotional_intelligence@1
determinism  : seeded
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Responds to people as people.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. emotional-context recognition and appropriate response calibration
  2. sensitive-topic handling with genuine care and correct boundaries
  3. cultural-appropriateness adaptation
  4. evaluation by human-interaction experts

Expanded obligations:
  1. Implement emotional-context recognition and appropriate response
     calibration with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement sensitive-topic handling with genuine care and correct
     boundaries together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against MMMU — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement cultural-appropriateness adaptation as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement evaluation by human-interaction experts, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of MMMU, so its p99 latency
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.emotional.emotional_intelligence@1
  cap.t15.emotional.emotional_intelligence.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.personality.personality_consistency@1
      if unavailable: use the in-file conservative substitute for
      `personality_consistency` (documented, slower, lower quality) and set
      `degraded['personality_consistency']='local'`

  cap.t10.search.search_controller@1
      if unavailable: use the in-file conservative substitute for
      `search_controller` (documented, slower, lower quality) and set
      `degraded['search_controller']='local'`

  cap.t14.vision.vision_tokenisation@1
      if unavailable: use the in-file conservative substitute for
      `vision_tokenisation` (documented, slower, lower quality) and set
      `degraded['vision_tokenisation']='local'`

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
   3. [ 600 lines] Core implementation A - emotional-context recognition and appropriate response calibrati
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - sensitive-topic handling with genuine care and correct boundarie
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cultural-appropriateness adaptation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - evaluation by human-interaction experts
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.emotional.emotional_intelligence@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0734_emotional_intelligence.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0735-pedagogical-generation

**P0735 · `pedagogical_generation` — Explanation & Teaching Generation** · [spec](PART_SPECS_T15.md#p0735-pedagogical-generation) · [self-contained txt](../prompts/P0735_pedagogical_generation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0735  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0735 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0735  (35/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Explanation & Teaching Generation
file         : parts/t15_generation/P0735_pedagogical_generation.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.pedagogical_generation
language     : TypeScript 5.7
capability   : cap.t15.pedagogical.pedagogical_generation@1
determinism  : seeded
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Explains at exactly the right level.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. audience-expertise modelling and level-appropriate explanation
  2. scaffolding, analogy and worked-example generation
  3. misconception anticipation and pre-emptive correction
  4. learning-outcome evaluation with real learners

Expanded obligations:
  1. Implement audience-expertise modelling and level-appropriate explanation
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement scaffolding, analogy and worked-example generation as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement misconception anticipation and pre-emptive correction, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  4. Implement learning-outcome evaluation with real learners with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
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
  cap.t15.pedagogical.pedagogical_generation@1
  cap.t15.pedagogical.pedagogical_generation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.emotional.emotional_intelligence@1
      if unavailable: use the in-file conservative substitute for
      `emotional_intelligence` (documented, slower, lower quality) and set
      `degraded['emotional_intelligence']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t10.self.self_critique@1
      if unavailable: use the in-file conservative substitute for
      `self_critique` (documented, slower, lower quality) and set
      `degraded['self_critique']='local'`

  cap.t14.visual.visual_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `visual_reasoning` (documented, slower, lower quality) and set
      `degraded['visual_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - audience-expertise modelling and level-appropriate explanation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - scaffolding, analogy and worked-example generation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - misconception anticipation and pre-emptive correction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - learning-outcome evaluation with real learners
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.pedagogical.pedagogical_generation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0735_pedagogical_generation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0736-creative-writing

**P0736 · `creative_writing` — Creative & Narrative Generation** · [spec](PART_SPECS_T15.md#p0736-creative-writing) · [self-contained txt](../prompts/P0736_creative_writing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0736  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0736 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0736  (36/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Creative & Narrative Generation
file         : parts/t15_generation/P0736_creative_writing.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.creative_writing
language     : TypeScript 5.7
capability   : cap.t15.creative.creative_writing@1
determinism  : seeded
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Actually good creative work, not competent filler.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. narrative structure, voice and pacing control
  2. character and world consistency across long works
  3. originality measurement and cliche avoidance
  4. evaluation by professional editors

Expanded obligations:
  1. Implement narrative structure, voice and pacing control as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement character and world consistency across long works, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of MMMU, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement originality measurement and cliche avoidance with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement evaluation by professional editors together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
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
                       p99 <= 34000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.creative.creative_writing@1
  cap.t15.creative.creative_writing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.pedagogical.pedagogical_generation@1
      if unavailable: use the in-file conservative substitute for
      `pedagogical_generation` (documented, slower, lower quality) and set
      `degraded['pedagogical_generation']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t10.abstraction.abstraction_engine@1
      if unavailable: use the in-file conservative substitute for
      `abstraction_engine` (documented, slower, lower quality) and set
      `degraded['abstraction_engine']='local'`

  cap.t14.speech.speech_recognition@1
      if unavailable: use the in-file conservative substitute for
      `speech_recognition` (documented, slower, lower quality) and set
      `degraded['speech_recognition']='local'`

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
   3. [ 600 lines] Core implementation A - narrative structure, voice and pacing control
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - character and world consistency across long works
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - originality measurement and cliche avoidance
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - evaluation by professional editors
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.creative.creative_writing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0736_creative_writing.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0737-technical-writing

**P0737 · `technical_writing` — Technical Documentation Generation** · [spec](PART_SPECS_T15.md#p0737-technical-writing) · [self-contained txt](../prompts/P0737_technical_writing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0737  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0737 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0737  (37/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Technical Documentation Generation
file         : parts/t15_generation/P0737_technical_writing.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.technical_writing
language     : TypeScript 5.7
capability   : cap.t15.technical.technical_writing@1
determinism  : seeded
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Documentation engineers actually use.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. task-oriented structure with executable examples
  2. completeness checking against API and behaviour inventories
  3. accuracy verification by executing every documented example
  4. usability evaluation with real developers

Expanded obligations:
  1. Implement task-oriented structure with executable examples, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of MMMU, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement completeness checking against API and behaviour inventories
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GDPval-AA v2 (Elo) — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement accuracy verification by executing every documented example
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement usability evaluation with real developers as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of GDPval-AA
     v2 (Elo), so its p99 latency assertion is part of the acceptance
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.technical.technical_writing@1
  cap.t15.technical.technical_writing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.creative.creative_writing@1
      if unavailable: use the in-file conservative substitute for
      `creative_writing` (documented, slower, lower quality) and set
      `degraded['creative_writing']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t10.spatial.spatial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `spatial_reasoning` (documented, slower, lower quality) and set
      `degraded['spatial_reasoning']='local'`

  cap.t14.scientific.scientific_imaging@1
      if unavailable: use the in-file conservative substitute for
      `scientific_imaging` (documented, slower, lower quality) and set
      `degraded['scientific_imaging']='local'`

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
   3. [ 600 lines] Core implementation A - task-oriented structure with executable examples
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - completeness checking against API and behaviour inventories
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accuracy verification by executing every documented example
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - usability evaluation with real developers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.technical.technical_writing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0737_technical_writing.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0738-legal-drafting

**P0738 · `legal_drafting` — Legal Document Drafting** · [spec](PART_SPECS_T15.md#p0738-legal-drafting) · [self-contained txt](../prompts/P0738_legal_drafting.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0738  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0738 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0738  (38/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Legal Document Drafting
file         : parts/t15_generation/P0738_legal_drafting.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.legal_drafting
language     : TypeScript 5.7
capability   : cap.t15.legal.legal_drafting@1
determinism  : seeded
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Drafts and redlines with lawyer-level precision.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. clause drafting with definition consistency and cross-reference integrity
  2. redline generation with rationale per change
  3. risk-flagging and alternative-language proposals
  4. target: highest first-turn redline quality, versus Opus 5 baseline

Expanded obligations:
  1. Implement clause drafting with definition consistency and
     cross-reference integrity with an explicit *a-priori* cost model. Before
     doing the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. Its contribution is measured
     against GDPval-AA v2 (Elo) — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement redline generation with rationale per change together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement risk-flagging and alternative-language proposals as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement target: highest first-turn redline quality, versus Opus 5
     baseline, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against MMMU — a
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.legal.legal_drafting@1
  cap.t15.legal.legal_drafting.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.technical.technical_writing@1
      if unavailable: use the in-file conservative substitute for
      `technical_writing` (documented, slower, lower quality) and set
      `degraded['technical_writing']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t10.chain.chain_compression@1
      if unavailable: use the in-file conservative substitute for
      `chain_compression` (documented, slower, lower quality) and set
      `degraded['chain_compression']='local'`

  cap.t14.multimodal.multimodal_context@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_context` (documented, slower, lower quality) and set
      `degraded['multimodal_context']='local'`

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
   3. [ 600 lines] Core implementation A - clause drafting with definition consistency and cross-reference 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - redline generation with rationale per change
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - risk-flagging and alternative-language proposals
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: highest first-turn redline quality, versus Opus 5 baseli
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.legal.legal_drafting@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0738_legal_drafting.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0739-financial-modelling-gen

**P0739 · `financial_modelling_gen` — Financial Model Generation** · [spec](PART_SPECS_T15.md#p0739-financial-modelling-gen) · [self-contained txt](../prompts/P0739_financial_modelling_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0739  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0739 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0739  (39/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Financial Model Generation
file         : parts/t15_generation/P0739_financial_modelling_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.financial_modelling_gen
language     : TypeScript 5.7
capability   : cap.t15.financial.financial_modelling_gen@1
determinism  : seeded
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Models that balance, tie out and survive audit.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structured model generation with formula integrity and traceability
  2. scenario and sensitivity analysis construction
  3. accounting-identity verification before delivery
  4. expert-analyst evaluation results

Expanded obligations:
  1. Implement structured model generation with formula integrity and
     traceability together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's MMMU target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement scenario and sensitivity analysis construction as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement accounting-identity verification before delivery, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  4. Implement expert-analyst evaluation results with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. Correctness here is
     what makes the tier's GDPval-AA v2 (Elo) target reachable; the part
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.financial.financial_modelling_gen@1
  cap.t15.financial.financial_modelling_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.legal.legal_drafting@1
      if unavailable: use the in-file conservative substitute for
      `legal_drafting` (documented, slower, lower quality) and set
      `degraded['legal_drafting']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t10.reasoning.reasoning_robustness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_robustness` (documented, slower, lower quality) and set
      `degraded['reasoning_robustness']='local'`

  cap.t14.visual.visual_search@1
      if unavailable: use the in-file conservative substitute for
      `visual_search` (documented, slower, lower quality) and set
      `degraded['visual_search']='local'`

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
   3. [ 600 lines] Core implementation A - structured model generation with formula integrity and traceabil
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - scenario and sensitivity analysis construction
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - accounting-identity verification before delivery
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - expert-analyst evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.financial.financial_modelling_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0739_financial_modelling_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0740-scientific-writing

**P0740 · `scientific_writing` — Scientific Manuscript & Protocol Generation** · [spec](PART_SPECS_T15.md#p0740-scientific-writing) · [self-contained txt](../prompts/P0740_scientific_writing.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0740  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0740 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0740  (40/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Scientific Manuscript & Protocol Generation
file         : parts/t15_generation/P0740_scientific_writing.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.scientific_writing
language     : TypeScript 5.7
capability   : cap.t15.scientific.scientific_writing@1
determinism  : seeded
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Publication-grade scientific writing.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. methods, results and discussion generation with statistical correctness
  2. protocol generation with reproducibility completeness
  3. citation and prior-work accuracy verification
  4. evaluation by domain scientists

Expanded obligations:
  1. Implement methods, results and discussion generation with statistical
     correctness as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of GDPval-AA v2 (Elo), so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement protocol generation with reproducibility completeness, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against MMMU — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement citation and prior-work accuracy verification with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GDPval-AA v2 (Elo) target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement evaluation by domain scientists together with its verification
     path, so that anything this mechanism produces can be independently
     re-checked *inside this same file* without contacting any other part.
     The checker must be cheap enough to run on every call in debug mode and
     must be wired into `selftest()`. This mechanism sits on the critical
     path of MMMU, so its p99 latency assertion is part of the acceptance
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.scientific.scientific_writing@1
  cap.t15.scientific.scientific_writing.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.financial.financial_modelling_gen@1
      if unavailable: use the in-file conservative substitute for
      `financial_modelling_gen` (documented, slower, lower quality) and set
      `degraded['financial_modelling_gen']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t10.reasoning.reasoning_transfer@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_transfer` (documented, slower, lower quality) and set
      `degraded['reasoning_transfer']='local'`

  cap.t14.legal.legal_docs_vision@1
      if unavailable: use the in-file conservative substitute for
      `legal_docs_vision` (documented, slower, lower quality) and set
      `degraded['legal_docs_vision']='local'`

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
   3. [ 600 lines] Core implementation A - methods, results and discussion generation with statistical corr
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - protocol generation with reproducibility completeness
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - citation and prior-work accuracy verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - evaluation by domain scientists
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.scientific.scientific_writing@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0740_scientific_writing.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0741-email-message-gen

**P0741 · `email_message_gen` — Correspondence & Message Generation** · [spec](PART_SPECS_T15.md#p0741-email-message-gen) · [self-contained txt](../prompts/P0741_email_message_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0741  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0741 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0741  (41/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Correspondence & Message Generation
file         : parts/t15_generation/P0741_email_message_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.email_message_gen
language     : TypeScript 5.7
capability   : cap.t15.email.email_message_gen@1
determinism  : seeded
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Professional communication that gets the response it needs.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. purpose-driven message construction with clear asks
  2. thread-context-appropriate length and tone
  3. stakeholder-sensitivity handling
  4. professional-reviewer evaluation results

Expanded obligations:
  1. Implement purpose-driven message construction with clear asks, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement thread-context-appropriate length and tone with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's GDPval-AA v2 (Elo) target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement stakeholder-sensitivity handling together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  4. Implement professional-reviewer evaluation results as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against GDPval-AA v2
     (Elo) — a regression on that benchmark is an automatic rejection of this
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.email.email_message_gen@1
  cap.t15.email.email_message_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.scientific.scientific_writing@1
      if unavailable: use the in-file conservative substitute for
      `scientific_writing` (documented, slower, lower quality) and set
      `degraded['scientific_writing']='local'`

  cap.t10.thought.thought_program_ir@1
      if unavailable: use the in-file conservative substitute for
      `thought_program_ir` (documented, slower, lower quality) and set
      `degraded['thought_program_ir']='local'`

  cap.t14.image.image_encoder@1
      if unavailable: use the in-file conservative substitute for
      `image_encoder` (documented, slower, lower quality) and set
      `degraded['image_encoder']='local'`

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
   3. [ 600 lines] Core implementation A - purpose-driven message construction with clear asks
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - thread-context-appropriate length and tone
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - stakeholder-sensitivity handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - professional-reviewer evaluation results
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.email.email_message_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0741_email_message_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0742-summarisation-gen

**P0742 · `summarisation_gen` — Summarisation & Distillation** · [spec](PART_SPECS_T15.md#p0742-summarisation-gen) · [self-contained txt](../prompts/P0742_summarisation_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0742  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0742 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0742  (42/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Summarisation & Distillation
file         : parts/t15_generation/P0742_summarisation_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.summarisation_gen
language     : TypeScript 5.7
capability   : cap.t15.summarisation.summarisation_gen@1
determinism  : seeded
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Shorter, and still true.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. extractive/abstractive hybrid with faithfulness guarantees
  2. audience and purpose-targeted summarisation
  3. omission-importance analysis (what was left out and why)
  4. faithfulness and coverage measurement

Expanded obligations:
  1. Implement extractive/abstractive hybrid with faithfulness guarantees
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement audience and purpose-targeted summarisation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  3. Implement omission-importance analysis (what was left out and why) as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  4. Implement faithfulness and coverage measurement, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.summarisation.summarisation_gen@1
  cap.t15.summarisation.summarisation_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.email.email_message_gen@1
      if unavailable: use the in-file conservative substitute for
      `email_message_gen` (documented, slower, lower quality) and set
      `degraded['email_message_gen']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t10.self.self_consistency@1
      if unavailable: use the in-file conservative substitute for
      `self_consistency` (documented, slower, lower quality) and set
      `degraded['self_consistency']='local'`

  cap.t14.scene.scene_graph@1
      if unavailable: use the in-file conservative substitute for
      `scene_graph` (documented, slower, lower quality) and set
      `degraded['scene_graph']='local'`

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
   3. [ 600 lines] Core implementation A - extractive/abstractive hybrid with faithfulness guarantees
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - audience and purpose-targeted summarisation
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - omission-importance analysis (what was left out and why)
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - faithfulness and coverage measurement
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.summarisation.summarisation_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0742_summarisation_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0743-structured-data-gen

**P0743 · `structured_data_gen` — Structured Data & Schema Output** · [spec](PART_SPECS_T15.md#p0743-structured-data-gen) · [self-contained txt](../prompts/P0743_structured_data_gen.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0743  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0743 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0743  (43/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Structured Data & Schema Output
file         : parts/t15_generation/P0743_structured_data_gen.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.structured_data_gen
language     : TypeScript 5.7
capability   : cap.t15.structured.structured_data_gen@1
determinism  : seeded
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Machine-consumable output that always validates.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. JSON/YAML/CSV/XML generation with schema conformance
  2. type, constraint and referential-integrity enforcement
  3. large-output streaming with validity maintained
  4. validity-rate measurement at 100% target

Expanded obligations:
  1. Implement JSON/YAML/CSV/XML generation with schema conformance together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of MMMU, so its p99 latency assertion is part of the
     acceptance criteria, not an optional extra.
  2. Implement type, constraint and referential-integrity enforcement as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  3. Implement large-output streaming with validity maintained, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement validity-rate measurement at 100% target with an explicit
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
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.structured.structured_data_gen@1
  cap.t15.structured.structured_data_gen.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.summarisation.summarisation_gen@1
      if unavailable: use the in-file conservative substitute for
      `summarisation_gen` (documented, slower, lower quality) and set
      `degraded['summarisation_gen']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t10.analogy.analogy_engine@1
      if unavailable: use the in-file conservative substitute for
      `analogy_engine` (documented, slower, lower quality) and set
      `degraded['analogy_engine']='local'`

  cap.t14.audio.audio_encoder@1
      if unavailable: use the in-file conservative substitute for
      `audio_encoder` (documented, slower, lower quality) and set
      `degraded['audio_encoder']='local'`

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
   3. [ 600 lines] Core implementation A - JSON/YAML/CSV/XML generation with schema conformance
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - type, constraint and referential-integrity enforcement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - large-output streaming with validity maintained
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - validity-rate measurement at 100% target
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.structured.structured_data_gen@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0743_structured_data_gen.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0744-artifact-versioning

**P0744 · `artifact_versioning` — Artifact Revision & Collaborative Editing** · [spec](PART_SPECS_T15.md#p0744-artifact-versioning) · [self-contained txt](../prompts/P0744_artifact_versioning.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0744  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0744 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0744  (44/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Artifact Revision & Collaborative Editing
file         : parts/t15_generation/P0744_artifact_versioning.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.artifact_versioning
language     : TypeScript 5.7
capability   : cap.t15.artifact.artifact_versioning@1
determinism  : seeded
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Iterates on work without losing anything.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. revision-request interpretation with scope determination
  2. surgical revision preserving unrelated content
  3. revision-history navigation and rollback
  4. measured revision-precision rate

Expanded obligations:
  1. Implement revision-request interpretation with scope determination as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against GDPval-AA v2 (Elo) — a regression on that benchmark is
     an automatic rejection of this part.
  2. Implement surgical revision preserving unrelated content, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement revision-history navigation and rollback with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of GDPval-AA v2 (Elo), so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured revision-precision rate together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.artifact.artifact_versioning@1
  cap.t15.artifact.artifact_versioning.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.structured.structured_data_gen@1
      if unavailable: use the in-file conservative substitute for
      `structured_data_gen` (documented, slower, lower quality) and set
      `degraded['structured_data_gen']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t10.temporal.temporal_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `temporal_reasoning` (documented, slower, lower quality) and set
      `degraded['temporal_reasoning']='local'`

  cap.t14.visual.visual_hallucination@1
      if unavailable: use the in-file conservative substitute for
      `visual_hallucination` (documented, slower, lower quality) and set
      `degraded['visual_hallucination']='local'`

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
   3. [ 600 lines] Core implementation A - revision-request interpretation with scope determination
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - surgical revision preserving unrelated content
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - revision-history navigation and rollback
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured revision-precision rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.artifact.artifact_versioning@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0744_artifact_versioning.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0745-output-localisation

**P0745 · `output_localisation` — Output Format Adaptation & Portability** · [spec](PART_SPECS_T15.md#p0745-output-localisation) · [self-contained txt](../prompts/P0745_output_localisation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0745  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0745 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0745  (45/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Output Format Adaptation & Portability
file         : parts/t15_generation/P0745_output_localisation.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.output_localisation
language     : TypeScript 5.7
capability   : cap.t15.output.output_localisation@1
determinism  : seeded
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
The same content, correct in every destination format.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. format-conversion with structure and meaning preservation
  2. destination-constraint handling (length, markup, character sets)
  3. conversion-fidelity verification
  4. fidelity measurement across format pairs

Expanded obligations:
  1. Implement format-conversion with structure and meaning preservation, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's MMMU
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  2. Implement destination-constraint handling (length, markup, character
     sets) with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of GDPval-AA v2
     (Elo), so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement conversion-fidelity verification together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement fidelity measurement across format pairs as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's GDPval-AA
     v2 (Elo) target reachable; the part therefore ships a microbenchmark
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
  cap.t15.output.output_localisation@1
  cap.t15.output.output_localisation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.artifact.artifact_versioning@1
      if unavailable: use the in-file conservative substitute for
      `artifact_versioning` (documented, slower, lower quality) and set
      `degraded['artifact_versioning']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t10.reasoning.reasoning_memory@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_memory` (documented, slower, lower quality) and set
      `degraded['reasoning_memory']='local'`

  cap.t14.code.code_screenshot@1
      if unavailable: use the in-file conservative substitute for
      `code_screenshot` (documented, slower, lower quality) and set
      `degraded['code_screenshot']='local'`

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
   3. [ 600 lines] Core implementation A - format-conversion with structure and meaning preservation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - destination-constraint handling (length, markup, character sets)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conversion-fidelity verification
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fidelity measurement across format pairs
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.output.output_localisation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0745_output_localisation.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0746-gdpval-harness

**P0746 · `gdpval_harness` — Knowledge Work Evaluation Harness** · [spec](PART_SPECS_T15.md#p0746-gdpval-harness) · [self-contained txt](../prompts/P0746_gdpval_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0746  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0746 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0746  (46/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Knowledge Work Evaluation Harness
file         : parts/t15_generation/P0746_gdpval_harness.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.gdpval_harness
language     : TypeScript 5.7
capability   : cap.t15.gdpval.gdpval_harness@1
determinism  : seeded
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Measures real economic work output quality.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. GDPval-AA style task harness with expert grading protocol
  2. Elo computation methodology with statistical rigor
  3. per-occupation capability breakdown
  4. target: 2650 Elo versus Opus 5's 1862

Expanded obligations:
  1. Implement GDPval-AA style task harness with expert grading protocol with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement Elo computation methodology with statistical rigor together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against MMMU — a regression on that benchmark is an automatic
     rejection of this part.
  3. Implement per-occupation capability breakdown as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's GDPval-AA v2 (Elo) target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement target: 2650 Elo versus Opus 5's 1862, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of MMMU, so its p99 latency
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
                       p99 <= 44000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.gdpval.gdpval_harness@1
  cap.t15.gdpval.gdpval_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.output.output_localisation@1
      if unavailable: use the in-file conservative substitute for
      `output_localisation` (documented, slower, lower quality) and set
      `degraded['output_localisation']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t10.reasoning.reasoning_faithfulness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_faithfulness` (documented, slower, lower quality) and set
      `degraded['reasoning_faithfulness']='local'`

  cap.t14.perception.perception_grounding_world@1
      if unavailable: use the in-file conservative substitute for
      `perception_grounding_world` (documented, slower, lower quality) and
      set `degraded['perception_grounding_world']='local'`

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
   3. [ 600 lines] Core implementation A - GDPval-AA style task harness with expert grading protocol
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - Elo computation methodology with statistical rigor
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-occupation capability breakdown
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: 2650 Elo versus Opus 5's 1862
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.gdpval.gdpval_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0746_gdpval_harness.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0747-artifact-quality-gate

**P0747 · `artifact_quality_gate` — Artifact Quality Gate** · [spec](PART_SPECS_T15.md#p0747-artifact-quality-gate) · [self-contained txt](../prompts/P0747_artifact_quality_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0747  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0747 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0747  (47/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Artifact Quality Gate
file         : parts/t15_generation/P0747_artifact_quality_gate.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.artifact_quality_gate
language     : TypeScript 5.7
capability   : cap.t15.artifact.artifact_quality_gate@1
determinism  : seeded
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Nothing substandard ever reaches a user.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-dimensional quality thresholds per artifact type
  2. automatic regeneration or explicit quality disclosure
  3. quality-score distribution monitoring over time
  4. measured user-rejection-rate reduction

Expanded obligations:
  1. Implement multi-dimensional quality thresholds per artifact type
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against MMMU — a regression on that benchmark
     is an automatic rejection of this part.
  2. Implement automatic regeneration or explicit quality disclosure as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement quality-score distribution monitoring over time, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of MMMU, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured user-rejection-rate reduction with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
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
  cap.t15.artifact.artifact_quality_gate@1
  cap.t15.artifact.artifact_quality_gate.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.gdpval.gdpval_harness@1
      if unavailable: use the in-file conservative substitute for
      `gdpval_harness` (documented, slower, lower quality) and set
      `degraded['gdpval_harness']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t10.subgoal.subgoal_caching@1
      if unavailable: use the in-file conservative substitute for
      `subgoal_caching` (documented, slower, lower quality) and set
      `degraded['subgoal_caching']='local'`

  cap.t14.receipt.receipt_finance_docs@1
      if unavailable: use the in-file conservative substitute for
      `receipt_finance_docs` (documented, slower, lower quality) and set
      `degraded['receipt_finance_docs']='local'`

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
   3. [ 600 lines] Core implementation A - multi-dimensional quality thresholds per artifact type
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - automatic regeneration or explicit quality disclosure
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - quality-score distribution monitoring over time
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured user-rejection-rate reduction
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.artifact.artifact_quality_gate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0747_artifact_quality_gate.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0748-generation-speed

**P0748 · `generation_speed` — Generation Latency & Cost Optimisation** · [spec](PART_SPECS_T15.md#p0748-generation-speed) · [self-contained txt](../prompts/P0748_generation_speed.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0748  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0748 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0748  (48/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Generation Latency & Cost Optimisation
file         : parts/t15_generation/P0748_generation_speed.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.generation_speed
language     : TypeScript 5.7
capability   : cap.t15.generation.generation_speed@1
determinism  : seeded
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
Publication quality at interactive speed.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. progressive-refinement generation with early usable output
  2. quality-tier selection under latency and cost budgets
  3. cached-component reuse for repeated structures
  4. measured latency reduction at matched quality

Expanded obligations:
  1. Implement progressive-refinement generation with early usable output as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's GDPval-AA v2 (Elo) target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement quality-tier selection under latency and cost budgets, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement cached-component reuse for repeated structures with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against GDPval-AA v2 (Elo) — a regression on
     that benchmark is an automatic rejection of this part.
  4. Implement measured latency reduction at matched quality together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.generation.generation_speed@1
  cap.t15.generation.generation_speed.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.artifact.artifact_quality_gate@1
      if unavailable: use the in-file conservative substitute for
      `artifact_quality_gate` (documented, slower, lower quality) and set
      `degraded['artifact_quality_gate']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t10.reasoning.reasoning_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_spec_doc` (documented, slower, lower quality) and set
      `degraded['reasoning_spec_doc']='local'`

  cap.t14.perception.perception_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `perception_spec_doc` (documented, slower, lower quality) and set
      `degraded['perception_spec_doc']='local'`

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
   3. [ 600 lines] Core implementation A - progressive-refinement generation with early usable output
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - quality-tier selection under latency and cost budgets
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - cached-component reuse for repeated structures
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured latency reduction at matched quality
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t15.generation.generation_speed@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0748_generation_speed.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0749-output-safety-filter

**P0749 · `output_safety_filter` — Output Safety & Policy Compliance Filter** · [spec](PART_SPECS_T15.md#p0749-output-safety-filter) · [self-contained txt](../prompts/P0749_output_safety_filter.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0749  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0749 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0749  (49/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Output Safety & Policy Compliance Filter
file         : parts/t15_generation/P0749_output_safety_filter.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.output_safety_filter
language     : TypeScript 5.7
capability   : cap.t15.output.output_safety_filter@1
determinism  : seeded
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
The final check before anything leaves the system.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mandatory T19 policy evaluation on all generated artifacts
  2. context-aware filtering avoiding over-refusal of legitimate work
  3. explanation generation when output is modified or withheld
  4. false-positive and false-negative rate measurement

Expanded obligations:
  1. Implement mandatory T19 policy evaluation on all generated artifacts,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     MMMU, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  2. Implement context-aware filtering avoiding over-refusal of legitimate
     work with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against GDPval-AA v2 (Elo) —
     a regression on that benchmark is an automatic rejection of this part.
  3. Implement explanation generation when output is modified or withheld
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's MMMU target reachable; the
     part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement false-positive and false-negative rate measurement as a
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
                       p99 <= 47000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.output.output_safety_filter@1
  cap.t15.output.output_safety_filter.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.generation.generation_speed@1
      if unavailable: use the in-file conservative substitute for
      `generation_speed` (documented, slower, lower quality) and set
      `degraded['generation_speed']='local'`

  cap.t10.outcome.outcome_verifier@1
      if unavailable: use the in-file conservative substitute for
      `outcome_verifier` (documented, slower, lower quality) and set
      `degraded['outcome_verifier']='local'`

  cap.t14.visual.visual_grounding@1
      if unavailable: use the in-file conservative substitute for
      `visual_grounding` (documented, slower, lower quality) and set
      `degraded['visual_grounding']='local'`

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
   3. [ 600 lines] Core implementation A - mandatory T19 policy evaluation on all generated artifacts
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - context-aware filtering avoiding over-refusal of legitimate work
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - explanation generation when output is modified or withheld
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
     exactly (capability == cap.t15.output.output_safety_filter@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0749_output_safety_filter.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0750-generation-spec-doc

**P0750 · `generation_spec_doc` — Generation Subsystem Specification** · [spec](PART_SPECS_T15.md#p0750-generation-spec-doc) · [self-contained txt](../prompts/P0750_generation_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0750  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0750 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0750  (50/50 of tier T15)
tier         : T15 — Generation, Artifacts & Interface Craft
title        : Generation Subsystem Specification
file         : parts/t15_generation/P0750_generation_spec_doc.ts          <-- create exactly this path, nothing else
module       : hyperion.t15.generation.generation_spec_doc
language     : TypeScript 5.7
capability   : cap.t15.generation.generation_spec_doc@1
determinism  : seeded
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : GDPval-AA v2 (Elo), MMMU

MISSION
-------
The authoritative description of all output capabilities.

Tier context:
  Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D,
  video, audio, and the taste model that judges them.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. capability register with measured quality per artifact type
  2. supported-format and verification-level matrix
  3. honest limitation documentation
  4. drift detection between claims and measurements

Expanded obligations:
  1. Implement capability register with measured quality per artifact type
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against GDPval-AA v2 (Elo) — a regression
     on that benchmark is an automatic rejection of this part.
  2. Implement supported-format and verification-level matrix together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's MMMU target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  3. Implement honest limitation documentation as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of GDPval-AA v2 (Elo), so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement drift detection between claims and measurements, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against MMMU — a regression on that benchmark
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
                       p99 <= 48000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t15.generation.generation_spec_doc@1
  cap.t15.generation.generation_spec_doc.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t15.output.output_safety_filter@1
      if unavailable: use the in-file conservative substitute for
      `output_safety_filter` (documented, slower, lower quality) and set
      `degraded['output_safety_filter']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t10.constraint.constraint_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `constraint_reasoning` (documented, slower, lower quality) and set
      `degraded['constraint_reasoning']='local'`

  cap.t14.video.video_tracking@1
      if unavailable: use the in-file conservative substitute for
      `video_tracking` (documented, slower, lower quality) and set
      `degraded['video_tracking']='local'`

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
   3. [ 600 lines] Core implementation A - capability register with measured quality per artifact type
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - supported-format and verification-level matrix
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - honest limitation documentation
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
     exactly (capability == cap.t15.generation.generation_spec_doc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t15_generation/P0750_generation_spec_doc.ts`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
