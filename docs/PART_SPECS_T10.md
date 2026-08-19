# HYPERION-Ω — Part specifications · T10 · Reasoning, Search & Deliberation

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Benchmarks this tier is accountable for.** ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026

**Tier dependencies.** T01, T05, T07

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0451](#p0451-thought-program-ir) | `thought_program_ir` | Thought Program Representation | `cap.t10.thought.thought_program_ir@1` |
| [P0452](#p0452-search-controller) | `search_controller` | Deliberation Search Controller | `cap.t10.search.search_controller@1` |
| [P0453](#p0453-tree-search) | `tree_search` | Tree Search over Reasoning States | `cap.t10.tree.tree_search@1` |
| [P0454](#p0454-graph-search) | `graph_search` | Graph-of-Thought Reasoning | `cap.t10.graph.graph_search@1` |
| [P0455](#p0455-beam-pruning) | `beam_pruning` | Verifier-Guided Beam Pruning | `cap.t10.beam.beam_pruning@1` |
| [P0456](#p0456-process-verifier) | `process_verifier` | Process Reward Model & Step Verification | `cap.t10.process.process_verifier@1` |
| [P0457](#p0457-outcome-verifier) | `outcome_verifier` | Outcome Verification & Answer Checking | `cap.t10.outcome.outcome_verifier@1` |
| [P0458](#p0458-self-consistency) | `self_consistency` | Self-Consistency & Sample Aggregation | `cap.t10.self.self_consistency@1` |
| [P0459](#p0459-self-critique) | `self_critique` | Self-Critique & Revision Loop | `cap.t10.self.self_critique@1` |
| [P0460](#p0460-debate-ensemble) | `debate_ensemble` | Multi-Perspective Debate & Adversarial Review | `cap.t10.debate.debate_ensemble@1` |
| [P0461](#p0461-decomposition) | `decomposition` | Problem Decomposition Engine | `cap.t10.decomposition.decomposition@1` |
| [P0462](#p0462-planning-engine) | `planning_engine` | Hierarchical Planning Engine | `cap.t10.planning.planning_engine@1` |
| [P0463](#p0463-goal-management) | `goal_management` | Goal Stack & Intent Tracking | `cap.t10.goal.goal_management@1` |
| [P0464](#p0464-constraint-reasoning) | `constraint_reasoning` | Constraint Satisfaction & Optimisation Reasoning | `cap.t10.constraint.constraint_reasoning@1` |
| [P0465](#p0465-analogy-engine) | `analogy_engine` | Analogical & Case-Based Reasoning | `cap.t10.analogy.analogy_engine@1` |
| [P0466](#p0466-abstraction-engine) | `abstraction_engine` | Abstraction Discovery & Concept Formation | `cap.t10.abstraction.abstraction_engine@1` |
| [P0467](#p0467-induction-engine) | `induction_engine` | Rule Induction from Few Examples | `cap.t10.induction.induction_engine@1` |
| [P0468](#p0468-program-synthesis-reasoning) | `program_synthesis_reasoning` | Neural-Guided Program Synthesis | `cap.t10.program.program_synthesis_reasoning@1` |
| [P0469](#p0469-counterfactual-reasoning) | `counterfactual_reasoning` | Counterfactual & Hypothetical Reasoning | `cap.t10.counterfactual.counterfactual_reasoning@1` |
| [P0470](#p0470-probabilistic-reasoning) | `probabilistic_reasoning` | Probabilistic Inference Engine | `cap.t10.probabilistic.probabilistic_reasoning@1` |
| [P0471](#p0471-numeric-reasoning) | `numeric_reasoning` | Exact Numeric & Quantitative Reasoning | `cap.t10.numeric.numeric_reasoning@1` |
| [P0472](#p0472-temporal-reasoning) | `temporal_reasoning` | Temporal & Scheduling Reasoning | `cap.t10.temporal.temporal_reasoning@1` |
| [P0473](#p0473-spatial-reasoning) | `spatial_reasoning` | Spatial & Geometric Reasoning | `cap.t10.spatial.spatial_reasoning@1` |
| [P0474](#p0474-commonsense-engine) | `commonsense_engine` | Commonsense Reasoning & Default Inference | `cap.t10.commonsense.commonsense_engine@1` |
| [P0475](#p0475-meta-reasoning) | `meta_reasoning` | Meta-Reasoning & Strategy Selection | `cap.t10.meta.meta_reasoning@1` |
| [P0476](#p0476-difficulty-estimation) | `difficulty_estimation` | Problem Difficulty Estimation | `cap.t10.difficulty.difficulty_estimation@1` |
| [P0477](#p0477-stopping-rules) | `stopping_rules` | Optimal Stopping & Confidence Thresholds | `cap.t10.stopping.stopping_rules@1` |
| [P0478](#p0478-backtracking) | `backtracking` | Backtracking & Dead-End Recovery | `cap.t10.backtracking.backtracking@1` |
| [P0479](#p0479-reasoning-memory) | `reasoning_memory` | Reasoning Trace Memory & Lesson Extraction | `cap.t10.reasoning.reasoning_memory@1` |
| [P0480](#p0480-chain-compression) | `chain_compression` | Reasoning Chain Compression & Distillation | `cap.t10.chain.chain_compression@1` |
| [P0481](#p0481-parallel-reasoning) | `parallel_reasoning` | Parallel Reasoning Orchestration | `cap.t10.parallel.parallel_reasoning@1` |
| [P0482](#p0482-hypothesis-management) | `hypothesis_management` | Hypothesis Space Management | `cap.t10.hypothesis.hypothesis_management@1` |
| [P0483](#p0483-evidence-integration) | `evidence_integration` | Evidence Aggregation & Weighing | `cap.t10.evidence.evidence_integration@1` |
| [P0484](#p0484-assumption-tracking) | `assumption_tracking` | Assumption Tracking & Explicit Uncertainty | `cap.t10.assumption.assumption_tracking@1` |
| [P0485](#p0485-question-asking) | `question_asking` | Clarification & Active Information Gathering | `cap.t10.question.question_asking@1` |
| [P0486](#p0486-reasoning-faithfulness) | `reasoning_faithfulness` | Reasoning Faithfulness Verification | `cap.t10.reasoning.reasoning_faithfulness@1` |
| [P0487](#p0487-reasoning-robustness) | `reasoning_robustness` | Reasoning Robustness to Perturbation | `cap.t10.reasoning.reasoning_robustness@1` |
| [P0488](#p0488-multi-step-arithmetic) | `multi_step_arithmetic` | Long Multi-Step Derivation Engine | `cap.t10.multi.multi_step_arithmetic@1` |
| [P0489](#p0489-proof-sketch) | `proof_sketch` | Proof Sketch Generation & Refinement | `cap.t10.proof.proof_sketch@1` |
| [P0490](#p0490-reasoning-search-bench) | `reasoning_search_bench` | Reasoning Benchmark Harness | `cap.t10.reasoning.reasoning_search_bench@1` |
| [P0491](#p0491-reasoning-cost-model) | `reasoning_cost_model` | Value of Computation Model | `cap.t10.reasoning.reasoning_cost_model@1` |
| [P0492](#p0492-scratchpad-manager) | `scratchpad_manager` | Scratchpad & Working Memory Manager | `cap.t10.scratchpad.scratchpad_manager@1` |
| [P0493](#p0493-subgoal-caching) | `subgoal_caching` | Subgoal Solution Caching | `cap.t10.subgoal.subgoal_caching@1` |
| [P0494](#p0494-reasoning-transfer) | `reasoning_transfer` | Cross-Domain Reasoning Transfer | `cap.t10.reasoning.reasoning_transfer@1` |
| [P0495](#p0495-error-taxonomy) | `error_taxonomy` | Reasoning Error Taxonomy & Diagnosis | `cap.t10.error.error_taxonomy@1` |
| [P0496](#p0496-adversarial-reasoning) | `adversarial_reasoning` | Adversarial Reasoning Stress Tests | `cap.t10.adversarial.adversarial_reasoning@1` |
| [P0497](#p0497-reasoning-interpretability) | `reasoning_interpretability` | Reasoning Introspection & Explanation | `cap.t10.reasoning.reasoning_interpretability@1` |
| [P0498](#p0498-collective-reasoning) | `collective_reasoning` | Multi-Instance Collective Reasoning | `cap.t10.collective.collective_reasoning@1` |
| [P0499](#p0499-reasoning-speed-proof) | `reasoning_speed_proof` | S5 Speedup Proof & Attribution | `cap.t10.reasoning.reasoning_speed_proof@1` |
| [P0500](#p0500-reasoning-spec-doc) | `reasoning_spec_doc` | Reasoning Subsystem Specification | `cap.t10.reasoning.reasoning_spec_doc@1` |

---

### P0451 · `thought_program_ir` — Thought Program Representation

| field | value |
|---|---|
| part id | `P0451` (1/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0451_thought_program_ir.py` |
| module path | `hyperion.t10.reasoning.thought_program_ir` |
| capability published | `cap.t10.thought.thought_program_ir@1` |
| determinism class | `seeded` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0451_thought_program_ir.txt`](prompts/P0451_thought_program_ir.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0451-thought-program-ir) |

**Mission.** Reasoning as an explicit, inspectable, executable program rather than free text.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **typed thought-step IR: assume, derive, verify, retrieve, compute, branch, conclude** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **dependency graph over steps enabling parallel evaluation and pruning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **serialisation for caching, replay and audit**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **equivalence checking between thought programs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.thought.thought_program_ir@1`
- `cap.t10.thought.thought_program_ir.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t05.causal.causal_model@1` | use the in-file conservative substitute for `causal_model` (documented, slower, lower quality) and set `degraded['causal_model']='local'` |
| `cap.t07.freshness.freshness_manager@1` | use the in-file conservative substitute for `freshness_manager` (documented, slower, lower quality) and set `degraded['freshness_manager']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - typed thought-step IR: assume, derive, verify, retrieve, compute | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dependency graph over steps enabling parallel evaluation and pru | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - serialisation for caching, replay and audit | 520 | Third required mechanism. |
| 6 | Core implementation D - equivalence checking between thought programs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0451_thought_program_ir.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.thought.thought_program_ir@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 31000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0452 · `search_controller` — Deliberation Search Controller

| field | value |
|---|---|
| part id | `P0452` (2/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0452_search_controller.py` |
| module path | `hyperion.t10.reasoning.search_controller` |
| capability published | `cap.t10.search.search_controller@1` |
| determinism class | `seeded` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0452_search_controller.txt`](prompts/P0452_search_controller.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0452-search-controller) |

**Mission.** Decides how much to think, how to think, and when to stop.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **policy over search strategies (linear, tree, graph, iterative refinement)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **budget allocation from difficulty estimates and value-of-computation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **anytime behaviour returning the best answer so far** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured accuracy-per-token versus unguided long chains** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.search.search_controller@1`
- `cap.t10.search.search_controller.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.thought.thought_program_ir@1` | use the in-file conservative substitute for `thought_program_ir` (documented, slower, lower quality) and set `degraded['thought_program_ir']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t05.distillation.distillation_arch@1` | use the in-file conservative substitute for `distillation_arch` (documented, slower, lower quality) and set `degraded['distillation_arch']='local'` |
| `cap.t07.attention.attention_sink@1` | use the in-file conservative substitute for `attention_sink` (documented, slower, lower quality) and set `degraded['attention_sink']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - policy over search strategies (linear, tree, graph, iterative re | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - budget allocation from difficulty estimates and value-of-computa | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - anytime behaviour returning the best answer so far | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy-per-token versus unguided long chains | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0452_search_controller.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.search.search_controller@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 32000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0453 · `tree_search` — Tree Search over Reasoning States

| field | value |
|---|---|
| part id | `P0453` (3/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0453_tree_search.py` |
| module path | `hyperion.t10.reasoning.tree_search` |
| capability published | `cap.t10.tree.tree_search@1` |
| determinism class | `seeded` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0453_tree_search.txt`](prompts/P0453_tree_search.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0453-tree-search) |

**Mission.** MCTS-class search where the model is both policy and value.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **node expansion with policy-guided action sampling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **value backup with verifier-provided rewards** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **exploration constants tuned per task family** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured gain versus best-of-N at equal compute** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.tree.tree_search@1`
- `cap.t10.tree.tree_search.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.search.search_controller@1` | use the in-file conservative substitute for `search_controller` (documented, slower, lower quality) and set `degraded['search_controller']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t05.multimodal.multimodal_fusion_arch@1` | use the in-file conservative substitute for `multimodal_fusion_arch` (documented, slower, lower quality) and set `degraded['multimodal_fusion_arch']='local'` |
| `cap.t07.persistence.persistence_layer@1` | use the in-file conservative substitute for `persistence_layer` (documented, slower, lower quality) and set `degraded['persistence_layer']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - node expansion with policy-guided action sampling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - value backup with verifier-provided rewards | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - exploration constants tuned per task family | 520 | Third required mechanism. |
| 6 | Core implementation D - measured gain versus best-of-N at equal compute | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0453_tree_search.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.tree.tree_search@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 33000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0454 · `graph_search` — Graph-of-Thought Reasoning

| field | value |
|---|---|
| part id | `P0454` (4/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0454_graph_search.py` |
| module path | `hyperion.t10.reasoning.graph_search` |
| capability published | `cap.t10.graph.graph_search@1` |
| determinism class | `seeded` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0454_graph_search.txt`](prompts/P0454_graph_search.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0454-graph-search) |

**Mission.** Merges, splits and reuses reasoning paths instead of only branching.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **state merging via canonicalisation of equivalent partial solutions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **path aggregation with evidence combination** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cycle prevention and progress guarantees** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured efficiency gain from state merging**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.graph.graph_search@1`
- `cap.t10.graph.graph_search.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.tree.tree_search@1` | use the in-file conservative substitute for `tree_search` (documented, slower, lower quality) and set `degraded['tree_search']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t05.context.context_packing@1` | use the in-file conservative substitute for `context_packing` (documented, slower, lower quality) and set `degraded['context_packing']='local'` |
| `cap.t07.index.index_build_pipeline@1` | use the in-file conservative substitute for `index_build_pipeline` (documented, slower, lower quality) and set `degraded['index_build_pipeline']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - state merging via canonicalisation of equivalent partial solutio | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - path aggregation with evidence combination | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cycle prevention and progress guarantees | 520 | Third required mechanism. |
| 6 | Core implementation D - measured efficiency gain from state merging | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0454_graph_search.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.graph.graph_search@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 34000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0455 · `beam_pruning` — Verifier-Guided Beam Pruning

| field | value |
|---|---|
| part id | `P0455` (5/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0455_beam_pruning.py` |
| module path | `hyperion.t10.reasoning.beam_pruning` |
| capability published | `cap.t10.beam.beam_pruning@1` |
| determinism class | `seeded` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0455_beam_pruning.txt`](prompts/P0455_beam_pruning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0455-beam-pruning) |

**Mission.** Kills bad reasoning early: the core of the 2.2x S5 speedup.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **step-level verifier scoring with calibrated pruning thresholds** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **diversity preservation to avoid premature convergence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **compute-saving measurement at matched accuracy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **false-prune rate measurement and mitigation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.beam.beam_pruning@1`
- `cap.t10.beam.beam_pruning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.graph.graph_search@1` | use the in-file conservative substitute for `graph_search` (documented, slower, lower quality) and set `degraded['graph_search']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t05.capacity.capacity_probes@1` | use the in-file conservative substitute for `capacity_probes` (documented, slower, lower quality) and set `degraded['capacity_probes']='local'` |
| `cap.t07.cost.cost_aware_retrieval@1` | use the in-file conservative substitute for `cost_aware_retrieval` (documented, slower, lower quality) and set `degraded['cost_aware_retrieval']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - step-level verifier scoring with calibrated pruning thresholds | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - diversity preservation to avoid premature convergence | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - compute-saving measurement at matched accuracy | 520 | Third required mechanism. |
| 6 | Core implementation D - false-prune rate measurement and mitigation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0455_beam_pruning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.beam.beam_pruning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 35000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0456 · `process_verifier` — Process Reward Model & Step Verification

| field | value |
|---|---|
| part id | `P0456` (6/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0456_process_verifier.py` |
| module path | `hyperion.t10.reasoning.process_verifier` |
| capability published | `cap.t10.process.process_verifier@1` |
| determinism class | `seeded` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0456_process_verifier.txt`](prompts/P0456_process_verifier.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0456-process-verifier) |

**Mission.** Checks each reasoning step, not just the final answer.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **step-correctness scoring with calibration and abstention** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **training from automatically-labelled step data**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **generalisation across domains measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **correlation between step scores and final correctness** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.process.process_verifier@1`
- `cap.t10.process.process_verifier.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.beam.beam_pruning@1` | use the in-file conservative substitute for `beam_pruning` (documented, slower, lower quality) and set `degraded['beam_pruning']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t05.recurrent.recurrent_memory_layer@1` | use the in-file conservative substitute for `recurrent_memory_layer` (documented, slower, lower quality) and set `degraded['recurrent_memory_layer']='local'` |
| `cap.t07.context.context_window_manager@1` | use the in-file conservative substitute for `context_window_manager` (documented, slower, lower quality) and set `degraded['context_window_manager']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - step-correctness scoring with calibration and abstention | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - training from automatically-labelled step data | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - generalisation across domains measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - correlation between step scores and final correctness | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0456_process_verifier.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.process.process_verifier@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 36000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0457 · `outcome_verifier` — Outcome Verification & Answer Checking

| field | value |
|---|---|
| part id | `P0457` (7/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0457_outcome_verifier.py` |
| module path | `hyperion.t10.reasoning.outcome_verifier` |
| capability published | `cap.t10.outcome.outcome_verifier@1` |
| determinism class | `seeded` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0457_outcome_verifier.txt`](prompts/P0457_outcome_verifier.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0457-outcome-verifier) |

**Mission.** Independent confirmation that the final answer is right.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **domain-specific checkers (execution, unit test, symbolic, numeric, citation)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **verification-strength classification (proof, test, heuristic, none)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **escalation policy when verification is unavailable** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured error-rate reduction attributable to verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.outcome.outcome_verifier@1`
- `cap.t10.outcome.outcome_verifier.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.process.process_verifier@1` | use the in-file conservative substitute for `process_verifier` (documented, slower, lower quality) and set `degraded['process_verifier']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t05.byte.byte_latent_patching@1` | use the in-file conservative substitute for `byte_latent_patching` (documented, slower, lower quality) and set `degraded['byte_latent_patching']='local'` |
| `cap.t07.vector.vector_index@1` | use the in-file conservative substitute for `vector_index` (documented, slower, lower quality) and set `degraded['vector_index']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - domain-specific checkers (execution, unit test, symbolic, numeri | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - verification-strength classification (proof, test, heuristic, no | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - escalation policy when verification is unavailable | 520 | Third required mechanism. |
| 6 | Core implementation D - measured error-rate reduction attributable to verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0457_outcome_verifier.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.outcome.outcome_verifier@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 37000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0458 · `self_consistency` — Self-Consistency & Sample Aggregation

| field | value |
|---|---|
| part id | `P0458` (8/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0458_self_consistency.py` |
| module path | `hyperion.t10.reasoning.self_consistency` |
| capability published | `cap.t10.self.self_consistency@1` |
| determinism class | `seeded` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0458_self_consistency.txt`](prompts/P0458_self_consistency.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0458-self-consistency) |

**Mission.** Many independent attempts, one reliable answer.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **answer-equivalence clustering including semantic equivalence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **verifier-weighted voting instead of naive majority** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **adaptive sample count from agreement statistics** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **cost-versus-accuracy curves per task family**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.self.self_consistency@1`
- `cap.t10.self.self_consistency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.outcome.outcome_verifier@1` | use the in-file conservative substitute for `outcome_verifier` (documented, slower, lower quality) and set `degraded['outcome_verifier']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t05.world.world_model_core@1` | use the in-file conservative substitute for `world_model_core` (documented, slower, lower quality) and set `degraded['world_model_core']='local'` |
| `cap.t07.citation.citation_grounding@1` | use the in-file conservative substitute for `citation_grounding` (documented, slower, lower quality) and set `degraded['citation_grounding']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - answer-equivalence clustering including semantic equivalence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - verifier-weighted voting instead of naive majority | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - adaptive sample count from agreement statistics | 520 | Third required mechanism. |
| 6 | Core implementation D - cost-versus-accuracy curves per task family | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0458_self_consistency.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.self.self_consistency@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 38000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0459 · `self_critique` — Self-Critique & Revision Loop

| field | value |
|---|---|
| part id | `P0459` (9/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0459_self_critique.py` |
| module path | `hyperion.t10.reasoning.self_critique` |
| capability published | `cap.t10.self.self_critique@1` |
| determinism class | `seeded` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0459_self_critique.txt`](prompts/P0459_self_critique.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0459-self-critique) |

**Mission.** Finds its own mistakes and fixes them without human help.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **structured critique generation targeting specific failure modes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **revision application with regression prevention** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **convergence guarantees and oscillation detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured improvement per revision round with diminishing-returns analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.self.self_critique@1`
- `cap.t10.self.self_critique.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.self.self_consistency@1` | use the in-file conservative substitute for `self_consistency` (documented, slower, lower quality) and set `degraded['self_consistency']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t05.model.model_merging@1` | use the in-file conservative substitute for `model_merging` (documented, slower, lower quality) and set `degraded['model_merging']='local'` |
| `cap.t07.memory.memory_compression_learned@1` | use the in-file conservative substitute for `memory_compression_learned` (documented, slower, lower quality) and set `degraded['memory_compression_learned']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structured critique generation targeting specific failure modes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - revision application with regression prevention | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - convergence guarantees and oscillation detection | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement per revision round with diminishing-returns | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0459_self_critique.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.self.self_critique@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 39000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0460 · `debate_ensemble` — Multi-Perspective Debate & Adversarial Review

| field | value |
|---|---|
| part id | `P0460` (10/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0460_debate_ensemble.py` |
| module path | `hyperion.t10.reasoning.debate_ensemble` |
| capability published | `cap.t10.debate.debate_ensemble@1` |
| determinism class | `seeded` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0460_debate_ensemble.txt`](prompts/P0460_debate_ensemble.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0460-debate-ensemble) |

**Mission.** Two internal reasoners argue; the strongest evidence wins.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **role-conditioned reasoners with genuine perspective diversity** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **structured argumentation with claim-evidence-rebuttal tracking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **judge model with calibrated resolution** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured accuracy gain on contested and ambiguous questions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.debate.debate_ensemble@1`
- `cap.t10.debate.debate_ensemble.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.self.self_critique@1` | use the in-file conservative substitute for `self_critique` (documented, slower, lower quality) and set `degraded['self_critique']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t05.logit.logit_head_design@1` | use the in-file conservative substitute for `logit_head_design` (documented, slower, lower quality) and set `degraded['logit_head_design']='local'` |
| `cap.t07.memory.memory_gc@1` | use the in-file conservative substitute for `memory_gc` (documented, slower, lower quality) and set `degraded['memory_gc']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - role-conditioned reasoners with genuine perspective diversity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - structured argumentation with claim-evidence-rebuttal tracking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - judge model with calibrated resolution | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy gain on contested and ambiguous questions | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0460_debate_ensemble.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.debate.debate_ensemble@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 40000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0461 · `decomposition` — Problem Decomposition Engine

| field | value |
|---|---|
| part id | `P0461` (11/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0461_decomposition.py` |
| module path | `hyperion.t10.reasoning.decomposition` |
| capability published | `cap.t10.decomposition.decomposition@1` |
| determinism class | `seeded` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0461_decomposition.txt`](prompts/P0461_decomposition.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0461-decomposition) |

**Mission.** Breaks hard problems into provably sufficient sub-problems.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **decomposition-strategy library with applicability conditions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sufficiency checking (do the parts imply the whole)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **dependency-ordered subproblem scheduling for parallel solving** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured solve-rate improvement on multi-step problems** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.decomposition.decomposition@1`
- `cap.t10.decomposition.decomposition.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.debate.debate_ensemble@1` | use the in-file conservative substitute for `debate_ensemble` (documented, slower, lower quality) and set `degraded['debate_ensemble']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t05.numerical.numerical_arch_stability@1` | use the in-file conservative substitute for `numerical_arch_stability` (documented, slower, lower quality) and set `degraded['numerical_arch_stability']='local'` |
| `cap.t07.memory.memory_audit@1` | use the in-file conservative substitute for `memory_audit` (documented, slower, lower quality) and set `degraded['memory_audit']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - decomposition-strategy library with applicability conditions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sufficiency checking (do the parts imply the whole) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - dependency-ordered subproblem scheduling for parallel solving | 520 | Third required mechanism. |
| 6 | Core implementation D - measured solve-rate improvement on multi-step problems | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0461_decomposition.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.decomposition.decomposition@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 41000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0462 · `planning_engine` — Hierarchical Planning Engine

| field | value |
|---|---|
| part id | `P0462` (12/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0462_planning_engine.py` |
| module path | `hyperion.t10.reasoning.planning_engine` |
| capability published | `cap.t10.planning.planning_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0462_planning_engine.txt`](prompts/P0462_planning_engine.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0462-planning-engine) |

**Mission.** Long-horizon plans that survive contact with reality.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **HTN-style hierarchical planning with abstraction levels** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **precondition/effect reasoning over the world model** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **plan repair on execution failure rather than full replan** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **plan-success-rate measurement on long-horizon benchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.planning.planning_engine@1`
- `cap.t10.planning.planning_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.decomposition.decomposition@1` | use the in-file conservative substitute for `decomposition` (documented, slower, lower quality) and set `degraded['decomposition']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t05.arch.arch_ablation_suite@1` | use the in-file conservative substitute for `arch_ablation_suite` (documented, slower, lower quality) and set `degraded['arch_ablation_suite']='local'` |
| `cap.t07.streaming.streaming_ingest@1` | use the in-file conservative substitute for `streaming_ingest` (documented, slower, lower quality) and set `degraded['streaming_ingest']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - HTN-style hierarchical planning with abstraction levels | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - precondition/effect reasoning over the world model | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - plan repair on execution failure rather than full replan | 520 | Third required mechanism. |
| 6 | Core implementation D - plan-success-rate measurement on long-horizon benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0462_planning_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.planning.planning_engine@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 42000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0463 · `goal_management` — Goal Stack & Intent Tracking

| field | value |
|---|---|
| part id | `P0463` (13/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0463_goal_management.py` |
| module path | `hyperion.t10.reasoning.goal_management` |
| capability published | `cap.t10.goal.goal_management@1` |
| determinism class | `seeded` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0463_goal_management.txt`](prompts/P0463_goal_management.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0463-goal-management) |

**Mission.** Never loses sight of what the user actually asked for.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **explicit goal stack with priorities, constraints and success criteria** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **drift detection comparing current work against the original intent** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **goal-conflict detection and clarification triggering**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured reduction in off-target work on long tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.goal.goal_management@1`
- `cap.t10.goal.goal_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.planning.planning_engine@1` | use the in-file conservative substitute for `planning_engine` (documented, slower, lower quality) and set `degraded['planning_engine']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t05.state.state_space_layer@1` | use the in-file conservative substitute for `state_space_layer` (documented, slower, lower quality) and set `degraded['state_space_layer']='local'` |
| `cap.t07.kv.kv_compression_runtime@1` | use the in-file conservative substitute for `kv_compression_runtime` (documented, slower, lower quality) and set `degraded['kv_compression_runtime']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - explicit goal stack with priorities, constraints and success cri | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - drift detection comparing current work against the original inte | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - goal-conflict detection and clarification triggering | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction in off-target work on long tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0463_goal_management.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.goal.goal_management@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 43000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0464 · `constraint_reasoning` — Constraint Satisfaction & Optimisation Reasoning

| field | value |
|---|---|
| part id | `P0464` (14/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0464_constraint_reasoning.py` |
| module path | `hyperion.t10.reasoning.constraint_reasoning` |
| capability published | `cap.t10.constraint.constraint_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0464_constraint_reasoning.txt`](prompts/P0464_constraint_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0464-constraint-reasoning) |

**Mission.** Handles hard requirements exactly, not approximately.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **constraint extraction from natural language into a formal model** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **solver dispatch (CP/SAT/LP/MILP) with encoding selection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **infeasibility explanation and minimal-conflict extraction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement on constrained-planning benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.constraint.constraint_reasoning@1`
- `cap.t10.constraint.constraint_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.goal.goal_management@1` | use the in-file conservative substitute for `goal_management` (documented, slower, lower quality) and set `degraded['goal_management']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t05.tokeniser.tokeniser_omega@1` | use the in-file conservative substitute for `tokeniser_omega` (documented, slower, lower quality) and set `degraded['tokeniser_omega']='local'` |
| `cap.t07.forgetting.forgetting_policy@1` | use the in-file conservative substitute for `forgetting_policy` (documented, slower, lower quality) and set `degraded['forgetting_policy']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - constraint extraction from natural language into a formal model | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - solver dispatch (CP/SAT/LP/MILP) with encoding selection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - infeasibility explanation and minimal-conflict extraction | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on constrained-planning benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0464_constraint_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.constraint.constraint_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 44000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0465 · `analogy_engine` — Analogical & Case-Based Reasoning

| field | value |
|---|---|
| part id | `P0465` (15/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0465_analogy_engine.py` |
| module path | `hyperion.t10.reasoning.analogy_engine` |
| capability published | `cap.t10.analogy.analogy_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0465_analogy_engine.txt`](prompts/P0465_analogy_engine.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0465-analogy-engine) |

**Mission.** Solves new problems by mapping them to solved ones.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **structural-mapping engine over relational representations**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **case retrieval by structural rather than surface similarity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **adaptation of retrieved solutions with verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured transfer performance on novel-domain tasks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.analogy.analogy_engine@1`
- `cap.t10.analogy.analogy_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.constraint.constraint_reasoning@1` | use the in-file conservative substitute for `constraint_reasoning` (documented, slower, lower quality) and set `degraded['constraint_reasoning']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t05.uncertainty.uncertainty_calibration@1` | use the in-file conservative substitute for `uncertainty_calibration` (documented, slower, lower quality) and set `degraded['uncertainty_calibration']='local'` |
| `cap.t07.reranker.reranker_model@1` | use the in-file conservative substitute for `reranker_model` (documented, slower, lower quality) and set `degraded['reranker_model']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structural-mapping engine over relational representations | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - case retrieval by structural rather than surface similarity | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - adaptation of retrieved solutions with verification | 520 | Third required mechanism. |
| 6 | Core implementation D - measured transfer performance on novel-domain tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0465_analogy_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.analogy.analogy_engine@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 45000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0466 · `abstraction_engine` — Abstraction Discovery & Concept Formation

| field | value |
|---|---|
| part id | `P0466` (16/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0466_abstraction_engine.py` |
| module path | `hyperion.t10.reasoning.abstraction_engine` |
| capability published | `cap.t10.abstraction.abstraction_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0466_abstraction_engine.txt`](prompts/P0466_abstraction_engine.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0466-abstraction-engine) |

**Mission.** Invents the right concept for the problem: the ARC-AGI-3 core.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **compression-driven abstraction discovery over solved examples** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **concept library with reuse tracking and refactoring** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **concept naming and human-inspectable descriptions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target contribution to 88% ARC-AGI-3 versus Opus 5's 30.2%**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.abstraction.abstraction_engine@1`
- `cap.t10.abstraction.abstraction_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.analogy.analogy_engine@1` | use the in-file conservative substitute for `analogy_engine` (documented, slower, lower quality) and set `degraded['analogy_engine']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t05.knowledge.knowledge_editing@1` | use the in-file conservative substitute for `knowledge_editing` (documented, slower, lower quality) and set `degraded['knowledge_editing']='local'` |
| `cap.t07.belief.belief_revision@1` | use the in-file conservative substitute for `belief_revision` (documented, slower, lower quality) and set `degraded['belief_revision']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - compression-driven abstraction discovery over solved examples | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - concept library with reuse tracking and refactoring | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - concept naming and human-inspectable descriptions | 520 | Third required mechanism. |
| 6 | Core implementation D - target contribution to 88% ARC-AGI-3 versus Opus 5's 30.2% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0466_abstraction_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.abstraction.abstraction_engine@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 46000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0467 · `induction_engine` — Rule Induction from Few Examples

| field | value |
|---|---|
| part id | `P0467` (17/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0467_induction_engine.py` |
| module path | `hyperion.t10.reasoning.induction_engine` |
| capability published | `cap.t10.induction.induction_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0467_induction_engine.txt`](prompts/P0467_induction_engine.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0467-induction-engine) |

**Mission.** Infers the underlying rule from two or three demonstrations.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **hypothesis-space enumeration with Occam-style priors** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **consistency checking against all given examples** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **active-query generation to disambiguate hypotheses**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **sample-efficiency measurement versus baselines** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.induction.induction_engine@1`
- `cap.t10.induction.induction_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.abstraction.abstraction_engine@1` | use the in-file conservative substitute for `abstraction_engine` (documented, slower, lower quality) and set `degraded['abstraction_engine']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t05.residual.residual_stream_design@1` | use the in-file conservative substitute for `residual_stream_design` (documented, slower, lower quality) and set `degraded['residual_stream_design']='local'` |
| `cap.t07.retrieval.retrieval_cache@1` | use the in-file conservative substitute for `retrieval_cache` (documented, slower, lower quality) and set `degraded['retrieval_cache']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hypothesis-space enumeration with Occam-style priors | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - consistency checking against all given examples | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - active-query generation to disambiguate hypotheses | 520 | Third required mechanism. |
| 6 | Core implementation D - sample-efficiency measurement versus baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0467_induction_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.induction.induction_engine@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 47000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0468 · `program_synthesis_reasoning` — Neural-Guided Program Synthesis

| field | value |
|---|---|
| part id | `P0468` (18/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0468_program_synthesis_reasoning.py` |
| module path | `hyperion.t10.reasoning.program_synthesis_reasoning` |
| capability published | `cap.t10.program.program_synthesis_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0468_program_synthesis_reasoning.txt`](prompts/P0468_program_synthesis_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0468-program-synthesis-reasoning) |

**Mission.** Writes the program that solves the puzzle instead of guessing the output.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **DSL-based enumerative search with learned guidance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **type-directed and constraint-directed pruning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **synthesis-time budget control with anytime results** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **solve-rate and synthesis-time measurement on puzzle suites** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.program.program_synthesis_reasoning@1`
- `cap.t10.program.program_synthesis_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.induction.induction_engine@1` | use the in-file conservative substitute for `induction_engine` (documented, slower, lower quality) and set `degraded['induction_engine']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t05.model.model_surgery@1` | use the in-file conservative substitute for `model_surgery` (documented, slower, lower quality) and set `degraded['model_surgery']='local'` |
| `cap.t07.user.user_model@1` | use the in-file conservative substitute for `user_model` (documented, slower, lower quality) and set `degraded['user_model']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - DSL-based enumerative search with learned guidance | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - type-directed and constraint-directed pruning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - synthesis-time budget control with anytime results | 520 | Third required mechanism. |
| 6 | Core implementation D - solve-rate and synthesis-time measurement on puzzle suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0468_program_synthesis_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.program.program_synthesis_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 48000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0469 · `counterfactual_reasoning` — Counterfactual & Hypothetical Reasoning

| field | value |
|---|---|
| part id | `P0469` (19/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0469_counterfactual_reasoning.py` |
| module path | `hyperion.t10.reasoning.counterfactual_reasoning` |
| capability published | `cap.t10.counterfactual.counterfactual_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0469_counterfactual_reasoning.txt`](prompts/P0469_counterfactual_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0469-counterfactual-reasoning) |

**Mission.** Reasons about what would happen, reliably.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **intervention semantics over the causal world model**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **hypothetical-state isolation preventing belief contamination** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **consistency checking across counterfactual branches** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on counterfactual benchmark suites** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.counterfactual.counterfactual_reasoning@1`
- `cap.t10.counterfactual.counterfactual_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.program.program_synthesis_reasoning@1` | use the in-file conservative substitute for `program_synthesis_reasoning` (documented, slower, lower quality) and set `degraded['program_synthesis_reasoning']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t05.reference.reference_forward@1` | use the in-file conservative substitute for `reference_forward` (documented, slower, lower quality) and set `degraded['reference_forward']='local'` |
| `cap.t07.memory.memory_sharding@1` | use the in-file conservative substitute for `memory_sharding` (documented, slower, lower quality) and set `degraded['memory_sharding']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - intervention semantics over the causal world model | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hypothetical-state isolation preventing belief contamination | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - consistency checking across counterfactual branches | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on counterfactual benchmark suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0469_counterfactual_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.counterfactual.counterfactual_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 49000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0470 · `probabilistic_reasoning` — Probabilistic Inference Engine

| field | value |
|---|---|
| part id | `P0470` (20/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0470_probabilistic_reasoning.py` |
| module path | `hyperion.t10.reasoning.probabilistic_reasoning` |
| capability published | `cap.t10.probabilistic.probabilistic_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0470_probabilistic_reasoning.txt`](prompts/P0470_probabilistic_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0470-probabilistic-reasoning) |

**Mission.** Correct arithmetic on uncertainty, not vibes.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **graphical-model construction from context and exact/approximate inference** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **Bayesian updating with explicit priors and likelihoods** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **Monte Carlo methods with convergence diagnostics** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **calibration measurement on probabilistic question sets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.probabilistic.probabilistic_reasoning@1`
- `cap.t10.probabilistic.probabilistic_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.counterfactual.counterfactual_reasoning@1` | use the in-file conservative substitute for `counterfactual_reasoning` (documented, slower, lower quality) and set `degraded['counterfactual_reasoning']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t05.kv.kv_compression_model@1` | use the in-file conservative substitute for `kv_compression_model` (documented, slower, lower quality) and set `degraded['kv_compression_model']='local'` |
| `cap.t07.kv.kv_dedup@1` | use the in-file conservative substitute for `kv_dedup` (documented, slower, lower quality) and set `degraded['kv_dedup']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - graphical-model construction from context and exact/approximate  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - Bayesian updating with explicit priors and likelihoods | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - Monte Carlo methods with convergence diagnostics | 520 | Third required mechanism. |
| 6 | Core implementation D - calibration measurement on probabilistic question sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0470_probabilistic_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.probabilistic.probabilistic_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 3000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0471 · `numeric_reasoning` — Exact Numeric & Quantitative Reasoning

| field | value |
|---|---|
| part id | `P0471` (21/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0471_numeric_reasoning.py` |
| module path | `hyperion.t10.reasoning.numeric_reasoning` |
| capability published | `cap.t10.numeric.numeric_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0471_numeric_reasoning.txt`](prompts/P0471_numeric_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0471-numeric-reasoning) |

**Mission.** Never makes an arithmetic mistake.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **computation offloading to exact evaluators with unit checking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **magnitude sanity checking and dimensional analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **error-propagation tracking through multi-step calculations**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: zero arithmetic errors on the quantitative benchmark suite** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.numeric.numeric_reasoning@1`
- `cap.t10.numeric.numeric_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.probabilistic.probabilistic_reasoning@1` | use the in-file conservative substitute for `probabilistic_reasoning` (documented, slower, lower quality) and set `degraded['probabilistic_reasoning']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t05.embedding.embedding_design@1` | use the in-file conservative substitute for `embedding_design` (documented, slower, lower quality) and set `degraded['embedding_design']='local'` |
| `cap.t07.memory.memory_consolidation@1` | use the in-file conservative substitute for `memory_consolidation` (documented, slower, lower quality) and set `degraded['memory_consolidation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - computation offloading to exact evaluators with unit checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - magnitude sanity checking and dimensional analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - error-propagation tracking through multi-step calculations | 520 | Third required mechanism. |
| 6 | Core implementation D - target: zero arithmetic errors on the quantitative benchmark sui | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0471_numeric_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.numeric.numeric_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 4000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0472 · `temporal_reasoning` — Temporal & Scheduling Reasoning

| field | value |
|---|---|
| part id | `P0472` (22/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0472_temporal_reasoning.py` |
| module path | `hyperion.t10.reasoning.temporal_reasoning` |
| capability published | `cap.t10.temporal.temporal_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0472_temporal_reasoning.txt`](prompts/P0472_temporal_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0472-temporal-reasoning) |

**Mission.** Handles time, duration, order and deadlines correctly.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **interval algebra with constraint propagation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **timezone, calendar and duration arithmetic correctness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **schedule feasibility checking and conflict explanation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on temporal reasoning and scheduling benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.temporal.temporal_reasoning@1`
- `cap.t10.temporal.temporal_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.numeric.numeric_reasoning@1` | use the in-file conservative substitute for `numeric_reasoning` (documented, slower, lower quality) and set `degraded['numeric_reasoning']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t05.verifier.verifier_head@1` | use the in-file conservative substitute for `verifier_head` (documented, slower, lower quality) and set `degraded['verifier_head']='local'` |
| `cap.t07.embedding.embedding_model@1` | use the in-file conservative substitute for `embedding_model` (documented, slower, lower quality) and set `degraded['embedding_model']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - interval algebra with constraint propagation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - timezone, calendar and duration arithmetic correctness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - schedule feasibility checking and conflict explanation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on temporal reasoning and scheduling benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0472_temporal_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.temporal.temporal_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 5000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0473 · `spatial_reasoning` — Spatial & Geometric Reasoning

| field | value |
|---|---|
| part id | `P0473` (23/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0473_spatial_reasoning.py` |
| module path | `hyperion.t10.reasoning.spatial_reasoning` |
| capability published | `cap.t10.spatial.spatial_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0473_spatial_reasoning.txt`](prompts/P0473_spatial_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0473-spatial-reasoning) |

**Mission.** Reasons about shape, position and physical arrangement.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **qualitative spatial calculus plus exact geometric computation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **mental-rotation and transformation reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **3D scene consistency checking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on spatial reasoning benchmark suites** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.spatial.spatial_reasoning@1`
- `cap.t10.spatial.spatial_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.temporal.temporal_reasoning@1` | use the in-file conservative substitute for `temporal_reasoning` (documented, slower, lower quality) and set `degraded['temporal_reasoning']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t05.continual.continual_learning@1` | use the in-file conservative substitute for `continual_learning` (documented, slower, lower quality) and set `degraded['continual_learning']='local'` |
| `cap.t07.world.world_state_store@1` | use the in-file conservative substitute for `world_state_store` (documented, slower, lower quality) and set `degraded['world_state_store']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - qualitative spatial calculus plus exact geometric computation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mental-rotation and transformation reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - 3D scene consistency checking | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on spatial reasoning benchmark suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0473_spatial_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.spatial.spatial_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 6000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0474 · `commonsense_engine` — Commonsense Reasoning & Default Inference

| field | value |
|---|---|
| part id | `P0474` (24/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0474_commonsense_engine.py` |
| module path | `hyperion.t10.reasoning.commonsense_engine` |
| capability published | `cap.t10.commonsense.commonsense_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0474_commonsense_engine.txt`](prompts/P0474_commonsense_engine.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0474-commonsense-engine) |

**Mission.** Knows what everybody knows, and when defaults break.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **default-inference rules with defeasibility** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **physical, social and temporal commonsense knowledge integration** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **exception detection when defaults do not apply** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on commonsense benchmark suites**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.commonsense.commonsense_engine@1`
- `cap.t10.commonsense.commonsense_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.spatial.spatial_reasoning@1` | use the in-file conservative substitute for `spatial_reasoning` (documented, slower, lower quality) and set `degraded['spatial_reasoning']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t05.depth.depth_width_tradeoff@1` | use the in-file conservative substitute for `depth_width_tradeoff` (documented, slower, lower quality) and set `degraded['depth_width_tradeoff']='local'` |
| `cap.t07.subgraph.subgraph_memoize@1` | use the in-file conservative substitute for `subgraph_memoize` (documented, slower, lower quality) and set `degraded['subgraph_memoize']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - default-inference rules with defeasibility | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - physical, social and temporal commonsense knowledge integration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - exception detection when defaults do not apply | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on commonsense benchmark suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0474_commonsense_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.commonsense.commonsense_engine@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 7000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0475 · `meta_reasoning` — Meta-Reasoning & Strategy Selection

| field | value |
|---|---|
| part id | `P0475` (25/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0475_meta_reasoning.py` |
| module path | `hyperion.t10.reasoning.meta_reasoning` |
| capability published | `cap.t10.meta.meta_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0475_meta_reasoning.txt`](prompts/P0475_meta_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0475-meta-reasoning) |

**Mission.** Thinks about how to think, and adapts mid-problem.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **strategy-performance modelling per problem signature** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **mid-solution strategy switching on stagnation detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **value-of-computation estimation for each candidate strategy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured improvement over fixed-strategy reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.meta.meta_reasoning@1`
- `cap.t10.meta.meta_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.commonsense.commonsense_engine@1` | use the in-file conservative substitute for `commonsense_engine` (documented, slower, lower quality) and set `degraded['commonsense_engine']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t05.sparse.sparse_upcycling@1` | use the in-file conservative substitute for `sparse_upcycling` (documented, slower, lower quality) and set `degraded['sparse_upcycling']='local'` |
| `cap.t07.multimodal.multimodal_memory@1` | use the in-file conservative substitute for `multimodal_memory` (documented, slower, lower quality) and set `degraded['multimodal_memory']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - strategy-performance modelling per problem signature | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mid-solution strategy switching on stagnation detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - value-of-computation estimation for each candidate strategy | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement over fixed-strategy reasoning | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0475_meta_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.meta.meta_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 8000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0476 · `difficulty_estimation` — Problem Difficulty Estimation

| field | value |
|---|---|
| part id | `P0476` (26/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0476_difficulty_estimation.py` |
| module path | `hyperion.t10.reasoning.difficulty_estimation` |
| capability published | `cap.t10.difficulty.difficulty_estimation@1` |
| determinism class | `seeded` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0476_difficulty_estimation.txt`](prompts/P0476_difficulty_estimation.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0476-difficulty-estimation) |

**Mission.** Knows how hard something is before spending on it.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **difficulty prediction from problem features and early reasoning signals** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **calibration against measured solve rates**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **budget recommendation from predicted difficulty** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **prediction-accuracy measurement across domains** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.difficulty.difficulty_estimation@1`
- `cap.t10.difficulty.difficulty_estimation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.meta.meta_reasoning@1` | use the in-file conservative substitute for `meta_reasoning` (documented, slower, lower quality) and set `degraded['meta_reasoning']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t05.model.model_config_schema@1` | use the in-file conservative substitute for `model_config_schema` (documented, slower, lower quality) and set `degraded['model_config_schema']='local'` |
| `cap.t07.context.context_budget_optimiser@1` | use the in-file conservative substitute for `context_budget_optimiser` (documented, slower, lower quality) and set `degraded['context_budget_optimiser']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - difficulty prediction from problem features and early reasoning  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - calibration against measured solve rates | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - budget recommendation from predicted difficulty | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction-accuracy measurement across domains | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0476_difficulty_estimation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.difficulty.difficulty_estimation@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 9000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0477 · `stopping_rules` — Optimal Stopping & Confidence Thresholds

| field | value |
|---|---|
| part id | `P0477` (27/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0477_stopping_rules.py` |
| module path | `hyperion.t10.reasoning.stopping_rules` |
| capability published | `cap.t10.stopping.stopping_rules@1` |
| determinism class | `seeded` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0477_stopping_rules.txt`](prompts/P0477_stopping_rules.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0477-stopping-rules) |

**Mission.** Stops thinking at the mathematically right moment.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **sequential-analysis stopping rules with error guarantees**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **marginal-value-of-thinking estimation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **task-class-specific threshold calibration** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured compute saving at matched accuracy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.stopping.stopping_rules@1`
- `cap.t10.stopping.stopping_rules.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.difficulty.difficulty_estimation@1` | use the in-file conservative substitute for `difficulty_estimation` (documented, slower, lower quality) and set `degraded['difficulty_estimation']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t05.attention.attention_variants@1` | use the in-file conservative substitute for `attention_variants` (documented, slower, lower quality) and set `degraded['attention_variants']='local'` |
| `cap.t07.kv.kv_eviction@1` | use the in-file conservative substitute for `kv_eviction` (documented, slower, lower quality) and set `degraded['kv_eviction']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sequential-analysis stopping rules with error guarantees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - marginal-value-of-thinking estimation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - task-class-specific threshold calibration | 520 | Third required mechanism. |
| 6 | Core implementation D - measured compute saving at matched accuracy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0477_stopping_rules.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.stopping.stopping_rules@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 10000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0478 · `backtracking` — Backtracking & Dead-End Recovery

| field | value |
|---|---|
| part id | `P0478` (28/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0478_backtracking.py` |
| module path | `hyperion.t10.reasoning.backtracking` |
| capability published | `cap.t10.backtracking.backtracking@1` |
| determinism class | `seeded` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0478_backtracking.txt`](prompts/P0478_backtracking.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0478-backtracking) |

**Mission.** Recognises a dead end and returns to the last good decision.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **decision-point checkpointing with cheap state restoration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **dead-end detection signals and confidence in them** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **learned no-good constraints preventing repeat failures** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured recovery rate on trap-containing problems**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.backtracking.backtracking@1`
- `cap.t10.backtracking.backtracking.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.stopping.stopping_rules@1` | use the in-file conservative substitute for `stopping_rules` (documented, slower, lower quality) and set `degraded['stopping_rules']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t05.activation.activation_design@1` | use the in-file conservative substitute for `activation_design` (documented, slower, lower quality) and set `degraded['activation_design']='local'` |
| `cap.t07.procedural.procedural_memory@1` | use the in-file conservative substitute for `procedural_memory` (documented, slower, lower quality) and set `degraded['procedural_memory']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - decision-point checkpointing with cheap state restoration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dead-end detection signals and confidence in them | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - learned no-good constraints preventing repeat failures | 520 | Third required mechanism. |
| 6 | Core implementation D - measured recovery rate on trap-containing problems | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0478_backtracking.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.backtracking.backtracking@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 11000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0479 · `reasoning_memory` — Reasoning Trace Memory & Lesson Extraction

| field | value |
|---|---|
| part id | `P0479` (29/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0479_reasoning_memory.py` |
| module path | `hyperion.t10.reasoning.reasoning_memory` |
| capability published | `cap.t10.reasoning.reasoning_memory@1` |
| determinism class | `seeded` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0479_reasoning_memory.txt`](prompts/P0479_reasoning_memory.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0479-reasoning-memory) |

**Mission.** Learns from its own past reasoning, successes and failures.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **trace storage with outcome labelling and indexing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **lesson extraction generalising beyond the specific instance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **retrieval of relevant past reasoning during new problems**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured improvement from accumulated reasoning experience** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_memory@1`
- `cap.t10.reasoning.reasoning_memory.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.backtracking.backtracking@1` | use the in-file conservative substitute for `backtracking` (documented, slower, lower quality) and set `degraded['backtracking']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t05.draft.draft_model_arch@1` | use the in-file conservative substitute for `draft_model_arch` (documented, slower, lower quality) and set `degraded['draft_model_arch']='local'` |
| `cap.t07.chunking.chunking_strategy@1` | use the in-file conservative substitute for `chunking_strategy` (documented, slower, lower quality) and set `degraded['chunking_strategy']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - trace storage with outcome labelling and indexing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - lesson extraction generalising beyond the specific instance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - retrieval of relevant past reasoning during new problems | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement from accumulated reasoning experience | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0479_reasoning_memory.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_memory@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 12000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0480 · `chain_compression` — Reasoning Chain Compression & Distillation

| field | value |
|---|---|
| part id | `P0480` (30/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0480_chain_compression.py` |
| module path | `hyperion.t10.reasoning.chain_compression` |
| capability published | `cap.t10.chain.chain_compression@1` |
| determinism class | `seeded` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0480_chain_compression.txt`](prompts/P0480_chain_compression.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0480-chain-compression) |

**Mission.** Turns long deliberation into short, reusable reasoning.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **trace compression preserving logical sufficiency** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **distillation of search behaviour into single-pass reasoning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **compression-ratio versus accuracy-retention curves** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured token reduction contributing to S5** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.chain.chain_compression@1`
- `cap.t10.chain.chain_compression.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_memory@1` | use the in-file conservative substitute for `reasoning_memory` (documented, slower, lower quality) and set `degraded['reasoning_memory']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t05.meta.meta_learning_arch@1` | use the in-file conservative substitute for `meta_learning_arch` (documented, slower, lower quality) and set `degraded['meta_learning_arch']='local'` |
| `cap.t07.memory.memory_encryption@1` | use the in-file conservative substitute for `memory_encryption` (documented, slower, lower quality) and set `degraded['memory_encryption']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - trace compression preserving logical sufficiency | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - distillation of search behaviour into single-pass reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - compression-ratio versus accuracy-retention curves | 520 | Third required mechanism. |
| 6 | Core implementation D - measured token reduction contributing to S5 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0480_chain_compression.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.chain.chain_compression@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 13000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0481 · `parallel_reasoning` — Parallel Reasoning Orchestration

| field | value |
|---|---|
| part id | `P0481` (31/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0481_parallel_reasoning.py` |
| module path | `hyperion.t10.reasoning.parallel_reasoning` |
| capability published | `cap.t10.parallel.parallel_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0481_parallel_reasoning.txt`](prompts/P0481_parallel_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0481-parallel-reasoning) |

**Mission.** 1000 reasoning threads on one problem, coordinated.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **work partitioning across independent reasoning branches**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **shared-discovery propagation between branches** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **resource allocation and early termination of unpromising branches** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured wall-clock reduction on hard problems** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.parallel.parallel_reasoning@1`
- `cap.t10.parallel.parallel_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.chain.chain_compression@1` | use the in-file conservative substitute for `chain_compression` (documented, slower, lower quality) and set `degraded['chain_compression']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t05.architecture.architecture_search@1` | use the in-file conservative substitute for `architecture_search` (documented, slower, lower quality) and set `degraded['architecture_search']='local'` |
| `cap.t07.tool.tool_result_cache@1` | use the in-file conservative substitute for `tool_result_cache` (documented, slower, lower quality) and set `degraded['tool_result_cache']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - work partitioning across independent reasoning branches | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - shared-discovery propagation between branches | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - resource allocation and early termination of unpromising branche | 520 | Third required mechanism. |
| 6 | Core implementation D - measured wall-clock reduction on hard problems | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0481_parallel_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.parallel.parallel_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 14000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0482 · `hypothesis_management` — Hypothesis Space Management

| field | value |
|---|---|
| part id | `P0482` (32/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0482_hypothesis_management.py` |
| module path | `hyperion.t10.reasoning.hypothesis_management` |
| capability published | `cap.t10.hypothesis.hypothesis_management@1` |
| determinism class | `seeded` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0482_hypothesis_management.txt`](prompts/P0482_hypothesis_management.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0482-hypothesis-management) |

**Mission.** Tracks many possible answers without confusing them.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **hypothesis set with evidence accounting per hypothesis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **pruning and merging rules with justification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **discriminating-evidence selection (what to check next)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured efficiency on diagnostic-reasoning tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.hypothesis.hypothesis_management@1`
- `cap.t10.hypothesis.hypothesis_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.parallel.parallel_reasoning@1` | use the in-file conservative substitute for `parallel_reasoning` (documented, slower, lower quality) and set `degraded['parallel_reasoning']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t05.speculative.speculative_arch_hooks@1` | use the in-file conservative substitute for `speculative_arch_hooks` (documented, slower, lower quality) and set `degraded['speculative_arch_hooks']='local'` |
| `cap.t07.temporal.temporal_memory@1` | use the in-file conservative substitute for `temporal_memory` (documented, slower, lower quality) and set `degraded['temporal_memory']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hypothesis set with evidence accounting per hypothesis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - pruning and merging rules with justification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - discriminating-evidence selection (what to check next) | 520 | Third required mechanism. |
| 6 | Core implementation D - measured efficiency on diagnostic-reasoning tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0482_hypothesis_management.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.hypothesis.hypothesis_management@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 15000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0483 · `evidence_integration` — Evidence Aggregation & Weighing

| field | value |
|---|---|
| part id | `P0483` (33/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0483_evidence_integration.py` |
| module path | `hyperion.t10.reasoning.evidence_integration` |
| capability published | `cap.t10.evidence.evidence_integration@1` |
| determinism class | `seeded` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0483_evidence_integration.txt`](prompts/P0483_evidence_integration.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0483-evidence-integration) |

**Mission.** Combines many weak signals into one strong conclusion correctly.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **evidence-strength quantification and source reliability weighting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **dependence-aware combination avoiding double counting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **conflicting-evidence handling with explicit uncertainty**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy measurement on evidence-aggregation tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.evidence.evidence_integration@1`
- `cap.t10.evidence.evidence_integration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.hypothesis.hypothesis_management@1` | use the in-file conservative substitute for `hypothesis_management` (documented, slower, lower quality) and set `degraded['hypothesis_management']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t05.expert.expert_specialisation@1` | use the in-file conservative substitute for `expert_specialisation` (documented, slower, lower quality) and set `degraded['expert_specialisation']='local'` |
| `cap.t07.memory.memory_bench@1` | use the in-file conservative substitute for `memory_bench` (documented, slower, lower quality) and set `degraded['memory_bench']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - evidence-strength quantification and source reliability weightin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dependence-aware combination avoiding double counting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conflicting-evidence handling with explicit uncertainty | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on evidence-aggregation tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0483_evidence_integration.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.evidence.evidence_integration@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 16000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0484 · `assumption_tracking` — Assumption Tracking & Explicit Uncertainty

| field | value |
|---|---|
| part id | `P0484` (34/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0484_assumption_tracking.py` |
| module path | `hyperion.t10.reasoning.assumption_tracking` |
| capability published | `cap.t10.assumption.assumption_tracking@1` |
| determinism class | `seeded` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0484_assumption_tracking.txt`](prompts/P0484_assumption_tracking.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0484-assumption-tracking) |

**Mission.** Every conclusion carries the assumptions it rests on.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **assumption extraction and dependency linking to conclusions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **assumption-sensitivity analysis identifying fragile conclusions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **clarifying-question generation for critical unknowns** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured reduction in confidently-wrong answers** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.assumption.assumption_tracking@1`
- `cap.t10.assumption.assumption_tracking.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.evidence.evidence_integration@1` | use the in-file conservative substitute for `evidence_integration` (documented, slower, lower quality) and set `degraded['evidence_integration']='local'` |
| `cap.t05.hybrid.hybrid_mixer@1` | use the in-file conservative substitute for `hybrid_mixer` (documented, slower, lower quality) and set `degraded['hybrid_mixer']='local'` |
| `cap.t07.kv.kv_paging@1` | use the in-file conservative substitute for `kv_paging` (documented, slower, lower quality) and set `degraded['kv_paging']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - assumption extraction and dependency linking to conclusions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - assumption-sensitivity analysis identifying fragile conclusions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - clarifying-question generation for critical unknowns | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction in confidently-wrong answers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0484_assumption_tracking.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.assumption.assumption_tracking@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 17000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0485 · `question_asking` — Clarification & Active Information Gathering

| field | value |
|---|---|
| part id | `P0485` (35/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0485_question_asking.py` |
| module path | `hyperion.t10.reasoning.question_asking` |
| capability published | `cap.t10.question.question_asking@1` |
| determinism class | `seeded` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0485_question_asking.txt`](prompts/P0485_question_asking.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0485-question-asking) |

**Mission.** Asks the one question that resolves the ambiguity.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **ambiguity detection with impact estimation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **information-gain-maximising question selection** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **asking-versus-assuming policy with cost modelling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured task-success improvement from clarification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.question.question_asking@1`
- `cap.t10.question.question_asking.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.assumption.assumption_tracking@1` | use the in-file conservative substitute for `assumption_tracking` (documented, slower, lower quality) and set `degraded['assumption_tracking']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t05.normalisation.normalisation_design@1` | use the in-file conservative substitute for `normalisation_design` (documented, slower, lower quality) and set `degraded['normalisation_design']='local'` |
| `cap.t07.semantic.semantic_memory@1` | use the in-file conservative substitute for `semantic_memory` (documented, slower, lower quality) and set `degraded['semantic_memory']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - ambiguity detection with impact estimation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - information-gain-maximising question selection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - asking-versus-assuming policy with cost modelling | 520 | Third required mechanism. |
| 6 | Core implementation D - measured task-success improvement from clarification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0485_question_asking.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.question.question_asking@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 18000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0486 · `reasoning_faithfulness` — Reasoning Faithfulness Verification

| field | value |
|---|---|
| part id | `P0486` (36/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0486_reasoning_faithfulness.py` |
| module path | `hyperion.t10.reasoning.reasoning_faithfulness` |
| capability published | `cap.t10.reasoning.reasoning_faithfulness@1` |
| determinism class | `seeded` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0486_reasoning_faithfulness.txt`](prompts/P0486_reasoning_faithfulness.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0486-reasoning-faithfulness) |

**Mission.** The shown reasoning is the actual reasoning.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **causal-intervention tests linking stated steps to the final answer** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **post-hoc-rationalisation detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **faithfulness metrics with measurement methodology** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: measurably higher faithfulness than Opus-class baselines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_faithfulness@1`
- `cap.t10.reasoning.reasoning_faithfulness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.question.question_asking@1` | use the in-file conservative substitute for `question_asking` (documented, slower, lower quality) and set `degraded['question_asking']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t05.multi.multi_token_prediction@1` | use the in-file conservative substitute for `multi_token_prediction` (documented, slower, lower quality) and set `degraded['multi_token_prediction']='local'` |
| `cap.t07.query.query_reformulation@1` | use the in-file conservative substitute for `query_reformulation` (documented, slower, lower quality) and set `degraded['query_reformulation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - causal-intervention tests linking stated steps to the final answ | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - post-hoc-rationalisation detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - faithfulness metrics with measurement methodology | 520 | Third required mechanism. |
| 6 | Core implementation D - target: measurably higher faithfulness than Opus-class baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0486_reasoning_faithfulness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_faithfulness@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 19000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0487 · `reasoning_robustness` — Reasoning Robustness to Perturbation

| field | value |
|---|---|
| part id | `P0487` (37/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0487_reasoning_robustness.py` |
| module path | `hyperion.t10.reasoning.reasoning_robustness` |
| capability published | `cap.t10.reasoning.reasoning_robustness@1` |
| determinism class | `seeded` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0487_reasoning_robustness.txt`](prompts/P0487_reasoning_robustness.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0487-reasoning-robustness) |

**Mission.** Same problem, different wording, same answer.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **paraphrase, distractor and irrelevant-context robustness testing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **sycophancy resistance under user pressure and false authority** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **consistency measurement across semantically identical inputs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured robustness improvement over baselines** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_robustness@1`
- `cap.t10.reasoning.reasoning_robustness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_faithfulness@1` | use the in-file conservative substitute for `reasoning_faithfulness` (documented, slower, lower quality) and set `degraded['reasoning_faithfulness']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t05.program.program_induction_arch@1` | use the in-file conservative substitute for `program_induction_arch` (documented, slower, lower quality) and set `degraded['program_induction_arch']='local'` |
| `cap.t07.memory.memory_privacy@1` | use the in-file conservative substitute for `memory_privacy` (documented, slower, lower quality) and set `degraded['memory_privacy']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - paraphrase, distractor and irrelevant-context robustness testing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sycophancy resistance under user pressure and false authority | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - consistency measurement across semantically identical inputs | 520 | Third required mechanism. |
| 6 | Core implementation D - measured robustness improvement over baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0487_reasoning_robustness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_robustness@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 20000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0488 · `multi_step_arithmetic` — Long Multi-Step Derivation Engine

| field | value |
|---|---|
| part id | `P0488` (38/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0488_multi_step_arithmetic.py` |
| module path | `hyperion.t10.reasoning.multi_step_arithmetic` |
| capability published | `cap.t10.multi.multi_step_arithmetic@1` |
| determinism class | `seeded` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0488_multi_step_arithmetic.txt`](prompts/P0488_multi_step_arithmetic.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0488-multi-step-arithmetic) |

**Mission.** Hundreds of dependent steps without a single slip.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **step-by-step invariant checking during derivation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **intermediate-result verification and redundant recomputation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **error localisation when a check fails** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on very-long-derivation benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.multi.multi_step_arithmetic@1`
- `cap.t10.multi.multi_step_arithmetic.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_robustness@1` | use the in-file conservative substitute for `reasoning_robustness` (documented, slower, lower quality) and set `degraded['reasoning_robustness']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t05.init.init_scaling_laws@1` | use the in-file conservative substitute for `init_scaling_laws` (documented, slower, lower quality) and set `degraded['init_scaling_laws']='local'` |
| `cap.t07.semantic.semantic_cache@1` | use the in-file conservative substitute for `semantic_cache` (documented, slower, lower quality) and set `degraded['semantic_cache']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - step-by-step invariant checking during derivation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - intermediate-result verification and redundant recomputation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - error localisation when a check fails | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on very-long-derivation benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0488_multi_step_arithmetic.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.multi.multi_step_arithmetic@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 21000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0489 · `proof_sketch` — Proof Sketch Generation & Refinement

| field | value |
|---|---|
| part id | `P0489` (39/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0489_proof_sketch.py` |
| module path | `hyperion.t10.reasoning.proof_sketch` |
| capability published | `cap.t10.proof.proof_sketch@1` |
| determinism class | `seeded` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0489_proof_sketch.txt`](prompts/P0489_proof_sketch.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0489-proof-sketch) |

**Mission.** Bridges informal reasoning and formal verification.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **sketch generation with explicit gaps marked**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **gap-filling with targeted subproof search** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **handoff protocol to the formal-methods tier** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured formalisation success rate from sketches** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.proof.proof_sketch@1`
- `cap.t10.proof.proof_sketch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.multi.multi_step_arithmetic@1` | use the in-file conservative substitute for `multi_step_arithmetic` (documented, slower, lower quality) and set `degraded['multi_step_arithmetic']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t05.memory.memory_attention_bridge@1` | use the in-file conservative substitute for `memory_attention_bridge` (documented, slower, lower quality) and set `degraded['memory_attention_bridge']='local'` |
| `cap.t07.graph.graph_memory_queries@1` | use the in-file conservative substitute for `graph_memory_queries` (documented, slower, lower quality) and set `degraded['graph_memory_queries']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sketch generation with explicit gaps marked | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - gap-filling with targeted subproof search | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - handoff protocol to the formal-methods tier | 520 | Third required mechanism. |
| 6 | Core implementation D - measured formalisation success rate from sketches | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0489_proof_sketch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.proof.proof_sketch@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 22000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0490 · `reasoning_search_bench` — Reasoning Benchmark Harness

| field | value |
|---|---|
| part id | `P0490` (40/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0490_reasoning_search_bench.py` |
| module path | `hyperion.t10.reasoning.reasoning_search_bench` |
| capability published | `cap.t10.reasoning.reasoning_search_bench@1` |
| determinism class | `seeded` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0490_reasoning_search_bench.txt`](prompts/P0490_reasoning_search_bench.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0490-reasoning-search-bench) |

**Mission.** Measures every reasoning capability reproducibly.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **harnesses for ARC-AGI-3, ARC-AGI-2, AIME/HMMT, GPQA and internal suites** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **compute-matched comparison methodology versus Opus 5** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **per-capability breakdown with error taxonomy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **targets: ARC-AGI-3 88%, ARC-AGI-2 93%, GPQA 99.6%, AIME 100%**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_search_bench@1`
- `cap.t10.reasoning.reasoning_search_bench.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.proof.proof_sketch@1` | use the in-file conservative substitute for `proof_sketch` (documented, slower, lower quality) and set `degraded['proof_sketch']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t05.thought.thought_representation@1` | use the in-file conservative substitute for `thought_representation` (documented, slower, lower quality) and set `degraded['thought_representation']='local'` |
| `cap.t07.provenance.provenance_tracking@1` | use the in-file conservative substitute for `provenance_tracking` (documented, slower, lower quality) and set `degraded['provenance_tracking']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - harnesses for ARC-AGI-3, ARC-AGI-2, AIME/HMMT, GPQA and internal | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compute-matched comparison methodology versus Opus 5 | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-capability breakdown with error taxonomy | 520 | Third required mechanism. |
| 6 | Core implementation D - targets: ARC-AGI-3 88%, ARC-AGI-2 93%, GPQA 99.6%, AIME 100% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0490_reasoning_search_bench.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_search_bench@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 23000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0491 · `reasoning_cost_model` — Value of Computation Model

| field | value |
|---|---|
| part id | `P0491` (41/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0491_reasoning_cost_model.py` |
| module path | `hyperion.t10.reasoning.reasoning_cost_model` |
| capability published | `cap.t10.reasoning.reasoning_cost_model@1` |
| determinism class | `seeded` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0491_reasoning_cost_model.txt`](prompts/P0491_reasoning_cost_model.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0491-reasoning-cost-model) |

**Mission.** Predicts whether more thinking will actually help.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **marginal-accuracy-per-token estimation per task class** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **diminishing-returns detection from early signals** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **budget policy optimisation under cost constraints**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **prediction-accuracy validation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_cost_model@1`
- `cap.t10.reasoning.reasoning_cost_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_search_bench@1` | use the in-file conservative substitute for `reasoning_search_bench` (documented, slower, lower quality) and set `degraded['reasoning_search_bench']='local'` |
| `cap.t05.omega.omega_block@1` | use the in-file conservative substitute for `omega_block` (documented, slower, lower quality) and set `degraded['omega_block']='local'` |
| `cap.t07.kv.kv_hierarchy@1` | use the in-file conservative substitute for `kv_hierarchy` (documented, slower, lower quality) and set `degraded['kv_hierarchy']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - marginal-accuracy-per-token estimation per task class | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - diminishing-returns detection from early signals | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - budget policy optimisation under cost constraints | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction-accuracy validation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0491_reasoning_cost_model.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_cost_model@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 24000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0492 · `scratchpad_manager` — Scratchpad & Working Memory Manager

| field | value |
|---|---|
| part id | `P0492` (42/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0492_scratchpad_manager.py` |
| module path | `hyperion.t10.reasoning.scratchpad_manager` |
| capability published | `cap.t10.scratchpad.scratchpad_manager@1` |
| determinism class | `seeded` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0492_scratchpad_manager.txt`](prompts/P0492_scratchpad_manager.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0492-scratchpad-manager) |

**Mission.** Deliberation space that never overflows or loses the thread.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **structured scratchpad with typed slots and capacity management** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **compaction preserving logically necessary content**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **read/write discipline preventing contradiction accumulation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured effect on long-reasoning reliability** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.scratchpad.scratchpad_manager@1`
- `cap.t10.scratchpad.scratchpad_manager.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_cost_model@1` | use the in-file conservative substitute for `reasoning_cost_model` (documented, slower, lower quality) and set `degraded['reasoning_cost_model']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t05.adaptive.adaptive_depth@1` | use the in-file conservative substitute for `adaptive_depth` (documented, slower, lower quality) and set `degraded['adaptive_depth']='local'` |
| `cap.t07.episodic.episodic_memory@1` | use the in-file conservative substitute for `episodic_memory` (documented, slower, lower quality) and set `degraded['episodic_memory']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structured scratchpad with typed slots and capacity management | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compaction preserving logically necessary content | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - read/write discipline preventing contradiction accumulation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured effect on long-reasoning reliability | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0492_scratchpad_manager.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.scratchpad.scratchpad_manager@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 25000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0493 · `subgoal_caching` — Subgoal Solution Caching

| field | value |
|---|---|
| part id | `P0493` (43/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0493_subgoal_caching.py` |
| module path | `hyperion.t10.reasoning.subgoal_caching` |
| capability published | `cap.t10.subgoal.subgoal_caching@1` |
| determinism class | `seeded` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0493_subgoal_caching.txt`](prompts/P0493_subgoal_caching.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0493-subgoal-caching) |

**Mission.** Solves each subproblem once per lifetime, not once per request.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **canonical subgoal identification modulo irrelevant variation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **solution reuse with applicability verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cache growth management and quality assurance** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured reuse rate and its contribution to S4** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.subgoal.subgoal_caching@1`
- `cap.t10.subgoal.subgoal_caching.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.scratchpad.scratchpad_manager@1` | use the in-file conservative substitute for `scratchpad_manager` (documented, slower, lower quality) and set `degraded['scratchpad_manager']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t05.long.long_context_arch@1` | use the in-file conservative substitute for `long_context_arch` (documented, slower, lower quality) and set `degraded['long_context_arch']='local'` |
| `cap.t07.hybrid.hybrid_retrieval@1` | use the in-file conservative substitute for `hybrid_retrieval` (documented, slower, lower quality) and set `degraded['hybrid_retrieval']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - canonical subgoal identification modulo irrelevant variation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - solution reuse with applicability verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cache growth management and quality assurance | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reuse rate and its contribution to S4 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0493_subgoal_caching.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.subgoal.subgoal_caching@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 26000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0494 · `reasoning_transfer` — Cross-Domain Reasoning Transfer

| field | value |
|---|---|
| part id | `P0494` (44/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0494_reasoning_transfer.py` |
| module path | `hyperion.t10.reasoning.reasoning_transfer` |
| capability published | `cap.t10.reasoning.reasoning_transfer@1` |
| determinism class | `seeded` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0494_reasoning_transfer.txt`](prompts/P0494_reasoning_transfer.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0494-reasoning-transfer) |

**Mission.** A technique learned in math helps in law.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **domain-general strategy extraction and representation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **transfer applicability prediction** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **measured performance on domains absent from strategy training** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **negative-transfer detection and prevention**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_transfer@1`
- `cap.t10.reasoning.reasoning_transfer.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.subgoal.subgoal_caching@1` | use the in-file conservative substitute for `subgoal_caching` (documented, slower, lower quality) and set `degraded['subgoal_caching']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t05.symbolic.symbolic_bridge@1` | use the in-file conservative substitute for `symbolic_bridge` (documented, slower, lower quality) and set `degraded['symbolic_bridge']='local'` |
| `cap.t07.conflict.conflict_resolution@1` | use the in-file conservative substitute for `conflict_resolution` (documented, slower, lower quality) and set `degraded['conflict_resolution']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - domain-general strategy extraction and representation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - transfer applicability prediction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - measured performance on domains absent from strategy training | 520 | Third required mechanism. |
| 6 | Core implementation D - negative-transfer detection and prevention | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0494_reasoning_transfer.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_transfer@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 27000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0495 · `error_taxonomy` — Reasoning Error Taxonomy & Diagnosis

| field | value |
|---|---|
| part id | `P0495` (45/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0495_error_taxonomy.py` |
| module path | `hyperion.t10.reasoning.error_taxonomy` |
| capability published | `cap.t10.error.error_taxonomy@1` |
| determinism class | `seeded` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0495_error_taxonomy.txt`](prompts/P0495_error_taxonomy.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0495-error-taxonomy) |

**Mission.** Names every way reasoning fails, then fixes each one.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **error taxonomy with automatic classification of failures** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **per-error-class frequency tracking across benchmarks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **targeted remediation recommendation per class**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured reduction per error class over time** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.error.error_taxonomy@1`
- `cap.t10.error.error_taxonomy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_transfer@1` | use the in-file conservative substitute for `reasoning_transfer` (documented, slower, lower quality) and set `degraded['reasoning_transfer']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t05.weight.weight_sharing@1` | use the in-file conservative substitute for `weight_sharing` (documented, slower, lower quality) and set `degraded['weight_sharing']='local'` |
| `cap.t07.cache.cache_warm_predict@1` | use the in-file conservative substitute for `cache_warm_predict` (documented, slower, lower quality) and set `degraded['cache_warm_predict']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - error taxonomy with automatic classification of failures | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-error-class frequency tracking across benchmarks | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - targeted remediation recommendation per class | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction per error class over time | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0495_error_taxonomy.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.error.error_taxonomy@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 28000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0496 · `adversarial_reasoning` — Adversarial Reasoning Stress Tests

| field | value |
|---|---|
| part id | `P0496` (46/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0496_adversarial_reasoning.py` |
| module path | `hyperion.t10.reasoning.adversarial_reasoning` |
| capability published | `cap.t10.adversarial.adversarial_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0496_adversarial_reasoning.txt`](prompts/P0496_adversarial_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0496-adversarial-reasoning) |

**Mission.** Deliberately tries to break its own thinking.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **trap-problem generation (misleading framing, false premises, hidden constraints)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **measurement of failure modes under adversarial pressure**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **hardening feedback loop into training and policy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **adversarial-suite pass-rate tracking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.adversarial.adversarial_reasoning@1`
- `cap.t10.adversarial.adversarial_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.error.error_taxonomy@1` | use the in-file conservative substitute for `error_taxonomy` (documented, slower, lower quality) and set `degraded['error_taxonomy']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t05.action.action_head@1` | use the in-file conservative substitute for `action_head` (documented, slower, lower quality) and set `degraded['action_head']='local'` |
| `cap.t07.memory.memory_replication@1` | use the in-file conservative substitute for `memory_replication` (documented, slower, lower quality) and set `degraded['memory_replication']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - trap-problem generation (misleading framing, false premises, hid | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - measurement of failure modes under adversarial pressure | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hardening feedback loop into training and policy | 520 | Third required mechanism. |
| 6 | Core implementation D - adversarial-suite pass-rate tracking | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0496_adversarial_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.adversarial.adversarial_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 29000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0497 · `reasoning_interpretability` — Reasoning Introspection & Explanation

| field | value |
|---|---|
| part id | `P0497` (47/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0497_reasoning_interpretability.py` |
| module path | `hyperion.t10.reasoning.reasoning_interpretability` |
| capability published | `cap.t10.reasoning.reasoning_interpretability@1` |
| determinism class | `seeded` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0497_reasoning_interpretability.txt`](prompts/P0497_reasoning_interpretability.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0497-reasoning-interpretability) |

**Mission.** Explains its own reasoning process accurately.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **search-trace summarisation into human-readable explanation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **decision-point rationale extraction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **explanation-fidelity verification against the actual trace** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **usability validation with expert reviewers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_interpretability@1`
- `cap.t10.reasoning.reasoning_interpretability.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.adversarial.adversarial_reasoning@1` | use the in-file conservative substitute for `adversarial_reasoning` (documented, slower, lower quality) and set `degraded['adversarial_reasoning']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t05.prompt.prompt_representation@1` | use the in-file conservative substitute for `prompt_representation` (documented, slower, lower quality) and set `degraded['prompt_representation']='local'` |
| `cap.t07.dedup.dedup_engine@1` | use the in-file conservative substitute for `dedup_engine` (documented, slower, lower quality) and set `degraded['dedup_engine']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - search-trace summarisation into human-readable explanation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - decision-point rationale extraction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - explanation-fidelity verification against the actual trace | 520 | Third required mechanism. |
| 6 | Core implementation D - usability validation with expert reviewers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0497_reasoning_interpretability.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_interpretability@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 30000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0498 · `collective_reasoning` — Multi-Instance Collective Reasoning

| field | value |
|---|---|
| part id | `P0498` (48/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0498_collective_reasoning.py` |
| module path | `hyperion.t10.reasoning.collective_reasoning` |
| capability published | `cap.t10.collective.collective_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0498_collective_reasoning.txt`](prompts/P0498_collective_reasoning.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0498-collective-reasoning) |

**Mission.** Many Ω instances solving one problem better than any alone.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **work division and result integration protocols** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **disagreement resolution with evidence-based arbitration** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **communication-efficiency measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured gain versus single-instance at matched total compute**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t10.collective.collective_reasoning@1`
- `cap.t10.collective.collective_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_interpretability@1` | use the in-file conservative substitute for `reasoning_interpretability` (documented, slower, lower quality) and set `degraded['reasoning_interpretability']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t05.arch.arch_spec_doc@1` | use the in-file conservative substitute for `arch_spec_doc` (documented, slower, lower quality) and set `degraded['arch_spec_doc']='local'` |
| `cap.t07.memory.memory_spec_doc@1` | use the in-file conservative substitute for `memory_spec_doc` (documented, slower, lower quality) and set `degraded['memory_spec_doc']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - work division and result integration protocols | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - disagreement resolution with evidence-based arbitration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - communication-efficiency measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured gain versus single-instance at matched total compute | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0498_collective_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.collective.collective_reasoning@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 31000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0499 · `reasoning_speed_proof` — S5 Speedup Proof & Attribution

| field | value |
|---|---|
| part id | `P0499` (49/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0499_reasoning_speed_proof.py` |
| module path | `hyperion.t10.reasoning.reasoning_speed_proof` |
| capability published | `cap.t10.reasoning.reasoning_speed_proof@1` |
| determinism class | `seeded` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0499_reasoning_speed_proof.txt`](prompts/P0499_reasoning_speed_proof.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0499-reasoning-speed-proof) |

**Mission.** Proves the 2.2x reasoning-efficiency component of the 100x law.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **token-per-solved-task measurement versus unguided baselines** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **isolation of pruning, stopping and compression contributions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **confidence intervals across task families**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **attribution report feeding the 100x proof** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_speed_proof@1`
- `cap.t10.reasoning.reasoning_speed_proof.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.collective.collective_reasoning@1` | use the in-file conservative substitute for `collective_reasoning` (documented, slower, lower quality) and set `degraded['collective_reasoning']='local'` |
| `cap.t05.latent.latent_program_slots@1` | use the in-file conservative substitute for `latent_program_slots` (documented, slower, lower quality) and set `degraded['latent_program_slots']='local'` |
| `cap.t07.summarisation.summarisation_memory@1` | use the in-file conservative substitute for `summarisation_memory` (documented, slower, lower quality) and set `degraded['summarisation_memory']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - token-per-solved-task measurement versus unguided baselines | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - isolation of pruning, stopping and compression contributions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - confidence intervals across task families | 520 | Third required mechanism. |
| 6 | Core implementation D - attribution report feeding the 100x proof | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0499_reasoning_speed_proof.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_speed_proof@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 32000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---

### P0500 · `reasoning_spec_doc` — Reasoning Subsystem Specification

| field | value |
|---|---|
| part id | `P0500` (50/50 of T10) |
| tier | `T10` — Reasoning, Search & Deliberation |
| language | Python 3.13 |
| file to produce | `parts/t10_reasoning/P0500_reasoning_spec_doc.py` |
| module path | `hyperion.t10.reasoning.reasoning_spec_doc` |
| capability published | `cap.t10.reasoning.reasoning_spec_doc@1` |
| determinism class | `seeded` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | ARC-AGI-3, ARC-AGI-2, AIME / HMMT 2026 |
| worker prompt | [`prompts/P0500_reasoning_spec_doc.txt`](prompts/P0500_reasoning_spec_doc.txt) · [inline](docs/PROMPTS_T10.md#prompt-p0500-reasoning-spec-doc) |

**Mission.** The authoritative description of all deliberation machinery.

**Tier context.** Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.

**Mandate — all four items are required; none is optional.**

1. Implement **specification of thought IR, search policies and verification levels** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **auto-generated capability and budget tables**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **operator guidance for reasoning-quality incidents** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **ARC-AGI-2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **spec-versus-implementation drift detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **AIME / HMMT 2026**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t10.reasoning.reasoning_spec_doc@1`
- `cap.t10.reasoning.reasoning_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t10.reasoning.reasoning_speed_proof@1` | use the in-file conservative substitute for `reasoning_speed_proof` (documented, slower, lower quality) and set `degraded['reasoning_speed_proof']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t05.positional.positional_design@1` | use the in-file conservative substitute for `positional_design` (documented, slower, lower quality) and set `degraded['positional_design']='local'` |
| `cap.t07.sparse.sparse_retrieval@1` | use the in-file conservative substitute for `sparse_retrieval` (documented, slower, lower quality) and set `degraded['sparse_retrieval']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - specification of thought IR, search policies and verification le | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - auto-generated capability and budget tables | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - operator guidance for reasoning-quality incidents | 520 | Third required mechanism. |
| 6 | Core implementation D - spec-versus-implementation drift detection | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t10_reasoning/P0500_reasoning_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t10.reasoning.reasoning_spec_doc@1`.
- [ ] `register(bus)`, `selftest()`, `microbench(iters)`, `describe()` all exist with the contract signatures.
- [ ] `selftest()` returns `(True, report)` with zero network access, zero writes outside a temp dir, in under 60 s.
- [ ] `microbench()` asserts p99 ≤ 33000 ns at the declared reference shape.
- [ ] Declared determinism class `seeded` is proven by the in-file determinism harness.
- [ ] Every entry in `requires` has a working fallback; removing the bus entirely still lets `selftest()` pass in degraded mode.
- [ ] ≥ 40 unit/boundary/regression cases + property tests for every stated invariant + a fuzz target.
- [ ] A documented, honest **Limitations** section. Overstated claims are a rejection.
- [ ] Total lines within ±3 % of 5000.

**Forbidden.** Cross-part imports; reading a sibling's source; `print`/`console.log` outside a debug guard; global mutable state; wall-clock or RNG use outside the declared class; TODO / FIXME / `pass  # later`; suppressing type or lint errors without a written justification.

---
