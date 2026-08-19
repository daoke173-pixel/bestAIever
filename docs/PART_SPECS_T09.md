# HYPERION-Ω — Part specifications · T09 · Latency Engineering & Ω-Memoize

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Rust 1.86

**Tier mission.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Benchmarks this tier is accountable for.** Terminal-Bench 2.1, CursorBench 3.2

**Tier dependencies.** T01, T07, T08

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0401](#p0401-latency-accounting) | `latency_accounting` | End-to-End Latency Accounting Framework | `cap.t09.latency.latency_accounting@1` |
| [P0402](#p0402-speed-law-model) | `speed_law_model` | The 100x Speed Law Model | `cap.t09.speed.speed_law_model@1` |
| [P0403](#p0403-memoize-core) | `memoize_core` | Ω-Memoize Core Engine | `cap.t09.memoize.memoize_core@1` |
| [P0404](#p0404-exact-cache) | `exact_cache` | Exact-Match Response Cache | `cap.t09.exact.exact_cache@1` |
| [P0405](#p0405-similarity-cache) | `similarity_cache` | Approximate Semantic Cache with Safety Gates | `cap.t09.similarity.similarity_cache@1` |
| [P0406](#p0406-template-cache) | `template_cache` | Structural Template Cache | `cap.t09.template.template_cache@1` |
| [P0407](#p0407-computation-reuse) | `computation_reuse` | Cross-Request Computation Reuse | `cap.t09.computation.computation_reuse@1` |
| [P0408](#p0408-early-exit-runtime) | `early_exit_runtime` | Early-Exit Runtime Controller | `cap.t09.early.early_exit_runtime@1` |
| [P0409](#p0409-distill-fast-paths) | `distill_fast_paths` | Distilled Fast Path Registry | `cap.t09.distill.distill_fast_paths@1` |
| [P0410](#p0410-precompute-engine) | `precompute_engine` | Offline Precomputation Engine | `cap.t09.precompute.precompute_engine@1` |
| [P0411](#p0411-prefetch-predictor) | `prefetch_predictor` | Next-Action Prediction & Prefetch | `cap.t09.prefetch.prefetch_predictor@1` |
| [P0412](#p0412-parallel-horizon) | `parallel_horizon` | Parallel Horizon Execution Engine | `cap.t09.parallel.parallel_horizon@1` |
| [P0413](#p0413-dag-critical-path) | `dag_critical_path` | Critical Path Optimiser | `cap.t09.dag.dag_critical_path@1` |
| [P0414](#p0414-async-pipeline) | `async_pipeline` | Asynchronous Pipeline Orchestrator | `cap.t09.async.async_pipeline@1` |
| [P0415](#p0415-tail-latency) | `tail_latency` | Tail Latency Engineering | `cap.t09.tail.tail_latency@1` |
| [P0416](#p0416-jitter-control) | `jitter_control` | Latency Jitter & Predictability Control | `cap.t09.jitter.jitter_control@1` |
| [P0417](#p0417-warmup-manager) | `warmup_manager` | Warmup & Cold Start Elimination | `cap.t09.warmup.warmup_manager@1` |
| [P0418](#p0418-gc-pause-control) | `gc_pause_control` | Pause-Free Operation Engineering | `cap.t09.gc.gc_pause_control@1` |
| [P0419](#p0419-syscall-reduction) | `syscall_reduction` | Syscall & Context-Switch Minimisation | `cap.t09.syscall.syscall_reduction@1` |
| [P0420](#p0420-network-latency) | `network_latency` | Network Path Latency Optimisation | `cap.t09.network.network_latency@1` |
| [P0421](#p0421-edge-inference) | `edge_inference` | Edge & Local-First Execution | `cap.t09.edge.edge_inference@1` |
| [P0422](#p0422-compression-latency) | `compression_latency` | Payload Compression Latency Tradeoffs | `cap.t09.compression.compression_latency@1` |
| [P0423](#p0423-batch-latency-tradeoff) | `batch_latency_tradeoff` | Batching Latency/Throughput Optimiser | `cap.t09.batch.batch_latency_tradeoff@1` |
| [P0424](#p0424-priority-lanes) | `priority_lanes` | Priority Lanes & Interactive Fast Path | `cap.t09.priority.priority_lanes@1` |
| [P0425](#p0425-speculative-ui) | `speculative_ui` | Perceived Latency Engineering | `cap.t09.speculative.speculative_ui@1` |
| [P0426](#p0426-cache-coherence) | `cache_coherence` | Cross-Layer Cache Coherence & Invalidation | `cap.t09.cache.cache_coherence@1` |
| [P0427](#p0427-hot-cold-split) | `hot_cold_split` | Hot/Cold Path Separation | `cap.t09.hot.hot_cold_split@1` |
| [P0428](#p0428-lock-free-paths) | `lock_free_paths` | Lock-Free Request Path | `cap.t09.lock.lock_free_paths@1` |
| [P0429](#p0429-numa-latency) | `numa_latency` | Memory Locality Latency Optimisation | `cap.t09.numa.numa_latency@1` |
| [P0430](#p0430-io-scheduling) | `io_scheduling` | Storage IO Latency Scheduling | `cap.t09.io.io_scheduling@1` |
| [P0431](#p0431-adaptive-quality) | `adaptive_quality` | Adaptive Quality/Latency Controller | `cap.t09.adaptive.adaptive_quality@1` |
| [P0432](#p0432-slo-manager) | `slo_manager` | SLO Definition, Tracking & Error Budgets | `cap.t09.slo.slo_manager@1` |
| [P0433](#p0433-latency-regression-gate) | `latency_regression_gate` | Latency Regression Gate for 1000 Parts | `cap.t09.latency.latency_regression_gate@1` |
| [P0434](#p0434-perf-ci) | `perf_ci` | Continuous Performance Integration | `cap.t09.perf.perf_ci@1` |
| [P0435](#p0435-flamegraph-tooling) | `flamegraph_tooling` | Profiling & Flamegraph Analysis Tooling | `cap.t09.flamegraph.flamegraph_tooling@1` |
| [P0436](#p0436-bottleneck-analyser) | `bottleneck_analyser` | Automatic Bottleneck Analyser | `cap.t09.bottleneck.bottleneck_analyser@1` |
| [P0437](#p0437-throughput-optimiser) | `throughput_optimiser` | Throughput Optimisation Engine | `cap.t09.throughput.throughput_optimiser@1` |
| [P0438](#p0438-energy-efficiency) | `energy_efficiency` | Energy per Token Optimisation | `cap.t09.energy.energy_efficiency@1` |
| [P0439](#p0439-cost-optimiser) | `cost_optimiser` | Cost per Solved Task Optimiser | `cap.t09.cost.cost_optimiser@1` |
| [P0440](#p0440-capacity-planner) | `capacity_planner` | Capacity Planning & Headroom Model | `cap.t09.capacity.capacity_planner@1` |
| [P0441](#p0441-cache-sizing) | `cache_sizing` | Cache Sizing & Memory Allocation Optimiser | `cap.t09.cache.cache_sizing@1` |
| [P0442](#p0442-speculation-budget) | `speculation_budget` | Speculation Budget Governor | `cap.t09.speculation.speculation_budget@1` |
| [P0443](#p0443-latency-simulator) | `latency_simulator` | Latency Simulator & What-If Engine | `cap.t09.latency.latency_simulator@1` |
| [P0444](#p0444-benchmark-speed-public) | `benchmark_speed_public` | Public Speed Comparison Harness | `cap.t09.benchmark.benchmark_speed_public@1` |
| [P0445](#p0445-realtime-mode) | `realtime_mode` | Real-Time & Voice-Latency Mode | `cap.t09.realtime.realtime_mode@1` |
| [P0446](#p0446-burst-handling) | `burst_handling` | Burst Absorption & Queue Shaping | `cap.t09.burst.burst_handling@1` |
| [P0447](#p0447-degradation-ladder) | `degradation_ladder` | Formal Degradation Ladder | `cap.t09.degradation.degradation_ladder@1` |
| [P0448](#p0448-latency-dashboard) | `latency_dashboard` | Latency & Cost Observability Artifacts | `cap.t09.latency.latency_dashboard@1` |
| [P0449](#p0449-speed-proof-report) | `speed_proof_report` | The 100x Speed Proof Report Generator | `cap.t09.speed.speed_proof_report@1` |
| [P0450](#p0450-latency-spec-doc) | `latency_spec_doc` | Latency Engineering Specification & Runbook | `cap.t09.latency.latency_spec_doc@1` |

---

### P0401 · `latency_accounting` — End-to-End Latency Accounting Framework

| field | value |
|---|---|
| part id | `P0401` (1/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0401_latency_accounting.rs` |
| module path | `hyperion.t09.latency.latency_accounting` |
| capability published | `cap.t09.latency.latency_accounting@1` |
| determinism class | `io` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0401_latency_accounting.txt`](prompts/P0401_latency_accounting.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0401-latency-accounting) |

**Mission.** The measurement system that makes the 100x claim auditable.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **phase decomposition with nanosecond attribution and no double counting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **critical-path extraction from the span tree** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-part latency attribution across all 1000 parts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accounting-completeness verification (sum equals wall clock)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.latency.latency_accounting@1`
- `cap.t09.latency.latency_accounting.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t07.freshness.freshness_manager@1` | use the in-file conservative substitute for `freshness_manager` (documented, slower, lower quality) and set `degraded['freshness_manager']='local'` |
| `cap.t08.stop.stop_conditions@1` | use the in-file conservative substitute for `stop_conditions` (documented, slower, lower quality) and set `degraded['stop_conditions']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - phase decomposition with nanosecond attribution and no double co | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - critical-path extraction from the span tree | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-part latency attribution across all 1000 parts | 520 | Third required mechanism. |
| 6 | Core implementation D - accounting-completeness verification (sum equals wall clock) | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 28000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0401_latency_accounting.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.latency.latency_accounting@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 28000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0402 · `speed_law_model` — The 100x Speed Law Model

| field | value |
|---|---|
| part id | `P0402` (2/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0402_speed_law_model.rs` |
| module path | `hyperion.t09.latency.speed_law_model` |
| capability published | `cap.t09.speed.speed_law_model@1` |
| determinism class | `io` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0402_speed_law_model.txt`](prompts/P0402_speed_law_model.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0402-speed-law-model) |

**Mission.** Formalises S1..S6 multiplicativity and proves the product exceeds 100.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **formal model of each speedup source with measured inputs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **interaction/overlap correction so factors are not double counted** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **confidence intervals and sensitivity analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **auditable derivation report with reproducible measurements**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.speed.speed_law_model@1`
- `cap.t09.speed.speed_law_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.latency.latency_accounting@1` | use the in-file conservative substitute for `latency_accounting` (documented, slower, lower quality) and set `degraded['latency_accounting']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t07.attention.attention_sink@1` | use the in-file conservative substitute for `attention_sink` (documented, slower, lower quality) and set `degraded['attention_sink']='local'` |
| `cap.t08.adapter.adapter_serving@1` | use the in-file conservative substitute for `adapter_serving` (documented, slower, lower quality) and set `degraded['adapter_serving']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - formal model of each speedup source with measured inputs | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - interaction/overlap correction so factors are not double counted | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - confidence intervals and sensitivity analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - auditable derivation report with reproducible measurements | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 29000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0402_speed_law_model.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.speed.speed_law_model@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 29000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0403 · `memoize_core` — Ω-Memoize Core Engine

| field | value |
|---|---|
| part id | `P0403` (3/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0403_memoize_core.rs` |
| module path | `hyperion.t09.latency.memoize_core` |
| capability published | `cap.t09.memoize.memoize_core@1` |
| determinism class | `io` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0403_memoize_core.txt`](prompts/P0403_memoize_core.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0403-memoize-core) |

**Mission.** The unified reuse layer: 60-75% of traffic answered without decoding (S4).

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-level cache hierarchy (exact, prefix, semantic, subgraph, tool)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **unified lookup with cost-ordered probing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **correctness conditions per level with enforcement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured overall reuse rate on production-shaped traffic** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.memoize.memoize_core@1`
- `cap.t09.memoize.memoize_core.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.speed.speed_law_model@1` | use the in-file conservative substitute for `speed_law_model` (documented, slower, lower quality) and set `degraded['speed_law_model']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t07.persistence.persistence_layer@1` | use the in-file conservative substitute for `persistence_layer` (documented, slower, lower quality) and set `degraded['persistence_layer']='local'` |
| `cap.t08.engine.engine_telemetry@1` | use the in-file conservative substitute for `engine_telemetry` (documented, slower, lower quality) and set `degraded['engine_telemetry']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-level cache hierarchy (exact, prefix, semantic, subgraph,  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - unified lookup with cost-ordered probing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - correctness conditions per level with enforcement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured overall reuse rate on production-shaped traffic | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 30000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0403_memoize_core.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.memoize.memoize_core@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 30000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0404 · `exact_cache` — Exact-Match Response Cache

| field | value |
|---|---|
| part id | `P0404` (4/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0404_exact_cache.rs` |
| module path | `hyperion.t09.latency.exact_cache` |
| capability published | `cap.t09.exact.exact_cache@1` |
| determinism class | `io` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0404_exact_cache.txt`](prompts/P0404_exact_cache.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0404-exact-cache) |

**Mission.** Byte-identical requests answered in microseconds.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **canonical request normalisation and hashing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **scope/permission-aware key composition**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **invalidation on model, knowledge and policy changes** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **hit-rate and latency measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.exact.exact_cache@1`
- `cap.t09.exact.exact_cache.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.memoize.memoize_core@1` | use the in-file conservative substitute for `memoize_core` (documented, slower, lower quality) and set `degraded['memoize_core']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t07.index.index_build_pipeline@1` | use the in-file conservative substitute for `index_build_pipeline` (documented, slower, lower quality) and set `degraded['index_build_pipeline']='local'` |
| `cap.t08.api.api_gateway_runtime@1` | use the in-file conservative substitute for `api_gateway_runtime` (documented, slower, lower quality) and set `degraded['api_gateway_runtime']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - canonical request normalisation and hashing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - scope/permission-aware key composition | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - invalidation on model, knowledge and policy changes | 520 | Third required mechanism. |
| 6 | Core implementation D - hit-rate and latency measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 31000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0404_exact_cache.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.exact.exact_cache@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 31000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0405 · `similarity_cache` — Approximate Semantic Cache with Safety Gates

| field | value |
|---|---|
| part id | `P0405` (5/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0405_similarity_cache.rs` |
| module path | `hyperion.t09.latency.similarity_cache` |
| capability published | `cap.t09.similarity.similarity_cache@1` |
| determinism class | `io` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0405_similarity_cache.txt`](prompts/P0405_similarity_cache.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0405-similarity-cache) |

**Mission.** Reuse by meaning, with hard guards against wrong reuse.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **calibrated similarity thresholds per query class**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **context-sensitivity detection preventing unsafe reuse** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **shadow verification sampling to measure false-hit rate** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **quality audit with a target false-hit rate under 0.1%** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.similarity.similarity_cache@1`
- `cap.t09.similarity.similarity_cache.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.exact.exact_cache@1` | use the in-file conservative substitute for `exact_cache` (documented, slower, lower quality) and set `degraded['exact_cache']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t07.cost.cost_aware_retrieval@1` | use the in-file conservative substitute for `cost_aware_retrieval` (documented, slower, lower quality) and set `degraded['cost_aware_retrieval']='local'` |
| `cap.t08.cost.cost_accounting_runtime@1` | use the in-file conservative substitute for `cost_accounting_runtime` (documented, slower, lower quality) and set `degraded['cost_accounting_runtime']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - calibrated similarity thresholds per query class | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - context-sensitivity detection preventing unsafe reuse | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - shadow verification sampling to measure false-hit rate | 520 | Third required mechanism. |
| 6 | Core implementation D - quality audit with a target false-hit rate under 0.1% | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 32000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0405_similarity_cache.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.similarity.similarity_cache@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 32000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0406 · `template_cache` — Structural Template Cache

| field | value |
|---|---|
| part id | `P0406` (6/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0406_template_cache.rs` |
| module path | `hyperion.t09.latency.template_cache` |
| capability published | `cap.t09.template.template_cache@1` |
| determinism class | `io` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0406_template_cache.txt`](prompts/P0406_template_cache.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0406-template-cache) |

**Mission.** Recognises repeated task shapes and reuses their solution skeletons.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **task-shape abstraction and template extraction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **slot-filling with verification of the filled result** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **template library growth and pruning policy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured cost reduction on repetitive workloads**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.template.template_cache@1`
- `cap.t09.template.template_cache.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.similarity.similarity_cache@1` | use the in-file conservative substitute for `similarity_cache` (documented, slower, lower quality) and set `degraded['similarity_cache']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t07.context.context_window_manager@1` | use the in-file conservative substitute for `context_window_manager` (documented, slower, lower quality) and set `degraded['context_window_manager']='local'` |
| `cap.t08.cascade.cascade_stage1_draft@1` | use the in-file conservative substitute for `cascade_stage1_draft` (documented, slower, lower quality) and set `degraded['cascade_stage1_draft']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - task-shape abstraction and template extraction | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - slot-filling with verification of the filled result | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - template library growth and pruning policy | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cost reduction on repetitive workloads | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 33000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0406_template_cache.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.template.template_cache@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 33000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0407 · `computation_reuse` — Cross-Request Computation Reuse

| field | value |
|---|---|
| part id | `P0407` (7/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0407_computation_reuse.rs` |
| module path | `hyperion.t09.latency.computation_reuse` |
| capability published | `cap.t09.computation.computation_reuse@1` |
| determinism class | `io` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0407_computation_reuse.txt`](prompts/P0407_computation_reuse.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0407-computation-reuse) |

**Mission.** Shares expensive intermediate work between concurrent requests.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **identical-subcomputation detection across in-flight requests** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **single-flight coalescing with result fan-out** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **isolation verification preventing cross-tenant leakage**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured duplicate-work elimination rate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.computation.computation_reuse@1`
- `cap.t09.computation.computation_reuse.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.template.template_cache@1` | use the in-file conservative substitute for `template_cache` (documented, slower, lower quality) and set `degraded['template_cache']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t07.vector.vector_index@1` | use the in-file conservative substitute for `vector_index` (documented, slower, lower quality) and set `degraded['vector_index']='local'` |
| `cap.t08.cascade.cascade_rollback@1` | use the in-file conservative substitute for `cascade_rollback` (documented, slower, lower quality) and set `degraded['cascade_rollback']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - identical-subcomputation detection across in-flight requests | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - single-flight coalescing with result fan-out | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - isolation verification preventing cross-tenant leakage | 520 | Third required mechanism. |
| 6 | Core implementation D - measured duplicate-work elimination rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 34000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0407_computation_reuse.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.computation.computation_reuse@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 34000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0408 · `early_exit_runtime` — Early-Exit Runtime Controller

| field | value |
|---|---|
| part id | `P0408` (8/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0408_early_exit_runtime.rs` |
| module path | `hyperion.t09.latency.early_exit_runtime` |
| capability published | `cap.t09.early.early_exit_runtime@1` |
| determinism class | `io` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0408_early_exit_runtime.txt`](prompts/P0408_early_exit_runtime.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0408-early-exit-runtime) |

**Mission.** Stops thinking the moment the answer is certain (S5 contributor).

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **confidence-threshold policy per task class with calibration** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **verifier-gated exit preventing premature confident errors**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **compute-saving measurement at matched accuracy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **worst-case-quality guardrails** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.early.early_exit_runtime@1`
- `cap.t09.early.early_exit_runtime.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.computation.computation_reuse@1` | use the in-file conservative substitute for `computation_reuse` (documented, slower, lower quality) and set `degraded['computation_reuse']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t07.citation.citation_grounding@1` | use the in-file conservative substitute for `citation_grounding` (documented, slower, lower quality) and set `degraded['citation_grounding']='local'` |
| `cap.t08.logit.logit_processor@1` | use the in-file conservative substitute for `logit_processor` (documented, slower, lower quality) and set `degraded['logit_processor']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - confidence-threshold policy per task class with calibration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - verifier-gated exit preventing premature confident errors | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - compute-saving measurement at matched accuracy | 520 | Third required mechanism. |
| 6 | Core implementation D - worst-case-quality guardrails | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 35000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0408_early_exit_runtime.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.early.early_exit_runtime@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 35000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0409 · `distill_fast_paths` — Distilled Fast Path Registry

| field | value |
|---|---|
| part id | `P0409` (9/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0409_distill_fast_paths.rs` |
| module path | `hyperion.t09.latency.distill_fast_paths` |
| capability published | `cap.t09.distill.distill_fast_paths@1` |
| determinism class | `io` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0409_distill_fast_paths.txt`](prompts/P0409_distill_fast_paths.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0409-distill-fast-paths) |

**Mission.** Small models handle the easy majority; the core handles the rest.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **fast-path model registry with per-task competence maps**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **routing thresholds calibrated to maintain quality parity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **continuous distillation from core traffic** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured fraction of traffic served by fast paths** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.distill.distill_fast_paths@1`
- `cap.t09.distill.distill_fast_paths.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.early.early_exit_runtime@1` | use the in-file conservative substitute for `early_exit_runtime` (documented, slower, lower quality) and set `degraded['early_exit_runtime']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t07.memory.memory_compression_learned@1` | use the in-file conservative substitute for `memory_compression_learned` (documented, slower, lower quality) and set `degraded['memory_compression_learned']='local'` |
| `cap.t08.multi.multi_model_serving@1` | use the in-file conservative substitute for `multi_model_serving` (documented, slower, lower quality) and set `degraded['multi_model_serving']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fast-path model registry with per-task competence maps | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - routing thresholds calibrated to maintain quality parity | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - continuous distillation from core traffic | 520 | Third required mechanism. |
| 6 | Core implementation D - measured fraction of traffic served by fast paths | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 36000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0409_distill_fast_paths.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.distill.distill_fast_paths@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 36000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0410 · `precompute_engine` — Offline Precomputation Engine

| field | value |
|---|---|
| part id | `P0410` (10/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0410_precompute_engine.rs` |
| module path | `hyperion.t09.latency.precompute_engine` |
| capability published | `cap.t09.precompute.precompute_engine@1` |
| determinism class | `io` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0410_precompute_engine.txt`](prompts/P0410_precompute_engine.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0410-precompute-engine) |

**Mission.** Does tomorrow's work tonight, cheaply.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **forecast-driven precomputation of likely requests and embeddings** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cost-arbitrage scheduling into cheap capacity windows** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **staleness management and invalidation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured online-latency reduction versus precompute cost**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.precompute.precompute_engine@1`
- `cap.t09.precompute.precompute_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.distill.distill_fast_paths@1` | use the in-file conservative substitute for `distill_fast_paths` (documented, slower, lower quality) and set `degraded['distill_fast_paths']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t07.memory.memory_gc@1` | use the in-file conservative substitute for `memory_gc` (documented, slower, lower quality) and set `degraded['memory_gc']='local'` |
| `cap.t08.output.output_verification_loop@1` | use the in-file conservative substitute for `output_verification_loop` (documented, slower, lower quality) and set `degraded['output_verification_loop']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - forecast-driven precomputation of likely requests and embeddings | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost-arbitrage scheduling into cheap capacity windows | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - staleness management and invalidation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured online-latency reduction versus precompute cost | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 37000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0410_precompute_engine.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.precompute.precompute_engine@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 37000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0411 · `prefetch_predictor` — Next-Action Prediction & Prefetch

| field | value |
|---|---|
| part id | `P0411` (11/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0411_prefetch_predictor.rs` |
| module path | `hyperion.t09.latency.prefetch_predictor` |
| capability published | `cap.t09.prefetch.prefetch_predictor@1` |
| determinism class | `io` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0411_prefetch_predictor.txt`](prompts/P0411_prefetch_predictor.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0411-prefetch-predictor) |

**Mission.** Predicts the user's or agent's next need and prepares it (S6).

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **sequence models over session and workflow traces** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **prefetch budget control with wasted-work accounting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **accuracy measurement per prediction horizon**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured p50/p99 improvement attributable to prefetch** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.prefetch.prefetch_predictor@1`
- `cap.t09.prefetch.prefetch_predictor.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.precompute.precompute_engine@1` | use the in-file conservative substitute for `precompute_engine` (documented, slower, lower quality) and set `degraded['precompute_engine']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t07.memory.memory_audit@1` | use the in-file conservative substitute for `memory_audit` (documented, slower, lower quality) and set `degraded['memory_audit']='local'` |
| `cap.t08.engine.engine_fault_tolerance@1` | use the in-file conservative substitute for `engine_fault_tolerance` (documented, slower, lower quality) and set `degraded['engine_fault_tolerance']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sequence models over session and workflow traces | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - prefetch budget control with wasted-work accounting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accuracy measurement per prediction horizon | 520 | Third required mechanism. |
| 6 | Core implementation D - measured p50/p99 improvement attributable to prefetch | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 38000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0411_prefetch_predictor.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.prefetch.prefetch_predictor@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 38000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0412 · `parallel_horizon` — Parallel Horizon Execution Engine

| field | value |
|---|---|
| part id | `P0412` (12/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0412_parallel_horizon.rs` |
| module path | `hyperion.t09.latency.parallel_horizon` |
| capability published | `cap.t09.parallel.parallel_horizon@1` |
| determinism class | `io` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0412_parallel_horizon.txt`](prompts/P0412_parallel_horizon.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0412-parallel-horizon) |

**Mission.** Turns serial long-horizon work into critical-path-time work (S6 core).

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **speculative parallel execution of independent DAG branches** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **optimistic execution with dependency-violation rollback**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **1000-way concurrency management with resource caps** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured wall-clock reduction on long-horizon tasks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.parallel.parallel_horizon@1`
- `cap.t09.parallel.parallel_horizon.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.prefetch.prefetch_predictor@1` | use the in-file conservative substitute for `prefetch_predictor` (documented, slower, lower quality) and set `degraded['prefetch_predictor']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t07.streaming.streaming_ingest@1` | use the in-file conservative substitute for `streaming_ingest` (documented, slower, lower quality) and set `degraded['streaming_ingest']='local'` |
| `cap.t08.engine.engine_security@1` | use the in-file conservative substitute for `engine_security` (documented, slower, lower quality) and set `degraded['engine_security']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - speculative parallel execution of independent DAG branches | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - optimistic execution with dependency-violation rollback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - 1000-way concurrency management with resource caps | 520 | Third required mechanism. |
| 6 | Core implementation D - measured wall-clock reduction on long-horizon tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 39000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0412_parallel_horizon.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.parallel.parallel_horizon@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 39000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0413 · `dag_critical_path` — Critical Path Optimiser

| field | value |
|---|---|
| part id | `P0413` (13/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0413_dag_critical_path.rs` |
| module path | `hyperion.t09.latency.dag_critical_path` |
| capability published | `cap.t09.dag.dag_critical_path@1` |
| determinism class | `io` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0413_dag_critical_path.txt`](prompts/P0413_dag_critical_path.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0413-dag-critical-path) |

**Mission.** Finds and shortens the one path that determines total time.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **critical-path computation with measured node costs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **targeted optimisation recommendation per path node** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **what-if analysis for proposed changes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured makespan reduction after optimisation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.dag.dag_critical_path@1`
- `cap.t09.dag.dag_critical_path.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.parallel.parallel_horizon@1` | use the in-file conservative substitute for `parallel_horizon` (documented, slower, lower quality) and set `degraded['parallel_horizon']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t07.kv.kv_compression_runtime@1` | use the in-file conservative substitute for `kv_compression_runtime` (documented, slower, lower quality) and set `degraded['kv_compression_runtime']='local'` |
| `cap.t08.admission.admission_control@1` | use the in-file conservative substitute for `admission_control` (documented, slower, lower quality) and set `degraded['admission_control']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - critical-path computation with measured node costs | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - targeted optimisation recommendation per path node | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - what-if analysis for proposed changes | 520 | Third required mechanism. |
| 6 | Core implementation D - measured makespan reduction after optimisation | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 40000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0413_dag_critical_path.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.dag.dag_critical_path@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 40000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0414 · `async_pipeline` — Asynchronous Pipeline Orchestrator

| field | value |
|---|---|
| part id | `P0414` (14/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0414_async_pipeline.rs` |
| module path | `hyperion.t09.latency.async_pipeline` |
| capability published | `cap.t09.async.async_pipeline@1` |
| determinism class | `io` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0414_async_pipeline.txt`](prompts/P0414_async_pipeline.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0414-async-pipeline) |

**Mission.** Everything that can overlap, does.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **dependency-driven async execution with structured concurrency** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **overlap-efficiency measurement (achieved versus ideal)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deadlock freedom and cancellation correctness** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **pipeline-depth tuning under memory limits**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.async.async_pipeline@1`
- `cap.t09.async.async_pipeline.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.dag.dag_critical_path@1` | use the in-file conservative substitute for `dag_critical_path` (documented, slower, lower quality) and set `degraded['dag_critical_path']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t07.forgetting.forgetting_policy@1` | use the in-file conservative substitute for `forgetting_policy` (documented, slower, lower quality) and set `degraded['forgetting_policy']='local'` |
| `cap.t08.cascade.cascade_batching@1` | use the in-file conservative substitute for `cascade_batching` (documented, slower, lower quality) and set `degraded['cascade_batching']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dependency-driven async execution with structured concurrency | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - overlap-efficiency measurement (achieved versus ideal) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deadlock freedom and cancellation correctness | 520 | Third required mechanism. |
| 6 | Core implementation D - pipeline-depth tuning under memory limits | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 41000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0414_async_pipeline.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.async.async_pipeline@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 41000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0415 · `tail_latency` — Tail Latency Engineering

| field | value |
|---|---|
| part id | `P0415` (15/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0415_tail_latency.rs` |
| module path | `hyperion.t09.latency.tail_latency` |
| capability published | `cap.t09.tail.tail_latency@1` |
| determinism class | `io` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0415_tail_latency.txt`](prompts/P0415_tail_latency.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0415-tail-latency) |

**Mission.** p99.9 matters more than p50 for agents making 1000 calls.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **hedged requests with cancellation and cost caps** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **tail-cause attribution (GC, cache miss, straggler, throttle)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **per-cause mitigation with measured effect**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **p99.9 target enforcement in the benchmark gate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.tail.tail_latency@1`
- `cap.t09.tail.tail_latency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.async.async_pipeline@1` | use the in-file conservative substitute for `async_pipeline` (documented, slower, lower quality) and set `degraded['async_pipeline']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t07.reranker.reranker_model@1` | use the in-file conservative substitute for `reranker_model` (documented, slower, lower quality) and set `degraded['reranker_model']='local'` |
| `cap.t08.constrained.constrained_decoding@1` | use the in-file conservative substitute for `constrained_decoding` (documented, slower, lower quality) and set `degraded['constrained_decoding']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hedged requests with cancellation and cost caps | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tail-cause attribution (GC, cache miss, straggler, throttle) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-cause mitigation with measured effect | 520 | Third required mechanism. |
| 6 | Core implementation D - p99.9 target enforcement in the benchmark gate | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 42000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0415_tail_latency.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.tail.tail_latency@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 42000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0416 · `jitter_control` — Latency Jitter & Predictability Control

| field | value |
|---|---|
| part id | `P0416` (16/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0416_jitter_control.rs` |
| module path | `hyperion.t09.latency.jitter_control` |
| capability published | `cap.t09.jitter.jitter_control@1` |
| determinism class | `io` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0416_jitter_control.txt`](prompts/P0416_jitter_control.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0416-jitter-control) |

**Mission.** Consistent latency is a feature; variance is a bug.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **variance-source identification and elimination** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **pacing and admission smoothing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **jitter measurement with distribution shape analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **predictability score reported per endpoint** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.jitter.jitter_control@1`
- `cap.t09.jitter.jitter_control.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.tail.tail_latency@1` | use the in-file conservative substitute for `tail_latency` (documented, slower, lower quality) and set `degraded['tail_latency']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t07.belief.belief_revision@1` | use the in-file conservative substitute for `belief_revision` (documented, slower, lower quality) and set `degraded['belief_revision']='local'` |
| `cap.t08.weight.weight_hotswap@1` | use the in-file conservative substitute for `weight_hotswap` (documented, slower, lower quality) and set `degraded['weight_hotswap']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - variance-source identification and elimination | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - pacing and admission smoothing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - jitter measurement with distribution shape analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - predictability score reported per endpoint | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 43000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0416_jitter_control.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.jitter.jitter_control@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 43000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0417 · `warmup_manager` — Warmup & Cold Start Elimination

| field | value |
|---|---|
| part id | `P0417` (17/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0417_warmup_manager.rs` |
| module path | `hyperion.t09.latency.warmup_manager` |
| capability published | `cap.t09.warmup.warmup_manager@1` |
| determinism class | `io` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0417_warmup_manager.txt`](prompts/P0417_warmup_manager.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0417-warmup-manager) |

**Mission.** The first request is as fast as the thousandth.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **staged warmup: weights, kernels, caches, JIT, indexes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **predictive warmup from deployment and traffic signals** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **cold-start latency measurement per stage** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: cold start within 1.2x of warm latency** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.warmup.warmup_manager@1`
- `cap.t09.warmup.warmup_manager.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.jitter.jitter_control@1` | use the in-file conservative substitute for `jitter_control` (documented, slower, lower quality) and set `degraded['jitter_control']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t07.retrieval.retrieval_cache@1` | use the in-file conservative substitute for `retrieval_cache` (documented, slower, lower quality) and set `degraded['retrieval_cache']='local'` |
| `cap.t08.parallel.parallel_generation@1` | use the in-file conservative substitute for `parallel_generation` (documented, slower, lower quality) and set `degraded['parallel_generation']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - staged warmup: weights, kernels, caches, JIT, indexes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - predictive warmup from deployment and traffic signals | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cold-start latency measurement per stage | 520 | Third required mechanism. |
| 6 | Core implementation D - target: cold start within 1.2x of warm latency | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 44000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0417_warmup_manager.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.warmup.warmup_manager@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 44000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0418 · `gc_pause_control` — Pause-Free Operation Engineering

| field | value |
|---|---|
| part id | `P0418` (18/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0418_gc_pause_control.rs` |
| module path | `hyperion.t09.latency.gc_pause_control` |
| capability published | `cap.t09.gc.gc_pause_control@1` |
| determinism class | `io` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0418_gc_pause_control.txt`](prompts/P0418_gc_pause_control.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0418-gc-pause-control) |

**Mission.** No stop-the-world event ever touches a request.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **allocation-free hot paths with preallocated pools** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **incremental background reclamation with bounded steps** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **pause-time distribution measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **verification that no pause exceeds the jitter budget**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.gc.gc_pause_control@1`
- `cap.t09.gc.gc_pause_control.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.warmup.warmup_manager@1` | use the in-file conservative substitute for `warmup_manager` (documented, slower, lower quality) and set `degraded['warmup_manager']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t07.user.user_model@1` | use the in-file conservative substitute for `user_model` (documented, slower, lower quality) and set `degraded['user_model']='local'` |
| `cap.t08.quantised.quantised_serving@1` | use the in-file conservative substitute for `quantised_serving` (documented, slower, lower quality) and set `degraded['quantised_serving']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - allocation-free hot paths with preallocated pools | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - incremental background reclamation with bounded steps | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - pause-time distribution measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - verification that no pause exceeds the jitter budget | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 45000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0418_gc_pause_control.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.gc.gc_pause_control@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 45000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0419 · `syscall_reduction` — Syscall & Context-Switch Minimisation

| field | value |
|---|---|
| part id | `P0419` (19/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0419_syscall_reduction.rs` |
| module path | `hyperion.t09.latency.syscall_reduction` |
| capability published | `cap.t09.syscall.syscall_reduction@1` |
| determinism class | `io` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0419_syscall_reduction.txt`](prompts/P0419_syscall_reduction.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0419-syscall-reduction) |

**Mission.** Removes operating-system overhead from the hot path.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **batched IO, io_uring-style submission and busy-poll modes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **thread-affinity and preemption avoidance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **syscall-count measurement per request**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured latency improvement from each reduction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.syscall.syscall_reduction@1`
- `cap.t09.syscall.syscall_reduction.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.gc.gc_pause_control@1` | use the in-file conservative substitute for `gc_pause_control` (documented, slower, lower quality) and set `degraded['gc_pause_control']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t07.memory.memory_sharding@1` | use the in-file conservative substitute for `memory_sharding` (documented, slower, lower quality) and set `degraded['memory_sharding']='local'` |
| `cap.t08.prompt.prompt_compilation@1` | use the in-file conservative substitute for `prompt_compilation` (documented, slower, lower quality) and set `degraded['prompt_compilation']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - batched IO, io_uring-style submission and busy-poll modes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - thread-affinity and preemption avoidance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - syscall-count measurement per request | 520 | Third required mechanism. |
| 6 | Core implementation D - measured latency improvement from each reduction | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 46000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0419_syscall_reduction.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.syscall.syscall_reduction@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 46000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0420 · `network_latency` — Network Path Latency Optimisation

| field | value |
|---|---|
| part id | `P0420` (20/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0420_network_latency.rs` |
| module path | `hyperion.t09.latency.network_latency` |
| capability published | `cap.t09.network.network_latency@1` |
| determinism class | `io` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0420_network_latency.txt`](prompts/P0420_network_latency.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0420-network-latency) |

**Mission.** The wire should add microseconds, not milliseconds.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **connection reuse, 0-RTT resumption and header compression** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **geographic routing and edge termination policy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **protocol-overhead measurement and reduction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured RTT contribution to end-to-end latency** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.network.network_latency@1`
- `cap.t09.network.network_latency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.syscall.syscall_reduction@1` | use the in-file conservative substitute for `syscall_reduction` (documented, slower, lower quality) and set `degraded['syscall_reduction']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t07.kv.kv_dedup@1` | use the in-file conservative substitute for `kv_dedup` (documented, slower, lower quality) and set `degraded['kv_dedup']='local'` |
| `cap.t08.prefill.prefill_decode_split@1` | use the in-file conservative substitute for `prefill_decode_split` (documented, slower, lower quality) and set `degraded['prefill_decode_split']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - connection reuse, 0-RTT resumption and header compression | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - geographic routing and edge termination policy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - protocol-overhead measurement and reduction | 520 | Third required mechanism. |
| 6 | Core implementation D - measured RTT contribution to end-to-end latency | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 47000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0420_network_latency.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.network.network_latency@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 47000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0421 · `edge_inference` — Edge & Local-First Execution

| field | value |
|---|---|
| part id | `P0421` (21/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0421_edge_inference.rs` |
| module path | `hyperion.t09.latency.edge_inference` |
| capability published | `cap.t09.edge.edge_inference@1` |
| determinism class | `io` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0421_edge_inference.txt`](prompts/P0421_edge_inference.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0421-edge-inference) |

**Mission.** The lowest-latency path is the one that never leaves the device.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **local model tier with capability-based cloud escalation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **hybrid local/cloud execution splitting a single request** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **privacy benefits and quality tradeoffs measured** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **latency comparison versus cloud-only serving** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.edge.edge_inference@1`
- `cap.t09.edge.edge_inference.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.network.network_latency@1` | use the in-file conservative substitute for `network_latency` (documented, slower, lower quality) and set `degraded['network_latency']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t07.memory.memory_consolidation@1` | use the in-file conservative substitute for `memory_consolidation` (documented, slower, lower quality) and set `degraded['memory_consolidation']='local'` |
| `cap.t08.cascade.cascade_scheduler@1` | use the in-file conservative substitute for `cascade_scheduler` (documented, slower, lower quality) and set `degraded['cascade_scheduler']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - local model tier with capability-based cloud escalation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hybrid local/cloud execution splitting a single request | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - privacy benefits and quality tradeoffs measured | 520 | Third required mechanism. |
| 6 | Core implementation D - latency comparison versus cloud-only serving | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 48000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0421_edge_inference.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.edge.edge_inference@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 48000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0422 · `compression_latency` — Payload Compression Latency Tradeoffs

| field | value |
|---|---|
| part id | `P0422` (22/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0422_compression_latency.rs` |
| module path | `hyperion.t09.latency.compression_latency` |
| capability published | `cap.t09.compression.compression_latency@1` |
| determinism class | `io` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0422_compression_latency.txt`](prompts/P0422_compression_latency.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0422-compression-latency) |

**Mission.** Compresses only when it actually makes things faster.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **adaptive compression decisions from payload size and link speed** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **streaming compression avoiding buffering delay** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **CPU-cost versus transfer-saving model** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured net latency effect per decision**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.compression.compression_latency@1`
- `cap.t09.compression.compression_latency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.edge.edge_inference@1` | use the in-file conservative substitute for `edge_inference` (documented, slower, lower quality) and set `degraded['edge_inference']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t07.embedding.embedding_model@1` | use the in-file conservative substitute for `embedding_model` (documented, slower, lower quality) and set `degraded['embedding_model']='local'` |
| `cap.t08.sampler.sampler_engine@1` | use the in-file conservative substitute for `sampler_engine` (documented, slower, lower quality) and set `degraded['sampler_engine']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - adaptive compression decisions from payload size and link speed | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - streaming compression avoiding buffering delay | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - CPU-cost versus transfer-saving model | 520 | Third required mechanism. |
| 6 | Core implementation D - measured net latency effect per decision | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 49000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0422_compression_latency.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.compression.compression_latency@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 49000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0423 · `batch_latency_tradeoff` — Batching Latency/Throughput Optimiser

| field | value |
|---|---|
| part id | `P0423` (23/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0423_batch_latency_tradeoff.rs` |
| module path | `hyperion.t09.latency.batch_latency_tradeoff` |
| capability published | `cap.t09.batch.batch_latency_tradeoff@1` |
| determinism class | `io` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0423_batch_latency_tradeoff.txt`](prompts/P0423_batch_latency_tradeoff.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0423-batch-latency-tradeoff) |

**Mission.** Finds the exact batching point that meets SLOs at minimum cost.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **queueing-theory model calibrated with measurements** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **per-SLO-class batching parameter selection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **dynamic adjustment under changing load**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **cost-at-SLO measurement versus fixed configurations** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.batch.batch_latency_tradeoff@1`
- `cap.t09.batch.batch_latency_tradeoff.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.compression.compression_latency@1` | use the in-file conservative substitute for `compression_latency` (documented, slower, lower quality) and set `degraded['compression_latency']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t07.world.world_state_store@1` | use the in-file conservative substitute for `world_state_store` (documented, slower, lower quality) and set `degraded['world_state_store']='local'` |
| `cap.t08.model.model_loading@1` | use the in-file conservative substitute for `model_loading` (documented, slower, lower quality) and set `degraded['model_loading']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - queueing-theory model calibrated with measurements | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-SLO-class batching parameter selection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - dynamic adjustment under changing load | 520 | Third required mechanism. |
| 6 | Core implementation D - cost-at-SLO measurement versus fixed configurations | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 3000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0423_batch_latency_tradeoff.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.batch.batch_latency_tradeoff@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 3000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0424 · `priority_lanes` — Priority Lanes & Interactive Fast Path

| field | value |
|---|---|
| part id | `P0424` (24/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0424_priority_lanes.rs` |
| module path | `hyperion.t09.latency.priority_lanes` |
| capability published | `cap.t09.priority.priority_lanes@1` |
| determinism class | `io` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0424_priority_lanes.txt`](prompts/P0424_priority_lanes.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0424-priority-lanes) |

**Mission.** Interactive requests never queue behind batch work.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **strict-priority lanes with reserved capacity** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **batch-work preemption with safe checkpointing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **interactive p99 protection measurement under batch load** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **fairness accounting across lanes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.priority.priority_lanes@1`
- `cap.t09.priority.priority_lanes.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.batch.batch_latency_tradeoff@1` | use the in-file conservative substitute for `batch_latency_tradeoff` (documented, slower, lower quality) and set `degraded['batch_latency_tradeoff']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t07.subgraph.subgraph_memoize@1` | use the in-file conservative substitute for `subgraph_memoize` (documented, slower, lower quality) and set `degraded['subgraph_memoize']='local'` |
| `cap.t08.speculative.speculative_tools@1` | use the in-file conservative substitute for `speculative_tools` (documented, slower, lower quality) and set `degraded['speculative_tools']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - strict-priority lanes with reserved capacity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - batch-work preemption with safe checkpointing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - interactive p99 protection measurement under batch load | 520 | Third required mechanism. |
| 6 | Core implementation D - fairness accounting across lanes | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 4000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0424_priority_lanes.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.priority.priority_lanes@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 4000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0425 · `speculative_ui` — Perceived Latency Engineering

| field | value |
|---|---|
| part id | `P0425` (25/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0425_speculative_ui.rs` |
| module path | `hyperion.t09.latency.speculative_ui` |
| capability published | `cap.t09.speculative.speculative_ui@1` |
| determinism class | `io` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0425_speculative_ui.txt`](prompts/P0425_speculative_ui.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0425-speculative-ui) |

**Mission.** Feels instant even when it is not.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **progressive disclosure and streaming-order optimisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **optimistic partial results with correction protocol** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **perceived-latency measurement methodology** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **user-facing latency budget definitions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.speculative.speculative_ui@1`
- `cap.t09.speculative.speculative_ui.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.priority.priority_lanes@1` | use the in-file conservative substitute for `priority_lanes` (documented, slower, lower quality) and set `degraded['priority_lanes']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t07.multimodal.multimodal_memory@1` | use the in-file conservative substitute for `multimodal_memory` (documented, slower, lower quality) and set `degraded['multimodal_memory']='local'` |
| `cap.t08.kv.kv_offload_runtime@1` | use the in-file conservative substitute for `kv_offload_runtime` (documented, slower, lower quality) and set `degraded['kv_offload_runtime']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - progressive disclosure and streaming-order optimisation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - optimistic partial results with correction protocol | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - perceived-latency measurement methodology | 520 | Third required mechanism. |
| 6 | Core implementation D - user-facing latency budget definitions | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 5000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0425_speculative_ui.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.speculative.speculative_ui@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 5000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0426 · `cache_coherence` — Cross-Layer Cache Coherence & Invalidation

| field | value |
|---|---|
| part id | `P0426` (26/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0426_cache_coherence.rs` |
| module path | `hyperion.t09.latency.cache_coherence` |
| capability published | `cap.t09.cache.cache_coherence@1` |
| determinism class | `io` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0426_cache_coherence.txt`](prompts/P0426_cache_coherence.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0426-cache-coherence) |

**Mission.** Ten cache layers, zero stale answers.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **global invalidation protocol with versioned epochs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **dependency tracking from source data to cached answers** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **stale-read detection and measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **invalidation-latency and correctness verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.cache.cache_coherence@1`
- `cap.t09.cache.cache_coherence.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.speculative.speculative_ui@1` | use the in-file conservative substitute for `speculative_ui` (documented, slower, lower quality) and set `degraded['speculative_ui']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t07.context.context_budget_optimiser@1` | use the in-file conservative substitute for `context_budget_optimiser` (documented, slower, lower quality) and set `degraded['context_budget_optimiser']='local'` |
| `cap.t08.tokenizer.tokenizer_runtime@1` | use the in-file conservative substitute for `tokenizer_runtime` (documented, slower, lower quality) and set `degraded['tokenizer_runtime']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - global invalidation protocol with versioned epochs | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dependency tracking from source data to cached answers | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - stale-read detection and measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - invalidation-latency and correctness verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 6000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0426_cache_coherence.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.cache.cache_coherence@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 6000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0427 · `hot_cold_split` — Hot/Cold Path Separation

| field | value |
|---|---|
| part id | `P0427` (27/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0427_hot_cold_split.rs` |
| module path | `hyperion.t09.latency.hot_cold_split` |
| capability published | `cap.t09.hot.hot_cold_split@1` |
| determinism class | `io` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0427_hot_cold_split.txt`](prompts/P0427_hot_cold_split.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0427-hot-cold-split) |

**Mission.** The 1% of code that runs 99% of the time gets all the attention.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **profile-driven hot-path identification and isolation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **cold-path outlining to keep instruction caches warm** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **branch-layout and code-alignment optimisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured instruction-cache-miss reduction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.hot.hot_cold_split@1`
- `cap.t09.hot.hot_cold_split.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.cache.cache_coherence@1` | use the in-file conservative substitute for `cache_coherence` (documented, slower, lower quality) and set `degraded['cache_coherence']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t07.kv.kv_eviction@1` | use the in-file conservative substitute for `kv_eviction` (documented, slower, lower quality) and set `degraded['kv_eviction']='local'` |
| `cap.t08.chunked.chunked_prefill@1` | use the in-file conservative substitute for `chunked_prefill` (documented, slower, lower quality) and set `degraded['chunked_prefill']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - profile-driven hot-path identification and isolation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cold-path outlining to keep instruction caches warm | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - branch-layout and code-alignment optimisation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured instruction-cache-miss reduction | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 7000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0427_hot_cold_split.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.hot.hot_cold_split@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 7000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0428 · `lock_free_paths` — Lock-Free Request Path

| field | value |
|---|---|
| part id | `P0428` (28/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0428_lock_free_paths.rs` |
| module path | `hyperion.t09.latency.lock_free_paths` |
| capability published | `cap.t09.lock.lock_free_paths@1` |
| determinism class | `io` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0428_lock_free_paths.txt`](prompts/P0428_lock_free_paths.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0428-lock-free-paths) |

**Mission.** No request ever waits for a mutex.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **lock-free data structures on every shared hot structure** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **contention measurement and elimination**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **progress guarantees (lock-freedom or wait-freedom) stated per structure** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **scalability measurement to 256 threads** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.lock.lock_free_paths@1`
- `cap.t09.lock.lock_free_paths.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.hot.hot_cold_split@1` | use the in-file conservative substitute for `hot_cold_split` (documented, slower, lower quality) and set `degraded['hot_cold_split']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t07.procedural.procedural_memory@1` | use the in-file conservative substitute for `procedural_memory` (documented, slower, lower quality) and set `degraded['procedural_memory']='local'` |
| `cap.t08.cascade.cascade_acceptance@1` | use the in-file conservative substitute for `cascade_acceptance` (documented, slower, lower quality) and set `degraded['cascade_acceptance']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - lock-free data structures on every shared hot structure | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - contention measurement and elimination | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - progress guarantees (lock-freedom or wait-freedom) stated per st | 520 | Third required mechanism. |
| 6 | Core implementation D - scalability measurement to 256 threads | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 8000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0428_lock_free_paths.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.lock.lock_free_paths@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 8000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0429 · `numa_latency` — Memory Locality Latency Optimisation

| field | value |
|---|---|
| part id | `P0429` (29/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0429_numa_latency.rs` |
| module path | `hyperion.t09.latency.numa_latency` |
| capability published | `cap.t09.numa.numa_latency@1` |
| determinism class | `io` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0429_numa_latency.txt`](prompts/P0429_numa_latency.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0429-numa-latency) |

**Mission.** Every hot access is local.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **access-pattern profiling and remote-access detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **data placement and thread pinning remediation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **measured latency improvement from locality fixes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **regression detection on placement changes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.numa.numa_latency@1`
- `cap.t09.numa.numa_latency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.lock.lock_free_paths@1` | use the in-file conservative substitute for `lock_free_paths` (documented, slower, lower quality) and set `degraded['lock_free_paths']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t07.chunking.chunking_strategy@1` | use the in-file conservative substitute for `chunking_strategy` (documented, slower, lower quality) and set `degraded['chunking_strategy']='local'` |
| `cap.t08.session.session_affinity@1` | use the in-file conservative substitute for `session_affinity` (documented, slower, lower quality) and set `degraded['session_affinity']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - access-pattern profiling and remote-access detection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - data placement and thread pinning remediation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - measured latency improvement from locality fixes | 520 | Third required mechanism. |
| 6 | Core implementation D - regression detection on placement changes | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 9000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0429_numa_latency.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.numa.numa_latency@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 9000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0430 · `io_scheduling` — Storage IO Latency Scheduling

| field | value |
|---|---|
| part id | `P0430` (30/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0430_io_scheduling.rs` |
| module path | `hyperion.t09.latency.io_scheduling` |
| capability published | `cap.t09.io.io_scheduling@1` |
| determinism class | `io` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0430_io_scheduling.txt`](prompts/P0430_io_scheduling.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0430-io-scheduling) |

**Mission.** Disk never stalls a token.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **priority IO scheduling with deadline awareness** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **readahead tuning from access-pattern prediction** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **IO-latency percentile measurement per class** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **stall-free verification under heavy IO load**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.io.io_scheduling@1`
- `cap.t09.io.io_scheduling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.numa.numa_latency@1` | use the in-file conservative substitute for `numa_latency` (documented, slower, lower quality) and set `degraded['numa_latency']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t07.memory.memory_encryption@1` | use the in-file conservative substitute for `memory_encryption` (documented, slower, lower quality) and set `degraded['memory_encryption']='local'` |
| `cap.t08.multi.multi_gpu_runtime@1` | use the in-file conservative substitute for `multi_gpu_runtime` (documented, slower, lower quality) and set `degraded['multi_gpu_runtime']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - priority IO scheduling with deadline awareness | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - readahead tuning from access-pattern prediction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - IO-latency percentile measurement per class | 520 | Third required mechanism. |
| 6 | Core implementation D - stall-free verification under heavy IO load | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 10000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0430_io_scheduling.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.io.io_scheduling@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 10000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0431 · `adaptive_quality` — Adaptive Quality/Latency Controller

| field | value |
|---|---|
| part id | `P0431` (31/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0431_adaptive_quality.rs` |
| module path | `hyperion.t09.latency.adaptive_quality` |
| capability published | `cap.t09.adaptive.adaptive_quality@1` |
| determinism class | `io` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0431_adaptive_quality.txt`](prompts/P0431_adaptive_quality.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0431-adaptive-quality) |

**Mission.** Trades quality for speed only when explicitly permitted, and says so.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **quality-knob inventory with measured latency/quality effects** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **user-declared preference honoring with transparency** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **closed-loop control with stability guarantees**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured SLO attainment across preference settings** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.adaptive.adaptive_quality@1`
- `cap.t09.adaptive.adaptive_quality.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.io.io_scheduling@1` | use the in-file conservative substitute for `io_scheduling` (documented, slower, lower quality) and set `degraded['io_scheduling']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t07.tool.tool_result_cache@1` | use the in-file conservative substitute for `tool_result_cache` (documented, slower, lower quality) and set `degraded['tool_result_cache']='local'` |
| `cap.t08.deadline.deadline_scheduling@1` | use the in-file conservative substitute for `deadline_scheduling` (documented, slower, lower quality) and set `degraded['deadline_scheduling']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - quality-knob inventory with measured latency/quality effects | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - user-declared preference honoring with transparency | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - closed-loop control with stability guarantees | 520 | Third required mechanism. |
| 6 | Core implementation D - measured SLO attainment across preference settings | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 11000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0431_adaptive_quality.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.adaptive.adaptive_quality@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 11000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0432 · `slo_manager` — SLO Definition, Tracking & Error Budgets

| field | value |
|---|---|
| part id | `P0432` (32/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0432_slo_manager.rs` |
| module path | `hyperion.t09.latency.slo_manager` |
| capability published | `cap.t09.slo.slo_manager@1` |
| determinism class | `io` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0432_slo_manager.txt`](prompts/P0432_slo_manager.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0432-slo-manager) |

**Mission.** Turns latency goals into enforced engineering constraints.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **SLO/SLI definitions per endpoint and request class** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **error-budget accounting and burn-rate alerting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **automatic degradation when budget burns too fast** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **SLO-attainment reporting with statistical rigor** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.slo.slo_manager@1`
- `cap.t09.slo.slo_manager.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.adaptive.adaptive_quality@1` | use the in-file conservative substitute for `adaptive_quality` (documented, slower, lower quality) and set `degraded['adaptive_quality']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t07.temporal.temporal_memory@1` | use the in-file conservative substitute for `temporal_memory` (documented, slower, lower quality) and set `degraded['temporal_memory']='local'` |
| `cap.t08.engine.engine_determinism@1` | use the in-file conservative substitute for `engine_determinism` (documented, slower, lower quality) and set `degraded['engine_determinism']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - SLO/SLI definitions per endpoint and request class | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - error-budget accounting and burn-rate alerting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic degradation when budget burns too fast | 520 | Third required mechanism. |
| 6 | Core implementation D - SLO-attainment reporting with statistical rigor | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 12000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0432_slo_manager.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.slo.slo_manager@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 12000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0433 · `latency_regression_gate` — Latency Regression Gate for 1000 Parts

| field | value |
|---|---|
| part id | `P0433` (33/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0433_latency_regression_gate.rs` |
| module path | `hyperion.t09.latency.latency_regression_gate` |
| capability published | `cap.t09.latency.latency_regression_gate@1` |
| determinism class | `io` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0433_latency_regression_gate.txt`](prompts/P0433_latency_regression_gate.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0433-latency-regression-gate) |

**Mission.** No part can slow the system down without being caught.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **per-part latency budget enforcement in CI**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **statistical change detection resistant to machine noise** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **attribution of end-to-end regressions to specific parts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **gate false-positive/false-negative measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.latency.latency_regression_gate@1`
- `cap.t09.latency.latency_regression_gate.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.slo.slo_manager@1` | use the in-file conservative substitute for `slo_manager` (documented, slower, lower quality) and set `degraded['slo_manager']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t07.memory.memory_bench@1` | use the in-file conservative substitute for `memory_bench` (documented, slower, lower quality) and set `degraded['memory_bench']='local'` |
| `cap.t08.engine.engine_config_tuning@1` | use the in-file conservative substitute for `engine_config_tuning` (documented, slower, lower quality) and set `degraded['engine_config_tuning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-part latency budget enforcement in CI | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - statistical change detection resistant to machine noise | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - attribution of end-to-end regressions to specific parts | 520 | Third required mechanism. |
| 6 | Core implementation D - gate false-positive/false-negative measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 13000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0433_latency_regression_gate.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.latency.latency_regression_gate@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 13000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0434 · `perf_ci` — Continuous Performance Integration

| field | value |
|---|---|
| part id | `P0434` (34/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0434_perf_ci.rs` |
| module path | `hyperion.t09.latency.perf_ci` |
| capability published | `cap.t09.perf.perf_ci@1` |
| determinism class | `io` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0434_perf_ci.txt`](prompts/P0434_perf_ci.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0434-perf-ci) |

**Mission.** Performance is tested as rigorously as correctness.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **reproducible benchmark environment definition and fingerprinting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **per-commit measurement with variance control** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **historical performance database and trend analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **automated bisection of performance regressions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.perf.perf_ci@1`
- `cap.t09.perf.perf_ci.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.latency.latency_regression_gate@1` | use the in-file conservative substitute for `latency_regression_gate` (documented, slower, lower quality) and set `degraded['latency_regression_gate']='local'` |
| `cap.t07.kv.kv_paging@1` | use the in-file conservative substitute for `kv_paging` (documented, slower, lower quality) and set `degraded['kv_paging']='local'` |
| `cap.t08.continuous.continuous_batching@1` | use the in-file conservative substitute for `continuous_batching` (documented, slower, lower quality) and set `degraded['continuous_batching']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - reproducible benchmark environment definition and fingerprinting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-commit measurement with variance control | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - historical performance database and trend analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - automated bisection of performance regressions | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 14000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0434_perf_ci.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.perf.perf_ci@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 14000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0435 · `flamegraph_tooling` — Profiling & Flamegraph Analysis Tooling

| field | value |
|---|---|
| part id | `P0435` (35/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0435_flamegraph_tooling.rs` |
| module path | `hyperion.t09.latency.flamegraph_tooling` |
| capability published | `cap.t09.flamegraph.flamegraph_tooling@1` |
| determinism class | `io` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0435_flamegraph_tooling.txt`](prompts/P0435_flamegraph_tooling.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0435-flamegraph-tooling) |

**Mission.** Finds the next optimisation without guessing.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **low-overhead sampling profiler with symbolisation across languages** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **differential flamegraph comparison between versions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **automatic hotspot ranking with estimated payoff**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **profiler-overhead measurement under 1%** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.flamegraph.flamegraph_tooling@1`
- `cap.t09.flamegraph.flamegraph_tooling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.perf.perf_ci@1` | use the in-file conservative substitute for `perf_ci` (documented, slower, lower quality) and set `degraded['perf_ci']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t07.semantic.semantic_memory@1` | use the in-file conservative substitute for `semantic_memory` (documented, slower, lower quality) and set `degraded['semantic_memory']='local'` |
| `cap.t08.cascade.cascade_tree_verify@1` | use the in-file conservative substitute for `cascade_tree_verify` (documented, slower, lower quality) and set `degraded['cascade_tree_verify']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - low-overhead sampling profiler with symbolisation across languag | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - differential flamegraph comparison between versions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic hotspot ranking with estimated payoff | 520 | Third required mechanism. |
| 6 | Core implementation D - profiler-overhead measurement under 1% | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 15000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0435_flamegraph_tooling.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.flamegraph.flamegraph_tooling@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 15000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0436 · `bottleneck_analyser` — Automatic Bottleneck Analyser

| field | value |
|---|---|
| part id | `P0436` (36/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0436_bottleneck_analyser.rs` |
| module path | `hyperion.t09.latency.bottleneck_analyser` |
| capability published | `cap.t09.bottleneck.bottleneck_analyser@1` |
| determinism class | `io` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0436_bottleneck_analyser.txt`](prompts/P0436_bottleneck_analyser.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0436-bottleneck-analyser) |

**Mission.** Tells engineers exactly what to fix next, ranked by payoff.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **queueing-network model fitted to telemetry** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **bottleneck identification with sensitivity analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **prioritised recommendation list with projected gains** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **prediction accuracy validation on applied fixes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.bottleneck.bottleneck_analyser@1`
- `cap.t09.bottleneck.bottleneck_analyser.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.flamegraph.flamegraph_tooling@1` | use the in-file conservative substitute for `flamegraph_tooling` (documented, slower, lower quality) and set `degraded['flamegraph_tooling']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t07.query.query_reformulation@1` | use the in-file conservative substitute for `query_reformulation` (documented, slower, lower quality) and set `degraded['query_reformulation']='local'` |
| `cap.t08.prefix.prefix_cache_runtime@1` | use the in-file conservative substitute for `prefix_cache_runtime` (documented, slower, lower quality) and set `degraded['prefix_cache_runtime']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - queueing-network model fitted to telemetry | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - bottleneck identification with sensitivity analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - prioritised recommendation list with projected gains | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction accuracy validation on applied fixes | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 16000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0436_bottleneck_analyser.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.bottleneck.bottleneck_analyser@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 16000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0437 · `throughput_optimiser` — Throughput Optimisation Engine

| field | value |
|---|---|
| part id | `P0437` (37/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0437_throughput_optimiser.rs` |
| module path | `hyperion.t09.latency.throughput_optimiser` |
| capability published | `cap.t09.throughput.throughput_optimiser@1` |
| determinism class | `io` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0437_throughput_optimiser.txt`](prompts/P0437_throughput_optimiser.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0437-throughput-optimiser) |

**Mission.** Maximises tokens per dollar at fixed latency.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **capacity-planning model coupling batching, sparsity and precision**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **constrained optimisation with SLO feasibility checking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **measured tokens-per-dollar improvement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **sensitivity to traffic-mix changes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.throughput.throughput_optimiser@1`
- `cap.t09.throughput.throughput_optimiser.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.bottleneck.bottleneck_analyser@1` | use the in-file conservative substitute for `bottleneck_analyser` (documented, slower, lower quality) and set `degraded['bottleneck_analyser']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t07.memory.memory_privacy@1` | use the in-file conservative substitute for `memory_privacy` (documented, slower, lower quality) and set `degraded['memory_privacy']='local'` |
| `cap.t08.batch.batch_invariance@1` | use the in-file conservative substitute for `batch_invariance` (documented, slower, lower quality) and set `degraded['batch_invariance']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capacity-planning model coupling batching, sparsity and precisio | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - constrained optimisation with SLO feasibility checking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - measured tokens-per-dollar improvement | 520 | Third required mechanism. |
| 6 | Core implementation D - sensitivity to traffic-mix changes | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 17000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0437_throughput_optimiser.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.throughput.throughput_optimiser@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 17000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0438 · `energy_efficiency` — Energy per Token Optimisation

| field | value |
|---|---|
| part id | `P0438` (38/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0438_energy_efficiency.rs` |
| module path | `hyperion.t09.latency.energy_efficiency` |
| capability published | `cap.t09.energy.energy_efficiency@1` |
| determinism class | `io` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0438_energy_efficiency.txt`](prompts/P0438_energy_efficiency.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0438-energy-efficiency) |

**Mission.** Speed that does not come from burning more power.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **joules-per-token measurement methodology and instrumentation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **frequency/precision/sparsity joint optimisation for efficiency** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **carbon accounting integration** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured efficiency improvement at matched quality**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.energy.energy_efficiency@1`
- `cap.t09.energy.energy_efficiency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.throughput.throughput_optimiser@1` | use the in-file conservative substitute for `throughput_optimiser` (documented, slower, lower quality) and set `degraded['throughput_optimiser']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t07.semantic.semantic_cache@1` | use the in-file conservative substitute for `semantic_cache` (documented, slower, lower quality) and set `degraded['semantic_cache']='local'` |
| `cap.t08.cancellation.cancellation@1` | use the in-file conservative substitute for `cancellation` (documented, slower, lower quality) and set `degraded['cancellation']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - joules-per-token measurement methodology and instrumentation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - frequency/precision/sparsity joint optimisation for efficiency | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - carbon accounting integration | 520 | Third required mechanism. |
| 6 | Core implementation D - measured efficiency improvement at matched quality | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 18000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0438_energy_efficiency.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.energy.energy_efficiency@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 18000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0439 · `cost_optimiser` — Cost per Solved Task Optimiser

| field | value |
|---|---|
| part id | `P0439` (39/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0439_cost_optimiser.rs` |
| module path | `hyperion.t09.latency.cost_optimiser` |
| capability published | `cap.t09.cost.cost_optimiser@1` |
| determinism class | `io` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0439_cost_optimiser.txt`](prompts/P0439_cost_optimiser.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0439-cost-optimiser) |

**Mission.** The only metric that matters: dollars per correct answer.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **cost-per-success accounting including retries and verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **policy optimisation over model tier, search depth and tools** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **comparison against Opus 5 published pricing on identical tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 100x cheaper per solved task on the benchmark suite** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.cost.cost_optimiser@1`
- `cap.t09.cost.cost_optimiser.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.energy.energy_efficiency@1` | use the in-file conservative substitute for `energy_efficiency` (documented, slower, lower quality) and set `degraded['energy_efficiency']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t07.graph.graph_memory_queries@1` | use the in-file conservative substitute for `graph_memory_queries` (documented, slower, lower quality) and set `degraded['graph_memory_queries']='local'` |
| `cap.t08.overload.overload_shedding@1` | use the in-file conservative substitute for `overload_shedding` (documented, slower, lower quality) and set `degraded['overload_shedding']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cost-per-success accounting including retries and verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - policy optimisation over model tier, search depth and tools | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - comparison against Opus 5 published pricing on identical tasks | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 100x cheaper per solved task on the benchmark suite | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 19000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0439_cost_optimiser.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.cost.cost_optimiser@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 19000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0440 · `capacity_planner` — Capacity Planning & Headroom Model

| field | value |
|---|---|
| part id | `P0440` (40/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0440_capacity_planner.rs` |
| module path | `hyperion.t09.latency.capacity_planner` |
| capability published | `cap.t09.capacity.capacity_planner@1` |
| determinism class | `io` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0440_capacity_planner.txt`](prompts/P0440_capacity_planner.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0440-capacity-planner) |

**Mission.** Enough capacity, never too much.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **demand forecasting with uncertainty quantification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **headroom policy derived from failure and burst analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cost-of-headroom versus risk-of-shortfall tradeoff** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **forecast accuracy measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.capacity.capacity_planner@1`
- `cap.t09.capacity.capacity_planner.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.cost.cost_optimiser@1` | use the in-file conservative substitute for `cost_optimiser` (documented, slower, lower quality) and set `degraded['cost_optimiser']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t07.provenance.provenance_tracking@1` | use the in-file conservative substitute for `provenance_tracking` (documented, slower, lower quality) and set `degraded['provenance_tracking']='local'` |
| `cap.t08.cascade.cascade_speed_proof@1` | use the in-file conservative substitute for `cascade_speed_proof` (documented, slower, lower quality) and set `degraded['cascade_speed_proof']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - demand forecasting with uncertainty quantification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - headroom policy derived from failure and burst analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost-of-headroom versus risk-of-shortfall tradeoff | 520 | Third required mechanism. |
| 6 | Core implementation D - forecast accuracy measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 20000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0440_capacity_planner.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.capacity.capacity_planner@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 20000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0441 · `cache_sizing` — Cache Sizing & Memory Allocation Optimiser

| field | value |
|---|---|
| part id | `P0441` (41/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0441_cache_sizing.rs` |
| module path | `hyperion.t09.latency.cache_sizing` |
| capability published | `cap.t09.cache.cache_sizing@1` |
| determinism class | `io` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0441_cache_sizing.txt`](prompts/P0441_cache_sizing.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0441-cache-sizing) |

**Mission.** Splits limited memory across ten caches optimally.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **marginal-hit-rate curves per cache measured online**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **global allocation solver maximising total value** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **dynamic reallocation with hysteresis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured improvement over fixed allocation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.cache.cache_sizing@1`
- `cap.t09.cache.cache_sizing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.capacity.capacity_planner@1` | use the in-file conservative substitute for `capacity_planner` (documented, slower, lower quality) and set `degraded['capacity_planner']='local'` |
| `cap.t07.kv.kv_hierarchy@1` | use the in-file conservative substitute for `kv_hierarchy` (documented, slower, lower quality) and set `degraded['kv_hierarchy']='local'` |
| `cap.t08.engine.engine_core@1` | use the in-file conservative substitute for `engine_core` (documented, slower, lower quality) and set `degraded['engine_core']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - marginal-hit-rate curves per cache measured online | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - global allocation solver maximising total value | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - dynamic reallocation with hysteresis | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement over fixed allocation | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 21000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0441_cache_sizing.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.cache.cache_sizing@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 21000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0442 · `speculation_budget` — Speculation Budget Governor

| field | value |
|---|---|
| part id | `P0442` (42/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0442_speculation_budget.rs` |
| module path | `hyperion.t09.latency.speculation_budget` |
| capability published | `cap.t09.speculation.speculation_budget@1` |
| determinism class | `io` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0442_speculation_budget.txt`](prompts/P0442_speculation_budget.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0442-speculation-budget) |

**Mission.** Speculation must never cost more than it saves.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **global speculation budget with per-source accounting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **value-of-speculation estimation and dynamic throttling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **wasted-work measurement across all speculative subsystems** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **net-benefit verification with confidence intervals**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.speculation.speculation_budget@1`
- `cap.t09.speculation.speculation_budget.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.cache.cache_sizing@1` | use the in-file conservative substitute for `cache_sizing` (documented, slower, lower quality) and set `degraded['cache_sizing']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t07.episodic.episodic_memory@1` | use the in-file conservative substitute for `episodic_memory` (documented, slower, lower quality) and set `degraded['episodic_memory']='local'` |
| `cap.t08.cascade.cascade_stage3_draft@1` | use the in-file conservative substitute for `cascade_stage3_draft` (documented, slower, lower quality) and set `degraded['cascade_stage3_draft']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - global speculation budget with per-source accounting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - value-of-speculation estimation and dynamic throttling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - wasted-work measurement across all speculative subsystems | 520 | Third required mechanism. |
| 6 | Core implementation D - net-benefit verification with confidence intervals | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 22000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0442_speculation_budget.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.speculation.speculation_budget@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 22000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0443 · `latency_simulator` — Latency Simulator & What-If Engine

| field | value |
|---|---|
| part id | `P0443` (43/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0443_latency_simulator.rs` |
| module path | `hyperion.t09.latency.latency_simulator` |
| capability published | `cap.t09.latency.latency_simulator@1` |
| determinism class | `io` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0443_latency_simulator.txt`](prompts/P0443_latency_simulator.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0443-latency-simulator) |

**Mission.** Tests optimisation ideas before building them.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **discrete-event simulation of the full request path** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **calibration against production measurements with error bounds** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **what-if scenario library for planned changes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **prediction-accuracy validation on implemented changes** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.latency.latency_simulator@1`
- `cap.t09.latency.latency_simulator.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.speculation.speculation_budget@1` | use the in-file conservative substitute for `speculation_budget` (documented, slower, lower quality) and set `degraded['speculation_budget']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t07.hybrid.hybrid_retrieval@1` | use the in-file conservative substitute for `hybrid_retrieval` (documented, slower, lower quality) and set `degraded['hybrid_retrieval']='local'` |
| `cap.t08.paged.paged_attention_runtime@1` | use the in-file conservative substitute for `paged_attention_runtime` (documented, slower, lower quality) and set `degraded['paged_attention_runtime']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - discrete-event simulation of the full request path | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - calibration against production measurements with error bounds | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - what-if scenario library for planned changes | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction-accuracy validation on implemented changes | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 23000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0443_latency_simulator.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.latency.latency_simulator@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 23000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0444 · `benchmark_speed_public` — Public Speed Comparison Harness

| field | value |
|---|---|
| part id | `P0444` (44/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0444_benchmark_speed_public.rs` |
| module path | `hyperion.t09.latency.benchmark_speed_public` |
| capability published | `cap.t09.benchmark.benchmark_speed_public@1` |
| determinism class | `io` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0444_benchmark_speed_public.txt`](prompts/P0444_benchmark_speed_public.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0444-benchmark-speed-public) |

**Mission.** Reproducible, fair, third-party-verifiable speed comparisons.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **identical-task-set methodology against Opus-class baselines** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **measurement of wall-clock, tokens, cost and quality together**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **publication-ready result artifacts with full provenance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **independent-reproduction instructions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.benchmark.benchmark_speed_public@1`
- `cap.t09.benchmark.benchmark_speed_public.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.latency.latency_simulator@1` | use the in-file conservative substitute for `latency_simulator` (documented, slower, lower quality) and set `degraded['latency_simulator']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t07.conflict.conflict_resolution@1` | use the in-file conservative substitute for `conflict_resolution` (documented, slower, lower quality) and set `degraded['conflict_resolution']='local'` |
| `cap.t08.streaming.streaming_output@1` | use the in-file conservative substitute for `streaming_output` (documented, slower, lower quality) and set `degraded['streaming_output']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - identical-task-set methodology against Opus-class baselines | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - measurement of wall-clock, tokens, cost and quality together | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - publication-ready result artifacts with full provenance | 520 | Third required mechanism. |
| 6 | Core implementation D - independent-reproduction instructions | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 24000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0444_benchmark_speed_public.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.benchmark.benchmark_speed_public@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 24000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0445 · `realtime_mode` — Real-Time & Voice-Latency Mode

| field | value |
|---|---|
| part id | `P0445` (45/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0445_realtime_mode.rs` |
| module path | `hyperion.t09.latency.realtime_mode` |
| capability published | `cap.t09.realtime.realtime_mode@1` |
| determinism class | `io` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0445_realtime_mode.txt`](prompts/P0445_realtime_mode.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0445-realtime-mode) |

**Mission.** Sub-100ms interaction for conversational and control use.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **streaming input processing with incremental commitment**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **barge-in handling and partial-hypothesis revision** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **end-to-end audio-to-audio latency measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **quality-at-latency measurement versus batch mode** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.realtime.realtime_mode@1`
- `cap.t09.realtime.realtime_mode.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.benchmark.benchmark_speed_public@1` | use the in-file conservative substitute for `benchmark_speed_public` (documented, slower, lower quality) and set `degraded['benchmark_speed_public']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t07.cache.cache_warm_predict@1` | use the in-file conservative substitute for `cache_warm_predict` (documented, slower, lower quality) and set `degraded['cache_warm_predict']='local'` |
| `cap.t08.request.request_lifecycle@1` | use the in-file conservative substitute for `request_lifecycle` (documented, slower, lower quality) and set `degraded['request_lifecycle']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - streaming input processing with incremental commitment | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - barge-in handling and partial-hypothesis revision | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - end-to-end audio-to-audio latency measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - quality-at-latency measurement versus batch mode | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 25000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0445_realtime_mode.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.realtime.realtime_mode@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 25000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0446 · `burst_handling` — Burst Absorption & Queue Shaping

| field | value |
|---|---|
| part id | `P0446` (46/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0446_burst_handling.rs` |
| module path | `hyperion.t09.latency.burst_handling` |
| capability published | `cap.t09.burst.burst_handling@1` |
| determinism class | `io` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0446_burst_handling.txt`](prompts/P0446_burst_handling.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0446-burst-handling) |

**Mission.** A 100x traffic spike is a bump, not an outage.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **burst detection and rapid capacity engagement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **queue shaping with explicit wait-time communication** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **priority preservation during bursts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured behaviour under synthetic 100x spikes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.burst.burst_handling@1`
- `cap.t09.burst.burst_handling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.realtime.realtime_mode@1` | use the in-file conservative substitute for `realtime_mode` (documented, slower, lower quality) and set `degraded['realtime_mode']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t07.memory.memory_replication@1` | use the in-file conservative substitute for `memory_replication` (documented, slower, lower quality) and set `degraded['memory_replication']='local'` |
| `cap.t08.autoscaling.autoscaling@1` | use the in-file conservative substitute for `autoscaling` (documented, slower, lower quality) and set `degraded['autoscaling']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - burst detection and rapid capacity engagement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - queue shaping with explicit wait-time communication | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - priority preservation during bursts | 520 | Third required mechanism. |
| 6 | Core implementation D - measured behaviour under synthetic 100x spikes | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 26000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0446_burst_handling.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.burst.burst_handling@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 26000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0447 · `degradation_ladder` — Formal Degradation Ladder

| field | value |
|---|---|
| part id | `P0447` (47/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0447_degradation_ladder.rs` |
| module path | `hyperion.t09.latency.degradation_ladder` |
| capability published | `cap.t09.degradation.degradation_ladder@1` |
| determinism class | `io` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0447_degradation_ladder.txt`](prompts/P0447_degradation_ladder.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0447-degradation-ladder) |

**Mission.** Exactly how quality is traded for availability, documented.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **ordered degradation steps with measured quality/latency effects** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **automatic trigger conditions and recovery criteria** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **user-visible signalling of the active degradation level**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **verification that each step behaves as specified** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.degradation.degradation_ladder@1`
- `cap.t09.degradation.degradation_ladder.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.burst.burst_handling@1` | use the in-file conservative substitute for `burst_handling` (documented, slower, lower quality) and set `degraded['burst_handling']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t07.dedup.dedup_engine@1` | use the in-file conservative substitute for `dedup_engine` (documented, slower, lower quality) and set `degraded['dedup_engine']='local'` |
| `cap.t08.engine.engine_bench_serving@1` | use the in-file conservative substitute for `engine_bench_serving` (documented, slower, lower quality) and set `degraded['engine_bench_serving']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - ordered degradation steps with measured quality/latency effects | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automatic trigger conditions and recovery criteria | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - user-visible signalling of the active degradation level | 520 | Third required mechanism. |
| 6 | Core implementation D - verification that each step behaves as specified | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 27000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0447_degradation_ladder.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.degradation.degradation_ladder@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 27000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0448 · `latency_dashboard` — Latency & Cost Observability Artifacts

| field | value |
|---|---|
| part id | `P0448` (48/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0448_latency_dashboard.rs` |
| module path | `hyperion.t09.latency.latency_dashboard` |
| capability published | `cap.t09.latency.latency_dashboard@1` |
| determinism class | `io` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0448_latency_dashboard.txt`](prompts/P0448_latency_dashboard.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0448-latency-dashboard) |

**Mission.** One place to see whether the 100x claim still holds.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **metric definitions, aggregation rules and export schemas** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Terminal-Bench 2.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-part and per-phase drilldown data products**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **regression and anomaly annotation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **operator-task usability validation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t09.latency.latency_dashboard@1`
- `cap.t09.latency.latency_dashboard.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.degradation.degradation_ladder@1` | use the in-file conservative substitute for `degradation_ladder` (documented, slower, lower quality) and set `degraded['degradation_ladder']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t07.memory.memory_spec_doc@1` | use the in-file conservative substitute for `memory_spec_doc` (documented, slower, lower quality) and set `degraded['memory_spec_doc']='local'` |
| `cap.t08.engine.engine_spec_doc@1` | use the in-file conservative substitute for `engine_spec_doc` (documented, slower, lower quality) and set `degraded['engine_spec_doc']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - metric definitions, aggregation rules and export schemas | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-part and per-phase drilldown data products | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regression and anomaly annotation | 520 | Third required mechanism. |
| 6 | Core implementation D - operator-task usability validation | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 28000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0448_latency_dashboard.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.latency.latency_dashboard@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 28000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0449 · `speed_proof_report` — The 100x Speed Proof Report Generator

| field | value |
|---|---|
| part id | `P0449` (49/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0449_speed_proof_report.rs` |
| module path | `hyperion.t09.latency.speed_proof_report` |
| capability published | `cap.t09.speed.speed_proof_report@1` |
| determinism class | `io` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0449_speed_proof_report.txt`](prompts/P0449_speed_proof_report.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0449-speed-proof-report) |

**Mission.** Generates the auditable document proving 100x versus Opus 5.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **measurement collection across all six speed sources**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **task-matched wall-clock comparison methodology** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **statistical treatment with confidence intervals and caveats** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **reproducibility package with scripts and raw data** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t09.speed.speed_proof_report@1`
- `cap.t09.speed.speed_proof_report.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.latency.latency_dashboard@1` | use the in-file conservative substitute for `latency_dashboard` (documented, slower, lower quality) and set `degraded['latency_dashboard']='local'` |
| `cap.t07.summarisation.summarisation_memory@1` | use the in-file conservative substitute for `summarisation_memory` (documented, slower, lower quality) and set `degraded['summarisation_memory']='local'` |
| `cap.t08.cascade.cascade_stage2_draft@1` | use the in-file conservative substitute for `cascade_stage2_draft` (documented, slower, lower quality) and set `degraded['cascade_stage2_draft']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - measurement collection across all six speed sources | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - task-matched wall-clock comparison methodology | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - statistical treatment with confidence intervals and caveats | 520 | Third required mechanism. |
| 6 | Core implementation D - reproducibility package with scripts and raw data | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 29000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0449_speed_proof_report.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.speed.speed_proof_report@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 29000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0450 · `latency_spec_doc` — Latency Engineering Specification & Runbook

| field | value |
|---|---|
| part id | `P0450` (50/50 of T09) |
| tier | `T09` — Latency Engineering & Ω-Memoize |
| language | Rust 1.86 |
| file to produce | `parts/t09_latency/P0450_latency_spec_doc.rs` |
| module path | `hyperion.t09.latency.latency_spec_doc` |
| capability published | `cap.t09.latency.latency_spec_doc@1` |
| determinism class | `io` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Terminal-Bench 2.1, CursorBench 3.2 |
| worker prompt | [`prompts/P0450_latency_spec_doc.txt`](prompts/P0450_latency_spec_doc.txt) · [inline](docs/PROMPTS_T09.md#prompt-p0450-latency-spec-doc) |

**Mission.** The authoritative description of all latency machinery.

**Tier context.** Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.

**Mandate — all four items are required; none is optional.**

1. Implement **specification of budgets, SLOs, caches and degradation modes** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Terminal-Bench 2.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **auto-generated budget tables per part and phase** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **incident runbook for latency regressions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Terminal-Bench 2.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **spec-versus-implementation drift detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t09.latency.latency_spec_doc@1`
- `cap.t09.latency.latency_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t09.speed.speed_proof_report@1` | use the in-file conservative substitute for `speed_proof_report` (documented, slower, lower quality) and set `degraded['speed_proof_report']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t07.sparse.sparse_retrieval@1` | use the in-file conservative substitute for `sparse_retrieval` (documented, slower, lower quality) and set `degraded['sparse_retrieval']='local'` |
| `cap.t08.cascade.cascade_tuning@1` | use the in-file conservative substitute for `cascade_tuning` (documented, slower, lower quality) and set `degraded['cascade_tuning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - specification of budgets, SLOs, caches and degradation modes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - auto-generated budget tables per part and phase | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - incident runbook for latency regressions | 520 | Third required mechanism. |
| 6 | Core implementation D - spec-versus-implementation drift detection | 480 | Fourth required mechanism, including its measurement/assertion path. |
| 7 | Ω-Bus integration: register(), describe(), capability handles | 210 | Idempotent registration, schema export, handle lifetime and teardown. |
| 8 | Degradation ladder: declared fallbacks for every required capability | 200 | For each entry in `requires`, a working local fallback + quality annotation. |
| 9 | Error paths, budget/deadline handling, partial results | 250 | Every OmegaCode this part can emit, with remedy text and retryability. |
| 10 | Observability: events, counters, histograms, latency attribution | 150 | Structured events only; no stdout. Counters registered through T20 telemetry. |
| 11 | Determinism harness: split_seed usage, replay, batch-invariance | 170 | Proves the declared determinism class holds. |
| 12 | In-file test suite: >= 40 cases (unit + boundary + regression) | 440 | pytest/cfg(test)/vitest style per language, no shared fixtures, offline. |
| 13 | Property-based tests for every stated invariant | 250 | Generators + shrinkers; each invariant named in a comment. |
| 14 | Adversarial / fuzz tests | 170 | Coverage-guided in-process fuzzing within the 60s budget. |
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 30000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t09_latency/P0450_latency_spec_doc.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t09.latency.latency_spec_doc@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 30000 ns at the declared reference shape.
- [ ] Declared determinism class `io` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---
