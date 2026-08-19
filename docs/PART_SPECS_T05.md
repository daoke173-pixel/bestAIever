# HYPERION-Ω — Part specifications · T05 · Ω-Core Model Architecture

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Benchmarks this tier is accountable for.** GPQA Diamond, MMMU

**Tier dependencies.** T01, T02, T03

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0201](#p0201-omega-block) | `omega_block` | Ω-Block: The Core Residual Unit | `cap.t05.omega.omega_block@1` |
| [P0202](#p0202-hybrid-mixer) | `hybrid_mixer` | Attention/SSM Hybrid Mixing Policy | `cap.t05.hybrid.hybrid_mixer@1` |
| [P0203](#p0203-attention-variants) | `attention_variants` | Attention Variant Zoo & Selection | `cap.t05.attention.attention_variants@1` |
| [P0204](#p0204-kv-compression-model) | `kv_compression_model` | Learned KV Compression | `cap.t05.kv.kv_compression_model@1` |
| [P0205](#p0205-state-space-layer) | `state_space_layer` | Selective State-Space Layer | `cap.t05.state.state_space_layer@1` |
| [P0206](#p0206-recurrent-memory-layer) | `recurrent_memory_layer` | Recurrent Compressive Memory Layer | `cap.t05.recurrent.recurrent_memory_layer@1` |
| [P0207](#p0207-latent-program-slots) | `latent_program_slots` | Latent Program Slot Mechanism | `cap.t05.latent.latent_program_slots@1` |
| [P0208](#p0208-adaptive-depth) | `adaptive_depth` | Adaptive Computation Depth | `cap.t05.adaptive.adaptive_depth@1` |
| [P0209](#p0209-normalisation-design) | `normalisation_design` | Normalisation & Residual Scaling Design | `cap.t05.normalisation.normalisation_design@1` |
| [P0210](#p0210-activation-design) | `activation_design` | Activation & Gating Function Design | `cap.t05.activation.activation_design@1` |
| [P0211](#p0211-embedding-design) | `embedding_design` | Tokenisation-Aware Embedding & Unembedding | `cap.t05.embedding.embedding_design@1` |
| [P0212](#p0212-tokeniser-omega) | `tokeniser_omega` | Ω-Tokeniser: Byte-Level Adaptive Segmentation | `cap.t05.tokeniser.tokeniser_omega@1` |
| [P0213](#p0213-byte-latent-patching) | `byte_latent_patching` | Byte-Latent Patch Encoder | `cap.t05.byte.byte_latent_patching@1` |
| [P0214](#p0214-positional-design) | `positional_design` | Positional Representation Strategy | `cap.t05.positional.positional_design@1` |
| [P0215](#p0215-long-context-arch) | `long_context_arch` | Ultra-Long Context Architecture | `cap.t05.long.long_context_arch@1` |
| [P0216](#p0216-multi-token-prediction) | `multi_token_prediction` | Multi-Token Prediction Heads | `cap.t05.multi.multi_token_prediction@1` |
| [P0217](#p0217-draft-model-arch) | `draft_model_arch` | Ω-Draft Model Family Architecture | `cap.t05.draft.draft_model_arch@1` |
| [P0218](#p0218-verifier-head) | `verifier_head` | Internal Verifier & Confidence Heads | `cap.t05.verifier.verifier_head@1` |
| [P0219](#p0219-uncertainty-calibration) | `uncertainty_calibration` | Uncertainty Representation & Calibration | `cap.t05.uncertainty.uncertainty_calibration@1` |
| [P0220](#p0220-world-model-core) | `world_model_core` | Internal World Model & State Tracking | `cap.t05.world.world_model_core@1` |
| [P0221](#p0221-causal-model) | `causal_model` | Causal Representation & Intervention Reasoning | `cap.t05.causal.causal_model@1` |
| [P0222](#p0222-symbolic-bridge) | `symbolic_bridge` | Neural/Symbolic Interface Layer | `cap.t05.symbolic.symbolic_bridge@1` |
| [P0223](#p0223-program-induction-arch) | `program_induction_arch` | Program Induction & Abstraction Learning | `cap.t05.program.program_induction_arch@1` |
| [P0224](#p0224-meta-learning-arch) | `meta_learning_arch` | In-Context Meta-Learning Architecture | `cap.t05.meta.meta_learning_arch@1` |
| [P0225](#p0225-continual-learning) | `continual_learning` | Continual Learning Without Forgetting | `cap.t05.continual.continual_learning@1` |
| [P0226](#p0226-knowledge-editing) | `knowledge_editing` | Targeted Knowledge Editing | `cap.t05.knowledge.knowledge_editing@1` |
| [P0227](#p0227-model-merging) | `model_merging` | Model Merging & Capability Composition | `cap.t05.model.model_merging@1` |
| [P0228](#p0228-distillation-arch) | `distillation_arch` | Distillation Architecture & Objectives | `cap.t05.distillation.distillation_arch@1` |
| [P0229](#p0229-weight-sharing) | `weight_sharing` | Weight Sharing & Parameter Efficiency | `cap.t05.weight.weight_sharing@1` |
| [P0230](#p0230-init-scaling-laws) | `init_scaling_laws` | Initialisation & Scaling Law Framework | `cap.t05.init.init_scaling_laws@1` |
| [P0231](#p0231-architecture-search) | `architecture_search` | Architecture Search & Ablation Engine | `cap.t05.architecture.architecture_search@1` |
| [P0232](#p0232-depth-width-tradeoff) | `depth_width_tradeoff` | Depth/Width/Sparsity Allocation | `cap.t05.depth.depth_width_tradeoff@1` |
| [P0233](#p0233-residual-stream-design) | `residual_stream_design` | Residual Stream Capacity & Interference | `cap.t05.residual.residual_stream_design@1` |
| [P0234](#p0234-logit-head-design) | `logit_head_design` | Output Head, Logit Shaping & Constraints | `cap.t05.logit.logit_head_design@1` |
| [P0235](#p0235-multimodal-fusion-arch) | `multimodal_fusion_arch` | Multimodal Fusion Architecture | `cap.t05.multimodal.multimodal_fusion_arch@1` |
| [P0236](#p0236-action-head) | `action_head` | Action & Tool-Call Head | `cap.t05.action.action_head@1` |
| [P0237](#p0237-memory-attention-bridge) | `memory_attention_bridge` | Memory Retrieval Attention Bridge | `cap.t05.memory.memory_attention_bridge@1` |
| [P0238](#p0238-speculative-arch-hooks) | `speculative_arch_hooks` | Architecture Hooks for Speculative Decoding | `cap.t05.speculative.speculative_arch_hooks@1` |
| [P0239](#p0239-sparse-upcycling) | `sparse_upcycling` | Sparse Upcycling & Expert Initialisation | `cap.t05.sparse.sparse_upcycling@1` |
| [P0240](#p0240-model-surgery) | `model_surgery` | Model Surgery: Pruning, Grafting, Extension | `cap.t05.model.model_surgery@1` |
| [P0241](#p0241-numerical-arch-stability) | `numerical_arch_stability` | Architectural Numerical Stability | `cap.t05.numerical.numerical_arch_stability@1` |
| [P0242](#p0242-context-packing) | `context_packing` | Context Composition & Packing Strategy | `cap.t05.context.context_packing@1` |
| [P0243](#p0243-prompt-representation) | `prompt_representation` | Internal Prompt & Role Representation | `cap.t05.prompt.prompt_representation@1` |
| [P0244](#p0244-thought-representation) | `thought_representation` | Latent Thought Channel | `cap.t05.thought.thought_representation@1` |
| [P0245](#p0245-expert-specialisation) | `expert_specialisation` | Expert Specialisation Analysis & Design | `cap.t05.expert.expert_specialisation@1` |
| [P0246](#p0246-model-config-schema) | `model_config_schema` | Model Configuration Schema & Validation | `cap.t05.model.model_config_schema@1` |
| [P0247](#p0247-reference-forward) | `reference_forward` | Reference Forward Pass Implementation | `cap.t05.reference.reference_forward@1` |
| [P0248](#p0248-arch-ablation-suite) | `arch_ablation_suite` | Architecture Ablation & Evidence Suite | `cap.t05.arch.arch_ablation_suite@1` |
| [P0249](#p0249-capacity-probes) | `capacity_probes` | Capability Probes & Representation Diagnostics | `cap.t05.capacity.capacity_probes@1` |
| [P0250](#p0250-arch-spec-doc) | `arch_spec_doc` | Architecture Specification Document Generator | `cap.t05.arch.arch_spec_doc@1` |

---

### P0201 · `omega_block` — Ω-Block: The Core Residual Unit

| field | value |
|---|---|
| part id | `P0201` (1/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0201_omega_block.py` |
| module path | `hyperion.t05.core_model.omega_block` |
| capability published | `cap.t05.omega.omega_block@1` |
| determinism class | `pure` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0201_omega_block.txt`](prompts/P0201_omega_block.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0201-omega-block) |

**Mission.** The fundamental repeated block combining attention, SSM, MoE and latent program slots.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **block topology with parallel attention/SSM branches and learned mixing gates**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **residual scaling and depth-stable initialisation derivation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **per-branch precision and determinism declarations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **ablation harness measuring each branch's contribution** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.omega.omega_block@1`
- `cap.t05.omega.omega_block.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t02.fused.fused_moe_kernel@1` | use the in-file conservative substitute for `fused_moe_kernel` (documented, slower, lower quality) and set `degraded['fused_moe_kernel']='local'` |
| `cap.t03.guard.guard_specialise@1` | use the in-file conservative substitute for `guard_specialise` (documented, slower, lower quality) and set `degraded['guard_specialise']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - block topology with parallel attention/SSM branches and learned  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - residual scaling and depth-stable initialisation derivation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-branch precision and determinism declarations | 520 | Third required mechanism. |
| 6 | Core implementation D - ablation harness measuring each branch's contribution | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0201_omega_block.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.omega.omega_block@1`.
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

### P0202 · `hybrid_mixer` — Attention/SSM Hybrid Mixing Policy

| field | value |
|---|---|
| part id | `P0202` (2/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0202_hybrid_mixer.py` |
| module path | `hyperion.t05.core_model.hybrid_mixer` |
| capability published | `cap.t05.hybrid.hybrid_mixer@1` |
| determinism class | `pure` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0202_hybrid_mixer.txt`](prompts/P0202_hybrid_mixer.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0202-hybrid-mixer) |

**Mission.** Decides, per layer and per token, how much exact attention versus linear state is used.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **layer-interleaving schedule search and learned per-token gating** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **quality/compute tradeoff curves at multiple ratios** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **long-range retrieval probe accuracy versus pure attention** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **stability analysis of the gate under distribution shift**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.hybrid.hybrid_mixer@1`
- `cap.t05.hybrid.hybrid_mixer.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.omega.omega_block@1` | use the in-file conservative substitute for `omega_block` (documented, slower, lower quality) and set `degraded['omega_block']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t02.numa.numa_placement@1` | use the in-file conservative substitute for `numa_placement` (documented, slower, lower quality) and set `degraded['numa_placement']='local'` |
| `cap.t03.constant.constant_folding@1` | use the in-file conservative substitute for `constant_folding` (documented, slower, lower quality) and set `degraded['constant_folding']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - layer-interleaving schedule search and learned per-token gating | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quality/compute tradeoff curves at multiple ratios | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - long-range retrieval probe accuracy versus pure attention | 520 | Third required mechanism. |
| 6 | Core implementation D - stability analysis of the gate under distribution shift | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0202_hybrid_mixer.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.hybrid.hybrid_mixer@1`.
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

### P0203 · `attention_variants` — Attention Variant Zoo & Selection

| field | value |
|---|---|
| part id | `P0203` (3/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0203_attention_variants.py` |
| module path | `hyperion.t05.core_model.attention_variants` |
| capability published | `cap.t05.attention.attention_variants@1` |
| determinism class | `pure` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0203_attention_variants.txt`](prompts/P0203_attention_variants.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0203-attention-variants) |

**Mission.** Every attention form the model can use, with a principled selection rule.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **MHA/GQA/MQA/MLA-style latent compression with head-budget analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sliding-window, dilated, global-token and retrieval-augmented forms** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-layer variant assignment optimiser**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured quality/cost frontier per variant** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.attention.attention_variants@1`
- `cap.t05.attention.attention_variants.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.hybrid.hybrid_mixer@1` | use the in-file conservative substitute for `hybrid_mixer` (documented, slower, lower quality) and set `degraded['hybrid_mixer']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t02.kernel.kernel_fusion_rules@1` | use the in-file conservative substitute for `kernel_fusion_rules` (documented, slower, lower quality) and set `degraded['kernel_fusion_rules']='local'` |
| `cap.t03.target.target_description@1` | use the in-file conservative substitute for `target_description` (documented, slower, lower quality) and set `degraded['target_description']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - MHA/GQA/MQA/MLA-style latent compression with head-budget analys | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sliding-window, dilated, global-token and retrieval-augmented fo | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-layer variant assignment optimiser | 520 | Third required mechanism. |
| 6 | Core implementation D - measured quality/cost frontier per variant | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0203_attention_variants.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.attention.attention_variants@1`.
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

### P0204 · `kv_compression_model` — Learned KV Compression

| field | value |
|---|---|
| part id | `P0204` (4/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0204_kv_compression_model.py` |
| module path | `hyperion.t05.core_model.kv_compression_model` |
| capability published | `cap.t05.kv.kv_compression_model@1` |
| determinism class | `pure` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0204_kv_compression_model.txt`](prompts/P0204_kv_compression_model.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0204-kv-compression-model) |

**Mission.** Shrinks the KV cache by learning what is worth remembering.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **low-rank latent KV projection with reconstruction objective** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **importance-predicting head for eviction decisions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **quality-preservation validation on long-context tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured memory reduction at matched accuracy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.kv.kv_compression_model@1`
- `cap.t05.kv.kv_compression_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.attention.attention_variants@1` | use the in-file conservative substitute for `attention_variants` (documented, slower, lower quality) and set `degraded['attention_variants']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t02.sparse.sparse_attention_kernels@1` | use the in-file conservative substitute for `sparse_attention_kernels` (documented, slower, lower quality) and set `degraded['sparse_attention_kernels']='local'` |
| `cap.t03.kernel.kernel_template_lib@1` | use the in-file conservative substitute for `kernel_template_lib` (documented, slower, lower quality) and set `degraded['kernel_template_lib']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - low-rank latent KV projection with reconstruction objective | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - importance-predicting head for eviction decisions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality-preservation validation on long-context tasks | 520 | Third required mechanism. |
| 6 | Core implementation D - measured memory reduction at matched accuracy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0204_kv_compression_model.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.kv.kv_compression_model@1`.
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

### P0205 · `state_space_layer` — Selective State-Space Layer

| field | value |
|---|---|
| part id | `P0205` (5/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0205_state_space_layer.py` |
| module path | `hyperion.t05.core_model.state_space_layer` |
| capability published | `cap.t05.state.state_space_layer@1` |
| determinism class | `pure` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0205_state_space_layer.txt`](prompts/P0205_state_space_layer.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0205-state-space-layer) |

**Mission.** The O(N) memory backbone for extreme context.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **input-dependent A/B/C parameterisation with stability constraints**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **state initialisation and reset semantics across documents** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **gradient-flow analysis over very long sequences** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **recall accuracy on needle-in-haystack probes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.state.state_space_layer@1`
- `cap.t05.state.state_space_layer.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.kv.kv_compression_model@1` | use the in-file conservative substitute for `kv_compression_model` (documented, slower, lower quality) and set `degraded['kv_compression_model']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t02.tensor.tensor_core_util@1` | use the in-file conservative substitute for `tensor_core_util` (documented, slower, lower quality) and set `degraded['tensor_core_util']='local'` |
| `cap.t03.compiler.compiler_fuzzer@1` | use the in-file conservative substitute for `compiler_fuzzer` (documented, slower, lower quality) and set `degraded['compiler_fuzzer']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - input-dependent A/B/C parameterisation with stability constraint | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - state initialisation and reset semantics across documents | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - gradient-flow analysis over very long sequences | 520 | Third required mechanism. |
| 6 | Core implementation D - recall accuracy on needle-in-haystack probes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0205_state_space_layer.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.state.state_space_layer@1`.
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

### P0206 · `recurrent_memory_layer` — Recurrent Compressive Memory Layer

| field | value |
|---|---|
| part id | `P0206` (6/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0206_recurrent_memory_layer.py` |
| module path | `hyperion.t05.core_model.recurrent_memory_layer` |
| capability published | `cap.t05.recurrent.recurrent_memory_layer@1` |
| determinism class | `pure` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0206_recurrent_memory_layer.txt`](prompts/P0206_recurrent_memory_layer.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0206-recurrent-memory-layer) |

**Mission.** Carries information across millions of tokens with bounded state.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **compressive memory update rule with write/erase gating** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **capacity analysis and interference measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **read-out attention over memory slots** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **multi-document recall benchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.recurrent.recurrent_memory_layer@1`
- `cap.t05.recurrent.recurrent_memory_layer.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.state.state_space_layer@1` | use the in-file conservative substitute for `state_space_layer` (documented, slower, lower quality) and set `degraded['state_space_layer']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t02.attn.attn_flash_bwd@1` | use the in-file conservative substitute for `attn_flash_bwd` (documented, slower, lower quality) and set `degraded['attn_flash_bwd']='local'` |
| `cap.t03.dtype.dtype_promotion@1` | use the in-file conservative substitute for `dtype_promotion` (documented, slower, lower quality) and set `degraded['dtype_promotion']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - compressive memory update rule with write/erase gating | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capacity analysis and interference measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - read-out attention over memory slots | 520 | Third required mechanism. |
| 6 | Core implementation D - multi-document recall benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0206_recurrent_memory_layer.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.recurrent.recurrent_memory_layer@1`.
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

### P0207 · `latent_program_slots` — Latent Program Slot Mechanism

| field | value |
|---|---|
| part id | `P0207` (7/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0207_latent_program_slots.py` |
| module path | `hyperion.t05.core_model.latent_program_slots` |
| capability published | `cap.t05.latent.latent_program_slots@1` |
| determinism class | `pure` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0207_latent_program_slots.txt`](prompts/P0207_latent_program_slots.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0207-latent-program-slots) |

**Mission.** Lets the network allocate reusable internal subroutines rather than re-deriving them.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **slot bank with addressing, binding and reuse counting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **program-induction objective and slot specialisation analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **interpretability probes naming what each slot computes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured gain on compositional generalisation tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.latent.latent_program_slots@1`
- `cap.t05.latent.latent_program_slots.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.recurrent.recurrent_memory_layer@1` | use the in-file conservative substitute for `recurrent_memory_layer` (documented, slower, lower quality) and set `degraded['recurrent_memory_layer']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t02.reduction.reduction_kernels@1` | use the in-file conservative substitute for `reduction_kernels` (documented, slower, lower quality) and set `degraded['reduction_kernels']='local'` |
| `cap.t03.parallel.parallel_partition@1` | use the in-file conservative substitute for `parallel_partition` (documented, slower, lower quality) and set `degraded['parallel_partition']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - slot bank with addressing, binding and reuse counting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - program-induction objective and slot specialisation analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - interpretability probes naming what each slot computes | 520 | Third required mechanism. |
| 6 | Core implementation D - measured gain on compositional generalisation tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0207_latent_program_slots.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.latent.latent_program_slots@1`.
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

### P0208 · `adaptive_depth` — Adaptive Computation Depth

| field | value |
|---|---|
| part id | `P0208` (8/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0208_adaptive_depth.py` |
| module path | `hyperion.t05.core_model.adaptive_depth` |
| capability published | `cap.t05.adaptive.adaptive_depth@1` |
| determinism class | `pure` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0208_adaptive_depth.txt`](prompts/P0208_adaptive_depth.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0208-adaptive-depth) |

**Mission.** Easy tokens exit early; hard tokens recurse deeper (part of speed source S2).

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **per-token halting head with calibrated confidence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **layer-recurrence for hard tokens with shared weights**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **compute-vs-accuracy curves and budget-constrained mode** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **worst-case latency bound proof** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.adaptive.adaptive_depth@1`
- `cap.t05.adaptive.adaptive_depth.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.latent.latent_program_slots@1` | use the in-file conservative substitute for `latent_program_slots` (documented, slower, lower quality) and set `degraded['latent_program_slots']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t02.rng.rng_kernels@1` | use the in-file conservative substitute for `rng_kernels` (documented, slower, lower quality) and set `degraded['rng_kernels']='local'` |
| `cap.t03.jit.jit_cache_compiler@1` | use the in-file conservative substitute for `jit_cache_compiler` (documented, slower, lower quality) and set `degraded['jit_cache_compiler']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-token halting head with calibrated confidence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - layer-recurrence for hard tokens with shared weights | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - compute-vs-accuracy curves and budget-constrained mode | 520 | Third required mechanism. |
| 6 | Core implementation D - worst-case latency bound proof | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0208_adaptive_depth.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.adaptive.adaptive_depth@1`.
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

### P0209 · `normalisation_design` — Normalisation & Residual Scaling Design

| field | value |
|---|---|
| part id | `P0209` (9/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0209_normalisation_design.py` |
| module path | `hyperion.t05.core_model.normalisation_design` |
| capability published | `cap.t05.normalisation.normalisation_design@1` |
| determinism class | `pure` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0209_normalisation_design.txt`](prompts/P0209_normalisation_design.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0209-normalisation-design) |

**Mission.** The choices that make a very deep, very sparse model trainable and stable.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **pre/post/sandwich norm comparison with gradient-norm evidence**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **QK-norm and logit-cap for attention stability** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **depth-dependent residual scaling derivation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **training-stability evidence at extreme depth** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.normalisation.normalisation_design@1`
- `cap.t05.normalisation.normalisation_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.adaptive.adaptive_depth@1` | use the in-file conservative substitute for `adaptive_depth` (documented, slower, lower quality) and set `degraded['adaptive_depth']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t02.simd.simd_cpu@1` | use the in-file conservative substitute for `simd_cpu` (documented, slower, lower quality) and set `degraded['simd_cpu']='local'` |
| `cap.t03.loop.loop_transform@1` | use the in-file conservative substitute for `loop_transform` (documented, slower, lower quality) and set `degraded['loop_transform']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pre/post/sandwich norm comparison with gradient-norm evidence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - QK-norm and logit-cap for attention stability | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - depth-dependent residual scaling derivation | 520 | Third required mechanism. |
| 6 | Core implementation D - training-stability evidence at extreme depth | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0209_normalisation_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.normalisation.normalisation_design@1`.
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

### P0210 · `activation_design` — Activation & Gating Function Design

| field | value |
|---|---|
| part id | `P0210` (10/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0210_activation_design.py` |
| module path | `hyperion.t05.core_model.activation_design` |
| capability published | `cap.t05.activation.activation_design@1` |
| determinism class | `pure` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0210_activation_design.txt`](prompts/P0210_activation_design.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0210-activation-design) |

**Mission.** Activation choices justified by measurement, not tradition.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **gated-linear family comparison at matched parameter and FLOP budgets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **numerical range analysis for low-precision safety** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **expressivity arguments and empirical ablations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **kernel-fusion friendliness assessment**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.activation.activation_design@1`
- `cap.t05.activation.activation_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.normalisation.normalisation_design@1` | use the in-file conservative substitute for `normalisation_design` (documented, slower, lower quality) and set `degraded['normalisation_design']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t02.emulation.emulation_reference@1` | use the in-file conservative substitute for `emulation_reference` (documented, slower, lower quality) and set `degraded['emulation_reference']='local'` |
| `cap.t03.profile.profile_guided@1` | use the in-file conservative substitute for `profile_guided` (documented, slower, lower quality) and set `degraded['profile_guided']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gated-linear family comparison at matched parameter and FLOP bud | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - numerical range analysis for low-precision safety | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - expressivity arguments and empirical ablations | 520 | Third required mechanism. |
| 6 | Core implementation D - kernel-fusion friendliness assessment | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0210_activation_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.activation.activation_design@1`.
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

### P0211 · `embedding_design` — Tokenisation-Aware Embedding & Unembedding

| field | value |
|---|---|
| part id | `P0211` (11/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0211_embedding_design.py` |
| module path | `hyperion.t05.core_model.embedding_design` |
| capability published | `cap.t05.embedding.embedding_design@1` |
| determinism class | `pure` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0211_embedding_design.txt`](prompts/P0211_embedding_design.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0211-embedding-design) |

**Mission.** Input/output representations, including tied and factorised forms.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **factorised embedding with rank selection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **tied-weight analysis and separate-head comparison** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **vocabulary-frequency-aware initialisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured perplexity and downstream effect** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.embedding.embedding_design@1`
- `cap.t05.embedding.embedding_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.activation.activation_design@1` | use the in-file conservative substitute for `activation_design` (documented, slower, lower quality) and set `degraded['activation_design']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t02.kernel.kernel_codegen_rt@1` | use the in-file conservative substitute for `kernel_codegen_rt` (documented, slower, lower quality) and set `degraded['kernel_codegen_rt']='local'` |
| `cap.t03.equality.equality_saturation@1` | use the in-file conservative substitute for `equality_saturation` (documented, slower, lower quality) and set `degraded['equality_saturation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - factorised embedding with rank selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tied-weight analysis and separate-head comparison | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - vocabulary-frequency-aware initialisation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured perplexity and downstream effect | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0211_embedding_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.embedding.embedding_design@1`.
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

### P0212 · `tokeniser_omega` — Ω-Tokeniser: Byte-Level Adaptive Segmentation

| field | value |
|---|---|
| part id | `P0212` (12/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0212_tokeniser_omega.py` |
| module path | `hyperion.t05.core_model.tokeniser_omega` |
| capability published | `cap.t05.tokeniser.tokeniser_omega@1` |
| determinism class | `pure` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0212_tokeniser_omega.txt`](prompts/P0212_tokeniser_omega.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0212-tokeniser-omega) |

**Mission.** Fixes the tokenizer tax that inflates Opus-class token counts by up to 35%.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **byte-level BPE with learned merge policy and code/math-aware pre-tokenisation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **multilingual fairness measurement of tokens-per-character**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **adaptive patching that lets frequent structures cost one token** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured token-count reduction versus the Opus 4.7+ tokenizer** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.tokeniser.tokeniser_omega@1`
- `cap.t05.tokeniser.tokeniser_omega.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.embedding.embedding_design@1` | use the in-file conservative substitute for `embedding_design` (documented, slower, lower quality) and set `degraded['embedding_design']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t02.micro.micro_opt_catalog@1` | use the in-file conservative substitute for `micro_opt_catalog` (documented, slower, lower quality) and set `degraded['micro_opt_catalog']='local'` |
| `cap.t03.graph.graph_diff_tool@1` | use the in-file conservative substitute for `graph_diff_tool` (documented, slower, lower quality) and set `degraded['graph_diff_tool']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - byte-level BPE with learned merge policy and code/math-aware pre | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multilingual fairness measurement of tokens-per-character | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - adaptive patching that lets frequent structures cost one token | 520 | Third required mechanism. |
| 6 | Core implementation D - measured token-count reduction versus the Opus 4.7+ tokenizer | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0212_tokeniser_omega.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.tokeniser.tokeniser_omega@1`.
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

### P0213 · `byte_latent_patching` — Byte-Latent Patch Encoder

| field | value |
|---|---|
| part id | `P0213` (13/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0213_byte_latent_patching.py` |
| module path | `hyperion.t05.core_model.byte_latent_patching` |
| capability published | `cap.t05.byte.byte_latent_patching@1` |
| determinism class | `pure` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0213_byte_latent_patching.txt`](prompts/P0213_byte_latent_patching.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0213-byte-latent-patching) |

**Mission.** Tokeniser-free path: entropy-driven patching straight from bytes.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **entropy-model-driven patch boundary prediction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **patch encoder/decoder with variable compression rate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **robustness to typos, code, binary and rare scripts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **quality/compute comparison against the tokenised path** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.byte.byte_latent_patching@1`
- `cap.t05.byte.byte_latent_patching.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.tokeniser.tokeniser_omega@1` | use the in-file conservative substitute for `tokeniser_omega` (documented, slower, lower quality) and set `degraded['tokeniser_omega']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t02.attn.attn_flash_fwd@1` | use the in-file conservative substitute for `attn_flash_fwd` (documented, slower, lower quality) and set `degraded['attn_flash_fwd']='local'` |
| `cap.t03.shape.shape_inference@1` | use the in-file conservative substitute for `shape_inference` (documented, slower, lower quality) and set `degraded['shape_inference']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - entropy-model-driven patch boundary prediction | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - patch encoder/decoder with variable compression rate | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - robustness to typos, code, binary and rare scripts | 520 | Third required mechanism. |
| 6 | Core implementation D - quality/compute comparison against the tokenised path | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0213_byte_latent_patching.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.byte.byte_latent_patching@1`.
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

### P0214 · `positional_design` — Positional Representation Strategy

| field | value |
|---|---|
| part id | `P0214` (14/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0214_positional_design.py` |
| module path | `hyperion.t05.core_model.positional_design` |
| capability published | `cap.t05.positional.positional_design@1` |
| determinism class | `pure` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0214_positional_design.txt`](prompts/P0214_positional_design.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0214-positional-design) |

**Mission.** Position handling that extrapolates far past training length.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **RoPE-family scaling analysis with theoretical extrapolation bounds** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **learned-relative and no-position ablations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **position interpolation policy per attention variant** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **length-generalisation curves to 10x training length**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.positional.positional_design@1`
- `cap.t05.positional.positional_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.byte.byte_latent_patching@1` | use the in-file conservative substitute for `byte_latent_patching` (documented, slower, lower quality) and set `degraded['byte_latent_patching']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t02.elementwise.elementwise_fusion@1` | use the in-file conservative substitute for `elementwise_fusion` (documented, slower, lower quality) and set `degraded['elementwise_fusion']='local'` |
| `cap.t03.scheduler.scheduler_pass@1` | use the in-file conservative substitute for `scheduler_pass` (documented, slower, lower quality) and set `degraded['scheduler_pass']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - RoPE-family scaling analysis with theoretical extrapolation boun | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - learned-relative and no-position ablations | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - position interpolation policy per attention variant | 520 | Third required mechanism. |
| 6 | Core implementation D - length-generalisation curves to 10x training length | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0214_positional_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.positional.positional_design@1`.
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

### P0215 · `long_context_arch` — Ultra-Long Context Architecture

| field | value |
|---|---|
| part id | `P0215` (15/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0215_long_context_arch.py` |
| module path | `hyperion.t05.core_model.long_context_arch` |
| capability published | `cap.t05.long.long_context_arch@1` |
| determinism class | `pure` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0215_long_context_arch.txt`](prompts/P0215_long_context_arch.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0215-long-context-arch) |

**Mission.** The design that makes an effective 1G-token context feasible.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **hierarchical context: exact recent window, compressed mid, retrieved far** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cross-level consistency and information-routing analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cost model per context tier**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **recall and reasoning benchmarks at extreme lengths** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.long.long_context_arch@1`
- `cap.t05.long.long_context_arch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.positional.positional_design@1` | use the in-file conservative substitute for `positional_design` (documented, slower, lower quality) and set `degraded['positional_design']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t02.transpose.transpose_layout@1` | use the in-file conservative substitute for `transpose_layout` (documented, slower, lower quality) and set `degraded['transpose_layout']='local'` |
| `cap.t03.codegen.codegen_cpu@1` | use the in-file conservative substitute for `codegen_cpu` (documented, slower, lower quality) and set `degraded['codegen_cpu']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hierarchical context: exact recent window, compressed mid, retri | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-level consistency and information-routing analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost model per context tier | 520 | Third required mechanism. |
| 6 | Core implementation D - recall and reasoning benchmarks at extreme lengths | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0215_long_context_arch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.long.long_context_arch@1`.
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

### P0216 · `multi_token_prediction` — Multi-Token Prediction Heads

| field | value |
|---|---|
| part id | `P0216` (16/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0216_multi_token_prediction.py` |
| module path | `hyperion.t05.core_model.multi_token_prediction` |
| capability published | `cap.t05.multi.multi_token_prediction@1` |
| determinism class | `pure` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0216_multi_token_prediction.txt`](prompts/P0216_multi_token_prediction.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0216-multi-token-prediction) |

**Mission.** Predicts several future tokens per step: better representations and faster decode.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **head architecture with shared trunk and per-offset calibration** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **training objective weighting across offsets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **integration with the speculative cascade as a free draft source** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured acceptance-rate contribution to S1** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.multi.multi_token_prediction@1`
- `cap.t05.multi.multi_token_prediction.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.long.long_context_arch@1` | use the in-file conservative substitute for `long_context_arch` (documented, slower, lower quality) and set `degraded['long_context_arch']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t02.cache.cache_blocking@1` | use the in-file conservative substitute for `cache_blocking` (documented, slower, lower quality) and set `degraded['cache_blocking']='local'` |
| `cap.t03.vectorisation.vectorisation_transform@1` | use the in-file conservative substitute for `vectorisation_transform` (documented, slower, lower quality) and set `degraded['vectorisation_transform']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - head architecture with shared trunk and per-offset calibration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - training objective weighting across offsets | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - integration with the speculative cascade as a free draft source | 520 | Third required mechanism. |
| 6 | Core implementation D - measured acceptance-rate contribution to S1 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0216_multi_token_prediction.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.multi.multi_token_prediction@1`.
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

### P0217 · `draft_model_arch` — Ω-Draft Model Family Architecture

| field | value |
|---|---|
| part id | `P0217` (17/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0217_draft_model_arch.py` |
| module path | `hyperion.t05.core_model.draft_model_arch` |
| capability published | `cap.t05.draft.draft_model_arch@1` |
| determinism class | `pure` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0217_draft_model_arch.txt`](prompts/P0217_draft_model_arch.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0217-draft-model-arch) |

**Mission.** The 1.5B/7B/70B drafters that power the 8-stage cascade.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **capacity ladder design with shared vocabulary and KV layout**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **distillation-friendly architecture choices for high acceptance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **per-stage acceptance-rate targets and measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **memory footprint budget for co-residency with the core** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.draft.draft_model_arch@1`
- `cap.t05.draft.draft_model_arch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.multi.multi_token_prediction@1` | use the in-file conservative substitute for `multi_token_prediction` (documented, slower, lower quality) and set `degraded['multi_token_prediction']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t02.profiler.profiler_hooks@1` | use the in-file conservative substitute for `profiler_hooks` (documented, slower, lower quality) and set `degraded['profiler_hooks']='local'` |
| `cap.t03.compile.compile_time_budget@1` | use the in-file conservative substitute for `compile_time_budget` (documented, slower, lower quality) and set `degraded['compile_time_budget']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capacity ladder design with shared vocabulary and KV layout | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - distillation-friendly architecture choices for high acceptance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-stage acceptance-rate targets and measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - memory footprint budget for co-residency with the core | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0217_draft_model_arch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.draft.draft_model_arch@1`.
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

### P0218 · `verifier_head` — Internal Verifier & Confidence Heads

| field | value |
|---|---|
| part id | `P0218` (18/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0218_verifier_head.py` |
| module path | `hyperion.t05.core_model.verifier_head` |
| capability published | `cap.t05.verifier.verifier_head@1` |
| determinism class | `pure` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0218_verifier_head.txt`](prompts/P0218_verifier_head.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0218-verifier-head) |

**Mission.** The model's own critic: predicts correctness before the answer ships.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **per-claim and per-step correctness heads with calibration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **abstention/escalation policy driven by the verifier** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **selective-prediction risk-coverage curves** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured reduction in confident errors versus baseline**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.verifier.verifier_head@1`
- `cap.t05.verifier.verifier_head.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.draft.draft_model_arch@1` | use the in-file conservative substitute for `draft_model_arch` (documented, slower, lower quality) and set `degraded['draft_model_arch']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t02.error.error_correction@1` | use the in-file conservative substitute for `error_correction` (documented, slower, lower quality) and set `degraded['error_correction']='local'` |
| `cap.t03.superoptimiser.superoptimiser@1` | use the in-file conservative substitute for `superoptimiser` (documented, slower, lower quality) and set `degraded['superoptimiser']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-claim and per-step correctness heads with calibration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - abstention/escalation policy driven by the verifier | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - selective-prediction risk-coverage curves | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction in confident errors versus baseline | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0218_verifier_head.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.verifier.verifier_head@1`.
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

### P0219 · `uncertainty_calibration` — Uncertainty Representation & Calibration

| field | value |
|---|---|
| part id | `P0219` (19/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0219_uncertainty_calibration.py` |
| module path | `hyperion.t05.core_model.uncertainty_calibration` |
| capability published | `cap.t05.uncertainty.uncertainty_calibration@1` |
| determinism class | `pure` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0219_uncertainty_calibration.txt`](prompts/P0219_uncertainty_calibration.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0219-uncertainty-calibration) |

**Mission.** Numbers you can act on: calibrated probabilities everywhere.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **temperature/vector scaling and conformal prediction integration** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **epistemic-vs-aleatoric decomposition** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **calibration metrics (ECE, ACE) with target thresholds**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **decision-theoretic use in routing and escalation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.uncertainty.uncertainty_calibration@1`
- `cap.t05.uncertainty.uncertainty_calibration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.verifier.verifier_head@1` | use the in-file conservative substitute for `verifier_head` (documented, slower, lower quality) and set `degraded['verifier_head']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t02.kernel.kernel_bench_suite@1` | use the in-file conservative substitute for `kernel_bench_suite` (documented, slower, lower quality) and set `degraded['kernel_bench_suite']='local'` |
| `cap.t03.op.op_registry@1` | use the in-file conservative substitute for `op_registry` (documented, slower, lower quality) and set `degraded['op_registry']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - temperature/vector scaling and conformal prediction integration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - epistemic-vs-aleatoric decomposition | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - calibration metrics (ECE, ACE) with target thresholds | 520 | Third required mechanism. |
| 6 | Core implementation D - decision-theoretic use in routing and escalation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0219_uncertainty_calibration.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.uncertainty.uncertainty_calibration@1`.
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

### P0220 · `world_model_core` — Internal World Model & State Tracking

| field | value |
|---|---|
| part id | `P0220` (20/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0220_world_model_core.py` |
| module path | `hyperion.t05.core_model.world_model_core` |
| capability published | `cap.t05.world.world_model_core@1` |
| determinism class | `pure` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0220_world_model_core.txt`](prompts/P0220_world_model_core.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0220-world-model-core) |

**Mission.** Explicit, updatable beliefs about entities, quantities and constraints.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **entity/relation state representation with typed slots** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **update rules from text, tools and observations with conflict handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **consistency checking against retrieved evidence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **state-tracking benchmark accuracy on long narratives** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.world.world_model_core@1`
- `cap.t05.world.world_model_core.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.uncertainty.uncertainty_calibration@1` | use the in-file conservative substitute for `uncertainty_calibration` (documented, slower, lower quality) and set `degraded['uncertainty_calibration']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t02.gemm.gemm_sparse@1` | use the in-file conservative substitute for `gemm_sparse` (documented, slower, lower quality) and set `degraded['gemm_sparse']='local'` |
| `cap.t03.pass.pass_manager@1` | use the in-file conservative substitute for `pass_manager` (documented, slower, lower quality) and set `degraded['pass_manager']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - entity/relation state representation with typed slots | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - update rules from text, tools and observations with conflict han | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - consistency checking against retrieved evidence | 520 | Third required mechanism. |
| 6 | Core implementation D - state-tracking benchmark accuracy on long narratives | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0220_world_model_core.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.world.world_model_core@1`.
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

### P0221 · `causal_model` — Causal Representation & Intervention Reasoning

| field | value |
|---|---|
| part id | `P0221` (21/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0221_causal_model.py` |
| module path | `hyperion.t05.core_model.causal_model` |
| capability published | `cap.t05.causal.causal_model@1` |
| determinism class | `pure` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0221_causal_model.txt`](prompts/P0221_causal_model.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0221-causal-model) |

**Mission.** Distinguishes correlation from causation in the model's own reasoning.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **structural causal model representation and do-calculus evaluation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **confounder identification from context** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **counterfactual query answering with assumptions made explicit** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **benchmark on causal-inference question suites** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.causal.causal_model@1`
- `cap.t05.causal.causal_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.world.world_model_core@1` | use the in-file conservative substitute for `world_model_core` (documented, slower, lower quality) and set `degraded['world_model_core']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t02.softmax.softmax_norm@1` | use the in-file conservative substitute for `softmax_norm` (documented, slower, lower quality) and set `degraded['softmax_norm']='local'` |
| `cap.t03.rematerialisat.rematerialisation@1` | use the in-file conservative substitute for `rematerialisation` (documented, slower, lower quality) and set `degraded['rematerialisation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structural causal model representation and do-calculus evaluatio | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - confounder identification from context | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - counterfactual query answering with assumptions made explicit | 520 | Third required mechanism. |
| 6 | Core implementation D - benchmark on causal-inference question suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0221_causal_model.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.causal.causal_model@1`.
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

### P0222 · `symbolic_bridge` — Neural/Symbolic Interface Layer

| field | value |
|---|---|
| part id | `P0222` (22/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0222_symbolic_bridge.py` |
| module path | `hyperion.t05.core_model.symbolic_bridge` |
| capability published | `cap.t05.symbolic.symbolic_bridge@1` |
| determinism class | `pure` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0222_symbolic_bridge.txt`](prompts/P0222_symbolic_bridge.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0222-symbolic-bridge) |

**Mission.** Lets the network hand a subproblem to an exact solver and use the result.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **differentiable-to-symbolic translation with type checking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **solver result integration and belief update** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **failure handling when symbolic translation is impossible** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured accuracy gain on math and constraint tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.symbolic.symbolic_bridge@1`
- `cap.t05.symbolic.symbolic_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.causal.causal_model@1` | use the in-file conservative substitute for `causal_model` (documented, slower, lower quality) and set `degraded['causal_model']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t02.gather.gather_scatter@1` | use the in-file conservative substitute for `gather_scatter` (documented, slower, lower quality) and set `degraded['gather_scatter']='local'` |
| `cap.t03.codegen.codegen_gpu@1` | use the in-file conservative substitute for `codegen_gpu` (documented, slower, lower quality) and set `degraded['codegen_gpu']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - differentiable-to-symbolic translation with type checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - solver result integration and belief update | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - failure handling when symbolic translation is impossible | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy gain on math and constraint tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0222_symbolic_bridge.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.symbolic.symbolic_bridge@1`.
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

### P0223 · `program_induction_arch` — Program Induction & Abstraction Learning

| field | value |
|---|---|
| part id | `P0223` (23/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0223_program_induction_arch.py` |
| module path | `hyperion.t05.core_model.program_induction_arch` |
| capability published | `cap.t05.program.program_induction_arch@1` |
| determinism class | `pure` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0223_program_induction_arch.txt`](prompts/P0223_program_induction_arch.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0223-program-induction-arch) |

**Mission.** Learns reusable abstractions from few examples: the ARC-AGI-3 engine.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **DSL design for grid/graph/sequence transformations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **library learning with compression-based abstraction discovery** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **neural-guided enumerative synthesis over the DSL**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 88% on ARC-AGI-3 versus Opus 5's 30.2%** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.program.program_induction_arch@1`
- `cap.t05.program.program_induction_arch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.symbolic.symbolic_bridge@1` | use the in-file conservative substitute for `symbolic_bridge` (documented, slower, lower quality) and set `degraded['symbolic_bridge']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t02.async.async_copy@1` | use the in-file conservative substitute for `async_copy` (documented, slower, lower quality) and set `degraded['async_copy']='local'` |
| `cap.t03.differentiatio.differentiation@1` | use the in-file conservative substitute for `differentiation` (documented, slower, lower quality) and set `degraded['differentiation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - DSL design for grid/graph/sequence transformations | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - library learning with compression-based abstraction discovery | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - neural-guided enumerative synthesis over the DSL | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 88% on ARC-AGI-3 versus Opus 5's 30.2% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0223_program_induction_arch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.program.program_induction_arch@1`.
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

### P0224 · `meta_learning_arch` — In-Context Meta-Learning Architecture

| field | value |
|---|---|
| part id | `P0224` (24/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0224_meta_learning_arch.py` |
| module path | `hyperion.t05.core_model.meta_learning_arch` |
| capability published | `cap.t05.meta.meta_learning_arch@1` |
| determinism class | `pure` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0224_meta_learning_arch.txt`](prompts/P0224_meta_learning_arch.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0224-meta-learning-arch) |

**Mission.** Learns new tasks within a single conversation and keeps the skill.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **fast-weight/adapter-in-context mechanism with bounded capacity** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **task-inference head identifying the current task family**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **catastrophic-interference measurement and mitigation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **few-shot learning curves versus baseline in-context learning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.meta.meta_learning_arch@1`
- `cap.t05.meta.meta_learning_arch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.program.program_induction_arch@1` | use the in-file conservative substitute for `program_induction_arch` (documented, slower, lower quality) and set `degraded['program_induction_arch']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t02.roofline.roofline_model@1` | use the in-file conservative substitute for `roofline_model` (documented, slower, lower quality) and set `degraded['roofline_model']='local'` |
| `cap.t03.differential.differential_testing@1` | use the in-file conservative substitute for `differential_testing` (documented, slower, lower quality) and set `degraded['differential_testing']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fast-weight/adapter-in-context mechanism with bounded capacity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - task-inference head identifying the current task family | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - catastrophic-interference measurement and mitigation | 520 | Third required mechanism. |
| 6 | Core implementation D - few-shot learning curves versus baseline in-context learning | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0224_meta_learning_arch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.meta.meta_learning_arch@1`.
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

### P0225 · `continual_learning` — Continual Learning Without Forgetting

| field | value |
|---|---|
| part id | `P0225` (25/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0225_continual_learning.py` |
| module path | `hyperion.t05.core_model.continual_learning` |
| capability published | `cap.t05.continual.continual_learning@1` |
| determinism class | `pure` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0225_continual_learning.txt`](prompts/P0225_continual_learning.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0225-continual-learning) |

**Mission.** Absorbs new knowledge after deployment, safely and reversibly.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **parameter-isolation and replay strategies with forgetting bounds**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **knowledge-edit application with locality verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **rollback and provenance for every learned change** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **forgetting/plasticity tradeoff measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.continual.continual_learning@1`
- `cap.t05.continual.continual_learning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.meta.meta_learning_arch@1` | use the in-file conservative substitute for `meta_learning_arch` (documented, slower, lower quality) and set `degraded['meta_learning_arch']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t02.power.power_thermal@1` | use the in-file conservative substitute for `power_thermal` (documented, slower, lower quality) and set `degraded['power_thermal']='local'` |
| `cap.t03.pass.pass_search@1` | use the in-file conservative substitute for `pass_search` (documented, slower, lower quality) and set `degraded['pass_search']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - parameter-isolation and replay strategies with forgetting bounds | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - knowledge-edit application with locality verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - rollback and provenance for every learned change | 520 | Third required mechanism. |
| 6 | Core implementation D - forgetting/plasticity tradeoff measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0225_continual_learning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.continual.continual_learning@1`.
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

### P0226 · `knowledge_editing` — Targeted Knowledge Editing

| field | value |
|---|---|
| part id | `P0226` (26/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0226_knowledge_editing.py` |
| module path | `hyperion.t05.core_model.knowledge_editing` |
| capability published | `cap.t05.knowledge.knowledge_editing@1` |
| determinism class | `pure` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0226_knowledge_editing.txt`](prompts/P0226_knowledge_editing.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0226-knowledge-editing) |

**Mission.** Change one fact without breaking a thousand others.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **locate-then-edit method with causal tracing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **ripple-effect evaluation across paraphrases and implications** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **batch-edit interference analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **edit success/locality/generalisation metrics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.knowledge.knowledge_editing@1`
- `cap.t05.knowledge.knowledge_editing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.continual.continual_learning@1` | use the in-file conservative substitute for `continual_learning` (documented, slower, lower quality) and set `degraded['continual_learning']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t02.ragged.ragged_batch@1` | use the in-file conservative substitute for `ragged_batch` (documented, slower, lower quality) and set `degraded['ragged_batch']='local'` |
| `cap.t03.numeric.numeric_mode_lowering@1` | use the in-file conservative substitute for `numeric_mode_lowering` (documented, slower, lower quality) and set `degraded['numeric_mode_lowering']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - locate-then-edit method with causal tracing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - ripple-effect evaluation across paraphrases and implications | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - batch-edit interference analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - edit success/locality/generalisation metrics | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0226_knowledge_editing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.knowledge.knowledge_editing@1`.
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

### P0227 · `model_merging` — Model Merging & Capability Composition

| field | value |
|---|---|
| part id | `P0227` (27/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0227_model_merging.py` |
| module path | `hyperion.t05.core_model.model_merging` |
| capability published | `cap.t05.model.model_merging@1` |
| determinism class | `pure` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0227_model_merging.txt`](prompts/P0227_model_merging.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0227-model-merging) |

**Mission.** Combines specialists into one model without averaging away skill.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **task-vector arithmetic with interference resolution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **permutation alignment before merging** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **merge-quality prediction and layer-wise weighting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured retention of each specialist's capability** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.model.model_merging@1`
- `cap.t05.model.model_merging.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.knowledge.knowledge_editing@1` | use the in-file conservative substitute for `knowledge_editing` (documented, slower, lower quality) and set `degraded['knowledge_editing']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t02.gemm.gemm_grouped@1` | use the in-file conservative substitute for `gemm_grouped` (documented, slower, lower quality) and set `degraded['gemm_grouped']='local'` |
| `cap.t03.ir.ir_printer@1` | use the in-file conservative substitute for `ir_printer` (documented, slower, lower quality) and set `degraded['ir_printer']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - task-vector arithmetic with interference resolution | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - permutation alignment before merging | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - merge-quality prediction and layer-wise weighting | 520 | Third required mechanism. |
| 6 | Core implementation D - measured retention of each specialist's capability | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0227_model_merging.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.model.model_merging@1`.
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

### P0228 · `distillation_arch` — Distillation Architecture & Objectives

| field | value |
|---|---|
| part id | `P0228` (28/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0228_distillation_arch.py` |
| module path | `hyperion.t05.core_model.distillation_arch` |
| capability published | `cap.t05.distillation.distillation_arch@1` |
| determinism class | `pure` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0228_distillation_arch.txt`](prompts/P0228_distillation_arch.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0228-distillation-arch) |

**Mission.** Transfers Ω-core quality into the fast paths (enables S1 and S4).

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **logit/feature/attention-map distillation with matched tokenisation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **on-policy distillation from the core's own search traces**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **capacity-gap handling with intermediate teachers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **quality-retention measurement per size tier** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.distillation.distillation_arch@1`
- `cap.t05.distillation.distillation_arch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.model.model_merging@1` | use the in-file conservative substitute for `model_merging` (documented, slower, lower quality) and set `degraded['model_merging']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t02.conv.conv_depthwise@1` | use the in-file conservative substitute for `conv_depthwise` (documented, slower, lower quality) and set `degraded['conv_depthwise']='local'` |
| `cap.t03.memory.memory_planner@1` | use the in-file conservative substitute for `memory_planner` (documented, slower, lower quality) and set `degraded['memory_planner']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - logit/feature/attention-map distillation with matched tokenisati | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - on-policy distillation from the core's own search traces | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - capacity-gap handling with intermediate teachers | 520 | Third required mechanism. |
| 6 | Core implementation D - quality-retention measurement per size tier | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0228_distillation_arch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.distillation.distillation_arch@1`.
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

### P0229 · `weight_sharing` — Weight Sharing & Parameter Efficiency

| field | value |
|---|---|
| part id | `P0229` (29/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0229_weight_sharing.py` |
| module path | `hyperion.t05.core_model.weight_sharing` |
| capability published | `cap.t05.weight.weight_sharing@1` |
| determinism class | `pure` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0229_weight_sharing.txt`](prompts/P0229_weight_sharing.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0229-weight-sharing) |

**Mission.** More capability per byte of memory.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **cross-layer sharing schemes with per-layer modulation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **low-rank and structured factorisation with rank selection** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **hypernetwork-generated weights for rare paths** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **quality-per-parameter frontier measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.weight.weight_sharing@1`
- `cap.t05.weight.weight_sharing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.distillation.distillation_arch@1` | use the in-file conservative substitute for `distillation_arch` (documented, slower, lower quality) and set `degraded['distillation_arch']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t02.rope.rope_embed@1` | use the in-file conservative substitute for `rope_embed` (documented, slower, lower quality) and set `degraded['rope_embed']='local'` |
| `cap.t03.cost.cost_model_learned@1` | use the in-file conservative substitute for `cost_model_learned` (documented, slower, lower quality) and set `degraded['cost_model_learned']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cross-layer sharing schemes with per-layer modulation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - low-rank and structured factorisation with rank selection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hypernetwork-generated weights for rare paths | 520 | Third required mechanism. |
| 6 | Core implementation D - quality-per-parameter frontier measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0229_weight_sharing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.weight.weight_sharing@1`.
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

### P0230 · `init_scaling_laws` — Initialisation & Scaling Law Framework

| field | value |
|---|---|
| part id | `P0230` (30/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0230_init_scaling_laws.py` |
| module path | `hyperion.t05.core_model.init_scaling_laws` |
| capability published | `cap.t05.init.init_scaling_laws@1` |
| determinism class | `pure` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0230_init_scaling_laws.txt`](prompts/P0230_init_scaling_laws.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0230-init-scaling-laws) |

**Mission.** Predicts, before training, what a configuration will achieve.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **muP-style parameterisation for hyperparameter transfer across scale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **compute-optimal allocation including sparsity and data repetition** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **loss-prediction fits with confidence intervals** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **prediction accuracy validated on held-out scales**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.init.init_scaling_laws@1`
- `cap.t05.init.init_scaling_laws.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.weight.weight_sharing@1` | use the in-file conservative substitute for `weight_sharing` (documented, slower, lower quality) and set `degraded['weight_sharing']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t02.mem.mem_pool_device@1` | use the in-file conservative substitute for `mem_pool_device` (documented, slower, lower quality) and set `degraded['mem_pool_device']='local'` |
| `cap.t03.dynamic.dynamic_shapes@1` | use the in-file conservative substitute for `dynamic_shapes` (documented, slower, lower quality) and set `degraded['dynamic_shapes']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - muP-style parameterisation for hyperparameter transfer across sc | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compute-optimal allocation including sparsity and data repetitio | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - loss-prediction fits with confidence intervals | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction accuracy validated on held-out scales | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0230_init_scaling_laws.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.init.init_scaling_laws@1`.
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

### P0231 · `architecture_search` — Architecture Search & Ablation Engine

| field | value |
|---|---|
| part id | `P0231` (31/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0231_architecture_search.py` |
| module path | `hyperion.t05.core_model.architecture_search` |
| capability published | `cap.t05.architecture.architecture_search@1` |
| determinism class | `pure` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0231_architecture_search.txt`](prompts/P0231_architecture_search.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0231-architecture-search) |

**Mission.** Systematically finds the best block design under real constraints.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **search space definition with hardware-aware constraints** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **proxy tasks and early-stopping predictors for cheap evaluation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **multi-objective selection (quality, latency, memory, energy)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **discovered-versus-baseline architecture comparison** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.architecture.architecture_search@1`
- `cap.t05.architecture.architecture_search.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.init.init_scaling_laws@1` | use the in-file conservative substitute for `init_scaling_laws` (documented, slower, lower quality) and set `degraded['init_scaling_laws']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t02.kernel.kernel_verify@1` | use the in-file conservative substitute for `kernel_verify` (documented, slower, lower quality) and set `degraded['kernel_verify']='local'` |
| `cap.t03.ir.ir_verifier@1` | use the in-file conservative substitute for `ir_verifier` (documented, slower, lower quality) and set `degraded['ir_verifier']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - search space definition with hardware-aware constraints | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - proxy tasks and early-stopping predictors for cheap evaluation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - multi-objective selection (quality, latency, memory, energy) | 520 | Third required mechanism. |
| 6 | Core implementation D - discovered-versus-baseline architecture comparison | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0231_architecture_search.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.architecture.architecture_search@1`.
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

### P0232 · `depth_width_tradeoff` — Depth/Width/Sparsity Allocation

| field | value |
|---|---|
| part id | `P0232` (32/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0232_depth_width_tradeoff.py` |
| module path | `hyperion.t05.core_model.depth_width_tradeoff` |
| capability published | `cap.t05.depth.depth_width_tradeoff@1` |
| determinism class | `pure` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0232_depth_width_tradeoff.txt`](prompts/P0232_depth_width_tradeoff.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0232-depth-width-tradeoff) |

**Mission.** Where to spend the parameter budget, decided by measurement.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **allocation sweep methodology at matched compute** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **reasoning-depth versus knowledge-capacity analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **latency implications of depth under the cascade** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **recommended configuration with supporting evidence** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.depth.depth_width_tradeoff@1`
- `cap.t05.depth.depth_width_tradeoff.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.architecture.architecture_search@1` | use the in-file conservative substitute for `architecture_search` (documented, slower, lower quality) and set `degraded['architecture_search']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t02.stream.stream_scheduler@1` | use the in-file conservative substitute for `stream_scheduler` (documented, slower, lower quality) and set `degraded['stream_scheduler']='local'` |
| `cap.t03.debug.debug_symbols@1` | use the in-file conservative substitute for `debug_symbols` (documented, slower, lower quality) and set `degraded['debug_symbols']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - allocation sweep methodology at matched compute | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reasoning-depth versus knowledge-capacity analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - latency implications of depth under the cascade | 520 | Third required mechanism. |
| 6 | Core implementation D - recommended configuration with supporting evidence | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0232_depth_width_tradeoff.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.depth.depth_width_tradeoff@1`.
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

### P0233 · `residual_stream_design` — Residual Stream Capacity & Interference

| field | value |
|---|---|
| part id | `P0233` (33/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0233_residual_stream_design.py` |
| module path | `hyperion.t05.core_model.residual_stream_design` |
| capability published | `cap.t05.residual.residual_stream_design@1` |
| determinism class | `pure` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0233_residual_stream_design.txt`](prompts/P0233_residual_stream_design.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0233-residual-stream-design) |

**Mission.** Prevents features from colliding in a heavily shared representation.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **stream-width analysis and superposition measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **feature-interference detection and mitigation via subspace allocation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **read/write pattern analysis per layer** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **interpretability-driven design recommendations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.residual.residual_stream_design@1`
- `cap.t05.residual.residual_stream_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.depth.depth_width_tradeoff@1` | use the in-file conservative substitute for `depth_width_tradeoff` (documented, slower, lower quality) and set `degraded['depth_width_tradeoff']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t02.tensor.tensor_view@1` | use the in-file conservative substitute for `tensor_view` (documented, slower, lower quality) and set `degraded['tensor_view']='local'` |
| `cap.t03.crosscompile.crosscompile@1` | use the in-file conservative substitute for `crosscompile` (documented, slower, lower quality) and set `degraded['crosscompile']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - stream-width analysis and superposition measurement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - feature-interference detection and mitigation via subspace alloc | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - read/write pattern analysis per layer | 520 | Third required mechanism. |
| 6 | Core implementation D - interpretability-driven design recommendations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0233_residual_stream_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.residual.residual_stream_design@1`.
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

### P0234 · `logit_head_design` — Output Head, Logit Shaping & Constraints

| field | value |
|---|---|
| part id | `P0234` (34/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0234_logit_head_design.py` |
| module path | `hyperion.t05.core_model.logit_head_design` |
| capability published | `cap.t05.logit.logit_head_design@1` |
| determinism class | `pure` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0234_logit_head_design.txt`](prompts/P0234_logit_head_design.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0234-logit-head-design) |

**Mission.** Correct, constrained, calibrated output distributions.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **logit soft-capping and vocabulary masking mechanics** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **grammar/schema-constrained decoding integration at the head** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **temperature/penalty semantics defined exactly** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **constraint-satisfaction guarantees with proofs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.logit.logit_head_design@1`
- `cap.t05.logit.logit_head_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.residual.residual_stream_design@1` | use the in-file conservative substitute for `residual_stream_design` (documented, slower, lower quality) and set `degraded['residual_stream_design']='local'` |
| `cap.t02.gemm.gemm_int4@1` | use the in-file conservative substitute for `gemm_int4` (documented, slower, lower quality) and set `degraded['gemm_int4']='local'` |
| `cap.t03.ir.ir_builder@1` | use the in-file conservative substitute for `ir_builder` (documented, slower, lower quality) and set `degraded['ir_builder']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - logit soft-capping and vocabulary masking mechanics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - grammar/schema-constrained decoding integration at the head | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - temperature/penalty semantics defined exactly | 520 | Third required mechanism. |
| 6 | Core implementation D - constraint-satisfaction guarantees with proofs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0234_logit_head_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.logit.logit_head_design@1`.
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

### P0235 · `multimodal_fusion_arch` — Multimodal Fusion Architecture

| field | value |
|---|---|
| part id | `P0235` (35/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0235_multimodal_fusion_arch.py` |
| module path | `hyperion.t05.core_model.multimodal_fusion_arch` |
| capability published | `cap.t05.multimodal.multimodal_fusion_arch@1` |
| determinism class | `pure` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0235_multimodal_fusion_arch.txt`](prompts/P0235_multimodal_fusion_arch.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0235-multimodal-fusion-arch) |

**Mission.** One backbone, many senses, no modality tax.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **early/mid/late fusion comparison with cross-attention adapters** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **modality-specific tokenisation into a shared latent space** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **modality dropout and robustness to missing inputs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **cross-modal transfer measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.multimodal.multimodal_fusion_arch@1`
- `cap.t05.multimodal.multimodal_fusion_arch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.logit.logit_head_design@1` | use the in-file conservative substitute for `logit_head_design` (documented, slower, lower quality) and set `degraded['logit_head_design']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t02.ssm.ssm_scan@1` | use the in-file conservative substitute for `ssm_scan` (documented, slower, lower quality) and set `degraded['ssm_scan']='local'` |
| `cap.t03.layout.layout_assignment@1` | use the in-file conservative substitute for `layout_assignment` (documented, slower, lower quality) and set `degraded['layout_assignment']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - early/mid/late fusion comparison with cross-attention adapters | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - modality-specific tokenisation into a shared latent space | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - modality dropout and robustness to missing inputs | 520 | Third required mechanism. |
| 6 | Core implementation D - cross-modal transfer measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0235_multimodal_fusion_arch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.multimodal.multimodal_fusion_arch@1`.
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

### P0236 · `action_head` — Action & Tool-Call Head

| field | value |
|---|---|
| part id | `P0236` (36/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0236_action_head.py` |
| module path | `hyperion.t05.core_model.action_head` |
| capability published | `cap.t05.action.action_head@1` |
| determinism class | `pure` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0236_action_head.txt`](prompts/P0236_action_head.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0236-action-head) |

**Mission.** Generates structured actions with the same rigor as text.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **typed action schema decoding with validity guarantees** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **argument grounding against live environment state**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **action-confidence estimation feeding the safety gate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **action validity rate measurement on agent benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.action.action_head@1`
- `cap.t05.action.action_head.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.multimodal.multimodal_fusion_arch@1` | use the in-file conservative substitute for `multimodal_fusion_arch` (documented, slower, lower quality) and set `degraded['multimodal_fusion_arch']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t02.kv.kv_cache_kernels@1` | use the in-file conservative substitute for `kv_cache_kernels` (documented, slower, lower quality) and set `degraded['kv_cache_kernels']='local'` |
| `cap.t03.autotuner.autotuner_core@1` | use the in-file conservative substitute for `autotuner_core` (documented, slower, lower quality) and set `degraded['autotuner_core']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - typed action schema decoding with validity guarantees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - argument grounding against live environment state | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - action-confidence estimation feeding the safety gate | 520 | Third required mechanism. |
| 6 | Core implementation D - action validity rate measurement on agent benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0236_action_head.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.action.action_head@1`.
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

### P0237 · `memory_attention_bridge` — Memory Retrieval Attention Bridge

| field | value |
|---|---|
| part id | `P0237` (37/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0237_memory_attention_bridge.py` |
| module path | `hyperion.t05.core_model.memory_attention_bridge` |
| capability published | `cap.t05.memory.memory_attention_bridge@1` |
| determinism class | `pure` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0237_memory_attention_bridge.txt`](prompts/P0237_memory_attention_bridge.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0237-memory-attention-bridge) |

**Mission.** How the model reads its own long-term memory mid-generation.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **retrieval-in-the-loop attention with query reformulation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **relevance scoring and evidence-attribution tracking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **latency budget for in-loop retrieval** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured accuracy gain on knowledge-intensive tasks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.memory.memory_attention_bridge@1`
- `cap.t05.memory.memory_attention_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.action.action_head@1` | use the in-file conservative substitute for `action_head` (documented, slower, lower quality) and set `degraded['action_head']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t02.graph.graph_capture@1` | use the in-file conservative substitute for `graph_capture` (documented, slower, lower quality) and set `degraded['graph_capture']='local'` |
| `cap.t03.graph.graph_partition_device@1` | use the in-file conservative substitute for `graph_partition_device` (documented, slower, lower quality) and set `degraded['graph_partition_device']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - retrieval-in-the-loop attention with query reformulation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - relevance scoring and evidence-attribution tracking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - latency budget for in-loop retrieval | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy gain on knowledge-intensive tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0237_memory_attention_bridge.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.memory.memory_attention_bridge@1`.
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

### P0238 · `speculative_arch_hooks` — Architecture Hooks for Speculative Decoding

| field | value |
|---|---|
| part id | `P0238` (38/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0238_speculative_arch_hooks.py` |
| module path | `hyperion.t05.core_model.speculative_arch_hooks` |
| capability published | `cap.t05.speculative.speculative_arch_hooks@1` |
| determinism class | `pure` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0238_speculative_arch_hooks.txt`](prompts/P0238_speculative_arch_hooks.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0238-speculative-arch-hooks) |

**Mission.** Makes the core cheap to verify in parallel (foundation of S1).

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **tree-attention-compatible KV layout and mask construction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **batched multi-branch verification in one forward pass** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **acceptance-rate instrumentation per branch depth** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **verified equivalence with sequential decoding**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.speculative.speculative_arch_hooks@1`
- `cap.t05.speculative.speculative_arch_hooks.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.memory.memory_attention_bridge@1` | use the in-file conservative substitute for `memory_attention_bridge` (documented, slower, lower quality) and set `degraded['memory_attention_bridge']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t02.kernel.kernel_registry@1` | use the in-file conservative substitute for `kernel_registry` (documented, slower, lower quality) and set `degraded['kernel_registry']='local'` |
| `cap.t03.effect.effect_system@1` | use the in-file conservative substitute for `effect_system` (documented, slower, lower quality) and set `degraded['effect_system']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tree-attention-compatible KV layout and mask construction | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - batched multi-branch verification in one forward pass | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - acceptance-rate instrumentation per branch depth | 520 | Third required mechanism. |
| 6 | Core implementation D - verified equivalence with sequential decoding | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0238_speculative_arch_hooks.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.speculative.speculative_arch_hooks@1`.
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

### P0239 · `sparse_upcycling` — Sparse Upcycling & Expert Initialisation

| field | value |
|---|---|
| part id | `P0239` (39/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0239_sparse_upcycling.py` |
| module path | `hyperion.t05.core_model.sparse_upcycling` |
| capability published | `cap.t05.sparse.sparse_upcycling@1` |
| determinism class | `pure` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0239_sparse_upcycling.txt`](prompts/P0239_sparse_upcycling.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0239-sparse-upcycling) |

**Mission.** Turns dense checkpoints into sparse ones without quality loss.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **expert initialisation from dense weights with diversity injection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **router warmup schedule preventing collapse** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **quality trajectory versus training-from-scratch**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **compute saved measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.sparse.sparse_upcycling@1`
- `cap.t05.sparse.sparse_upcycling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.speculative.speculative_arch_hooks@1` | use the in-file conservative substitute for `speculative_arch_hooks` (documented, slower, lower quality) and set `degraded['speculative_arch_hooks']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t02.p2p.p2p_transfer@1` | use the in-file conservative substitute for `p2p_transfer` (documented, slower, lower quality) and set `degraded['p2p_transfer']='local'` |
| `cap.t03.bytecode.bytecode_vm@1` | use the in-file conservative substitute for `bytecode_vm` (documented, slower, lower quality) and set `degraded['bytecode_vm']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - expert initialisation from dense weights with diversity injectio | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - router warmup schedule preventing collapse | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality trajectory versus training-from-scratch | 520 | Third required mechanism. |
| 6 | Core implementation D - compute saved measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0239_sparse_upcycling.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.sparse.sparse_upcycling@1`.
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

### P0240 · `model_surgery` — Model Surgery: Pruning, Grafting, Extension

| field | value |
|---|---|
| part id | `P0240` (40/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0240_model_surgery.py` |
| module path | `hyperion.t05.core_model.model_surgery` |
| capability published | `cap.t05.model.model_surgery@1` |
| determinism class | `pure` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0240_model_surgery.txt`](prompts/P0240_model_surgery.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0240-model-surgery) |

**Mission.** Safely modifies a trained model's structure.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **structured pruning with sensitivity-guided selection and healing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **layer/expert grafting between compatible checkpoints**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **context-length and vocabulary extension procedures** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **post-surgery quality verification protocol** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.model.model_surgery@1`
- `cap.t05.model.model_surgery.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.sparse.sparse_upcycling@1` | use the in-file conservative substitute for `sparse_upcycling` (documented, slower, lower quality) and set `degraded['sparse_upcycling']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t02.mask.mask_engine@1` | use the in-file conservative substitute for `mask_engine` (documented, slower, lower quality) and set `degraded['mask_engine']='local'` |
| `cap.t03.incremental.incremental_build@1` | use the in-file conservative substitute for `incremental_build` (documented, slower, lower quality) and set `degraded['incremental_build']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structured pruning with sensitivity-guided selection and healing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - layer/expert grafting between compatible checkpoints | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - context-length and vocabulary extension procedures | 520 | Third required mechanism. |
| 6 | Core implementation D - post-surgery quality verification protocol | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0240_model_surgery.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.model.model_surgery@1`.
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

### P0241 · `numerical_arch_stability` — Architectural Numerical Stability

| field | value |
|---|---|
| part id | `P0241` (41/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0241_numerical_arch_stability.py` |
| module path | `hyperion.t05.core_model.numerical_arch_stability` |
| capability published | `cap.t05.numerical.numerical_arch_stability@1` |
| determinism class | `pure` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0241_numerical_arch_stability.txt`](prompts/P0241_numerical_arch_stability.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0241-numerical-arch-stability) |

**Mission.** Design-level defences against divergence and low-precision failure.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **activation-range budgeting per layer with measured margins**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **attention-logit and gradient-explosion prevention mechanisms** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **low-precision-safe formulation of every block** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **extreme-input and long-run stability tests** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.numerical.numerical_arch_stability@1`
- `cap.t05.numerical.numerical_arch_stability.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.model.model_surgery@1` | use the in-file conservative substitute for `model_surgery` (documented, slower, lower quality) and set `degraded['model_surgery']='local'` |
| `cap.t02.gemm.gemm_fp8@1` | use the in-file conservative substitute for `gemm_fp8` (documented, slower, lower quality) and set `degraded['gemm_fp8']='local'` |
| `cap.t03.ir.ir_core@1` | use the in-file conservative substitute for `ir_core` (documented, slower, lower quality) and set `degraded['ir_core']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - activation-range budgeting per layer with measured margins | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - attention-logit and gradient-explosion prevention mechanisms | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - low-precision-safe formulation of every block | 520 | Third required mechanism. |
| 6 | Core implementation D - extreme-input and long-run stability tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0241_numerical_arch_stability.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.numerical.numerical_arch_stability@1`.
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

### P0242 · `context_packing` — Context Composition & Packing Strategy

| field | value |
|---|---|
| part id | `P0242` (42/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0242_context_packing.py` |
| module path | `hyperion.t05.core_model.context_packing` |
| capability published | `cap.t05.context.context_packing@1` |
| determinism class | `pure` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0242_context_packing.txt`](prompts/P0242_context_packing.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0242-context-packing) |

**Mission.** What actually goes into the window, and in what order.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **document packing with attention isolation and position resets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **priority-based context assembly under a token budget** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **lost-in-the-middle mitigation via ordering and restatement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured accuracy versus naive concatenation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.context.context_packing@1`
- `cap.t05.context.context_packing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.numerical.numerical_arch_stability@1` | use the in-file conservative substitute for `numerical_arch_stability` (documented, slower, lower quality) and set `degraded['numerical_arch_stability']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t02.attn.attn_linear@1` | use the in-file conservative substitute for `attn_linear` (documented, slower, lower quality) and set `degraded['attn_linear']='local'` |
| `cap.t03.fusion.fusion_pass@1` | use the in-file conservative substitute for `fusion_pass` (documented, slower, lower quality) and set `degraded['fusion_pass']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - document packing with attention isolation and position resets | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - priority-based context assembly under a token budget | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - lost-in-the-middle mitigation via ordering and restatement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy versus naive concatenation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0242_context_packing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.context.context_packing@1`.
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

### P0243 · `prompt_representation` — Internal Prompt & Role Representation

| field | value |
|---|---|
| part id | `P0243` (43/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0243_prompt_representation.py` |
| module path | `hyperion.t05.core_model.prompt_representation` |
| capability published | `cap.t05.prompt.prompt_representation@1` |
| determinism class | `pure` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0243_prompt_representation.txt`](prompts/P0243_prompt_representation.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0243-prompt-representation) |

**Mission.** Unambiguous instruction hierarchy encoded in the architecture.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **role/channel embeddings for system, developer, user, tool and thought** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **instruction-priority encoding resistant to injection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **hierarchy-violation detection head**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **injection-resistance benchmark results** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.prompt.prompt_representation@1`
- `cap.t05.prompt.prompt_representation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.context.context_packing@1` | use the in-file conservative substitute for `context_packing` (documented, slower, lower quality) and set `degraded['context_packing']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t02.quantize.quantize_kernels@1` | use the in-file conservative substitute for `quantize_kernels` (documented, slower, lower quality) and set `degraded['quantize_kernels']='local'` |
| `cap.t03.collective.collective_insertion@1` | use the in-file conservative substitute for `collective_insertion` (documented, slower, lower quality) and set `degraded['collective_insertion']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - role/channel embeddings for system, developer, user, tool and th | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - instruction-priority encoding resistant to injection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hierarchy-violation detection head | 520 | Third required mechanism. |
| 6 | Core implementation D - injection-resistance benchmark results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0243_prompt_representation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.prompt.prompt_representation@1`.
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

### P0244 · `thought_representation` — Latent Thought Channel

| field | value |
|---|---|
| part id | `P0244` (44/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0244_thought_representation.py` |
| module path | `hyperion.t05.core_model.thought_representation` |
| capability published | `cap.t05.thought.thought_representation@1` |
| determinism class | `pure` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0244_thought_representation.txt`](prompts/P0244_thought_representation.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0244-thought-representation) |

**Mission.** Separates deliberation from output, with controllable visibility.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **dedicated thought channel with its own budget and decoding policy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **thought-to-answer distillation reducing visible token count**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **leakage prevention between channels** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured accuracy gain per thought token spent** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.thought.thought_representation@1`
- `cap.t05.thought.thought_representation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.prompt.prompt_representation@1` | use the in-file conservative substitute for `prompt_representation` (documented, slower, lower quality) and set `degraded['prompt_representation']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t02.fused.fused_decode_step@1` | use the in-file conservative substitute for `fused_decode_step` (documented, slower, lower quality) and set `degraded['fused_decode_step']='local'` |
| `cap.t03.kernel.kernel_selection@1` | use the in-file conservative substitute for `kernel_selection` (documented, slower, lower quality) and set `degraded['kernel_selection']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dedicated thought channel with its own budget and decoding polic | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - thought-to-answer distillation reducing visible token count | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - leakage prevention between channels | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy gain per thought token spent | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0244_thought_representation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.thought.thought_representation@1`.
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

### P0245 · `expert_specialisation` — Expert Specialisation Analysis & Design

| field | value |
|---|---|
| part id | `P0245` (45/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0245_expert_specialisation.py` |
| module path | `hyperion.t05.core_model.expert_specialisation` |
| capability published | `cap.t05.expert.expert_specialisation@1` |
| determinism class | `pure` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0245_expert_specialisation.txt`](prompts/P0245_expert_specialisation.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0245-expert-specialisation) |

**Mission.** Makes 512 experts genuinely different from each other.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **specialisation metrics (domain, syntax, modality) with clustering**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **diversity-promoting objectives and initialisation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **redundancy detection and expert retirement criteria** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **specialisation report over real traffic** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.expert.expert_specialisation@1`
- `cap.t05.expert.expert_specialisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.thought.thought_representation@1` | use the in-file conservative substitute for `thought_representation` (documented, slower, lower quality) and set `degraded['thought_representation']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t02.bf16.bf16_stability@1` | use the in-file conservative substitute for `bf16_stability` (documented, slower, lower quality) and set `degraded['bf16_stability']='local'` |
| `cap.t03.dead.dead_code_dce@1` | use the in-file conservative substitute for `dead_code_dce` (documented, slower, lower quality) and set `degraded['dead_code_dce']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - specialisation metrics (domain, syntax, modality) with clusterin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - diversity-promoting objectives and initialisation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - redundancy detection and expert retirement criteria | 520 | Third required mechanism. |
| 6 | Core implementation D - specialisation report over real traffic | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0245_expert_specialisation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.expert.expert_specialisation@1`.
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

### P0246 · `model_config_schema` — Model Configuration Schema & Validation

| field | value |
|---|---|
| part id | `P0246` (46/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0246_model_config_schema.py` |
| module path | `hyperion.t05.core_model.model_config_schema` |
| capability published | `cap.t05.model.model_config_schema@1` |
| determinism class | `pure` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0246_model_config_schema.txt`](prompts/P0246_model_config_schema.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0246-model-config-schema) |

**Mission.** One validated description of every model variant.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **exhaustive config schema with constraint checking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **derived-quantity computation (parameters, FLOPs, memory, latency)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **invalid-configuration rejection with explanations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **config-to-artifact provenance binding**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.model.model_config_schema@1`
- `cap.t05.model.model_config_schema.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.expert.expert_specialisation@1` | use the in-file conservative substitute for `expert_specialisation` (documented, slower, lower quality) and set `degraded['expert_specialisation']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t02.collective.collective_local@1` | use the in-file conservative substitute for `collective_local` (documented, slower, lower quality) and set `degraded['collective_local']='local'` |
| `cap.t03.ir.ir_serialization@1` | use the in-file conservative substitute for `ir_serialization` (documented, slower, lower quality) and set `degraded['ir_serialization']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - exhaustive config schema with constraint checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - derived-quantity computation (parameters, FLOPs, memory, latency | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - invalid-configuration rejection with explanations | 520 | Third required mechanism. |
| 6 | Core implementation D - config-to-artifact provenance binding | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0246_model_config_schema.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.model.model_config_schema@1`.
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

### P0247 · `reference_forward` — Reference Forward Pass Implementation

| field | value |
|---|---|
| part id | `P0247` (47/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0247_reference_forward.py` |
| module path | `hyperion.t05.core_model.reference_forward` |
| capability published | `cap.t05.reference.reference_forward@1` |
| determinism class | `pure` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0247_reference_forward.txt`](prompts/P0247_reference_forward.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0247-reference-forward) |

**Mission.** Slow, transparent, obviously-correct model execution as the oracle.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **pure implementation with no fused kernels and explicit intermediates** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **intermediate-value dump format for debugging** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **bit-exactness policy versus optimised paths**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **cross-checked against optimised execution on a fixed corpus** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.reference.reference_forward@1`
- `cap.t05.reference.reference_forward.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.model.model_config_schema@1` | use the in-file conservative substitute for `model_config_schema` (documented, slower, lower quality) and set `degraded['model_config_schema']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t02.embedding.embedding_kernels@1` | use the in-file conservative substitute for `embedding_kernels` (documented, slower, lower quality) and set `degraded['embedding_kernels']='local'` |
| `cap.t03.linker.linker_omega@1` | use the in-file conservative substitute for `linker_omega` (documented, slower, lower quality) and set `degraded['linker_omega']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pure implementation with no fused kernels and explicit intermedi | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - intermediate-value dump format for debugging | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - bit-exactness policy versus optimised paths | 520 | Third required mechanism. |
| 6 | Core implementation D - cross-checked against optimised execution on a fixed corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0247_reference_forward.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.reference.reference_forward@1`.
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

### P0248 · `arch_ablation_suite` — Architecture Ablation & Evidence Suite

| field | value |
|---|---|
| part id | `P0248` (48/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0248_arch_ablation_suite.py` |
| module path | `hyperion.t05.core_model.arch_ablation_suite` |
| capability published | `cap.t05.arch.arch_ablation_suite@1` |
| determinism class | `pure` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0248_arch_ablation_suite.txt`](prompts/P0248_arch_ablation_suite.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0248-arch-ablation-suite) |

**Mission.** Every architectural claim backed by a reproducible experiment.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **ablation matrix over all major design choices** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GPQA Diamond**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **matched-compute experimental protocol with seeds and variance**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **statistical analysis with confidence intervals** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **evidence report for each design decision** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t05.arch.arch_ablation_suite@1`
- `cap.t05.arch.arch_ablation_suite.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.reference.reference_forward@1` | use the in-file conservative substitute for `reference_forward` (documented, slower, lower quality) and set `degraded['reference_forward']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t02.kernel.kernel_docs_spec@1` | use the in-file conservative substitute for `kernel_docs_spec` (documented, slower, lower quality) and set `degraded['kernel_docs_spec']='local'` |
| `cap.t03.build.build_provenance@1` | use the in-file conservative substitute for `build_provenance` (documented, slower, lower quality) and set `degraded['build_provenance']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - ablation matrix over all major design choices | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - matched-compute experimental protocol with seeds and variance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - statistical analysis with confidence intervals | 520 | Third required mechanism. |
| 6 | Core implementation D - evidence report for each design decision | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0248_arch_ablation_suite.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.arch.arch_ablation_suite@1`.
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

### P0249 · `capacity_probes` — Capability Probes & Representation Diagnostics

| field | value |
|---|---|
| part id | `P0249` (49/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0249_capacity_probes.py` |
| module path | `hyperion.t05.core_model.capacity_probes` |
| capability published | `cap.t05.capacity.capacity_probes@1` |
| determinism class | `pure` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0249_capacity_probes.txt`](prompts/P0249_capacity_probes.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0249-capacity-probes) |

**Mission.** Measures what the network actually represents, not just its loss.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **linear/nonlinear probing suite over layers and features**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **circuit-level capability localisation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **emergence tracking across training checkpoints** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **probe-to-benchmark correlation analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t05.capacity.capacity_probes@1`
- `cap.t05.capacity.capacity_probes.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.arch.arch_ablation_suite@1` | use the in-file conservative substitute for `arch_ablation_suite` (documented, slower, lower quality) and set `degraded['arch_ablation_suite']='local'` |
| `cap.t02.attn.attn_paged_decode@1` | use the in-file conservative substitute for `attn_paged_decode` (documented, slower, lower quality) and set `degraded['attn_paged_decode']='local'` |
| `cap.t03.algebraic.algebraic_rewrite@1` | use the in-file conservative substitute for `algebraic_rewrite` (documented, slower, lower quality) and set `degraded['algebraic_rewrite']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - linear/nonlinear probing suite over layers and features | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - circuit-level capability localisation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - emergence tracking across training checkpoints | 520 | Third required mechanism. |
| 6 | Core implementation D - probe-to-benchmark correlation analysis | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0249_capacity_probes.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.capacity.capacity_probes@1`.
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

### P0250 · `arch_spec_doc` — Architecture Specification Document Generator

| field | value |
|---|---|
| part id | `P0250` (50/50 of T05) |
| tier | `T05` — Ω-Core Model Architecture |
| language | Python 3.13 |
| file to produce | `parts/t05_core_model/P0250_arch_spec_doc.py` |
| module path | `hyperion.t05.core_model.arch_spec_doc` |
| capability published | `cap.t05.arch.arch_spec_doc@1` |
| determinism class | `pure` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, MMMU |
| worker prompt | [`prompts/P0250_arch_spec_doc.txt`](prompts/P0250_arch_spec_doc.txt) · [inline](docs/PROMPTS_T05.md#prompt-p0250-arch-spec-doc) |

**Mission.** The authoritative, auto-generated description of the Ω-core.

**Tier context.** The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.

**Mandate — all four items are required; none is optional.**

1. Implement **spec extraction from config and code with consistency checking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GPQA Diamond** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **diagram and tensor-shape-table generation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **parameter/FLOP accounting per component** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **spec-vs-implementation drift detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t05.arch.arch_spec_doc@1`
- `cap.t05.arch.arch_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t05.capacity.capacity_probes@1` | use the in-file conservative substitute for `capacity_probes` (documented, slower, lower quality) and set `degraded['capacity_probes']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t02.topk.topk_sort@1` | use the in-file conservative substitute for `topk_sort` (documented, slower, lower quality) and set `degraded['topk_sort']='local'` |
| `cap.t03.pipeline.pipeline_planner@1` | use the in-file conservative substitute for `pipeline_planner` (documented, slower, lower quality) and set `degraded['pipeline_planner']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - spec extraction from config and code with consistency checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - diagram and tensor-shape-table generation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - parameter/FLOP accounting per component | 520 | Third required mechanism. |
| 6 | Core implementation D - spec-vs-implementation drift detection | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t05_core_model/P0250_arch_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t05.arch.arch_spec_doc@1`.
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
