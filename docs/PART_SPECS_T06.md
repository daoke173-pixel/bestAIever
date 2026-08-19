# HYPERION-Ω — Part specifications · T06 · Sparse Routing & Mixture-of-Ω-Experts

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Benchmarks this tier is accountable for.** GPQA Diamond

**Tier dependencies.** T01, T05

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0251](#p0251-router-core) | `router_core` | Top-K Router Core | `cap.t06.router.router_core@1` |
| [P0252](#p0252-router-balance) | `router_balance` | Load Balancing Losses & Constraints | `cap.t06.router.router_balance@1` |
| [P0253](#p0253-router-capacity) | `router_capacity` | Capacity Factor & Overflow Policy | `cap.t06.router.router_capacity@1` |
| [P0254](#p0254-router-hash-hybrid) | `router_hash_hybrid` | Hybrid Learned/Deterministic Routing | `cap.t06.router.router_hash_hybrid@1` |
| [P0255](#p0255-expert-ffn) | `expert_ffn` | Expert Feed-Forward Implementation | `cap.t06.expert.expert_ffn@1` |
| [P0256](#p0256-expert-attention) | `expert_attention` | Mixture-of-Attention-Heads Routing | `cap.t06.expert.expert_attention@1` |
| [P0257](#p0257-shared-expert) | `shared_expert` | Shared & Residual Expert Design | `cap.t06.shared.shared_expert@1` |
| [P0258](#p0258-fine-grained-experts) | `fine_grained_experts` | Fine-Grained Expert Segmentation | `cap.t06.fine.fine_grained_experts@1` |
| [P0259](#p0259-expert-placement) | `expert_placement` | Expert Placement & Replication Policy | `cap.t06.expert.expert_placement@1` |
| [P0260](#p0260-expert-prefetch) | `expert_prefetch` | Expert Weight Prefetching & Caching | `cap.t06.expert.expert_prefetch@1` |
| [P0261](#p0261-router-lookahead) | `router_lookahead` | Router Prediction & Speculative Routing | `cap.t06.router.router_lookahead@1` |
| [P0262](#p0262-moe-determinism) | `moe_determinism` | Deterministic MoE Execution | `cap.t06.moe.moe_determinism@1` |
| [P0263](#p0263-expert-lifecycle) | `expert_lifecycle` | Expert Birth, Death & Reincarnation | `cap.t06.expert.expert_lifecycle@1` |
| [P0264](#p0264-expert-diversity) | `expert_diversity` | Expert Diversity Objectives | `cap.t06.expert.expert_diversity@1` |
| [P0265](#p0265-router-temperature) | `router_temperature` | Router Sharpness & Exploration Schedule | `cap.t06.router.router_temperature@1` |
| [P0266](#p0266-sparse-activation-stats) | `sparse_activation_stats` | Sparse Activation Statistics & Diagnostics | `cap.t06.sparse.sparse_activation_stats@1` |
| [P0267](#p0267-moe-quantisation) | `moe_quantisation` | Per-Expert Quantisation Strategy | `cap.t06.moe.moe_quantisation@1` |
| [P0268](#p0268-expert-offload) | `expert_offload` | Expert Offloading to Host/Storage | `cap.t06.expert.expert_offload@1` |
| [P0269](#p0269-moe-batching) | `moe_batching` | MoE-Aware Request Batching | `cap.t06.moe.moe_batching@1` |
| [P0270](#p0270-token-dropping) | `token_dropping` | Token Dropping & Early Exit Policy | `cap.t06.token.token_dropping@1` |
| [P0271](#p0271-conditional-layers) | `conditional_layers` | Layer Skipping & Conditional Depth Routing | `cap.t06.conditional.conditional_layers@1` |
| [P0272](#p0272-mod-routing) | `mod_routing` | Mixture-of-Depths Routing | `cap.t06.mod.mod_routing@1` |
| [P0273](#p0273-router-robustness) | `router_robustness` | Router Adversarial Robustness | `cap.t06.router.router_robustness@1` |
| [P0274](#p0274-gating-alternatives) | `gating_alternatives` | Alternative Gating Mechanisms | `cap.t06.gating.gating_alternatives@1` |
| [P0275](#p0275-expert-choice-routing) | `expert_choice_routing` | Expert-Choice Routing | `cap.t06.expert.expert_choice_routing@1` |
| [P0276](#p0276-moe-scaling-laws) | `moe_scaling_laws` | MoE Scaling Laws & Budget Allocation | `cap.t06.moe.moe_scaling_laws@1` |
| [P0277](#p0277-router-interpretability) | `router_interpretability` | Router Interpretability & Expert Naming | `cap.t06.router.router_interpretability@1` |
| [P0278](#p0278-moe-training-stability) | `moe_training_stability` | MoE Training Stability Engineering | `cap.t06.moe.moe_training_stability@1` |
| [P0279](#p0279-expert-dropout) | `expert_dropout` | Expert Dropout & Robustness to Missing Experts | `cap.t06.expert.expert_dropout@1` |
| [P0280](#p0280-sparse-kernels-bridge) | `sparse_kernels_bridge` | Routing-to-Kernel Bridge | `cap.t06.sparse.sparse_kernels_bridge@1` |
| [P0281](#p0281-modality-routing) | `modality_routing` | Modality- & Language-Aware Routing | `cap.t06.modality.modality_routing@1` |
| [P0282](#p0282-difficulty-routing) | `difficulty_routing` | Difficulty-Aware Compute Routing | `cap.t06.difficulty.difficulty_routing@1` |
| [P0283](#p0283-cost-aware-routing) | `cost_aware_routing` | Cost- & SLO-Aware Routing Policy | `cap.t06.cost.cost_aware_routing@1` |
| [P0284](#p0284-model-cascade-routing) | `model_cascade_routing` | Model Cascade & Escalation Router | `cap.t06.model.model_cascade_routing@1` |
| [P0285](#p0285-ensemble-combiner) | `ensemble_combiner` | Ensemble & Multi-Sample Combination | `cap.t06.ensemble.ensemble_combiner@1` |
| [P0286](#p0286-router-cache) | `router_cache` | Routing Decision Cache | `cap.t06.router.router_cache@1` |
| [P0287](#p0287-expert-warmup) | `expert_warmup` | Expert Warmup & Cold-Start Handling | `cap.t06.expert.expert_warmup@1` |
| [P0288](#p0288-routing-fairness) | `routing_fairness` | Cross-User Routing Fairness & Isolation | `cap.t06.routing.routing_fairness@1` |
| [P0289](#p0289-moe-memory-budget) | `moe_memory_budget` | MoE Memory Budget Planner | `cap.t06.moe.moe_memory_budget@1` |
| [P0290](#p0290-router-online-learning) | `router_online_learning` | Online Router Adaptation | `cap.t06.router.router_online_learning@1` |
| [P0291](#p0291-sparse-gradient) | `sparse_gradient` | Sparse Gradient Handling & Accumulation | `cap.t06.sparse.sparse_gradient@1` |
| [P0292](#p0292-expert-alignment) | `expert_alignment` | Per-Expert Safety & Alignment Auditing | `cap.t06.expert.expert_alignment@1` |
| [P0293](#p0293-routing-privacy) | `routing_privacy` | Routing Privacy & Side-Channel Defence | `cap.t06.routing.routing_privacy@1` |
| [P0294](#p0294-hierarchical-routing) | `hierarchical_routing` | Hierarchical Two-Level Routing | `cap.t06.hierarchical.hierarchical_routing@1` |
| [P0295](#p0295-router-bench) | `router_bench` | Routing Benchmark & Regression Suite | `cap.t06.router.router_bench@1` |
| [P0296](#p0296-moe-visualisation) | `moe_visualisation` | Sparse Compute Visualisation & Explainer | `cap.t06.moe.moe_visualisation@1` |
| [P0297](#p0297-adaptive-sparsity) | `adaptive_sparsity` | Runtime-Adaptive Sparsity Control | `cap.t06.adaptive.adaptive_sparsity@1` |
| [P0298](#p0298-sparsity-verification) | `sparsity_verification` | Conditional-Compute Correctness Verification | `cap.t06.sparsity.sparsity_verification@1` |
| [P0299](#p0299-moe-speed-accounting) | `moe_speed_accounting` | S2 Speedup Accounting & Attribution | `cap.t06.moe.moe_speed_accounting@1` |
| [P0300](#p0300-moe-spec-doc) | `moe_spec_doc` | Sparse Architecture Specification & Docs | `cap.t06.moe.moe_spec_doc@1` |

---

### P0251 · `router_core` — Top-K Router Core

| field | value |
|---|---|
| part id | `P0251` (1/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0251_router_core.py` |
| module path | `hyperion.t06.routing.router_core` |
| capability published | `cap.t06.router.router_core@1` |
| determinism class | `seeded` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0251_router_core.txt`](prompts/P0251_router_core.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0251-router-core) |

**Mission.** The gating function that selects 2 of 512 experts per token.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **gate scoring with normalisation choice justified by measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **top-k selection with deterministic tie-breaking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **gradient path (straight-through vs REINFORCE) comparison**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **routing-decision determinism under batch reordering** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.router.router_core@1`
- `cap.t06.router.router_core.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t05.causal.causal_model@1` | use the in-file conservative substitute for `causal_model` (documented, slower, lower quality) and set `degraded['causal_model']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gate scoring with normalisation choice justified by measurement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - top-k selection with deterministic tie-breaking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - gradient path (straight-through vs REINFORCE) comparison | 520 | Third required mechanism. |
| 6 | Core implementation D - routing-decision determinism under batch reordering | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0251_router_core.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_core@1`.
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

### P0252 · `router_balance` — Load Balancing Losses & Constraints

| field | value |
|---|---|
| part id | `P0252` (2/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0252_router_balance.py` |
| module path | `hyperion.t06.routing.router_balance` |
| capability published | `cap.t06.router.router_balance@1` |
| determinism class | `seeded` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0252_router_balance.txt`](prompts/P0252_router_balance.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0252-router-balance) |

**Mission.** Prevents expert collapse without hurting quality.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **auxiliary-loss and loss-free bias-correction methods compared** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **per-batch and per-sequence balance metrics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **coefficient tuning with quality-versus-balance curves** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **collapse detection and automatic remediation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.router.router_balance@1`
- `cap.t06.router.router_balance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_core@1` | use the in-file conservative substitute for `router_core` (documented, slower, lower quality) and set `degraded['router_core']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t05.distillation.distillation_arch@1` | use the in-file conservative substitute for `distillation_arch` (documented, slower, lower quality) and set `degraded['distillation_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - auxiliary-loss and loss-free bias-correction methods compared | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-batch and per-sequence balance metrics | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - coefficient tuning with quality-versus-balance curves | 520 | Third required mechanism. |
| 6 | Core implementation D - collapse detection and automatic remediation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0252_router_balance.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_balance@1`.
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

### P0253 · `router_capacity` — Capacity Factor & Overflow Policy

| field | value |
|---|---|
| part id | `P0253` (3/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0253_router_capacity.py` |
| module path | `hyperion.t06.routing.router_capacity` |
| capability published | `cap.t06.router.router_capacity@1` |
| determinism class | `seeded` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0253_router_capacity.txt`](prompts/P0253_router_capacity.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0253-router-capacity) |

**Mission.** What happens when an expert is oversubscribed.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **capacity computation per batch shape with headroom policy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **overflow handling: drop, reroute, residual-pass with quality accounting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **deterministic overflow ordering** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **quality impact measurement at multiple capacity factors** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.router.router_capacity@1`
- `cap.t06.router.router_capacity.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_balance@1` | use the in-file conservative substitute for `router_balance` (documented, slower, lower quality) and set `degraded['router_balance']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t05.multimodal.multimodal_fusion_arch@1` | use the in-file conservative substitute for `multimodal_fusion_arch` (documented, slower, lower quality) and set `degraded['multimodal_fusion_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capacity computation per batch shape with headroom policy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - overflow handling: drop, reroute, residual-pass with quality acc | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deterministic overflow ordering | 520 | Third required mechanism. |
| 6 | Core implementation D - quality impact measurement at multiple capacity factors | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0253_router_capacity.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_capacity@1`.
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

### P0254 · `router_hash_hybrid` — Hybrid Learned/Deterministic Routing

| field | value |
|---|---|
| part id | `P0254` (4/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0254_router_hash_hybrid.py` |
| module path | `hyperion.t06.routing.router_hash_hybrid` |
| capability published | `cap.t06.router.router_hash_hybrid@1` |
| determinism class | `seeded` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0254_router_hash_hybrid.txt`](prompts/P0254_router_hash_hybrid.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0254-router-hash-hybrid) |

**Mission.** Combines learned gates with hash and rule-based routing for stability.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **hash-routing fallback with balanced-by-construction guarantees** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **rule-based routing for known domains (code, math, language)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **blending policy and switchover criteria** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **stability-versus-adaptivity measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.router.router_hash_hybrid@1`
- `cap.t06.router.router_hash_hybrid.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_capacity@1` | use the in-file conservative substitute for `router_capacity` (documented, slower, lower quality) and set `degraded['router_capacity']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t05.context.context_packing@1` | use the in-file conservative substitute for `context_packing` (documented, slower, lower quality) and set `degraded['context_packing']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hash-routing fallback with balanced-by-construction guarantees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - rule-based routing for known domains (code, math, language) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blending policy and switchover criteria | 520 | Third required mechanism. |
| 6 | Core implementation D - stability-versus-adaptivity measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0254_router_hash_hybrid.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_hash_hybrid@1`.
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

### P0255 · `expert_ffn` — Expert Feed-Forward Implementation

| field | value |
|---|---|
| part id | `P0255` (5/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0255_expert_ffn.py` |
| module path | `hyperion.t06.routing.expert_ffn` |
| capability published | `cap.t06.expert.expert_ffn@1` |
| determinism class | `seeded` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0255_expert_ffn.txt`](prompts/P0255_expert_ffn.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0255-expert-ffn) |

**Mission.** The expert body: fast, quantisation-friendly, specialisable.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **gated-linear expert with per-expert scaling and bias handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **quantised expert weights with per-expert calibration** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **expert-local normalisation choices**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **throughput at 512 experts with realistic skew** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.expert.expert_ffn@1`
- `cap.t06.expert.expert_ffn.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_hash_hybrid@1` | use the in-file conservative substitute for `router_hash_hybrid` (documented, slower, lower quality) and set `degraded['router_hash_hybrid']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t05.capacity.capacity_probes@1` | use the in-file conservative substitute for `capacity_probes` (documented, slower, lower quality) and set `degraded['capacity_probes']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gated-linear expert with per-expert scaling and bias handling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quantised expert weights with per-expert calibration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - expert-local normalisation choices | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput at 512 experts with realistic skew | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0255_expert_ffn.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_ffn@1`.
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

### P0256 · `expert_attention` — Mixture-of-Attention-Heads Routing

| field | value |
|---|---|
| part id | `P0256` (6/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0256_expert_attention.py` |
| module path | `hyperion.t06.routing.expert_attention` |
| capability published | `cap.t06.expert.expert_attention@1` |
| determinism class | `seeded` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0256_expert_attention.txt`](prompts/P0256_expert_attention.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0256-expert-attention) |

**Mission.** Applies conditional compute to attention, not just feed-forward.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **head-group routing with per-token selection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **KV-cost implications and sharing strategy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **quality gain measurement versus dense attention** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **kernel integration with the paged decode path** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.expert.expert_attention@1`
- `cap.t06.expert.expert_attention.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_ffn@1` | use the in-file conservative substitute for `expert_ffn` (documented, slower, lower quality) and set `degraded['expert_ffn']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t05.recurrent.recurrent_memory_layer@1` | use the in-file conservative substitute for `recurrent_memory_layer` (documented, slower, lower quality) and set `degraded['recurrent_memory_layer']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - head-group routing with per-token selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - KV-cost implications and sharing strategy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality gain measurement versus dense attention | 520 | Third required mechanism. |
| 6 | Core implementation D - kernel integration with the paged decode path | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0256_expert_attention.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_attention@1`.
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

### P0257 · `shared_expert` — Shared & Residual Expert Design

| field | value |
|---|---|
| part id | `P0257` (7/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0257_shared_expert.py` |
| module path | `hyperion.t06.routing.shared_expert` |
| capability published | `cap.t06.shared.shared_expert@1` |
| determinism class | `seeded` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0257_shared_expert.txt`](prompts/P0257_shared_expert.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0257-shared-expert) |

**Mission.** A always-on expert that captures common structure, letting specialists specialise.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **shared-expert sizing analysis and residual combination**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **interaction with load-balancing objectives** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **ablation showing the quality contribution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **cost accounting of the always-on path** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.shared.shared_expert@1`
- `cap.t06.shared.shared_expert.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_attention@1` | use the in-file conservative substitute for `expert_attention` (documented, slower, lower quality) and set `degraded['expert_attention']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t05.byte.byte_latent_patching@1` | use the in-file conservative substitute for `byte_latent_patching` (documented, slower, lower quality) and set `degraded['byte_latent_patching']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - shared-expert sizing analysis and residual combination | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - interaction with load-balancing objectives | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - ablation showing the quality contribution | 520 | Third required mechanism. |
| 6 | Core implementation D - cost accounting of the always-on path | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0257_shared_expert.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.shared.shared_expert@1`.
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

### P0258 · `fine_grained_experts` — Fine-Grained Expert Segmentation

| field | value |
|---|---|
| part id | `P0258` (8/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0258_fine_grained_experts.py` |
| module path | `hyperion.t06.routing.fine_grained_experts` |
| capability published | `cap.t06.fine.fine_grained_experts@1` |
| determinism class | `seeded` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0258_fine_grained_experts.txt`](prompts/P0258_fine_grained_experts.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0258-fine-grained-experts) |

**Mission.** Many small experts beat few large ones: proving and exploiting it.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **granularity sweep at matched active parameters** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **combinatorial-coverage analysis of expert combinations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **routing-overhead measurement at high expert counts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **recommended granularity with evidence**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.fine.fine_grained_experts@1`
- `cap.t06.fine.fine_grained_experts.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.shared.shared_expert@1` | use the in-file conservative substitute for `shared_expert` (documented, slower, lower quality) and set `degraded['shared_expert']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t05.world.world_model_core@1` | use the in-file conservative substitute for `world_model_core` (documented, slower, lower quality) and set `degraded['world_model_core']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - granularity sweep at matched active parameters | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - combinatorial-coverage analysis of expert combinations | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - routing-overhead measurement at high expert counts | 520 | Third required mechanism. |
| 6 | Core implementation D - recommended granularity with evidence | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0258_fine_grained_experts.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.fine.fine_grained_experts@1`.
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

### P0259 · `expert_placement` — Expert Placement & Replication Policy

| field | value |
|---|---|
| part id | `P0259` (9/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0259_expert_placement.py` |
| module path | `hyperion.t06.routing.expert_placement` |
| capability published | `cap.t06.expert.expert_placement@1` |
| determinism class | `seeded` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0259_expert_placement.txt`](prompts/P0259_expert_placement.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0259-expert-placement) |

**Mission.** Where each expert lives across the cluster, and how many copies exist.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **traffic-driven placement solver minimising all-to-all volume** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **hot-expert replication with consistency handling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **migration protocol with zero request loss**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured communication reduction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.expert.expert_placement@1`
- `cap.t06.expert.expert_placement.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.fine.fine_grained_experts@1` | use the in-file conservative substitute for `fine_grained_experts` (documented, slower, lower quality) and set `degraded['fine_grained_experts']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t05.model.model_merging@1` | use the in-file conservative substitute for `model_merging` (documented, slower, lower quality) and set `degraded['model_merging']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - traffic-driven placement solver minimising all-to-all volume | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hot-expert replication with consistency handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - migration protocol with zero request loss | 520 | Third required mechanism. |
| 6 | Core implementation D - measured communication reduction | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0259_expert_placement.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_placement@1`.
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

### P0260 · `expert_prefetch` — Expert Weight Prefetching & Caching

| field | value |
|---|---|
| part id | `P0260` (10/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0260_expert_prefetch.py` |
| module path | `hyperion.t06.routing.expert_prefetch` |
| capability published | `cap.t06.expert.expert_prefetch@1` |
| determinism class | `seeded` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0260_expert_prefetch.txt`](prompts/P0260_expert_prefetch.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0260-expert-prefetch) |

**Mission.** Streams only the experts a request will actually use.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **router-lookahead prediction of needed experts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **device-memory expert cache with cost-aware eviction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **prefetch-accuracy and stall-time measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **memory-footprint reduction at matched latency** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.expert.expert_prefetch@1`
- `cap.t06.expert.expert_prefetch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_placement@1` | use the in-file conservative substitute for `expert_placement` (documented, slower, lower quality) and set `degraded['expert_placement']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t05.logit.logit_head_design@1` | use the in-file conservative substitute for `logit_head_design` (documented, slower, lower quality) and set `degraded['logit_head_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - router-lookahead prediction of needed experts | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - device-memory expert cache with cost-aware eviction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - prefetch-accuracy and stall-time measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - memory-footprint reduction at matched latency | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0260_expert_prefetch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_prefetch@1`.
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

### P0261 · `router_lookahead` — Router Prediction & Speculative Routing

| field | value |
|---|---|
| part id | `P0261` (11/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0261_router_lookahead.py` |
| module path | `hyperion.t06.routing.router_lookahead` |
| capability published | `cap.t06.router.router_lookahead@1` |
| determinism class | `seeded` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0261_router_lookahead.txt`](prompts/P0261_router_lookahead.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0261-router-lookahead) |

**Mission.** Predicts routing before the layer runs so weights arrive in time.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **lightweight predictor from earlier-layer activations**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **speculative fetch with misprediction rollback** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **prediction accuracy per layer depth** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **latency improvement attributable to lookahead** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.router.router_lookahead@1`
- `cap.t06.router.router_lookahead.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_prefetch@1` | use the in-file conservative substitute for `expert_prefetch` (documented, slower, lower quality) and set `degraded['expert_prefetch']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t05.numerical.numerical_arch_stability@1` | use the in-file conservative substitute for `numerical_arch_stability` (documented, slower, lower quality) and set `degraded['numerical_arch_stability']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - lightweight predictor from earlier-layer activations | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - speculative fetch with misprediction rollback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - prediction accuracy per layer depth | 520 | Third required mechanism. |
| 6 | Core implementation D - latency improvement attributable to lookahead | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0261_router_lookahead.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_lookahead@1`.
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

### P0262 · `moe_determinism` — Deterministic MoE Execution

| field | value |
|---|---|
| part id | `P0262` (12/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0262_moe_determinism.py` |
| module path | `hyperion.t06.routing.moe_determinism` |
| capability published | `cap.t06.moe.moe_determinism@1` |
| determinism class | `seeded` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0262_moe_determinism.txt`](prompts/P0262_moe_determinism.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0262-moe-determinism) |

**Mission.** Same input, same experts, same bytes, regardless of batching.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **batch-invariant routing and combine ordering** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **capacity-independent result guarantees or documented exceptions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **replay verification across batch sizes and rank counts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **cost-of-determinism measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.moe.moe_determinism@1`
- `cap.t06.moe.moe_determinism.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_lookahead@1` | use the in-file conservative substitute for `router_lookahead` (documented, slower, lower quality) and set `degraded['router_lookahead']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t05.arch.arch_ablation_suite@1` | use the in-file conservative substitute for `arch_ablation_suite` (documented, slower, lower quality) and set `degraded['arch_ablation_suite']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - batch-invariant routing and combine ordering | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capacity-independent result guarantees or documented exceptions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - replay verification across batch sizes and rank counts | 520 | Third required mechanism. |
| 6 | Core implementation D - cost-of-determinism measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0262_moe_determinism.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_determinism@1`.
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

### P0263 · `expert_lifecycle` — Expert Birth, Death & Reincarnation

| field | value |
|---|---|
| part id | `P0263` (13/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0263_expert_lifecycle.py` |
| module path | `hyperion.t06.routing.expert_lifecycle` |
| capability published | `cap.t06.expert.expert_lifecycle@1` |
| determinism class | `seeded` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0263_expert_lifecycle.txt`](prompts/P0263_expert_lifecycle.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0263-expert-lifecycle) |

**Mission.** Grows and prunes the expert population over the model's life.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **utilisation-driven expert retirement with knowledge absorption** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **expert splitting when overloaded, with diversity injection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **population-size scheduling during training**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **quality trajectory across lifecycle events** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.expert.expert_lifecycle@1`
- `cap.t06.expert.expert_lifecycle.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_determinism@1` | use the in-file conservative substitute for `moe_determinism` (documented, slower, lower quality) and set `degraded['moe_determinism']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t05.state.state_space_layer@1` | use the in-file conservative substitute for `state_space_layer` (documented, slower, lower quality) and set `degraded['state_space_layer']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - utilisation-driven expert retirement with knowledge absorption | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - expert splitting when overloaded, with diversity injection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - population-size scheduling during training | 520 | Third required mechanism. |
| 6 | Core implementation D - quality trajectory across lifecycle events | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0263_expert_lifecycle.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_lifecycle@1`.
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

### P0264 · `expert_diversity` — Expert Diversity Objectives

| field | value |
|---|---|
| part id | `P0264` (14/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0264_expert_diversity.py` |
| module path | `hyperion.t06.routing.expert_diversity` |
| capability published | `cap.t06.expert.expert_diversity@1` |
| determinism class | `seeded` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0264_expert_diversity.txt`](prompts/P0264_expert_diversity.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0264-expert-diversity) |

**Mission.** Actively prevents 512 experts from converging to the same function.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **diversity metrics over weights, activations and gradients** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **orthogonality/repulsion regularisers with tuning evidence**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **collapse early-warning indicators** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured diversity-versus-quality relationship** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.expert.expert_diversity@1`
- `cap.t06.expert.expert_diversity.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_lifecycle@1` | use the in-file conservative substitute for `expert_lifecycle` (documented, slower, lower quality) and set `degraded['expert_lifecycle']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t05.tokeniser.tokeniser_omega@1` | use the in-file conservative substitute for `tokeniser_omega` (documented, slower, lower quality) and set `degraded['tokeniser_omega']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - diversity metrics over weights, activations and gradients | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - orthogonality/repulsion regularisers with tuning evidence | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - collapse early-warning indicators | 520 | Third required mechanism. |
| 6 | Core implementation D - measured diversity-versus-quality relationship | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0264_expert_diversity.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_diversity@1`.
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

### P0265 · `router_temperature` — Router Sharpness & Exploration Schedule

| field | value |
|---|---|
| part id | `P0265` (15/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0265_router_temperature.py` |
| module path | `hyperion.t06.routing.router_temperature` |
| capability published | `cap.t06.router.router_temperature@1` |
| determinism class | `seeded` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0265_router_temperature.txt`](prompts/P0265_router_temperature.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0265-router-temperature) |

**Mission.** Explores early, commits late, without instability.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **temperature/noise schedule design and justification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **exploration bonus for underused experts** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **annealing effect on final specialisation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **training-stability evidence across schedules** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.router.router_temperature@1`
- `cap.t06.router.router_temperature.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_diversity@1` | use the in-file conservative substitute for `expert_diversity` (documented, slower, lower quality) and set `degraded['expert_diversity']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t05.uncertainty.uncertainty_calibration@1` | use the in-file conservative substitute for `uncertainty_calibration` (documented, slower, lower quality) and set `degraded['uncertainty_calibration']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - temperature/noise schedule design and justification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - exploration bonus for underused experts | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - annealing effect on final specialisation | 520 | Third required mechanism. |
| 6 | Core implementation D - training-stability evidence across schedules | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0265_router_temperature.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_temperature@1`.
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

### P0266 · `sparse_activation_stats` — Sparse Activation Statistics & Diagnostics

| field | value |
|---|---|
| part id | `P0266` (16/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0266_sparse_activation_stats.py` |
| module path | `hyperion.t06.routing.sparse_activation_stats` |
| capability published | `cap.t06.sparse.sparse_activation_stats@1` |
| determinism class | `seeded` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0266_sparse_activation_stats.txt`](prompts/P0266_sparse_activation_stats.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0266-sparse-activation-stats) |

**Mission.** The observability layer for conditional compute.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **per-expert utilisation, entropy and co-activation statistics** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **drift detection over traffic distribution shifts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **diagnostic report with actionable remediation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **overhead under 0.5% of step time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.sparse.sparse_activation_stats@1`
- `cap.t06.sparse.sparse_activation_stats.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_temperature@1` | use the in-file conservative substitute for `router_temperature` (documented, slower, lower quality) and set `degraded['router_temperature']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t05.knowledge.knowledge_editing@1` | use the in-file conservative substitute for `knowledge_editing` (documented, slower, lower quality) and set `degraded['knowledge_editing']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-expert utilisation, entropy and co-activation statistics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - drift detection over traffic distribution shifts | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - diagnostic report with actionable remediation | 520 | Third required mechanism. |
| 6 | Core implementation D - overhead under 0.5% of step time | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0266_sparse_activation_stats.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.sparse.sparse_activation_stats@1`.
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

### P0267 · `moe_quantisation` — Per-Expert Quantisation Strategy

| field | value |
|---|---|
| part id | `P0267` (17/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0267_moe_quantisation.py` |
| module path | `hyperion.t06.routing.moe_quantisation` |
| capability published | `cap.t06.moe.moe_quantisation@1` |
| determinism class | `seeded` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0267_moe_quantisation.txt`](prompts/P0267_moe_quantisation.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0267-moe-quantisation) |

**Mission.** Cheap experts where possible, precise experts where necessary.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **per-expert sensitivity analysis and precision assignment** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **mixed-precision expert pool with routing awareness** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **accuracy verification per assignment plan**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured memory and bandwidth savings** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.moe.moe_quantisation@1`
- `cap.t06.moe.moe_quantisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.sparse.sparse_activation_stats@1` | use the in-file conservative substitute for `sparse_activation_stats` (documented, slower, lower quality) and set `degraded['sparse_activation_stats']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t05.residual.residual_stream_design@1` | use the in-file conservative substitute for `residual_stream_design` (documented, slower, lower quality) and set `degraded['residual_stream_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-expert sensitivity analysis and precision assignment | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mixed-precision expert pool with routing awareness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accuracy verification per assignment plan | 520 | Third required mechanism. |
| 6 | Core implementation D - measured memory and bandwidth savings | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0267_moe_quantisation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_quantisation@1`.
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

### P0268 · `expert_offload` — Expert Offloading to Host/Storage

| field | value |
|---|---|
| part id | `P0268` (18/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0268_expert_offload.py` |
| module path | `hyperion.t06.routing.expert_offload` |
| capability published | `cap.t06.expert.expert_offload@1` |
| determinism class | `seeded` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0268_expert_offload.txt`](prompts/P0268_expert_offload.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0268-expert-offload) |

**Mission.** Serves 512-expert models on limited device memory.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **residency tiering driven by access frequency** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **asynchronous fetch overlapped with earlier layers**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **worst-case latency bound under cold experts** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **memory-reduction versus latency-cost curve** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.expert.expert_offload@1`
- `cap.t06.expert.expert_offload.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_quantisation@1` | use the in-file conservative substitute for `moe_quantisation` (documented, slower, lower quality) and set `degraded['moe_quantisation']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t05.model.model_surgery@1` | use the in-file conservative substitute for `model_surgery` (documented, slower, lower quality) and set `degraded['model_surgery']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - residency tiering driven by access frequency | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - asynchronous fetch overlapped with earlier layers | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - worst-case latency bound under cold experts | 520 | Third required mechanism. |
| 6 | Core implementation D - memory-reduction versus latency-cost curve | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0268_expert_offload.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_offload@1`.
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

### P0269 · `moe_batching` — MoE-Aware Request Batching

| field | value |
|---|---|
| part id | `P0269` (19/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0269_moe_batching.py` |
| module path | `hyperion.t06.routing.moe_batching` |
| capability published | `cap.t06.moe.moe_batching@1` |
| determinism class | `seeded` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0269_moe_batching.txt`](prompts/P0269_moe_batching.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0269-moe-batching) |

**Mission.** Groups requests so their expert demands overlap.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **batching policy using predicted expert sets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **affinity grouping with fairness constraints** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **throughput improvement measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **latency-fairness tradeoff analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.moe.moe_batching@1`
- `cap.t06.moe.moe_batching.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_offload@1` | use the in-file conservative substitute for `expert_offload` (documented, slower, lower quality) and set `degraded['expert_offload']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t05.reference.reference_forward@1` | use the in-file conservative substitute for `reference_forward` (documented, slower, lower quality) and set `degraded['reference_forward']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - batching policy using predicted expert sets | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - affinity grouping with fairness constraints | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - throughput improvement measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - latency-fairness tradeoff analysis | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0269_moe_batching.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_batching@1`.
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

### P0270 · `token_dropping` — Token Dropping & Early Exit Policy

| field | value |
|---|---|
| part id | `P0270` (20/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0270_token_dropping.py` |
| module path | `hyperion.t06.routing.token_dropping` |
| capability published | `cap.t06.token.token_dropping@1` |
| determinism class | `seeded` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0270_token_dropping.txt`](prompts/P0270_token_dropping.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0270-token-dropping) |

**Mission.** Spends compute only where it changes the answer.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **token-importance scoring with calibrated thresholds** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **safe-drop guarantees for structurally critical tokens** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **quality impact measurement at multiple drop rates** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **interaction with adaptive depth**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.token.token_dropping@1`
- `cap.t06.token.token_dropping.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_batching@1` | use the in-file conservative substitute for `moe_batching` (documented, slower, lower quality) and set `degraded['moe_batching']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t05.kv.kv_compression_model@1` | use the in-file conservative substitute for `kv_compression_model` (documented, slower, lower quality) and set `degraded['kv_compression_model']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - token-importance scoring with calibrated thresholds | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - safe-drop guarantees for structurally critical tokens | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality impact measurement at multiple drop rates | 520 | Third required mechanism. |
| 6 | Core implementation D - interaction with adaptive depth | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0270_token_dropping.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.token.token_dropping@1`.
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

### P0271 · `conditional_layers` — Layer Skipping & Conditional Depth Routing

| field | value |
|---|---|
| part id | `P0271` (21/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0271_conditional_layers.py` |
| module path | `hyperion.t06.routing.conditional_layers` |
| capability published | `cap.t06.conditional.conditional_layers@1` |
| determinism class | `seeded` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0271_conditional_layers.txt`](prompts/P0271_conditional_layers.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0271-conditional-layers) |

**Mission.** Whole layers become optional for easy inputs.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **layer-skip policy learning with a compute budget** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **skip-pattern regularisation for cache friendliness** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **worst-case-quality guardrails**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured FLOP reduction at matched accuracy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.conditional.conditional_layers@1`
- `cap.t06.conditional.conditional_layers.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.token.token_dropping@1` | use the in-file conservative substitute for `token_dropping` (documented, slower, lower quality) and set `degraded['token_dropping']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t05.embedding.embedding_design@1` | use the in-file conservative substitute for `embedding_design` (documented, slower, lower quality) and set `degraded['embedding_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - layer-skip policy learning with a compute budget | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - skip-pattern regularisation for cache friendliness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - worst-case-quality guardrails | 520 | Third required mechanism. |
| 6 | Core implementation D - measured FLOP reduction at matched accuracy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0271_conditional_layers.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.conditional.conditional_layers@1`.
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

### P0272 · `mod_routing` — Mixture-of-Depths Routing

| field | value |
|---|---|
| part id | `P0272` (22/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0272_mod_routing.py` |
| module path | `hyperion.t06.routing.mod_routing` |
| capability published | `cap.t06.mod.mod_routing@1` |
| determinism class | `seeded` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0272_mod_routing.txt`](prompts/P0272_mod_routing.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0272-mod-routing) |

**Mission.** Routes only a fraction of tokens through each heavy block.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **per-block token selection with capacity guarantees** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **static-shape formulation for kernel efficiency**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **quality-versus-fraction curves** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **kernel-level speedup verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.mod.mod_routing@1`
- `cap.t06.mod.mod_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.conditional.conditional_layers@1` | use the in-file conservative substitute for `conditional_layers` (documented, slower, lower quality) and set `degraded['conditional_layers']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t05.verifier.verifier_head@1` | use the in-file conservative substitute for `verifier_head` (documented, slower, lower quality) and set `degraded['verifier_head']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-block token selection with capacity guarantees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - static-shape formulation for kernel efficiency | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality-versus-fraction curves | 520 | Third required mechanism. |
| 6 | Core implementation D - kernel-level speedup verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0272_mod_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.mod.mod_routing@1`.
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

### P0273 · `router_robustness` — Router Adversarial Robustness

| field | value |
|---|---|
| part id | `P0273` (23/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0273_router_robustness.py` |
| module path | `hyperion.t06.routing.router_robustness` |
| capability published | `cap.t06.router.router_robustness@1` |
| determinism class | `seeded` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0273_router_robustness.txt`](prompts/P0273_router_robustness.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0273-router-robustness) |

**Mission.** Stops crafted inputs from steering compute or leaking routing information.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **adversarial routing attack construction and defence**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **routing-side-channel analysis and mitigation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **input-perturbation sensitivity measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **defence effectiveness evaluation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.router.router_robustness@1`
- `cap.t06.router.router_robustness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.mod.mod_routing@1` | use the in-file conservative substitute for `mod_routing` (documented, slower, lower quality) and set `degraded['mod_routing']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t05.continual.continual_learning@1` | use the in-file conservative substitute for `continual_learning` (documented, slower, lower quality) and set `degraded['continual_learning']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - adversarial routing attack construction and defence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - routing-side-channel analysis and mitigation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - input-perturbation sensitivity measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - defence effectiveness evaluation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0273_router_robustness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_robustness@1`.
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

### P0274 · `gating_alternatives` — Alternative Gating Mechanisms

| field | value |
|---|---|
| part id | `P0274` (24/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0274_gating_alternatives.py` |
| module path | `hyperion.t06.routing.gating_alternatives` |
| capability published | `cap.t06.gating.gating_alternatives@1` |
| determinism class | `seeded` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0274_gating_alternatives.txt`](prompts/P0274_gating_alternatives.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0274-gating-alternatives) |

**Mission.** Sinkhorn, expert-choice, soft-merge and hash gating, compared fairly.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **implementation of four gating families behind one interface** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **matched-budget quality and latency comparison** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **stability and determinism properties per family** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **recommendation with evidence**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.gating.gating_alternatives@1`
- `cap.t06.gating.gating_alternatives.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_robustness@1` | use the in-file conservative substitute for `router_robustness` (documented, slower, lower quality) and set `degraded['router_robustness']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t05.depth.depth_width_tradeoff@1` | use the in-file conservative substitute for `depth_width_tradeoff` (documented, slower, lower quality) and set `degraded['depth_width_tradeoff']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - implementation of four gating families behind one interface | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - matched-budget quality and latency comparison | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - stability and determinism properties per family | 520 | Third required mechanism. |
| 6 | Core implementation D - recommendation with evidence | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0274_gating_alternatives.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.gating.gating_alternatives@1`.
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

### P0275 · `expert_choice_routing` — Expert-Choice Routing

| field | value |
|---|---|
| part id | `P0275` (25/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0275_expert_choice_routing.py` |
| module path | `hyperion.t06.routing.expert_choice_routing` |
| capability published | `cap.t06.expert.expert_choice_routing@1` |
| determinism class | `seeded` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0275_expert_choice_routing.txt`](prompts/P0275_expert_choice_routing.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0275-expert-choice-routing) |

**Mission.** Experts pick tokens: perfect balance by construction.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **expert-choice assignment with capacity-exact selection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **causality preservation in autoregressive decoding** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **quality comparison against token-choice routing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **throughput measurement under skew** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.expert.expert_choice_routing@1`
- `cap.t06.expert.expert_choice_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.gating.gating_alternatives@1` | use the in-file conservative substitute for `gating_alternatives` (documented, slower, lower quality) and set `degraded['gating_alternatives']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t05.sparse.sparse_upcycling@1` | use the in-file conservative substitute for `sparse_upcycling` (documented, slower, lower quality) and set `degraded['sparse_upcycling']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - expert-choice assignment with capacity-exact selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - causality preservation in autoregressive decoding | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality comparison against token-choice routing | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput measurement under skew | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0275_expert_choice_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_choice_routing@1`.
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

### P0276 · `moe_scaling_laws` — MoE Scaling Laws & Budget Allocation

| field | value |
|---|---|
| part id | `P0276` (26/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0276_moe_scaling_laws.py` |
| module path | `hyperion.t06.routing.moe_scaling_laws` |
| capability published | `cap.t06.moe.moe_scaling_laws@1` |
| determinism class | `seeded` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0276_moe_scaling_laws.txt`](prompts/P0276_moe_scaling_laws.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0276-moe-scaling-laws) |

**Mission.** Predicts the best (experts, granularity, active-params) point.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **scaling-law fits over expert count and granularity** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **compute-optimal sparsity derivation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **extrapolation confidence intervals** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **validation on held-out configurations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.moe.moe_scaling_laws@1`
- `cap.t06.moe.moe_scaling_laws.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_choice_routing@1` | use the in-file conservative substitute for `expert_choice_routing` (documented, slower, lower quality) and set `degraded['expert_choice_routing']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t05.model.model_config_schema@1` | use the in-file conservative substitute for `model_config_schema` (documented, slower, lower quality) and set `degraded['model_config_schema']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - scaling-law fits over expert count and granularity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compute-optimal sparsity derivation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - extrapolation confidence intervals | 520 | Third required mechanism. |
| 6 | Core implementation D - validation on held-out configurations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0276_moe_scaling_laws.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_scaling_laws@1`.
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

### P0277 · `router_interpretability` — Router Interpretability & Expert Naming

| field | value |
|---|---|
| part id | `P0277` (27/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0277_router_interpretability.py` |
| module path | `hyperion.t06.routing.router_interpretability` |
| capability published | `cap.t06.router.router_interpretability@1` |
| determinism class | `seeded` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0277_router_interpretability.txt`](prompts/P0277_router_interpretability.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0277-router-interpretability) |

**Mission.** Explains what each of 512 experts is for, in words.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **activation-clustering and exemplar extraction per expert**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **automatic expert labelling with verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **routing-decision explanation for a given token** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **label-accuracy human-agreement measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.router.router_interpretability@1`
- `cap.t06.router.router_interpretability.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_scaling_laws@1` | use the in-file conservative substitute for `moe_scaling_laws` (documented, slower, lower quality) and set `degraded['moe_scaling_laws']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t05.attention.attention_variants@1` | use the in-file conservative substitute for `attention_variants` (documented, slower, lower quality) and set `degraded['attention_variants']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - activation-clustering and exemplar extraction per expert | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automatic expert labelling with verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - routing-decision explanation for a given token | 520 | Third required mechanism. |
| 6 | Core implementation D - label-accuracy human-agreement measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0277_router_interpretability.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_interpretability@1`.
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

### P0278 · `moe_training_stability` — MoE Training Stability Engineering

| field | value |
|---|---|
| part id | `P0278` (28/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0278_moe_training_stability.py` |
| module path | `hyperion.t06.routing.moe_training_stability` |
| capability published | `cap.t06.moe.moe_training_stability@1` |
| determinism class | `seeded` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0278_moe_training_stability.txt`](prompts/P0278_moe_training_stability.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0278-moe-training-stability) |

**Mission.** Sparse models are fragile; this part makes them not.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **router z-loss and logit-clipping with tuning evidence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **gradient-spike detection and rollback** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **precision requirements for the routing path** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **long-run stability evidence at scale**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.moe.moe_training_stability@1`
- `cap.t06.moe.moe_training_stability.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_interpretability@1` | use the in-file conservative substitute for `router_interpretability` (documented, slower, lower quality) and set `degraded['router_interpretability']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t05.activation.activation_design@1` | use the in-file conservative substitute for `activation_design` (documented, slower, lower quality) and set `degraded['activation_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - router z-loss and logit-clipping with tuning evidence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - gradient-spike detection and rollback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - precision requirements for the routing path | 520 | Third required mechanism. |
| 6 | Core implementation D - long-run stability evidence at scale | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0278_moe_training_stability.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_training_stability@1`.
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

### P0279 · `expert_dropout` — Expert Dropout & Robustness to Missing Experts

| field | value |
|---|---|
| part id | `P0279` (29/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0279_expert_dropout.py` |
| module path | `hyperion.t06.routing.expert_dropout` |
| capability published | `cap.t06.expert.expert_dropout@1` |
| determinism class | `seeded` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0279_expert_dropout.txt`](prompts/P0279_expert_dropout.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0279-expert-dropout) |

**Mission.** The model still works when some experts are unavailable.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **expert-dropout training for graceful degradation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **quality curves versus fraction of missing experts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **automatic rerouting on expert failure**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **failure-mode testing under device loss** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.expert.expert_dropout@1`
- `cap.t06.expert.expert_dropout.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_training_stability@1` | use the in-file conservative substitute for `moe_training_stability` (documented, slower, lower quality) and set `degraded['moe_training_stability']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t05.draft.draft_model_arch@1` | use the in-file conservative substitute for `draft_model_arch` (documented, slower, lower quality) and set `degraded['draft_model_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - expert-dropout training for graceful degradation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quality curves versus fraction of missing experts | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic rerouting on expert failure | 520 | Third required mechanism. |
| 6 | Core implementation D - failure-mode testing under device loss | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0279_expert_dropout.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_dropout@1`.
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

### P0280 · `sparse_kernels_bridge` — Routing-to-Kernel Bridge

| field | value |
|---|---|
| part id | `P0280` (30/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0280_sparse_kernels_bridge.py` |
| module path | `hyperion.t06.routing.sparse_kernels_bridge` |
| capability published | `cap.t06.sparse.sparse_kernels_bridge@1` |
| determinism class | `seeded` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0280_sparse_kernels_bridge.txt`](prompts/P0280_sparse_kernels_bridge.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0280-sparse-kernels-bridge) |

**Mission.** Turns routing decisions into efficient grouped-GEMM invocations.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **permutation/index construction fused with routing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **group-descriptor generation for the T02 grouped kernels**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **index-build overhead measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **end-to-end MoE layer latency budget enforcement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.sparse.sparse_kernels_bridge@1`
- `cap.t06.sparse.sparse_kernels_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_dropout@1` | use the in-file conservative substitute for `expert_dropout` (documented, slower, lower quality) and set `degraded['expert_dropout']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t05.meta.meta_learning_arch@1` | use the in-file conservative substitute for `meta_learning_arch` (documented, slower, lower quality) and set `degraded['meta_learning_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - permutation/index construction fused with routing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - group-descriptor generation for the T02 grouped kernels | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - index-build overhead measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - end-to-end MoE layer latency budget enforcement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0280_sparse_kernels_bridge.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.sparse.sparse_kernels_bridge@1`.
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

### P0281 · `modality_routing` — Modality- & Language-Aware Routing

| field | value |
|---|---|
| part id | `P0281` (31/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0281_modality_routing.py` |
| module path | `hyperion.t06.routing.modality_routing` |
| capability published | `cap.t06.modality.modality_routing@1` |
| determinism class | `seeded` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0281_modality_routing.txt`](prompts/P0281_modality_routing.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0281-modality-routing) |

**Mission.** Sends image, audio, code and language tokens to the right specialists.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **modality tag propagation into the routing decision**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **language-family expert allocation with fairness measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cross-modal expert sharing analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **per-modality quality measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.modality.modality_routing@1`
- `cap.t06.modality.modality_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.sparse.sparse_kernels_bridge@1` | use the in-file conservative substitute for `sparse_kernels_bridge` (documented, slower, lower quality) and set `degraded['sparse_kernels_bridge']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t05.architecture.architecture_search@1` | use the in-file conservative substitute for `architecture_search` (documented, slower, lower quality) and set `degraded['architecture_search']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - modality tag propagation into the routing decision | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - language-family expert allocation with fairness measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cross-modal expert sharing analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - per-modality quality measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0281_modality_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.modality.modality_routing@1`.
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

### P0282 · `difficulty_routing` — Difficulty-Aware Compute Routing

| field | value |
|---|---|
| part id | `P0282` (32/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0282_difficulty_routing.py` |
| module path | `hyperion.t06.routing.difficulty_routing` |
| capability published | `cap.t06.difficulty.difficulty_routing@1` |
| determinism class | `seeded` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0282_difficulty_routing.txt`](prompts/P0282_difficulty_routing.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0282-difficulty-routing) |

**Mission.** Predicts problem hardness and allocates compute accordingly.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **difficulty estimator trained on solve-rate labels** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **compute-allocation policy under a global budget** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **calibration of difficulty predictions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured accuracy-per-FLOP improvement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.difficulty.difficulty_routing@1`
- `cap.t06.difficulty.difficulty_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.modality.modality_routing@1` | use the in-file conservative substitute for `modality_routing` (documented, slower, lower quality) and set `degraded['modality_routing']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t05.speculative.speculative_arch_hooks@1` | use the in-file conservative substitute for `speculative_arch_hooks` (documented, slower, lower quality) and set `degraded['speculative_arch_hooks']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - difficulty estimator trained on solve-rate labels | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compute-allocation policy under a global budget | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - calibration of difficulty predictions | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy-per-FLOP improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0282_difficulty_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.difficulty.difficulty_routing@1`.
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

### P0283 · `cost_aware_routing` — Cost- & SLO-Aware Routing Policy

| field | value |
|---|---|
| part id | `P0283` (33/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0283_cost_aware_routing.py` |
| module path | `hyperion.t06.routing.cost_aware_routing` |
| capability published | `cap.t06.cost.cost_aware_routing@1` |
| determinism class | `seeded` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0283_cost_aware_routing.txt`](prompts/P0283_cost_aware_routing.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0283-cost-aware-routing) |

**Mission.** Routes for dollars and deadlines, not only accuracy.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-objective routing with explicit price of quality** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **SLO-class-specific policies with admission control** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cost-per-solved-task accounting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **Pareto-frontier measurement versus fixed policies** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.cost.cost_aware_routing@1`
- `cap.t06.cost.cost_aware_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.difficulty.difficulty_routing@1` | use the in-file conservative substitute for `difficulty_routing` (documented, slower, lower quality) and set `degraded['difficulty_routing']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t05.expert.expert_specialisation@1` | use the in-file conservative substitute for `expert_specialisation` (documented, slower, lower quality) and set `degraded['expert_specialisation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-objective routing with explicit price of quality | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - SLO-class-specific policies with admission control | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost-per-solved-task accounting | 520 | Third required mechanism. |
| 6 | Core implementation D - Pareto-frontier measurement versus fixed policies | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0283_cost_aware_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.cost.cost_aware_routing@1`.
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

### P0284 · `model_cascade_routing` — Model Cascade & Escalation Router

| field | value |
|---|---|
| part id | `P0284` (34/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0284_model_cascade_routing.py` |
| module path | `hyperion.t06.routing.model_cascade_routing` |
| capability published | `cap.t06.model.model_cascade_routing@1` |
| determinism class | `seeded` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0284_model_cascade_routing.txt`](prompts/P0284_model_cascade_routing.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0284-model-cascade-routing) |

**Mission.** Cheap model first, escalate only when the verifier is unsure.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **cascade tier definition with calibrated escalation thresholds** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **escalation-policy optimisation under cost constraints**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **quality-preservation proof versus always-large routing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured cost reduction at matched accuracy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.model.model_cascade_routing@1`
- `cap.t06.model.model_cascade_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.cost.cost_aware_routing@1` | use the in-file conservative substitute for `cost_aware_routing` (documented, slower, lower quality) and set `degraded['cost_aware_routing']='local'` |
| `cap.t05.hybrid.hybrid_mixer@1` | use the in-file conservative substitute for `hybrid_mixer` (documented, slower, lower quality) and set `degraded['hybrid_mixer']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cascade tier definition with calibrated escalation thresholds | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - escalation-policy optimisation under cost constraints | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality-preservation proof versus always-large routing | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cost reduction at matched accuracy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0284_model_cascade_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.model.model_cascade_routing@1`.
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

### P0285 · `ensemble_combiner` — Ensemble & Multi-Sample Combination

| field | value |
|---|---|
| part id | `P0285` (35/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0285_ensemble_combiner.py` |
| module path | `hyperion.t06.routing.ensemble_combiner` |
| capability published | `cap.t06.ensemble.ensemble_combiner@1` |
| determinism class | `seeded` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0285_ensemble_combiner.txt`](prompts/P0285_ensemble_combiner.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0285-ensemble-combiner) |

**Mission.** Turns several cheap samples into one better answer.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **self-consistency, weighted voting and verifier-ranked selection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **diversity-inducing sampling policies** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **cost-versus-accuracy curves for sample counts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **when-not-to-ensemble decision rule** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.ensemble.ensemble_combiner@1`
- `cap.t06.ensemble.ensemble_combiner.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.model.model_cascade_routing@1` | use the in-file conservative substitute for `model_cascade_routing` (documented, slower, lower quality) and set `degraded['model_cascade_routing']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t05.normalisation.normalisation_design@1` | use the in-file conservative substitute for `normalisation_design` (documented, slower, lower quality) and set `degraded['normalisation_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - self-consistency, weighted voting and verifier-ranked selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - diversity-inducing sampling policies | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost-versus-accuracy curves for sample counts | 520 | Third required mechanism. |
| 6 | Core implementation D - when-not-to-ensemble decision rule | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0285_ensemble_combiner.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.ensemble.ensemble_combiner@1`.
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

### P0286 · `router_cache` — Routing Decision Cache

| field | value |
|---|---|
| part id | `P0286` (36/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0286_router_cache.py` |
| module path | `hyperion.t06.routing.router_cache` |
| capability published | `cap.t06.router.router_cache@1` |
| determinism class | `seeded` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0286_router_cache.txt`](prompts/P0286_router_cache.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0286-router-cache) |

**Mission.** Reuses routing decisions for repeated prefixes (feeds S4).

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **prefix-keyed routing cache with invalidation rules** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **hit-rate measurement on production-like traffic** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **correctness verification of cached routing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **latency saving attribution**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.router.router_cache@1`
- `cap.t06.router.router_cache.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.ensemble.ensemble_combiner@1` | use the in-file conservative substitute for `ensemble_combiner` (documented, slower, lower quality) and set `degraded['ensemble_combiner']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t05.multi.multi_token_prediction@1` | use the in-file conservative substitute for `multi_token_prediction` (documented, slower, lower quality) and set `degraded['multi_token_prediction']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - prefix-keyed routing cache with invalidation rules | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hit-rate measurement on production-like traffic | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - correctness verification of cached routing | 520 | Third required mechanism. |
| 6 | Core implementation D - latency saving attribution | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0286_router_cache.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_cache@1`.
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

### P0287 · `expert_warmup` — Expert Warmup & Cold-Start Handling

| field | value |
|---|---|
| part id | `P0287` (37/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0287_expert_warmup.py` |
| module path | `hyperion.t06.routing.expert_warmup` |
| capability published | `cap.t06.expert.expert_warmup@1` |
| determinism class | `seeded` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0287_expert_warmup.txt`](prompts/P0287_expert_warmup.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0287-expert-warmup) |

**Mission.** Avoids first-request latency cliffs.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **predictive warmup from traffic forecasts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cold-expert latency measurement and mitigation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **warmup cost budgeting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **p99 improvement measurement after warmup** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.expert.expert_warmup@1`
- `cap.t06.expert.expert_warmup.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_cache@1` | use the in-file conservative substitute for `router_cache` (documented, slower, lower quality) and set `degraded['router_cache']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t05.program.program_induction_arch@1` | use the in-file conservative substitute for `program_induction_arch` (documented, slower, lower quality) and set `degraded['program_induction_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - predictive warmup from traffic forecasts | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cold-expert latency measurement and mitigation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - warmup cost budgeting | 520 | Third required mechanism. |
| 6 | Core implementation D - p99 improvement measurement after warmup | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0287_expert_warmup.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_warmup@1`.
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

### P0288 · `routing_fairness` — Cross-User Routing Fairness & Isolation

| field | value |
|---|---|
| part id | `P0288` (38/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0288_routing_fairness.py` |
| module path | `hyperion.t06.routing.routing_fairness` |
| capability published | `cap.t06.routing.routing_fairness@1` |
| determinism class | `seeded` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0288_routing_fairness.txt`](prompts/P0288_routing_fairness.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0288-routing-fairness) |

**Mission.** One user's traffic must not degrade another's routing quality.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **per-tenant expert-utilisation accounting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **fairness enforcement in capacity allocation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **isolation verification under adversarial load** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **fairness metric reporting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.routing.routing_fairness@1`
- `cap.t06.routing.routing_fairness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_warmup@1` | use the in-file conservative substitute for `expert_warmup` (documented, slower, lower quality) and set `degraded['expert_warmup']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t05.init.init_scaling_laws@1` | use the in-file conservative substitute for `init_scaling_laws` (documented, slower, lower quality) and set `degraded['init_scaling_laws']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-tenant expert-utilisation accounting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fairness enforcement in capacity allocation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - isolation verification under adversarial load | 520 | Third required mechanism. |
| 6 | Core implementation D - fairness metric reporting | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0288_routing_fairness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.routing.routing_fairness@1`.
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

### P0289 · `moe_memory_budget` — MoE Memory Budget Planner

| field | value |
|---|---|
| part id | `P0289` (39/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0289_moe_memory_budget.py` |
| module path | `hyperion.t06.routing.moe_memory_budget` |
| capability published | `cap.t06.moe.moe_memory_budget@1` |
| determinism class | `seeded` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0289_moe_memory_budget.txt`](prompts/P0289_moe_memory_budget.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0289-moe-memory-budget) |

**Mission.** Fits a sparse model into a fixed memory envelope, optimally.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **placement/precision/offload joint optimisation under a memory cap**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **feasibility checking with clear infeasibility explanations** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **plan quality versus exhaustive search on small cases** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured quality at multiple memory budgets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.moe.moe_memory_budget@1`
- `cap.t06.moe.moe_memory_budget.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.routing.routing_fairness@1` | use the in-file conservative substitute for `routing_fairness` (documented, slower, lower quality) and set `degraded['routing_fairness']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t05.memory.memory_attention_bridge@1` | use the in-file conservative substitute for `memory_attention_bridge` (documented, slower, lower quality) and set `degraded['memory_attention_bridge']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - placement/precision/offload joint optimisation under a memory ca | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - feasibility checking with clear infeasibility explanations | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - plan quality versus exhaustive search on small cases | 520 | Third required mechanism. |
| 6 | Core implementation D - measured quality at multiple memory budgets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0289_moe_memory_budget.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_memory_budget@1`.
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

### P0290 · `router_online_learning` — Online Router Adaptation

| field | value |
|---|---|
| part id | `P0290` (40/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0290_router_online_learning.py` |
| module path | `hyperion.t06.routing.router_online_learning` |
| capability published | `cap.t06.router.router_online_learning@1` |
| determinism class | `seeded` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0290_router_online_learning.txt`](prompts/P0290_router_online_learning.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0290-router-online-learning) |

**Mission.** The router keeps improving from production feedback, safely.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **bandit-style online updates with guardrails and rollback** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **distribution-shift detection triggering adaptation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **safety constraints preventing quality regression** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured improvement over a frozen router**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.router.router_online_learning@1`
- `cap.t06.router.router_online_learning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_memory_budget@1` | use the in-file conservative substitute for `moe_memory_budget` (documented, slower, lower quality) and set `degraded['moe_memory_budget']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t05.thought.thought_representation@1` | use the in-file conservative substitute for `thought_representation` (documented, slower, lower quality) and set `degraded['thought_representation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - bandit-style online updates with guardrails and rollback | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - distribution-shift detection triggering adaptation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - safety constraints preventing quality regression | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement over a frozen router | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0290_router_online_learning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_online_learning@1`.
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

### P0291 · `sparse_gradient` — Sparse Gradient Handling & Accumulation

| field | value |
|---|---|
| part id | `P0291` (41/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0291_sparse_gradient.py` |
| module path | `hyperion.t06.routing.sparse_gradient` |
| capability published | `cap.t06.sparse.sparse_gradient@1` |
| determinism class | `seeded` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0291_sparse_gradient.txt`](prompts/P0291_sparse_gradient.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0291-sparse-gradient) |

**Mission.** Correct, efficient gradients through discrete routing.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **gradient routing with correct expert attribution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **sparse accumulation with deterministic ordering** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **gradient-correctness verification versus dense reference**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **throughput measurement of the backward path** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.sparse.sparse_gradient@1`
- `cap.t06.sparse.sparse_gradient.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_online_learning@1` | use the in-file conservative substitute for `router_online_learning` (documented, slower, lower quality) and set `degraded['router_online_learning']='local'` |
| `cap.t05.omega.omega_block@1` | use the in-file conservative substitute for `omega_block` (documented, slower, lower quality) and set `degraded['omega_block']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gradient routing with correct expert attribution | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sparse accumulation with deterministic ordering | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - gradient-correctness verification versus dense reference | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput measurement of the backward path | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0291_sparse_gradient.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.sparse.sparse_gradient@1`.
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

### P0292 · `expert_alignment` — Per-Expert Safety & Alignment Auditing

| field | value |
|---|---|
| part id | `P0292` (42/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0292_expert_alignment.py` |
| module path | `hyperion.t06.routing.expert_alignment` |
| capability published | `cap.t06.expert.expert_alignment@1` |
| determinism class | `seeded` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0292_expert_alignment.txt`](prompts/P0292_expert_alignment.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0292-expert-alignment) |

**Mission.** No expert becomes a loophole in the safety system.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **per-expert behavioural audit with targeted probes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **detection of experts that disproportionately produce refusable content**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **expert-level intervention and retraining protocol** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **audit coverage report over all 512 experts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.expert.expert_alignment@1`
- `cap.t06.expert.expert_alignment.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.sparse.sparse_gradient@1` | use the in-file conservative substitute for `sparse_gradient` (documented, slower, lower quality) and set `degraded['sparse_gradient']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t05.adaptive.adaptive_depth@1` | use the in-file conservative substitute for `adaptive_depth` (documented, slower, lower quality) and set `degraded['adaptive_depth']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-expert behavioural audit with targeted probes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - detection of experts that disproportionately produce refusable c | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - expert-level intervention and retraining protocol | 520 | Third required mechanism. |
| 6 | Core implementation D - audit coverage report over all 512 experts | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0292_expert_alignment.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.expert.expert_alignment@1`.
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

### P0293 · `routing_privacy` — Routing Privacy & Side-Channel Defence

| field | value |
|---|---|
| part id | `P0293` (43/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0293_routing_privacy.py` |
| module path | `hyperion.t06.routing.routing_privacy` |
| capability published | `cap.t06.routing.routing_privacy@1` |
| determinism class | `seeded` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0293_routing_privacy.txt`](prompts/P0293_routing_privacy.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0293-routing-privacy) |

**Mission.** Routing patterns must not leak user content.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **information-leakage quantification from routing traces**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **noise/padding defences with utility cost measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **telemetry redaction policy for routing data** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **attack-simulation results** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.routing.routing_privacy@1`
- `cap.t06.routing.routing_privacy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.expert.expert_alignment@1` | use the in-file conservative substitute for `expert_alignment` (documented, slower, lower quality) and set `degraded['expert_alignment']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t05.long.long_context_arch@1` | use the in-file conservative substitute for `long_context_arch` (documented, slower, lower quality) and set `degraded['long_context_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - information-leakage quantification from routing traces | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - noise/padding defences with utility cost measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - telemetry redaction policy for routing data | 520 | Third required mechanism. |
| 6 | Core implementation D - attack-simulation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0293_routing_privacy.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.routing.routing_privacy@1`.
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

### P0294 · `hierarchical_routing` — Hierarchical Two-Level Routing

| field | value |
|---|---|
| part id | `P0294` (44/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0294_hierarchical_routing.py` |
| module path | `hyperion.t06.routing.hierarchical_routing` |
| capability published | `cap.t06.hierarchical.hierarchical_routing@1` |
| determinism class | `seeded` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0294_hierarchical_routing.txt`](prompts/P0294_hierarchical_routing.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0294-hierarchical-routing) |

**Mission.** Route to a group, then to an expert: scales to 100k experts.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **group-then-expert routing with balanced group assignment** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **communication savings from group locality** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **quality comparison against flat routing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **scalability measurement at very high expert counts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.hierarchical.hierarchical_routing@1`
- `cap.t06.hierarchical.hierarchical_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.routing.routing_privacy@1` | use the in-file conservative substitute for `routing_privacy` (documented, slower, lower quality) and set `degraded['routing_privacy']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t05.symbolic.symbolic_bridge@1` | use the in-file conservative substitute for `symbolic_bridge` (documented, slower, lower quality) and set `degraded['symbolic_bridge']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - group-then-expert routing with balanced group assignment | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - communication savings from group locality | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality comparison against flat routing | 520 | Third required mechanism. |
| 6 | Core implementation D - scalability measurement at very high expert counts | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0294_hierarchical_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.hierarchical.hierarchical_routing@1`.
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

### P0295 · `router_bench` — Routing Benchmark & Regression Suite

| field | value |
|---|---|
| part id | `P0295` (45/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0295_router_bench.py` |
| module path | `hyperion.t06.routing.router_bench` |
| capability published | `cap.t06.router.router_bench@1` |
| determinism class | `seeded` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0295_router_bench.txt`](prompts/P0295_router_bench.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0295-router-bench) |

**Mission.** The canonical measurements for every routing change.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **benchmark tasks covering balance, quality, latency and determinism** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **traffic replay corpus with realistic skew** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **regression gates with statistical significance**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **baseline records and change-review checklist** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.router.router_bench@1`
- `cap.t06.router.router_bench.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.hierarchical.hierarchical_routing@1` | use the in-file conservative substitute for `hierarchical_routing` (documented, slower, lower quality) and set `degraded['hierarchical_routing']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t05.weight.weight_sharing@1` | use the in-file conservative substitute for `weight_sharing` (documented, slower, lower quality) and set `degraded['weight_sharing']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - benchmark tasks covering balance, quality, latency and determini | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - traffic replay corpus with realistic skew | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regression gates with statistical significance | 520 | Third required mechanism. |
| 6 | Core implementation D - baseline records and change-review checklist | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0295_router_bench.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.router.router_bench@1`.
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

### P0296 · `moe_visualisation` — Sparse Compute Visualisation & Explainer

| field | value |
|---|---|
| part id | `P0296` (46/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0296_moe_visualisation.py` |
| module path | `hyperion.t06.routing.moe_visualisation` |
| capability published | `cap.t06.moe.moe_visualisation@1` |
| determinism class | `seeded` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0296_moe_visualisation.txt`](prompts/P0296_moe_visualisation.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0296-moe-visualisation) |

**Mission.** Makes 512-expert behaviour legible to a human operator.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **routing heatmaps, flow diagrams and drift dashboards as data artifacts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **per-request routing trace explanation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **anomaly highlighting with drill-down** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **usability validation with operator tasks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.moe.moe_visualisation@1`
- `cap.t06.moe.moe_visualisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.router.router_bench@1` | use the in-file conservative substitute for `router_bench` (documented, slower, lower quality) and set `degraded['router_bench']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t05.action.action_head@1` | use the in-file conservative substitute for `action_head` (documented, slower, lower quality) and set `degraded['action_head']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - routing heatmaps, flow diagrams and drift dashboards as data art | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-request routing trace explanation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - anomaly highlighting with drill-down | 520 | Third required mechanism. |
| 6 | Core implementation D - usability validation with operator tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0296_moe_visualisation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_visualisation@1`.
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

### P0297 · `adaptive_sparsity` — Runtime-Adaptive Sparsity Control

| field | value |
|---|---|
| part id | `P0297` (47/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0297_adaptive_sparsity.py` |
| module path | `hyperion.t06.routing.adaptive_sparsity` |
| capability published | `cap.t06.adaptive.adaptive_sparsity@1` |
| determinism class | `seeded` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0297_adaptive_sparsity.txt`](prompts/P0297_adaptive_sparsity.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0297-adaptive-sparsity) |

**Mission.** Turns sparsity up or down live to meet load and SLOs.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **closed-loop controller from latency/quality telemetry**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **stability analysis preventing oscillation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **quality floor enforcement under load spikes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured SLO attainment during traffic surges** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.adaptive.adaptive_sparsity@1`
- `cap.t06.adaptive.adaptive_sparsity.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_visualisation@1` | use the in-file conservative substitute for `moe_visualisation` (documented, slower, lower quality) and set `degraded['moe_visualisation']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t05.prompt.prompt_representation@1` | use the in-file conservative substitute for `prompt_representation` (documented, slower, lower quality) and set `degraded['prompt_representation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - closed-loop controller from latency/quality telemetry | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - stability analysis preventing oscillation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality floor enforcement under load spikes | 520 | Third required mechanism. |
| 6 | Core implementation D - measured SLO attainment during traffic surges | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0297_adaptive_sparsity.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.adaptive.adaptive_sparsity@1`.
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

### P0298 · `sparsity_verification` — Conditional-Compute Correctness Verification

| field | value |
|---|---|
| part id | `P0298` (48/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0298_sparsity_verification.py` |
| module path | `hyperion.t06.routing.sparsity_verification` |
| capability published | `cap.t06.sparsity.sparsity_verification@1` |
| determinism class | `seeded` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0298_sparsity_verification.txt`](prompts/P0298_sparsity_verification.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0298-sparsity-verification) |

**Mission.** Proves the sparse model equals its intended computation.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **dense-equivalence testing for the non-dropped path** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **invariant checks on combine weights and capacity accounting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **differential testing across sparsity settings** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **certification artifact for the eval tier**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t06.sparsity.sparsity_verification@1`
- `cap.t06.sparsity.sparsity_verification.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.adaptive.adaptive_sparsity@1` | use the in-file conservative substitute for `adaptive_sparsity` (documented, slower, lower quality) and set `degraded['adaptive_sparsity']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t05.arch.arch_spec_doc@1` | use the in-file conservative substitute for `arch_spec_doc` (documented, slower, lower quality) and set `degraded['arch_spec_doc']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dense-equivalence testing for the non-dropped path | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - invariant checks on combine weights and capacity accounting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - differential testing across sparsity settings | 520 | Third required mechanism. |
| 6 | Core implementation D - certification artifact for the eval tier | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0298_sparsity_verification.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.sparsity.sparsity_verification@1`.
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

### P0299 · `moe_speed_accounting` — S2 Speedup Accounting & Attribution

| field | value |
|---|---|
| part id | `P0299` (49/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0299_moe_speed_accounting.py` |
| module path | `hyperion.t06.routing.moe_speed_accounting` |
| capability published | `cap.t06.moe.moe_speed_accounting@1` |
| determinism class | `seeded` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0299_moe_speed_accounting.txt`](prompts/P0299_moe_speed_accounting.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0299-moe-speed-accounting) |

**Mission.** Proves the 3.2x conditional-compute component of the 100x law.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **FLOP and latency accounting per sparsity mechanism** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **additive-versus-multiplicative interaction analysis with S1/S5** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **measurement protocol with confidence intervals**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **attribution report feeding the 100x proof** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t06.moe.moe_speed_accounting@1`
- `cap.t06.moe.moe_speed_accounting.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.sparsity.sparsity_verification@1` | use the in-file conservative substitute for `sparsity_verification` (documented, slower, lower quality) and set `degraded['sparsity_verification']='local'` |
| `cap.t05.latent.latent_program_slots@1` | use the in-file conservative substitute for `latent_program_slots` (documented, slower, lower quality) and set `degraded['latent_program_slots']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - FLOP and latency accounting per sparsity mechanism | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - additive-versus-multiplicative interaction analysis with S1/S5 | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - measurement protocol with confidence intervals | 520 | Third required mechanism. |
| 6 | Core implementation D - attribution report feeding the 100x proof | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0299_moe_speed_accounting.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_speed_accounting@1`.
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

### P0300 · `moe_spec_doc` — Sparse Architecture Specification & Docs

| field | value |
|---|---|
| part id | `P0300` (50/50 of T06) |
| tier | `T06` — Sparse Routing & Mixture-of-Ω-Experts |
| language | Python 3.13 |
| file to produce | `parts/t06_routing/P0300_moe_spec_doc.py` |
| module path | `hyperion.t06.routing.moe_spec_doc` |
| capability published | `cap.t06.moe.moe_spec_doc@1` |
| determinism class | `seeded` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond |
| worker prompt | [`prompts/P0300_moe_spec_doc.txt`](prompts/P0300_moe_spec_doc.txt) · [inline](docs/PROMPTS_T06.md#prompt-p0300-moe-spec-doc) |

**Mission.** The authoritative description of all conditional-compute behaviour.

**Tier context.** 512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.

**Mandate — all four items are required; none is optional.**

1. Implement **spec of routing, capacity, placement and degradation semantics** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **auto-generated tables from the live configuration**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **drift detection between spec and implementation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **operator runbook for routing incidents** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t06.moe.moe_spec_doc@1`
- `cap.t06.moe.moe_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t06.moe.moe_speed_accounting@1` | use the in-file conservative substitute for `moe_speed_accounting` (documented, slower, lower quality) and set `degraded['moe_speed_accounting']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t05.positional.positional_design@1` | use the in-file conservative substitute for `positional_design` (documented, slower, lower quality) and set `degraded['positional_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - spec of routing, capacity, placement and degradation semantics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - auto-generated tables from the live configuration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - drift detection between spec and implementation | 520 | Third required mechanism. |
| 6 | Core implementation D - operator runbook for routing incidents | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t06_routing/P0300_moe_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t06.moe.moe_spec_doc@1`.
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
