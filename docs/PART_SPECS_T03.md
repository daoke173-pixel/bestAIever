# HYPERION-Ω — Part specifications · T03 · Graph IR, Compiler & Autotuner

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Rust 1.86

**Tier mission.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Benchmarks this tier is accountable for.** SWE-bench Verified

**Tier dependencies.** T01, T02

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0101](#p0101-ir-core) | `ir_core` | Ω-IR Core Data Structures | `cap.t03.ir.ir_core@1` |
| [P0102](#p0102-ir-builder) | `ir_builder` | IR Construction & Tracing Frontend | `cap.t03.ir.ir_builder@1` |
| [P0103](#p0103-ir-printer) | `ir_printer` | IR Textual Format, Parser & Round-Trip | `cap.t03.ir.ir_printer@1` |
| [P0104](#p0104-pass-manager) | `pass_manager` | Pass Manager & Optimisation Pipelines | `cap.t03.pass.pass_manager@1` |
| [P0105](#p0105-shape-inference) | `shape_inference` | Symbolic Shape Inference & Constraint Solver | `cap.t03.shape.shape_inference@1` |
| [P0106](#p0106-dtype-promotion) | `dtype_promotion` | Precision Assignment & Mixed-Precision Planner | `cap.t03.dtype.dtype_promotion@1` |
| [P0107](#p0107-algebraic-rewrite) | `algebraic_rewrite` | Algebraic Simplification & Rewrite Engine | `cap.t03.algebraic.algebraic_rewrite@1` |
| [P0108](#p0108-fusion-pass) | `fusion_pass` | Operator Fusion Pass | `cap.t03.fusion.fusion_pass@1` |
| [P0109](#p0109-layout-assignment) | `layout_assignment` | Layout Assignment & Relayout Minimisation | `cap.t03.layout.layout_assignment@1` |
| [P0110](#p0110-memory-planner) | `memory_planner` | Static Memory Planner & Liveness Allocator | `cap.t03.memory.memory_planner@1` |
| [P0111](#p0111-rematerialisation) | `rematerialisation` | Activation Rematerialisation Planner | `cap.t03.rematerialisat.rematerialisation@1` |
| [P0112](#p0112-scheduler-pass) | `scheduler_pass` | Instruction Scheduling & Overlap Pass | `cap.t03.scheduler.scheduler_pass@1` |
| [P0113](#p0113-parallel-partition) | `parallel_partition` | Automatic Parallelism Partitioner | `cap.t03.parallel.parallel_partition@1` |
| [P0114](#p0114-pipeline-planner) | `pipeline_planner` | Pipeline Parallel Schedule Synthesiser | `cap.t03.pipeline.pipeline_planner@1` |
| [P0115](#p0115-collective-insertion) | `collective_insertion` | Collective Communication Insertion & Fusion | `cap.t03.collective.collective_insertion@1` |
| [P0116](#p0116-autotuner-core) | `autotuner_core` | Autotuning Search Engine | `cap.t03.autotuner.autotuner_core@1` |
| [P0117](#p0117-cost-model-learned) | `cost_model_learned` | Learned Cost Model | `cap.t03.cost.cost_model_learned@1` |
| [P0118](#p0118-codegen-gpu) | `codegen_gpu` | Accelerator Code Generator | `cap.t03.codegen.codegen_gpu@1` |
| [P0119](#p0119-codegen-cpu) | `codegen_cpu` | CPU Code Generator | `cap.t03.codegen.codegen_cpu@1` |
| [P0120](#p0120-jit-cache-compiler) | `jit_cache_compiler` | Compilation Cache & Warm Start | `cap.t03.jit.jit_cache_compiler@1` |
| [P0121](#p0121-guard-specialise) | `guard_specialise` | Guarded Specialisation & Recompilation Policy | `cap.t03.guard.guard_specialise@1` |
| [P0122](#p0122-kernel-selection) | `kernel_selection` | Global Kernel Selection Optimiser | `cap.t03.kernel.kernel_selection@1` |
| [P0123](#p0123-graph-partition-device) | `graph_partition_device` | Device Placement & Graph Partitioning | `cap.t03.graph.graph_partition_device@1` |
| [P0124](#p0124-dynamic-shapes) | `dynamic_shapes` | Dynamic Shape Execution Strategy | `cap.t03.dynamic.dynamic_shapes@1` |
| [P0125](#p0125-differentiation) | `differentiation` | Automatic Differentiation on Ω-IR | `cap.t03.differentiatio.differentiation@1` |
| [P0126](#p0126-vectorisation-transform) | `vectorisation_transform` | Batching & Vectorisation Transform | `cap.t03.vectorisation.vectorisation_transform@1` |
| [P0127](#p0127-loop-transform) | `loop_transform` | Polyhedral Loop Transformation | `cap.t03.loop.loop_transform@1` |
| [P0128](#p0128-constant-folding) | `constant_folding` | Constant Folding & Weight Preprocessing | `cap.t03.constant.constant_folding@1` |
| [P0129](#p0129-dead-code-dce) | `dead_code_dce` | Dead Code, CSE & Canonicalisation | `cap.t03.dead.dead_code_dce@1` |
| [P0130](#p0130-effect-system) | `effect_system` | Effect & Purity Analysis | `cap.t03.effect.effect_system@1` |
| [P0131](#p0131-ir-verifier) | `ir_verifier` | IR Verification & Invariant Checking | `cap.t03.ir.ir_verifier@1` |
| [P0132](#p0132-differential-testing) | `differential_testing` | Compiler Differential Test Harness | `cap.t03.differential.differential_testing@1` |
| [P0133](#p0133-compile-time-budget) | `compile_time_budget` | Compilation Time Budget Manager | `cap.t03.compile.compile_time_budget@1` |
| [P0134](#p0134-profile-guided) | `profile_guided` | Profile-Guided Optimisation Pipeline | `cap.t03.profile.profile_guided@1` |
| [P0135](#p0135-target-description) | `target_description` | Target Machine Description Language | `cap.t03.target.target_description@1` |
| [P0136](#p0136-ir-serialization) | `ir_serialization` | IR Serialisation & Portable Artifact Format | `cap.t03.ir.ir_serialization@1` |
| [P0137](#p0137-bytecode-vm) | `bytecode_vm` | Ω Execution Bytecode & Interpreter | `cap.t03.bytecode.bytecode_vm@1` |
| [P0138](#p0138-debug-symbols) | `debug_symbols` | Debug Info, Source Mapping & Blame | `cap.t03.debug.debug_symbols@1` |
| [P0139](#p0139-pass-search) | `pass_search` | Automated Pass Pipeline Search | `cap.t03.pass.pass_search@1` |
| [P0140](#p0140-superoptimiser) | `superoptimiser` | Bounded Superoptimiser for Hot Kernels | `cap.t03.superoptimiser.superoptimiser@1` |
| [P0141](#p0141-equality-saturation) | `equality_saturation` | E-Graph Engine & Extraction | `cap.t03.equality.equality_saturation@1` |
| [P0142](#p0142-kernel-template-lib) | `kernel_template_lib` | Kernel Template Library | `cap.t03.kernel.kernel_template_lib@1` |
| [P0143](#p0143-linker-omega) | `linker_omega` | Ω-Linker for 1000 Compiled Parts | `cap.t03.linker.linker_omega@1` |
| [P0144](#p0144-incremental-build) | `incremental_build` | Incremental Compilation & Change Impact | `cap.t03.incremental.incremental_build@1` |
| [P0145](#p0145-crosscompile) | `crosscompile` | Cross-Compilation & Target Matrix | `cap.t03.crosscompile.crosscompile@1` |
| [P0146](#p0146-numeric-mode-lowering) | `numeric_mode_lowering` | Determinism-Mode Lowering | `cap.t03.numeric.numeric_mode_lowering@1` |
| [P0147](#p0147-op-registry) | `op_registry` | Operator Registry & Semantics Database | `cap.t03.op.op_registry@1` |
| [P0148](#p0148-graph-diff-tool) | `graph_diff_tool` | Graph Diff & Optimisation Explainer | `cap.t03.graph.graph_diff_tool@1` |
| [P0149](#p0149-compiler-fuzzer) | `compiler_fuzzer` | Compiler Fuzzer & Miscompile Hunter | `cap.t03.compiler.compiler_fuzzer@1` |
| [P0150](#p0150-build-provenance) | `build_provenance` | Build Provenance & Reproducibility Attestation | `cap.t03.build.build_provenance@1` |

---

### P0101 · `ir_core` — Ω-IR Core Data Structures

| field | value |
|---|---|
| part id | `P0101` (1/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0101_ir_core.rs` |
| module path | `hyperion.t03.compiler.ir_core` |
| capability published | `cap.t03.ir.ir_core@1` |
| determinism class | `pure` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0101_ir_core.txt`](prompts/P0101_ir_core.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0101-ir-core) |

**Mission.** The SSA-based graph IR that all compilation and optimisation operates on.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **typed SSA with regions, blocks and explicit effect edges**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **shape/dtype/device/determinism attributes on every value** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **structural hashing and interning for O(1) equality** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **verifier catching every malformed-IR class with precise diagnostics** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.ir.ir_core@1`
- `cap.t03.ir.ir_core.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t02.fused.fused_moe_kernel@1` | use the in-file conservative substitute for `fused_moe_kernel` (documented, slower, lower quality) and set `degraded['fused_moe_kernel']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - typed SSA with regions, blocks and explicit effect edges | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - shape/dtype/device/determinism attributes on every value | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - structural hashing and interning for O(1) equality | 520 | Third required mechanism. |
| 6 | Core implementation D - verifier catching every malformed-IR class with precise diagnost | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0101_ir_core.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.ir.ir_core@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 10000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0102 · `ir_builder` — IR Construction & Tracing Frontend

| field | value |
|---|---|
| part id | `P0102` (2/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0102_ir_builder.rs` |
| module path | `hyperion.t03.compiler.ir_builder` |
| capability published | `cap.t03.ir.ir_builder@1` |
| determinism class | `pure` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0102_ir_builder.txt`](prompts/P0102_ir_builder.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0102-ir-builder) |

**Mission.** Captures model code into Ω-IR without behavioural surprises.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **tracing with control-flow capture and guard generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **symbolic-shape propagation during capture** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **side-effect ordering preservation and explicit barriers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **trace-vs-eager equivalence differential tests**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.ir.ir_builder@1`
- `cap.t03.ir.ir_builder.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.ir.ir_core@1` | use the in-file conservative substitute for `ir_core` (documented, slower, lower quality) and set `degraded['ir_core']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t02.numa.numa_placement@1` | use the in-file conservative substitute for `numa_placement` (documented, slower, lower quality) and set `degraded['numa_placement']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tracing with control-flow capture and guard generation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - symbolic-shape propagation during capture | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - side-effect ordering preservation and explicit barriers | 520 | Third required mechanism. |
| 6 | Core implementation D - trace-vs-eager equivalence differential tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0102_ir_builder.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.ir.ir_builder@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 11000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0103 · `ir_printer` — IR Textual Format, Parser & Round-Trip

| field | value |
|---|---|
| part id | `P0103` (3/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0103_ir_printer.rs` |
| module path | `hyperion.t03.compiler.ir_printer` |
| capability published | `cap.t03.ir.ir_printer@1` |
| determinism class | `pure` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0103_ir_printer.txt`](prompts/P0103_ir_printer.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0103-ir-printer) |

**Mission.** Human-readable IR that round-trips exactly, essential for 1000-way debugging.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **stable textual syntax with attribute pretty-printing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **parser accepting the full grammar with error recovery** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **round-trip fidelity property test over random IR**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **diff-friendly canonical ordering** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.ir.ir_printer@1`
- `cap.t03.ir.ir_printer.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.ir.ir_builder@1` | use the in-file conservative substitute for `ir_builder` (documented, slower, lower quality) and set `degraded['ir_builder']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t02.kernel.kernel_fusion_rules@1` | use the in-file conservative substitute for `kernel_fusion_rules` (documented, slower, lower quality) and set `degraded['kernel_fusion_rules']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - stable textual syntax with attribute pretty-printing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - parser accepting the full grammar with error recovery | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - round-trip fidelity property test over random IR | 520 | Third required mechanism. |
| 6 | Core implementation D - diff-friendly canonical ordering | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0103_ir_printer.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.ir.ir_printer@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 12000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0104 · `pass_manager` — Pass Manager & Optimisation Pipelines

| field | value |
|---|---|
| part id | `P0104` (4/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0104_pass_manager.rs` |
| module path | `hyperion.t03.compiler.pass_manager` |
| capability published | `cap.t03.pass.pass_manager@1` |
| determinism class | `pure` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0104_pass_manager.txt`](prompts/P0104_pass_manager.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0104-pass-manager) |

**Mission.** Orchestrates passes with dependency, invalidation and instrumentation support.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **analysis caching with precise invalidation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **pipeline description language and preset pipelines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-pass timing, IR-size and diagnostic capture** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **pass-ordering search harness for pipeline tuning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.pass.pass_manager@1`
- `cap.t03.pass.pass_manager.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.ir.ir_printer@1` | use the in-file conservative substitute for `ir_printer` (documented, slower, lower quality) and set `degraded['ir_printer']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t02.sparse.sparse_attention_kernels@1` | use the in-file conservative substitute for `sparse_attention_kernels` (documented, slower, lower quality) and set `degraded['sparse_attention_kernels']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - analysis caching with precise invalidation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - pipeline description language and preset pipelines | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-pass timing, IR-size and diagnostic capture | 520 | Third required mechanism. |
| 6 | Core implementation D - pass-ordering search harness for pipeline tuning | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0104_pass_manager.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.pass.pass_manager@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 13000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0105 · `shape_inference` — Symbolic Shape Inference & Constraint Solver

| field | value |
|---|---|
| part id | `P0105` (5/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0105_shape_inference.rs` |
| module path | `hyperion.t03.compiler.shape_inference` |
| capability published | `cap.t03.shape.shape_inference@1` |
| determinism class | `pure` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0105_shape_inference.txt`](prompts/P0105_shape_inference.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0105-shape-inference) |

**Mission.** Resolves dynamic shapes to a small set of specialised plans.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **symbolic dimension algebra with guard accumulation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **constraint solving for divisibility and bounds** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **shape-bucket selection minimising padding and recompiles** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **unsat diagnosis pointing at the offending op** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.shape.shape_inference@1`
- `cap.t03.shape.shape_inference.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.pass.pass_manager@1` | use the in-file conservative substitute for `pass_manager` (documented, slower, lower quality) and set `degraded['pass_manager']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t02.tensor.tensor_core_util@1` | use the in-file conservative substitute for `tensor_core_util` (documented, slower, lower quality) and set `degraded['tensor_core_util']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - symbolic dimension algebra with guard accumulation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - constraint solving for divisibility and bounds | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - shape-bucket selection minimising padding and recompiles | 520 | Third required mechanism. |
| 6 | Core implementation D - unsat diagnosis pointing at the offending op | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0105_shape_inference.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.shape.shape_inference@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 14000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0106 · `dtype_promotion` — Precision Assignment & Mixed-Precision Planner

| field | value |
|---|---|
| part id | `P0106` (6/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0106_dtype_promotion.rs` |
| module path | `hyperion.t03.compiler.dtype_promotion` |
| capability published | `cap.t03.dtype.dtype_promotion@1` |
| determinism class | `pure` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0106_dtype_promotion.txt`](prompts/P0106_dtype_promotion.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0106-dtype-promotion) |

**Mission.** Chooses the cheapest precision per op that still meets the accuracy contract.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **sensitivity analysis via perturbation and gradient proxies** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **ILP/greedy solver over the precision-assignment space** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **accuracy constraint verification against a reference run** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured speedup at certified accuracy parity**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.dtype.dtype_promotion@1`
- `cap.t03.dtype.dtype_promotion.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.shape.shape_inference@1` | use the in-file conservative substitute for `shape_inference` (documented, slower, lower quality) and set `degraded['shape_inference']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t02.attn.attn_flash_bwd@1` | use the in-file conservative substitute for `attn_flash_bwd` (documented, slower, lower quality) and set `degraded['attn_flash_bwd']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sensitivity analysis via perturbation and gradient proxies | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - ILP/greedy solver over the precision-assignment space | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accuracy constraint verification against a reference run | 520 | Third required mechanism. |
| 6 | Core implementation D - measured speedup at certified accuracy parity | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0106_dtype_promotion.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.dtype.dtype_promotion@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 15000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0107 · `algebraic_rewrite` — Algebraic Simplification & Rewrite Engine

| field | value |
|---|---|
| part id | `P0107` (7/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0107_algebraic_rewrite.rs` |
| module path | `hyperion.t03.compiler.algebraic_rewrite` |
| capability published | `cap.t03.algebraic.algebraic_rewrite@1` |
| determinism class | `pure` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0107_algebraic_rewrite.txt`](prompts/P0107_algebraic_rewrite.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0107-algebraic-rewrite) |

**Mission.** The rule-based optimiser: hundreds of semantics-preserving rewrites.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **e-graph saturation with cost-based extraction** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **rule library covering linear algebra, softmax, norms and gating identities** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **confluence/termination handling with iteration limits**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **semantics-preservation tests per rule** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.algebraic.algebraic_rewrite@1`
- `cap.t03.algebraic.algebraic_rewrite.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.dtype.dtype_promotion@1` | use the in-file conservative substitute for `dtype_promotion` (documented, slower, lower quality) and set `degraded['dtype_promotion']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t02.reduction.reduction_kernels@1` | use the in-file conservative substitute for `reduction_kernels` (documented, slower, lower quality) and set `degraded['reduction_kernels']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - e-graph saturation with cost-based extraction | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - rule library covering linear algebra, softmax, norms and gating  | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - confluence/termination handling with iteration limits | 520 | Third required mechanism. |
| 6 | Core implementation D - semantics-preservation tests per rule | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0107_algebraic_rewrite.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.algebraic.algebraic_rewrite@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 16000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0108 · `fusion_pass` — Operator Fusion Pass

| field | value |
|---|---|
| part id | `P0108` (8/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0108_fusion_pass.rs` |
| module path | `hyperion.t03.compiler.fusion_pass` |
| capability published | `cap.t03.fusion.fusion_pass@1` |
| determinism class | `pure` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0108_fusion_pass.txt`](prompts/P0108_fusion_pass.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0108-fusion-pass) |

**Mission.** Merges ops into single-pass kernels using the T02 legality rules.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **fusion group formation with cut-based partitioning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **profitability model from arithmetic intensity and memory traffic**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **recomputation-vs-materialisation decisions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured memory-traffic reduction on the benchmark corpus** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.fusion.fusion_pass@1`
- `cap.t03.fusion.fusion_pass.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.algebraic.algebraic_rewrite@1` | use the in-file conservative substitute for `algebraic_rewrite` (documented, slower, lower quality) and set `degraded['algebraic_rewrite']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t02.rng.rng_kernels@1` | use the in-file conservative substitute for `rng_kernels` (documented, slower, lower quality) and set `degraded['rng_kernels']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fusion group formation with cut-based partitioning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - profitability model from arithmetic intensity and memory traffic | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - recomputation-vs-materialisation decisions | 520 | Third required mechanism. |
| 6 | Core implementation D - measured memory-traffic reduction on the benchmark corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0108_fusion_pass.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.fusion.fusion_pass@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 17000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0109 · `layout_assignment` — Layout Assignment & Relayout Minimisation

| field | value |
|---|---|
| part id | `P0109` (9/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0109_layout_assignment.rs` |
| module path | `hyperion.t03.compiler.layout_assignment` |
| capability published | `cap.t03.layout.layout_assignment@1` |
| determinism class | `pure` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0109_layout_assignment.txt`](prompts/P0109_layout_assignment.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0109-layout-assignment) |

**Mission.** Picks tensor layouts globally to eliminate transposes.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **layout constraint propagation across the whole graph**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **min-cut formulation for relayout placement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **blocked/padded layout selection for tensor cores** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **count of eliminated relayouts as the gate metric** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.layout.layout_assignment@1`
- `cap.t03.layout.layout_assignment.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.fusion.fusion_pass@1` | use the in-file conservative substitute for `fusion_pass` (documented, slower, lower quality) and set `degraded['fusion_pass']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t02.simd.simd_cpu@1` | use the in-file conservative substitute for `simd_cpu` (documented, slower, lower quality) and set `degraded['simd_cpu']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - layout constraint propagation across the whole graph | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - min-cut formulation for relayout placement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blocked/padded layout selection for tensor cores | 520 | Third required mechanism. |
| 6 | Core implementation D - count of eliminated relayouts as the gate metric | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0109_layout_assignment.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.layout.layout_assignment@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 18000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0110 · `memory_planner` — Static Memory Planner & Liveness Allocator

| field | value |
|---|---|
| part id | `P0110` (10/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0110_memory_planner.rs` |
| module path | `hyperion.t03.compiler.memory_planner` |
| capability published | `cap.t03.memory.memory_planner@1` |
| determinism class | `pure` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0110_memory_planner.txt`](prompts/P0110_memory_planner.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0110-memory-planner) |

**Mission.** Assigns every buffer an offset with minimal peak memory.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **liveness analysis with interval graph construction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **best-fit-by-size allocation with proven bounds** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **in-place and aliasing opportunity detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **peak-memory reduction versus naive allocation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.memory.memory_planner@1`
- `cap.t03.memory.memory_planner.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.layout.layout_assignment@1` | use the in-file conservative substitute for `layout_assignment` (documented, slower, lower quality) and set `degraded['layout_assignment']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t02.emulation.emulation_reference@1` | use the in-file conservative substitute for `emulation_reference` (documented, slower, lower quality) and set `degraded['emulation_reference']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - liveness analysis with interval graph construction | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - best-fit-by-size allocation with proven bounds | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - in-place and aliasing opportunity detection | 520 | Third required mechanism. |
| 6 | Core implementation D - peak-memory reduction versus naive allocation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0110_memory_planner.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.memory.memory_planner@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 19000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0111 · `rematerialisation` — Activation Rematerialisation Planner

| field | value |
|---|---|
| part id | `P0111` (11/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0111_rematerialisation.rs` |
| module path | `hyperion.t03.compiler.rematerialisation` |
| capability published | `cap.t03.rematerialisat.rematerialisation@1` |
| determinism class | `pure` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0111_rematerialisation.txt`](prompts/P0111_rematerialisation.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0111-rematerialisation) |

**Mission.** Trades compute for memory optimally during training and long-context inference.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **cost-model-driven checkpoint selection (dynamic programming)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **segment-based recompute schedules with nested checkpoints** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **memory-budget-constrained optimisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured memory/compute Pareto frontier** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.rematerialisat.rematerialisation@1`
- `cap.t03.rematerialisat.rematerialisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.memory.memory_planner@1` | use the in-file conservative substitute for `memory_planner` (documented, slower, lower quality) and set `degraded['memory_planner']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t02.kernel.kernel_codegen_rt@1` | use the in-file conservative substitute for `kernel_codegen_rt` (documented, slower, lower quality) and set `degraded['kernel_codegen_rt']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cost-model-driven checkpoint selection (dynamic programming) | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - segment-based recompute schedules with nested checkpoints | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - memory-budget-constrained optimisation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured memory/compute Pareto frontier | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0111_rematerialisation.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.rematerialisat.rematerialisation@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 20000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0112 · `scheduler_pass` — Instruction Scheduling & Overlap Pass

| field | value |
|---|---|
| part id | `P0112` (12/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0112_scheduler_pass.rs` |
| module path | `hyperion.t03.compiler.scheduler_pass` |
| capability published | `cap.t03.scheduler.scheduler_pass@1` |
| determinism class | `pure` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0112_scheduler_pass.txt`](prompts/P0112_scheduler_pass.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0112-scheduler-pass) |

**Mission.** Orders operations to hide latency and maximise concurrency.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **list scheduling with a machine model of latencies and ports** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **communication/compute overlap insertion**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **critical-path shortening with resource constraints** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **achieved-overlap metric versus theoretical ideal** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.scheduler.scheduler_pass@1`
- `cap.t03.scheduler.scheduler_pass.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.rematerialisat.rematerialisation@1` | use the in-file conservative substitute for `rematerialisation` (documented, slower, lower quality) and set `degraded['rematerialisation']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t02.micro.micro_opt_catalog@1` | use the in-file conservative substitute for `micro_opt_catalog` (documented, slower, lower quality) and set `degraded['micro_opt_catalog']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - list scheduling with a machine model of latencies and ports | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - communication/compute overlap insertion | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - critical-path shortening with resource constraints | 520 | Third required mechanism. |
| 6 | Core implementation D - achieved-overlap metric versus theoretical ideal | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0112_scheduler_pass.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.scheduler.scheduler_pass@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 21000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0113 · `parallel_partition` — Automatic Parallelism Partitioner

| field | value |
|---|---|
| part id | `P0113` (13/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0113_parallel_partition.rs` |
| module path | `hyperion.t03.compiler.parallel_partition` |
| capability published | `cap.t03.parallel.parallel_partition@1` |
| determinism class | `pure` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0113_parallel_partition.txt`](prompts/P0113_parallel_partition.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0113-parallel-partition) |

**Mission.** Derives tensor/pipeline/expert/sequence parallel plans automatically.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **sharding-propagation solver over annotated inputs and outputs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cost model including collective volume and bubble time** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **hybrid-plan search across 4 parallelism axes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **plan quality versus hand-tuned expert baselines** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.parallel.parallel_partition@1`
- `cap.t03.parallel.parallel_partition.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.scheduler.scheduler_pass@1` | use the in-file conservative substitute for `scheduler_pass` (documented, slower, lower quality) and set `degraded['scheduler_pass']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t02.attn.attn_flash_fwd@1` | use the in-file conservative substitute for `attn_flash_fwd` (documented, slower, lower quality) and set `degraded['attn_flash_fwd']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sharding-propagation solver over annotated inputs and outputs | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost model including collective volume and bubble time | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hybrid-plan search across 4 parallelism axes | 520 | Third required mechanism. |
| 6 | Core implementation D - plan quality versus hand-tuned expert baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0113_parallel_partition.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.parallel.parallel_partition@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 22000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0114 · `pipeline_planner` — Pipeline Parallel Schedule Synthesiser

| field | value |
|---|---|
| part id | `P0114` (14/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0114_pipeline_planner.rs` |
| module path | `hyperion.t03.compiler.pipeline_planner` |
| capability published | `cap.t03.pipeline.pipeline_planner@1` |
| determinism class | `pure` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0114_pipeline_planner.txt`](prompts/P0114_pipeline_planner.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0114-pipeline-planner) |

**Mission.** Generates bubble-minimal pipeline schedules.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **1F1B, interleaved and zero-bubble schedule generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **stage-balancing partitioner using measured per-layer costs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **activation-memory accounting per schedule** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **bubble-fraction measurement and target enforcement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.pipeline.pipeline_planner@1`
- `cap.t03.pipeline.pipeline_planner.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.parallel.parallel_partition@1` | use the in-file conservative substitute for `parallel_partition` (documented, slower, lower quality) and set `degraded['parallel_partition']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t02.elementwise.elementwise_fusion@1` | use the in-file conservative substitute for `elementwise_fusion` (documented, slower, lower quality) and set `degraded['elementwise_fusion']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - 1F1B, interleaved and zero-bubble schedule generation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - stage-balancing partitioner using measured per-layer costs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - activation-memory accounting per schedule | 520 | Third required mechanism. |
| 6 | Core implementation D - bubble-fraction measurement and target enforcement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0114_pipeline_planner.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.pipeline.pipeline_planner@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 23000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0115 · `collective_insertion` — Collective Communication Insertion & Fusion

| field | value |
|---|---|
| part id | `P0115` (15/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0115_collective_insertion.rs` |
| module path | `hyperion.t03.compiler.collective_insertion` |
| capability published | `cap.t03.collective.collective_insertion@1` |
| determinism class | `pure` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0115_collective_insertion.txt`](prompts/P0115_collective_insertion.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0115-collective-insertion) |

**Mission.** Places, fuses and overlaps every collective operation.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **all-reduce/all-gather/reduce-scatter insertion from sharding specs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **collective fusion with bucketing to amortise latency** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **overlap with compute via async handles and dependency edges**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **communication-volume reduction measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.collective.collective_insertion@1`
- `cap.t03.collective.collective_insertion.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.pipeline.pipeline_planner@1` | use the in-file conservative substitute for `pipeline_planner` (documented, slower, lower quality) and set `degraded['pipeline_planner']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t02.transpose.transpose_layout@1` | use the in-file conservative substitute for `transpose_layout` (documented, slower, lower quality) and set `degraded['transpose_layout']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - all-reduce/all-gather/reduce-scatter insertion from sharding spe | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - collective fusion with bucketing to amortise latency | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - overlap with compute via async handles and dependency edges | 520 | Third required mechanism. |
| 6 | Core implementation D - communication-volume reduction measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0115_collective_insertion.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.collective.collective_insertion@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 24000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0116 · `autotuner_core` — Autotuning Search Engine

| field | value |
|---|---|
| part id | `P0116` (16/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0116_autotuner_core.rs` |
| module path | `hyperion.t03.compiler.autotuner_core` |
| capability published | `cap.t03.autotuner.autotuner_core@1` |
| determinism class | `pure` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0116_autotuner_core.txt`](prompts/P0116_autotuner_core.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0116-autotuner-core) |

**Mission.** Finds the best kernel configuration per shape with a small measurement budget.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **search over tile/stage/precision spaces with pruning by legality and cost model** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **bayesian/bandit search with transfer from similar shapes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **measurement harness with noise handling and early stopping** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **tuning-budget-vs-quality curves** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.autotuner.autotuner_core@1`
- `cap.t03.autotuner.autotuner_core.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.collective.collective_insertion@1` | use the in-file conservative substitute for `collective_insertion` (documented, slower, lower quality) and set `degraded['collective_insertion']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t02.cache.cache_blocking@1` | use the in-file conservative substitute for `cache_blocking` (documented, slower, lower quality) and set `degraded['cache_blocking']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - search over tile/stage/precision spaces with pruning by legality | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - bayesian/bandit search with transfer from similar shapes | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - measurement harness with noise handling and early stopping | 520 | Third required mechanism. |
| 6 | Core implementation D - tuning-budget-vs-quality curves | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0116_autotuner_core.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.autotuner.autotuner_core@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 25000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0117 · `cost_model_learned` — Learned Cost Model

| field | value |
|---|---|
| part id | `P0117` (17/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0117_cost_model_learned.rs` |
| module path | `hyperion.t03.compiler.cost_model_learned` |
| capability published | `cap.t03.cost.cost_model_learned@1` |
| determinism class | `pure` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0117_cost_model_learned.txt`](prompts/P0117_cost_model_learned.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0117-cost-model-learned) |

**Mission.** Predicts kernel runtime accurately enough to skip most measurements.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **feature extraction from IR and target description**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **regression model with uncertainty estimates for search guidance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **online updating from production measurements** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **prediction-error target under 8% on held-out shapes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.cost.cost_model_learned@1`
- `cap.t03.cost.cost_model_learned.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.autotuner.autotuner_core@1` | use the in-file conservative substitute for `autotuner_core` (documented, slower, lower quality) and set `degraded['autotuner_core']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t02.profiler.profiler_hooks@1` | use the in-file conservative substitute for `profiler_hooks` (documented, slower, lower quality) and set `degraded['profiler_hooks']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - feature extraction from IR and target description | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - regression model with uncertainty estimates for search guidance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - online updating from production measurements | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction-error target under 8% on held-out shapes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0117_cost_model_learned.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.cost.cost_model_learned@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 26000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0118 · `codegen_gpu` — Accelerator Code Generator

| field | value |
|---|---|
| part id | `P0118` (18/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0118_codegen_gpu.rs` |
| module path | `hyperion.t03.compiler.codegen_gpu` |
| capability published | `cap.t03.codegen.codegen_gpu@1` |
| determinism class | `pure` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0118_codegen_gpu.txt`](prompts/P0118_codegen_gpu.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0118-codegen-gpu) |

**Mission.** Emits high-performance device code from scheduled Ω-IR.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **tile-level IR lowering with explicit memory-hierarchy staging** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **async-copy/barrier/pipeline emission and register allocation hints** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **vendor-neutral backend interface with two concrete targets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **generated-vs-handwritten performance comparison**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.codegen.codegen_gpu@1`
- `cap.t03.codegen.codegen_gpu.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.cost.cost_model_learned@1` | use the in-file conservative substitute for `cost_model_learned` (documented, slower, lower quality) and set `degraded['cost_model_learned']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t02.error.error_correction@1` | use the in-file conservative substitute for `error_correction` (documented, slower, lower quality) and set `degraded['error_correction']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tile-level IR lowering with explicit memory-hierarchy staging | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - async-copy/barrier/pipeline emission and register allocation hin | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - vendor-neutral backend interface with two concrete targets | 520 | Third required mechanism. |
| 6 | Core implementation D - generated-vs-handwritten performance comparison | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0118_codegen_gpu.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.codegen.codegen_gpu@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 27000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0119 · `codegen_cpu` — CPU Code Generator

| field | value |
|---|---|
| part id | `P0119` (19/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0119_codegen_cpu.rs` |
| module path | `hyperion.t03.compiler.codegen_cpu` |
| capability published | `cap.t03.codegen.codegen_cpu@1` |
| determinism class | `pure` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0119_codegen_cpu.txt`](prompts/P0119_codegen_cpu.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0119-codegen-cpu) |

**Mission.** Vectorised CPU codegen for small-batch, edge and reference execution.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **loop vectorisation with ISA-specific intrinsic selection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cache blocking and prefetch insertion from the machine model** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **multi-threading with deterministic work partitioning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **efficiency versus tuned BLAS baselines** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.codegen.codegen_cpu@1`
- `cap.t03.codegen.codegen_cpu.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.codegen.codegen_gpu@1` | use the in-file conservative substitute for `codegen_gpu` (documented, slower, lower quality) and set `degraded['codegen_gpu']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t02.kernel.kernel_bench_suite@1` | use the in-file conservative substitute for `kernel_bench_suite` (documented, slower, lower quality) and set `degraded['kernel_bench_suite']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - loop vectorisation with ISA-specific intrinsic selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cache blocking and prefetch insertion from the machine model | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - multi-threading with deterministic work partitioning | 520 | Third required mechanism. |
| 6 | Core implementation D - efficiency versus tuned BLAS baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0119_codegen_cpu.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.codegen.codegen_cpu@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 28000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0120 · `jit_cache_compiler` — Compilation Cache & Warm Start

| field | value |
|---|---|
| part id | `P0120` (20/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0120_jit_cache_compiler.rs` |
| module path | `hyperion.t03.compiler.jit_cache_compiler` |
| capability published | `cap.t03.jit.jit_cache_compiler@1` |
| determinism class | `pure` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0120_jit_cache_compiler.txt`](prompts/P0120_jit_cache_compiler.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0120-jit-cache-compiler) |

**Mission.** Never compiles the same thing twice, across processes and machines.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **content-addressed cache keyed by IR hash + target + flags** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **shared cache protocol safe for concurrent writers**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **profile-guided precompilation of the hot shape set** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **cold-start compile-time reduction measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.jit.jit_cache_compiler@1`
- `cap.t03.jit.jit_cache_compiler.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.codegen.codegen_cpu@1` | use the in-file conservative substitute for `codegen_cpu` (documented, slower, lower quality) and set `degraded['codegen_cpu']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t02.gemm.gemm_sparse@1` | use the in-file conservative substitute for `gemm_sparse` (documented, slower, lower quality) and set `degraded['gemm_sparse']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - content-addressed cache keyed by IR hash + target + flags | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - shared cache protocol safe for concurrent writers | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - profile-guided precompilation of the hot shape set | 520 | Third required mechanism. |
| 6 | Core implementation D - cold-start compile-time reduction measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0120_jit_cache_compiler.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.jit.jit_cache_compiler@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 29000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0121 · `guard_specialise` — Guarded Specialisation & Recompilation Policy

| field | value |
|---|---|
| part id | `P0121` (21/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0121_guard_specialise.rs` |
| module path | `hyperion.t03.compiler.guard_specialise` |
| capability published | `cap.t03.guard.guard_specialise@1` |
| determinism class | `pure` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0121_guard_specialise.txt`](prompts/P0121_guard_specialise.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0121-guard-specialise) |

**Mission.** Specialises aggressively while staying correct under shape/flag changes.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **guard generation, minimisation and cheap runtime evaluation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **specialisation-cache with LRU and recompile-storm prevention** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **deoptimisation path preserving semantics** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **guard-overhead measurement under 1% of step time** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.guard.guard_specialise@1`
- `cap.t03.guard.guard_specialise.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.jit.jit_cache_compiler@1` | use the in-file conservative substitute for `jit_cache_compiler` (documented, slower, lower quality) and set `degraded['jit_cache_compiler']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t02.softmax.softmax_norm@1` | use the in-file conservative substitute for `softmax_norm` (documented, slower, lower quality) and set `degraded['softmax_norm']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - guard generation, minimisation and cheap runtime evaluation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - specialisation-cache with LRU and recompile-storm prevention | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deoptimisation path preserving semantics | 520 | Third required mechanism. |
| 6 | Core implementation D - guard-overhead measurement under 1% of step time | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0121_guard_specialise.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.guard.guard_specialise@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 30000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0122 · `kernel_selection` — Global Kernel Selection Optimiser

| field | value |
|---|---|
| part id | `P0122` (22/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0122_kernel_selection.rs` |
| module path | `hyperion.t03.compiler.kernel_selection` |
| capability published | `cap.t03.kernel.kernel_selection@1` |
| determinism class | `pure` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0122_kernel_selection.txt`](prompts/P0122_kernel_selection.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0122-kernel-selection) |

**Mission.** Chooses kernels jointly rather than greedily, accounting for layout coupling.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **joint selection formulated over the layout/precision/kernel product space** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **beam search with cost-model pruning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **constraint handling for determinism and accuracy modes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **end-to-end gain versus greedy selection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.kernel.kernel_selection@1`
- `cap.t03.kernel.kernel_selection.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.guard.guard_specialise@1` | use the in-file conservative substitute for `guard_specialise` (documented, slower, lower quality) and set `degraded['guard_specialise']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t02.gather.gather_scatter@1` | use the in-file conservative substitute for `gather_scatter` (documented, slower, lower quality) and set `degraded['gather_scatter']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - joint selection formulated over the layout/precision/kernel prod | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - beam search with cost-model pruning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - constraint handling for determinism and accuracy modes | 520 | Third required mechanism. |
| 6 | Core implementation D - end-to-end gain versus greedy selection | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0122_kernel_selection.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.kernel.kernel_selection@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 31000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0123 · `graph_partition_device` — Device Placement & Graph Partitioning

| field | value |
|---|---|
| part id | `P0123` (23/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0123_graph_partition_device.rs` |
| module path | `hyperion.t03.compiler.graph_partition_device` |
| capability published | `cap.t03.graph.graph_partition_device@1` |
| determinism class | `pure` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0123_graph_partition_device.txt`](prompts/P0123_graph_partition_device.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0123-graph-partition-device) |

**Mission.** Assigns subgraphs to heterogeneous devices under memory and bandwidth limits.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-constraint partitioning with communication minimisation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **heterogeneous-device cost modelling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **memory-feasibility checking with rematerialisation coupling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **placement quality versus exhaustive search on small graphs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.graph.graph_partition_device@1`
- `cap.t03.graph.graph_partition_device.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.kernel.kernel_selection@1` | use the in-file conservative substitute for `kernel_selection` (documented, slower, lower quality) and set `degraded['kernel_selection']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t02.async.async_copy@1` | use the in-file conservative substitute for `async_copy` (documented, slower, lower quality) and set `degraded['async_copy']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-constraint partitioning with communication minimisation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - heterogeneous-device cost modelling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - memory-feasibility checking with rematerialisation coupling | 520 | Third required mechanism. |
| 6 | Core implementation D - placement quality versus exhaustive search on small graphs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0123_graph_partition_device.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.graph.graph_partition_device@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 32000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0124 · `dynamic_shapes` — Dynamic Shape Execution Strategy

| field | value |
|---|---|
| part id | `P0124` (24/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0124_dynamic_shapes.rs` |
| module path | `hyperion.t03.compiler.dynamic_shapes` |
| capability published | `cap.t03.dynamic.dynamic_shapes@1` |
| determinism class | `pure` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0124_dynamic_shapes.txt`](prompts/P0124_dynamic_shapes.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0124-dynamic-shapes) |

**Mission.** Handles unbounded shape variety with bounded compilation cost.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **bucketing policy with padding-cost/recompile-cost tradeoff** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **fully dynamic fallback kernels with acceptable efficiency**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **shape-distribution learning from production traces** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **tail-latency impact measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.dynamic.dynamic_shapes@1`
- `cap.t03.dynamic.dynamic_shapes.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.graph.graph_partition_device@1` | use the in-file conservative substitute for `graph_partition_device` (documented, slower, lower quality) and set `degraded['graph_partition_device']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t02.roofline.roofline_model@1` | use the in-file conservative substitute for `roofline_model` (documented, slower, lower quality) and set `degraded['roofline_model']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - bucketing policy with padding-cost/recompile-cost tradeoff | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fully dynamic fallback kernels with acceptable efficiency | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - shape-distribution learning from production traces | 520 | Third required mechanism. |
| 6 | Core implementation D - tail-latency impact measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0124_dynamic_shapes.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.dynamic.dynamic_shapes@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 33000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0125 · `differentiation` — Automatic Differentiation on Ω-IR

| field | value |
|---|---|
| part id | `P0125` (25/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0125_differentiation.rs` |
| module path | `hyperion.t03.compiler.differentiation` |
| capability published | `cap.t03.differentiatio.differentiation@1` |
| determinism class | `pure` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0125_differentiation.txt`](prompts/P0125_differentiation.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0125-differentiation) |

**Mission.** Reverse and forward mode AD with checkpointing integration.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **reverse-mode transformation with correct effect and control-flow handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **forward-mode and JVP/VJP composition for higher-order needs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **custom-gradient registration and verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **gradient correctness versus numerical differentiation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.differentiatio.differentiation@1`
- `cap.t03.differentiatio.differentiation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.dynamic.dynamic_shapes@1` | use the in-file conservative substitute for `dynamic_shapes` (documented, slower, lower quality) and set `degraded['dynamic_shapes']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t02.power.power_thermal@1` | use the in-file conservative substitute for `power_thermal` (documented, slower, lower quality) and set `degraded['power_thermal']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - reverse-mode transformation with correct effect and control-flow | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - forward-mode and JVP/VJP composition for higher-order needs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - custom-gradient registration and verification | 520 | Third required mechanism. |
| 6 | Core implementation D - gradient correctness versus numerical differentiation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0125_differentiation.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.differentiatio.differentiation@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 34000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0126 · `vectorisation_transform` — Batching & Vectorisation Transform

| field | value |
|---|---|
| part id | `P0126` (26/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0126_vectorisation_transform.rs` |
| module path | `hyperion.t03.compiler.vectorisation_transform` |
| capability published | `cap.t03.vectorisation.vectorisation_transform@1` |
| determinism class | `pure` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0126_vectorisation_transform.txt`](prompts/P0126_vectorisation_transform.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0126-vectorisation-transform) |

**Mission.** Automatic vmap-style batching over arbitrary subgraphs.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **rank-polymorphic transformation with batching rules per op** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **nested batching composition** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **fallback loop generation with clear performance warnings** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **equivalence tests against explicit loops**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.vectorisation.vectorisation_transform@1`
- `cap.t03.vectorisation.vectorisation_transform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.differentiatio.differentiation@1` | use the in-file conservative substitute for `differentiation` (documented, slower, lower quality) and set `degraded['differentiation']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t02.ragged.ragged_batch@1` | use the in-file conservative substitute for `ragged_batch` (documented, slower, lower quality) and set `degraded['ragged_batch']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - rank-polymorphic transformation with batching rules per op | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - nested batching composition | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - fallback loop generation with clear performance warnings | 520 | Third required mechanism. |
| 6 | Core implementation D - equivalence tests against explicit loops | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0126_vectorisation_transform.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.vectorisation.vectorisation_transform@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 35000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0127 · `loop_transform` — Polyhedral Loop Transformation

| field | value |
|---|---|
| part id | `P0127` (27/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0127_loop_transform.rs` |
| module path | `hyperion.t03.compiler.loop_transform` |
| capability published | `cap.t03.loop.loop_transform@1` |
| determinism class | `pure` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0127_loop_transform.txt`](prompts/P0127_loop_transform.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0127-loop-transform) |

**Mission.** Tiling, fusion, interchange and skewing with dependence legality.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **dependence analysis and legality checking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **tiling/skewing/interchange transformation composition** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **objective functions for locality and parallelism**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **transformation legality proofs on a benchmark set** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.loop.loop_transform@1`
- `cap.t03.loop.loop_transform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.vectorisation.vectorisation_transform@1` | use the in-file conservative substitute for `vectorisation_transform` (documented, slower, lower quality) and set `degraded['vectorisation_transform']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t02.gemm.gemm_grouped@1` | use the in-file conservative substitute for `gemm_grouped` (documented, slower, lower quality) and set `degraded['gemm_grouped']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dependence analysis and legality checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tiling/skewing/interchange transformation composition | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - objective functions for locality and parallelism | 520 | Third required mechanism. |
| 6 | Core implementation D - transformation legality proofs on a benchmark set | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0127_loop_transform.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.loop.loop_transform@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 36000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0128 · `constant_folding` — Constant Folding & Weight Preprocessing

| field | value |
|---|---|
| part id | `P0128` (28/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0128_constant_folding.rs` |
| module path | `hyperion.t03.compiler.constant_folding` |
| capability published | `cap.t03.constant.constant_folding@1` |
| determinism class | `pure` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0128_constant_folding.txt`](prompts/P0128_constant_folding.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0128-constant-folding) |

**Mission.** Precomputes everything that does not depend on the request.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **exact constant evaluation with the same numerics as runtime** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **weight transformation baking (layout, quantisation, fusion of scales)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **memory-bounded folding policy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **startup-time and per-request savings measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.constant.constant_folding@1`
- `cap.t03.constant.constant_folding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.loop.loop_transform@1` | use the in-file conservative substitute for `loop_transform` (documented, slower, lower quality) and set `degraded['loop_transform']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t02.conv.conv_depthwise@1` | use the in-file conservative substitute for `conv_depthwise` (documented, slower, lower quality) and set `degraded['conv_depthwise']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - exact constant evaluation with the same numerics as runtime | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - weight transformation baking (layout, quantisation, fusion of sc | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - memory-bounded folding policy | 520 | Third required mechanism. |
| 6 | Core implementation D - startup-time and per-request savings measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0128_constant_folding.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.constant.constant_folding@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 37000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0129 · `dead_code_dce` — Dead Code, CSE & Canonicalisation

| field | value |
|---|---|
| part id | `P0129` (29/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0129_dead_code_dce.rs` |
| module path | `hyperion.t03.compiler.dead_code_dce` |
| capability published | `cap.t03.dead.dead_code_dce@1` |
| determinism class | `pure` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0129_dead_code_dce.txt`](prompts/P0129_dead_code_dce.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0129-dead-code-dce) |

**Mission.** The classic cleanups, made effect-aware and determinism-safe.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **effect-aware DCE preserving observable behaviour**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **global value numbering and common-subexpression elimination** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **canonicalisation to a normal form enabling later matches** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **IR-size and op-count reduction metrics** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.dead.dead_code_dce@1`
- `cap.t03.dead.dead_code_dce.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.constant.constant_folding@1` | use the in-file conservative substitute for `constant_folding` (documented, slower, lower quality) and set `degraded['constant_folding']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t02.rope.rope_embed@1` | use the in-file conservative substitute for `rope_embed` (documented, slower, lower quality) and set `degraded['rope_embed']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - effect-aware DCE preserving observable behaviour | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - global value numbering and common-subexpression elimination | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - canonicalisation to a normal form enabling later matches | 520 | Third required mechanism. |
| 6 | Core implementation D - IR-size and op-count reduction metrics | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0129_dead_code_dce.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.dead.dead_code_dce@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 38000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0130 · `effect_system` — Effect & Purity Analysis

| field | value |
|---|---|
| part id | `P0130` (30/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0130_effect_system.rs` |
| module path | `hyperion.t03.compiler.effect_system` |
| capability published | `cap.t03.effect.effect_system@1` |
| determinism class | `pure` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0130_effect_system.txt`](prompts/P0130_effect_system.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0130-effect-system) |

**Mission.** Tracks IO, randomness, mutation and safety effects through the graph.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **effect lattice with precise join semantics** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **purity inference enabling reordering and caching** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **randomness-source tracking tied to split_seed** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **misclassification detection tests**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.effect.effect_system@1`
- `cap.t03.effect.effect_system.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.dead.dead_code_dce@1` | use the in-file conservative substitute for `dead_code_dce` (documented, slower, lower quality) and set `degraded['dead_code_dce']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t02.mem.mem_pool_device@1` | use the in-file conservative substitute for `mem_pool_device` (documented, slower, lower quality) and set `degraded['mem_pool_device']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - effect lattice with precise join semantics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - purity inference enabling reordering and caching | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - randomness-source tracking tied to split_seed | 520 | Third required mechanism. |
| 6 | Core implementation D - misclassification detection tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0130_effect_system.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.effect.effect_system@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 39000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0131 · `ir_verifier` — IR Verification & Invariant Checking

| field | value |
|---|---|
| part id | `P0131` (31/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0131_ir_verifier.rs` |
| module path | `hyperion.t03.compiler.ir_verifier` |
| capability published | `cap.t03.ir.ir_verifier@1` |
| determinism class | `pure` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0131_ir_verifier.txt`](prompts/P0131_ir_verifier.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0131-ir-verifier) |

**Mission.** Catches compiler bugs before they become model bugs.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **structural, type, shape, effect and determinism invariants** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **pass-boundary verification with cheap and thorough modes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **counterexample minimisation for failed invariants**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **verifier coverage over a mutation-generated bad-IR corpus** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.ir.ir_verifier@1`
- `cap.t03.ir.ir_verifier.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.effect.effect_system@1` | use the in-file conservative substitute for `effect_system` (documented, slower, lower quality) and set `degraded['effect_system']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t02.kernel.kernel_verify@1` | use the in-file conservative substitute for `kernel_verify` (documented, slower, lower quality) and set `degraded['kernel_verify']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structural, type, shape, effect and determinism invariants | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - pass-boundary verification with cheap and thorough modes | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - counterexample minimisation for failed invariants | 520 | Third required mechanism. |
| 6 | Core implementation D - verifier coverage over a mutation-generated bad-IR corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0131_ir_verifier.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.ir.ir_verifier@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 40000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0132 · `differential_testing` — Compiler Differential Test Harness

| field | value |
|---|---|
| part id | `P0132` (32/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0132_differential_testing.rs` |
| module path | `hyperion.t03.compiler.differential_testing` |
| capability published | `cap.t03.differential.differential_testing@1` |
| determinism class | `pure` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0132_differential_testing.txt`](prompts/P0132_differential_testing.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0132-differential-testing) |

**Mission.** Proves optimised execution matches reference execution exactly.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **random IR generation with realistic op distributions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **optimisation-level differential comparison with tolerance classes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **bisection over the pass pipeline to localise miscompiles** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **nightly-scale corpus with pinned regressions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.differential.differential_testing@1`
- `cap.t03.differential.differential_testing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.ir.ir_verifier@1` | use the in-file conservative substitute for `ir_verifier` (documented, slower, lower quality) and set `degraded['ir_verifier']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t02.stream.stream_scheduler@1` | use the in-file conservative substitute for `stream_scheduler` (documented, slower, lower quality) and set `degraded['stream_scheduler']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - random IR generation with realistic op distributions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - optimisation-level differential comparison with tolerance classe | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - bisection over the pass pipeline to localise miscompiles | 520 | Third required mechanism. |
| 6 | Core implementation D - nightly-scale corpus with pinned regressions | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0132_differential_testing.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.differential.differential_testing@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 41000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0133 · `compile_time_budget` — Compilation Time Budget Manager

| field | value |
|---|---|
| part id | `P0133` (33/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0133_compile_time_budget.rs` |
| module path | `hyperion.t03.compiler.compile_time_budget` |
| capability published | `cap.t03.compile.compile_time_budget@1` |
| determinism class | `pure` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0133_compile_time_budget.txt`](prompts/P0133_compile_time_budget.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0133-compile-time-budget) |

**Mission.** Keeps compile time predictable, even under aggressive optimisation.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **per-pass time budgeting with graceful degradation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **priority ordering so the hottest subgraphs get the most effort** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **background/incremental compilation with hot swap** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **compile-time distribution measurement and tail control** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.compile.compile_time_budget@1`
- `cap.t03.compile.compile_time_budget.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.differential.differential_testing@1` | use the in-file conservative substitute for `differential_testing` (documented, slower, lower quality) and set `degraded['differential_testing']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t02.tensor.tensor_view@1` | use the in-file conservative substitute for `tensor_view` (documented, slower, lower quality) and set `degraded['tensor_view']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-pass time budgeting with graceful degradation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - priority ordering so the hottest subgraphs get the most effort | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - background/incremental compilation with hot swap | 520 | Third required mechanism. |
| 6 | Core implementation D - compile-time distribution measurement and tail control | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0133_compile_time_budget.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.compile.compile_time_budget@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 42000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0134 · `profile_guided` — Profile-Guided Optimisation Pipeline

| field | value |
|---|---|
| part id | `P0134` (34/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0134_profile_guided.rs` |
| module path | `hyperion.t03.compiler.profile_guided` |
| capability published | `cap.t03.profile.profile_guided@1` |
| determinism class | `pure` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0134_profile_guided.txt`](prompts/P0134_profile_guided.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0134-profile-guided) |

**Mission.** Feeds production behaviour back into compilation decisions.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **execution profile collection and aggregation format** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **hot-path specialisation and branch-probability propagation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **profile-staleness detection and safe reuse** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured gain from PGO versus static heuristics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.profile.profile_guided@1`
- `cap.t03.profile.profile_guided.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.compile.compile_time_budget@1` | use the in-file conservative substitute for `compile_time_budget` (documented, slower, lower quality) and set `degraded['compile_time_budget']='local'` |
| `cap.t02.gemm.gemm_int4@1` | use the in-file conservative substitute for `gemm_int4` (documented, slower, lower quality) and set `degraded['gemm_int4']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - execution profile collection and aggregation format | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hot-path specialisation and branch-probability propagation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - profile-staleness detection and safe reuse | 520 | Third required mechanism. |
| 6 | Core implementation D - measured gain from PGO versus static heuristics | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0134_profile_guided.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.profile.profile_guided@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 43000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0135 · `target_description` — Target Machine Description Language

| field | value |
|---|---|
| part id | `P0135` (35/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0135_target_description.rs` |
| module path | `hyperion.t03.compiler.target_description` |
| capability published | `cap.t03.target.target_description@1` |
| determinism class | `pure` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0135_target_description.txt`](prompts/P0135_target_description.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0135-target-description) |

**Mission.** One declarative description per accelerator drives all target-specific decisions.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **hierarchical description: compute units, memories, bandwidths, latencies, ISA features** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **capability queries used by passes instead of hardcoded checks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **validation of a description against measured microbenchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **new-target onboarding checklist and conformance suite** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.target.target_description@1`
- `cap.t03.target.target_description.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.profile.profile_guided@1` | use the in-file conservative substitute for `profile_guided` (documented, slower, lower quality) and set `degraded['profile_guided']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t02.ssm.ssm_scan@1` | use the in-file conservative substitute for `ssm_scan` (documented, slower, lower quality) and set `degraded['ssm_scan']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hierarchical description: compute units, memories, bandwidths, l | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability queries used by passes instead of hardcoded checks | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - validation of a description against measured microbenchmarks | 520 | Third required mechanism. |
| 6 | Core implementation D - new-target onboarding checklist and conformance suite | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0135_target_description.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.target.target_description@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 44000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0136 · `ir_serialization` — IR Serialisation & Portable Artifact Format

| field | value |
|---|---|
| part id | `P0136` (36/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0136_ir_serialization.rs` |
| module path | `hyperion.t03.compiler.ir_serialization` |
| capability published | `cap.t03.ir.ir_serialization@1` |
| determinism class | `pure` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0136_ir_serialization.txt`](prompts/P0136_ir_serialization.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0136-ir-serialization) |

**Mission.** Compiled artifacts that ship, version and verify.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **compact binary format with schema versioning and forward compat** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **embedded provenance, guards and target requirements**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **signature and integrity verification before load** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **cross-version load tests** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.ir.ir_serialization@1`
- `cap.t03.ir.ir_serialization.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.target.target_description@1` | use the in-file conservative substitute for `target_description` (documented, slower, lower quality) and set `degraded['target_description']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t02.kv.kv_cache_kernels@1` | use the in-file conservative substitute for `kv_cache_kernels` (documented, slower, lower quality) and set `degraded['kv_cache_kernels']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - compact binary format with schema versioning and forward compat | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - embedded provenance, guards and target requirements | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - signature and integrity verification before load | 520 | Third required mechanism. |
| 6 | Core implementation D - cross-version load tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0136_ir_serialization.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.ir.ir_serialization@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 45000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0137 · `bytecode_vm` — Ω Execution Bytecode & Interpreter

| field | value |
|---|---|
| part id | `P0137` (37/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0137_bytecode_vm.rs` |
| module path | `hyperion.t03.compiler.bytecode_vm` |
| capability published | `cap.t03.bytecode.bytecode_vm@1` |
| determinism class | `pure` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0137_bytecode_vm.txt`](prompts/P0137_bytecode_vm.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0137-bytecode-vm) |

**Mission.** The portable, debuggable execution path used as the correctness oracle.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **compact bytecode with explicit buffer and effect operands**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **interpreter with single-step, breakpoint and watch support** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **identical numerics to compiled paths in reference mode** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **interpretive overhead documented and bounded** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.bytecode.bytecode_vm@1`
- `cap.t03.bytecode.bytecode_vm.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.ir.ir_serialization@1` | use the in-file conservative substitute for `ir_serialization` (documented, slower, lower quality) and set `degraded['ir_serialization']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t02.graph.graph_capture@1` | use the in-file conservative substitute for `graph_capture` (documented, slower, lower quality) and set `degraded['graph_capture']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - compact bytecode with explicit buffer and effect operands | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - interpreter with single-step, breakpoint and watch support | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - identical numerics to compiled paths in reference mode | 520 | Third required mechanism. |
| 6 | Core implementation D - interpretive overhead documented and bounded | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0137_bytecode_vm.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.bytecode.bytecode_vm@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 46000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0138 · `debug_symbols` — Debug Info, Source Mapping & Blame

| field | value |
|---|---|
| part id | `P0138` (38/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0138_debug_symbols.rs` |
| module path | `hyperion.t03.compiler.debug_symbols` |
| capability published | `cap.t03.debug.debug_symbols@1` |
| determinism class | `pure` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0138_debug_symbols.txt`](prompts/P0138_debug_symbols.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0138-debug-symbols) |

**Mission.** Maps any runtime anomaly back to a source line in one of 1000 files.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **source-location propagation surviving every transformation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **inlining and fusion attribution with multi-origin support** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **blame report generation for numerical anomalies** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **attribution accuracy tests through deep pass pipelines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.debug.debug_symbols@1`
- `cap.t03.debug.debug_symbols.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.bytecode.bytecode_vm@1` | use the in-file conservative substitute for `bytecode_vm` (documented, slower, lower quality) and set `degraded['bytecode_vm']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t02.kernel.kernel_registry@1` | use the in-file conservative substitute for `kernel_registry` (documented, slower, lower quality) and set `degraded['kernel_registry']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - source-location propagation surviving every transformation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - inlining and fusion attribution with multi-origin support | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blame report generation for numerical anomalies | 520 | Third required mechanism. |
| 6 | Core implementation D - attribution accuracy tests through deep pass pipelines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0138_debug_symbols.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.debug.debug_symbols@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 47000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0139 · `pass_search` — Automated Pass Pipeline Search

| field | value |
|---|---|
| part id | `P0139` (39/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0139_pass_search.rs` |
| module path | `hyperion.t03.compiler.pass_search` |
| capability published | `cap.t03.pass.pass_search@1` |
| determinism class | `pure` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0139_pass_search.txt`](prompts/P0139_pass_search.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0139-pass-search) |

**Mission.** Discovers better optimisation pipelines than hand-written ones.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **pipeline space definition with legality and idempotence constraints** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **evolutionary/bandit search with early stopping** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **generalisation validation across model families**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured improvement over the default pipeline** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.pass.pass_search@1`
- `cap.t03.pass.pass_search.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.debug.debug_symbols@1` | use the in-file conservative substitute for `debug_symbols` (documented, slower, lower quality) and set `degraded['debug_symbols']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t02.p2p.p2p_transfer@1` | use the in-file conservative substitute for `p2p_transfer` (documented, slower, lower quality) and set `degraded['p2p_transfer']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pipeline space definition with legality and idempotence constrai | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - evolutionary/bandit search with early stopping | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - generalisation validation across model families | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement over the default pipeline | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0139_pass_search.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.pass.pass_search@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 48000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0140 · `superoptimiser` — Bounded Superoptimiser for Hot Kernels

| field | value |
|---|---|
| part id | `P0140` (40/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0140_superoptimiser.rs` |
| module path | `hyperion.t03.compiler.superoptimiser` |
| capability published | `cap.t03.superoptimiser.superoptimiser@1` |
| determinism class | `pure` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0140_superoptimiser.txt`](prompts/P0140_superoptimiser.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0140-superoptimiser) |

**Mission.** Exhaustively searches for optimal instruction sequences on small critical regions.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **region selection by profile contribution and size bound** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **enumerative/SMT-based equivalent-sequence search**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **verified equivalence before adoption** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **catalogue of discovered sequences with measured wins** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.superoptimiser.superoptimiser@1`
- `cap.t03.superoptimiser.superoptimiser.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.pass.pass_search@1` | use the in-file conservative substitute for `pass_search` (documented, slower, lower quality) and set `degraded['pass_search']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t02.mask.mask_engine@1` | use the in-file conservative substitute for `mask_engine` (documented, slower, lower quality) and set `degraded['mask_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - region selection by profile contribution and size bound | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - enumerative/SMT-based equivalent-sequence search | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - verified equivalence before adoption | 520 | Third required mechanism. |
| 6 | Core implementation D - catalogue of discovered sequences with measured wins | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0140_superoptimiser.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.superoptimiser.superoptimiser@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 49000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0141 · `equality_saturation` — E-Graph Engine & Extraction

| field | value |
|---|---|
| part id | `P0141` (41/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0141_equality_saturation.rs` |
| module path | `hyperion.t03.compiler.equality_saturation` |
| capability published | `cap.t03.equality.equality_saturation@1` |
| determinism class | `pure` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0141_equality_saturation.txt`](prompts/P0141_equality_saturation.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0141-equality-saturation) |

**Mission.** The rewriting substrate: saturate, then extract the cheapest equivalent program.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **congruence-closure e-graph with efficient rebuild**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cost function plugins including learned costs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **extraction with cycle avoidance and global optimality bounds** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **saturation-limit policies and quality-vs-time curves** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.equality.equality_saturation@1`
- `cap.t03.equality.equality_saturation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.superoptimiser.superoptimiser@1` | use the in-file conservative substitute for `superoptimiser` (documented, slower, lower quality) and set `degraded['superoptimiser']='local'` |
| `cap.t02.gemm.gemm_fp8@1` | use the in-file conservative substitute for `gemm_fp8` (documented, slower, lower quality) and set `degraded['gemm_fp8']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - congruence-closure e-graph with efficient rebuild | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost function plugins including learned costs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - extraction with cycle avoidance and global optimality bounds | 520 | Third required mechanism. |
| 6 | Core implementation D - saturation-limit policies and quality-vs-time curves | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0141_equality_saturation.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.equality.equality_saturation@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 3000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0142 · `kernel_template_lib` — Kernel Template Library

| field | value |
|---|---|
| part id | `P0142` (42/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0142_kernel_template_lib.rs` |
| module path | `hyperion.t03.compiler.kernel_template_lib` |
| capability published | `cap.t03.kernel.kernel_template_lib@1` |
| determinism class | `pure` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0142_kernel_template_lib.txt`](prompts/P0142_kernel_template_lib.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0142-kernel-template-lib) |

**Mission.** Parameterised templates the codegen instantiates for any shape.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **template families for GEMM, attention, scan, reduction, elementwise** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **parameter validity constraints and default heuristics** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **instantiation cost and code-size control** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **coverage report over the benchmark shape corpus**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.kernel.kernel_template_lib@1`
- `cap.t03.kernel.kernel_template_lib.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.equality.equality_saturation@1` | use the in-file conservative substitute for `equality_saturation` (documented, slower, lower quality) and set `degraded['equality_saturation']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t02.attn.attn_linear@1` | use the in-file conservative substitute for `attn_linear` (documented, slower, lower quality) and set `degraded['attn_linear']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - template families for GEMM, attention, scan, reduction, elementw | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - parameter validity constraints and default heuristics | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - instantiation cost and code-size control | 520 | Third required mechanism. |
| 6 | Core implementation D - coverage report over the benchmark shape corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0142_kernel_template_lib.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.kernel.kernel_template_lib@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 4000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0143 · `linker_omega` — Ω-Linker for 1000 Compiled Parts

| field | value |
|---|---|
| part id | `P0143` (43/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0143_linker_omega.rs` |
| module path | `hyperion.t03.compiler.linker_omega` |
| capability published | `cap.t03.linker.linker_omega@1` |
| determinism class | `pure` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0143_linker_omega.txt`](prompts/P0143_linker_omega.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0143-linker-omega) |

**Mission.** Links independently compiled part artifacts into one executable assembly.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **capability symbol resolution across artifact boundaries** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cross-part inlining and whole-assembly optimisation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **version/ABI compatibility enforcement at link time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **link-time report: unresolved, duplicate, degraded capabilities** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.linker.linker_omega@1`
- `cap.t03.linker.linker_omega.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.kernel.kernel_template_lib@1` | use the in-file conservative substitute for `kernel_template_lib` (documented, slower, lower quality) and set `degraded['kernel_template_lib']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t02.quantize.quantize_kernels@1` | use the in-file conservative substitute for `quantize_kernels` (documented, slower, lower quality) and set `degraded['quantize_kernels']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability symbol resolution across artifact boundaries | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-part inlining and whole-assembly optimisation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - version/ABI compatibility enforcement at link time | 520 | Third required mechanism. |
| 6 | Core implementation D - link-time report: unresolved, duplicate, degraded capabilities | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0143_linker_omega.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.linker.linker_omega@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 5000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0144 · `incremental_build` — Incremental Compilation & Change Impact

| field | value |
|---|---|
| part id | `P0144` (44/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0144_incremental_build.rs` |
| module path | `hyperion.t03.compiler.incremental_build` |
| capability published | `cap.t03.incremental.incremental_build@1` |
| determinism class | `pure` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0144_incremental_build.txt`](prompts/P0144_incremental_build.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0144-incremental-build) |

**Mission.** Recompiles only what 1 changed part affects, across the 1000-part assembly.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **fine-grained dependency graph with content hashing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **change-impact analysis and minimal rebuild set computation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **cache reuse across branches and machines** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **rebuild-time measurement for single-part edits** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.incremental.incremental_build@1`
- `cap.t03.incremental.incremental_build.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.linker.linker_omega@1` | use the in-file conservative substitute for `linker_omega` (documented, slower, lower quality) and set `degraded['linker_omega']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t02.fused.fused_decode_step@1` | use the in-file conservative substitute for `fused_decode_step` (documented, slower, lower quality) and set `degraded['fused_decode_step']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fine-grained dependency graph with content hashing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - change-impact analysis and minimal rebuild set computation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cache reuse across branches and machines | 520 | Third required mechanism. |
| 6 | Core implementation D - rebuild-time measurement for single-part edits | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0144_incremental_build.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.incremental.incremental_build@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 6000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0145 · `crosscompile` — Cross-Compilation & Target Matrix

| field | value |
|---|---|
| part id | `P0145` (45/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0145_crosscompile.rs` |
| module path | `hyperion.t03.compiler.crosscompile` |
| capability published | `cap.t03.crosscompile.crosscompile@1` |
| determinism class | `pure` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0145_crosscompile.txt`](prompts/P0145_crosscompile.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0145-crosscompile) |

**Mission.** Build once, run on every supported accelerator and CPU.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **hermetic toolchain description and pinned versions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **multi-target artifact bundling with runtime selection** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **reproducible-build verification (identical bytes)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target-matrix CI definition** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.crosscompile.crosscompile@1`
- `cap.t03.crosscompile.crosscompile.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.incremental.incremental_build@1` | use the in-file conservative substitute for `incremental_build` (documented, slower, lower quality) and set `degraded['incremental_build']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t02.bf16.bf16_stability@1` | use the in-file conservative substitute for `bf16_stability` (documented, slower, lower quality) and set `degraded['bf16_stability']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hermetic toolchain description and pinned versions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-target artifact bundling with runtime selection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reproducible-build verification (identical bytes) | 520 | Third required mechanism. |
| 6 | Core implementation D - target-matrix CI definition | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0145_crosscompile.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.crosscompile.crosscompile@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 7000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0146 · `numeric_mode_lowering` — Determinism-Mode Lowering

| field | value |
|---|---|
| part id | `P0146` (46/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0146_numeric_mode_lowering.rs` |
| module path | `hyperion.t03.compiler.numeric_mode_lowering` |
| capability published | `cap.t03.numeric.numeric_mode_lowering@1` |
| determinism class | `pure` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0146_numeric_mode_lowering.txt`](prompts/P0146_numeric_mode_lowering.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0146-numeric-mode-lowering) |

**Mission.** Compiles the same graph into deterministic or fast variants with declared differences.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **mode-aware lowering rules for reductions, atomics and scheduling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cost-of-determinism measurement per model region** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **mode conformance verification (bit-exactness in deterministic mode)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **policy for mixed-mode graphs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.numeric.numeric_mode_lowering@1`
- `cap.t03.numeric.numeric_mode_lowering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.crosscompile.crosscompile@1` | use the in-file conservative substitute for `crosscompile` (documented, slower, lower quality) and set `degraded['crosscompile']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t02.collective.collective_local@1` | use the in-file conservative substitute for `collective_local` (documented, slower, lower quality) and set `degraded['collective_local']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - mode-aware lowering rules for reductions, atomics and scheduling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost-of-determinism measurement per model region | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - mode conformance verification (bit-exactness in deterministic mo | 520 | Third required mechanism. |
| 6 | Core implementation D - policy for mixed-mode graphs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0146_numeric_mode_lowering.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.numeric.numeric_mode_lowering@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 8000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0147 · `op_registry` — Operator Registry & Semantics Database

| field | value |
|---|---|
| part id | `P0147` (47/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0147_op_registry.rs` |
| module path | `hyperion.t03.compiler.op_registry` |
| capability published | `cap.t03.op.op_registry@1` |
| determinism class | `pure` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0147_op_registry.txt`](prompts/P0147_op_registry.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0147-op-registry) |

**Mission.** The canonical definition of every operator in Ω-IR.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **op schema: signature, semantics, effects, error bounds, determinism** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **reference implementation link and lowering candidates** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **registry consistency checks and completeness audit**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **documentation generation for all operators** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.op.op_registry@1`
- `cap.t03.op.op_registry.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.numeric.numeric_mode_lowering@1` | use the in-file conservative substitute for `numeric_mode_lowering` (documented, slower, lower quality) and set `degraded['numeric_mode_lowering']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t02.embedding.embedding_kernels@1` | use the in-file conservative substitute for `embedding_kernels` (documented, slower, lower quality) and set `degraded['embedding_kernels']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - op schema: signature, semantics, effects, error bounds, determin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reference implementation link and lowering candidates | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - registry consistency checks and completeness audit | 520 | Third required mechanism. |
| 6 | Core implementation D - documentation generation for all operators | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0147_op_registry.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.op.op_registry@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 9000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0148 · `graph_diff_tool` — Graph Diff & Optimisation Explainer

| field | value |
|---|---|
| part id | `P0148` (48/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0148_graph_diff_tool.rs` |
| module path | `hyperion.t03.compiler.graph_diff_tool` |
| capability published | `cap.t03.graph.graph_diff_tool@1` |
| determinism class | `pure` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0148_graph_diff_tool.txt`](prompts/P0148_graph_diff_tool.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0148-graph-diff-tool) |

**Mission.** Explains, in human terms, what the compiler did and why.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **structural graph diff with matching heuristics** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-decision rationale capture during passes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **human-readable optimisation report with measured impact** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **explanation fidelity tests against pass logs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t03.graph.graph_diff_tool@1`
- `cap.t03.graph.graph_diff_tool.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.op.op_registry@1` | use the in-file conservative substitute for `op_registry` (documented, slower, lower quality) and set `degraded['op_registry']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t02.kernel.kernel_docs_spec@1` | use the in-file conservative substitute for `kernel_docs_spec` (documented, slower, lower quality) and set `degraded['kernel_docs_spec']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structural graph diff with matching heuristics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-decision rationale capture during passes | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - human-readable optimisation report with measured impact | 520 | Third required mechanism. |
| 6 | Core implementation D - explanation fidelity tests against pass logs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0148_graph_diff_tool.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.graph.graph_diff_tool@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 10000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0149 · `compiler_fuzzer` — Compiler Fuzzer & Miscompile Hunter

| field | value |
|---|---|
| part id | `P0149` (49/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0149_compiler_fuzzer.rs` |
| module path | `hyperion.t03.compiler.compiler_fuzzer` |
| capability published | `cap.t03.compiler.compiler_fuzzer@1` |
| determinism class | `pure` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0149_compiler_fuzzer.txt`](prompts/P0149_compiler_fuzzer.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0149-compiler-fuzzer) |

**Mission.** Continuously attacks the compiler with generated programs.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **grammar-based IR generation with semantic validity**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **metamorphic testing (equivalent programs must agree)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **automatic reduction of miscompile cases** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **found-bug corpus with pinned regression tests** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t03.compiler.compiler_fuzzer@1`
- `cap.t03.compiler.compiler_fuzzer.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.graph.graph_diff_tool@1` | use the in-file conservative substitute for `graph_diff_tool` (documented, slower, lower quality) and set `degraded['graph_diff_tool']='local'` |
| `cap.t02.attn.attn_paged_decode@1` | use the in-file conservative substitute for `attn_paged_decode` (documented, slower, lower quality) and set `degraded['attn_paged_decode']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - grammar-based IR generation with semantic validity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - metamorphic testing (equivalent programs must agree) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic reduction of miscompile cases | 520 | Third required mechanism. |
| 6 | Core implementation D - found-bug corpus with pinned regression tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0149_compiler_fuzzer.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.compiler.compiler_fuzzer@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 11000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0150 · `build_provenance` — Build Provenance & Reproducibility Attestation

| field | value |
|---|---|
| part id | `P0150` (50/50 of T03) |
| tier | `T03` — Graph IR, Compiler & Autotuner |
| language | Rust 1.86 |
| file to produce | `parts/t03_compiler/P0150_build_provenance.rs` |
| module path | `hyperion.t03.compiler.build_provenance` |
| capability published | `cap.t03.build.build_provenance@1` |
| determinism class | `pure` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0150_build_provenance.txt`](prompts/P0150_build_provenance.txt) · [inline](docs/PROMPTS_T03.md#prompt-p0150-build-provenance) |

**Mission.** Every artifact proves exactly how it was produced.

**Tier context.** Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.

**Mandate — all four items are required; none is optional.**

1. Implement **full input hashing: sources, toolchains, flags, target descriptions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **in-toto-style attestation generation and verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **bit-identical rebuild verification across machines** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **provenance query interface for audits**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t03.build.build_provenance@1`
- `cap.t03.build.build_provenance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t03.compiler.compiler_fuzzer@1` | use the in-file conservative substitute for `compiler_fuzzer` (documented, slower, lower quality) and set `degraded['compiler_fuzzer']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t02.topk.topk_sort@1` | use the in-file conservative substitute for `topk_sort` (documented, slower, lower quality) and set `degraded['topk_sort']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - full input hashing: sources, toolchains, flags, target descripti | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - in-toto-style attestation generation and verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - bit-identical rebuild verification across machines | 520 | Third required mechanism. |
| 6 | Core implementation D - provenance query interface for audits | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t03_compiler/P0150_build_provenance.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t03.build.build_provenance@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 12000 ns at the declared reference shape.
- [ ] Declared determinism class `pure` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---
