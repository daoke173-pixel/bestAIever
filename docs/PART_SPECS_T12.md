# HYPERION-Ω — Part specifications · T12 · Code Intelligence & Repository Surgery

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Benchmarks this tier is accountable for.** SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond

**Tier dependencies.** T01, T10, T11

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0551](#p0551-repo-index) | `repo_index` | Whole-Repository Semantic Index | `cap.t12.repo.repo_index@1` |
| [P0552](#p0552-code-parsing) | `code_parsing` | Multi-Language Parsing & Concrete Syntax Trees | `cap.t12.code.code_parsing@1` |
| [P0553](#p0553-semantic-analysis) | `semantic_analysis` | Cross-Language Semantic Analysis | `cap.t12.semantic.semantic_analysis@1` |
| [P0554](#p0554-call-graph) | `call_graph` | Call Graph & Dependency Analysis | `cap.t12.call.call_graph@1` |
| [P0555](#p0555-code-search) | `code_search` | Semantic & Structural Code Search | `cap.t12.code.code_search@1` |
| [P0556](#p0556-code-embeddings) | `code_embeddings` | Code Representation & Embeddings | `cap.t12.code.code_embeddings@1` |
| [P0557](#p0557-bug-localisation) | `bug_localisation` | Bug Localisation & Root Cause Analysis | `cap.t12.bug.bug_localisation@1` |
| [P0558](#p0558-patch-synthesis) | `patch_synthesis` | Patch Synthesis Engine | `cap.t12.patch.patch_synthesis@1` |
| [P0559](#p0559-patch-validation) | `patch_validation` | Patch Validation & Regression Guarding | `cap.t12.patch.patch_validation@1` |
| [P0560](#p0560-test-synthesis) | `test_synthesis` | Test Generation & Coverage Engineering | `cap.t12.test.test_synthesis@1` |
| [P0561](#p0561-mutation-testing) | `mutation_testing` | Mutation Testing & Test Quality Assessment | `cap.t12.mutation.mutation_testing@1` |
| [P0562](#p0562-code-review-engine) | `code_review_engine` | Automated Code Review & Hazard Detection | `cap.t12.code.code_review_engine@1` |
| [P0563](#p0563-static-analysis) | `static_analysis` | Static Analysis & Linting Integration | `cap.t12.static.static_analysis@1` |
| [P0564](#p0564-refactoring-engine) | `refactoring_engine` | Semantics-Preserving Refactoring Engine | `cap.t12.refactoring.refactoring_engine@1` |
| [P0565](#p0565-migration-engine) | `migration_engine` | Large-Scale Migration & Codemod Engine | `cap.t12.migration.migration_engine@1` |
| [P0566](#p0566-api-evolution) | `api_evolution` | API Compatibility & Breaking Change Analysis | `cap.t12.api.api_evolution@1` |
| [P0567](#p0567-dependency-reasoning) | `dependency_reasoning` | Dependency & Supply Chain Reasoning | `cap.t12.dependency.dependency_reasoning@1` |
| [P0568](#p0568-build-system) | `build_system` | Build System Understanding & Repair | `cap.t12.build.build_system@1` |
| [P0569](#p0569-code-execution-sandbox) | `code_execution_sandbox` | Code Execution & Validation Sandbox | `cap.t12.code.code_execution_sandbox@1` |
| [P0570](#p0570-test-orchestration) | `test_orchestration` | Test Selection, Ordering & Parallel Execution | `cap.t12.test.test_orchestration@1` |
| [P0571](#p0571-flaky-detection) | `flaky_detection` | Flaky Test Detection & Stabilisation | `cap.t12.flaky.flaky_detection@1` |
| [P0572](#p0572-performance-engineering) | `performance_engineering` | Performance Profiling & Optimisation Agent | `cap.t12.performance.performance_engineering@1` |
| [P0573](#p0573-concurrency-bugs) | `concurrency_bugs` | Concurrency Bug Detection & Repair | `cap.t12.concurrency.concurrency_bugs@1` |
| [P0574](#p0574-memory-safety) | `memory_safety` | Memory Safety & Resource Leak Analysis | `cap.t12.memory.memory_safety@1` |
| [P0575](#p0575-security-code-analysis) | `security_code_analysis` | Security Vulnerability Discovery | `cap.t12.security.security_code_analysis@1` |
| [P0576](#p0576-fuzzing-agent) | `fuzzing_agent` | Fuzzing Campaign Orchestration | `cap.t12.fuzzing.fuzzing_agent@1` |
| [P0577](#p0577-crash-triage) | `crash_triage` | Crash Triage & Deduplication | `cap.t12.crash.crash_triage@1` |
| [P0578](#p0578-code-generation-core) | `code_generation_core` | Production Code Generation Engine | `cap.t12.code.code_generation_core@1` |
| [P0579](#p0579-architecture-design) | `architecture_design` | Software Architecture Design & Review | `cap.t12.architecture.architecture_design@1` |
| [P0580](#p0580-legacy-comprehension) | `legacy_comprehension` | Legacy Code Comprehension | `cap.t12.legacy.legacy_comprehension@1` |
| [P0581](#p0581-code-documentation) | `code_documentation` | Documentation Generation & Maintenance | `cap.t12.code.code_documentation@1` |
| [P0582](#p0582-commit-history) | `commit_history` | Version History Analysis & Blame Reasoning | `cap.t12.commit.commit_history@1` |
| [P0583](#p0583-pr-workflow) | `pr_workflow` | Pull Request Authoring & Review Workflow | `cap.t12.pr.pr_workflow@1` |
| [P0584](#p0584-multi-repo) | `multi_repo` | Cross-Repository & Monorepo Coordination | `cap.t12.multi.multi_repo@1` |
| [P0585](#p0585-environment-setup) | `environment_setup` | Development Environment Reconstruction | `cap.t12.environment.environment_setup@1` |
| [P0586](#p0586-debugger-agent) | `debugger_agent` | Interactive Debugging Agent | `cap.t12.debugger.debugger_agent@1` |
| [P0587](#p0587-observability-agent) | `observability_agent` | Production Debugging from Telemetry | `cap.t12.observability.observability_agent@1` |
| [P0588](#p0588-data-pipeline-code) | `data_pipeline_code` | Data & ML Pipeline Engineering | `cap.t12.data.data_pipeline_code@1` |
| [P0589](#p0589-notebook-engineering) | `notebook_engineering` | Notebook & Exploratory Code Quality | `cap.t12.notebook.notebook_engineering@1` |
| [P0590](#p0590-frontend-engineering) | `frontend_engineering` | Frontend & UI Code Engineering | `cap.t12.frontend.frontend_engineering@1` |
| [P0591](#p0591-systems-programming) | `systems_programming` | Systems & Low-Level Code Engineering | `cap.t12.systems.systems_programming@1` |
| [P0592](#p0592-scientific-computing-code) | `scientific_computing_code` | Scientific & Numerical Code Engineering | `cap.t12.scientific.scientific_computing_code@1` |
| [P0593](#p0593-competitive-programming) | `competitive_programming` | Algorithmic Problem Solving Engine | `cap.t12.competitive.competitive_programming@1` |
| [P0594](#p0594-code-translation) | `code_translation` | Cross-Language Code Translation | `cap.t12.code.code_translation@1` |
| [P0595](#p0595-codebase-metrics) | `codebase_metrics` | Codebase Health Metrics & Technical Debt | `cap.t12.codebase.codebase_metrics@1` |
| [P0596](#p0596-swe-bench-harness) | `swe_bench_harness` | SWE-bench Family Harness | `cap.t12.swe.swe_bench_harness@1` |
| [P0597](#p0597-frontier-bench-harness) | `frontier_bench_harness` | Frontier-Bench & Terminal Coding Harness | `cap.t12.frontier.frontier_bench_harness@1` |
| [P0598](#p0598-cursorbench-harness) | `cursorbench_harness` | IDE-Integrated Coding Evaluation | `cap.t12.cursorbench.cursorbench_harness@1` |
| [P0599](#p0599-code-quality-gate) | `code_quality_gate` | Code Quality Gate for the 1000-Part Assembly | `cap.t12.code.code_quality_gate@1` |
| [P0600](#p0600-code-spec-doc) | `code_spec_doc` | Code Intelligence Specification & Capability Register | `cap.t12.code.code_spec_doc@1` |

---

### P0551 · `repo_index` — Whole-Repository Semantic Index

| field | value |
|---|---|
| part id | `P0551` (1/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0551_repo_index.py` |
| module path | `hyperion.t12.code.repo_index` |
| capability published | `cap.t12.repo.repo_index@1` |
| determinism class | `pure` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0551_repo_index.txt`](prompts/P0551_repo_index.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0551-repo-index) |

**Mission.** Understands a million-file repository as one coherent object.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **incremental multi-language index of symbols, types, references and call graphs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **build-system-aware target and dependency extraction** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **index freshness under concurrent edits with sub-second updates**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **indexing throughput and query-latency budgets on large monorepos** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.repo.repo_index@1`
- `cap.t12.repo.repo_index.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t10.numeric.numeric_reasoning@1` | use the in-file conservative substitute for `numeric_reasoning` (documented, slower, lower quality) and set `degraded['numeric_reasoning']='local'` |
| `cap.t11.spec.spec_language@1` | use the in-file conservative substitute for `spec_language` (documented, slower, lower quality) and set `degraded['spec_language']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - incremental multi-language index of symbols, types, references a | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - build-system-aware target and dependency extraction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - index freshness under concurrent edits with sub-second updates | 520 | Third required mechanism. |
| 6 | Core implementation D - indexing throughput and query-latency budgets on large monorepos | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0551_repo_index.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.repo.repo_index@1`.
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

### P0552 · `code_parsing` — Multi-Language Parsing & Concrete Syntax Trees

| field | value |
|---|---|
| part id | `P0552` (2/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0552_code_parsing.py` |
| module path | `hyperion.t12.code.code_parsing` |
| capability published | `cap.t12.code.code_parsing@1` |
| determinism class | `pure` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0552_code_parsing.txt`](prompts/P0552_code_parsing.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0552-code-parsing) |

**Mission.** Exact, error-tolerant parsing for 40+ languages.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **error-recovering parsers producing full-fidelity trees with trivia** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **incremental reparse of edited regions only**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **round-trip guarantee (parse then print equals original bytes)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **conformance testing against language test suites** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.code.code_parsing@1`
- `cap.t12.code.code_parsing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.repo.repo_index@1` | use the in-file conservative substitute for `repo_index` (documented, slower, lower quality) and set `degraded['repo_index']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t10.backtracking.backtracking@1` | use the in-file conservative substitute for `backtracking` (documented, slower, lower quality) and set `degraded['backtracking']='local'` |
| `cap.t11.verified.verified_kernels@1` | use the in-file conservative substitute for `verified_kernels` (documented, slower, lower quality) and set `degraded['verified_kernels']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - error-recovering parsers producing full-fidelity trees with triv | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - incremental reparse of edited regions only | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - round-trip guarantee (parse then print equals original bytes) | 520 | Third required mechanism. |
| 6 | Core implementation D - conformance testing against language test suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0552_code_parsing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_parsing@1`.
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

### P0553 · `semantic_analysis` — Cross-Language Semantic Analysis

| field | value |
|---|---|
| part id | `P0553` (3/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0553_semantic_analysis.py` |
| module path | `hyperion.t12.code.semantic_analysis` |
| capability published | `cap.t12.semantic.semantic_analysis@1` |
| determinism class | `pure` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0553_semantic_analysis.txt`](prompts/P0553_semantic_analysis.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0553-semantic-analysis) |

**Mission.** Types, scopes, effects and data flow, computed not guessed.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **scope and binding resolution with language-specific rules**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **type inference/checking integration with existing compilers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **data-flow and taint analysis across function boundaries** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy measurement against compiler ground truth** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.semantic.semantic_analysis@1`
- `cap.t12.semantic.semantic_analysis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_parsing@1` | use the in-file conservative substitute for `code_parsing` (documented, slower, lower quality) and set `degraded['code_parsing']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t10.question.question_asking@1` | use the in-file conservative substitute for `question_asking` (documented, slower, lower quality) and set `degraded['question_asking']='local'` |
| `cap.t11.proof.proof_of_work_bounds@1` | use the in-file conservative substitute for `proof_of_work_bounds` (documented, slower, lower quality) and set `degraded['proof_of_work_bounds']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - scope and binding resolution with language-specific rules | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - type inference/checking integration with existing compilers | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - data-flow and taint analysis across function boundaries | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement against compiler ground truth | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0553_semantic_analysis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.semantic.semantic_analysis@1`.
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

### P0554 · `call_graph` — Call Graph & Dependency Analysis

| field | value |
|---|---|
| part id | `P0554` (4/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0554_call_graph.py` |
| module path | `hyperion.t12.code.call_graph` |
| capability published | `cap.t12.call.call_graph@1` |
| determinism class | `pure` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0554_call_graph.txt`](prompts/P0554_call_graph.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0554-call-graph) |

**Mission.** Knows what calls what, including through dynamic dispatch.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **static call graph with virtual/dynamic dispatch resolution** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **dynamic-trace-informed graph refinement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **reachability, impact and blast-radius queries** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **precision/recall measurement against runtime traces**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.call.call_graph@1`
- `cap.t12.call.call_graph.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.semantic.semantic_analysis@1` | use the in-file conservative substitute for `semantic_analysis` (documented, slower, lower quality) and set `degraded['semantic_analysis']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t10.scratchpad.scratchpad_manager@1` | use the in-file conservative substitute for `scratchpad_manager` (documented, slower, lower quality) and set `degraded['scratchpad_manager']='local'` |
| `cap.t11.math.math_benchmark_formal@1` | use the in-file conservative substitute for `math_benchmark_formal` (documented, slower, lower quality) and set `degraded['math_benchmark_formal']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - static call graph with virtual/dynamic dispatch resolution | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dynamic-trace-informed graph refinement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reachability, impact and blast-radius queries | 520 | Third required mechanism. |
| 6 | Core implementation D - precision/recall measurement against runtime traces | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0554_call_graph.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.call.call_graph@1`.
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

### P0555 · `code_search` — Semantic & Structural Code Search

| field | value |
|---|---|
| part id | `P0555` (5/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0555_code_search.py` |
| module path | `hyperion.t12.code.code_search` |
| capability published | `cap.t12.code.code_search@1` |
| determinism class | `pure` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0555_code_search.txt`](prompts/P0555_code_search.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0555-code-search) |

**Mission.** Finds the right code by meaning, structure or behaviour.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **structural pattern queries (AST/tree-sitter-style) with variables** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **semantic search over code embeddings** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **behavioural search (find functions with this input/output relation)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **search-quality measurement on curated developer queries** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.code.code_search@1`
- `cap.t12.code.code_search.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.call.call_graph@1` | use the in-file conservative substitute for `call_graph` (documented, slower, lower quality) and set `degraded['call_graph']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t10.reasoning.reasoning_speed_proof@1` | use the in-file conservative substitute for `reasoning_speed_proof` (documented, slower, lower quality) and set `degraded['reasoning_speed_proof']='local'` |
| `cap.t11.proof.proof_speed@1` | use the in-file conservative substitute for `proof_speed` (documented, slower, lower quality) and set `degraded['proof_speed']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structural pattern queries (AST/tree-sitter-style) with variable | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - semantic search over code embeddings | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - behavioural search (find functions with this input/output relati | 520 | Third required mechanism. |
| 6 | Core implementation D - search-quality measurement on curated developer queries | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0555_code_search.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_search@1`.
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

### P0556 · `code_embeddings` — Code Representation & Embeddings

| field | value |
|---|---|
| part id | `P0556` (6/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0556_code_embeddings.py` |
| module path | `hyperion.t12.code.code_embeddings` |
| capability published | `cap.t12.code.code_embeddings@1` |
| determinism class | `pure` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0556_code_embeddings.txt`](prompts/P0556_code_embeddings.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0556-code-embeddings) |

**Mission.** Representations that capture what code does, not how it looks.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **structure-aware code embedding training and evaluation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **cross-language semantic alignment (same algorithm, different language)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **clone and near-clone detection accuracy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **retrieval quality on code-search benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.code.code_embeddings@1`
- `cap.t12.code.code_embeddings.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_search@1` | use the in-file conservative substitute for `code_search` (documented, slower, lower quality) and set `degraded['code_search']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t10.process.process_verifier@1` | use the in-file conservative substitute for `process_verifier` (documented, slower, lower quality) and set `degraded['process_verifier']='local'` |
| `cap.t11.premise.premise_selection@1` | use the in-file conservative substitute for `premise_selection` (documented, slower, lower quality) and set `degraded['premise_selection']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structure-aware code embedding training and evaluation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-language semantic alignment (same algorithm, different lan | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - clone and near-clone detection accuracy | 520 | Third required mechanism. |
| 6 | Core implementation D - retrieval quality on code-search benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0556_code_embeddings.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_embeddings@1`.
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

### P0557 · `bug_localisation` — Bug Localisation & Root Cause Analysis

| field | value |
|---|---|
| part id | `P0557` (7/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0557_bug_localisation.py` |
| module path | `hyperion.t12.code.bug_localisation` |
| capability published | `cap.t12.bug.bug_localisation@1` |
| determinism class | `pure` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0557_bug_localisation.txt`](prompts/P0557_bug_localisation.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0557-bug-localisation) |

**Mission.** Finds the actual cause, not the symptom.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **failure-to-code localisation from tests, traces and stack frames**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **causal chain reconstruction from symptom to root cause** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **distinguishing root cause from downstream symptom explicitly** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **localisation accuracy on curated real-bug datasets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.bug.bug_localisation@1`
- `cap.t12.bug.bug_localisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_embeddings@1` | use the in-file conservative substitute for `code_embeddings` (documented, slower, lower quality) and set `degraded['code_embeddings']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t10.goal.goal_management@1` | use the in-file conservative substitute for `goal_management` (documented, slower, lower quality) and set `degraded['goal_management']='local'` |
| `cap.t11.dependent.dependent_types@1` | use the in-file conservative substitute for `dependent_types` (documented, slower, lower quality) and set `degraded['dependent_types']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - failure-to-code localisation from tests, traces and stack frames | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - causal chain reconstruction from symptom to root cause | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - distinguishing root cause from downstream symptom explicitly | 520 | Third required mechanism. |
| 6 | Core implementation D - localisation accuracy on curated real-bug datasets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0557_bug_localisation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.bug.bug_localisation@1`.
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

### P0558 · `patch_synthesis` — Patch Synthesis Engine

| field | value |
|---|---|
| part id | `P0558` (8/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0558_patch_synthesis.py` |
| module path | `hyperion.t12.code.patch_synthesis` |
| capability published | `cap.t12.patch.patch_synthesis@1` |
| determinism class | `pure` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0558_patch_synthesis.txt`](prompts/P0558_patch_synthesis.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0558-patch-synthesis) |

**Mission.** Writes the minimal correct fix.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **repair candidate generation from root-cause understanding** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **minimality and style-consistency constraints** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **test-driven candidate validation with regression checking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **core contributor to SWE-bench Verified 99.8% target**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.patch.patch_synthesis@1`
- `cap.t12.patch.patch_synthesis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.bug.bug_localisation@1` | use the in-file conservative substitute for `bug_localisation` (documented, slower, lower quality) and set `degraded['bug_localisation']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t10.probabilistic.probabilistic_reasoning@1` | use the in-file conservative substitute for `probabilistic_reasoning` (documented, slower, lower quality) and set `degraded['probabilistic_reasoning']='local'` |
| `cap.t11.informalisatio.informalisation@1` | use the in-file conservative substitute for `informalisation` (documented, slower, lower quality) and set `degraded['informalisation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - repair candidate generation from root-cause understanding | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - minimality and style-consistency constraints | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - test-driven candidate validation with regression checking | 520 | Third required mechanism. |
| 6 | Core implementation D - core contributor to SWE-bench Verified 99.8% target | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0558_patch_synthesis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.patch.patch_synthesis@1`.
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

### P0559 · `patch_validation` — Patch Validation & Regression Guarding

| field | value |
|---|---|
| part id | `P0559` (9/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0559_patch_validation.py` |
| module path | `hyperion.t12.code.patch_validation` |
| capability published | `cap.t12.patch.patch_validation@1` |
| determinism class | `pure` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0559_patch_validation.txt`](prompts/P0559_patch_validation.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0559-patch-validation) |

**Mission.** Proves the fix fixes it and breaks nothing else.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **targeted test selection plus full-suite validation strategy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **behavioural-diff analysis beyond test outcomes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **flaky-test detection preventing false verdicts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured false-positive and false-negative validation rates** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.patch.patch_validation@1`
- `cap.t12.patch.patch_validation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.patch.patch_synthesis@1` | use the in-file conservative substitute for `patch_synthesis` (documented, slower, lower quality) and set `degraded['patch_synthesis']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t10.stopping.stopping_rules@1` | use the in-file conservative substitute for `stopping_rules` (documented, slower, lower quality) and set `degraded['stopping_rules']='local'` |
| `cap.t11.proof.proof_compression@1` | use the in-file conservative substitute for `proof_compression` (documented, slower, lower quality) and set `degraded['proof_compression']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - targeted test selection plus full-suite validation strategy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - behavioural-diff analysis beyond test outcomes | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - flaky-test detection preventing false verdicts | 520 | Third required mechanism. |
| 6 | Core implementation D - measured false-positive and false-negative validation rates | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0559_patch_validation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.patch.patch_validation@1`.
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

### P0560 · `test_synthesis` — Test Generation & Coverage Engineering

| field | value |
|---|---|
| part id | `P0560` (10/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0560_test_synthesis.py` |
| module path | `hyperion.t12.code.test_synthesis` |
| capability published | `cap.t12.test.test_synthesis@1` |
| determinism class | `pure` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0560_test_synthesis.txt`](prompts/P0560_test_synthesis.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0560-test-synthesis) |

**Mission.** Writes the tests that would have caught the bug.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **specification-derived and coverage-guided test generation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **property-based test synthesis with invariant discovery**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **assertion-quality scoring (does it actually detect faults)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **mutation-score measurement of generated suites** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.test.test_synthesis@1`
- `cap.t12.test.test_synthesis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.patch.patch_validation@1` | use the in-file conservative substitute for `patch_validation` (documented, slower, lower quality) and set `degraded['patch_validation']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t10.assumption.assumption_tracking@1` | use the in-file conservative substitute for `assumption_tracking` (documented, slower, lower quality) and set `degraded['assumption_tracking']='local'` |
| `cap.t11.statistical.statistical_guarantees@1` | use the in-file conservative substitute for `statistical_guarantees` (documented, slower, lower quality) and set `degraded['statistical_guarantees']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - specification-derived and coverage-guided test generation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - property-based test synthesis with invariant discovery | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - assertion-quality scoring (does it actually detect faults) | 520 | Third required mechanism. |
| 6 | Core implementation D - mutation-score measurement of generated suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0560_test_synthesis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.test.test_synthesis@1`.
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

### P0561 · `mutation_testing` — Mutation Testing & Test Quality Assessment

| field | value |
|---|---|
| part id | `P0561` (11/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0561_mutation_testing.py` |
| module path | `hyperion.t12.code.mutation_testing` |
| capability published | `cap.t12.mutation.mutation_testing@1` |
| determinism class | `pure` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0561_mutation_testing.txt`](prompts/P0561_mutation_testing.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0561-mutation-testing) |

**Mission.** Measures whether tests are real or decorative.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **mutation-operator library per language with realistic faults**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **equivalent-mutant detection and cost control** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **test-suite quality scoring and gap identification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **correlation between mutation score and real bug detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.mutation.mutation_testing@1`
- `cap.t12.mutation.mutation_testing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.test.test_synthesis@1` | use the in-file conservative substitute for `test_synthesis` (documented, slower, lower quality) and set `degraded['test_synthesis']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t10.reasoning.reasoning_cost_model@1` | use the in-file conservative substitute for `reasoning_cost_model` (documented, slower, lower quality) and set `degraded['reasoning_cost_model']='local'` |
| `cap.t11.regression.regression_proofs@1` | use the in-file conservative substitute for `regression_proofs` (documented, slower, lower quality) and set `degraded['regression_proofs']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - mutation-operator library per language with realistic faults | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - equivalent-mutant detection and cost control | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - test-suite quality scoring and gap identification | 520 | Third required mechanism. |
| 6 | Core implementation D - correlation between mutation score and real bug detection | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0561_mutation_testing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.mutation.mutation_testing@1`.
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

### P0562 · `code_review_engine` — Automated Code Review & Hazard Detection

| field | value |
|---|---|
| part id | `P0562` (12/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0562_code_review_engine.py` |
| module path | `hyperion.t12.code.code_review_engine` |
| capability published | `cap.t12.code.code_review_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0562_code_review_engine.txt`](prompts/P0562_code_review_engine.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0562-code-review-engine) |

**Mission.** Spots the subtle, codebase-specific problem a human reviewer would.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **review-comment generation with severity and confidence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **codebase-convention learning and enforcement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **hazard classes: concurrency, resource, security, numerical, API misuse** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 4x fewer missed flaws than Opus-class review baselines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.code.code_review_engine@1`
- `cap.t12.code.code_review_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.mutation.mutation_testing@1` | use the in-file conservative substitute for `mutation_testing` (documented, slower, lower quality) and set `degraded['mutation_testing']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t10.collective.collective_reasoning@1` | use the in-file conservative substitute for `collective_reasoning` (documented, slower, lower quality) and set `degraded['collective_reasoning']='local'` |
| `cap.t11.verification.verification_bench@1` | use the in-file conservative substitute for `verification_bench` (documented, slower, lower quality) and set `degraded['verification_bench']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - review-comment generation with severity and confidence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - codebase-convention learning and enforcement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hazard classes: concurrency, resource, security, numerical, API  | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 4x fewer missed flaws than Opus-class review baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0562_code_review_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_review_engine@1`.
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

### P0563 · `static_analysis` — Static Analysis & Linting Integration

| field | value |
|---|---|
| part id | `P0563` (13/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0563_static_analysis.py` |
| module path | `hyperion.t12.code.static_analysis` |
| capability published | `cap.t12.static.static_analysis@1` |
| determinism class | `pure` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0563_static_analysis.txt`](prompts/P0563_static_analysis.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0563-static-analysis) |

**Mission.** All the cheap checks, deduplicated and prioritised.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-tool orchestration with finding deduplication** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **false-positive suppression learned from developer feedback** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **severity ranking by exploitability and blast radius**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **precision measurement on labelled finding sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.static.static_analysis@1`
- `cap.t12.static.static_analysis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_review_engine@1` | use the in-file conservative substitute for `code_review_engine` (documented, slower, lower quality) and set `degraded['code_review_engine']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t10.beam.beam_pruning@1` | use the in-file conservative substitute for `beam_pruning` (documented, slower, lower quality) and set `degraded['beam_pruning']='local'` |
| `cap.t11.proof.proof_search@1` | use the in-file conservative substitute for `proof_search` (documented, slower, lower quality) and set `degraded['proof_search']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-tool orchestration with finding deduplication | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - false-positive suppression learned from developer feedback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - severity ranking by exploitability and blast radius | 520 | Third required mechanism. |
| 6 | Core implementation D - precision measurement on labelled finding sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0563_static_analysis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.static.static_analysis@1`.
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

### P0564 · `refactoring_engine` — Semantics-Preserving Refactoring Engine

| field | value |
|---|---|
| part id | `P0564` (14/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0564_refactoring_engine.py` |
| module path | `hyperion.t12.code.refactoring_engine` |
| capability published | `cap.t12.refactoring.refactoring_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0564_refactoring_engine.txt`](prompts/P0564_refactoring_engine.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0564-refactoring-engine) |

**Mission.** Large-scale changes that provably do not change behaviour.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **refactoring catalogue with precondition checking per transformation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cross-file atomic application with rollback**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **behaviour-preservation verification (tests plus static equivalence)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **success rate on large-scale refactoring tasks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.refactoring.refactoring_engine@1`
- `cap.t12.refactoring.refactoring_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.static.static_analysis@1` | use the in-file conservative substitute for `static_analysis` (documented, slower, lower quality) and set `degraded['static_analysis']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t10.planning.planning_engine@1` | use the in-file conservative substitute for `planning_engine` (documented, slower, lower quality) and set `degraded['planning_engine']='local'` |
| `cap.t11.refinement.refinement_types@1` | use the in-file conservative substitute for `refinement_types` (documented, slower, lower quality) and set `degraded['refinement_types']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - refactoring catalogue with precondition checking per transformat | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-file atomic application with rollback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - behaviour-preservation verification (tests plus static equivalen | 520 | Third required mechanism. |
| 6 | Core implementation D - success rate on large-scale refactoring tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0564_refactoring_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.refactoring.refactoring_engine@1`.
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

### P0565 · `migration_engine` — Large-Scale Migration & Codemod Engine

| field | value |
|---|---|
| part id | `P0565` (15/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0565_migration_engine.py` |
| module path | `hyperion.t12.code.migration_engine` |
| capability published | `cap.t12.migration.migration_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0565_migration_engine.txt`](prompts/P0565_migration_engine.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0565-migration-engine) |

**Mission.** Upgrades a million-line codebase in one session.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **codemod authoring from few examples with generalisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **incremental application with continuous validation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **progress tracking and partial-migration coherence** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured throughput on real migration corpora** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.migration.migration_engine@1`
- `cap.t12.migration.migration_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.refactoring.refactoring_engine@1` | use the in-file conservative substitute for `refactoring_engine` (documented, slower, lower quality) and set `degraded['refactoring_engine']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t10.counterfactual.counterfactual_reasoning@1` | use the in-file conservative substitute for `counterfactual_reasoning` (documented, slower, lower quality) and set `degraded['counterfactual_reasoning']='local'` |
| `cap.t11.autoformalisat.autoformalisation@1` | use the in-file conservative substitute for `autoformalisation` (documented, slower, lower quality) and set `degraded['autoformalisation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - codemod authoring from few examples with generalisation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - incremental application with continuous validation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - progress tracking and partial-migration coherence | 520 | Third required mechanism. |
| 6 | Core implementation D - measured throughput on real migration corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0565_migration_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.migration.migration_engine@1`.
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

### P0566 · `api_evolution` — API Compatibility & Breaking Change Analysis

| field | value |
|---|---|
| part id | `P0566` (16/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0566_api_evolution.py` |
| module path | `hyperion.t12.code.api_evolution` |
| capability published | `cap.t12.api.api_evolution@1` |
| determinism class | `pure` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0566_api_evolution.txt`](prompts/P0566_api_evolution.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0566-api-evolution) |

**Mission.** Knows exactly who breaks when an interface changes.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **semantic diff of public interfaces across versions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **downstream impact analysis with usage evidence** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **migration-guide and shim generation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on curated API-change datasets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.api.api_evolution@1`
- `cap.t12.api.api_evolution.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.migration.migration_engine@1` | use the in-file conservative substitute for `migration_engine` (documented, slower, lower quality) and set `degraded['migration_engine']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t10.difficulty.difficulty_estimation@1` | use the in-file conservative substitute for `difficulty_estimation` (documented, slower, lower quality) and set `degraded['difficulty_estimation']='local'` |
| `cap.t11.counterexample.counterexample_engine@1` | use the in-file conservative substitute for `counterexample_engine` (documented, slower, lower quality) and set `degraded['counterexample_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - semantic diff of public interfaces across versions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - downstream impact analysis with usage evidence | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - migration-guide and shim generation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on curated API-change datasets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0566_api_evolution.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.api.api_evolution@1`.
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

### P0567 · `dependency_reasoning` — Dependency & Supply Chain Reasoning

| field | value |
|---|---|
| part id | `P0567` (17/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0567_dependency_reasoning.py` |
| module path | `hyperion.t12.code.dependency_reasoning` |
| capability published | `cap.t12.dependency.dependency_reasoning@1` |
| determinism class | `pure` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0567_dependency_reasoning.txt`](prompts/P0567_dependency_reasoning.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0567-dependency-reasoning) |

**Mission.** Understands the whole dependency tree and its risks.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **version-constraint solving and conflict explanation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **vulnerability and license analysis with transitive reach** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **update-risk assessment with behavioural-change prediction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured accuracy of update-safety predictions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.dependency.dependency_reasoning@1`
- `cap.t12.dependency.dependency_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.api.api_evolution@1` | use the in-file conservative substitute for `api_evolution` (documented, slower, lower quality) and set `degraded['api_evolution']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t10.evidence.evidence_integration@1` | use the in-file conservative substitute for `evidence_integration` (documented, slower, lower quality) and set `degraded['evidence_integration']='local'` |
| `cap.t11.numeric.numeric_verification_ml@1` | use the in-file conservative substitute for `numeric_verification_ml` (documented, slower, lower quality) and set `degraded['numeric_verification_ml']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - version-constraint solving and conflict explanation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - vulnerability and license analysis with transitive reach | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - update-risk assessment with behavioural-change prediction | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy of update-safety predictions | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0567_dependency_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.dependency.dependency_reasoning@1`.
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

### P0568 · `build_system` — Build System Understanding & Repair

| field | value |
|---|---|
| part id | `P0568` (18/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0568_build_system.py` |
| module path | `hyperion.t12.code.build_system` |
| capability published | `cap.t12.build.build_system@1` |
| determinism class | `pure` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0568_build_system.txt`](prompts/P0568_build_system.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0568-build-system) |

**Mission.** Fixes the build, the hardest part of real engineering work.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **build-graph extraction across major build systems** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **build-failure diagnosis with actionable remediation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **hermeticity and reproducibility analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **build-repair success rate on curated failure corpora** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.build.build_system@1`
- `cap.t12.build.build_system.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.dependency.dependency_reasoning@1` | use the in-file conservative substitute for `dependency_reasoning` (documented, slower, lower quality) and set `degraded['dependency_reasoning']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t10.reasoning.reasoning_search_bench@1` | use the in-file conservative substitute for `reasoning_search_bench` (documented, slower, lower quality) and set `degraded['reasoning_search_bench']='local'` |
| `cap.t11.hybrid.hybrid_verification@1` | use the in-file conservative substitute for `hybrid_verification` (documented, slower, lower quality) and set `degraded['hybrid_verification']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - build-graph extraction across major build systems | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - build-failure diagnosis with actionable remediation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hermeticity and reproducibility analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - build-repair success rate on curated failure corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0568_build_system.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.build.build_system@1`.
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

### P0569 · `code_execution_sandbox` — Code Execution & Validation Sandbox

| field | value |
|---|---|
| part id | `P0569` (19/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0569_code_execution_sandbox.py` |
| module path | `hyperion.t12.code.code_execution_sandbox` |
| capability published | `cap.t12.code.code_execution_sandbox@1` |
| determinism class | `pure` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0569_code_execution_sandbox.txt`](prompts/P0569_code_execution_sandbox.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0569-code-execution-sandbox) |

**Mission.** Runs untrusted code safely, fast, thousands of times.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **isolated execution with resource limits and syscall filtering**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **snapshot/restore for fast repeated runs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **deterministic execution mode for reproducible results** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **throughput measurement of validation runs per second** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.code.code_execution_sandbox@1`
- `cap.t12.code.code_execution_sandbox.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.build.build_system@1` | use the in-file conservative substitute for `build_system` (documented, slower, lower quality) and set `degraded['build_system']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t10.reasoning.reasoning_interpretability@1` | use the in-file conservative substitute for `reasoning_interpretability` (documented, slower, lower quality) and set `degraded['reasoning_interpretability']='local'` |
| `cap.t11.trust.trust_boundaries@1` | use the in-file conservative substitute for `trust_boundaries` (documented, slower, lower quality) and set `degraded['trust_boundaries']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - isolated execution with resource limits and syscall filtering | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - snapshot/restore for fast repeated runs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deterministic execution mode for reproducible results | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput measurement of validation runs per second | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0569_code_execution_sandbox.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_execution_sandbox@1`.
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

### P0570 · `test_orchestration` — Test Selection, Ordering & Parallel Execution

| field | value |
|---|---|
| part id | `P0570` (20/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0570_test_orchestration.py` |
| module path | `hyperion.t12.code.test_orchestration` |
| capability published | `cap.t12.test.test_orchestration@1` |
| determinism class | `pure` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0570_test_orchestration.txt`](prompts/P0570_test_orchestration.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0570-test-orchestration) |

**Mission.** Runs the right 1% of tests in seconds instead of all of them in hours.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **change-impact-based test selection with safety bounds** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **failure-probability ordering for fastest feedback** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **parallel execution with dependency and resource awareness** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured feedback-latency reduction at equal fault detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.test.test_orchestration@1`
- `cap.t12.test.test_orchestration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_execution_sandbox@1` | use the in-file conservative substitute for `code_execution_sandbox` (documented, slower, lower quality) and set `degraded['code_execution_sandbox']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t10.graph.graph_search@1` | use the in-file conservative substitute for `graph_search` (documented, slower, lower quality) and set `degraded['graph_search']='local'` |
| `cap.t11.itp.itp_bridge@1` | use the in-file conservative substitute for `itp_bridge` (documented, slower, lower quality) and set `degraded['itp_bridge']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - change-impact-based test selection with safety bounds | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - failure-probability ordering for fastest feedback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - parallel execution with dependency and resource awareness | 520 | Third required mechanism. |
| 6 | Core implementation D - measured feedback-latency reduction at equal fault detection | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0570_test_orchestration.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.test.test_orchestration@1`.
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

### P0571 · `flaky_detection` — Flaky Test Detection & Stabilisation

| field | value |
|---|---|
| part id | `P0571` (21/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0571_flaky_detection.py` |
| module path | `hyperion.t12.code.flaky_detection` |
| capability published | `cap.t12.flaky.flaky_detection@1` |
| determinism class | `pure` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0571_flaky_detection.txt`](prompts/P0571_flaky_detection.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0571-flaky-detection) |

**Mission.** Distinguishes real failures from noise, then removes the noise.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **flakiness detection via repeated and varied execution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **root-cause classification (timing, order, resource, randomness)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **stabilisation patch generation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured reduction in flaky-failure rate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.flaky.flaky_detection@1`
- `cap.t12.flaky.flaky_detection.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.test.test_orchestration@1` | use the in-file conservative substitute for `test_orchestration` (documented, slower, lower quality) and set `degraded['test_orchestration']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t10.decomposition.decomposition@1` | use the in-file conservative substitute for `decomposition` (documented, slower, lower quality) and set `degraded['decomposition']='local'` |
| `cap.t11.model.model_checking@1` | use the in-file conservative substitute for `model_checking` (documented, slower, lower quality) and set `degraded['model_checking']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - flakiness detection via repeated and varied execution | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - root-cause classification (timing, order, resource, randomness) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - stabilisation patch generation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction in flaky-failure rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0571_flaky_detection.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.flaky.flaky_detection@1`.
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

### P0572 · `performance_engineering` — Performance Profiling & Optimisation Agent

| field | value |
|---|---|
| part id | `P0572` (22/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0572_performance_engineering.py` |
| module path | `hyperion.t12.code.performance_engineering` |
| capability published | `cap.t12.performance.performance_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0572_performance_engineering.txt`](prompts/P0572_performance_engineering.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0572-performance-engineering) |

**Mission.** Makes other people's code faster, with proof.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **profiling orchestration and bottleneck identification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **optimisation candidate generation with correctness preservation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **before/after measurement with statistical rigor** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured speedups achieved on real codebases** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.performance.performance_engineering@1`
- `cap.t12.performance.performance_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.flaky.flaky_detection@1` | use the in-file conservative substitute for `flaky_detection` (documented, slower, lower quality) and set `degraded['flaky_detection']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t10.program.program_synthesis_reasoning@1` | use the in-file conservative substitute for `program_synthesis_reasoning` (documented, slower, lower quality) and set `degraded['program_synthesis_reasoning']='local'` |
| `cap.t11.theorem.theorem_library@1` | use the in-file conservative substitute for `theorem_library` (documented, slower, lower quality) and set `degraded['theorem_library']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - profiling orchestration and bottleneck identification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - optimisation candidate generation with correctness preservation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - before/after measurement with statistical rigor | 520 | Third required mechanism. |
| 6 | Core implementation D - measured speedups achieved on real codebases | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0572_performance_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.performance.performance_engineering@1`.
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

### P0573 · `concurrency_bugs` — Concurrency Bug Detection & Repair

| field | value |
|---|---|
| part id | `P0573` (23/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0573_concurrency_bugs.py` |
| module path | `hyperion.t12.code.concurrency_bugs` |
| capability published | `cap.t12.concurrency.concurrency_bugs@1` |
| determinism class | `pure` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0573_concurrency_bugs.txt`](prompts/P0573_concurrency_bugs.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0573-concurrency-bugs) |

**Mission.** Finds the race that only happens in production.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **race, deadlock and atomicity-violation detection (static plus dynamic)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **schedule exploration with systematic interleaving control** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **repair synthesis preserving performance** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **detection rate on curated concurrency bug datasets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.concurrency.concurrency_bugs@1`
- `cap.t12.concurrency.concurrency_bugs.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.performance.performance_engineering@1` | use the in-file conservative substitute for `performance_engineering` (documented, slower, lower quality) and set `degraded['performance_engineering']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t10.meta.meta_reasoning@1` | use the in-file conservative substitute for `meta_reasoning` (documented, slower, lower quality) and set `degraded['meta_reasoning']='local'` |
| `cap.t11.proof.proof_repair@1` | use the in-file conservative substitute for `proof_repair` (documented, slower, lower quality) and set `degraded['proof_repair']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - race, deadlock and atomicity-violation detection (static plus dy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - schedule exploration with systematic interleaving control | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - repair synthesis preserving performance | 520 | Third required mechanism. |
| 6 | Core implementation D - detection rate on curated concurrency bug datasets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0573_concurrency_bugs.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.concurrency.concurrency_bugs@1`.
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

### P0574 · `memory_safety` — Memory Safety & Resource Leak Analysis

| field | value |
|---|---|
| part id | `P0574` (24/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0574_memory_safety.py` |
| module path | `hyperion.t12.code.memory_safety` |
| capability published | `cap.t12.memory.memory_safety@1` |
| determinism class | `pure` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0574_memory_safety.txt`](prompts/P0574_memory_safety.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0574-memory-safety) |

**Mission.** Catches use-after-free, leaks and overflows before shipping.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **ownership and lifetime analysis across languages** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **leak detection for memory, handles, locks and connections** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **sanitiser orchestration and finding triage** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **detection rate on labelled memory-bug corpora**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.memory.memory_safety@1`
- `cap.t12.memory.memory_safety.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.concurrency.concurrency_bugs@1` | use the in-file conservative substitute for `concurrency_bugs` (documented, slower, lower quality) and set `degraded['concurrency_bugs']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t10.hypothesis.hypothesis_management@1` | use the in-file conservative substitute for `hypothesis_management` (documented, slower, lower quality) and set `degraded['hypothesis_management']='local'` |
| `cap.t11.concurrency.concurrency_verification@1` | use the in-file conservative substitute for `concurrency_verification` (documented, slower, lower quality) and set `degraded['concurrency_verification']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - ownership and lifetime analysis across languages | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - leak detection for memory, handles, locks and connections | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - sanitiser orchestration and finding triage | 520 | Third required mechanism. |
| 6 | Core implementation D - detection rate on labelled memory-bug corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0574_memory_safety.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.memory.memory_safety@1`.
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

### P0575 · `security_code_analysis` — Security Vulnerability Discovery

| field | value |
|---|---|
| part id | `P0575` (25/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0575_security_code_analysis.py` |
| module path | `hyperion.t12.code.security_code_analysis` |
| capability published | `cap.t12.security.security_code_analysis@1` |
| determinism class | `pure` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0575_security_code_analysis.txt`](prompts/P0575_security_code_analysis.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0575-security-code-analysis) |

**Mission.** Finds real, exploitable vulnerabilities in source code.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **taint analysis from sources to sinks with sanitiser awareness** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **vulnerability-class detectors mapped to a standard taxonomy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **exploitability triage without generating exploit code**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: OSS-Fuzz find rate 97% versus Opus 5's ~78%** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.security.security_code_analysis@1`
- `cap.t12.security.security_code_analysis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.memory.memory_safety@1` | use the in-file conservative substitute for `memory_safety` (documented, slower, lower quality) and set `degraded['memory_safety']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t10.proof.proof_sketch@1` | use the in-file conservative substitute for `proof_sketch` (documented, slower, lower quality) and set `degraded['proof_sketch']='local'` |
| `cap.t11.verification.verification_scheduling@1` | use the in-file conservative substitute for `verification_scheduling` (documented, slower, lower quality) and set `degraded['verification_scheduling']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - taint analysis from sources to sinks with sanitiser awareness | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - vulnerability-class detectors mapped to a standard taxonomy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - exploitability triage without generating exploit code | 520 | Third required mechanism. |
| 6 | Core implementation D - target: OSS-Fuzz find rate 97% versus Opus 5's ~78% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0575_security_code_analysis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.security.security_code_analysis@1`.
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

### P0576 · `fuzzing_agent` — Fuzzing Campaign Orchestration

| field | value |
|---|---|
| part id | `P0576` (26/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0576_fuzzing_agent.py` |
| module path | `hyperion.t12.code.fuzzing_agent` |
| capability published | `cap.t12.fuzzing.fuzzing_agent@1` |
| determinism class | `pure` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0576_fuzzing_agent.txt`](prompts/P0576_fuzzing_agent.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0576-fuzzing-agent) |

**Mission.** Drives fuzzers to the interesting parts of the code.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **harness generation for arbitrary library entry points** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **corpus construction, minimisation and seed scheduling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **coverage-plateau detection and strategy switching** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured bug-discovery rate per CPU hour** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.fuzzing.fuzzing_agent@1`
- `cap.t12.fuzzing.fuzzing_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.security.security_code_analysis@1` | use the in-file conservative substitute for `security_code_analysis` (documented, slower, lower quality) and set `degraded['security_code_analysis']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t10.adversarial.adversarial_reasoning@1` | use the in-file conservative substitute for `adversarial_reasoning` (documented, slower, lower quality) and set `degraded['adversarial_reasoning']='local'` |
| `cap.t11.verification.verification_cache@1` | use the in-file conservative substitute for `verification_cache` (documented, slower, lower quality) and set `degraded['verification_cache']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - harness generation for arbitrary library entry points | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - corpus construction, minimisation and seed scheduling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - coverage-plateau detection and strategy switching | 520 | Third required mechanism. |
| 6 | Core implementation D - measured bug-discovery rate per CPU hour | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0576_fuzzing_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.fuzzing.fuzzing_agent@1`.
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

### P0577 · `crash_triage` — Crash Triage & Deduplication

| field | value |
|---|---|
| part id | `P0577` (27/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0577_crash_triage.py` |
| module path | `hyperion.t12.code.crash_triage` |
| capability published | `cap.t12.crash.crash_triage@1` |
| determinism class | `pure` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0577_crash_triage.txt`](prompts/P0577_crash_triage.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0577-crash-triage) |

**Mission.** Turns 10000 crashes into 12 distinct bugs.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **stack and root-cause based crash clustering**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **severity and exploitability assessment** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **minimal reproducer generation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **deduplication accuracy on labelled crash corpora** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.crash.crash_triage@1`
- `cap.t12.crash.crash_triage.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.fuzzing.fuzzing_agent@1` | use the in-file conservative substitute for `fuzzing_agent` (documented, slower, lower quality) and set `degraded['fuzzing_agent']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t10.tree.tree_search@1` | use the in-file conservative substitute for `tree_search` (documented, slower, lower quality) and set `degraded['tree_search']='local'` |
| `cap.t11.sat.sat_engine@1` | use the in-file conservative substitute for `sat_engine` (documented, slower, lower quality) and set `degraded['sat_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - stack and root-cause based crash clustering | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - severity and exploitability assessment | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - minimal reproducer generation | 520 | Third required mechanism. |
| 6 | Core implementation D - deduplication accuracy on labelled crash corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0577_crash_triage.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.crash.crash_triage@1`.
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

### P0578 · `code_generation_core` — Production Code Generation Engine

| field | value |
|---|---|
| part id | `P0578` (28/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0578_code_generation_core.py` |
| module path | `hyperion.t12.code.code_generation_core` |
| capability published | `cap.t12.code.code_generation_core@1` |
| determinism class | `pure` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0578_code_generation_core.txt`](prompts/P0578_code_generation_core.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0578-code-generation-core) |

**Mission.** Writes code that ships: correct, idiomatic, tested, documented.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **specification-to-implementation generation with design rationale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **codebase-convention conformance and API reuse over reinvention** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **self-verification loop before returning code** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured first-pass acceptance rate by expert reviewers**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.code.code_generation_core@1`
- `cap.t12.code.code_generation_core.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.crash.crash_triage@1` | use the in-file conservative substitute for `crash_triage` (documented, slower, lower quality) and set `degraded['crash_triage']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t10.debate.debate_ensemble@1` | use the in-file conservative substitute for `debate_ensemble` (documented, slower, lower quality) and set `degraded['debate_ensemble']='local'` |
| `cap.t11.abstract.abstract_interpretation@1` | use the in-file conservative substitute for `abstract_interpretation` (documented, slower, lower quality) and set `degraded['abstract_interpretation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - specification-to-implementation generation with design rationale | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - codebase-convention conformance and API reuse over reinvention | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - self-verification loop before returning code | 520 | Third required mechanism. |
| 6 | Core implementation D - measured first-pass acceptance rate by expert reviewers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0578_code_generation_core.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_generation_core@1`.
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

### P0579 · `architecture_design` — Software Architecture Design & Review

| field | value |
|---|---|
| part id | `P0579` (29/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0579_architecture_design.py` |
| module path | `hyperion.t12.code.architecture_design` |
| capability published | `cap.t12.architecture.architecture_design@1` |
| determinism class | `pure` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0579_architecture_design.txt`](prompts/P0579_architecture_design.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0579-architecture-design) |

**Mission.** Makes the big decisions well, and explains the tradeoffs.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **design-alternative generation with explicit tradeoff analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **constraint-driven architecture selection and documentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **architecture-erosion detection against the intended design**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert-evaluation results on real design tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.architecture.architecture_design@1`
- `cap.t12.architecture.architecture_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_generation_core@1` | use the in-file conservative substitute for `code_generation_core` (documented, slower, lower quality) and set `degraded['code_generation_core']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t10.induction.induction_engine@1` | use the in-file conservative substitute for `induction_engine` (documented, slower, lower quality) and set `degraded['induction_engine']='local'` |
| `cap.t11.computer.computer_algebra@1` | use the in-file conservative substitute for `computer_algebra` (documented, slower, lower quality) and set `degraded['computer_algebra']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - design-alternative generation with explicit tradeoff analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - constraint-driven architecture selection and documentation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - architecture-erosion detection against the intended design | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-evaluation results on real design tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0579_architecture_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.architecture.architecture_design@1`.
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

### P0580 · `legacy_comprehension` — Legacy Code Comprehension

| field | value |
|---|---|
| part id | `P0580` (30/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0580_legacy_comprehension.py` |
| module path | `hyperion.t12.code.legacy_comprehension` |
| capability published | `cap.t12.legacy.legacy_comprehension@1` |
| determinism class | `pure` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0580_legacy_comprehension.txt`](prompts/P0580_legacy_comprehension.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0580-legacy-comprehension) |

**Mission.** Understands undocumented code nobody remembers writing.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **behaviour reconstruction from code, tests and history** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **implicit-contract and invariant extraction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **documentation generation with accuracy verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **comprehension-accuracy measurement via expert quizzes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.legacy.legacy_comprehension@1`
- `cap.t12.legacy.legacy_comprehension.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.architecture.architecture_design@1` | use the in-file conservative substitute for `architecture_design` (documented, slower, lower quality) and set `degraded['architecture_design']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t10.commonsense.commonsense_engine@1` | use the in-file conservative substitute for `commonsense_engine` (documented, slower, lower quality) and set `degraded['commonsense_engine']='local'` |
| `cap.t11.symbolic.symbolic_execution@1` | use the in-file conservative substitute for `symbolic_execution` (documented, slower, lower quality) and set `degraded['symbolic_execution']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - behaviour reconstruction from code, tests and history | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - implicit-contract and invariant extraction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - documentation generation with accuracy verification | 520 | Third required mechanism. |
| 6 | Core implementation D - comprehension-accuracy measurement via expert quizzes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0580_legacy_comprehension.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.legacy.legacy_comprehension@1`.
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

### P0581 · `code_documentation` — Documentation Generation & Maintenance

| field | value |
|---|---|
| part id | `P0581` (31/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0581_code_documentation.py` |
| module path | `hyperion.t12.code.code_documentation` |
| capability published | `cap.t12.code.code_documentation@1` |
| determinism class | `pure` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0581_code_documentation.txt`](prompts/P0581_code_documentation.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0581-code-documentation) |

**Mission.** Docs that are correct and stay correct.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **API and design documentation generation from code and intent**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **doc/code drift detection and automatic repair** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **example generation with executable verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement of generated documentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.code.code_documentation@1`
- `cap.t12.code.code_documentation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.legacy.legacy_comprehension@1` | use the in-file conservative substitute for `legacy_comprehension` (documented, slower, lower quality) and set `degraded['legacy_comprehension']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t10.parallel.parallel_reasoning@1` | use the in-file conservative substitute for `parallel_reasoning` (documented, slower, lower quality) and set `degraded['parallel_reasoning']='local'` |
| `cap.t11.crypto.crypto_verification@1` | use the in-file conservative substitute for `crypto_verification` (documented, slower, lower quality) and set `degraded['crypto_verification']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - API and design documentation generation from code and intent | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - doc/code drift detection and automatic repair | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - example generation with executable verification | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement of generated documentation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0581_code_documentation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_documentation@1`.
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

### P0582 · `commit_history` — Version History Analysis & Blame Reasoning

| field | value |
|---|---|
| part id | `P0582` (32/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0582_commit_history.py` |
| module path | `hyperion.t12.code.commit_history` |
| capability published | `cap.t12.commit.commit_history@1` |
| determinism class | `pure` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0582_commit_history.txt`](prompts/P0582_commit_history.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0582-commit-history) |

**Mission.** Uses the repository's past to solve its present.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **change-intent reconstruction from commits and reviews** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **regression introduction identification (bisect-style reasoning)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **code-ownership and expertise mapping** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on curated regression-attribution tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.commit.commit_history@1`
- `cap.t12.commit.commit_history.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_documentation@1` | use the in-file conservative substitute for `code_documentation` (documented, slower, lower quality) and set `degraded['code_documentation']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t10.multi.multi_step_arithmetic@1` | use the in-file conservative substitute for `multi_step_arithmetic` (documented, slower, lower quality) and set `degraded['multi_step_arithmetic']='local'` |
| `cap.t11.proof.proof_assistant_ux@1` | use the in-file conservative substitute for `proof_assistant_ux` (documented, slower, lower quality) and set `degraded['proof_assistant_ux']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - change-intent reconstruction from commits and reviews | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - regression introduction identification (bisect-style reasoning) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - code-ownership and expertise mapping | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on curated regression-attribution tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0582_commit_history.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.commit.commit_history@1`.
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

### P0583 · `pr_workflow` — Pull Request Authoring & Review Workflow

| field | value |
|---|---|
| part id | `P0583` (33/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0583_pr_workflow.py` |
| module path | `hyperion.t12.code.pr_workflow` |
| capability published | `cap.t12.pr.pr_workflow@1` |
| determinism class | `pure` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0583_pr_workflow.txt`](prompts/P0583_pr_workflow.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0583-pr-workflow) |

**Mission.** Handles the whole change lifecycle like a careful senior engineer.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **branch hygiene, template conformance and CI-expectation reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **PR description generation with testing evidence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **review-feedback incorporation with change tracking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured PR acceptance rate without rework** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.pr.pr_workflow@1`
- `cap.t12.pr.pr_workflow.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.commit.commit_history@1` | use the in-file conservative substitute for `commit_history` (documented, slower, lower quality) and set `degraded['commit_history']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t10.error.error_taxonomy@1` | use the in-file conservative substitute for `error_taxonomy` (documented, slower, lower quality) and set `degraded['error_taxonomy']='local'` |
| `cap.t11.financial.financial_verification@1` | use the in-file conservative substitute for `financial_verification` (documented, slower, lower quality) and set `degraded['financial_verification']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - branch hygiene, template conformance and CI-expectation reasonin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - PR description generation with testing evidence | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - review-feedback incorporation with change tracking | 520 | Third required mechanism. |
| 6 | Core implementation D - measured PR acceptance rate without rework | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0583_pr_workflow.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.pr.pr_workflow@1`.
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

### P0584 · `multi_repo` — Cross-Repository & Monorepo Coordination

| field | value |
|---|---|
| part id | `P0584` (34/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0584_multi_repo.py` |
| module path | `hyperion.t12.code.multi_repo` |
| capability published | `cap.t12.multi.multi_repo@1` |
| determinism class | `pure` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0584_multi_repo.txt`](prompts/P0584_multi_repo.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0584-multi-repo) |

**Mission.** Coordinated changes across many repositories at once.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **cross-repo dependency and change-order planning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **atomic-ish multi-repo landing strategies**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **version-skew reasoning during rollout** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **success rate on multi-repo change tasks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.multi.multi_repo@1`
- `cap.t12.multi.multi_repo.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.pr.pr_workflow@1` | use the in-file conservative substitute for `pr_workflow` (documented, slower, lower quality) and set `degraded['pr_workflow']='local'` |
| `cap.t10.search.search_controller@1` | use the in-file conservative substitute for `search_controller` (documented, slower, lower quality) and set `degraded['search_controller']='local'` |
| `cap.t11.smt.smt_bridge@1` | use the in-file conservative substitute for `smt_bridge` (documented, slower, lower quality) and set `degraded['smt_bridge']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cross-repo dependency and change-order planning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - atomic-ish multi-repo landing strategies | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - version-skew reasoning during rollout | 520 | Third required mechanism. |
| 6 | Core implementation D - success rate on multi-repo change tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0584_multi_repo.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.multi.multi_repo@1`.
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

### P0585 · `environment_setup` — Development Environment Reconstruction

| field | value |
|---|---|
| part id | `P0585` (35/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0585_environment_setup.py` |
| module path | `hyperion.t12.code.environment_setup` |
| capability published | `cap.t12.environment.environment_setup@1` |
| determinism class | `pure` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0585_environment_setup.txt`](prompts/P0585_environment_setup.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0585-environment-setup) |

**Mission.** Gets an unfamiliar project building and testing from scratch.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **environment inference from repository signals**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **dependency installation with conflict resolution** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **container/hermetic environment generation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **success rate on a corpus of arbitrary open-source projects** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.environment.environment_setup@1`
- `cap.t12.environment.environment_setup.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.multi.multi_repo@1` | use the in-file conservative substitute for `multi_repo` (documented, slower, lower quality) and set `degraded['multi_repo']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t10.self.self_critique@1` | use the in-file conservative substitute for `self_critique` (documented, slower, lower quality) and set `degraded['self_critique']='local'` |
| `cap.t11.invariant.invariant_inference@1` | use the in-file conservative substitute for `invariant_inference` (documented, slower, lower quality) and set `degraded['invariant_inference']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - environment inference from repository signals | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dependency installation with conflict resolution | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - container/hermetic environment generation | 520 | Third required mechanism. |
| 6 | Core implementation D - success rate on a corpus of arbitrary open-source projects | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0585_environment_setup.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.environment.environment_setup@1`.
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

### P0586 · `debugger_agent` — Interactive Debugging Agent

| field | value |
|---|---|
| part id | `P0586` (36/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0586_debugger_agent.py` |
| module path | `hyperion.t12.code.debugger_agent` |
| capability published | `cap.t12.debugger.debugger_agent@1` |
| determinism class | `pure` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0586_debugger_agent.txt`](prompts/P0586_debugger_agent.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0586-debugger-agent) |

**Mission.** Uses a real debugger the way an expert does.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **breakpoint/watchpoint strategy from hypotheses about the bug** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **state inspection and hypothesis-driven experimentation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **time-travel debugging where available** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured bug-resolution rate versus print-debugging baselines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.debugger.debugger_agent@1`
- `cap.t12.debugger.debugger_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.environment.environment_setup@1` | use the in-file conservative substitute for `environment_setup` (documented, slower, lower quality) and set `degraded['environment_setup']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t10.abstraction.abstraction_engine@1` | use the in-file conservative substitute for `abstraction_engine` (documented, slower, lower quality) and set `degraded['abstraction_engine']='local'` |
| `cap.t11.exact.exact_arithmetic@1` | use the in-file conservative substitute for `exact_arithmetic` (documented, slower, lower quality) and set `degraded['exact_arithmetic']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - breakpoint/watchpoint strategy from hypotheses about the bug | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - state inspection and hypothesis-driven experimentation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - time-travel debugging where available | 520 | Third required mechanism. |
| 6 | Core implementation D - measured bug-resolution rate versus print-debugging baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0586_debugger_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.debugger.debugger_agent@1`.
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

### P0587 · `observability_agent` — Production Debugging from Telemetry

| field | value |
|---|---|
| part id | `P0587` (37/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0587_observability_agent.py` |
| module path | `hyperion.t12.code.observability_agent` |
| capability published | `cap.t12.observability.observability_agent@1` |
| determinism class | `pure` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0587_observability_agent.txt`](prompts/P0587_observability_agent.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0587-observability-agent) |

**Mission.** Diagnoses live systems from logs, metrics and traces.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-signal correlation and anomaly localisation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **hypothesis generation and validation from telemetry queries** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **incident-timeline reconstruction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **diagnosis accuracy on labelled incident corpora** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.observability.observability_agent@1`
- `cap.t12.observability.observability_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.debugger.debugger_agent@1` | use the in-file conservative substitute for `debugger_agent` (documented, slower, lower quality) and set `degraded['debugger_agent']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t10.spatial.spatial_reasoning@1` | use the in-file conservative substitute for `spatial_reasoning` (documented, slower, lower quality) and set `degraded['spatial_reasoning']='local'` |
| `cap.t11.property.property_testing_formal@1` | use the in-file conservative substitute for `property_testing_formal` (documented, slower, lower quality) and set `degraded['property_testing_formal']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-signal correlation and anomaly localisation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hypothesis generation and validation from telemetry queries | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - incident-timeline reconstruction | 520 | Third required mechanism. |
| 6 | Core implementation D - diagnosis accuracy on labelled incident corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0587_observability_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.observability.observability_agent@1`.
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

### P0588 · `data_pipeline_code` — Data & ML Pipeline Engineering

| field | value |
|---|---|
| part id | `P0588` (38/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0588_data_pipeline_code.py` |
| module path | `hyperion.t12.code.data_pipeline_code` |
| capability published | `cap.t12.data.data_pipeline_code@1` |
| determinism class | `pure` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0588_data_pipeline_code.txt`](prompts/P0588_data_pipeline_code.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0588-data-pipeline-code) |

**Mission.** Correct data code: schemas, joins, leakage, reproducibility.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **schema and data-contract validation with drift detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **join-correctness and cardinality reasoning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **train/test leakage detection in ML pipelines** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **error detection rate on seeded data-bug corpora** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.data.data_pipeline_code@1`
- `cap.t12.data.data_pipeline_code.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.observability.observability_agent@1` | use the in-file conservative substitute for `observability_agent` (documented, slower, lower quality) and set `degraded['observability_agent']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t10.chain.chain_compression@1` | use the in-file conservative substitute for `chain_compression` (documented, slower, lower quality) and set `degraded['chain_compression']='local'` |
| `cap.t11.type.type_safety_proofs@1` | use the in-file conservative substitute for `type_safety_proofs` (documented, slower, lower quality) and set `degraded['type_safety_proofs']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - schema and data-contract validation with drift detection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - join-correctness and cardinality reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - train/test leakage detection in ML pipelines | 520 | Third required mechanism. |
| 6 | Core implementation D - error detection rate on seeded data-bug corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0588_data_pipeline_code.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.data.data_pipeline_code@1`.
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

### P0589 · `notebook_engineering` — Notebook & Exploratory Code Quality

| field | value |
|---|---|
| part id | `P0589` (39/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0589_notebook_engineering.py` |
| module path | `hyperion.t12.code.notebook_engineering` |
| capability published | `cap.t12.notebook.notebook_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0589_notebook_engineering.txt`](prompts/P0589_notebook_engineering.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0589-notebook-engineering) |

**Mission.** Turns exploratory analysis into reproducible engineering.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **execution-order and hidden-state hazard detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **notebook-to-module refactoring with equivalence checking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **result reproducibility verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured reproducibility improvement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.notebook.notebook_engineering@1`
- `cap.t12.notebook.notebook_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.data.data_pipeline_code@1` | use the in-file conservative substitute for `data_pipeline_code` (documented, slower, lower quality) and set `degraded['data_pipeline_code']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t10.reasoning.reasoning_robustness@1` | use the in-file conservative substitute for `reasoning_robustness` (documented, slower, lower quality) and set `degraded['reasoning_robustness']='local'` |
| `cap.t11.rewriting.rewriting_systems@1` | use the in-file conservative substitute for `rewriting_systems` (documented, slower, lower quality) and set `degraded['rewriting_systems']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - execution-order and hidden-state hazard detection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - notebook-to-module refactoring with equivalence checking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - result reproducibility verification | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reproducibility improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0589_notebook_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.notebook.notebook_engineering@1`.
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

### P0590 · `frontend_engineering` — Frontend & UI Code Engineering

| field | value |
|---|---|
| part id | `P0590` (40/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0590_frontend_engineering.py` |
| module path | `hyperion.t12.code.frontend_engineering` |
| capability published | `cap.t12.frontend.frontend_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0590_frontend_engineering.txt`](prompts/P0590_frontend_engineering.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0590-frontend-engineering) |

**Mission.** Builds interfaces that actually work at every viewport.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **component architecture with accessibility and state-management rigor** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **browser-based self-verification at multiple viewports** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **visual-regression and layout-hazard detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured defect rate versus Opus-class frontend baselines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.frontend.frontend_engineering@1`
- `cap.t12.frontend.frontend_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.notebook.notebook_engineering@1` | use the in-file conservative substitute for `notebook_engineering` (documented, slower, lower quality) and set `degraded['notebook_engineering']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t10.reasoning.reasoning_transfer@1` | use the in-file conservative substitute for `reasoning_transfer` (documented, slower, lower quality) and set `degraded['reasoning_transfer']='local'` |
| `cap.t11.legal.legal_formalisation@1` | use the in-file conservative substitute for `legal_formalisation` (documented, slower, lower quality) and set `degraded['legal_formalisation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - component architecture with accessibility and state-management r | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - browser-based self-verification at multiple viewports | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - visual-regression and layout-hazard detection | 520 | Third required mechanism. |
| 6 | Core implementation D - measured defect rate versus Opus-class frontend baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0590_frontend_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.frontend.frontend_engineering@1`.
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

### P0591 · `systems_programming` — Systems & Low-Level Code Engineering

| field | value |
|---|---|
| part id | `P0591` (41/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0591_systems_programming.py` |
| module path | `hyperion.t12.code.systems_programming` |
| capability published | `cap.t12.systems.systems_programming@1` |
| determinism class | `pure` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0591_systems_programming.txt`](prompts/P0591_systems_programming.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0591-systems-programming) |

**Mission.** Correct code where correctness is hardest.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **memory model, alignment and undefined-behaviour reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **driver, embedded and kernel-adjacent code patterns** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **hardware-interaction correctness verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **success rate on systems-programming task suites** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.systems.systems_programming@1`
- `cap.t12.systems.systems_programming.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.frontend.frontend_engineering@1` | use the in-file conservative substitute for `frontend_engineering` (documented, slower, lower quality) and set `degraded['frontend_engineering']='local'` |
| `cap.t10.thought.thought_program_ir@1` | use the in-file conservative substitute for `thought_program_ir` (documented, slower, lower quality) and set `degraded['thought_program_ir']='local'` |
| `cap.t11.logic.logic_core@1` | use the in-file conservative substitute for `logic_core` (documented, slower, lower quality) and set `degraded['logic_core']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - memory model, alignment and undefined-behaviour reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - driver, embedded and kernel-adjacent code patterns | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hardware-interaction correctness verification | 520 | Third required mechanism. |
| 6 | Core implementation D - success rate on systems-programming task suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0591_systems_programming.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.systems.systems_programming@1`.
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

### P0592 · `scientific_computing_code` — Scientific & Numerical Code Engineering

| field | value |
|---|---|
| part id | `P0592` (42/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0592_scientific_computing_code.py` |
| module path | `hyperion.t12.code.scientific_computing_code` |
| capability published | `cap.t12.scientific.scientific_computing_code@1` |
| determinism class | `pure` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0592_scientific_computing_code.txt`](prompts/P0592_scientific_computing_code.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0592-scientific-computing-code) |

**Mission.** Numerically correct, not just syntactically correct.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **numerical stability and conditioning analysis of implementations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **unit and dimensional correctness enforcement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **reproducibility and determinism engineering** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **error detection rate on seeded numerical-bug corpora** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.scientific.scientific_computing_code@1`
- `cap.t12.scientific.scientific_computing_code.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.systems.systems_programming@1` | use the in-file conservative substitute for `systems_programming` (documented, slower, lower quality) and set `degraded['systems_programming']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t10.self.self_consistency@1` | use the in-file conservative substitute for `self_consistency` (documented, slower, lower quality) and set `degraded['self_consistency']='local'` |
| `cap.t11.verification.verification_conditions@1` | use the in-file conservative substitute for `verification_conditions` (documented, slower, lower quality) and set `degraded['verification_conditions']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - numerical stability and conditioning analysis of implementations | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - unit and dimensional correctness enforcement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reproducibility and determinism engineering | 520 | Third required mechanism. |
| 6 | Core implementation D - error detection rate on seeded numerical-bug corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0592_scientific_computing_code.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.scientific.scientific_computing_code@1`.
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

### P0593 · `competitive_programming` — Algorithmic Problem Solving Engine

| field | value |
|---|---|
| part id | `P0593` (43/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0593_competitive_programming.py` |
| module path | `hyperion.t12.code.competitive_programming` |
| capability published | `cap.t12.competitive.competitive_programming@1` |
| determinism class | `pure` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0593_competitive_programming.txt`](prompts/P0593_competitive_programming.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0593-competitive-programming) |

**Mission.** Solves hard algorithmic problems with proven complexity.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **algorithm selection with complexity analysis against constraints**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Pro**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **edge-case enumeration and stress testing against brute force** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **proof of correctness for the chosen approach** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **solve rate on contest-problem benchmark sets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.competitive.competitive_programming@1`
- `cap.t12.competitive.competitive_programming.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.scientific.scientific_computing_code@1` | use the in-file conservative substitute for `scientific_computing_code` (documented, slower, lower quality) and set `degraded['scientific_computing_code']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t10.analogy.analogy_engine@1` | use the in-file conservative substitute for `analogy_engine` (documented, slower, lower quality) and set `degraded['analogy_engine']='local'` |
| `cap.t11.certified.certified_numerics@1` | use the in-file conservative substitute for `certified_numerics` (documented, slower, lower quality) and set `degraded['certified_numerics']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - algorithm selection with complexity analysis against constraints | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - edge-case enumeration and stress testing against brute force | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - proof of correctness for the chosen approach | 520 | Third required mechanism. |
| 6 | Core implementation D - solve rate on contest-problem benchmark sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0593_competitive_programming.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.competitive.competitive_programming@1`.
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

### P0594 · `code_translation` — Cross-Language Code Translation

| field | value |
|---|---|
| part id | `P0594` (44/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0594_code_translation.py` |
| module path | `hyperion.t12.code.code_translation` |
| capability published | `cap.t12.code.code_translation@1` |
| determinism class | `pure` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0594_code_translation.txt`](prompts/P0594_code_translation.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0594-code-translation) |

**Mission.** Ports code between languages without changing behaviour.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **idiomatic translation preserving semantics and performance characteristics** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **behavioural-equivalence verification via differential testing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **unsupported-construct handling with explicit reporting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **equivalence rate measurement on translation benchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.code.code_translation@1`
- `cap.t12.code.code_translation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.competitive.competitive_programming@1` | use the in-file conservative substitute for `competitive_programming` (documented, slower, lower quality) and set `degraded['competitive_programming']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t10.temporal.temporal_reasoning@1` | use the in-file conservative substitute for `temporal_reasoning` (documented, slower, lower quality) and set `degraded['temporal_reasoning']='local'` |
| `cap.t11.contract.contract_checking@1` | use the in-file conservative substitute for `contract_checking` (documented, slower, lower quality) and set `degraded['contract_checking']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - idiomatic translation preserving semantics and performance chara | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - behavioural-equivalence verification via differential testing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - unsupported-construct handling with explicit reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - equivalence rate measurement on translation benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0594_code_translation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_translation@1`.
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

### P0595 · `codebase_metrics` — Codebase Health Metrics & Technical Debt

| field | value |
|---|---|
| part id | `P0595` (45/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0595_codebase_metrics.py` |
| module path | `hyperion.t12.code.codebase_metrics` |
| capability published | `cap.t12.codebase.codebase_metrics@1` |
| determinism class | `pure` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0595_codebase_metrics.txt`](prompts/P0595_codebase_metrics.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0595-codebase-metrics) |

**Mission.** Quantifies what is wrong with a codebase and what to fix first.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **complexity, coupling, duplication and churn metrics** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **FrontierCode Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **technical-debt quantification with remediation cost estimates** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **prioritised remediation roadmap generation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **validation that metric-driven fixes reduce real defect rates** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.codebase.codebase_metrics@1`
- `cap.t12.codebase.codebase_metrics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_translation@1` | use the in-file conservative substitute for `code_translation` (documented, slower, lower quality) and set `degraded['code_translation']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t10.reasoning.reasoning_memory@1` | use the in-file conservative substitute for `reasoning_memory` (documented, slower, lower quality) and set `degraded['reasoning_memory']='local'` |
| `cap.t11.hoare.hoare_logic_engine@1` | use the in-file conservative substitute for `hoare_logic_engine` (documented, slower, lower quality) and set `degraded['hoare_logic_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - complexity, coupling, duplication and churn metrics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - technical-debt quantification with remediation cost estimates | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - prioritised remediation roadmap generation | 520 | Third required mechanism. |
| 6 | Core implementation D - validation that metric-driven fixes reduce real defect rates | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0595_codebase_metrics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.codebase.codebase_metrics@1`.
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

### P0596 · `swe_bench_harness` — SWE-bench Family Harness

| field | value |
|---|---|
| part id | `P0596` (46/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0596_swe_bench_harness.py` |
| module path | `hyperion.t12.code.swe_bench_harness` |
| capability published | `cap.t12.swe.swe_bench_harness@1` |
| determinism class | `pure` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0596_swe_bench_harness.txt`](prompts/P0596_swe_bench_harness.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0596-swe-bench-harness) |

**Mission.** Reproducible measurement on the benchmarks that define coding ability.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **SWE-bench Verified/Pro harnesses with containerised evaluation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **minimal-bash-agent and full-scaffold modes for fair comparison**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-instance failure analysis and error taxonomy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **targets: Verified 99.8% (Opus 5: 97.0%), Pro 96.5%** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.swe.swe_bench_harness@1`
- `cap.t12.swe.swe_bench_harness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.codebase.codebase_metrics@1` | use the in-file conservative substitute for `codebase_metrics` (documented, slower, lower quality) and set `degraded['codebase_metrics']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t10.reasoning.reasoning_faithfulness@1` | use the in-file conservative substitute for `reasoning_faithfulness` (documented, slower, lower quality) and set `degraded['reasoning_faithfulness']='local'` |
| `cap.t11.decision.decision_procedures@1` | use the in-file conservative substitute for `decision_procedures` (documented, slower, lower quality) and set `degraded['decision_procedures']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - SWE-bench Verified/Pro harnesses with containerised evaluation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - minimal-bash-agent and full-scaffold modes for fair comparison | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-instance failure analysis and error taxonomy | 520 | Third required mechanism. |
| 6 | Core implementation D - targets: Verified 99.8% (Opus 5: 97.0%), Pro 96.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0596_swe_bench_harness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.swe.swe_bench_harness@1`.
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

### P0597 · `frontier_bench_harness` — Frontier-Bench & Terminal Coding Harness

| field | value |
|---|---|
| part id | `P0597` (47/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0597_frontier_bench_harness.py` |
| module path | `hyperion.t12.code.frontier_bench_harness` |
| capability published | `cap.t12.frontier.frontier_bench_harness@1` |
| determinism class | `pure` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0597_frontier_bench_harness.txt`](prompts/P0597_frontier_bench_harness.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0597-frontier-bench-harness) |

**Mission.** The hardest agentic coding evaluations.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **Frontier-Bench v0.1 style long-horizon task harness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Pro** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **Terminal-Bench 2.1 harness with environment fidelity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **task-level diagnostics and capability attribution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **targets: Frontier-Bench 92% (Opus 5: 43.3%), Terminal-Bench 98.5%** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.frontier.frontier_bench_harness@1`
- `cap.t12.frontier.frontier_bench_harness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.swe.swe_bench_harness@1` | use the in-file conservative substitute for `swe_bench_harness` (documented, slower, lower quality) and set `degraded['swe_bench_harness']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t10.subgoal.subgoal_caching@1` | use the in-file conservative substitute for `subgoal_caching` (documented, slower, lower quality) and set `degraded['subgoal_caching']='local'` |
| `cap.t11.scientific.scientific_verification@1` | use the in-file conservative substitute for `scientific_verification` (documented, slower, lower quality) and set `degraded['scientific_verification']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - Frontier-Bench v0.1 style long-horizon task harness | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - Terminal-Bench 2.1 harness with environment fidelity | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - task-level diagnostics and capability attribution | 520 | Third required mechanism. |
| 6 | Core implementation D - targets: Frontier-Bench 92% (Opus 5: 43.3%), Terminal-Bench 98.5 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0597_frontier_bench_harness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.frontier.frontier_bench_harness@1`.
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

### P0598 · `cursorbench_harness` — IDE-Integrated Coding Evaluation

| field | value |
|---|---|
| part id | `P0598` (48/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0598_cursorbench_harness.py` |
| module path | `hyperion.t12.code.cursorbench_harness` |
| capability published | `cap.t12.cursorbench.cursorbench_harness@1` |
| determinism class | `pure` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0598_cursorbench_harness.txt`](prompts/P0598_cursorbench_harness.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0598-cursorbench-harness) |

**Mission.** Measures real developer-workflow performance, not just benchmarks.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **CursorBench-style harness with edit-application fidelity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **latency and cost-per-task measurement alongside quality** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **developer-workflow task library** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 140% of Opus 5's CursorBench-relative score at lower cost**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t12.cursorbench.cursorbench_harness@1`
- `cap.t12.cursorbench.cursorbench_harness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.frontier.frontier_bench_harness@1` | use the in-file conservative substitute for `frontier_bench_harness` (documented, slower, lower quality) and set `degraded['frontier_bench_harness']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t10.reasoning.reasoning_spec_doc@1` | use the in-file conservative substitute for `reasoning_spec_doc` (documented, slower, lower quality) and set `degraded['reasoning_spec_doc']='local'` |
| `cap.t11.formal.formal_spec_doc@1` | use the in-file conservative substitute for `formal_spec_doc` (documented, slower, lower quality) and set `degraded['formal_spec_doc']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - CursorBench-style harness with edit-application fidelity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - latency and cost-per-task measurement alongside quality | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - developer-workflow task library | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 140% of Opus 5's CursorBench-relative score at lower cos | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0598_cursorbench_harness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.cursorbench.cursorbench_harness@1`.
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

### P0599 · `code_quality_gate` — Code Quality Gate for the 1000-Part Assembly

| field | value |
|---|---|
| part id | `P0599` (49/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0599_code_quality_gate.py` |
| module path | `hyperion.t12.code.code_quality_gate` |
| capability published | `cap.t12.code.code_quality_gate@1` |
| determinism class | `pure` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0599_code_quality_gate.txt`](prompts/P0599_code_quality_gate.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0599-code-quality-gate) |

**Mission.** Applies this tier's own capabilities to the project itself.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **automated review of all 1000 part files against the Ω-Contract** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **FrontierCode Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cross-part consistency and duplication detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-part quality scorecard with remediation guidance**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **assembly-wide quality report generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t12.code.code_quality_gate@1`
- `cap.t12.code.code_quality_gate.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.cursorbench.cursorbench_harness@1` | use the in-file conservative substitute for `cursorbench_harness` (documented, slower, lower quality) and set `degraded['cursorbench_harness']='local'` |
| `cap.t10.outcome.outcome_verifier@1` | use the in-file conservative substitute for `outcome_verifier` (documented, slower, lower quality) and set `degraded['outcome_verifier']='local'` |
| `cap.t11.proof.proof_certificate@1` | use the in-file conservative substitute for `proof_certificate` (documented, slower, lower quality) and set `degraded['proof_certificate']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - automated review of all 1000 part files against the Ω-Contract | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-part consistency and duplication detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-part quality scorecard with remediation guidance | 520 | Third required mechanism. |
| 6 | Core implementation D - assembly-wide quality report generation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0599_code_quality_gate.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_quality_gate@1`.
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

### P0600 · `code_spec_doc` — Code Intelligence Specification & Capability Register

| field | value |
|---|---|
| part id | `P0600` (50/50 of T12) |
| tier | `T12` — Code Intelligence & Repository Surgery |
| language | Python 3.13 |
| file to produce | `parts/t12_code/P0600_code_spec_doc.py` |
| module path | `hyperion.t12.code.code_spec_doc` |
| capability published | `cap.t12.code.code_spec_doc@1` |
| determinism class | `pure` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, SWE-bench Pro, Frontier-Bench v0.1, FrontierCode Diamond |
| worker prompt | [`prompts/P0600_code_spec_doc.txt`](prompts/P0600_code_spec_doc.txt) · [inline](docs/PROMPTS_T12.md#prompt-p0600-code-spec-doc) |

**Mission.** The authoritative description of all code capabilities and their limits.

**Tier context.** Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.

**Mandate — all four items are required; none is optional.**

1. Implement **capability register with measured performance per task class** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **honest limitation documentation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Pro** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **benchmark-result aggregation with provenance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **drift detection between claims and measurements** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **FrontierCode Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t12.code.code_spec_doc@1`
- `cap.t12.code.code_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t12.code.code_quality_gate@1` | use the in-file conservative substitute for `code_quality_gate` (documented, slower, lower quality) and set `degraded['code_quality_gate']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t10.constraint.constraint_reasoning@1` | use the in-file conservative substitute for `constraint_reasoning` (documented, slower, lower quality) and set `degraded['constraint_reasoning']='local'` |
| `cap.t11.termination.termination_analysis@1` | use the in-file conservative substitute for `termination_analysis` (documented, slower, lower quality) and set `degraded['termination_analysis']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability register with measured performance per task class | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - honest limitation documentation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - benchmark-result aggregation with provenance | 520 | Third required mechanism. |
| 6 | Core implementation D - drift detection between claims and measurements | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t12_code/P0600_code_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t12.code.code_spec_doc@1`.
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
