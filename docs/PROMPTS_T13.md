# HYPERION-Ω — Worker prompts · T13 · Agents, Tool Use & Computer Control

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

## PROMPT p0601-agent-loop

**P0601 · `agent_loop` — Core Agent Execution Loop** · [spec](PART_SPECS_T13.md#p0601-agent-loop) · [self-contained txt](../prompts/P0601_agent_loop.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0601  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0601 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0601  (1/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Core Agent Execution Loop
file         : parts/t13_agents/P0601_agent_loop.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_loop
language     : Python 3.13
capability   : cap.t13.agent.agent_loop@1
determinism  : io
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
The observe-think-act-verify cycle that runs for hours without drifting.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. loop with explicit state, budget and termination conditions
  2. progress detection and stagnation breaking
  3. checkpointing so a long task survives interruption
  4. measured task-completion rate on multi-hour horizons

Expanded obligations:
  1. Implement loop with explicit state, budget and termination conditions,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement progress detection and stagnation breaking with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement checkpointing so a long task survives interruption together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured task-completion rate on multi-hour horizons as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_loop@1
  cap.t13.agent.agent_loop.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

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

  cap.t07.freshness.freshness_manager@1
      if unavailable: use the in-file conservative substitute for
      `freshness_manager` (documented, slower, lower quality) and set
      `degraded['freshness_manager']='local'`

  cap.t10.numeric.numeric_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `numeric_reasoning` (documented, slower, lower quality) and set
      `degraded['numeric_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - loop with explicit state, budget and termination conditions
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - progress detection and stagnation breaking
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - checkpointing so a long task survives interruption
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured task-completion rate on multi-hour horizons
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_loop@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0601_agent_loop.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0602-tool-protocol

**P0602 · `tool_protocol` — Tool Definition & Invocation Protocol** · [spec](PART_SPECS_T13.md#p0602-tool-protocol) · [self-contained txt](../prompts/P0602_tool_protocol.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0602  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0602 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0602  (2/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Tool Definition & Invocation Protocol
file         : parts/t13_agents/P0602_tool_protocol.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.tool_protocol
language     : Python 3.13
capability   : cap.t13.tool.tool_protocol@1
determinism  : io
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
How the model discovers, calls and interprets tools.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tool schema format with typed arguments, errors and side-effect declarations
  2. argument validation and coercion with clear failure messages
  3. result normalisation into a uniform observation format
  4. protocol conformance test suite for tool authors

Expanded obligations:
  1. Implement tool schema format with typed arguments, errors and
     side-effect declarations with an explicit *a-priori* cost model. Before
     doing the work the part must be able to state the tokens, FLOPs and
     microseconds it intends to consume, and it must abort with an
     `OmegaError` in the 4xxx budget range rather than silently exceed the
     envelope's `budget` or `deadline_ns`. This mechanism sits on the
     critical path of Zapier AutomationBench, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement argument validation and coercion with clear failure messages
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Online-Mind2Web — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement result normalisation into a uniform observation format as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement protocol conformance test suite for tool authors, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
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
  cap.t13.tool.tool_protocol@1
  cap.t13.tool.tool_protocol.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_loop@1
      if unavailable: use the in-file conservative substitute for
      `agent_loop` (documented, slower, lower quality) and set
      `degraded['agent_loop']='local'`

  cap.t01.property.property_gen@1
      if unavailable: use the in-file conservative substitute for
      `property_gen` (documented, slower, lower quality) and set
      `degraded['property_gen']='local'`

  cap.t07.attention.attention_sink@1
      if unavailable: use the in-file conservative substitute for
      `attention_sink` (documented, slower, lower quality) and set
      `degraded['attention_sink']='local'`

  cap.t10.backtracking.backtracking@1
      if unavailable: use the in-file conservative substitute for
      `backtracking` (documented, slower, lower quality) and set
      `degraded['backtracking']='local'`

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
   3. [ 600 lines] Core implementation A - tool schema format with typed arguments, errors and side-effect 
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - argument validation and coercion with clear failure messages
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - result normalisation into a uniform observation format
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - protocol conformance test suite for tool authors
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.tool.tool_protocol@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0602_tool_protocol.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0603-tool-selection

**P0603 · `tool_selection` — Tool Selection & Discovery** · [spec](PART_SPECS_T13.md#p0603-tool-selection) · [self-contained txt](../prompts/P0603_tool_selection.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0603  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0603 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0603  (3/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Tool Selection & Discovery
file         : parts/t13_agents/P0603_tool_selection.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.tool_selection
language     : Python 3.13
capability   : cap.t13.tool.tool_selection@1
determinism  : io
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Picks the right tool from thousands without confusion.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. semantic tool retrieval scaling to 10000+ tools
  2. capability matching against the current subgoal
  3. selection-accuracy measurement and confusion analysis
  4. cost/latency-aware selection among equivalent tools

Expanded obligations:
  1. Implement semantic tool retrieval scaling to 10000+ tools together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement capability matching against the current subgoal as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement selection-accuracy measurement and confusion analysis, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     BrowseComp, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement cost/latency-aware selection among equivalent tools with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
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
                       p99 <= 42000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.tool.tool_selection@1
  cap.t13.tool.tool_selection.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.tool.tool_protocol@1
      if unavailable: use the in-file conservative substitute for
      `tool_protocol` (documented, slower, lower quality) and set
      `degraded['tool_protocol']='local'`

  cap.t01.link.link_validator@1
      if unavailable: use the in-file conservative substitute for
      `link_validator` (documented, slower, lower quality) and set
      `degraded['link_validator']='local'`

  cap.t07.persistence.persistence_layer@1
      if unavailable: use the in-file conservative substitute for
      `persistence_layer` (documented, slower, lower quality) and set
      `degraded['persistence_layer']='local'`

  cap.t10.question.question_asking@1
      if unavailable: use the in-file conservative substitute for
      `question_asking` (documented, slower, lower quality) and set
      `degraded['question_asking']='local'`

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
   3. [ 600 lines] Core implementation A - semantic tool retrieval scaling to 10000+ tools
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability matching against the current subgoal
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - selection-accuracy measurement and confusion analysis
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - cost/latency-aware selection among equivalent tools
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.tool.tool_selection@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0603_tool_selection.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0604-tool-composition

**P0604 · `tool_composition` — Tool Chaining & Composition Planner** · [spec](PART_SPECS_T13.md#p0604-tool-composition) · [self-contained txt](../prompts/P0604_tool_composition.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0604  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0604 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0604  (4/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Tool Chaining & Composition Planner
file         : parts/t13_agents/P0604_tool_composition.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.tool_composition
language     : Python 3.13
capability   : cap.t13.tool.tool_composition@1
determinism  : io
p99 budget   : 43000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Builds multi-tool pipelines and runs them in parallel.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. dataflow planning across tool calls with type compatibility checking
  2. parallel execution of independent calls (S6 contributor)
  3. intermediate-result management and transformation
  4. measured latency reduction from parallel composition

Expanded obligations:
  1. Implement dataflow planning across tool calls with type compatibility
     checking as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement parallel execution of independent calls (S6 contributor), and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     BrowseComp, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement intermediate-result management and transformation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement measured latency reduction from parallel composition together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
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
                       p99 <= 43000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.tool.tool_composition@1
  cap.t13.tool.tool_composition.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.tool.tool_selection@1
      if unavailable: use the in-file conservative substitute for
      `tool_selection` (documented, slower, lower quality) and set
      `degraded['tool_selection']='local'`

  cap.t01.rate.rate_limiter@1
      if unavailable: use the in-file conservative substitute for
      `rate_limiter` (documented, slower, lower quality) and set
      `degraded['rate_limiter']='local'`

  cap.t07.index.index_build_pipeline@1
      if unavailable: use the in-file conservative substitute for
      `index_build_pipeline` (documented, slower, lower quality) and set
      `degraded['index_build_pipeline']='local'`

  cap.t10.scratchpad.scratchpad_manager@1
      if unavailable: use the in-file conservative substitute for
      `scratchpad_manager` (documented, slower, lower quality) and set
      `degraded['scratchpad_manager']='local'`

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
   3. [ 600 lines] Core implementation A - dataflow planning across tool calls with type compatibility chec
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - parallel execution of independent calls (S6 contributor)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - intermediate-result management and transformation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured latency reduction from parallel composition
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.tool.tool_composition@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0604_tool_composition.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0605-mid-conversation-tools

**P0605 · `mid_conversation_tools` — Dynamic Tool Set Management** · [spec](PART_SPECS_T13.md#p0605-mid-conversation-tools) · [self-contained txt](../prompts/P0605_mid_conversation_tools.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0605  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0605 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0605  (5/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Dynamic Tool Set Management
file         : parts/t13_agents/P0605_mid_conversation_tools.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.mid_conversation_tools
language     : Python 3.13
capability   : cap.t13.mid.mid_conversation_tools@1
determinism  : io
p99 budget   : 44000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Tools appear and disappear mid-task without breaking the cache.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tool-set mutation with prompt-cache preservation
  2. capability re-planning when a tool disappears
  3. consistency verification across tool-set changes
  4. measured cache-hit preservation rate

Expanded obligations:
  1. Implement tool-set mutation with prompt-cache preservation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement capability re-planning when a tool disappears with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement consistency verification across tool-set changes together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured cache-hit preservation rate as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of OSWorld 2.0, so its p99
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
  cap.t13.mid.mid_conversation_tools@1
  cap.t13.mid.mid_conversation_tools.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.tool.tool_composition@1
      if unavailable: use the in-file conservative substitute for
      `tool_composition` (documented, slower, lower quality) and set
      `degraded['tool_composition']='local'`

  cap.t01.bootstrap.bootstrap_init@1
      if unavailable: use the in-file conservative substitute for
      `bootstrap_init` (documented, slower, lower quality) and set
      `degraded['bootstrap_init']='local'`

  cap.t07.cost.cost_aware_retrieval@1
      if unavailable: use the in-file conservative substitute for
      `cost_aware_retrieval` (documented, slower, lower quality) and set
      `degraded['cost_aware_retrieval']='local'`

  cap.t10.reasoning.reasoning_speed_proof@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_speed_proof` (documented, slower, lower quality) and set
      `degraded['reasoning_speed_proof']='local'`

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
   3. [ 600 lines] Core implementation A - tool-set mutation with prompt-cache preservation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability re-planning when a tool disappears
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - consistency verification across tool-set changes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured cache-hit preservation rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.mid.mid_conversation_tools@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0605_mid_conversation_tools.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0606-terminal-agent

**P0606 · `terminal_agent` — Terminal & Shell Operation Agent** · [spec](PART_SPECS_T13.md#p0606-terminal-agent) · [self-contained txt](../prompts/P0606_terminal_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0606  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0606 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0606  (6/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Terminal & Shell Operation Agent
file         : parts/t13_agents/P0606_terminal_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.terminal_agent
language     : Python 3.13
capability   : cap.t13.terminal.terminal_agent@1
determinism  : io
p99 budget   : 45000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Uses a real shell as competently as a senior engineer.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. command construction with quoting, escaping and platform awareness
  2. output parsing including interactive and paging behaviour
  3. destructive-command detection and confirmation gating
  4. target contribution to Terminal-Bench 98.5%

Expanded obligations:
  1. Implement command construction with quoting, escaping and platform
     awareness with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement output parsing including interactive and paging behaviour
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Online-Mind2Web target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement destructive-command detection and confirmation gating as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement target contribution to Terminal-Bench 98.5%, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
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
                       p99 <= 45000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.terminal.terminal_agent@1
  cap.t13.terminal.terminal_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.mid.mid_conversation_tools@1
      if unavailable: use the in-file conservative substitute for
      `mid_conversation_tools` (documented, slower, lower quality) and set
      `degraded['mid_conversation_tools']='local'`

  cap.t01.chacha.chacha_seeds@1
      if unavailable: use the in-file conservative substitute for
      `chacha_seeds` (documented, slower, lower quality) and set
      `degraded['chacha_seeds']='local'`

  cap.t07.context.context_window_manager@1
      if unavailable: use the in-file conservative substitute for
      `context_window_manager` (documented, slower, lower quality) and set
      `degraded['context_window_manager']='local'`

  cap.t10.process.process_verifier@1
      if unavailable: use the in-file conservative substitute for
      `process_verifier` (documented, slower, lower quality) and set
      `degraded['process_verifier']='local'`

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
   3. [ 600 lines] Core implementation A - command construction with quoting, escaping and platform awarene
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - output parsing including interactive and paging behaviour
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - destructive-command detection and confirmation gating
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target contribution to Terminal-Bench 98.5%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.terminal.terminal_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0606_terminal_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0607-filesystem-agent

**P0607 · `filesystem_agent` — Filesystem Navigation & Manipulation** · [spec](PART_SPECS_T13.md#p0607-filesystem-agent) · [self-contained txt](../prompts/P0607_filesystem_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0607  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0607 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0607  (7/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Filesystem Navigation & Manipulation
file         : parts/t13_agents/P0607_filesystem_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.filesystem_agent
language     : Python 3.13
capability   : cap.t13.filesystem.filesystem_agent@1
determinism  : io
p99 budget   : 46000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Explores and edits large file trees efficiently and safely.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. efficient exploration strategies avoiding full-tree scans
  2. atomic multi-file edit application with rollback
  3. permission and symlink hazard handling
  4. measured efficiency versus naive traversal

Expanded obligations:
  1. Implement efficient exploration strategies avoiding full-tree scans
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Online-Mind2Web target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement atomic multi-file edit application with rollback as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  3. Implement permission and symlink hazard handling, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured efficiency versus naive traversal with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Zapier AutomationBench target reachable;
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
                       p99 <= 46000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.filesystem.filesystem_agent@1
  cap.t13.filesystem.filesystem_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.terminal.terminal_agent@1
      if unavailable: use the in-file conservative substitute for
      `terminal_agent` (documented, slower, lower quality) and set
      `degraded['terminal_agent']='local'`

  cap.t01.mem.mem_layout@1
      if unavailable: use the in-file conservative substitute for
      `mem_layout` (documented, slower, lower quality) and set
      `degraded['mem_layout']='local'`

  cap.t07.vector.vector_index@1
      if unavailable: use the in-file conservative substitute for
      `vector_index` (documented, slower, lower quality) and set
      `degraded['vector_index']='local'`

  cap.t10.goal.goal_management@1
      if unavailable: use the in-file conservative substitute for
      `goal_management` (documented, slower, lower quality) and set
      `degraded['goal_management']='local'`

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
   3. [ 600 lines] Core implementation A - efficient exploration strategies avoiding full-tree scans
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - atomic multi-file edit application with rollback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - permission and symlink hazard handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured efficiency versus naive traversal
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.filesystem.filesystem_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0607_filesystem_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0608-browser-agent

**P0608 · `browser_agent` — Web Browser Automation Agent** · [spec](PART_SPECS_T13.md#p0608-browser-agent) · [self-contained txt](../prompts/P0608_browser_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0608  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0608 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0608  (8/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Web Browser Automation Agent
file         : parts/t13_agents/P0608_browser_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.browser_agent
language     : Python 3.13
capability   : cap.t13.browser.browser_agent@1
determinism  : io
p99 budget   : 47000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Uses the real web: forms, auth, dynamic content, verification.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. DOM plus visual understanding for element identification
  2. form filling, navigation, waiting and dynamic-content handling
  3. self-verification of achieved state after each action
  4. targets: Online-Mind2Web 98.5%, BrowseComp 99.0%

Expanded obligations:
  1. Implement DOM plus visual understanding for element identification as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement form filling, navigation, waiting and dynamic-content
     handling, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against BrowseComp
     — a regression on that benchmark is an automatic rejection of this part.
  3. Implement self-verification of achieved state after each action with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement targets: Online-Mind2Web 98.5%, BrowseComp 99.0% together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Online-Mind2Web, so its p99 latency assertion is
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
  cap.t13.browser.browser_agent@1
  cap.t13.browser.browser_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.filesystem.filesystem_agent@1
      if unavailable: use the in-file conservative substitute for
      `filesystem_agent` (documented, slower, lower quality) and set
      `degraded['filesystem_agent']='local'`

  cap.t01.hash.hash_maps@1
      if unavailable: use the in-file conservative substitute for
      `hash_maps` (documented, slower, lower quality) and set
      `degraded['hash_maps']='local'`

  cap.t07.citation.citation_grounding@1
      if unavailable: use the in-file conservative substitute for
      `citation_grounding` (documented, slower, lower quality) and set
      `degraded['citation_grounding']='local'`

  cap.t10.probabilistic.probabilistic_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `probabilistic_reasoning` (documented, slower, lower quality) and set
      `degraded['probabilistic_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - DOM plus visual understanding for element identification
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - form filling, navigation, waiting and dynamic-content handling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - self-verification of achieved state after each action
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - targets: Online-Mind2Web 98.5%, BrowseComp 99.0%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.browser.browser_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0608_browser_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0609-web-research

**P0609 · `web_research` — Deep Web Research Agent** · [spec](PART_SPECS_T13.md#p0609-web-research) · [self-contained txt](../prompts/P0609_web_research.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0609  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0609 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0609  (9/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Deep Web Research Agent
file         : parts/t13_agents/P0609_web_research.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.web_research
language     : Python 3.13
capability   : cap.t13.web.web_research@1
determinism  : io
p99 budget   : 48000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Finds the answer that requires reading forty pages.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. search-query strategy with iterative refinement
  2. source credibility assessment and cross-verification
  3. information synthesis with full citation tracking
  4. target: BrowseComp 99.0% versus Opus 5's 90.8%

Expanded obligations:
  1. Implement search-query strategy with iterative refinement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement source credibility assessment and cross-verification with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement information synthesis with full citation tracking together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Online-Mind2Web, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  4. Implement target: BrowseComp 99.0% versus Opus 5's 90.8% as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
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
  cap.t13.web.web_research@1
  cap.t13.web.web_research.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.browser.browser_agent@1
      if unavailable: use the in-file conservative substitute for
      `browser_agent` (documented, slower, lower quality) and set
      `degraded['browser_agent']='local'`

  cap.t01.selftest.selftest_harness@1
      if unavailable: use the in-file conservative substitute for
      `selftest_harness` (documented, slower, lower quality) and set
      `degraded['selftest_harness']='local'`

  cap.t07.memory.memory_compression_learned@1
      if unavailable: use the in-file conservative substitute for
      `memory_compression_learned` (documented, slower, lower quality) and
      set `degraded['memory_compression_learned']='local'`

  cap.t10.stopping.stopping_rules@1
      if unavailable: use the in-file conservative substitute for
      `stopping_rules` (documented, slower, lower quality) and set
      `degraded['stopping_rules']='local'`

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
   3. [ 600 lines] Core implementation A - search-query strategy with iterative refinement
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - source credibility assessment and cross-verification
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - information synthesis with full citation tracking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: BrowseComp 99.0% versus Opus 5's 90.8%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.web.web_research@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0609_web_research.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0610-computer-use-agent

**P0610 · `computer_use_agent` — Desktop Computer Use Agent** · [spec](PART_SPECS_T13.md#p0610-computer-use-agent) · [self-contained txt](../prompts/P0610_computer_use_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0610  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0610 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0610  (10/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Desktop Computer Use Agent
file         : parts/t13_agents/P0610_computer_use_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.computer_use_agent
language     : Python 3.13
capability   : cap.t13.computer.computer_use_agent@1
determinism  : io
p99 budget   : 49000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Operates arbitrary GUI applications through screenshots.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. screen understanding, element grounding and precise coordinate action
  2. keyboard/mouse action sequencing with verification after each step
  3. application-state tracking and error recovery
  4. target: OSWorld 2.0 95.5% versus Opus 5's 70.5%

Expanded obligations:
  1. Implement screen understanding, element grounding and precise coordinate
     action with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Zapier
     AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement keyboard/mouse action sequencing with verification after each
     step together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of
     Online-Mind2Web, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement application-state tracking and error recovery as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement target: OSWorld 2.0 95.5% versus Opus 5's 70.5%, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's BrowseComp target reachable;
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
                       p99 <= 49000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.computer.computer_use_agent@1
  cap.t13.computer.computer_use_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.web.web_research@1
      if unavailable: use the in-file conservative substitute for
      `web_research` (documented, slower, lower quality) and set
      `degraded['web_research']='local'`

  cap.t01.version.version_semver@1
      if unavailable: use the in-file conservative substitute for
      `version_semver` (documented, slower, lower quality) and set
      `degraded['version_semver']='local'`

  cap.t07.memory.memory_gc@1
      if unavailable: use the in-file conservative substitute for
      `memory_gc` (documented, slower, lower quality) and set
      `degraded['memory_gc']='local'`

  cap.t10.assumption.assumption_tracking@1
      if unavailable: use the in-file conservative substitute for
      `assumption_tracking` (documented, slower, lower quality) and set
      `degraded['assumption_tracking']='local'`

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
   3. [ 600 lines] Core implementation A - screen understanding, element grounding and precise coordinate a
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - keyboard/mouse action sequencing with verification after each st
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - application-state tracking and error recovery
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: OSWorld 2.0 95.5% versus Opus 5's 70.5%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.computer.computer_use_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0610_computer_use_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0611-gui-grounding

**P0611 · `gui_grounding` — GUI Element Grounding & Interaction** · [spec](PART_SPECS_T13.md#p0611-gui-grounding) · [self-contained txt](../prompts/P0611_gui_grounding.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0611  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0611 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0611  (11/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : GUI Element Grounding & Interaction
file         : parts/t13_agents/P0611_gui_grounding.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.gui_grounding
language     : Python 3.13
capability   : cap.t13.gui.gui_grounding@1
determinism  : io
p99 budget   : 3000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Clicks the right pixel, every time.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. visual element detection with role and state inference
  2. accessibility-tree fusion where available
  3. coordinate-precision measurement and calibration across resolutions
  4. grounding accuracy measurement on GUI benchmark suites

Expanded obligations:
  1. Implement visual element detection with role and state inference
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Online-Mind2Web, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  2. Implement accessibility-tree fusion where available as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against OSWorld 2.0 — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement coordinate-precision measurement and calibration across
     resolutions, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement grounding accuracy measurement on GUI benchmark suites with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
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
                       p99 <= 3000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.gui.gui_grounding@1
  cap.t13.gui.gui_grounding.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.computer.computer_use_agent@1
      if unavailable: use the in-file conservative substitute for
      `computer_use_agent` (documented, slower, lower quality) and set
      `degraded['computer_use_agent']='local'`

  cap.t01.budget.budget_ledger@1
      if unavailable: use the in-file conservative substitute for
      `budget_ledger` (documented, slower, lower quality) and set
      `degraded['budget_ledger']='local'`

  cap.t07.memory.memory_audit@1
      if unavailable: use the in-file conservative substitute for
      `memory_audit` (documented, slower, lower quality) and set
      `degraded['memory_audit']='local'`

  cap.t10.reasoning.reasoning_cost_model@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_cost_model` (documented, slower, lower quality) and set
      `degraded['reasoning_cost_model']='local'`

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
   3. [ 600 lines] Core implementation A - visual element detection with role and state inference
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - accessibility-tree fusion where available
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - coordinate-precision measurement and calibration across resoluti
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - grounding accuracy measurement on GUI benchmark suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.gui.gui_grounding@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0611_gui_grounding.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0612-mobile-agent

**P0612 · `mobile_agent` — Mobile Device Automation** · [spec](PART_SPECS_T13.md#p0612-mobile-agent) · [self-contained txt](../prompts/P0612_mobile_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0612  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0612 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0612  (12/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Mobile Device Automation
file         : parts/t13_agents/P0612_mobile_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.mobile_agent
language     : Python 3.13
capability   : cap.t13.mobile.mobile_agent@1
determinism  : io
p99 budget   : 4000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Operates phone and tablet interfaces natively.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. touch-gesture action space including swipe, pinch and long-press
  2. mobile-app state tracking across activities
  3. platform-specific convention handling
  4. task-success measurement on mobile benchmark suites

Expanded obligations:
  1. Implement touch-gesture action space including swipe, pinch and
     long-press as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement mobile-app state tracking across activities, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's BrowseComp target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement platform-specific convention handling with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement task-success measurement on mobile benchmark suites together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
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
  cap.t13.mobile.mobile_agent@1
  cap.t13.mobile.mobile_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.gui.gui_grounding@1
      if unavailable: use the in-file conservative substitute for
      `gui_grounding` (documented, slower, lower quality) and set
      `degraded['gui_grounding']='local'`

  cap.t01.compression.compression@1
      if unavailable: use the in-file conservative substitute for
      `compression` (documented, slower, lower quality) and set
      `degraded['compression']='local'`

  cap.t07.streaming.streaming_ingest@1
      if unavailable: use the in-file conservative substitute for
      `streaming_ingest` (documented, slower, lower quality) and set
      `degraded['streaming_ingest']='local'`

  cap.t10.collective.collective_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `collective_reasoning` (documented, slower, lower quality) and set
      `degraded['collective_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - touch-gesture action space including swipe, pinch and long-press
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - mobile-app state tracking across activities
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - platform-specific convention handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - task-success measurement on mobile benchmark suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.mobile.mobile_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0612_mobile_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0613-api-agent

**P0613 · `api_agent` — REST/GraphQL API Integration Agent** · [spec](PART_SPECS_T13.md#p0613-api-agent) · [self-contained txt](../prompts/P0613_api_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0613  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0613 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0613  (13/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : REST/GraphQL API Integration Agent
file         : parts/t13_agents/P0613_api_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.api_agent
language     : Python 3.13
capability   : cap.t13.api.api_agent@1
determinism  : io
p99 budget   : 5000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Uses arbitrary APIs correctly from their documentation.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. API-documentation comprehension into executable call plans
  2. authentication flow handling (OAuth, keys, tokens) with secret hygiene
  3. pagination, rate limiting and error-code handling
  4. success rate on unseen-API task suites

Expanded obligations:
  1. Implement API-documentation comprehension into executable call plans,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement authentication flow handling (OAuth, keys, tokens) with secret
     hygiene with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of Zapier
     AutomationBench, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement pagination, rate limiting and error-code handling together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement success rate on unseen-API task suites as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's OSWorld 2.0 target reachable;
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
                       p99 <= 5000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.api.api_agent@1
  cap.t13.api.api_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.mobile.mobile_agent@1
      if unavailable: use the in-file conservative substitute for
      `mobile_agent` (documented, slower, lower quality) and set
      `degraded['mobile_agent']='local'`

  cap.t01.blake3.blake3_hash@1
      if unavailable: use the in-file conservative substitute for
      `blake3_hash` (documented, slower, lower quality) and set
      `degraded['blake3_hash']='local'`

  cap.t07.kv.kv_compression_runtime@1
      if unavailable: use the in-file conservative substitute for
      `kv_compression_runtime` (documented, slower, lower quality) and set
      `degraded['kv_compression_runtime']='local'`

  cap.t10.beam.beam_pruning@1
      if unavailable: use the in-file conservative substitute for
      `beam_pruning` (documented, slower, lower quality) and set
      `degraded['beam_pruning']='local'`

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
   3. [ 600 lines] Core implementation A - API-documentation comprehension into executable call plans
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - authentication flow handling (OAuth, keys, tokens) with secret h
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - pagination, rate limiting and error-code handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - success rate on unseen-API task suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.api.api_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0613_api_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0614-database-agent

**P0614 · `database_agent` — Database Query & Administration Agent** · [spec](PART_SPECS_T13.md#p0614-database-agent) · [self-contained txt](../prompts/P0614_database_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0614  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0614 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0614  (14/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Database Query & Administration Agent
file         : parts/t13_agents/P0614_database_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.database_agent
language     : Python 3.13
capability   : cap.t13.database.database_agent@1
determinism  : io
p99 budget   : 6000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Writes correct SQL against schemas it has never seen.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. schema exploration and semantic understanding
  2. query construction with correctness verification before execution
  3. migration authoring with rollback plans
  4. accuracy measurement on text-to-SQL and admin task suites

Expanded obligations:
  1. Implement schema exploration and semantic understanding with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  2. Implement query construction with correctness verification before
     execution together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against Online-Mind2Web — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement migration authoring with rollback plans as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's OSWorld 2.0
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  4. Implement accuracy measurement on text-to-SQL and admin task suites, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     BrowseComp, so its p99 latency assertion is part of the acceptance
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
                       p99 <= 6000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.database.database_agent@1
  cap.t13.database.database_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.api.api_agent@1
      if unavailable: use the in-file conservative substitute for
      `api_agent` (documented, slower, lower quality) and set
      `degraded['api_agent']='local'`

  cap.t01.alloc.alloc_arena@1
      if unavailable: use the in-file conservative substitute for
      `alloc_arena` (documented, slower, lower quality) and set
      `degraded['alloc_arena']='local'`

  cap.t07.forgetting.forgetting_policy@1
      if unavailable: use the in-file conservative substitute for
      `forgetting_policy` (documented, slower, lower quality) and set
      `degraded['forgetting_policy']='local'`

  cap.t10.planning.planning_engine@1
      if unavailable: use the in-file conservative substitute for
      `planning_engine` (documented, slower, lower quality) and set
      `degraded['planning_engine']='local'`

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
   3. [ 600 lines] Core implementation A - schema exploration and semantic understanding
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - query construction with correctness verification before executio
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - migration authoring with rollback plans
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy measurement on text-to-SQL and admin task suites
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.database.database_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0614_database_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0615-business-automation

**P0615 · `business_automation` — Business Workflow Automation Agent** · [spec](PART_SPECS_T13.md#p0615-business-automation) · [self-contained txt](../prompts/P0615_business_automation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0615  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0615 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0615  (15/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Business Workflow Automation Agent
file         : parts/t13_agents/P0615_business_automation.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.business_automation
language     : Python 3.13
capability   : cap.t13.business.business_automation@1
determinism  : io
p99 budget   : 7000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Completes real office work end to end.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-app workflow orchestration with state tracking
  2. spreadsheet, CRM, email and document operation competence
  3. human-handoff points for judgment calls
  4. target: Zapier AutomationBench 92% versus Opus 5's 26.0%

Expanded obligations:
  1. Implement multi-app workflow orchestration with state tracking together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement spreadsheet, CRM, email and document operation competence as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement human-handoff points for judgment calls, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement target: Zapier AutomationBench 92% versus Opus 5's 26.0% with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Zapier AutomationBench — a
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
  cap.t13.business.business_automation@1
  cap.t13.business.business_automation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.database.database_agent@1
      if unavailable: use the in-file conservative substitute for
      `database_agent` (documented, slower, lower quality) and set
      `degraded['database_agent']='local'`

  cap.t01.bitset.bitset_rank@1
      if unavailable: use the in-file conservative substitute for
      `bitset_rank` (documented, slower, lower quality) and set
      `degraded['bitset_rank']='local'`

  cap.t07.reranker.reranker_model@1
      if unavailable: use the in-file conservative substitute for
      `reranker_model` (documented, slower, lower quality) and set
      `degraded['reranker_model']='local'`

  cap.t10.counterfactual.counterfactual_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `counterfactual_reasoning` (documented, slower, lower quality) and set
      `degraded['counterfactual_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - multi-app workflow orchestration with state tracking
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - spreadsheet, CRM, email and document operation competence
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - human-handoff points for judgment calls
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - target: Zapier AutomationBench 92% versus Opus 5's 26.0%
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.business.business_automation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0615_business_automation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0616-spreadsheet-agent

**P0616 · `spreadsheet_agent` — Spreadsheet & Tabular Data Agent** · [spec](PART_SPECS_T13.md#p0616-spreadsheet-agent) · [self-contained txt](../prompts/P0616_spreadsheet_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0616  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0616 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0616  (16/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Spreadsheet & Tabular Data Agent
file         : parts/t13_agents/P0616_spreadsheet_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.spreadsheet_agent
language     : Python 3.13
capability   : cap.t13.spreadsheet.spreadsheet_agent@1
determinism  : io
p99 budget   : 8000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Handles real workbooks: formulas, pivots, errors, scale.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. formula construction and dependency reasoning
  2. data cleaning, reconciliation and anomaly detection
  3. large-workbook handling without loading everything into context
  4. accuracy measurement on spreadsheet task benchmarks

Expanded obligations:
  1. Implement formula construction and dependency reasoning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement data cleaning, reconciliation and anomaly detection, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     This mechanism sits on the critical path of BrowseComp, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement large-workbook handling without loading everything into
     context with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  4. Implement accuracy measurement on spreadsheet task benchmarks together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
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
                       p99 <= 8000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.spreadsheet.spreadsheet_agent@1
  cap.t13.spreadsheet.spreadsheet_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.business.business_automation@1
      if unavailable: use the in-file conservative substitute for
      `business_automation` (documented, slower, lower quality) and set
      `degraded['business_automation']='local'`

  cap.t01.metrics.metrics_core@1
      if unavailable: use the in-file conservative substitute for
      `metrics_core` (documented, slower, lower quality) and set
      `degraded['metrics_core']='local'`

  cap.t07.belief.belief_revision@1
      if unavailable: use the in-file conservative substitute for
      `belief_revision` (documented, slower, lower quality) and set
      `degraded['belief_revision']='local'`

  cap.t10.difficulty.difficulty_estimation@1
      if unavailable: use the in-file conservative substitute for
      `difficulty_estimation` (documented, slower, lower quality) and set
      `degraded['difficulty_estimation']='local'`

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
   3. [ 600 lines] Core implementation A - formula construction and dependency reasoning
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - data cleaning, reconciliation and anomaly detection
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - large-workbook handling without loading everything into context
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy measurement on spreadsheet task benchmarks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.spreadsheet.spreadsheet_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0616_spreadsheet_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0617-document-workflow

**P0617 · `document_workflow` — Document Processing Workflow Agent** · [spec](PART_SPECS_T13.md#p0617-document-workflow) · [self-contained txt](../prompts/P0617_document_workflow.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0617  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0617 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0617  (17/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Document Processing Workflow Agent
file         : parts/t13_agents/P0617_document_workflow.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.document_workflow
language     : Python 3.13
capability   : cap.t13.document.document_workflow@1
determinism  : io
p99 budget   : 9000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Reads, edits and produces business documents faithfully.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. multi-format document parsing with layout and structure preservation
  2. tracked-change and comment authoring
  3. template-conformant document generation
  4. fidelity measurement on document-task corpora

Expanded obligations:
  1. Implement multi-format document parsing with layout and structure
     preservation, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. This mechanism sits on the critical path of
     BrowseComp, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement tracked-change and comment authoring with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement template-conformant document generation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement fidelity measurement on document-task corpora as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
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
                       p99 <= 9000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.document.document_workflow@1
  cap.t13.document.document_workflow.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.spreadsheet.spreadsheet_agent@1
      if unavailable: use the in-file conservative substitute for
      `spreadsheet_agent` (documented, slower, lower quality) and set
      `degraded['spreadsheet_agent']='local'`

  cap.t01.capability.capability_gate@1
      if unavailable: use the in-file conservative substitute for
      `capability_gate` (documented, slower, lower quality) and set
      `degraded['capability_gate']='local'`

  cap.t07.retrieval.retrieval_cache@1
      if unavailable: use the in-file conservative substitute for
      `retrieval_cache` (documented, slower, lower quality) and set
      `degraded['retrieval_cache']='local'`

  cap.t10.evidence.evidence_integration@1
      if unavailable: use the in-file conservative substitute for
      `evidence_integration` (documented, slower, lower quality) and set
      `degraded['evidence_integration']='local'`

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
   3. [ 600 lines] Core implementation A - multi-format document parsing with layout and structure preserva
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tracked-change and comment authoring
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - template-conformant document generation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - fidelity measurement on document-task corpora
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.document.document_workflow@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0617_document_workflow.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0618-email-communication

**P0618 · `email_communication` — Communication & Correspondence Agent** · [spec](PART_SPECS_T13.md#p0618-email-communication) · [self-contained txt](../prompts/P0618_email_communication.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0618  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0618 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0618  (18/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Communication & Correspondence Agent
file         : parts/t13_agents/P0618_email_communication.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.email_communication
language     : Python 3.13
capability   : cap.t13.email.email_communication@1
determinism  : io
p99 budget   : 10000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Writes and manages professional correspondence appropriately.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. thread comprehension and context-appropriate composition
  2. tone, formality and stakeholder-awareness control
  3. action-item extraction and follow-up tracking
  4. quality evaluation by professional reviewers

Expanded obligations:
  1. Implement thread comprehension and context-appropriate composition with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Zapier AutomationBench — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement tone, formality and stakeholder-awareness control together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement action-item extraction and follow-up tracking as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement quality evaluation by professional reviewers, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
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
                       p99 <= 10000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.email.email_communication@1
  cap.t13.email.email_communication.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.document.document_workflow@1
      if unavailable: use the in-file conservative substitute for
      `document_workflow` (documented, slower, lower quality) and set
      `degraded['document_workflow']='local'`

  cap.t01.unit.unit_dimensions@1
      if unavailable: use the in-file conservative substitute for
      `unit_dimensions` (documented, slower, lower quality) and set
      `degraded['unit_dimensions']='local'`

  cap.t07.user.user_model@1
      if unavailable: use the in-file conservative substitute for
      `user_model` (documented, slower, lower quality) and set
      `degraded['user_model']='local'`

  cap.t10.reasoning.reasoning_search_bench@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_search_bench` (documented, slower, lower quality) and set
      `degraded['reasoning_search_bench']='local'`

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
   3. [ 600 lines] Core implementation A - thread comprehension and context-appropriate composition
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - tone, formality and stakeholder-awareness control
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - action-item extraction and follow-up tracking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - quality evaluation by professional reviewers
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.email.email_communication@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0618_email_communication.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0619-scheduling-agent

**P0619 · `scheduling_agent` — Calendar & Coordination Agent** · [spec](PART_SPECS_T13.md#p0619-scheduling-agent) · [self-contained txt](../prompts/P0619_scheduling_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0619  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0619 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0619  (19/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Calendar & Coordination Agent
file         : parts/t13_agents/P0619_scheduling_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.scheduling_agent
language     : Python 3.13
capability   : cap.t13.scheduling.scheduling_agent@1
determinism  : io
p99 budget   : 11000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Solves the real constraint problem of many people's time.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. constraint-based scheduling across timezones and preferences
  2. negotiation-style multi-party coordination
  3. conflict detection and resolution proposals
  4. success rate on scheduling benchmark scenarios

Expanded obligations:
  1. Implement constraint-based scheduling across timezones and preferences
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Online-Mind2Web target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement negotiation-style multi-party coordination as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of OSWorld
     2.0, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement conflict detection and resolution proposals, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement success rate on scheduling benchmark scenarios with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 11000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.scheduling.scheduling_agent@1
  cap.t13.scheduling.scheduling_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.email.email_communication@1
      if unavailable: use the in-file conservative substitute for
      `email_communication` (documented, slower, lower quality) and set
      `degraded['email_communication']='local'`

  cap.t01.fs.fs_atomic@1
      if unavailable: use the in-file conservative substitute for
      `fs_atomic` (documented, slower, lower quality) and set
      `degraded['fs_atomic']='local'`

  cap.t07.memory.memory_sharding@1
      if unavailable: use the in-file conservative substitute for
      `memory_sharding` (documented, slower, lower quality) and set
      `degraded['memory_sharding']='local'`

  cap.t10.reasoning.reasoning_interpretability@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_interpretability` (documented, slower, lower quality) and
      set `degraded['reasoning_interpretability']='local'`

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
   3. [ 600 lines] Core implementation A - constraint-based scheduling across timezones and preferences
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - negotiation-style multi-party coordination
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conflict detection and resolution proposals
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - success rate on scheduling benchmark scenarios
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.scheduling.scheduling_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0619_scheduling_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0620-multi-agent-orchestration

**P0620 · `multi_agent_orchestration` — Multi-Agent Orchestration Framework** · [spec](PART_SPECS_T13.md#p0620-multi-agent-orchestration) · [self-contained txt](../prompts/P0620_multi_agent_orchestration.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0620  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0620 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0620  (20/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Multi-Agent Orchestration Framework
file         : parts/t13_agents/P0620_multi_agent_orchestration.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.multi_agent_orchestration
language     : Python 3.13
capability   : cap.t13.multi.multi_agent_orchestration@1
determinism  : io
p99 budget   : 12000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Runs 1000 sub-agents on one goal without chaos.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. role and responsibility assignment with clear interfaces
  2. work partitioning, dependency management and result integration
  3. conflict detection between concurrent agents' actions
  4. measured speedup and quality versus single-agent execution

Expanded obligations:
  1. Implement role and responsibility assignment with clear interfaces as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement work partitioning, dependency management and result
     integration, and make it correct under concurrency: at least 64
     in-flight `OmegaEnvelope`s must be able to traverse it simultaneously.
     No lock, mutex or borrow may be held across an `await` / `.await` /
     `yield` boundary, and the part must expose a contention counter so T09
     can attribute latency to it. Its contribution is measured against
     BrowseComp — a regression on that benchmark is an automatic rejection of
     this part.
  3. Implement conflict detection between concurrent agents' actions with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement measured speedup and quality versus single-agent execution
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Online-Mind2Web, so its p99
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
  cap.t13.multi.multi_agent_orchestration@1
  cap.t13.multi.multi_agent_orchestration.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.scheduling.scheduling_agent@1
      if unavailable: use the in-file conservative substitute for
      `scheduling_agent` (documented, slower, lower quality) and set
      `degraded['scheduling_agent']='local'`

  cap.t01.cbor.cbor_canonical@1
      if unavailable: use the in-file conservative substitute for
      `cbor_canonical` (documented, slower, lower quality) and set
      `degraded['cbor_canonical']='local'`

  cap.t07.kv.kv_dedup@1
      if unavailable: use the in-file conservative substitute for `kv_dedup`
      (documented, slower, lower quality) and set
      `degraded['kv_dedup']='local'`

  cap.t10.graph.graph_search@1
      if unavailable: use the in-file conservative substitute for
      `graph_search` (documented, slower, lower quality) and set
      `degraded['graph_search']='local'`

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
   3. [ 600 lines] Core implementation A - role and responsibility assignment with clear interfaces
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - work partitioning, dependency management and result integration
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - conflict detection between concurrent agents' actions
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured speedup and quality versus single-agent execution
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.multi.multi_agent_orchestration@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0620_multi_agent_orchestration.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0621-agent-communication

**P0621 · `agent_communication` — Inter-Agent Communication Protocol** · [spec](PART_SPECS_T13.md#p0621-agent-communication) · [self-contained txt](../prompts/P0621_agent_communication.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0621  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0621 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0621  (21/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Inter-Agent Communication Protocol
file         : parts/t13_agents/P0621_agent_communication.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_communication
language     : Python 3.13
capability   : cap.t13.agent.agent_communication@1
determinism  : io
p99 budget   : 13000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
How 1000 agents share findings without drowning each other.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. structured message protocol with typed intents
  2. shared-blackboard versus point-to-point policy
  3. information-relevance filtering to control communication volume
  4. measured coordination overhead and its reduction

Expanded obligations:
  1. Implement structured message protocol with typed intents, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement shared-blackboard versus point-to-point policy with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement information-relevance filtering to control communication
     volume together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of
     Online-Mind2Web, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  4. Implement measured coordination overhead and its reduction as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
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
                       p99 <= 13000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_communication@1
  cap.t13.agent.agent_communication.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.multi.multi_agent_orchestration@1
      if unavailable: use the in-file conservative substitute for
      `multi_agent_orchestration` (documented, slower, lower quality) and
      set `degraded['multi_agent_orchestration']='local'`

  cap.t01.clock.clock_time@1
      if unavailable: use the in-file conservative substitute for
      `clock_time` (documented, slower, lower quality) and set
      `degraded['clock_time']='local'`

  cap.t07.memory.memory_consolidation@1
      if unavailable: use the in-file conservative substitute for
      `memory_consolidation` (documented, slower, lower quality) and set
      `degraded['memory_consolidation']='local'`

  cap.t10.decomposition.decomposition@1
      if unavailable: use the in-file conservative substitute for
      `decomposition` (documented, slower, lower quality) and set
      `degraded['decomposition']='local'`

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
   3. [ 600 lines] Core implementation A - structured message protocol with typed intents
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - shared-blackboard versus point-to-point policy
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - information-relevance filtering to control communication volume
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured coordination overhead and its reduction
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_communication@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0621_agent_communication.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0622-agent-delegation

**P0622 · `agent_delegation` — Task Delegation & Subagent Spawning** · [spec](PART_SPECS_T13.md#p0622-agent-delegation) · [self-contained txt](../prompts/P0622_agent_delegation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0622  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0622 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0622  (22/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Task Delegation & Subagent Spawning
file         : parts/t13_agents/P0622_agent_delegation.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_delegation
language     : Python 3.13
capability   : cap.t13.agent.agent_delegation@1
determinism  : io
p99 budget   : 14000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Knows when to do it itself and when to delegate.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. delegation decision policy from task decomposability and cost
  2. subagent briefing quality (context sufficiency without bloat)
  3. result verification before accepting subagent output
  4. measured quality/cost improvement from delegation

Expanded obligations:
  1. Implement delegation decision policy from task decomposability and cost
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement subagent briefing quality (context sufficiency without bloat)
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Online-Mind2Web, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  3. Implement result verification before accepting subagent output as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement measured quality/cost improvement from delegation, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's BrowseComp target reachable;
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
                       p99 <= 14000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_delegation@1
  cap.t13.agent.agent_delegation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_communication@1
      if unavailable: use the in-file conservative substitute for
      `agent_communication` (documented, slower, lower quality) and set
      `degraded['agent_communication']='local'`

  cap.t01.bigint.bigint_modmath@1
      if unavailable: use the in-file conservative substitute for
      `bigint_modmath` (documented, slower, lower quality) and set
      `degraded['bigint_modmath']='local'`

  cap.t07.embedding.embedding_model@1
      if unavailable: use the in-file conservative substitute for
      `embedding_model` (documented, slower, lower quality) and set
      `degraded['embedding_model']='local'`

  cap.t10.program.program_synthesis_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `program_synthesis_reasoning` (documented, slower, lower quality) and
      set `degraded['program_synthesis_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - delegation decision policy from task decomposability and cost
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - subagent briefing quality (context sufficiency without bloat)
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - result verification before accepting subagent output
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured quality/cost improvement from delegation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_delegation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0622_agent_delegation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0623-agent-supervision

**P0623 · `agent_supervision` — Agent Supervision & Intervention** · [spec](PART_SPECS_T13.md#p0623-agent-supervision) · [self-contained txt](../prompts/P0623_agent_supervision.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0623  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0623 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0623  (23/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Supervision & Intervention
file         : parts/t13_agents/P0623_agent_supervision.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_supervision
language     : Python 3.13
capability   : cap.t13.agent.agent_supervision@1
determinism  : io
p99 budget   : 15000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Watches its own workers and steps in when needed.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. progress monitoring with stall and drift detection
  2. intervention policy: correct, restart, reassign or escalate
  3. supervision-overhead measurement
  4. measured improvement in long-horizon success rate

Expanded obligations:
  1. Implement progress monitoring with stall and drift detection together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Online-Mind2Web, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement intervention policy: correct, restart, reassign or escalate as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement supervision-overhead measurement, and make it correct under
     concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to
     traverse it simultaneously. No lock, mutex or borrow may be held across
     an `await` / `.await` / `yield` boundary, and the part must expose a
     contention counter so T09 can attribute latency to it. Correctness here
     is what makes the tier's BrowseComp target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured improvement in long-horizon success rate with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
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
                       p99 <= 15000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_supervision@1
  cap.t13.agent.agent_supervision.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_delegation@1
      if unavailable: use the in-file conservative substitute for
      `agent_delegation` (documented, slower, lower quality) and set
      `degraded['agent_delegation']='local'`

  cap.t01.logging.logging_events@1
      if unavailable: use the in-file conservative substitute for
      `logging_events` (documented, slower, lower quality) and set
      `degraded['logging_events']='local'`

  cap.t07.world.world_state_store@1
      if unavailable: use the in-file conservative substitute for
      `world_state_store` (documented, slower, lower quality) and set
      `degraded['world_state_store']='local'`

  cap.t10.meta.meta_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `meta_reasoning` (documented, slower, lower quality) and set
      `degraded['meta_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - progress monitoring with stall and drift detection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - intervention policy: correct, restart, reassign or escalate
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - supervision-overhead measurement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured improvement in long-horizon success rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_supervision@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0623_agent_supervision.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0624-consensus-agents

**P0624 · `consensus_agents` — Multi-Agent Consensus & Conflict Resolution** · [spec](PART_SPECS_T13.md#p0624-consensus-agents) · [self-contained txt](../prompts/P0624_consensus_agents.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0624  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0624 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0624  (24/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Multi-Agent Consensus & Conflict Resolution
file         : parts/t13_agents/P0624_consensus_agents.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.consensus_agents
language     : Python 3.13
capability   : cap.t13.consensus.consensus_agents@1
determinism  : io
p99 budget   : 16000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Resolves disagreement between agents with evidence.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. disagreement detection and structured resolution protocols
  2. evidence-weighted arbitration with tie-breaking rules
  3. deadlock prevention in negotiation
  4. measured decision quality versus single-agent decisions

Expanded obligations:
  1. Implement disagreement detection and structured resolution protocols as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement evidence-weighted arbitration with tie-breaking rules, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement deadlock prevention in negotiation with an explicit *a-priori*
     cost model. Before doing the work the part must be able to state the
     tokens, FLOPs and microseconds it intends to consume, and it must abort
     with an `OmegaError` in the 4xxx budget range rather than silently
     exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on
     the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured decision quality versus single-agent decisions
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Online-Mind2Web — a regression on that
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
                       p99 <= 16000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.consensus.consensus_agents@1
  cap.t13.consensus.consensus_agents.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_supervision@1
      if unavailable: use the in-file conservative substitute for
      `agent_supervision` (documented, slower, lower quality) and set
      `degraded['agent_supervision']='local'`

  cap.t01.checksum.checksum_verify@1
      if unavailable: use the in-file conservative substitute for
      `checksum_verify` (documented, slower, lower quality) and set
      `degraded['checksum_verify']='local'`

  cap.t07.subgraph.subgraph_memoize@1
      if unavailable: use the in-file conservative substitute for
      `subgraph_memoize` (documented, slower, lower quality) and set
      `degraded['subgraph_memoize']='local'`

  cap.t10.hypothesis.hypothesis_management@1
      if unavailable: use the in-file conservative substitute for
      `hypothesis_management` (documented, slower, lower quality) and set
      `degraded['hypothesis_management']='local'`

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
   3. [ 600 lines] Core implementation A - disagreement detection and structured resolution protocols
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - evidence-weighted arbitration with tie-breaking rules
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - deadlock prevention in negotiation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured decision quality versus single-agent decisions
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.consensus.consensus_agents@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0624_consensus_agents.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0625-environment-model

**P0625 · `environment_model` — Environment State Modelling & Prediction** · [spec](PART_SPECS_T13.md#p0625-environment-model) · [self-contained txt](../prompts/P0625_environment_model.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0625  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0625 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0625  (25/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Environment State Modelling & Prediction
file         : parts/t13_agents/P0625_environment_model.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.environment_model
language     : Python 3.13
capability   : cap.t13.environment.environment_model@1
determinism  : io
p99 budget   : 17000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Predicts what an action will do before doing it.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. action-effect prediction with uncertainty estimates
  2. state-divergence detection between predicted and observed
  3. model updating from observed outcomes
  4. prediction accuracy measurement across environments

Expanded obligations:
  1. Implement action-effect prediction with uncertainty estimates, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's BrowseComp target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  2. Implement state-divergence detection between predicted and observed with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Zapier AutomationBench, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement model updating from observed outcomes together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement prediction accuracy measurement across environments as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
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
                       p99 <= 17000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.environment.environment_model@1
  cap.t13.environment.environment_model.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.consensus.consensus_agents@1
      if unavailable: use the in-file conservative substitute for
      `consensus_agents` (documented, slower, lower quality) and set
      `degraded['consensus_agents']='local'`

  cap.t01.numeric.numeric_limits@1
      if unavailable: use the in-file conservative substitute for
      `numeric_limits` (documented, slower, lower quality) and set
      `degraded['numeric_limits']='local'`

  cap.t07.multimodal.multimodal_memory@1
      if unavailable: use the in-file conservative substitute for
      `multimodal_memory` (documented, slower, lower quality) and set
      `degraded['multimodal_memory']='local'`

  cap.t10.proof.proof_sketch@1
      if unavailable: use the in-file conservative substitute for
      `proof_sketch` (documented, slower, lower quality) and set
      `degraded['proof_sketch']='local'`

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
   3. [ 600 lines] Core implementation A - action-effect prediction with uncertainty estimates
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - state-divergence detection between predicted and observed
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - model updating from observed outcomes
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - prediction accuracy measurement across environments
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.environment.environment_model@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0625_environment_model.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0626-action-verification

**P0626 · `action_verification` — Post-Action Verification Loop** · [spec](PART_SPECS_T13.md#p0626-action-verification) · [self-contained txt](../prompts/P0626_action_verification.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0626  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0626 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0626  (26/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Post-Action Verification Loop
file         : parts/t13_agents/P0626_action_verification.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.action_verification
language     : Python 3.13
capability   : cap.t13.action.action_verification@1
determinism  : io
p99 budget   : 18000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Confirms every action achieved its intended effect.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. expected-effect specification per action and observation matching
  2. silent-failure detection (action reported success but did nothing)
  3. retry versus replan decision on verification failure
  4. measured reduction in undetected failures

Expanded obligations:
  1. Implement expected-effect specification per action and observation
     matching with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. This mechanism sits on the critical path of Zapier
     AutomationBench, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement silent-failure detection (action reported success but did
     nothing) together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against Online-Mind2Web — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement retry versus replan decision on verification failure as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured reduction in undetected failures, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
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
                       p99 <= 18000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.action.action_verification@1
  cap.t13.action.action_verification.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.environment.environment_model@1
      if unavailable: use the in-file conservative substitute for
      `environment_model` (documented, slower, lower quality) and set
      `degraded['environment_model']='local'`

  cap.t01.sandbox.sandbox_policy@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_policy` (documented, slower, lower quality) and set
      `degraded['sandbox_policy']='local'`

  cap.t07.context.context_budget_optimiser@1
      if unavailable: use the in-file conservative substitute for
      `context_budget_optimiser` (documented, slower, lower quality) and set
      `degraded['context_budget_optimiser']='local'`

  cap.t10.adversarial.adversarial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `adversarial_reasoning` (documented, slower, lower quality) and set
      `degraded['adversarial_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - expected-effect specification per action and observation matchin
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - silent-failure detection (action reported success but did nothin
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - retry versus replan decision on verification failure
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured reduction in undetected failures
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.action.action_verification@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0626_action_verification.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0627-error-recovery-agent

**P0627 · `error_recovery_agent` — Failure Recovery & Adaptation** · [spec](PART_SPECS_T13.md#p0627-error-recovery-agent) · [self-contained txt](../prompts/P0627_error_recovery_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0627  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0627 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0627  (27/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Failure Recovery & Adaptation
file         : parts/t13_agents/P0627_error_recovery_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.error_recovery_agent
language     : Python 3.13
capability   : cap.t13.error.error_recovery_agent@1
determinism  : io
p99 budget   : 19000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Recovers from unexpected states without human help.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. failure classification and recovery-strategy selection
  2. state restoration and safe-point rollback
  3. learned recovery patterns from past failures
  4. recovery success rate measurement on injected-failure scenarios

Expanded obligations:
  1. Implement failure classification and recovery-strategy selection
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Online-Mind2Web — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement state restoration and safe-point rollback as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Correctness here is what makes the tier's OSWorld 2.0
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement learned recovery patterns from past failures, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement recovery success rate measurement on injected-failure
     scenarios with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Zapier
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
                       p99 <= 19000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.error.error_recovery_agent@1
  cap.t13.error.error_recovery_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.action.action_verification@1
      if unavailable: use the in-file conservative substitute for
      `action_verification` (documented, slower, lower quality) and set
      `degraded['action_verification']='local'`

  cap.t01.abi.abi_result@1
      if unavailable: use the in-file conservative substitute for
      `abi_result` (documented, slower, lower quality) and set
      `degraded['abi_result']='local'`

  cap.t07.kv.kv_eviction@1
      if unavailable: use the in-file conservative substitute for
      `kv_eviction` (documented, slower, lower quality) and set
      `degraded['kv_eviction']='local'`

  cap.t10.tree.tree_search@1
      if unavailable: use the in-file conservative substitute for
      `tree_search` (documented, slower, lower quality) and set
      `degraded['tree_search']='local'`

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
   3. [ 600 lines] Core implementation A - failure classification and recovery-strategy selection
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - state restoration and safe-point rollback
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - learned recovery patterns from past failures
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - recovery success rate measurement on injected-failure scenarios
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.error.error_recovery_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0627_error_recovery_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0628-long-horizon-memory

**P0628 · `long_horizon_memory` — Long-Horizon Task Memory** · [spec](PART_SPECS_T13.md#p0628-long-horizon-memory) · [self-contained txt](../prompts/P0628_long_horizon_memory.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0628  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0628 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0628  (28/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Long-Horizon Task Memory
file         : parts/t13_agents/P0628_long_horizon_memory.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.long_horizon_memory
language     : Python 3.13
capability   : cap.t13.long.long_horizon_memory@1
determinism  : io
p99 budget   : 20000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Remembers everything relevant across a twelve-hour task.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. task-scoped memory with progress, decisions and dead ends recorded
  2. context compaction preserving decision-critical information
  3. resumption after interruption with full context restoration
  4. measured coherence over very long task horizons

Expanded obligations:
  1. Implement task-scoped memory with progress, decisions and dead ends
     recorded as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement context compaction preserving decision-critical information,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     BrowseComp, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement resumption after interruption with full context restoration
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Zapier AutomationBench — a
     regression on that benchmark is an automatic rejection of this part.
  4. Implement measured coherence over very long task horizons together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
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
                       p99 <= 20000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.long.long_horizon_memory@1
  cap.t13.long.long_horizon_memory.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.error.error_recovery_agent@1
      if unavailable: use the in-file conservative substitute for
      `error_recovery_agent` (documented, slower, lower quality) and set
      `degraded['error_recovery_agent']='local'`

  cap.t01.trace.trace_context@1
      if unavailable: use the in-file conservative substitute for
      `trace_context` (documented, slower, lower quality) and set
      `degraded['trace_context']='local'`

  cap.t07.procedural.procedural_memory@1
      if unavailable: use the in-file conservative substitute for
      `procedural_memory` (documented, slower, lower quality) and set
      `degraded['procedural_memory']='local'`

  cap.t10.debate.debate_ensemble@1
      if unavailable: use the in-file conservative substitute for
      `debate_ensemble` (documented, slower, lower quality) and set
      `degraded['debate_ensemble']='local'`

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
   3. [ 600 lines] Core implementation A - task-scoped memory with progress, decisions and dead ends record
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - context compaction preserving decision-critical information
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - resumption after interruption with full context restoration
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured coherence over very long task horizons
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.long.long_horizon_memory@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0628_long_horizon_memory.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0629-progress-tracking

**P0629 · `progress_tracking` — Progress Estimation & Reporting** · [spec](PART_SPECS_T13.md#p0629-progress-tracking) · [self-contained txt](../prompts/P0629_progress_tracking.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0629  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0629 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0629  (29/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Progress Estimation & Reporting
file         : parts/t13_agents/P0629_progress_tracking.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.progress_tracking
language     : Python 3.13
capability   : cap.t13.progress.progress_tracking@1
determinism  : io
p99 budget   : 21000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Honest answers to 'how much longer'.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. completion estimation from subtask structure and observed velocity
  2. milestone reporting with confidence intervals
  3. blocked-state detection and escalation
  4. estimation-accuracy measurement against actual completion

Expanded obligations:
  1. Implement completion estimation from subtask structure and observed
     velocity, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     BrowseComp, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement milestone reporting with confidence intervals with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  3. Implement blocked-state detection and escalation together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement estimation-accuracy measurement against actual completion as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
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
                       p99 <= 21000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.progress.progress_tracking@1
  cap.t13.progress.progress_tracking.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.long.long_horizon_memory@1
      if unavailable: use the in-file conservative substitute for
      `long_horizon_memory` (documented, slower, lower quality) and set
      `degraded['long_horizon_memory']='local'`

  cap.t01.fixed.fixed_point@1
      if unavailable: use the in-file conservative substitute for
      `fixed_point` (documented, slower, lower quality) and set
      `degraded['fixed_point']='local'`

  cap.t07.chunking.chunking_strategy@1
      if unavailable: use the in-file conservative substitute for
      `chunking_strategy` (documented, slower, lower quality) and set
      `degraded['chunking_strategy']='local'`

  cap.t10.induction.induction_engine@1
      if unavailable: use the in-file conservative substitute for
      `induction_engine` (documented, slower, lower quality) and set
      `degraded['induction_engine']='local'`

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
   3. [ 600 lines] Core implementation A - completion estimation from subtask structure and observed veloci
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - milestone reporting with confidence intervals
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blocked-state detection and escalation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - estimation-accuracy measurement against actual completion
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.progress.progress_tracking@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0629_progress_tracking.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0630-human-in-loop

**P0630 · `human_in_loop` — Human Handoff & Approval Workflow** · [spec](PART_SPECS_T13.md#p0630-human-in-loop) · [self-contained txt](../prompts/P0630_human_in_loop.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0630  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0630 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0630  (30/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Human Handoff & Approval Workflow
file         : parts/t13_agents/P0630_human_in_loop.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.human_in_loop
language     : Python 3.13
capability   : cap.t13.human.human_in_loop@1
determinism  : io
p99 budget   : 22000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Asks for permission at exactly the right moments.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. approval-requirement classification by reversibility and stakes
  2. context-sufficient approval requests (human can decide in seconds)
  3. asynchronous approval handling without blocking other work
  4. measured approval-quality and interruption-rate balance

Expanded obligations:
  1. Implement approval-requirement classification by reversibility and
     stakes with an explicit *a-priori* cost model. Before doing the work the
     part must be able to state the tokens, FLOPs and microseconds it intends
     to consume, and it must abort with an `OmegaError` in the 4xxx budget
     range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement context-sufficient approval requests (human can decide in
     seconds) together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Online-Mind2Web
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  3. Implement asynchronous approval handling without blocking other work as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement measured approval-quality and interruption-rate balance, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against BrowseComp
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
                       p99 <= 22000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.human.human_in_loop@1
  cap.t13.human.human_in_loop.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.progress.progress_tracking@1
      if unavailable: use the in-file conservative substitute for
      `progress_tracking` (documented, slower, lower quality) and set
      `degraded['progress_tracking']='local'`

  cap.t01.config.config_system@1
      if unavailable: use the in-file conservative substitute for
      `config_system` (documented, slower, lower quality) and set
      `degraded['config_system']='local'`

  cap.t07.memory.memory_encryption@1
      if unavailable: use the in-file conservative substitute for
      `memory_encryption` (documented, slower, lower quality) and set
      `degraded['memory_encryption']='local'`

  cap.t10.commonsense.commonsense_engine@1
      if unavailable: use the in-file conservative substitute for
      `commonsense_engine` (documented, slower, lower quality) and set
      `degraded['commonsense_engine']='local'`

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
   3. [ 600 lines] Core implementation A - approval-requirement classification by reversibility and stakes
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - context-sufficient approval requests (human can decide in second
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - asynchronous approval handling without blocking other work
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured approval-quality and interruption-rate balance
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.human.human_in_loop@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0630_human_in_loop.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0631-agent-safety-gate

**P0631 · `agent_safety_gate` — Agent Action Safety Gate** · [spec](PART_SPECS_T13.md#p0631-agent-safety-gate) · [self-contained txt](../prompts/P0631_agent_safety_gate.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0631  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0631 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0631  (31/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Action Safety Gate
file         : parts/t13_agents/P0631_agent_safety_gate.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_safety_gate
language     : Python 3.13
capability   : cap.t13.agent.agent_safety_gate@1
determinism  : io
p99 budget   : 23000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
The hard stop before anything irreversible happens.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. action classification: reversible, costly, irreversible, prohibited
  2. mandatory T19 gate consultation with fail-closed behaviour
  3. blast-radius estimation before execution
  4. verification that no prohibited action can bypass the gate

Expanded obligations:
  1. Implement action classification: reversible, costly, irreversible,
     prohibited together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Correctness here is what makes the tier's Online-Mind2Web
     target reachable; the part therefore ships a microbenchmark that stands
     in for that benchmark's inner loop.
  2. Implement mandatory T19 gate consultation with fail-closed behaviour as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  3. Implement blast-radius estimation before execution, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement verification that no prohibited action can bypass the gate
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 23000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_safety_gate@1
  cap.t13.agent.agent_safety_gate.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.human.human_in_loop@1
      if unavailable: use the in-file conservative substitute for
      `human_in_loop` (documented, slower, lower quality) and set
      `degraded['human_in_loop']='local'`

  cap.t01.determinism.determinism_replay@1
      if unavailable: use the in-file conservative substitute for
      `determinism_replay` (documented, slower, lower quality) and set
      `degraded['determinism_replay']='local'`

  cap.t07.tool.tool_result_cache@1
      if unavailable: use the in-file conservative substitute for
      `tool_result_cache` (documented, slower, lower quality) and set
      `degraded['tool_result_cache']='local'`

  cap.t10.parallel.parallel_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `parallel_reasoning` (documented, slower, lower quality) and set
      `degraded['parallel_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - action classification: reversible, costly, irreversible, prohibi
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - mandatory T19 gate consultation with fail-closed behaviour
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - blast-radius estimation before execution
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - verification that no prohibited action can bypass the gate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_safety_gate@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0631_agent_safety_gate.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0632-credential-management

**P0632 · `credential_management` — Credential & Permission Management** · [spec](PART_SPECS_T13.md#p0632-credential-management) · [self-contained txt](../prompts/P0632_credential_management.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0632  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0632 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0632  (32/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Credential & Permission Management
file         : parts/t13_agents/P0632_credential_management.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.credential_management
language     : Python 3.13
capability   : cap.t13.credential.credential_management@1
determinism  : io
p99 budget   : 24000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Uses secrets correctly and never leaks them.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. scoped credential acquisition with least-privilege defaults
  2. secret redaction from all logs, traces and model context
  3. credential-lifetime management and rotation handling
  4. leak-detection testing across all output channels

Expanded obligations:
  1. Implement scoped credential acquisition with least-privilege defaults as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement secret redaction from all logs, traces and model context, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against BrowseComp
     — a regression on that benchmark is an automatic rejection of this part.
  3. Implement credential-lifetime management and rotation handling with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  4. Implement leak-detection testing across all output channels together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Online-Mind2Web, so its p99 latency assertion is
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
  cap.t13.credential.credential_management@1
  cap.t13.credential.credential_management.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_safety_gate@1
      if unavailable: use the in-file conservative substitute for
      `agent_safety_gate` (documented, slower, lower quality) and set
      `degraded['agent_safety_gate']='local'`

  cap.t01.compat.compat_shims@1
      if unavailable: use the in-file conservative substitute for
      `compat_shims` (documented, slower, lower quality) and set
      `degraded['compat_shims']='local'`

  cap.t07.temporal.temporal_memory@1
      if unavailable: use the in-file conservative substitute for
      `temporal_memory` (documented, slower, lower quality) and set
      `degraded['temporal_memory']='local'`

  cap.t10.multi.multi_step_arithmetic@1
      if unavailable: use the in-file conservative substitute for
      `multi_step_arithmetic` (documented, slower, lower quality) and set
      `degraded['multi_step_arithmetic']='local'`

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
   3. [ 600 lines] Core implementation A - scoped credential acquisition with least-privilege defaults
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - secret redaction from all logs, traces and model context
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - credential-lifetime management and rotation handling
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - leak-detection testing across all output channels
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.credential.credential_management@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0632_credential_management.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0633-cost-control-agent

**P0633 · `cost_control_agent` — Agent Cost Governance** · [spec](PART_SPECS_T13.md#p0633-cost-control-agent) · [self-contained txt](../prompts/P0633_cost_control_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0633  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0633 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0633  (33/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Cost Governance
file         : parts/t13_agents/P0633_cost_control_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.cost_control_agent
language     : Python 3.13
capability   : cap.t13.cost.cost_control_agent@1
determinism  : io
p99 budget   : 25000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
An autonomous agent must not spend without limit.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hierarchical budget enforcement across agent trees
  2. cost-per-subtask accounting and forecasting
  3. budget-exhaustion behaviour with partial-result delivery
  4. measured budget-adherence rate

Expanded obligations:
  1. Implement hierarchical budget enforcement across agent trees, and make
     it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s
     must be able to traverse it simultaneously. No lock, mutex or borrow may
     be held across an `await` / `.await` / `yield` boundary, and the part
     must expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
     benchmark is an automatic rejection of this part.
  2. Implement cost-per-subtask accounting and forecasting with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Zapier AutomationBench target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  3. Implement budget-exhaustion behaviour with partial-result delivery
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Online-Mind2Web, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured budget-adherence rate as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Its contribution is measured against OSWorld 2.0 — a regression on that
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
  cap.t13.cost.cost_control_agent@1
  cap.t13.cost.cost_control_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.credential.credential_management@1
      if unavailable: use the in-file conservative substitute for
      `credential_management` (documented, slower, lower quality) and set
      `degraded['credential_management']='local'`

  cap.t01.secure.secure_zeroize@1
      if unavailable: use the in-file conservative substitute for
      `secure_zeroize` (documented, slower, lower quality) and set
      `degraded['secure_zeroize']='local'`

  cap.t07.memory.memory_bench@1
      if unavailable: use the in-file conservative substitute for
      `memory_bench` (documented, slower, lower quality) and set
      `degraded['memory_bench']='local'`

  cap.t10.error.error_taxonomy@1
      if unavailable: use the in-file conservative substitute for
      `error_taxonomy` (documented, slower, lower quality) and set
      `degraded['error_taxonomy']='local'`

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
   3. [ 600 lines] Core implementation A - hierarchical budget enforcement across agent trees
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - cost-per-subtask accounting and forecasting
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - budget-exhaustion behaviour with partial-result delivery
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured budget-adherence rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.cost.cost_control_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0633_cost_control_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0634-sandbox-execution

**P0634 · `sandbox_execution` — Agent Sandbox & Isolation Runtime** · [spec](PART_SPECS_T13.md#p0634-sandbox-execution) · [self-contained txt](../prompts/P0634_sandbox_execution.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0634  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0634 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0634  (34/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Sandbox & Isolation Runtime
file         : parts/t13_agents/P0634_sandbox_execution.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.sandbox_execution
language     : Python 3.13
capability   : cap.t13.sandbox.sandbox_execution@1
determinism  : io
p99 budget   : 26000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Powerful autonomy inside a strong box.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. container/VM isolation profiles per task risk level
  2. network egress policy with allowlists and audit
  3. resource limits with graceful enforcement
  4. escape-attempt testing and verification of containment

Expanded obligations:
  1. Implement container/VM isolation profiles per task risk level with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement network egress policy with allowlists and audit together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Online-Mind2Web, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  3. Implement resource limits with graceful enforcement as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against OSWorld 2.0 — a
     regression on that benchmark is an automatic rejection of this part.
  4. Implement escape-attempt testing and verification of containment, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
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
                       p99 <= 26000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.sandbox.sandbox_execution@1
  cap.t13.sandbox.sandbox_execution.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.cost.cost_control_agent@1
      if unavailable: use the in-file conservative substitute for
      `cost_control_agent` (documented, slower, lower quality) and set
      `degraded['cost_control_agent']='local'`

  cap.t07.kv.kv_paging@1
      if unavailable: use the in-file conservative substitute for
      `kv_paging` (documented, slower, lower quality) and set
      `degraded['kv_paging']='local'`

  cap.t10.search.search_controller@1
      if unavailable: use the in-file conservative substitute for
      `search_controller` (documented, slower, lower quality) and set
      `degraded['search_controller']='local'`

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
   3. [ 600 lines] Core implementation A - container/VM isolation profiles per task risk level
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - network egress policy with allowlists and audit
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - resource limits with graceful enforcement
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - escape-attempt testing and verification of containment
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.sandbox.sandbox_execution@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0634_sandbox_execution.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0635-tool-creation

**P0635 · `tool_creation` — Dynamic Tool Creation** · [spec](PART_SPECS_T13.md#p0635-tool-creation) · [self-contained txt](../prompts/P0635_tool_creation.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0635  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0635 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0635  (35/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Dynamic Tool Creation
file         : parts/t13_agents/P0635_tool_creation.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.tool_creation
language     : Python 3.13
capability   : cap.t13.tool.tool_creation@1
determinism  : io
p99 budget   : 27000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Builds the tool it needs when none exists.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. tool synthesis from a described capability gap
  2. generated-tool validation, sandboxing and registration
  3. tool-library curation and reuse across tasks
  4. measured task-success improvement from created tools

Expanded obligations:
  1. Implement tool synthesis from a described capability gap together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Online-Mind2Web, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement generated-tool validation, sandboxing and registration as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement tool-library curation and reuse across tasks, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it.
     Correctness here is what makes the tier's BrowseComp target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured task-success improvement from created tools with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
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
                       p99 <= 27000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.tool.tool_creation@1
  cap.t13.tool.tool_creation.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.sandbox.sandbox_execution@1
      if unavailable: use the in-file conservative substitute for
      `sandbox_execution` (documented, slower, lower quality) and set
      `degraded['sandbox_execution']='local'`

  cap.t01.envelope.envelope_codec@1
      if unavailable: use the in-file conservative substitute for
      `envelope_codec` (documented, slower, lower quality) and set
      `degraded['envelope_codec']='local'`

  cap.t07.semantic.semantic_memory@1
      if unavailable: use the in-file conservative substitute for
      `semantic_memory` (documented, slower, lower quality) and set
      `degraded['semantic_memory']='local'`

  cap.t10.self.self_critique@1
      if unavailable: use the in-file conservative substitute for
      `self_critique` (documented, slower, lower quality) and set
      `degraded['self_critique']='local'`

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
   3. [ 600 lines] Core implementation A - tool synthesis from a described capability gap
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - generated-tool validation, sandboxing and registration
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - tool-library curation and reuse across tasks
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured task-success improvement from created tools
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.tool.tool_creation@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0635_tool_creation.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0636-workflow-learning

**P0636 · `workflow_learning` — Workflow Learning & Skill Acquisition** · [spec](PART_SPECS_T13.md#p0636-workflow-learning) · [self-contained txt](../prompts/P0636_workflow_learning.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0636  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0636 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0636  (36/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Workflow Learning & Skill Acquisition
file         : parts/t13_agents/P0636_workflow_learning.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.workflow_learning
language     : Python 3.13
capability   : cap.t13.workflow.workflow_learning@1
determinism  : io
p99 budget   : 28000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Gets faster at repeated work.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. successful-trajectory generalisation into reusable procedures
  2. procedure parameterisation and applicability conditions
  3. procedure library maintenance with success-rate tracking
  4. measured speedup on repeated task families

Expanded obligations:
  1. Implement successful-trajectory generalisation into reusable procedures
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement procedure parameterisation and applicability conditions, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement procedure library maintenance with success-rate tracking with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Zapier AutomationBench, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  4. Implement measured speedup on repeated task families together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
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
                       p99 <= 28000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.workflow.workflow_learning@1
  cap.t13.workflow.workflow_learning.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.tool.tool_creation@1
      if unavailable: use the in-file conservative substitute for
      `tool_creation` (documented, slower, lower quality) and set
      `degraded['tool_creation']='local'`

  cap.t01.dataflow.dataflow_dag@1
      if unavailable: use the in-file conservative substitute for
      `dataflow_dag` (documented, slower, lower quality) and set
      `degraded['dataflow_dag']='local'`

  cap.t07.query.query_reformulation@1
      if unavailable: use the in-file conservative substitute for
      `query_reformulation` (documented, slower, lower quality) and set
      `degraded['query_reformulation']='local'`

  cap.t10.abstraction.abstraction_engine@1
      if unavailable: use the in-file conservative substitute for
      `abstraction_engine` (documented, slower, lower quality) and set
      `degraded['abstraction_engine']='local'`

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
   3. [ 600 lines] Core implementation A - successful-trajectory generalisation into reusable procedures
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - procedure parameterisation and applicability conditions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - procedure library maintenance with success-rate tracking
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured speedup on repeated task families
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.workflow.workflow_learning@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0636_workflow_learning.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0637-observation-compression

**P0637 · `observation_compression` — Observation Compression & Attention** · [spec](PART_SPECS_T13.md#p0637-observation-compression) · [self-contained txt](../prompts/P0637_observation_compression.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0637  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0637 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0637  (37/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Observation Compression & Attention
file         : parts/t13_agents/P0637_observation_compression.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.observation_compression
language     : Python 3.13
capability   : cap.t13.observation.observation_compression@1
determinism  : io
p99 budget   : 29000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Handles megabyte tool outputs without drowning.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. relevance-based observation filtering and summarisation
  2. structured extraction from logs, HTML and large outputs
  3. information-loss measurement against downstream success
  4. measured token reduction at matched task success

Expanded obligations:
  1. Implement relevance-based observation filtering and summarisation, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement structured extraction from logs, HTML and large outputs with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Zapier AutomationBench, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement information-loss measurement against downstream success
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Online-Mind2Web — a regression on that
     benchmark is an automatic rejection of this part.
  4. Implement measured token reduction at matched task success as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
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
                       p99 <= 29000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.observation.observation_compression@1
  cap.t13.observation.observation_compression.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.workflow.workflow_learning@1
      if unavailable: use the in-file conservative substitute for
      `workflow_learning` (documented, slower, lower quality) and set
      `degraded['workflow_learning']='local'`

  cap.t01.serialization.serialization_schema@1
      if unavailable: use the in-file conservative substitute for
      `serialization_schema` (documented, slower, lower quality) and set
      `degraded['serialization_schema']='local'`

  cap.t07.memory.memory_privacy@1
      if unavailable: use the in-file conservative substitute for
      `memory_privacy` (documented, slower, lower quality) and set
      `degraded['memory_privacy']='local'`

  cap.t10.spatial.spatial_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `spatial_reasoning` (documented, slower, lower quality) and set
      `degraded['spatial_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - relevance-based observation filtering and summarisation
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - structured extraction from logs, HTML and large outputs
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - information-loss measurement against downstream success
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured token reduction at matched task success
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.observation.observation_compression@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0637_observation_compression.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0638-agent-determinism

**P0638 · `agent_determinism` — Reproducible Agent Execution** · [spec](PART_SPECS_T13.md#p0638-agent-determinism) · [self-contained txt](../prompts/P0638_agent_determinism.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0638  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0638 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0638  (38/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Reproducible Agent Execution
file         : parts/t13_agents/P0638_agent_determinism.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_determinism
language     : Python 3.13
capability   : cap.t13.agent.agent_determinism@1
determinism  : io
p99 budget   : 30000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
The same task run twice does the same thing.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. environment and tool-result recording for exact replay
  2. deterministic decision mode with seeded sampling
  3. divergence detection during replay
  4. replay-fidelity measurement on real trajectories

Expanded obligations:
  1. Implement environment and tool-result recording for exact replay with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. This
     mechanism sits on the critical path of Zapier AutomationBench, so its
     p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement deterministic decision mode with seeded sampling together with
     its verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
     automatic rejection of this part.
  3. Implement divergence detection during replay as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's OSWorld 2.0 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement replay-fidelity measurement on real trajectories, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
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
                       p99 <= 30000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_determinism@1
  cap.t13.agent.agent_determinism.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.observation.observation_compression@1
      if unavailable: use the in-file conservative substitute for
      `observation_compression` (documented, slower, lower quality) and set
      `degraded['observation_compression']='local'`

  cap.t01.bench.bench_harness@1
      if unavailable: use the in-file conservative substitute for
      `bench_harness` (documented, slower, lower quality) and set
      `degraded['bench_harness']='local'`

  cap.t07.semantic.semantic_cache@1
      if unavailable: use the in-file conservative substitute for
      `semantic_cache` (documented, slower, lower quality) and set
      `degraded['semantic_cache']='local'`

  cap.t10.chain.chain_compression@1
      if unavailable: use the in-file conservative substitute for
      `chain_compression` (documented, slower, lower quality) and set
      `degraded['chain_compression']='local'`

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
   3. [ 600 lines] Core implementation A - environment and tool-result recording for exact replay
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - deterministic decision mode with seeded sampling
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - divergence detection during replay
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - replay-fidelity measurement on real trajectories
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_determinism@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0638_agent_determinism.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0639-agent-eval-harness

**P0639 · `agent_eval_harness` — Agent Benchmark Harness** · [spec](PART_SPECS_T13.md#p0639-agent-eval-harness) · [self-contained txt](../prompts/P0639_agent_eval_harness.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0639  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0639 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0639  (39/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Benchmark Harness
file         : parts/t13_agents/P0639_agent_eval_harness.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_eval_harness
language     : Python 3.13
capability   : cap.t13.agent.agent_eval_harness@1
determinism  : io
p99 budget   : 31000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Measures agent capability across all major public benchmarks.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. OSWorld 2.0, Online-Mind2Web, AutomationBench and BrowseComp harnesses
  2. environment-fidelity verification and version pinning
  3. per-task diagnostics with failure taxonomy
  4. targets versus Opus 5: OSWorld 95.5 vs 70.5, AutomationBench 92 vs 26

Expanded obligations:
  1. Implement OSWorld 2.0, Online-Mind2Web, AutomationBench and BrowseComp
     harnesses together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. Its contribution is measured against Online-Mind2Web — a
     regression on that benchmark is an automatic rejection of this part.
  2. Implement environment-fidelity verification and version pinning as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  3. Implement per-task diagnostics with failure taxonomy, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement targets versus Opus 5: OSWorld 95.5 vs 70.5, AutomationBench
     92 vs 26 with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Zapier
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
                       p99 <= 31000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_eval_harness@1
  cap.t13.agent.agent_eval_harness.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_determinism@1
      if unavailable: use the in-file conservative substitute for
      `agent_determinism` (documented, slower, lower quality) and set
      `degraded['agent_determinism']='local'`

  cap.t01.abi.abi_stability@1
      if unavailable: use the in-file conservative substitute for
      `abi_stability` (documented, slower, lower quality) and set
      `degraded['abi_stability']='local'`

  cap.t07.graph.graph_memory_queries@1
      if unavailable: use the in-file conservative substitute for
      `graph_memory_queries` (documented, slower, lower quality) and set
      `degraded['graph_memory_queries']='local'`

  cap.t10.reasoning.reasoning_robustness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_robustness` (documented, slower, lower quality) and set
      `degraded['reasoning_robustness']='local'`

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
   3. [ 600 lines] Core implementation A - OSWorld 2.0, Online-Mind2Web, AutomationBench and BrowseComp har
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - environment-fidelity verification and version pinning
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - per-task diagnostics with failure taxonomy
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - targets versus Opus 5: OSWorld 95.5 vs 70.5, AutomationBench 92 
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_eval_harness@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0639_agent_eval_harness.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0640-trajectory-analysis

**P0640 · `trajectory_analysis` — Trajectory Analysis & Improvement Mining** · [spec](PART_SPECS_T13.md#p0640-trajectory-analysis) · [self-contained txt](../prompts/P0640_trajectory_analysis.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0640  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0640 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0640  (40/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Trajectory Analysis & Improvement Mining
file         : parts/t13_agents/P0640_trajectory_analysis.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.trajectory_analysis
language     : Python 3.13
capability   : cap.t13.trajectory.trajectory_analysis@1
determinism  : io
p99 budget   : 32000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Learns from thousands of past runs what to do differently.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. trajectory database with outcome and cost labelling
  2. failure-pattern mining and clustering
  3. improvement-hypothesis generation and validation
  4. measured success-rate improvement from mined lessons

Expanded obligations:
  1. Implement trajectory database with outcome and cost labelling as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
     a microbenchmark that stands in for that benchmark's inner loop.
  2. Implement failure-pattern mining and clustering, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  3. Implement improvement-hypothesis generation and validation with an
     explicit *a-priori* cost model. Before doing the work the part must be
     able to state the tokens, FLOPs and microseconds it intends to consume,
     and it must abort with an `OmegaError` in the 4xxx budget range rather
     than silently exceed the envelope's `budget` or `deadline_ns`. Its
     contribution is measured against Zapier AutomationBench — a regression
     on that benchmark is an automatic rejection of this part.
  4. Implement measured success-rate improvement from mined lessons together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
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
                       p99 <= 32000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.trajectory.trajectory_analysis@1
  cap.t13.trajectory.trajectory_analysis.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_eval_harness@1
      if unavailable: use the in-file conservative substitute for
      `agent_eval_harness` (documented, slower, lower quality) and set
      `degraded['agent_eval_harness']='local'`

  cap.t01.retry.retry_idempotency@1
      if unavailable: use the in-file conservative substitute for
      `retry_idempotency` (documented, slower, lower quality) and set
      `degraded['retry_idempotency']='local'`

  cap.t07.provenance.provenance_tracking@1
      if unavailable: use the in-file conservative substitute for
      `provenance_tracking` (documented, slower, lower quality) and set
      `degraded['provenance_tracking']='local'`

  cap.t10.reasoning.reasoning_transfer@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_transfer` (documented, slower, lower quality) and set
      `degraded['reasoning_transfer']='local'`

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
   3. [ 600 lines] Core implementation A - trajectory database with outcome and cost labelling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - failure-pattern mining and clustering
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - improvement-hypothesis generation and validation
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured success-rate improvement from mined lessons
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.trajectory.trajectory_analysis@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0640_trajectory_analysis.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0641-agent-interruption

**P0641 · `agent_interruption` — Interruption, Steering & Course Correction** · [spec](PART_SPECS_T13.md#p0641-agent-interruption) · [self-contained txt](../prompts/P0641_agent_interruption.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0641  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0641 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0641  (41/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Interruption, Steering & Course Correction
file         : parts/t13_agents/P0641_agent_interruption.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_interruption
language     : Python 3.13
capability   : cap.t13.agent.agent_interruption@1
determinism  : io
p99 budget   : 33000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
The user can change direction mid-task without a restart.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. mid-execution instruction incorporation with plan repair
  2. priority reconciliation between old and new instructions
  3. state consistency after steering
  4. measured steering-success rate

Expanded obligations:
  1. Implement mid-execution instruction incorporation with plan repair, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. This mechanism sits on the critical path of
     BrowseComp, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  2. Implement priority reconciliation between old and new instructions with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Its contribution is measured against Zapier AutomationBench — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement state consistency after steering together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Correctness here is what
     makes the tier's Online-Mind2Web target reachable; the part therefore
     ships a microbenchmark that stands in for that benchmark's inner loop.
  4. Implement measured steering-success rate as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     This mechanism sits on the critical path of OSWorld 2.0, so its p99
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
  cap.t13.agent.agent_interruption@1
  cap.t13.agent.agent_interruption.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.trajectory.trajectory_analysis@1
      if unavailable: use the in-file conservative substitute for
      `trajectory_analysis` (documented, slower, lower quality) and set
      `degraded['trajectory_analysis']='local'`

  cap.t07.kv.kv_hierarchy@1
      if unavailable: use the in-file conservative substitute for
      `kv_hierarchy` (documented, slower, lower quality) and set
      `degraded['kv_hierarchy']='local'`

  cap.t10.thought.thought_program_ir@1
      if unavailable: use the in-file conservative substitute for
      `thought_program_ir` (documented, slower, lower quality) and set
      `degraded['thought_program_ir']='local'`

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
   3. [ 600 lines] Core implementation A - mid-execution instruction incorporation with plan repair
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - priority reconciliation between old and new instructions
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - state consistency after steering
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured steering-success rate
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_interruption@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0641_agent_interruption.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0642-simulation-env

**P0642 · `simulation_env` — Agent Training & Testing Environments** · [spec](PART_SPECS_T13.md#p0642-simulation-env) · [self-contained txt](../prompts/P0642_simulation_env.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0642  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0642 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0642  (42/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Training & Testing Environments
file         : parts/t13_agents/P0642_simulation_env.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.simulation_env
language     : Python 3.13
capability   : cap.t13.simulation.simulation_env@1
determinism  : io
p99 budget   : 34000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Thousands of realistic environments for evaluation and training.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. environment generation with controllable difficulty and stochasticity
  2. task-and-verifier pair generation with automatic grading
  3. environment-fidelity validation against real applications
  4. coverage report across task categories

Expanded obligations:
  1. Implement environment generation with controllable difficulty and
     stochasticity with an explicit *a-priori* cost model. Before doing the
     work the part must be able to state the tokens, FLOPs and microseconds
     it intends to consume, and it must abort with an `OmegaError` in the
     4xxx budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Its contribution is measured against Zapier
     AutomationBench — a regression on that benchmark is an automatic
     rejection of this part.
  2. Implement task-and-verifier pair generation with automatic grading
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Online-Mind2Web target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement environment-fidelity validation against real applications as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  4. Implement coverage report across task categories, and make it correct
     under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able
     to traverse it simultaneously. No lock, mutex or borrow may be held
     across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
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
  cap.t13.simulation.simulation_env@1
  cap.t13.simulation.simulation_env.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_interruption@1
      if unavailable: use the in-file conservative substitute for
      `agent_interruption` (documented, slower, lower quality) and set
      `degraded['agent_interruption']='local'`

  cap.t01.omega.omega_bus_ipc@1
      if unavailable: use the in-file conservative substitute for
      `omega_bus_ipc` (documented, slower, lower quality) and set
      `degraded['omega_bus_ipc']='local'`

  cap.t07.episodic.episodic_memory@1
      if unavailable: use the in-file conservative substitute for
      `episodic_memory` (documented, slower, lower quality) and set
      `degraded['episodic_memory']='local'`

  cap.t10.self.self_consistency@1
      if unavailable: use the in-file conservative substitute for
      `self_consistency` (documented, slower, lower quality) and set
      `degraded['self_consistency']='local'`

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
   3. [ 600 lines] Core implementation A - environment generation with controllable difficulty and stochast
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - task-and-verifier pair generation with automatic grading
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - environment-fidelity validation against real applications
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - coverage report across task categories
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.simulation.simulation_env@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0642_simulation_env.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0643-robotics-bridge

**P0643 · `robotics_bridge` — Physical Actuation Interface** · [spec](PART_SPECS_T13.md#p0643-robotics-bridge) · [self-contained txt](../prompts/P0643_robotics_bridge.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0643  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0643 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0643  (43/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Physical Actuation Interface
file         : parts/t13_agents/P0643_robotics_bridge.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.robotics_bridge
language     : Python 3.13
capability   : cap.t13.robotics.robotics_bridge@1
determinism  : io
p99 budget   : 35000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
The bridge to robots, with safety as the first requirement.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. action-space abstraction over robot control interfaces
  2. safety envelope enforcement with hard limits
  3. sensor-feedback integration and closed-loop correction
  4. simulation-first validation policy before physical execution

Expanded obligations:
  1. Implement action-space abstraction over robot control interfaces
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`.
     Correctness here is what makes the tier's Online-Mind2Web target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  2. Implement safety envelope enforcement with hard limits as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. This mechanism sits on the critical path of OSWorld
     2.0, so its p99 latency assertion is part of the acceptance criteria,
     not an optional extra.
  3. Implement sensor-feedback integration and closed-loop correction, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against BrowseComp
     — a regression on that benchmark is an automatic rejection of this part.
  4. Implement simulation-first validation policy before physical execution
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
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
                       p99 <= 35000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.robotics.robotics_bridge@1
  cap.t13.robotics.robotics_bridge.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.simulation.simulation_env@1
      if unavailable: use the in-file conservative substitute for
      `simulation_env` (documented, slower, lower quality) and set
      `degraded['simulation_env']='local'`

  cap.t01.task.task_runtime@1
      if unavailable: use the in-file conservative substitute for
      `task_runtime` (documented, slower, lower quality) and set
      `degraded['task_runtime']='local'`

  cap.t07.hybrid.hybrid_retrieval@1
      if unavailable: use the in-file conservative substitute for
      `hybrid_retrieval` (documented, slower, lower quality) and set
      `degraded['hybrid_retrieval']='local'`

  cap.t10.analogy.analogy_engine@1
      if unavailable: use the in-file conservative substitute for
      `analogy_engine` (documented, slower, lower quality) and set
      `degraded['analogy_engine']='local'`

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
   3. [ 600 lines] Core implementation A - action-space abstraction over robot control interfaces
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - safety envelope enforcement with hard limits
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - sensor-feedback integration and closed-loop correction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - simulation-first validation policy before physical execution
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.robotics.robotics_bridge@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0643_robotics_bridge.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0644-iot-control

**P0644 · `iot_control` — Device & Infrastructure Control Agent** · [spec](PART_SPECS_T13.md#p0644-iot-control) · [self-contained txt](../prompts/P0644_iot_control.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0644  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0644 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0644  (44/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Device & Infrastructure Control Agent
file         : parts/t13_agents/P0644_iot_control.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.iot_control
language     : Python 3.13
capability   : cap.t13.iot.iot_control@1
determinism  : io
p99 budget   : 36000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Operates real infrastructure responsibly.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. device capability discovery and safe command construction
  2. change-window and blast-radius policy enforcement
  3. rollback plan requirement before every change
  4. measured incident rate on controlled infrastructure tasks

Expanded obligations:
  1. Implement device capability discovery and safe command construction as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. This mechanism sits on the
     critical path of OSWorld 2.0, so its p99 latency assertion is part of
     the acceptance criteria, not an optional extra.
  2. Implement change-window and blast-radius policy enforcement, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. Its
     contribution is measured against BrowseComp — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement rollback plan requirement before every change with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. Correctness
     here is what makes the tier's Zapier AutomationBench target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement measured incident rate on controlled infrastructure tasks
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Online-Mind2Web, so its p99
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
                       p99 <= 36000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.iot.iot_control@1
  cap.t13.iot.iot_control.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.robotics.robotics_bridge@1
      if unavailable: use the in-file conservative substitute for
      `robotics_bridge` (documented, slower, lower quality) and set
      `degraded['robotics_bridge']='local'`

  cap.t01.arena.arena_graph@1
      if unavailable: use the in-file conservative substitute for
      `arena_graph` (documented, slower, lower quality) and set
      `degraded['arena_graph']='local'`

  cap.t07.conflict.conflict_resolution@1
      if unavailable: use the in-file conservative substitute for
      `conflict_resolution` (documented, slower, lower quality) and set
      `degraded['conflict_resolution']='local'`

  cap.t10.temporal.temporal_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `temporal_reasoning` (documented, slower, lower quality) and set
      `degraded['temporal_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - device capability discovery and safe command construction
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - change-window and blast-radius policy enforcement
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - rollback plan requirement before every change
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured incident rate on controlled infrastructure tasks
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.iot.iot_control@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0644_iot_control.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0645-scientific-agent

**P0645 · `scientific_agent` — Autonomous Research Agent** · [spec](PART_SPECS_T13.md#p0645-scientific-agent) · [self-contained txt](../prompts/P0645_scientific_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0645  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0645 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0645  (45/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Autonomous Research Agent
file         : parts/t13_agents/P0645_scientific_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.scientific_agent
language     : Python 3.13
capability   : cap.t13.scientific.scientific_agent@1
determinism  : io
p99 budget   : 37000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Runs the full research loop: hypothesise, experiment, analyse, iterate.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hypothesis generation and experiment design with power analysis
  2. instrument/tool control and data collection orchestration
  3. result analysis with correct statistics and honest reporting
  4. measured research-task success on curated scientific problems

Expanded obligations:
  1. Implement hypothesis generation and experiment design with power
     analysis, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Its contribution is measured against BrowseComp
     — a regression on that benchmark is an automatic rejection of this part.
  2. Implement instrument/tool control and data collection orchestration with
     an explicit *a-priori* cost model. Before doing the work the part must
     be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     Correctness here is what makes the tier's Zapier AutomationBench target
     reachable; the part therefore ships a microbenchmark that stands in for
     that benchmark's inner loop.
  3. Implement result analysis with correct statistics and honest reporting
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. This
     mechanism sits on the critical path of Online-Mind2Web, so its p99
     latency assertion is part of the acceptance criteria, not an optional
     extra.
  4. Implement measured research-task success on curated scientific problems
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
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
                       p99 <= 37000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.scientific.scientific_agent@1
  cap.t13.scientific.scientific_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.iot.iot_control@1
      if unavailable: use the in-file conservative substitute for
      `iot_control` (documented, slower, lower quality) and set
      `degraded['iot_control']='local'`

  cap.t01.fuzz.fuzz_engine@1
      if unavailable: use the in-file conservative substitute for
      `fuzz_engine` (documented, slower, lower quality) and set
      `degraded['fuzz_engine']='local'`

  cap.t07.cache.cache_warm_predict@1
      if unavailable: use the in-file conservative substitute for
      `cache_warm_predict` (documented, slower, lower quality) and set
      `degraded['cache_warm_predict']='local'`

  cap.t10.reasoning.reasoning_memory@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_memory` (documented, slower, lower quality) and set
      `degraded['reasoning_memory']='local'`

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
   3. [ 600 lines] Core implementation A - hypothesis generation and experiment design with power analysis
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - instrument/tool control and data collection orchestration
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - result analysis with correct statistics and honest reporting
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured research-task success on curated scientific problems
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.scientific.scientific_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0645_scientific_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0646-data-analysis-agent

**P0646 · `data_analysis_agent` — Autonomous Data Analysis Agent** · [spec](PART_SPECS_T13.md#p0646-data-analysis-agent) · [self-contained txt](../prompts/P0646_data_analysis_agent.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0646  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0646 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0646  (46/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Autonomous Data Analysis Agent
file         : parts/t13_agents/P0646_data_analysis_agent.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.data_analysis_agent
language     : Python 3.13
capability   : cap.t13.data.data_analysis_agent@1
determinism  : io
p99 budget   : 38000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Behaves like a careful scientist, not a plot generator.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. appropriate statistical test selection with assumption checking
  2. confounder identification and independent cross-checking of results
  3. analysis-narrative generation with limitations stated
  4. accuracy measurement on analysis tasks with known ground truth

Expanded obligations:
  1. Implement appropriate statistical test selection with assumption
     checking with an explicit *a-priori* cost model. Before doing the work
     the part must be able to state the tokens, FLOPs and microseconds it
     intends to consume, and it must abort with an `OmegaError` in the 4xxx
     budget range rather than silently exceed the envelope's `budget` or
     `deadline_ns`. Correctness here is what makes the tier's Zapier
     AutomationBench target reachable; the part therefore ships a
     microbenchmark that stands in for that benchmark's inner loop.
  2. Implement confounder identification and independent cross-checking of
     results together with its verification path, so that anything this
     mechanism produces can be independently re-checked *inside this same
     file* without contacting any other part. The checker must be cheap
     enough to run on every call in debug mode and must be wired into
     `selftest()`. This mechanism sits on the critical path of
     Online-Mind2Web, so its p99 latency assertion is part of the acceptance
     criteria, not an optional extra.
  3. Implement analysis-narrative generation with limitations stated as a
     first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement accuracy measurement on analysis tasks with known ground
     truth, and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
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
                       p99 <= 38000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.data.data_analysis_agent@1
  cap.t13.data.data_analysis_agent.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.scientific.scientific_agent@1
      if unavailable: use the in-file conservative substitute for
      `scientific_agent` (documented, slower, lower quality) and set
      `degraded['scientific_agent']='local'`

  cap.t01.manifest.manifest_parser@1
      if unavailable: use the in-file conservative substitute for
      `manifest_parser` (documented, slower, lower quality) and set
      `degraded['manifest_parser']='local'`

  cap.t07.memory.memory_replication@1
      if unavailable: use the in-file conservative substitute for
      `memory_replication` (documented, slower, lower quality) and set
      `degraded['memory_replication']='local'`

  cap.t10.reasoning.reasoning_faithfulness@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_faithfulness` (documented, slower, lower quality) and set
      `degraded['reasoning_faithfulness']='local'`

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
   3. [ 600 lines] Core implementation A - appropriate statistical test selection with assumption checking
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - confounder identification and independent cross-checking of resu
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - analysis-narrative generation with limitations stated
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - accuracy measurement on analysis tasks with known ground truth
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.data.data_analysis_agent@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0646_data_analysis_agent.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0647-agent-ux

**P0647 · `agent_ux` — Agent Transparency & Explainability** · [spec](PART_SPECS_T13.md#p0647-agent-ux) · [self-contained txt](../prompts/P0647_agent_ux.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0647  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0647 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0647  (47/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Transparency & Explainability
file         : parts/t13_agents/P0647_agent_ux.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_ux
language     : Python 3.13
capability   : cap.t13.agent.agent_ux@1
determinism  : io
p99 budget   : 39000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
The user always knows what it is doing and why.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. real-time action narration with rationale
  2. decision-log artifact for post-hoc review
  3. uncertainty and assumption surfacing during execution
  4. user-trust and comprehension evaluation

Expanded obligations:
  1. Implement real-time action narration with rationale together with its
     verification path, so that anything this mechanism produces can be
     independently re-checked *inside this same file* without contacting any
     other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. This mechanism sits on
     the critical path of Online-Mind2Web, so its p99 latency assertion is
     part of the acceptance criteria, not an optional extra.
  2. Implement decision-log artifact for post-hoc review as a first-class,
     fully realised mechanism. No stub, no `NotImplementedError`, no
     configuration flag whose default disables it. Its state must be
     reportable through `describe()` and it must be exercised by at least
     eight in-file tests, including one that fails loudly if the mechanism is
     silently bypassed. Its contribution is measured against OSWorld 2.0 — a
     regression on that benchmark is an automatic rejection of this part.
  3. Implement uncertainty and assumption surfacing during execution, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  4. Implement user-trust and comprehension evaluation with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Zapier AutomationBench, so its p99 latency
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
                       p99 <= 39000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_ux@1
  cap.t13.agent.agent_ux.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.data.data_analysis_agent@1
      if unavailable: use the in-file conservative substitute for
      `data_analysis_agent` (documented, slower, lower quality) and set
      `degraded['data_analysis_agent']='local'`

  cap.t01.circuit.circuit_breaker@1
      if unavailable: use the in-file conservative substitute for
      `circuit_breaker` (documented, slower, lower quality) and set
      `degraded['circuit_breaker']='local'`

  cap.t07.dedup.dedup_engine@1
      if unavailable: use the in-file conservative substitute for
      `dedup_engine` (documented, slower, lower quality) and set
      `degraded['dedup_engine']='local'`

  cap.t10.subgoal.subgoal_caching@1
      if unavailable: use the in-file conservative substitute for
      `subgoal_caching` (documented, slower, lower quality) and set
      `degraded['subgoal_caching']='local'`

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
   3. [ 600 lines] Core implementation A - real-time action narration with rationale
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - decision-log artifact for post-hoc review
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - uncertainty and assumption surfacing during execution
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - user-trust and comprehension evaluation
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_ux@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0647_agent_ux.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0648-agent-speed

**P0648 · `agent_speed` — Agent Latency Engineering** · [spec](PART_SPECS_T13.md#p0648-agent-speed) · [self-contained txt](../prompts/P0648_agent_speed.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0648  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0648 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0648  (48/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Latency Engineering
file         : parts/t13_agents/P0648_agent_speed.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_speed
language     : Python 3.13
capability   : cap.t13.agent.agent_speed@1
determinism  : io
p99 budget   : 40000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Long-horizon tasks finished in critical-path time (S6 realisation).

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. parallel subtask execution with dependency-aware scheduling
  2. speculative tool execution for side-effect-free calls
  3. observation-processing latency reduction
  4. measured wall-clock reduction versus serial execution

Expanded obligations:
  1. Implement parallel subtask execution with dependency-aware scheduling as
     a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Its contribution is
     measured against OSWorld 2.0 — a regression on that benchmark is an
     automatic rejection of this part.
  2. Implement speculative tool execution for side-effect-free calls, and
     make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  3. Implement observation-processing latency reduction with an explicit
     *a-priori* cost model. Before doing the work the part must be able to
     state the tokens, FLOPs and microseconds it intends to consume, and it
     must abort with an `OmegaError` in the 4xxx budget range rather than
     silently exceed the envelope's `budget` or `deadline_ns`. This mechanism
     sits on the critical path of Zapier AutomationBench, so its p99 latency
     assertion is part of the acceptance criteria, not an optional extra.
  4. Implement measured wall-clock reduction versus serial execution together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
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
                       p99 <= 40000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_speed@1
  cap.t13.agent.agent_speed.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_ux@1
      if unavailable: use the in-file conservative substitute for `agent_ux`
      (documented, slower, lower quality) and set
      `degraded['agent_ux']='local'`

  cap.t01.shutdown.shutdown_drain@1
      if unavailable: use the in-file conservative substitute for
      `shutdown_drain` (documented, slower, lower quality) and set
      `degraded['shutdown_drain']='local'`

  cap.t07.memory.memory_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `memory_spec_doc` (documented, slower, lower quality) and set
      `degraded['memory_spec_doc']='local'`

  cap.t10.reasoning.reasoning_spec_doc@1
      if unavailable: use the in-file conservative substitute for
      `reasoning_spec_doc` (documented, slower, lower quality) and set
      `degraded['reasoning_spec_doc']='local'`

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
   3. [ 600 lines] Core implementation A - parallel subtask execution with dependency-aware scheduling
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - speculative tool execution for side-effect-free calls
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - observation-processing latency reduction
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - measured wall-clock reduction versus serial execution
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_speed@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0648_agent_speed.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0649-agent-scaling

**P0649 · `agent_scaling` — 1000-Agent Scale Coordination** · [spec](PART_SPECS_T13.md#p0649-agent-scaling) · [self-contained txt](../prompts/P0649_agent_scaling.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0649  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0649 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0649  (49/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : 1000-Agent Scale Coordination
file         : parts/t13_agents/P0649_agent_scaling.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_scaling
language     : Python 3.13
capability   : cap.t13.agent.agent_scaling@1
determinism  : io
p99 budget   : 41000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
Proves the orchestration works at the target scale.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. hierarchical coordination topology for 1000 concurrent agents
  2. communication and coordination overhead measurement at scale
  3. failure isolation so one agent cannot stall the swarm
  4. throughput and quality measurement at 1, 10, 100, 1000 agents

Expanded obligations:
  1. Implement hierarchical coordination topology for 1000 concurrent agents,
     and make it correct under concurrency: at least 64 in-flight
     `OmegaEnvelope`s must be able to traverse it simultaneously. No lock,
     mutex or borrow may be held across an `await` / `.await` / `yield`
     boundary, and the part must expose a contention counter so T09 can
     attribute latency to it. Correctness here is what makes the tier's
     BrowseComp target reachable; the part therefore ships a microbenchmark
     that stands in for that benchmark's inner loop.
  2. Implement communication and coordination overhead measurement at scale
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Zapier AutomationBench, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  3. Implement failure isolation so one agent cannot stall the swarm together
     with its verification path, so that anything this mechanism produces can
     be independently re-checked *inside this same file* without contacting
     any other part. The checker must be cheap enough to run on every call in
     debug mode and must be wired into `selftest()`. Its contribution is
     measured against Online-Mind2Web — a regression on that benchmark is an
     automatic rejection of this part.
  4. Implement throughput and quality measurement at 1, 10, 100, 1000 agents
     as a first-class, fully realised mechanism. No stub, no
     `NotImplementedError`, no configuration flag whose default disables it.
     Its state must be reportable through `describe()` and it must be
     exercised by at least eight in-file tests, including one that fails
     loudly if the mechanism is silently bypassed. Correctness here is what
     makes the tier's OSWorld 2.0 target reachable; the part therefore ships
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
                       p99 <= 41000 ns at the reference shape
  describe()         : -> JSON-serialisable dict: schemas, version, degraded{}

PROVIDES
--------
  cap.t13.agent.agent_scaling@1
  cap.t13.agent.agent_scaling.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_speed@1
      if unavailable: use the in-file conservative substitute for
      `agent_speed` (documented, slower, lower quality) and set
      `degraded['agent_speed']='local'`

  cap.t07.summarisation.summarisation_memory@1
      if unavailable: use the in-file conservative substitute for
      `summarisation_memory` (documented, slower, lower quality) and set
      `degraded['summarisation_memory']='local'`

  cap.t10.outcome.outcome_verifier@1
      if unavailable: use the in-file conservative substitute for
      `outcome_verifier` (documented, slower, lower quality) and set
      `degraded['outcome_verifier']='local'`

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
   3. [ 600 lines] Core implementation A - hierarchical coordination topology for 1000 concurrent agents
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - communication and coordination overhead measurement at scale
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - failure isolation so one agent cannot stall the swarm
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - throughput and quality measurement at 1, 10, 100, 1000 agents
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_scaling@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0649_agent_scaling.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````

## PROMPT p0650-agent-spec-doc

**P0650 · `agent_spec_doc` — Agent Subsystem Specification & Runbook** · [spec](PART_SPECS_T13.md#p0650-agent-spec-doc) · [self-contained txt](../prompts/P0650_agent_spec_doc.txt)

````text
==============================================================================
HYPERION-Ω  ·  WORKER P0650  ·  ONE FILE  ·  ~5000 LINES
==============================================================================

ROLE
----
You are worker P0650 of 1000 independent Claude Opus 5 instances building HYPERION-OMEGA, a general AI that must beat Claude Opus 5 on every benchmark and run 100x
faster. You are running on your own machine. You have NO access to the other 999 workers,
NO shared folder, NO ability to ask questions. Everything you need is in this prompt.
Produce your file in one pass. Do not ask for clarification. Do not stop early.

Ω-CONTRACT: use BLOCK A at the top of this file, VERBATIM, in your file header.

YOUR PART
---------
part_id      : P0650  (50/50 of tier T13)
tier         : T13 — Agents, Tool Use & Computer Control
title        : Agent Subsystem Specification & Runbook
file         : parts/t13_agents/P0650_agent_spec_doc.py          <-- create exactly this path, nothing else
module       : hyperion.t13.agents.agent_spec_doc
language     : Python 3.13
capability   : cap.t13.agent.agent_spec_doc@1
determinism  : io
p99 budget   : 42000 ns
line budget  : 5000 (+/- 3%)
tier benches : OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

MISSION
-------
The authoritative description of agent behaviour and limits.

Tier context:
  Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and
  1000-way agent orchestration.

MANDATE — implement all four. None is optional. None may be stubbed.
-------------------------------------------------------------------
  1. specification of loop semantics, safety gates and budget rules
  2. capability register with measured success rates per task class
  3. operator runbook for agent incidents
  4. spec-versus-implementation drift detection

Expanded obligations:
  1. Implement specification of loop semantics, safety gates and budget rules
     with an explicit *a-priori* cost model. Before doing the work the part
     must be able to state the tokens, FLOPs and microseconds it intends to
     consume, and it must abort with an `OmegaError` in the 4xxx budget range
     rather than silently exceed the envelope's `budget` or `deadline_ns`.
     This mechanism sits on the critical path of Zapier AutomationBench, so
     its p99 latency assertion is part of the acceptance criteria, not an
     optional extra.
  2. Implement capability register with measured success rates per task class
     together with its verification path, so that anything this mechanism
     produces can be independently re-checked *inside this same file* without
     contacting any other part. The checker must be cheap enough to run on
     every call in debug mode and must be wired into `selftest()`. Its
     contribution is measured against Online-Mind2Web — a regression on that
     benchmark is an automatic rejection of this part.
  3. Implement operator runbook for agent incidents as a first-class, fully
     realised mechanism. No stub, no `NotImplementedError`, no configuration
     flag whose default disables it. Its state must be reportable through
     `describe()` and it must be exercised by at least eight in-file tests,
     including one that fails loudly if the mechanism is silently bypassed.
     Correctness here is what makes the tier's OSWorld 2.0 target reachable;
     the part therefore ships a microbenchmark that stands in for that
     benchmark's inner loop.
  4. Implement spec-versus-implementation drift detection, and make it
     correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must
     be able to traverse it simultaneously. No lock, mutex or borrow may be
     held across an `await` / `.await` / `yield` boundary, and the part must
     expose a contention counter so T09 can attribute latency to it. This
     mechanism sits on the critical path of BrowseComp, so its p99 latency
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
  cap.t13.agent.agent_spec_doc@1
  cap.t13.agent.agent_spec_doc.describe@1

REQUIRES — and the fallback you MUST write for each one
------------------------------------------------------
You may NEVER assume a requirement resolves: the other 999 workers are on other
machines and their files may not exist when yours is loaded. For each line below,
write: try-acquire -> on failure use the fallback -> record it in describe()['degraded'].

  cap.t01.abi.abi_types@1
      if unavailable: re-declare the structural minimum locally (a frozen
      dataclass/struct mirror) and set `degraded['abi']='local-mirror'`

  cap.t01.abi.abi_errors@1
      if unavailable: raise the local `_OmegaErrorShim` carrying the same
      numeric code, and set `degraded['errors']='shim'`

  cap.t01.omega.omega_bus_core@1
      if unavailable: run against the in-file `_LoopbackBus` (direct call,
      no queue) and set `degraded['bus']='loopback'`

  cap.t13.agent.agent_scaling@1
      if unavailable: use the in-file conservative substitute for
      `agent_scaling` (documented, slower, lower quality) and set
      `degraded['agent_scaling']='local'`

  cap.t01.atomics.atomics_sync@1
      if unavailable: use the in-file conservative substitute for
      `atomics_sync` (documented, slower, lower quality) and set
      `degraded['atomics_sync']='local'`

  cap.t07.sparse.sparse_retrieval@1
      if unavailable: use the in-file conservative substitute for
      `sparse_retrieval` (documented, slower, lower quality) and set
      `degraded['sparse_retrieval']='local'`

  cap.t10.constraint.constraint_reasoning@1
      if unavailable: use the in-file conservative substitute for
      `constraint_reasoning` (documented, slower, lower quality) and set
      `degraded['constraint_reasoning']='local'`

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
   3. [ 600 lines] Core implementation A - specification of loop semantics, safety gates and budget rules
                     Primary algorithm. No TODOs, no placeholders, no stubbed branches.
   4. [ 580 lines] Core implementation B - capability register with measured success rates per task class
                     Second required mechanism, fully independent of A's internals.
   5. [ 520 lines] Core implementation C - operator runbook for agent incidents
                     Third required mechanism.
   6. [ 480 lines] Core implementation D - spec-versus-implementation drift detection
                     Fourth required mechanism, including its measurement/assertion
                     path.
   7. [ 210 lines] Ω-Bus integration: register(), describe(), capability handles
                     Idempotent registration, schema export, handle lifetime and
                     teardown.
   8. [ 200 lines] Degradation ladder: declared fallbacks for every required capability
                     For each entry in `requires`, a working local fallback + quality
                     annotation.
   9. [ 250 lines] Error paths, budget/deadline handling, partial results
                     Every OmegaCode this part can emit, with remedy text and
                     retryability.
  10. [ 150 lines] Observability: events, counters, histograms, latency attribution
                     Structured events only; no stdout. Counters registered through T20
                     telemetry.
  11. [ 170 lines] Determinism harness: split_seed usage, replay, batch-invariance
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
     exactly (capability == cap.t13.agent.agent_spec_doc@1)?
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
  Emit ONE fenced code block containing the complete contents of `parts/t13_agents/P0650_agent_spec_doc.py`.
  No prose before or after it. No ellipses. No '... rest omitted'. Complete file only.

BEGIN NOW.
==============================================================================
````
